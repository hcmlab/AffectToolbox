"""This file implements the main logic for click-events on the GUI."""
import gc
from GUI.Components.FloatWidget import FloatWidget
from modules.AffectPipeline import AffectPipeline
from GUI.Components.ImageWindow import ImageWindow
from GUI.Components.AudioWidget import PlotWidget
from GUI.Components.TranscriptWidget import TranscriptWidget

####################################### Top Half (Microphone Input) #########################################
def HeadphonesClick(window):
    """Implelments the click event for the headphones widget"""
    def turnOn():
        window.circle2_1.toggleColor()

    def turnOff():
        if window.MIC_LOOP:
            AudioClick(window)
        window.circle2_1.toggleColor()

    if window.HEADSET:
        window.HEADSET = False
        turnOff()
    else:
        window.HEADSET = True
        turnOn()

def AudioClick(window):
    """Implements the click event for the audio widget"""
    def turnOff():
        if window.VOICE_ACTIVITY_LOOP:
            VoiceActivityClick(window)
        if window.PARA_LOOP:
            ParaClick(window)
        if window.TRANSCRIPT_LOOP:
            TranscriptClick(window)
        window.rounded3_1.toggleColor()
        window.hlineWidgetHeadsettoAudio.toggleColor()

    def turnOn():
        window.rounded3_1.toggleColor()
        window.hlineWidgetHeadsettoAudio.toggleColor()
        if not window.HEADSET:
            HeadphonesClick(window)

    if window.MIC_LOOP:
        window.MIC_LOOP = False
        turnOff()
    else:
        window.MIC_LOOP = True
        turnOn()

def VoiceActivityClick(window):
    """Implements the click event for the voice activity widget"""
    def turnOff():
        window.rounded4_1.toggleColor()
        if window.PARA_LOOP:
            window.verLineWidgetVoicetoPara.toggleColor()
            window.hlineWidgetVoicetoPara.toggleColor()
            window.hlineWidgetAudiotoVoice.toggleColor()
            window.verLineWidgetAudiotoVoice.toggleColor()
        else:
            window.hlineWidgetAudiotoPara1.toggleColor()
            window.hlineWidgetAudiotoVoice.toggleColor()
            window.verLineWidgetAudiotoVoice.toggleColor()

    def turnOn():
        if not window.MIC_LOOP:
            AudioClick(window)
        window.rounded4_1.toggleColor()
        if window.PARA_LOOP:
            window.verLineWidgetVoicetoPara.toggleColor()
            window.hlineWidgetVoicetoPara.toggleColor()
            window.hlineWidgetAudiotoVoice.toggleColor()
            window.verLineWidgetAudiotoVoice.toggleColor()
        else:
            window.hlineWidgetAudiotoPara1.toggleColor()
            window.hlineWidgetAudiotoVoice.toggleColor()
            window.verLineWidgetAudiotoVoice.toggleColor()
        
    if window.VOICE_ACTIVITY_LOOP:
        window.VOICE_ACTIVITY_LOOP = False
        turnOff()
    else:
        window.VOICE_ACTIVITY_LOOP = True
        turnOn()

def ParaClick(window):
    """Implements the click event for the Para-Linguistic widget"""
    def turnOff():
        #Backtracking
        if window.PARA_PLEASURE:
            ParaPleasureClick(window)
        if window.PARA_AROUSAL:
            ParaArousalClick(window)
        if window.PARA_DOMINANCE:
            ParaDominanceClick(window)

        window.circle5_1_inner.toggleColor()
        if window.VOICE_ACTIVITY_LOOP:
            window.hlineWidgetAudiotoPara2.toggleColor()
            window.verLineWidgetVoicetoPara.toggleColor()
            window.hlineWidgetVoicetoPara.toggleColor()
        else:
            window.hlineWidgetAudiotoPara1.toggleColor()
            window.hlineWidgetAudiotoPara2.toggleColor()

    def turnOn():
        if window.MIC_LOOP and not window.VOICE_ACTIVITY_LOOP:
            window.hlineWidgetAudiotoPara1.toggleColor()
        if not window.MIC_LOOP:
            AudioClick(window)
            window.hlineWidgetAudiotoPara1.toggleColor()
        if window.VOICE_ACTIVITY_LOOP:
            window.verLineWidgetVoicetoPara.toggleColor()
            window.hlineWidgetVoicetoPara.toggleColor()
        window.circle5_1_inner.toggleColor()
        window.hlineWidgetAudiotoPara2.toggleColor()
    
    if window.PARA_LOOP:
        window.PARA_LOOP = False
        turnOff()
    else:
        window.PARA_LOOP = True
        turnOn()

def ParaPleasureClick(window):
    """Implements the click event for the Para-Linguistic-Pleasure widget"""
    def turnOff():
        #Left side
        window.rounded6_1.toggleColor()
        window.hline1fromCol5to6_1.toggleColor()
        if not window.PARA_AROUSAL and not window.PARA_DOMINANCE:
            window.hlinetoCol5to6_1.toggleColor()

        #Right side
        topHalf = True
        bottomHalf = True
        if window.FUSION_LOOP:
            if not window.PARA_AROUSAL and not window.PARA_DOMINANCE and not window.SENT_PLEASURE:
                topHalf = False
            if not window.FACIAL_PLEASURE and not window.FACIAL_AROUSAL and not window.FACIAL_DOMINANCE and not window.POSE_DOMINANCE:
                bottomHalf = False
            if not topHalf and not bottomHalf:
                window.hlineWidgetColtoF.toggleColor()
        
            window.hlineWidgettoCol1.toggleColor()
            if not topHalf:
                window.collectorLine6to7_1.toggleColor()
                window.collectorLine6to7_2.toggleColor()
                window.collectorLine6to7_3.toggleColor()
                window.collectorLine6to7_4.toggleColor()
                return
            if not window.PARA_AROUSAL:
                window.collectorLine6to7_1.toggleColor()
                window.collectorLine6to7_2.toggleColor()
                if not window.PARA_DOMINANCE:
                    window.collectorLine6to7_3.toggleColor()
                    return
            else:
                window.collectorLine6to7_1.toggleColor()

    def turnOn():
        #Left side
        window.rounded6_1.toggleColor()
        if not window.PARA_LOOP:
            ParaClick(window)
        if not window.PARA_AROUSAL and not window.PARA_DOMINANCE:
            window.hlinetoCol5to6_1.toggleColor()
        window.hline1fromCol5to6_1.toggleColor()

        #Right side
        topHalf = True
        bottomHalf = True
        if window.FUSION_LOOP:
            if not window.PARA_AROUSAL and not window.PARA_DOMINANCE and not window.SENT_PLEASURE:
                topHalf = False
            if not window.FACIAL_PLEASURE and not window.FACIAL_AROUSAL and not window.FACIAL_DOMINANCE and not window.POSE_DOMINANCE:
                bottomHalf = False
            if not topHalf and not bottomHalf:
                window.hlineWidgetColtoF.toggleColor()
        
            window.hlineWidgettoCol1.toggleColor()
            if not topHalf:
                window.collectorLine6to7_1.toggleColor()
                window.collectorLine6to7_2.toggleColor()
                window.collectorLine6to7_3.toggleColor()
                window.collectorLine6to7_4.toggleColor()
                return
            if not window.PARA_AROUSAL:
                window.collectorLine6to7_1.toggleColor()
                window.collectorLine6to7_2.toggleColor()
                if not window.PARA_DOMINANCE:
                    window.collectorLine6to7_3.toggleColor()
                    return
            else:
                window.collectorLine6to7_1.toggleColor()

    if window.PARA_PLEASURE:
        window.PARA_PLEASURE = False
        turnOff()
    else:
        window.PARA_PLEASURE = True
        turnOn()
    #Rest

