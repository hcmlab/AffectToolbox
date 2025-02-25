from collections import deque
import time


obj = time.gmtime(0)
epoch = time.asctime(obj)
start_time = round(time.time()*1000)


class AffectDeque():
    def __init__(self, maxlen):
        self.q = deque(maxlen=maxlen)
        self.time = deque(maxlen=maxlen)
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)
    
    def append(self, x) -> None:
        self.q.append(x)
        self.time.append(round(time.time()*1000) - start_time)
        # print(len(self.observers))
        for observer in self.observers:
            observer(x)

    
    def __getitem__(self, item):
        return self.q[item]

    def __len__(self):
        return len(self.q)


VALENCE_FACE = AffectDeque(maxlen=100)
for i in range(0, 100):
    VALENCE_FACE.append(.0)

AROUSAL_FACE = AffectDeque(maxlen=100)
for i in range(0, 100):
    AROUSAL_FACE.append(.0)

DOMINANCE_FACE = AffectDeque(maxlen=100)
for i in range(0, 100):
    DOMINANCE_FACE.append(.0)

VALENCE_SPEECH = AffectDeque(maxlen=100)
for i in range(0, 100):
    VALENCE_SPEECH.append(.0)

AROUSAL_SPEECH = AffectDeque(maxlen=100)
for i in range(0, 100):
    AROUSAL_SPEECH.append(.0)

DOMINANCE_SPEECH = AffectDeque(maxlen=100)
for i in range(0, 100):
    DOMINANCE_SPEECH.append(.0)

TRANSCRIPT_SPEECH = AffectDeque(maxlen=100)
for i in range(0, 100):
    TRANSCRIPT_SPEECH.append('')

RMS_VALUES = AffectDeque(maxlen=100)
for i in range(0, 100):
    RMS_VALUES.append(.0)

POS_SENTIMENT = AffectDeque(maxlen=100)
for i in range(0, 100):
    POS_SENTIMENT.append(.0)

NEU_SENTIMENT = AffectDeque(maxlen=100)
for i in range(0, 100):
    NEU_SENTIMENT.append(.0)

NEG_SENTIMENT = AffectDeque(maxlen=100)
for i in range(0, 100):
    NEG_SENTIMENT.append(.0)

VALENCE_SENTIMENT = AffectDeque(maxlen=100)
for i in range(0, 100):
    VALENCE_SENTIMENT.append(.0)

DOMINANCE_POSE = AffectDeque(maxlen=100)
for i in range(0, 100):
    DOMINANCE_POSE.append(.0)

FUSION = AffectDeque(maxlen=100)
for i in range(0, 100):
    FUSION.append([.0, .0, .0])

VOICE_ACTIVITY = AffectDeque(maxlen=1000)
for i in range(0, 1000):
    VOICE_ACTIVITY.append(.0)

FACE_ACTIVITY = AffectDeque(maxlen=1000)
for i in range(0, 1000):
    FACE_ACTIVITY.append(.0)

FACINGCAM_POSE = AffectDeque(maxlen=1000)
for i in range(0, 1000):
    FACINGCAM_POSE.append(.0)

AUDIO_QUEUE = deque(maxlen=100000) # why not AffectDeque?
for i in range(0, 100000):
    AUDIO_QUEUE.append(.0)

HEART_RATE = AffectDeque(maxlen=100)
for i in range(0, 100):
    HEART_RATE.append(.0)

IMAGE_FACE_RAW = AffectDeque(maxlen=200)
IMAGE_FACE_PREPROCESSED = AffectDeque(maxlen=200)
IMAGE_FACE_MESH = AffectDeque(maxlen=100)
IMAGE_BODY_SKEL = AffectDeque(maxlen=100)

FACE_MESH_QUEUE = AffectDeque(maxlen=100)
for i in range(0, 100):
    FACE_MESH_QUEUE.append("not available")

if __name__ == "__main__":
    q = AffectDeque(maxlen=5)
    for i in range(30):
        q.append(i)

    print(start_time)
    print(q[0])
    print(q.time[0])
