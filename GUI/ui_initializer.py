from GUI.circle_widget import CircleWidget
from GUI.rounded_frame import RoundedFrame
from GUI.horizontal_line_widget import HorLineWidget
from GUI.vertical_line_widget import VerLineWidget
from PyQt6.QtWidgets import QPushButton
from GUI.Consoleoutput import ConsoleOutput
from GUI.MyButton import MyButton

def initialize_ui(window):
    # Create the containers
        window.createTitleContainer()
        window.createBodyContainer()

        # Create the CircleWidget and add it to the bodyContainer
        window.circle8_1 = CircleWidget()  # Create a CircleWidget
        window.circle8_1.setFixedSize(130, 130)  # Set the size of the CircleWidget
        window.circle8_1.radius = min(window.circle8_1.width(), window.circle8_1.height()) // 2
        window.circle8_1.setParent(window.bodyContainer)  # Add the CircleWidget to the bodyContainer

        window.circle8_2 = CircleWidget()  # Create a CircleWidget
        window.circle8_2.setFixedSize(130, 130)
        window.circle8_2.radius = min(window.circle8_2.width(), window.circle8_2.height()) // 2  # Update the radius
        window.circle8_2.setParent(window.bodyContainer)

        window.circle8_3 = CircleWidget()  # Create a CircleWidget
        window.circle8_3.setFixedSize(130, 130)
        window.circle8_3.radius = min(window.circle8_3.width(), window.circle8_3.height()) // 2  # Update the radius
        window.circle8_3.setParent(window.bodyContainer)

        window.rounded8_1 = RoundedFrame("[P]leasure", "#d9d9d9", "black", "25", True)
        window.rounded8_1.setFixedSize(int(window.screen_width *0.08) ,int(window.screen_height * 0.05))
        window.rounded8_1.setParent(window.bodyContainer)

        window.rounded8_2 = RoundedFrame("[A]rousal", "#d9d9d9", "black", "25", True)
        window.rounded8_2.setFixedSize(int(window.screen_width *0.08) ,int(window.screen_height * 0.05))
        window.rounded8_2.setParent(window.bodyContainer)

        window.rounded8_3 = RoundedFrame("[D]ominance", "#d9d9d9", "black", "25", True)
        window.rounded8_3.setFixedSize(int(window.screen_width *0.08) ,int(window.screen_height * 0.05))
        window.rounded8_3.setParent(window.bodyContainer)

        window.circle7outer = CircleWidget("#d9d9d9")  # Create a CircleWidget
        window.circle7outer.setFixedSize(150, 150)
        window.circle7outer.radius = min(window.circle7outer.width(), window.circle7outer.height()) // 2  # Update the radius
        window.circle7outer.setParent(window.bodyContainer)

        window.circle7inner = CircleWidget("#f2f2f2")  # Create a CircleWidget
        window.circle7inner.setFixedSize(130, 130)
        window.circle7inner.setParent(window.bodyContainer)

        window.rounded7 = RoundedFrame("FUSION", "#d9d9d9", "black", "25", True)
        window.rounded7.setFixedSize(int(window.screen_width *0.1) ,int(window.screen_height * 0.05))
        window.rounded7.setParent(window.bodyContainer)

        #Create Widgets for Column 6

        window.circle6_1 = CircleWidget()  # Create a CircleWidget
        window.circle6_1.setFixedSize(80,80)
        window.circle6_1.radius = min(window.circle6_1.width(), window.circle6_1.height()) // 2
        window.circle6_1.setParent(window.bodyContainer)

        window.circle6_2 = CircleWidget()  # Create a CircleWidget
        window.circle6_2.setFixedSize(80,80)
        window.circle6_2.radius = min(window.circle6_2.width(), window.circle6_2.height()) // 2
        window.circle6_2.setParent(window.bodyContainer)

        window.circle6_3 = CircleWidget()  # Create a CircleWidget
        window.circle6_3.setFixedSize(80,80)
        window.circle6_3.radius = min(window.circle6_3.width(), window.circle6_3.height()) // 2
        window.circle6_3.setParent(window.bodyContainer)

        window.circle6_4 = CircleWidget()  # Create a CircleWidget
        window.circle6_4.setFixedSize(80,80)  # Set the size of the CircleWidget
        window.circle6_4.radius = min(window.circle6_4.width(), window.circle6_4.height()) // 2
        window.circle6_4.setParent(window.bodyContainer)  # Add the CircleWidget to the bodyContainer

        window.circle6_5 = CircleWidget()  # Create a CircleWidget
        window.circle6_5.setFixedSize(80,80)
        window.circle6_5.radius = min(window.circle6_5.width(), window.circle6_5.height()) // 2
        window.circle6_5.setParent(window.bodyContainer)

        window.circle6_6 = CircleWidget()  # Create a CircleWidget
        window.circle6_6.setFixedSize(80,80)
        window.circle6_6.radius = min(window.circle6_6.width(), window.circle6_6.height()) // 2
        window.circle6_6.setParent(window.bodyContainer)

        window.circle6_7 = CircleWidget()  # Create a CircleWidget
        window.circle6_7.setFixedSize(80,80)
        window.circle6_7.radius = min(window.circle6_7.width(), window.circle6_7.height()) // 2
        window.circle6_7.setParent(window.bodyContainer)

        window.circle6_8 = CircleWidget()  # Create a CircleWidget
        window.circle6_8.setFixedSize(80,80)
        window.circle6_8.radius = min(window.circle6_8.width(), window.circle6_8.height()) // 2
        window.circle6_8.setParent(window.bodyContainer)

        window.rounded6_1 = RoundedFrame("Pleasure", "#d9d9d9", "black", "20", True)
        window.rounded6_1.setFixedSize(100 ,45)
        window.rounded6_1.setParent(window.bodyContainer)

        window.rounded6_2 = RoundedFrame("Arousal", "#d9d9d9", "black", "20", True)
        window.rounded6_2.setFixedSize(100 ,45)
        window.rounded6_2.setParent(window.bodyContainer)

        window.rounded6_3 = RoundedFrame("Dominance", "#d9d9d9", "black", "20", True)
        window.rounded6_3.setFixedSize(100 ,45)
        window.rounded6_3.setParent(window.bodyContainer)
        
        window.rounded6_4 = RoundedFrame("Pleasure", "#d9d9d9", "black", "20", True)
        window.rounded6_4.setFixedSize(100 ,45)
        window.rounded6_4.setParent(window.bodyContainer)

        window.rounded6_5 = RoundedFrame("Pleasure", "#d9d9d9", "black", "20", True)
        window.rounded6_5.setFixedSize(100 ,45)#
        window.rounded6_5.setParent(window.bodyContainer)

        window.rounded6_6 = RoundedFrame("Arousal", "#d9d9d9", "black", "20", True)
        window.rounded6_6.setFixedSize(100 ,45)
        window.rounded6_6.setParent(window.bodyContainer)

        window.rounded6_7 = RoundedFrame("Dominance", "#d9d9d9", "black", "20", True)
        window.rounded6_7.setFixedSize(100 ,45)
        window.rounded6_7.setParent(window.bodyContainer)

        window.rounded6_8 = RoundedFrame("Dominance", "#d9d9d9", "black", "20", True)
        window.rounded6_8.setFixedSize(100 ,45)
        window.rounded6_8.setParent(window.bodyContainer)

        #Create Widgets for Column 5

        window.circle5_1_outer = CircleWidget("#d9d9d9")  # Create a CircleWidget
        window.circle5_1_outer.setFixedSize(150, 150)
        window.circle5_1_outer.radius = min(window.circle5_1_outer.width(), window.circle5_1_outer.height()) // 2
        window.circle5_1_outer.setParent(window.bodyContainer)

        window.circle5_1_inner = CircleWidget("#f2f2f2", "PARA - \nLINGUISTIC", 15)  # Create a CircleWidget
        window.circle5_1_inner.setFixedSize(130, 130)
        window.circle5_1_inner.setParent(window.bodyContainer)

        window.circle5_2_outer = CircleWidget("#d9d9d9")  # Create a CircleWidget
        window.circle5_2_outer.setFixedSize(150, 150)
        window.circle5_2_outer.radius = min(window.circle5_2_outer.width(), window.circle5_2_outer.height()) // 2
        window.circle5_2_outer.setParent(window.bodyContainer)

        window.circle5_2_inner = CircleWidget("#f2f2f2", "SENTIMENT", 15)  # Create a CircleWidget
        window.circle5_2_inner.setFixedSize(130, 130)
        window.circle5_2_inner.setParent(window.bodyContainer)

        window.circle5_3_outer = CircleWidget("#d9d9d9")  # Create a CircleWidget
        window.circle5_3_outer.setFixedSize(150, 150)
        window.circle5_3_outer.radius = min(window.circle5_3_outer.width(), window.circle5_3_outer.height()) // 2
        window.circle5_3_outer.setParent(window.bodyContainer)

        window.circle5_3_inner = CircleWidget("#f2f2f2", "FACIAL \nEXPRES-\nSION", 15)  # Create a CircleWidget
        window.circle5_3_inner.setFixedSize(130, 130)
        window.circle5_3_inner.setParent(window.bodyContainer)

        window.circle5_4_outer = CircleWidget("#d9d9d9")  # Create a CircleWidget
        window.circle5_4_outer.setFixedSize(150, 150)
        window.circle5_4_outer.radius = min(window.circle5_4_outer.width(), window.circle5_4_outer.height()) // 2
        window.circle5_4_outer.setParent(window.bodyContainer)

        window.circle5_4_inner = CircleWidget("#f2f2f2", "POSE", 15)  # Create a CircleWidget
        window.circle5_4_inner.setFixedSize(130, 130)
        window.circle5_4_inner.setParent(window.bodyContainer)

        #Column 4
        window.circle4_1 = CircleWidget("#f2f2f2")  # Create a CircleWidget
        window.circle4_1.setFixedSize(120, 120)
        window.circle4_1.radius = min(window.circle4_1.width(), window.circle4_1.height()) // 2
        window.circle4_1.setParent(window.bodyContainer)

        window.circle4_2 = CircleWidget("#f2f2f2")  # Create a CircleWidget
        window.circle4_2.setFixedSize(120, 120)
        window.circle4_2.radius = min(window.circle4_2.width(), window.circle4_2.height()) // 2
        window.circle4_2.setParent(window.bodyContainer)

        window.circle4_3 = CircleWidget("#f2f2f2")  # Create a CircleWidget
        window.circle4_3.setFixedSize(120, 120)
        window.circle4_3.radius = min(window.circle4_3.width(), window.circle4_3.height()) // 2
        window.circle4_3.setParent(window.bodyContainer)

        window.rounded4_1 = RoundedFrame("Voice Activity", "#d9d9d9", "black", "20", True)
        window.rounded4_1.setFixedSize(150 ,45)
        window.rounded4_1.setParent(window.bodyContainer)

        window.rounded4_2 = RoundedFrame("Face Tracking", "#d9d9d9", "black", "20", True)
        window.rounded4_2.setFixedSize(150 ,45)
        window.rounded4_2.setParent(window.bodyContainer)

        window.rounded4_3 = RoundedFrame("Body Tracking", "#d9d9d9", "black", "20", True)
        window.rounded4_3.setFixedSize(150 ,45)
        window.rounded4_3.setParent(window.bodyContainer)

        #Column 3
        window.rounded3_1 = RoundedFrame("Audio", "#d9d9d9", "black", "20", True)
        window.rounded3_1.setFixedSize(150 ,45)
        window.rounded3_1.setParent(window.bodyContainer)

        window.rounded3_2 = RoundedFrame("Transcript", "#d9d9d9", "black", "20", True)
        window.rounded3_2.setFixedSize(150 ,45)
        window.rounded3_2.setParent(window.bodyContainer)

        window.rounded3_3 = RoundedFrame("Video", "#d9d9d9", "black", "20", True)
        window.rounded3_3.setFixedSize(150 ,45)
        window.rounded3_3.setParent(window.bodyContainer)

        window.rounded3_4 = RoundedFrame("Skeleton", "#d9d9d9", "black", "20", True)
        window.rounded3_4.setFixedSize(150 ,45)
        window.rounded3_4.setParent(window.bodyContainer)

        #Column 2

        window.circle2_1 = CircleWidget("#f2f2f2", image_path="./GUI/Icons/headsetIcon.svg" )  # Create a CircleWidget
        window.circle2_1.setFixedSize(120, 120)
        window.circle2_1.radius = min(window.circle2_1.width(), window.circle2_1.height()) // 2
        window.circle2_1.setParent(window.bodyContainer)

        window.circle2_2 = CircleWidget("#f2f2f2", image_path="./GUI/Icons/webcamIcon.svg" )  # Create a CircleWidget
        window.circle2_2.setFixedSize(120, 120)
        window.circle2_2.radius = min(window.circle2_2.width(), window.circle2_2.height()) // 2
        window.circle2_2.setParent(window.bodyContainer)

        # Lines from Column 7 to 8
        window.hlineWidgetFtoA1 = HorLineWidget()
        window.hlineWidgetFtoA1.setFixedSize(3, 3)
        window.hlineWidgetFtoA1.setParent(window.bodyContainer)

        window.hlineWidgetFtoA2 = HorLineWidget()
        window.hlineWidgetFtoA2.setFixedSize(3, 3)
        window.hlineWidgetFtoA2.setParent(window.bodyContainer)

        window.vlineWidgetFtoP = VerLineWidget()
        window.vlineWidgetFtoP.setFixedSize(3, 3)
        window.vlineWidgetFtoP.setParent(window.bodyContainer)

        window.hlineWidgetFtoP = HorLineWidget()
        window.hlineWidgetFtoP.setFixedSize(3, 3)
        window.hlineWidgetFtoP.setParent(window.bodyContainer)

        window.vlineWidgetFtoD = VerLineWidget()
        window.vlineWidgetFtoD.setFixedSize(3, 3)
        window.vlineWidgetFtoD.setParent(window.bodyContainer)

        window.hlineWidgetFtoD = HorLineWidget()
        window.hlineWidgetFtoD.setFixedSize(3, 3)
        window.hlineWidgetFtoD.setParent(window.bodyContainer)

        # Lines from column 6 to 7

        window.collectorLine6to7_1 = VerLineWidget()
        window.collectorLine6to7_1.setFixedSize(3, 3)
        window.collectorLine6to7_1.setParent(window.bodyContainer)

        window.collectorLine6to7_2 = VerLineWidget()
        window.collectorLine6to7_2.setFixedSize(3, 3)
        window.collectorLine6to7_2.setParent(window.bodyContainer)

        window.collectorLine6to7_3 = VerLineWidget()
        window.collectorLine6to7_3.setFixedSize(3, 3)
        window.collectorLine6to7_3.setParent(window.bodyContainer)

        window.collectorLine6to7_4 = VerLineWidget()
        window.collectorLine6to7_4.setFixedSize(3, 3)
        window.collectorLine6to7_4.setParent(window.bodyContainer)

        window.collectorLine6to7_5 = VerLineWidget()
        window.collectorLine6to7_5.setFixedSize(3, 3)
        window.collectorLine6to7_5.setParent(window.bodyContainer)

        window.collectorLine6to7_6 = VerLineWidget()
        window.collectorLine6to7_6.setFixedSize(3, 3)
        window.collectorLine6to7_6.setParent(window.bodyContainer)

        window.collectorLine6to7_7 = VerLineWidget()
        window.collectorLine6to7_7.setFixedSize(3, 3)
        window.collectorLine6to7_7.setParent(window.bodyContainer)

        window.collectorLine6to7_8 = VerLineWidget()
        window.collectorLine6to7_8.setFixedSize(3, 3)
        window.collectorLine6to7_8.setParent(window.bodyContainer)

        window.hlineWidgettoCol1 = HorLineWidget()
        window.hlineWidgettoCol1.setFixedSize(3, 3)
        window.hlineWidgettoCol1.setParent(window.bodyContainer)

        window.hlineWidgettoCol2 = HorLineWidget()
        window.hlineWidgettoCol2.setFixedSize(3, 3)
        window.hlineWidgettoCol2.setParent(window.bodyContainer)

        window.hlineWidgettoCol3 = HorLineWidget()
        window.hlineWidgettoCol3.setFixedSize(3, 3)
        window.hlineWidgettoCol3.setParent(window.bodyContainer)

        window.hlineWidgettoCol4 = HorLineWidget()
        window.hlineWidgettoCol4.setFixedSize(3, 3)
        window.hlineWidgettoCol4.setParent(window.bodyContainer)

        window.hlineWidgettoCol5 = HorLineWidget()
        window.hlineWidgettoCol5.setFixedSize(3, 3)
        window.hlineWidgettoCol5.setParent(window.bodyContainer)

        window.hlineWidgettoCol6 = HorLineWidget()
        window.hlineWidgettoCol6.setFixedSize(3, 3)
        window.hlineWidgettoCol6.setParent(window.bodyContainer)

        window.hlineWidgettoCol7 = HorLineWidget()
        window.hlineWidgettoCol7.setFixedSize(3, 3)
        window.hlineWidgettoCol7.setParent(window.bodyContainer)

        window.hlineWidgettoCol8 = HorLineWidget()
        window.hlineWidgettoCol8.setFixedSize(3, 3)
        window.hlineWidgettoCol8.setParent(window.bodyContainer)

        window.hlineWidgetColtoF = HorLineWidget()
        window.hlineWidgetColtoF.setFixedSize(3, 3)
        window.hlineWidgetColtoF.setParent(window.bodyContainer)

        #Lines from Column 5 to Column 6

        window.collectorLine5to6_1 = VerLineWidget()
        window.collectorLine5to6_1.setFixedSize(3, 3)
        window.collectorLine5to6_1.setParent(window.bodyContainer)

        window.collectorLine5to6_1_1 = VerLineWidget()
        window.collectorLine5to6_1_1.setFixedSize(3, 3)
        window.collectorLine5to6_1_1.setParent(window.bodyContainer)
        
        window.hline1fromCol5to6_1 = HorLineWidget()
        window.hline1fromCol5to6_1.setFixedSize(3, 3)
        window.hline1fromCol5to6_1.setParent(window.bodyContainer)

        window.hline2fromCol5to6_1 = HorLineWidget()
        window.hline2fromCol5to6_1.setFixedSize(3, 3)
        window.hline2fromCol5to6_1.setParent(window.bodyContainer)

        window.hline3fromCol5to6_1 = HorLineWidget()
        window.hline3fromCol5to6_1.setFixedSize(3, 3)
        window.hline3fromCol5to6_1.setParent(window.bodyContainer)
        
        window.hlinetoCol5to6_1 = HorLineWidget()
        window.hlinetoCol5to6_1.setFixedSize(3, 3)
        window.hlinetoCol5to6_1.setParent(window.bodyContainer)

        window.horLineWidgetSertoVer = HorLineWidget()
        window.horLineWidgetSertoVer.setFixedSize(3, 3)
        window.horLineWidgetSertoVer.setParent(window.bodyContainer)

        window.verlineWidgetSertoP = VerLineWidget()
        window.verlineWidgetSertoP.setFixedSize(3, 3)
        window.verlineWidgetSertoP.setParent(window.bodyContainer)

        window.hlineWidgetVertoP = HorLineWidget()
        window.hlineWidgetVertoP.setFixedSize(3, 3)
        window.hlineWidgetVertoP.setParent(window.bodyContainer)

        #Facial to column 6

        window.collectorLine5to6_2 = VerLineWidget()
        window.collectorLine5to6_2.setFixedSize(3, 3)
        window.collectorLine5to6_2.setParent(window.bodyContainer)

        window.collectorLine5to6_2_2 = VerLineWidget()
        window.collectorLine5to6_2_2.setFixedSize(3, 3)
        window.collectorLine5to6_2_2.setParent(window.bodyContainer)

        window.collectorLine5to6_2_3 = VerLineWidget()
        window.collectorLine5to6_2_3.setFixedSize(3, 3)
        window.collectorLine5to6_2_3.setParent(window.bodyContainer)

        window.hline1fromCol5to6_2 = HorLineWidget()
        window.hline1fromCol5to6_2.setFixedSize(3, 3)
        window.hline1fromCol5to6_2.setParent(window.bodyContainer)

        window.hline2fromCol5to6_2 = HorLineWidget()
        window.hline2fromCol5to6_2.setFixedSize(3, 3)
        window.hline2fromCol5to6_2.setParent(window.bodyContainer)

        window.hline3fromCol5to6_2 = HorLineWidget()
        window.hline3fromCol5to6_2.setFixedSize(3, 3)
        window.hline3fromCol5to6_2.setParent(window.bodyContainer)

        window.hlinetoCol5to6_2 = HorLineWidget()
        window.hlinetoCol5to6_2.setFixedSize(3, 3)
        window.hlinetoCol5to6_2.setParent(window.bodyContainer)

        #Pose to column 6

        window.hLineWidgetPosetoVer = HorLineWidget()
        window.hLineWidgetPosetoVer.setFixedSize(3, 3)
        window.hLineWidgetPosetoVer.setParent(window.bodyContainer)

        window.verlineWidgetPosetoD = VerLineWidget()
        window.verlineWidgetPosetoD.setFixedSize(3, 3)
        window.verlineWidgetPosetoD.setParent(window.bodyContainer)

        window.hlineWidgetVertoD = HorLineWidget()
        window.hlineWidgetVertoD.setFixedSize(3, 3)
        window.hlineWidgetVertoD.setParent(window.bodyContainer)

        #Lines from 3 to 4 and 5
        
        window.hlineWidgetAudiotoPara1 = HorLineWidget()
        window.hlineWidgetAudiotoPara1.setFixedSize(3, 3)
        window.hlineWidgetAudiotoPara1.setParent(window.bodyContainer)

        window.hlineWidgetAudiotoPara2 = HorLineWidget()
        window.hlineWidgetAudiotoPara2.setFixedSize(3, 3)
        window.hlineWidgetAudiotoPara2.setParent(window.bodyContainer)
        
        window.verLineWidgetAudiotoVoice = VerLineWidget()
        window.verLineWidgetAudiotoVoice.setFixedSize(3, 3)
        window.verLineWidgetAudiotoVoice.setParent(window.bodyContainer)

        window.hlineWidgetAudiotoVoice = HorLineWidget()
        window.hlineWidgetAudiotoVoice.setFixedSize(3, 3)
        window.hlineWidgetAudiotoVoice.setParent(window.bodyContainer)

        window.verLineWidgetVoicetoPara = VerLineWidget()
        window.verLineWidgetVoicetoPara.setFixedSize(3, 3)
        window.verLineWidgetVoicetoPara.setParent(window.bodyContainer)

        window.hlineWidgetVoicetoPara = HorLineWidget()
        window.hlineWidgetVoicetoPara.setFixedSize(3, 3)
        window.hlineWidgetVoicetoPara.setParent(window.bodyContainer)
        
        window.hlinewidgetTratoSen = HorLineWidget()
        window.hlinewidgetTratoSen.setFixedSize(3, 3)
        window.hlinewidgetTratoSen.setParent(window.bodyContainer)

        window.verlineWidgetAudioToTra = VerLineWidget()
        window.verlineWidgetAudioToTra.setFixedSize(3, 3)
        window.verlineWidgetAudioToTra.setParent(window.bodyContainer)

        window.hlineWidgetVideotoFacial1 = HorLineWidget()
        window.hlineWidgetVideotoFacial1.setFixedSize(3, 3)
        window.hlineWidgetVideotoFacial1.setParent(window.bodyContainer)

        window.hlineWidgetVideotoFacial2 = HorLineWidget()
        window.hlineWidgetVideotoFacial2.setFixedSize(3, 3)
        window.hlineWidgetVideotoFacial2.setParent(window.bodyContainer)

        window.verlineWidgetVideotoFace = VerLineWidget()
        window.verlineWidgetVideotoFace.setFixedSize(3, 3)
        window.verlineWidgetVideotoFace.setParent(window.bodyContainer)

        window.hlineWidgetVideotoFace = HorLineWidget()
        window.hlineWidgetVideotoFace.setFixedSize(3, 3)
        window.hlineWidgetVideotoFace.setParent(window.bodyContainer)

        window.verlineWidgetFacetoFacial = VerLineWidget()
        window.verlineWidgetFacetoFacial.setFixedSize(3, 3)
        window.verlineWidgetFacetoFacial.setParent(window.bodyContainer)

        window.hlineWidgetFacetoFacial = HorLineWidget()
        window.hlineWidgetFacetoFacial.setFixedSize(3, 3)
        window.hlineWidgetFacetoFacial.setParent(window.bodyContainer)

        window.verlineWidgetVideotoSkel = VerLineWidget()
        window.verlineWidgetVideotoSkel.setFixedSize(3, 3)
        window.verlineWidgetVideotoSkel.setParent(window.bodyContainer)

        window.hlineWidgetSkeltoBody = HorLineWidget()
        window.hlineWidgetSkeltoBody.setFixedSize(3, 3)
        window.hlineWidgetSkeltoBody.setParent(window.bodyContainer)

        window.hlineWidgetBodytoPose = HorLineWidget()
        window.hlineWidgetBodytoPose.setFixedSize(3, 3)
        window.hlineWidgetBodytoPose.setParent(window.bodyContainer)

        #Lines from 2 to 3

        window.hlineWidgetHeadsettoAudio = HorLineWidget()
        window.hlineWidgetHeadsettoAudio.setFixedSize(3, 3)
        window.hlineWidgetHeadsettoAudio.setParent(window.bodyContainer)

        window.hlineWidgetCamtoVer = HorLineWidget()
        window.hlineWidgetCamtoVer.setFixedSize(3, 3)
        window.hlineWidgetCamtoVer.setParent(window.bodyContainer)

        window.verlineWidgetCamToVideo = VerLineWidget()
        window.verlineWidgetCamToVideo.setFixedSize(3, 3)
        window.verlineWidgetCamToVideo.setParent(window.bodyContainer)

        window.hlineWidgetVertoVideo = HorLineWidget()
        window.hlineWidgetVertoVideo.setFixedSize(3, 3)
        window.hlineWidgetVertoVideo.setParent(window.bodyContainer)
        
        #PlayButton

        window.play_button = QPushButton("Start")
        window.play_button.setFixedSize(100, 50)
        window.play_button.setParent(window.bodyContainer)
        window.play_button.setStyleSheet("background-color: #f0f0f0;")

        window.stop_button = QPushButton("Stop")
        window.stop_button.setFixedSize(100, 50)
        window.stop_button.setParent(window.bodyContainer)
        window.stop_button.setStyleSheet("background-color: #f0f0f0;")

        window.kafka_button = MyButton("Kafka")
        window.kafka_button.setFixedSize(100, 50)
        window.kafka_button.setParent(window.bodyContainer)
        window.kafka_button.setStyleSheet("background-color: #f0f0f0;")

        window.udp_button = MyButton("UDP")
        window.udp_button.setFixedSize(100, 50)
        window.udp_button.setParent(window.bodyContainer)
        window.udp_button.setStyleSheet("background-color: #f0f0f0;")

        window.console = ConsoleOutput()
        window.console.setFixedSize(300, 200)
        window.console.setParent(window.bodyContainer)
        
        # Create the layout
        window.createLayout()

        # Install an event filter to catch the resize events of the bodyContainer
        window.bodyContainer.installEventFilter(window)

        window.showMaximized()