def ParaArousalClick(window):
    """Implements the click event for the Para-Linguistic-Arousal widget"""
    def turnOff():
        #Left side
        window.rounded6_2.toggleColor()
        window.hline2fromCol5to6_1.toggleColor()
        if not window.PARA_DOMINANCE:
            window.collectorLine5to6_1.toggleColor()
        if not window.PARA_PLEASURE and not window.PARA_DOMINANCE:
            window.hlinetoCol5to6_1.toggleColor()

        #Right side
        topHalf = True
        bottomHalf = True
        if window.FUSION_LOOP:
            if not window.PARA_PLEASURE and not window.PARA_DOMINANCE and not window.SENT_PLEASURE:
                topHalf = False
            if not window.FACIAL_PLEASURE and not window.FACIAL_AROUSAL and not window.FACIAL_DOMINANCE and not window.POSE_DOMINANCE:
                bottomHalf = False
            if not topHalf and not bottomHalf:
                window.hlineWidgetColtoF.toggleColor()
        
            window.hlineWidgettoCol2.toggleColor()
            if not topHalf:
                window.collectorLine6to7_2.toggleColor()
                window.collectorLine6to7_3.toggleColor()
                window.collectorLine6to7_4.toggleColor()
                return
            if not window.PARA_PLEASURE:
                window.collectorLine6to7_2.toggleColor()
                if not window.PARA_DOMINANCE:
                    window.collectorLine6to7_3.toggleColor()
                    return

    def turnOn():
        #Left side
        window.rounded6_2.toggleColor()
        if not window.PARA_LOOP:
            ParaClick(window)
        if not window.PARA_DOMINANCE:
            window.collectorLine5to6_1.toggleColor()
        if not window.PARA_PLEASURE and not window.PARA_DOMINANCE:
            window.hlinetoCol5to6_1.toggleColor()
        window.hline2fromCol5to6_1.toggleColor()

        #Right side
        topHalf = True
        bottomHalf = True
        if window.FUSION_LOOP:
            if not window.PARA_PLEASURE and not window.PARA_DOMINANCE and not window.SENT_PLEASURE:
                topHalf = False
            if not window.FACIAL_PLEASURE and not window.FACIAL_AROUSAL and not window.FACIAL_DOMINANCE and not window.POSE_DOMINANCE:
                bottomHalf = False
            if not topHalf and not bottomHalf:
                window.hlineWidgetColtoF.toggleColor()
        
            window.hlineWidgettoCol2.toggleColor()
            if not topHalf:
                window.collectorLine6to7_2.toggleColor()
                window.collectorLine6to7_3.toggleColor()
                window.collectorLine6to7_4.toggleColor()
                return
            if not window.PARA_PLEASURE:
                window.collectorLine6to7_2.toggleColor()
                if not window.PARA_DOMINANCE:
                    window.collectorLine6to7_3.toggleColor()
                    return

    if window.PARA_AROUSAL:
        window.PARA_AROUSAL = False
        turnOff()
    else:
        window.PARA_AROUSAL = True
        turnOn()

def ParaDominanceClick(window):
    """Implements the click event for the Para-Linguistic-Dominance widget"""
    def turnOff():
        #Left side
        window.rounded6_3.toggleColor()
        window.hline3fromCol5to6_1.toggleColor()
        window.collectorLine5to6_1_1.toggleColor()
        if not window.PARA_PLEASURE and not window.PARA_AROUSAL:
            window.hlinetoCol5to6_1.toggleColor()
        if not window.PARA_AROUSAL:
            window.collectorLine5to6_1.toggleColor()

        #Right side
        topHalf = True
        bottomHalf = True
        if window.FUSION_LOOP:
            if not window.PARA_PLEASURE and not window.PARA_AROUSAL and not window.SENT_PLEASURE:
                topHalf = False
            if not window.FACIAL_PLEASURE and not window.FACIAL_AROUSAL and not window.FACIAL_DOMINANCE and not window.POSE_DOMINANCE:
                bottomHalf = False
            if not topHalf and not bottomHalf:
                window.hlineWidgetColtoF.toggleColor()
        
            window.hlineWidgettoCol3.toggleColor()
            if not topHalf:
                window.collectorLine6to7_3.toggleColor()
                window.collectorLine6to7_4.toggleColor()
                return
            if not window.PARA_AROUSAL and not window.PARA_PLEASURE:
                window.collectorLine6to7_3.toggleColor()
    
    def turnOn():
        #Left side
        window.rounded6_3.toggleColor()
        window.collectorLine5to6_1_1.toggleColor()
        window.hline3fromCol5to6_1.toggleColor()
        if not window.PARA_LOOP:
            ParaClick(window)
        if not window.PARA_PLEASURE and not window.PARA_AROUSAL:
            window.hlinetoCol5to6_1.toggleColor()
        if not window.PARA_AROUSAL:
            window.collectorLine5to6_1.toggleColor()

        #Right side
        topHalf = True
        bottomHalf = True
        if window.FUSION_LOOP:
            if not window.PARA_PLEASURE and not window.PARA_AROUSAL and not window.SENT_PLEASURE:
                topHalf = False
            if not window.FACIAL_PLEASURE and not window.FACIAL_AROUSAL and not window.FACIAL_DOMINANCE and not window.POSE_DOMINANCE:
                bottomHalf = False
            if not topHalf and not bottomHalf:
                window.hlineWidgetColtoF.toggleColor()
        
            window.hlineWidgettoCol3.toggleColor()
            if not topHalf:
                window.collectorLine6to7_3.toggleColor()
                window.collectorLine6to7_4.toggleColor()
                return
            if not window.PARA_AROUSAL and not window.PARA_PLEASURE:
                window.collectorLine6to7_3.toggleColor()
    
    if window.PARA_DOMINANCE:
        window.PARA_DOMINANCE = False
        turnOff()
    else:
        window.PARA_DOMINANCE = True
        turnOn()

def TranscriptClick(window):
    """Implements the click event for the transcript widget"""
    def turnOn():
        if not window.MIC_LOOP:
            AudioClick(window)
        window.rounded3_2.toggleColor()
        window.verlineWidgetAudioToTra.toggleColor()

    def turnOff():
        if window.SENTIMENT_LOOP:
            SentimentClick(window)
        window.rounded3_2.toggleColor()
        window.verlineWidgetAudioToTra.toggleColor()

    if window.TRANSCRIPT_LOOP:
        window.TRANSCRIPT_LOOP = False
        turnOff()
    else:
        window.TRANSCRIPT_LOOP = True
        turnOn()

def SentimentClick(window):
    """Implements the click event for the sentiment widget"""
    def turnOff():
        #Backtracking
        if window.SENT_PLEASURE:
            SentimentPleasureClick(window)

        window.circle5_2_inner.toggleColor()
        window.hlinewidgetTratoSen.toggleColor()
    
    def turnOn():
        window.circle5_2_inner.toggleColor()
        if not window.TRANSCRIPT_LOOP:
            TranscriptClick(window)
        window.hlinewidgetTratoSen.toggleColor()

    if window.SENTIMENT_LOOP:
        window.SENTIMENT_LOOP = False
        turnOff()
    else:
        window.SENTIMENT_LOOP = True
        turnOn()

