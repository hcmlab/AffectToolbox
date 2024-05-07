import math
from collections import deque
import time
import modules.QueueSystem as qs


obj = time.gmtime(0)
epoch = time.asctime(obj)


class EventDeque():
    def __init__(self, maxlen):
        self.q = deque(maxlen=maxlen)
        self.time = deque(maxlen=maxlen)
        self.weight = deque(maxlen=maxlen)
        self.speed = deque(maxlen=maxlen)

    def append(self, x, weight, speed) -> None:
        self.q.append(x)
        self.time.append(round(time.time()*1000) - qs.start_time)
        self.weight.append(weight)
        self.speed.append(speed)

    def __getitem__(self, item):
        return self.q[item]

    def __len__(self):
        return len(self.q)


EVENTS_VALENCE = EventDeque(maxlen=500)
EVENTS_AROUSAL = EventDeque(maxlen=500)
EVENTS_DOMINANCE = EventDeque(maxlen=500)


class FusionModule():
    def __init__(self):

        self.last_time_ms = qs.start_time

        self.event_threshold = 0.1
        self.fusion_speed = 1000

        self.voice_activity_tracked = False
        self.voice_speed = 5000
        self.voice_weight_valence = 1.0
        self.voice_boost_valence = 1.0
        self.voice_weight_arousal = 1.0
        self.voice_boost_arousal = 1.0
        self.voice_weight_dominance = 1.0
        self.voice_boost_dominance = 1.0

        self.face_speed = 5000
        self.face_weight_valence = 1.0
        self.face_boost_valence = 1.25
        self.face_weight_arousal = 0.5
        self.face_boost_arousal = 1.75
        self.face_weight_dominance = 1.0
        self.face_boost_dominance = 1.25

        self.sentiment_speed = 5000
        self.sentiment_weight_valence = 1.0
        self.sentiment_boost_valence = 1.0

        self.value_string = ''

        self.FUSION_USE_PARA_V = False
        self.FUSION_USE_PARA_A = False
        self.FUSION_USE_PARA_D = False
        self.FUSION_USE_SENTIMENT_V = False
        self.FUSION_USE_FACE_V = False
        self.FUSION_USE_FACE_A = False
        self.FUSION_USE_FACE_D = False
        self.FUSION_USE_POSE_D = False

    def update_fusion(self):

        # reset
        result_valence = 0.0
        result_arousal = 0.0
        result_dominance = 0.0

        # current time
        time_curr_ms = round(time.time()*1000) - qs.start_time

        # delete events in event deques not contributing anymore (value_decayed < threshold || lifetime > speed)
        # VALENCE
        if len(EVENTS_VALENCE) > 1:
            while EVENTS_VALENCE.time[0] + EVENTS_VALENCE.speed[0] < time_curr_ms:
                if len(EVENTS_VALENCE) > 1:
                    if EVENTS_VALENCE.time[0] + EVENTS_VALENCE.speed[0] < time_curr_ms:
                        EVENTS_VALENCE.q.popleft()
                        EVENTS_VALENCE.time.popleft()
                        EVENTS_VALENCE.weight.popleft()
                        EVENTS_VALENCE.speed.popleft()
                else:
                    break
        # AROUSAL
        if len(EVENTS_AROUSAL) > 1:
            while EVENTS_AROUSAL.time[0] + EVENTS_AROUSAL.speed[0] < time_curr_ms:
                if len(EVENTS_AROUSAL) > 1:
                    if EVENTS_AROUSAL.time[0] + EVENTS_AROUSAL.speed[0] < time_curr_ms:
                        EVENTS_AROUSAL.q.popleft()
                        EVENTS_AROUSAL.time.popleft()
                        EVENTS_AROUSAL.weight.popleft()
                        EVENTS_AROUSAL.speed.popleft()
                else:
                    break

        # DOMINANCE
        if len(EVENTS_DOMINANCE) > 1:
            while EVENTS_DOMINANCE.time[0] + EVENTS_DOMINANCE.speed[0] < time_curr_ms:
                if len(EVENTS_DOMINANCE) > 1:
                    if EVENTS_DOMINANCE.time[0] + EVENTS_DOMINANCE.speed[0] < time_curr_ms:
                        EVENTS_DOMINANCE.q.popleft()
                        EVENTS_DOMINANCE.time.popleft()
                        EVENTS_DOMINANCE.weight.popleft()
                        EVENTS_DOMINANCE.speed.popleft()
                else:
                    break

        # add new events to event deques
        # FACE - VALENCE
        if self.FUSION_USE_FACE_V:
            index = 1
            while qs.VALENCE_FACE.time[len(qs.VALENCE_FACE) - index] > self.last_time_ms:
                if qs.VALENCE_FACE.time[len(qs.VALENCE_FACE) - index] > self.last_time_ms:
                    EVENTS_VALENCE.append(qs.VALENCE_FACE[len(qs.VALENCE_FACE) - index] * self.face_boost_valence, self.face_weight_valence, self.face_speed)
                index = index + 1

        # FACE - AROUSAL
        if self.FUSION_USE_FACE_A:
            index = 1
            while qs.AROUSAL_FACE.time[len(qs.AROUSAL_FACE) - index] > self.last_time_ms:
                if qs.AROUSAL_FACE.time[len(qs.AROUSAL_FACE) - index] > self.last_time_ms:
                    EVENTS_AROUSAL.append(qs.AROUSAL_FACE[len(qs.AROUSAL_FACE) - index] * self.face_boost_arousal, self.face_weight_arousal, self.face_speed)
                index = index + 1

        # .. moved to AffectPipeline.py
        # DERIVE PERCEIVED DOMINANCE FROM VALENCE/AROUSAL
        # dominance_face_latest = 0.0
        # valence_face_latest = 0.0
        # arousal_face_latest = 0.0
        # if qs.AROUSAL_FACE[len(qs.AROUSAL_FACE) - 1] is not None and qs.VALENCE_FACE[len(qs.AROUSAL_FACE) - 1] is not None:
        #     valence_face_latest = qs.VALENCE_FACE[len(qs.VALENCE_FACE) - 1] * self.face_boost_valence
        #     arousal_face_latest = qs.AROUSAL_FACE[len(qs.AROUSAL_FACE) - 1] * self.face_boost_arousal
        #     if arousal_face_latest < 0.0:
        #         dominance_face_latest = -1.0
        #     elif arousal_face_latest > 0.5:
        #         dominance_face_latest = 1.0
        #     elif abs(valence_face_latest) > (-2.0 * arousal_face_latest + 1.0):
        #         dominance_face_latest = 1.0
        #     else:
        #         dominance_face_latest = -1.0

        # NORMALIZE PERCEIVED DOMINANCE
        # if dominance_face_latest == 1.0:
        #     dominance_face_latest = (math.sqrt(math.pow(valence_face_latest, 2.0) + math.pow(arousal_face_latest, 2.0))) / 1.4
        # else:
        #     dominance_face_latest = (math.sqrt(math.pow(valence_face_latest, 2.0) + math.pow(arousal_face_latest, 2.0))) / -1.4

        # FACE - PERCEIVED DOMINANCE
        # qs.DOMINANCE_FACE.append(dominance_face_latest * self.face_boost_dominance)
        # EVENTS_DOMINANCE.append(dominance_face_latest * self.face_boost_dominance, self.face_weight_dominance, self.face_speed)
        # .. instead now:

        if self.FUSION_USE_FACE_D:
            index = 1
            while qs.DOMINANCE_FACE.time[len(qs.DOMINANCE_FACE) - index] > self.last_time_ms:
                if qs.DOMINANCE_FACE.time[len(qs.DOMINANCE_FACE) - index] > self.last_time_ms:
                    EVENTS_DOMINANCE.append(qs.DOMINANCE_FACE[len(qs.DOMINANCE_FACE) - index] * self.face_boost_dominance,
                                          self.face_weight_dominance, self.face_speed)
                index = index + 1

        # VOICE - BUT ONLY IF VOICE ACTIVITY ...
        if qs.VOICE_ACTIVITY[len(qs.VOICE_ACTIVITY) - 1] != 0 or not self.voice_activity_tracked:
            # VOICE - VALENCE
            if self.FUSION_USE_PARA_V:
                index = 1
                while qs.VALENCE_SPEECH.time[len(qs.VALENCE_SPEECH) - index] > self.last_time_ms:
                    if qs.VALENCE_SPEECH.time[len(qs.VALENCE_SPEECH) - index] > self.last_time_ms:
                        EVENTS_VALENCE.append(qs.VALENCE_SPEECH[len(qs.VALENCE_SPEECH) - index] * self.voice_boost_valence, self.voice_weight_valence, self.voice_speed)
                    index = index + 1

            # VOICE - AROUSAL
            if self.FUSION_USE_PARA_A:
                index = 1
                while qs.AROUSAL_SPEECH.time[len(qs.AROUSAL_SPEECH) - index] > self.last_time_ms:
                    if qs.AROUSAL_SPEECH.time[len(qs.AROUSAL_SPEECH) - index] > self.last_time_ms:
                        EVENTS_AROUSAL.append(qs.AROUSAL_SPEECH[len(qs.AROUSAL_SPEECH) - index] * self.voice_boost_arousal, self.voice_weight_arousal, self.voice_speed)
                    index = index + 1

            # VOICE - DOMINANCE
            if self.FUSION_USE_PARA_D:
                index = 1
                while qs.DOMINANCE_SPEECH.time[len(qs.DOMINANCE_SPEECH) - index] > self.last_time_ms:
                    if qs.DOMINANCE_SPEECH.time[len(qs.DOMINANCE_SPEECH) - index] > self.last_time_ms:
                        EVENTS_DOMINANCE.append(qs.DOMINANCE_SPEECH[len(qs.DOMINANCE_SPEECH) - index] * self.voice_boost_dominance, self.voice_weight_dominance, self.voice_speed)
                    index = index + 1

        # SENTIMENT - BUT ONLY IF VOICE ACTIVITY ...
        # if qs.VOICE_ACTIVITY[len(qs.VOICE_ACTIVITY) - 1] != 0 or not self.voice_activity_tracked:
        # SENTIMENT - VALENCE
        if self.FUSION_USE_SENTIMENT_V:
            index = 1
            while qs.VALENCE_SENTIMENT.time[len(qs.VALENCE_SENTIMENT) - index] > self.last_time_ms:
                if qs.VALENCE_SENTIMENT.time[len(qs.VALENCE_SENTIMENT) - index] > self.last_time_ms:
                    EVENTS_VALENCE.append(qs.VALENCE_SENTIMENT[len(qs.VALENCE_SENTIMENT) - index] * self.sentiment_boost_valence, self.sentiment_weight_valence, self.sentiment_speed)
                index = index + 1

        # decay event contributions over event deques
        # VALENCE
        sum_of_weights_valence = 0.0
        for index in range(0, len(EVENTS_VALENCE) - 1):
            decay_factor = 1.0 - (float(time_curr_ms - EVENTS_VALENCE.time[index]) / float(EVENTS_VALENCE.speed[index]))
            decayed_value = (EVENTS_VALENCE.q[index] * decay_factor) * (EVENTS_VALENCE.weight[index] * decay_factor)
            result_valence = result_valence + decayed_value
            sum_of_weights_valence = sum_of_weights_valence + (EVENTS_VALENCE.weight[index] * decay_factor)

        # AROUSAL
        sum_of_weights_arousal = 0.0
        for index in range(0, len(EVENTS_AROUSAL) - 1):
            decay_factor = 1.0 - (float(time_curr_ms - EVENTS_AROUSAL.time[index]) / float(EVENTS_AROUSAL.speed[index]))
            decayed_value = (EVENTS_AROUSAL.q[index] * decay_factor) * (EVENTS_AROUSAL.weight[index] * decay_factor)
            result_arousal = result_arousal + decayed_value
            sum_of_weights_arousal = sum_of_weights_arousal + (EVENTS_AROUSAL.weight[index] * decay_factor)

        # DOMINANCE
        sum_of_weights_dominance = 0.0
        for index in range(0, len(EVENTS_DOMINANCE) - 1):
            decay_factor = 1.0 - (float(time_curr_ms - EVENTS_DOMINANCE.time[index]) / float(EVENTS_DOMINANCE.speed[index]))
            decayed_value = (EVENTS_DOMINANCE.q[index] * decay_factor) * (EVENTS_DOMINANCE.weight[index] * decay_factor)
            result_dominance = result_dominance + decayed_value
            sum_of_weights_dominance = sum_of_weights_dominance + (EVENTS_DOMINANCE.weight[index] * decay_factor)

        # calculate current fusion values
        # VALENCE
        if sum_of_weights_valence != 0.0:
            result_valence = result_valence / sum_of_weights_valence

        # AROUSAL
        if sum_of_weights_arousal != 0.0:
            result_arousal = result_arousal / sum_of_weights_arousal

        # DOMINANCE
        if sum_of_weights_dominance != 0.0:
            result_dominance = result_dominance / sum_of_weights_dominance

        # !results have a hard time reaching extrema! fix that :)
        # 1st try ...
        result_valence = result_valence * (2.0 - abs(result_valence))
        if result_valence > 1.0:
            result_valence = 1.0
        elif result_valence < -1.0:
            result_valence = -1.0

        result_arousal = result_arousal * (2.0 - abs(result_arousal))
        if result_arousal > 1.0:
            result_arousal = 1.0
        elif result_arousal < -1.0:
            result_arousal = -1.0

        result_dominance = result_dominance * (2.0 - abs(result_dominance))
        if result_dominance > 1.0:
            result_dominance = 1.0
        elif result_dominance < -1.0:
            result_dominance = -1.0

        # store last call time
        self.last_time_ms = time_curr_ms
        return [result_valence, result_arousal, result_dominance]


