import math

import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose

class PoseFromCam():

    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.model = self.mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.6)
        self.image = None
        self.value_string = ''

        self.look_left_min = math.inf
        self.look_left_max = -math.inf
        self.look_right_min = math.inf
        self.look_right_max = -math.inf
        self.look_up_min = math.inf
        self.look_up_max = -math.inf
        self.look_down_min = math.inf
        self.look_down_max = -math.inf
        self.overall_activation_left_last = 0.0
        self.overall_activation_right_last = 0.0
        self.overall_activation_min = math.inf
        self.overall_activation_max = -math.inf

        self.dominance = 0.0

        self.tracking = False

    def predict(self, img):
        self.image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        landmarks = self.model.process(self.image)

        #print(landmarks.pose_world_landmarks)

        if self.image is not None:
            self.image.flags.writeable = True
            self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
            self.mp_drawing.draw_landmarks(
                self.image,
                landmarks.pose_landmarks,
                self.mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=self.mp_drawing_styles.get_default_pose_landmarks_style())

        self.features(landmarks)

    def features(self, landmarks):
        if not landmarks.pose_landmarks:
            self.tracking = False
            return
        self.tracking = True

        look_left = self.distance(landmarks.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE],
                                   landmarks.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EAR])

        look_right = self.distance(landmarks.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE],
                                   landmarks.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EAR])

        norm = (look_left + look_right)
        look_left = look_left / norm
        look_right = look_right / norm

        look_up_1 = self.distance(landmarks.pose_landmarks.landmark[mp_pose.PoseLandmark.MOUTH_LEFT],
                                   landmarks.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW])
        look_up_2 = self.distance(landmarks.pose_landmarks.landmark[mp_pose.PoseLandmark.MOUTH_RIGHT],
                                   landmarks.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW])

        look_down_1 = self.distance(landmarks.pose_landmarks.landmark[mp_pose.PoseLandmark.MOUTH_LEFT],
                                    landmarks.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EAR])
        look_down_2 = self.distance(landmarks.pose_landmarks.landmark[mp_pose.PoseLandmark.MOUTH_RIGHT],
                                    landmarks.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EAR])

        look_up = (look_up_1 + look_up_2) * 0.5
        look_down = (look_down_1 + look_down_2) * 0.5

        norm = (look_up + look_down)
        look_up = look_up / norm
        look_down = look_down / norm

        oa_left = self.overall_activation_left_last
        if landmarks.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].visibility >= 0.5:
            oa_left = self.distance(landmarks.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST],
                                    landmarks.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER])

        oa_left_delta = math.fabs(oa_left - self.overall_activation_left_last)
        self.overall_activation_left_last = oa_left


        oa_right = self.overall_activation_right_last
        if landmarks.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].visibility >= 0.5:
            oa_right = self.distance(landmarks.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST],
                                    landmarks.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER])

        oa_right_delta = math.fabs(oa_right - self.overall_activation_right_last)
        self.overall_activation_right_last = oa_right

        overall_activation = oa_right_delta + oa_left_delta

        if look_left < self.look_left_min:
            self.look_left_min = look_left
        if look_left > self.look_left_max:
            self.look_left_max = look_left

        if look_right < self.look_right_min:
            self.look_right_min = look_right
        if look_right > self.look_right_max:
            self.look_right_max = look_right

        if look_down < self.look_down_min:
            self.look_down_min = look_down
        if look_down > self.look_down_max:
            self.look_down_max = look_down

        if look_up < self.look_up_min:
            self.look_up_min = look_up
        if look_up > self.look_up_max:
            self.look_up_max = look_up

        if overall_activation < self.overall_activation_min:
            self.overall_activation_min = overall_activation
        if overall_activation > self.overall_activation_max:
            self.overall_activation_max = overall_activation

        look_left = round(self.norm(look_left, self.look_left_min, self.look_left_max), 2)
        look_right = round(self.norm(look_right, self.look_right_min, self.look_right_max), 2)
        look_up = round(self.norm(look_up, self.look_up_min, self.look_up_max), 2)
        look_down = round(self.norm(look_down, self.look_down_min, self.look_down_max), 2)
        overall_activation = round(self.norm(overall_activation, self.overall_activation_min, self.overall_activation_max), 2)

        dominance = 0.0
        dominance -= (math.fabs(look_left - look_right) * 0.25)
        dominance += (look_up * 0.5)
        dominance -= (look_down * 0.25)
        # dominance += overall_activation

        if dominance < -1.0:
            dominance = -1.0
        elif dominance > 1.0:
            dominance = 1.0

        self.value_string = '|| '
        self.value_string += 'LookLeft: '
        self.value_string += f'{look_left}'
        self.value_string += ' || '
        self.value_string += f'LookRight: '
        self.value_string += f'{look_right}'
        self.value_string += ' || '
        self.value_string += 'LookUp: '
        self.value_string += f'{look_up}'
        self.value_string += ' || '
        self.value_string += f'LookDown: '
        self.value_string += f'{look_down}'
        self.value_string += ' || '
        self.value_string += f'Overall Activation: '
        self.value_string += f'{overall_activation}'
        self.value_string += ' || '
        self.value_string += f'Dominance: '
        self.value_string += f'{dominance}'
        self.value_string += ' || '

        self.dominance = dominance

        # print("\r" + self.value_string, end='')

    def distance(self, landmark1, landmark2):
        return math.sqrt(math.pow((landmark2.x - landmark1.x), 2) + math.pow((landmark2.y - landmark1.y), 2))

    def norm(self, value, min, max):
        if (max - min) == 0.0:
            return 0.0
        result = (value - min) * (1.0 / (max - min))
        if result < 0.0:
            return 0.0
        elif result > 1.0:
            return 1.0
        else:
            return result