def SentimentPleasureClick(window):
    """Implements the click event for the sentiment-pleasure widget"""
    def turnOff():
        #Left side
        window.rounded6_4.toggleColor()
        window.horLineWidgetSertoVer.toggleColor()
        window.verlineWidgetSertoP.toggleColor()
        window.hlineWidgetVertoP.toggleColor()

        #Right side
        topHalf = True
        bottomHalf = True
        if window.FUSION_LOOP:
            if not window.PARA_PLEASURE and not window.PARA_AROUSAL and not window.PARA_DOMINANCE:
                topHalf = False
            if not window.FACIAL_PLEASURE and not window.FACIAL_AROUSAL and not window.FACIAL_DOMINANCE and not window.POSE_DOMINANCE:
                bottomHalf = False
            if not topHalf and not bottomHalf:
                window.hlineWidgetColtoF.toggleColor()
        
            window.hlineWidgettoCol4.toggleColor()
            if not topHalf:
                window.collectorLine6to7_4.toggleColor()
                return
    
    def turnOn():
        #LeftSide
        window.rounded6_4.toggleColor()
        if not window.SENTIMENT_LOOP:
            SentimentClick(window)
        window.horLineWidgetSertoVer.toggleColor()
        window.verlineWidgetSertoP.toggleColor()
        window.hlineWidgetVertoP.toggleColor()

        #Right side
        topHalf = True
        bottomHalf = True
        if window.FUSION_LOOP:
            if not window.PARA_PLEASURE and not window.PARA_AROUSAL and not window.PARA_DOMINANCE:
                topHalf = False
            if not window.FACIAL_PLEASURE and not window.FACIAL_AROUSAL and not window.FACIAL_DOMINANCE and not window.POSE_DOMINANCE:
                bottomHalf = False
            if not topHalf and not bottomHalf:
                window.hlineWidgetColtoF.toggleColor()
        
            window.hlineWidgettoCol4.toggleColor()
            if not topHalf:
                window.collectorLine6to7_4.toggleColor()
                return
    
    if window.SENT_PLEASURE:
        window.SENT_PLEASURE = False
        turnOff()
    else:
        window.SENT_PLEASURE = True
        turnOn()

####################################### Bottom Half (Camera Input) ##########################################

def WebcamClick(window):
    """Implements the click event for the webcam widget"""
    if window.CAMERA:
        window.CAMERA = False
        if window.CAMERA_LOOP:
            VideoClick(window)
    else:
        window.CAMERA = True
    window.circle2_2.toggleColor()

def VideoClick(window):
    """Implements the click event for the video widget"""
    def turnOff():
        #BackTracking
        if window.FACE_TRACKING_LOOP:
            FaceTrackingClick(window)
        if window.FACIAL_EXPRESSION_LOOP:
            FacialExpressionClick(window)
        if window.SKELETON_LOOP:
            SkeletonClick(window)
        
        window.rounded3_3.toggleColor()
        window.hlineWidgetCamtoVer.toggleColor()
        window.verlineWidgetCamToVideo.toggleColor()
        window.hlineWidgetVertoVideo.toggleColor()
    
    def turnOn():
        window.rounded3_3.toggleColor()
        window.hlineWidgetCamtoVer.toggleColor()
        window.verlineWidgetCamToVideo.toggleColor()
        window.hlineWidgetVertoVideo.toggleColor()
        if not window.CAMERA:
            WebcamClick(window)

    if window.CAMERA_LOOP:
        window.CAMERA_LOOP = False
        turnOff()
    else:
        window.CAMERA_LOOP = True
        turnOn()

def FaceTrackingClick(window):
    """Implements the click event for the face tracking widget"""
    def turnOff():
        window.rounded4_2.toggleColor()
        window.verlineWidgetVideotoFace.toggleColor()
        window.hlineWidgetVideotoFace.toggleColor()
        if window.FACIAL_EXPRESSION_LOOP:
            window.verlineWidgetFacetoFacial.toggleColor()
            window.hlineWidgetFacetoFacial.toggleColor()
        if not window.FACIAL_EXPRESSION_LOOP:
            window.hlineWidgetVideotoFacial1.toggleColor()
        
    def turnOn():
        window.rounded4_2.toggleColor()
        window.verlineWidgetVideotoFace.toggleColor()
        window.hlineWidgetVideotoFace.toggleColor()
        if not window.CAMERA_LOOP:
            VideoClick(window)
        if not window.FACIAL_EXPRESSION_LOOP:
            window.hlineWidgetVideotoFacial1.toggleColor()
        if window.FACIAL_EXPRESSION_LOOP:
            window.verlineWidgetFacetoFacial.toggleColor()
            window.hlineWidgetFacetoFacial.toggleColor()
        
    if window.FACE_TRACKING_LOOP:
        window.FACE_TRACKING_LOOP = False
        turnOff()
    else:
        window.FACE_TRACKING_LOOP = True
        turnOn()

def FacialExpressionClick(window):
    """Implements the click event for the facial expression widget"""
    def turnOff():
        #BackTracking
        if window.FACIAL_PLEASURE:
            FacialPleasureClick(window)
        if window.FACIAL_AROUSAL:
            FacialArousalClick(window)
        if window.FACIAL_DOMINANCE:
            FacialDominanceClick(window)

        window.circle5_3_inner.toggleColor()
        window.hlineWidgetVideotoFacial2.toggleColor()
        if not window.FACE_TRACKING_LOOP:
            window.hlineWidgetVideotoFacial1.toggleColor()
        if window.FACE_TRACKING_LOOP:
            window.verlineWidgetFacetoFacial.toggleColor()
            window.hlineWidgetFacetoFacial.toggleColor()
        
    def turnOn():
        window.circle5_3_inner.toggleColor()
        window.hlineWidgetVideotoFacial2.toggleColor()
        if not window.FACE_TRACKING_LOOP:
            window.hlineWidgetVideotoFacial1.toggleColor()
        if window.FACE_TRACKING_LOOP:
            window.verlineWidgetFacetoFacial.toggleColor()
            window.hlineWidgetFacetoFacial.toggleColor()
        if not window.CAMERA_LOOP:
            VideoClick(window)
    
    if window.FACIAL_EXPRESSION_LOOP:
        window.FACIAL_EXPRESSION_LOOP = False
        turnOff()
    else:
        window.FACIAL_EXPRESSION_LOOP = True
        turnOn()
    #Rest

