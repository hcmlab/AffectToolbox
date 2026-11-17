![AffectToolbox](/AffectToolbox.png)
# The AffectToolbox: Affect Analysis for Everyone
## **1. What it is about**
The AffectToolbox provides a user-friendly solution for multimodal realtime analysis of Pleasure, Arousal and Dominance. See our paper for in-depth information: 
[ArXiv Link](https://arxiv.org/pdf/2402.15195)

And here is how it looks:
![System Scheme](/System.png)

## **2. Installation**
**** For getting access to a one-click-installer, please write an email to Silvan Mertes (silvan.mertes@uni-a.de). (We are still working on licence stuff before we can upload it on Github)****

For the standard installation (recommended!) via Python environment do the following:
- Clone repository
- Install [uv](https://docs.astral.sh/uv/getting-started/installation/) (Windows: `winget install --id astral-sh.uv -e`), then restart your terminal or IDE.
- Run `uv sync --locked --managed-python` in the repository root. uv downloads the Python 3.13 version in `.python-version`, creates `.venv`, and installs the locked dependencies. The current environment targets Windows x64.
- Download ressource folder here: ToDo
- Unzip, then put the res-Folder in root-Directory of this repository
- Run `uv run --locked python scripts/download_models.py` to download any missing MediaPipe Tasks models. The original `res/ier_model/valence_arousal_model.tflite` and `res/ser_model/model.onnx` plus `model.yaml` are still required.
- Run `uv run --locked main.py`.

In PyCharm, select `.venv\Scripts\python.exe` as the project interpreter after syncing. You can run `main.py` normally from the IDE.

Dependencies are maintained in `pyproject.toml`; `uv.lock` records the resolved versions. Commit both files and `.python-version`, but never commit virtual environments. To change a dependency, use `uv add "package==version"` and verify the application before committing the updated lockfile.

The original speech emotion, facial emotion, and Cardiff multilingual sentiment models remain the defaults. Facial inference uses LiteRT, speech emotion uses audonnx/ONNX Runtime, tracking uses MediaPipe Tasks, transcription uses faster-whisper (`base`, CPU INT8), and voice activity uses Silero ONNX. Transcription retains the existing English language setting. Whisper and sentiment weights download on first use; internet access is required until cached.

Fusion still receives valence/arousal/dominance in the existing order and scale. Sentiment valence is positive probability minus negative probability, resolved by label name. Facial and pose dominance retain their existing heuristic calculations.

Audio capture uses mono float32 at **16 kHz** with reads of at most 512 samples (32 ms). Other capture rates are rejected to avoid feeding the speech emotion model incorrectly sampled audio. Silero processes every new 512-sample frame once, retaining recurrent state for the run. `VAD_THRESHOLD` compares each frame's speech probability (default 0.25). The Audio preview also starts capture when no analysis module is selected.

Audio settings are available through the existing right-click dialogs:

| Dialog | Setting | Default | Meaning |
|---|---|---|---|
| PARALINGUISTIC | `SER_WINDOW_SIZE` | 3.0 s | Latest audio used for emotion inference |
| PARALINGUISTIC | `SER_MIN_SPEECH` | 0.5 s | Minimum detected speech within that window |
| PARALINGUISTIC | `SER_LOOP_RATE` | 1 Hz | Emotion update frequency |
| Transcript | `STT_WINDOW_SIZE` | 10.0 s | Maximum utterance length before splitting |
| Transcript | `STT_SILENCE` | 0.6 s | Silence required to finish an utterance |
| Transcript | `STT_PRE_ROLL` | 0.2 s | Audio retained before detected speech starts |

The rolling buffer grows to accommodate the longest configured window plus margin. Windows use exact sample counts, including fractional seconds, and emotion inference waits for enough recorded audio. Transcription runs on completed segments; sentiment runs once per new nonempty transcript. Silences and boundaries are resolved to 32 ms frames, except the exact maximum segment length. Continuous speech is split at the configured maximum without dropping speech samples. Stopping discards an unfinished utterance.

All fusion inputs are timestamped when their processing step finishes. Fusion uses that completion time for decay and expiry, consumes each result once, and includes a single valid event. Inference latency does not reduce a result's lifetime; sentiment starts its lifetime when sentiment inference finishes. Results that have already spent their entire lifetime waiting after completion expire normally. Processing history resets on Run; stopped GUI previews remain visible. Legacy `VAD_LOOP_RATE` no longer controls speech detection, old microphone chunk sizes are capped at 512, and the internal transcription queue is polled at least ten times per second. Existing saved settings override the new window defaults; review them when loading an older config.

`requirements.txt` is a compatibility export, not the dependency source. Regenerate it after dependency changes with `uv export --locked --format requirements-txt --no-hashes --output-file requirements.txt`.

To run the automated checks: `uv run --locked python -m unittest discover -s tests -v`. Model resources and camera/microphone devices are external prerequisites; uv does not install them. faster-whisper's audio decoding uses PyAV's bundled FFmpeg libraries, so a separate FFmpeg installation is not required for transcription.

## **3. Cite us :-)**
If you use the AffectToolbox (or parts of it) for scientific reasons, please cite us in your publication. 
```
@inproceedings{mertes2024affecttoolbox,
  title={The AffectToolbox: Affect Analysis for Everyone},
  author={Mertes, Silvan and Schiller, Dominik and Dietz, Michael and Andr{\'e}, Elisabeth and Lingenfelser, Florian},
  booktitle={2024 12th International conference on affective computing and intelligent interaction (ACII)},
  year={2024},
  organization={IEEE}
}
```
