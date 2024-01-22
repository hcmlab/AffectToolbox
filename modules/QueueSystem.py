from collections import deque
import time


obj = time.gmtime(0)
epoch = time.asctime(obj)
start_time = round(time.time()*1000)


class AffectDeque():
    def __init__(self, maxlen):
        self.q = deque(maxlen=maxlen)
        self.time = deque(maxlen=maxlen)

    def append(self, x) -> None:
        self.q.append(x)
        self.time.append(round(time.time()*1000) - start_time)

    def __getitem__(self, item):
        return self.q[item]

    def __len__(self):
        return len(self.q)


VALENCE_FACE = AffectDeque(maxlen=500)
for i in range(0, 500):
    VALENCE_FACE.append(.0)

AROUSAL_FACE = AffectDeque(maxlen=500)
for i in range(0, 500):
    AROUSAL_FACE.append(.0)

DOMINANCE_FACE = AffectDeque(maxlen=500)
for i in range(0, 500):
    DOMINANCE_FACE.append(.0)

VALENCE_SPEECH = AffectDeque(maxlen=500)
for i in range(0, 500):
    VALENCE_SPEECH.append(.0)

AROUSAL_SPEECH = AffectDeque(maxlen=500)
for i in range(0, 500):
    AROUSAL_SPEECH.append(.0)

DOMINANCE_SPEECH = AffectDeque(maxlen=500)
for i in range(0, 500):
    DOMINANCE_SPEECH.append(.0)

TRANSCRIPT_SPEECH = AffectDeque(maxlen=100)
for i in range(0, 100):
    TRANSCRIPT_SPEECH.append('')

RMS_VALUES = AffectDeque(maxlen=500)
for i in range(0, 500):
    RMS_VALUES.append(.0)

POS_SENTIMENT = AffectDeque(maxlen=500)
for i in range(0, 500):
    POS_SENTIMENT.append(.0)

NEU_SENTIMENT = AffectDeque(maxlen=500)
for i in range(0, 500):
    NEU_SENTIMENT.append(.0)

NEG_SENTIMENT = AffectDeque(maxlen=500)
for i in range(0, 500):
    NEG_SENTIMENT.append(.0)

FUSION = AffectDeque(maxlen=500)
for i in range(0, 500):
    FUSION.append([.0, .0, .0])

VOICE_ACTIVITY = AffectDeque(maxlen=500)
for i in range(0, 500000):
    VOICE_ACTIVITY.append(.0)

AUDIO_QUEUE = deque(maxlen=500000) # why not AffectDeque?
for i in range(0, 500000):
    AUDIO_QUEUE.append(.0)

IMAGE_FACE_RAW = AffectDeque(maxlen=500)
IMAGE_FACE_PREPROCESSED = AffectDeque(maxlen=500)
IMAGE_FACE_MESH = AffectDeque(maxlen=500)
IMAGE_BODY_SKEL = AffectDeque(maxlen=500)

FACE_MESH_QUEUE = AffectDeque(maxlen=500)
for i in range(0, 500):
    FACE_MESH_QUEUE.append("not available")

if __name__ == "__main__":
    q = AffectDeque(maxlen=5)
    for i in range(30):
        q.append(i)

    print(start_time)
    print(q[0])
    print(q.time[0])