def FacialPleasureClick(window):
    """Implements the click event for the facial expression pleasure widget"""
    def turnOff():
        #Left side
        window.rounded6_5.toggleColor()
        window.hline1fromCol5to6_2.toggleColor()
        if not window.FACIAL_AROUSAL and not window.FACIAL_DOMINANCE:
            window.collectorLine5to6_2.toggleColor()
            window.hlinetoCol5to6_2.toggleColor()

        #Right side
        topHalf = True
        bottomHalf = True
        if window.FUSION_LOOP:
            if not window.PARA_PLEASURE and not window.PARA_AROUSAL and not window.PARA_DOMINANCE and not window.SENT_PLEASURE:
                topHalf = False
            if not window.FACIAL_AROUSAL and not window.FACIAL_DOMINANCE and not window.POSE_DOMINANCE:
                bottomHalf = False
            if not topHalf and not bottomHalf:
                window.hlineWidgetColtoF.toggleColor()
        
            window.hlineWidgettoCol5.toggleColor()
            if not bottomHalf:
                window.collectorLine6to7_5.toggleColor()
                return
    
    def turnOn():
        #Left Side
        window.rounded6_5.toggleColor()
        window.hline1fromCol5to6_2.toggleColor()
        if not window.FACIAL_AROUSAL and not window.FACIAL_DOMINANCE:
            window.collectorLine5to6_2.toggleColor()
            window.hlinetoCol5to6_2.toggleColor()
        if not window.FACIAL_EXPRESSION_LOOP:
            FacialExpressionClick(window)
        
        #Right side
        topHalf = True
        bottomHalf = True
        if window.FUSION_LOOP:
            if not window.PARA_PLEASURE and not window.PARA_AROUSAL and not window.PARA_DOMINANCE and not window.SENT_PLEASURE:
                topHalf = False
            if not window.FACIAL_AROUSAL and not window.FACIAL_DOMINANCE and not window.POSE_DOMINANCE:
                bottomHalf = False
            if not topHalf and not bottomHalf:
                window.hlineWidgetColtoF.toggleColor()
        
            window.hlineWidgettoCol5.toggleColor()
            if not bottomHalf:
                window.collectorLine6to7_5.toggleColor()
                return
    
    if window.FACIAL_PLEASURE:
        window.FACIAL_PLEASURE = False
        turnOff()
    else:
        window.FACIAL_PLEASURE = True
        turnOn()

def FacialArousalClick(window):
    """Implements the click event for the facial expression arousal widget"""
    def turnOff():
        #Left Side
        window.rounded6_6.toggleColor()
        window.hline2fromCol5to6_2.toggleColor()
        if not window.FACIAL_PLEASURE and not window.FACIAL_DOMINANCE:
            window.collectorLine5to6_2.toggleColor()
            window.hlinetoCol5to6_2.toggleColor()
        if not window.FACIAL_DOMINANCE:
            window.collectorLine5to6_2_2.toggleColor()

        #Right side
        topHalf = True
        bottomHalf = True
        if window.FUSION_LOOP:
            if not window.PARA_PLEASURE and not window.PARA_AROUSAL and not window.PARA_DOMINANCE and not window.SENT_PLEASURE:
                topHalf = False
            if not window.FACIAL_PLEASURE and not window.FACIAL_DOMINANCE and not window.POSE_DOMINANCE:
                bottomHalf = False
            if not topHalf and not bottomHalf:
                window.hlineWidgetColtoF.toggleColor()
        
            window.hlineWidgettoCol6.toggleColor()
            if not bottomHalf:
                window.collectorLine6to7_6.toggleColor()
                window.collectorLine6to7_5.toggleColor()
                return
            if not window.POSE_DOMINANCE and not window.FACIAL_DOMINANCE:
                window.collectorLine6to7_6.toggleColor()
    
    def turnOn():
        #Left Side
        window.rounded6_6.toggleColor()
        window.hline2fromCol5to6_2.toggleColor()
        if not window.FACIAL_PLEASURE and not window.FACIAL_DOMINANCE:
            window.collectorLine5to6_2.toggleColor()
            window.hlinetoCol5to6_2.toggleColor()
        if not window.FACIAL_DOMINANCE:
            window.collectorLine5to6_2_2.toggleColor()
        if not window.FACIAL_EXPRESSION_LOOP:
            FacialExpressionClick(window)

        #Right side
        topHalf = True
        bottomHalf = True
        if window.FUSION_LOOP:
            if not window.PARA_PLEASURE and not window.PARA_AROUSAL and not window.PARA_DOMINANCE and not window.SENT_PLEASURE:
                topHalf = False
            if not window.FACIAL_PLEASURE and not window.FACIAL_DOMINANCE and not window.POSE_DOMINANCE:
                bottomHalf = False
            if not topHalf and not bottomHalf:
                window.hlineWidgetColtoF.toggleColor()
        
            window.hlineWidgettoCol6.toggleColor()
            if not bottomHalf:
                window.collectorLine6to7_6.toggleColor()
                window.collectorLine6to7_5.toggleColor()
                return
            if not window.POSE_DOMINANCE and not window.FACIAL_DOMINANCE:
                window.collectorLine6to7_6.toggleColor()
    
    if window.FACIAL_AROUSAL:
        window.FACIAL_AROUSAL = False
        turnOff()
    else:
        window.FACIAL_AROUSAL = True
        turnOn()

def FacialDominanceClick(window):
    """Implements the click event for the facial expression dominance widget"""
    def turnOff():
        #Left side
        window.rounded6_7.toggleColor()
        window.hline3fromCol5to6_2.toggleColor()
        window.collectorLine5to6_2_3.toggleColor()
        if not window.FACIAL_PLEASURE and not window.FACIAL_AROUSAL:
            window.collectorLine5to6_2.toggleColor()
            window.hlinetoCol5to6_2.toggleColor()
        if not window.FACIAL_AROUSAL:
            window.collectorLine5to6_2_2.toggleColor()

        #Right side
        topHalf = True
        bottomHalf = True
        if window.FUSION_LOOP:
            if not window.PARA_PLEASURE and not window.PARA_AROUSAL and not window.PARA_DOMINANCE and not window.SENT_PLEASURE:
                topHalf = False
            if not window.FACIAL_PLEASURE and not window.FACIAL_AROUSAL and not window.POSE_DOMINANCE:
                bottomHalf = False
            if not topHalf and not bottomHalf:
                window.hlineWidgetColtoF.toggleColor()
        
            window.hlineWidgettoCol7.toggleColor()
            if not bottomHalf:
                window.collectorLine6to7_7.toggleColor()
                window.collectorLine6to7_6.toggleColor()
                window.collectorLine6to7_5.toggleColor()
                return
            if not window.POSE_DOMINANCE:
                window.collectorLine6to7_7.toggleColor()
                if not window.FACIAL_AROUSAL:
                    window.collectorLine6to7_6.toggleColor()
                    return
    
    def turnOn():
        #Left side
        window.rounded6_7.toggleColor()
        window.hline3fromCol5to6_2.toggleColor()
        window.collectorLine5to6_2_3.toggleColor()
        if not window.FACIAL_PLEASURE and not window.FACIAL_AROUSAL:
            window.collectorLine5to6_2.toggleColor()
            window.hlinetoCol5to6_2.toggleColor()
        if not window.FACIAL_AROUSAL:
            window.collectorLine5to6_2_2.toggleColor()
        if not window.FACIAL_EXPRESSION_LOOP:
            FacialExpressionClick(window)

        #Right side
        topHalf = True
        bottomHalf = True
        if window.FUSION_LOOP:
            if not window.PARA_PLEASURE and not window.PARA_AROUSAL and not window.PARA_DOMINANCE and not window.SENT_PLEASURE:
                topHalf = False
            if not window.FACIAL_PLEASURE and not window.FACIAL_AROUSAL and not window.POSE_DOMINANCE:
                bottomHalf = False
            if not topHalf and not bottomHalf:
                window.hlineWidgetColtoF.toggleColor()
        
            window.hlineWidgettoCol7.toggleColor()
            if not bottomHalf:
                window.collectorLine6to7_7.toggleColor()
                window.collectorLine6to7_6.toggleColor()
                window.collectorLine6to7_5.toggleColor()
                return
            if not window.POSE_DOMINANCE:
                window.collectorLine6to7_7.toggleColor()
                if not window.FACIAL_AROUSAL:
                    window.collectorLine6to7_6.toggleColor()
                    return

    if window.FACIAL_DOMINANCE:
        window.FACIAL_DOMINANCE = False
        turnOff()
    else:
        window.FACIAL_DOMINANCE = True
        turnOn()

