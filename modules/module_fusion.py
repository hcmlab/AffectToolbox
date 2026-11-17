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

    def append(self, x, weight, speed, timestamp) -> None:
        now = round(time.time()*1000) - qs.start_time
        if timestamp + speed <= now:
            return
        self.q.append(x)
        self.time.append(timestamp)
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

        histories = (qs.VALENCE_FACE, qs.AROUSAL_FACE, qs.DOMINANCE_FACE,
                     qs.VALENCE_SPEECH, qs.AROUSAL_SPEECH, qs.DOMINANCE_SPEECH,
                     qs.VALENCE_SENTIMENT, qs.DOMINANCE_POSE)
        self._last_sequences = {history: history.sequence for history in histories}

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

        self.pose_speed = 5000
        self.pose_weight_dominance = 1.0
        self.pose_boost_dominance = 1.0

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

        # Expire events from the time their processing step finished.
        for events in (EVENTS_VALENCE, EVENTS_AROUSAL, EVENTS_DOMINANCE):
            for index in range(len(events) - 1, -1, -1):
                if events.time[index] + events.speed[index] <= time_curr_ms:
                    del events.q[index]
                    del events.time[index]
                    del events.weight[index]
                    del events.speed[index]

        # Every input uses completion timestamps and is consumed exactly once.
        sources = (
            (self.FUSION_USE_FACE_V, qs.VALENCE_FACE, EVENTS_VALENCE,
             self.face_boost_valence, self.face_weight_valence, self.face_speed),
            (self.FUSION_USE_FACE_A, qs.AROUSAL_FACE, EVENTS_AROUSAL,
             self.face_boost_arousal, self.face_weight_arousal, self.face_speed),
            (self.FUSION_USE_FACE_D, qs.DOMINANCE_FACE, EVENTS_DOMINANCE,
             self.face_boost_dominance, self.face_weight_dominance, self.face_speed),
            (self.FUSION_USE_PARA_V, qs.VALENCE_SPEECH, EVENTS_VALENCE,
             self.voice_boost_valence, self.voice_weight_valence, self.voice_speed),
            (self.FUSION_USE_PARA_A, qs.AROUSAL_SPEECH, EVENTS_AROUSAL,
             self.voice_boost_arousal, self.voice_weight_arousal, self.voice_speed),
            (self.FUSION_USE_PARA_D, qs.DOMINANCE_SPEECH, EVENTS_DOMINANCE,
             self.voice_boost_dominance, self.voice_weight_dominance, self.voice_speed),
            (self.FUSION_USE_SENTIMENT_V, qs.VALENCE_SENTIMENT, EVENTS_VALENCE,
             self.sentiment_boost_valence, self.sentiment_weight_valence, self.sentiment_speed),
            (self.FUSION_USE_POSE_D, qs.DOMINANCE_POSE, EVENTS_DOMINANCE,
             self.pose_boost_dominance, self.pose_weight_dominance, self.pose_speed),
        )
        for enabled, history, events, boost, weight, speed in sources:
            if not enabled:
                continue
            last_sequence = self._last_sequences.get(history, 0)
            for sequence, value, timestamp in tuple(history.records):
                if sequence > last_sequence:
                    events.append(value * boost, weight, speed, timestamp)
                    self._last_sequences[history] = sequence

        # decay event contributions over event deques
        # VALENCE
        sum_of_weights_valence = 0.0
        for index in range(0, len(EVENTS_VALENCE)):
            decay_factor = 1.0 - (float(time_curr_ms - EVENTS_VALENCE.time[index]) / float(EVENTS_VALENCE.speed[index]))
            decayed_value = (EVENTS_VALENCE.q[index] * decay_factor) * (EVENTS_VALENCE.weight[index] * decay_factor)
            result_valence = result_valence + decayed_value
            sum_of_weights_valence = sum_of_weights_valence + (EVENTS_VALENCE.weight[index] * decay_factor)

        # AROUSAL
        sum_of_weights_arousal = 0.0
        for index in range(0, len(EVENTS_AROUSAL)):
            decay_factor = 1.0 - (float(time_curr_ms - EVENTS_AROUSAL.time[index]) / float(EVENTS_AROUSAL.speed[index]))
            decayed_value = (EVENTS_AROUSAL.q[index] * decay_factor) * (EVENTS_AROUSAL.weight[index] * decay_factor)
            result_arousal = result_arousal + decayed_value
            sum_of_weights_arousal = sum_of_weights_arousal + (EVENTS_AROUSAL.weight[index] * decay_factor)

        # DOMINANCE
        sum_of_weights_dominance = 0.0
        for index in range(0, len(EVENTS_DOMINANCE)):
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

        return [result_valence, result_arousal, result_dominance]


