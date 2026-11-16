import os
from pathlib import Path
import subprocess
import sys
import textwrap
import unittest


class GuiShutdownTests(unittest.TestCase):
    def test_restart_preserves_selections_clears_live_ui_and_exits_cleanly(self):
        # Use a separate process so native Qt destruction is part of the check.
        script = textwrap.dedent('''
            import inspect
            import numpy as np
            from unittest.mock import Mock, patch
            from PySide6.QtWidgets import QApplication
            from PySide6.QtCore import Qt
            from PySide6.QtTest import QTest
            from GUI.mainWindow import MainWindow
            from modules.AffectPipeline import AffectPipeline
            from GUI.rightClickWindow import RightClickWindow
            import modules.QueueSystem as qs

            app = QApplication([])
            options = {
                name: False
                for name in inspect.signature(AffectPipeline).parameters
                if name.startswith("enable_")
            }
            created = []
            sockets = []

            def factory():
                resource = Mock()
                with patch("modules.AffectPipeline.socket.socket", return_value=resource):
                    pipeline = AffectPipeline(**options)
                created.append(pipeline)
                sockets.append(resource)
                return pipeline

            with patch("GUI.mainWindow.create_pipeline", side_effect=factory), \
                    patch("GUI.mainWindow.QMessageBox.warning") as warning:
                window = MainWindow()
                buttons = window.buttons_widget
                assert all(container.stream.isHidden() for container in window._preview_containers)
                buttons.Camera.click()
                buttons.Video.button.click()
                buttons.FaceMesh.button.click()
                assert not buttons.FaceMesh.stream.isHidden()
                buttons.BodyTracking.button.click()
                buttons.Micro.click()
                buttons.Audio.button.click()
                buttons.Transcript.button.click()
                buttons.Pleasure_3.click()
                buttons.FUSION_1.click()
                window.udp_button.click()
                window.kafka_button.click()
                selections = RightClickWindow.PARAMETERS.copy()
                assert selections["enable_fusion"]
                assert selections["enable_face_mesh_loop"]
                assert buttons.FaceMesh.stream.timer.isActive()
                assert buttons.Video.stream.timer.isActive()
                assert buttons.FaceMesh.button.styleSheet() == buttons.active_style
                assert window.udp_button.styleSheet() == buttons.active_style
                assert buttons.isEnabled()
                window.run_button.click()
                first = window.pipeline
                assert window.run_button.text() == "Stop"
                assert all(button.timer.isActive() for button in window._status_buttons)
                assert buttons.FaceMesh.stream.timer.isActive()
                assert buttons.FaceMesh.button.styleSheet() == buttons.active_style
                assert window.udp_button.styleSheet() == buttons.active_style
                assert buttons.isEnabled()
                assert not buttons.FaceMesh.button.isEnabled()
                assert not buttons.ANALYSIS.isEnabled()
                for container in (buttons.Video, buttons.FaceTracking, buttons.FaceMesh, buttons.Skeleton, buttons.BodyTracking):
                    assert container.isEnabled() and container.stream.label.isEnabled()
                assert all(not button.isEnabled() for button in (window.udp_button, window.kafka_button, window.load_button, window.save_button))
                assert window.run_button.isEnabled() and window.help_button.isEnabled()
                # Neither clicks nor context menus can change configuration while running.
                buttons.FaceMesh.button.click()
                buttons.Camera.click()
                window.udp_button.click()
                with patch("GUI.custom_button.InitSettingWindow") as settings_dialog:
                    QTest.mouseClick(buttons.FaceMesh.button, Qt.MouseButton.RightButton)
                    settings_dialog.assert_not_called()
                with patch("GUI.mainWindow.QFileDialog.getOpenFileName") as load_dialog:
                    window.load_button.click()
                    load_dialog.assert_not_called()
                assert RightClickWindow.PARAMETERS == selections
                qs.VALENCE_FACE.append(0.42)
                buttons.Pleasure_3.update_float()
                assert "0.42" in buttons.Pleasure_3.text()
                for container in (buttons.Video, buttons.FaceTracking, buttons.FaceMesh, buttons.Skeleton, buttons.BodyTracking):
                    frame = np.zeros((20, 20, 3), dtype=np.uint8)
                    frame[:] = [250, 80, 30]
                    container.stream.queue.append(frame)
                    container.stream.update_image()
                    assert not container.stream.label.pixmap().isNull()
                    rendered = container.stream.label.grab().toImage()
                    colour = rendered.pixelColor(rendered.width() // 2, rendered.height() // 2)
                    assert len({colour.red(), colour.green(), colour.blue()}) > 1
                qs.TRANSCRIPT_SPEECH.append("sample speech")
                buttons.Transcript.stream.update_transcript()
                assert "sample speech" in buttons.Transcript.stream.label.text()
                buttons.Audio.stream.plot_widget.plot([1, 2, 3])
                last_images = {
                    container: container.stream.label.pixmap().toImage()
                    for container in (buttons.Video, buttons.FaceTracking, buttons.FaceMesh, buttons.Skeleton, buttons.BodyTracking)
                }
                last_transcript = buttons.Transcript.stream.label.text()
                last_audio = list(buttons.Audio.stream.plot_widget.listDataItems())
                window.run_button.click()
                assert window.pipeline is None
                assert window.run_button.text() == "Run"
                assert first._SOCKET is None and not first._workers
                assert buttons.isEnabled()
                assert all(button.isEnabled() for button in (window.udp_button, window.kafka_button, window.load_button, window.save_button))
                assert all(not button.timer.isActive() for button in window._status_buttons)
                assert all(not button.timer.isActive() for button in window.buttons_widget.float_buttons)
                assert all(not container.stream.timer.isActive() for container in window._preview_containers)
                assert RightClickWindow.PARAMETERS == selections
                for group in buttons.header_to_buttons.values():
                    for button in group:
                        expected_style = buttons.active_style if buttons.is_selected(button) else buttons.inactive_style
                        assert button.styleSheet() == expected_style
                assert window.udp_button.styleSheet() == buttons.active_style
                assert window.kafka_button.styleSheet() == buttons.active_style
                for container in (buttons.Video, buttons.FaceTracking, buttons.FaceMesh, buttons.Skeleton, buttons.BodyTracking):
                    assert not container.stream.isHidden()
                    assert container.stream.label.pixmap().toImage() == last_images[container]
                    container.stream.queue.append(np.zeros((20, 20, 3), dtype=np.uint8))
                    container.stream.update_image()
                    assert container.stream.label.pixmap().toImage() == last_images[container]
                assert not buttons.Transcript.stream.isHidden()
                assert buttons.Transcript.stream.label.text() == last_transcript
                assert not buttons.Audio.stream.isHidden()
                assert buttons.Audio.stream.plot_widget.listDataItems() == last_audio
                assert all(button.text() == button.base_text for button in buttons.float_buttons)
                buttons.Pleasure_3.update_float()
                assert buttons.Pleasure_3.text() == buttons.Pleasure_3.base_text
                # Retained selections still deselect on the first click after stopping.
                buttons.FaceMesh.button.click()
                assert not buttons.is_selected(buttons.FaceMesh.button)
                assert not buttons.FaceMesh.stream.timer.isActive()
                assert buttons.FaceMesh.stream.isHidden()
                buttons.FaceMesh.button.click()
                assert buttons.is_selected(buttons.FaceMesh.button)
                assert buttons.FaceMesh.stream.timer.isActive()
                assert not buttons.FaceMesh.stream.isHidden()
                assert buttons.FaceMesh.button.styleSheet() == buttons.active_style
                assert RightClickWindow.PARAMETERS == selections
                window.sync_buttons_with_parameters()
                assert buttons.FaceMesh.stream.timer.isActive()
                assert buttons.FaceMesh.button.styleSheet() == buttons.active_style
                warning.assert_not_called()

                failed = factory()
                failed.start = Mock(side_effect=RuntimeError("simulated startup failure"))
                with patch("GUI.mainWindow.create_pipeline", return_value=failed):
                    window.run()
                assert window.pipeline is None and failed._SOCKET is None
                assert buttons.isEnabled() and window.load_button.isEnabled()
                assert window.run_button.text() == "Run"
                assert "simulated startup failure" in str(warning.call_args)

                busy = Mock()
                busy.stop.side_effect = [RuntimeError("simulated busy worker"), None]
                window.pipeline = busy
                window.run()
                assert window.pipeline is busy and window.run_button.text() == "Stop"
                assert not buttons.FaceMesh.button.isEnabled() and not window.load_button.isEnabled()
                window.run()
                assert window.pipeline is None and window.run_button.text() == "Run"
                assert buttons.isEnabled() and window.load_button.isEnabled()

                window.run()
                second = window.pipeline
                assert second is not first
                assert buttons.FaceMesh.stream.timer.isActive()
                assert buttons.BodyTracking.stream.timer.isActive()
                assert buttons.FaceMesh.button.styleSheet() == buttons.active_style
                assert RightClickWindow.PARAMETERS == selections
                # Running locks the retained selections and previews against clicks.
                buttons.FaceMesh.button.click()
                assert buttons.is_selected(buttons.FaceMesh.button)
                assert buttons.FaceMesh.stream.timer.isActive()
                window.close()
                assert window.pipeline is None and second._SOCKET is None
                assert all(not button.timer.isActive() for button in window._status_buttons)
                for resource in sockets:
                    resource.close.assert_called_once()
                print("GUI lifecycle checks passed", flush=True)
        ''')
        result = subprocess.run(
            [sys.executable, "-c", script],
            cwd=Path(__file__).resolve().parents[1],
            env=dict(os.environ, QT_QPA_PLATFORM="offscreen", PYTHONFAULTHANDLER="1"),
            capture_output=True,
            text=True,
            timeout=20,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("GUI lifecycle checks passed", result.stdout)


if __name__ == "__main__":
    unittest.main()