def SkeletonClick(window):
    """Implements the click event for the skeleton widget"""
    def turnOff():
        if window.BODY_TRACKING_LOOP:
            BodyTrackingClick(window)
        if window.POSE_LOOP:
            PoseClick(window)

        window.rounded3_4.toggleColor()
        window.verlineWidgetVideotoSkel.toggleColor()
    
    def turnOn():
        window.rounded3_4.toggleColor()
        window.verlineWidgetVideotoSkel.toggleColor()
        if not window.CAMERA_LOOP:
            VideoClick(window)
    
    if window.SKELETON_LOOP:
        window.SKELETON_LOOP = False
        turnOff()
    else:
        window.SKELETON_LOOP = True
        turnOn()

def BodyTrackingClick(window):
    """Implements the click event for the body tracking widget"""
    def turnOff():
        #BackTracking
        # if window.POSE_LOOP:
        #     PoseClick(window)

        window.rounded4_3.toggleColor()
        window.hlineWidgetSkeltoBody.toggleColor()
        window.verlineWidgetSkeltoBody.toggleColor()
        if window.POSE_LOOP:
            window.verlineWidgetBodytoPose.toggleColor()
            window.hlineWidgetBodytoPose.toggleColor()
        if not window.POSE_LOOP:
            window.hlineWidgetSkeltoPose.toggleColor()
    
    def turnOn():
        window.rounded4_3.toggleColor()
        window.hlineWidgetSkeltoBody.toggleColor()
        window.verlineWidgetSkeltoBody.toggleColor()
        if not window.SKELETON_LOOP:
            SkeletonClick(window)
        if not window.POSE_LOOP:
            window.hlineWidgetSkeltoPose.toggleColor()
        if window.POSE_LOOP:
            window.verlineWidgetBodytoPose.toggleColor()
            window.hlineWidgetBodytoPose.toggleColor()
    
    if window.BODY_TRACKING_LOOP:
        window.BODY_TRACKING_LOOP = False
        turnOff()
    else:
        window.BODY_TRACKING_LOOP = True
        turnOn()

def PoseClick(window):
    """Implements the click event for the pose widget"""
    def turnOff():
        #BackTracking
        if window.POSE_DOMINANCE:
            PoseDominanceClick(window)

        window.circle5_4_inner.toggleColor()
        window.hlineWidgetSkeltoPose2.toggleColor()
        if not window.BODY_TRACKING_LOOP:
            window.hlineWidgetSkeltoPose.toggleColor()
        if window.BODY_TRACKING_LOOP:
            window.verlineWidgetBodytoPose.toggleColor()
            window.hlineWidgetBodytoPose.toggleColor()
    
    def turnOn():
        window.circle5_4_inner.toggleColor()
        window.hlineWidgetSkeltoPose2.toggleColor()
        if not window.SKELETON_LOOP:
            SkeletonClick(window)
        if not window.BODY_TRACKING_LOOP:
            window.hlineWidgetSkeltoPose.toggleColor()
        if window.BODY_TRACKING_LOOP:
            window.verlineWidgetBodytoPose.toggleColor()
            window.hlineWidgetBodytoPose.toggleColor() 

    if window.POSE_LOOP:
        window.POSE_LOOP = False
        turnOff()
    else:
        window.POSE_LOOP = True
        turnOn()

def PoseDominanceClick(window):
    """Implements the click event for the pose-dominance widget"""
    def turnOff():
        #Left side
        window.rounded6_8.toggleColor()
        window.hLineWidgetPosetoVer.toggleColor()
        window.verlineWidgetPosetoD.toggleColor()
        window.hlineWidgetVertoD.toggleColor()

        #right side
        topHalf = True
        bottomHalf = True
        if window.FUSION_LOOP:
            if not window.PARA_PLEASURE and not window.PARA_AROUSAL and not window.PARA_DOMINANCE and not window.SENT_PLEASURE:
                topHalf = False
            if not window.FACIAL_PLEASURE and not window.FACIAL_AROUSAL and not window.FACIAL_DOMINANCE:
                bottomHalf = False
            if not topHalf and not bottomHalf:
                window.hlineWidgetColtoF.toggleColor()
            
            if not bottomHalf:
                window.collectorLine6to7_8.toggleColor()
                window.collectorLine6to7_7.toggleColor()
                window.collectorLine6to7_6.toggleColor()
                window.collectorLine6to7_5.toggleColor()
                window.hlineWidgettoCol8.toggleColor()
                return
            if not window.FACIAL_DOMINANCE:
                window.collectorLine6to7_8.toggleColor()
                window.collectorLine6to7_7.toggleColor()
                window.hlineWidgettoCol8.toggleColor()
                if not window.FACIAL_AROUSAL:
                    window.collectorLine6to7_6.toggleColor()
                    return
                else:
                    return
            else:
                window.collectorLine6to7_8.toggleColor()
                window.hlineWidgettoCol8.toggleColor()
    
    def turnOn():
        #Left side
        window.rounded6_8.toggleColor()
        window.hLineWidgetPosetoVer.toggleColor()
        window.verlineWidgetPosetoD.toggleColor()
        window.hlineWidgetVertoD.toggleColor()
        if not window.POSE_LOOP:
            PoseClick(window)
        
        #Right side
        topHalf = True
        bottomHalf = True
        if window.FUSION_LOOP:
            if not window.PARA_PLEASURE and not window.PARA_AROUSAL and not window.PARA_DOMINANCE and not window.SENT_PLEASURE:
                topHalf = False
            if not window.FACIAL_PLEASURE and not window.FACIAL_AROUSAL and not window.FACIAL_DOMINANCE:
                bottomHalf = False
            if not topHalf and not bottomHalf:
                window.hlineWidgetColtoF.toggleColor()
            
            if not bottomHalf:
                window.collectorLine6to7_8.toggleColor()
                window.collectorLine6to7_7.toggleColor()
                window.collectorLine6to7_6.toggleColor()
                window.collectorLine6to7_5.toggleColor()
                window.hlineWidgettoCol8.toggleColor()
                return
            if not window.FACIAL_DOMINANCE:
                window.collectorLine6to7_8.toggleColor()
                window.collectorLine6to7_7.toggleColor()
                window.hlineWidgettoCol8.toggleColor()
                if not window.FACIAL_AROUSAL:
                    window.collectorLine6to7_6.toggleColor()
                    return
                else:
                    return
            else:
                window.collectorLine6to7_8.toggleColor()
                window.hlineWidgettoCol8.toggleColor()
            
    if window.POSE_DOMINANCE:
        window.POSE_DOMINANCE = False
        turnOff()
    else:
        window.POSE_DOMINANCE = True
        turnOn()

####################################### Fusion Part #######################################################
    
def FusionClick(window):
    """Implements the click event for the fusion widget"""
    def turnOff():
        #BackTrack
        if window.PLEASURE:
            PleasureClick(window)
        if window.AROUSAL:
            ArousalClick(window)
        if window.DOMINANCE:
            DominanceClick(window)
            
        topHalf = True
        bottomHalf = True
        window.rounded7.toggleColor()
        if not window.PARA_PLEASURE and not window.PARA_AROUSAL and not window.PARA_DOMINANCE and not window.SENT_PLEASURE:
            topHalf = False
        if not window.FACIAL_PLEASURE and not window.FACIAL_AROUSAL and not window.FACIAL_DOMINANCE and not window.POSE_DOMINANCE:
            bottomHalf = False
        if not topHalf and not bottomHalf:
            return
        window.hlineWidgetColtoF.toggleColor()

        if topHalf:
            window.collectorLine6to7_4.toggleColor()
            if window.PARA_PLEASURE:
                window.collectorLine6to7_1.toggleColor()
                window.collectorLine6to7_2.toggleColor()
                window.collectorLine6to7_3.toggleColor()
                window.hlineWidgettoCol1.toggleColor()
            if window.PARA_AROUSAL and not window.PARA_PLEASURE:
                window.collectorLine6to7_2.toggleColor()
                window.collectorLine6to7_3.toggleColor()
            if window.PARA_DOMINANCE and not window.PARA_PLEASURE and not window.PARA_AROUSAL:
                window.collectorLine6to7_3.toggleColor()
            if window.PARA_AROUSAL:
                window.hlineWidgettoCol2.toggleColor()
            if window.PARA_DOMINANCE:
                window.hlineWidgettoCol3.toggleColor()
            if window.SENT_PLEASURE:
                window.hlineWidgettoCol4.toggleColor()

        if bottomHalf:
            window.collectorLine6to7_5.toggleColor()
            if window.POSE_DOMINANCE:
                window.collectorLine6to7_6.toggleColor()
                window.collectorLine6to7_7.toggleColor()
                window.collectorLine6to7_8.toggleColor()
                window.hlineWidgettoCol8.toggleColor()
            if window.FACIAL_DOMINANCE and not window.POSE_DOMINANCE:
                window.collectorLine6to7_6.toggleColor()
                window.collectorLine6to7_7.toggleColor()
            if window.FACIAL_AROUSAL and not window.FACIAL_DOMINANCE and not window.POSE_DOMINANCE:
                window.collectorLine6to7_6.toggleColor()
            if window.FACIAL_DOMINANCE:
                window.hlineWidgettoCol7.toggleColor()
            if window.FACIAL_AROUSAL:
                window.hlineWidgettoCol6.toggleColor()
            if window.FACIAL_PLEASURE:
                window.hlineWidgettoCol5.toggleColor()

    def turnOn():
        topHalf = True
        bottomHalf = True
        window.rounded7.toggleColor()
        if not window.PARA_PLEASURE and not window.PARA_AROUSAL and not window.PARA_DOMINANCE and not window.SENT_PLEASURE:
            topHalf = False
        if not window.FACIAL_PLEASURE and not window.FACIAL_AROUSAL and not window.FACIAL_DOMINANCE and not window.POSE_DOMINANCE:
            bottomHalf = False
        if not topHalf and not bottomHalf:
            return
        window.hlineWidgetColtoF.toggleColor()

        if topHalf:
            window.collectorLine6to7_4.toggleColor()
            if window.PARA_PLEASURE:
                window.collectorLine6to7_1.toggleColor()
                window.collectorLine6to7_2.toggleColor()
                window.collectorLine6to7_3.toggleColor()
                window.hlineWidgettoCol1.toggleColor()
            if window.PARA_AROUSAL and not window.PARA_PLEASURE:
                window.collectorLine6to7_2.toggleColor()
                window.collectorLine6to7_3.toggleColor()
            if window.PARA_DOMINANCE and not window.PARA_PLEASURE and not window.PARA_AROUSAL:
                window.collectorLine6to7_3.toggleColor()
            if window.PARA_AROUSAL:
                window.hlineWidgettoCol2.toggleColor()
            if window.PARA_DOMINANCE:
                window.hlineWidgettoCol3.toggleColor()
            if window.SENT_PLEASURE:
                window.hlineWidgettoCol4.toggleColor()

        if bottomHalf:
            window.collectorLine6to7_5.toggleColor()
            if window.POSE_DOMINANCE:
                window.collectorLine6to7_6.toggleColor()
                window.collectorLine6to7_7.toggleColor()
                window.collectorLine6to7_8.toggleColor()
                window.hlineWidgettoCol8.toggleColor()
            if window.FACIAL_DOMINANCE and not window.POSE_DOMINANCE:
                window.collectorLine6to7_6.toggleColor()
                window.collectorLine6to7_7.toggleColor()
            if window.FACIAL_AROUSAL and not window.FACIAL_DOMINANCE and not window.POSE_DOMINANCE:
                window.collectorLine6to7_6.toggleColor()
            if window.FACIAL_DOMINANCE:
                window.hlineWidgettoCol7.toggleColor()
            if window.FACIAL_AROUSAL:
                window.hlineWidgettoCol6.toggleColor()
            if window.FACIAL_PLEASURE:
                window.hlineWidgettoCol5.toggleColor()
        
    if window.FUSION_LOOP:
        window.FUSION_LOOP = False
        turnOff()
    else:
        window.FUSION_LOOP = True
        turnOn()

def PleasureClick(window):
    """Implements the click event for the pleasure widget"""
    def turnOff():
        window.rounded8_1.toggleColor()
        window.vlineWidgetFtoP.toggleColor()
        window.hlineWidgetFtoP.toggleColor()
        if not window.AROUSAL and not window.DOMINANCE:
            window.hlineWidgetFtoA1.toggleColor()

    def turnOn():
        window.rounded8_1.toggleColor()
        window.vlineWidgetFtoP.toggleColor()
        window.hlineWidgetFtoP.toggleColor()
        if not window.AROUSAL and not window.DOMINANCE:
            window.hlineWidgetFtoA1.toggleColor()
        if not window.FUSION_LOOP:
            FusionClick(window)
    
    if window.PLEASURE:
        window.PLEASURE = False
        turnOff()
    else:
        window.PLEASURE = True
        turnOn()

def ArousalClick(window):
    """Implements the click event for the arousal widget"""
    def turnOff():
        window.rounded8_2.toggleColor()
        window.hlineWidgetFtoA2.toggleColor()
        if not window.PLEASURE and not window.DOMINANCE:
            window.hlineWidgetFtoA1.toggleColor()

    def turnOn():
        window.rounded8_2.toggleColor()
        window.hlineWidgetFtoA2.toggleColor()
        if not window.PLEASURE and not window.DOMINANCE:
            window.hlineWidgetFtoA1.toggleColor()
        if not window.FUSION_LOOP:
            FusionClick(window)
    
    if window.AROUSAL:
        window.AROUSAL = False
        turnOff()
    else:
        window.AROUSAL = True
        turnOn()

def DominanceClick(window):
    """Implements the click event for the dominance widget"""
    def turnOff():
        window.rounded8_3.toggleColor()
        window.hlineWidgetFtoD.toggleColor()
        window.vlineWidgetFtoD.toggleColor()
        if not window.PLEASURE and not window.AROUSAL:
            window.hlineWidgetFtoA1.toggleColor()

    def turnOn():
        window.rounded8_3.toggleColor()
        window.hlineWidgetFtoD.toggleColor()
        window.vlineWidgetFtoD.toggleColor()
        if not window.PLEASURE and not window.AROUSAL:
            window.hlineWidgetFtoA1.toggleColor()
        if not window.FUSION_LOOP:
            FusionClick(window)
    
    if window.DOMINANCE:
        window.DOMINANCE = False
        turnOff()
    else:
        window.DOMINANCE = True
        turnOn()

####################################### Buttons #######################################################

def PlayButtonClick(window):
    """Implements the click event for the play button that starts the AffectPipeline"""
    window.pipe = AffectPipeline(enable_log_to_console=True,
                      enable_vad_loop=window.VOICE_ACTIVITY_LOOP,
                      enable_ser_loop=window.PARA_LOOP,
                      enable_stt_loop=window.TRANSCRIPT_LOOP,
                      enable_camera_loop=window.CAMERA_LOOP,
                      enable_print_loop=True,
                      enable_send_udp_loop=window.UDP,
                      enable_send_kafka_loop=window.KAFKA,
                      enable_face_er_loop= window.FACIAL_EXPRESSION_LOOP,
                      enable_face_mesh_loop=False,
                      enable_pose_loop=window.SKELETON_LOOP,
                      enable_fusion_loop=window.FUSION_LOOP,
                      enable_sentiment_loop=window.SENTIMENT_LOOP,
                      show_face_mesh=False,
                      face_mesh_show_face_edges=False,
                      face_mesh_show_face_pupils=False,
                      face_mesh_show_face_contour=False,
                      camera_id=window.CAM_ID,
                      ser_loop_rate=window.SER_LOOP_RATE,
                      stt_loop_rate=window.STT_LOOP_RATE,
                      sentiment_loop_rate=window.SENTIMENT_LOOP_RATE,
                      vad_loop_rate=window.VAD_LOOP_RATE,
                      er_loop_rate=window.ER_LOOP_RATE,
                      pose_loop_rate=window.POSE_LOOP_RATE,
                      fusion_loop_rate=window.FUSION_LOOP_RATE,
                      send_loop_rate=window.SEND_LOOP_RATE,
                      camera_loop_rate=window.CAMERA_LOOP_RATE,
                      logging_loop_rate=20.0,
                      face_mesh_rate=window.FACE_MESH_RATE,
                      udp_ip=window.UDP_IP,
                      udp_port=window.UDP_PORT,
                      kafka_ip=window.KAFKA_IP,
                      kafka_port=window.KAFKA_PORT,
                      kafka_topic_name=window.KAFKA_TOPIC,
                      sample_rate=window.SAMPLE_RATE,
                      vad_threshold=window.VAD_THRESHOLD,
                      face_padding=0.2,
                      microphone_chunks=16000,
                      microphone_id=window.MIC_ID,
                      stt_window_length=window.STT_WINDOW_SIZE,
                      stt_model_size="small",
                      sentiment_model="germansentiment")
    window.START = False # This is set to true when the pipeline is actually started
    
    #Check whether or not certain widgets are enabled
    if window.CAMERA_LOOP:
        window.image = ImageWindow(window=window)
        window.image.setParent(window.bodyContainer)
        window.image.show()
    if window.MIC_LOOP:
        window.audio = PlotWidget(window=window)
        window.audio.setParent(window.bodyContainer)
        window.audio.show()
        window.audio.playButtonClicked()
    if window.TRANSCRIPT_LOOP:
        window.transcript = TranscriptWidget(window=window)
        window.transcript.setParent(window.bodyContainer)
        window.transcript.show()
    if window.SKELETON_LOOP:
        window.skeleton = ImageWindow(window=window, name="Skeleton")
        window.skeleton.setParent(window.bodyContainer)
        window.skeleton.show()
    if window.VOICE_ACTIVITY_LOOP:
        window.circle4_1.window = window
        window.circle4_1.name = "Voice_Activity"
    if window.FACE_TRACKING_LOOP:
        window.circle4_2.window = window
        window.circle4_2.name = "Face_Tracking"
    if window.BODY_TRACKING_LOOP:
        window.circle4_3.window = window
        window.circle4_3.name = "Body_Tracking"
    if window.PARA_PLEASURE:
        window.para_pleasure = FloatWidget(name="Para_Pleasure")
        window.para_pleasure.setParent(window.bodyContainer)
        window.para_pleasure.setFixedSize(window.rounded6_1.width(), window.rounded6_1.height())
        window.para_pleasure.move(
            window.rounded6_1.x(),
            window.rounded6_1.y()
        )
        window.para_pleasure.show()
    if window.PARA_AROUSAL:
        window.para_arousal = FloatWidget(name="Para_Arousal")
        window.para_arousal.setParent(window.bodyContainer)
        window.para_arousal.setFixedSize(window.rounded6_2.width(), window.rounded6_2.height())
        window.para_arousal.move(
            window.rounded6_2.x(),
            window.rounded6_2.y()
        )
        window.para_arousal.show()    
    if window.PARA_DOMINANCE:
        window.para_dominance = FloatWidget(name="Para_Dominance")
        window.para_dominance.setParent(window.bodyContainer)
        window.para_dominance.setFixedSize(window.rounded6_3.width(), window.rounded6_3.height())
        window.para_dominance.move(
            window.rounded6_3.x(),
            window.rounded6_3.y()
        )
        window.para_dominance.show()
    if window.SENT_PLEASURE:
        window.sent_pleasure = FloatWidget(name="Sent_Pleasure")
        window.sent_pleasure.setParent(window.bodyContainer)
        window.sent_pleasure.setFixedSize(window.rounded6_4.width(), window.rounded6_4.height())
        window.sent_pleasure.move(
            window.rounded6_4.x(),
            window.rounded6_4.y()
        )
        window.sent_pleasure.show()
    if window.FACIAL_PLEASURE:
        window.facial_pleasure = FloatWidget(name="Facial_Pleasure")
        window.facial_pleasure.setParent(window.bodyContainer)
        window.facial_pleasure.setFixedSize(window.rounded6_5.width(), window.rounded6_5.height())
        window.facial_pleasure.move(
           window.rounded6_5.x(),
            window.rounded6_5.y()
        )
        window.facial_pleasure.show()
    if window.FACIAL_AROUSAL:
        window.facial_arousal = FloatWidget(name="Facial_Arousal")
        window.facial_arousal.setParent(window.bodyContainer)
        window.facial_arousal.setFixedSize(window.rounded6_6.width(), window.rounded6_6.height())
        window.facial_arousal.move(
            window.rounded6_6.x(),
            window.rounded6_6.y()
        )
        window.facial_arousal.show()
    if window.FACIAL_DOMINANCE:
        window.facial_dominance = FloatWidget(name="Facial_Dominance")
        window.facial_dominance.setParent(window.bodyContainer)
        window.facial_dominance.setFixedSize(window.rounded6_7.width(), window.rounded6_7.height())
        window.facial_dominance.move(
           window.rounded6_7.x(),
            window.rounded6_7.y()
        )
        window.facial_dominance.show()
    if window.POSE_DOMINANCE:
        window.pose_dominance = FloatWidget(name="Pose_Dominance")
        window.pose_dominance.setParent(window.bodyContainer)
        window.pose_dominance.setFixedSize(window.rounded6_8.width(), window.rounded6_8.height())
        window.pose_dominance.move(
            window.rounded6_8.x(),
            window.rounded6_8.y()
        )
        window.pose_dominance.show()
    if window.PLEASURE:
        window.pleasure = FloatWidget(name="Pleasure")
        window.pleasure.setParent(window.bodyContainer)
        window.pleasure.setFixedSize(window.rounded8_1.width(), window.rounded8_1.height())
        window.pleasure.move(
            window.rounded8_1.x(),
            window.rounded8_1.y()
        )
        window.pleasure.show()
    if window.AROUSAL:
        window.arousal = FloatWidget(name="Arousal")
        window.arousal.setParent(window.bodyContainer)
        window.arousal.setFixedSize(window.rounded8_2.width(), window.rounded8_2.height())
        window.arousal.move(
            window.rounded8_2.x(),
            window.rounded8_2.y()
        )
        window.arousal.show()
    if window.DOMINANCE:
        window.dominance = FloatWidget(name="Dominance")
        window.dominance.setParent(window.bodyContainer)
        window.dominance.setFixedSize(window.rounded8_3.width(), window.rounded8_3.height())
        window.dominance.move(
           window.rounded8_3.x(),
            window.rounded8_3.y()
        )
        window.dominance.show()
    window.pipe.start(window)

def StopButtonClick(window):
    """Implements the click event for the stop button that stops the AffectPipeline"""
    
    window.pipe.stop()
    layout = window.bodyContainer.layout()
    #Check if widgets are enabled and remove them if they are
    if window.image is not None:
        layout.removeWidget(window.image)
        window.image.setParent(None)
        del window.image
        
    if window.audio is not None:
        layout.removeWidget(window.audio)
        window.audio.setParent(None)
        del window.audio
        
    if window.transcript is not None:
        layout.removeWidget(window.transcript)
        window.transcript.setParent(None)
        del window.transcript
        
    if window.skeleton is not None:
        layout.removeWidget(window.skeleton)
        window.skeleton.setParent(None)
        del window.skeleton
        
    if window.VOICE_ACTIVITY_LOOP:
        window.circle4_1.window = None
        window.circle4_1.name = ""
        window.circle4_1.color = window.circle4_1.baseColor
        window.circle4_1.update()
        
    if window.FACE_TRACKING_LOOP:
        window.circle4_2.window = None
        window.circle4_2.name = ""
        window.circle4_2.color = window.circle4_2.baseColor
        window.circle4_2.update()
        
    if window.BODY_TRACKING_LOOP:
        window.circle4_3.window = None
        window.circle4_3.name = ""
        window.circle4_3.color = window.circle4_3.baseColor
        window.circle4_3.update()
        
    if window.PARA_PLEASURE:
        layout.removeWidget(window.para_pleasure)
        window.para_pleasure.setParent(None)
        del window.para_pleasure
        
    if window.PARA_AROUSAL:
        layout.removeWidget(window.para_arousal)
        window.para_arousal.setParent(None)
        del window.para_arousal
        
    if window.PARA_DOMINANCE:
        layout.removeWidget(window.para_dominance)
        window.para_dominance.setParent(None)
        del window.para_dominance
        
    if window.SENT_PLEASURE:
        layout.removeWidget(window.sent_pleasure)
        window.sent_pleasure.setParent(None)
        del window.sent_pleasure
        
    if window.FACIAL_PLEASURE:
        layout.removeWidget(window.facial_pleasure)
        window.facial_pleasure.setParent(None)
        del window.facial_pleasure
        
    if window.FACIAL_AROUSAL:
        layout.removeWidget(window.facial_arousal)
        window.facial_arousal.setParent(None)
        del window.facial_arousal
        
    if window.FACIAL_DOMINANCE:
        layout.removeWidget(window.facial_dominance)
        window.facial_dominance.setParent(None)
        del window.facial_dominance
        
    if window.POSE_DOMINANCE:
        layout.removeWidget(window.pose_dominance)
        window.pose_dominance.setParent(None)
        del window.pose_dominance
        
    if window.PLEASURE:
        layout.removeWidget(window.pleasure)
        window.pleasure.setParent(None)
        del window.pleasure
        
    if window.AROUSAL:
        layout.removeWidget(window.arousal)
        window.arousal.setParent(None)
        del window.arousal
        
    if window.DOMINANCE:
        layout.removeWidget(window.dominance)
        window.dominance.setParent(None)
        del window.dominance
        
    del window.pipe 
    gc.collect()

def kafkaClick(window):
    """Implements the click event for the kafka button"""

    def turnOn():
        window.kafka_button.setStyleSheet("background-color: green")
    
    def turnOff():
        window.kafka_button.setStyleSheet("background-color: white")

    if window.KAFKA:
        window.KAFKA = False
        turnOff()
    else:
        window.KAFKA = True
        turnOn()

def udpClick(window):
    """Implements the click event for the udp button"""
    def turnOn():
        window.udp_button.setStyleSheet("background-color: green")
    
    def turnOff():
        window.udp_button.setStyleSheet("background-color: white") # f0f0f0

    if window.UDP:
        window.UDP = False
        turnOff()
    else:
        window.UDP = True
        turnOn()

####################################### Connection #######################################################
def connect(window):
    """Connects the click events to the widgets in the GUI"""
    #Upper
    window.circle2_1.clicked.connect(lambda: HeadphonesClick(window)) 
    window.rounded3_1.clicked.connect(lambda: AudioClick(window)) 
    window.rounded3_2.clicked.connect(lambda: TranscriptClick(window))
    window.rounded4_1.clicked.connect(lambda: VoiceActivityClick(window))
    window.circle5_1_inner.clicked.connect(lambda: ParaClick(window))
    window.circle5_2_inner.clicked.connect(lambda: SentimentClick(window))
    window.rounded6_1.clicked.connect(lambda: ParaPleasureClick(window))
    window.rounded6_2.clicked.connect(lambda: ParaArousalClick(window))
    window.rounded6_3.clicked.connect(lambda: ParaDominanceClick(window))
    window.rounded6_4.clicked.connect(lambda: SentimentPleasureClick(window))

    #Lower
    window.circle2_2.clicked.connect(lambda: WebcamClick(window)) 
    window.rounded3_3.clicked.connect(lambda: VideoClick(window))
    window.rounded4_2.clicked.connect(lambda: FaceTrackingClick(window))
    window.circle5_3_inner.clicked.connect(lambda: FacialExpressionClick(window))
    window.rounded6_5.clicked.connect(lambda: FacialPleasureClick(window))
    window.rounded6_6.clicked.connect(lambda: FacialArousalClick(window))
    window.rounded6_7.clicked.connect(lambda: FacialDominanceClick(window))
    window.rounded3_4.clicked.connect(lambda: SkeletonClick(window))
    window.rounded4_3.clicked.connect(lambda: BodyTrackingClick(window))
    window.circle5_4_inner.clicked.connect(lambda: PoseClick(window))
    window.rounded6_8.clicked.connect(lambda: PoseDominanceClick(window))

    #Back
    window.rounded7.clicked.connect(lambda: FusionClick(window))
    window.rounded8_1.clicked.connect(lambda: PleasureClick(window))
    window.rounded8_2.clicked.connect(lambda: ArousalClick(window))
    window.rounded8_3.clicked.connect(lambda: DominanceClick(window))

    #Buttons
    window.kafka_button.leftClicked.connect(lambda: kafkaClick(window))
    window.udp_button.leftClicked.connect(lambda: udpClick(window))
    
    window.play_button.clicked.connect(lambda: PlayButtonClick(window))
    # window.stop_button.clicked.connect(lambda: StopButtonClick(window))