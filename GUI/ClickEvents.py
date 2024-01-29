from modules.AffectPipeline import AffectPipeline, DeviceManager
from GUI.Image_window import ImageWindow
from GUI.rounded_frame import RoundedFrame
from GUI.AudioWidget import PlotWidget
from time import sleep
from PyQt6.QtGui import QColor
from GUI.TranscriptWidget import TranscriptWidget

#Top Half
def headphonesClick(window):
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
    def turnOff():
        if window.VOICE_ACTIVITY_LOOP:
            VoiceActivityClick(window)
        if window.PARA_LOOP:
            ParaClick(window)
        if window.TRANSCRIPT_LOOP:
            TranscriptClick(window)
        window.rounded3_1.toggleColor()
        window.hlineWidgetHeadsettoAudio.toggleColor()
        #Check nachfolger

    def turnOn():
        window.rounded3_1.toggleColor()
        window.hlineWidgetHeadsettoAudio.toggleColor()
        if not window.HEADSET:
            headphonesClick(window)

    if window.MIC_LOOP:
        window.MIC_LOOP = False
        turnOff()
    else:
        window.MIC_LOOP = True
        turnOn()

    

def VoiceActivityClick(window):
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
    #Rest

def ParaClick(window):
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
    #Rest

def ParaPleasureClick(window):
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
    #Rest

def ParaDominanceClick(window):
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
    #Rest

def TranscriptClick(window):

    def turnOn():
        if not window.MIC_LOOP:
            AudioClick(window)
        window.rounded3_2.toggleColor()
        window.verlineWidgetAudioToTra.toggleColor()
        # window.test2 = RoundedFrame("Test2", "#d9d9d9", "green", "20", True)
        # window.test2.setFixedSize(100, 100)
        # window.test2.setParent(window.bodyContainer)
        # window.test2.move(100, 100)
        # window.test2.show()
        # print("Added")

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
    def turnOff():
        #Backtracking
        if window.SENT_PLEASURE:
            SentimentPleasureClick(window)

        window.circle5_2_inner.toggleColor()
        # if not window.TRANSCRIPT_LOOP:
        #     TranscriptClick(window)
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
    #Rest

def SentimentPleasureClick(window):
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
    #Rest

#Bottom Half

def WebcamClick(window):
    if window.CAMERA:
        window.CAMERA = False
        if window.CAMERA_LOOP:
            VideoClick(window)
    else:
        window.CAMERA = True
    window.circle2_2.toggleColor()

def VideoClick(window):
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
    #Rest

def FacialArousalClick(window):
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
    #Rest

def FacialDominanceClick(window):
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
    #Rest

def SkeletonClick(window):
    def turnOff():
        if window.BODY_TRACKING_LOOP:
            BodyTrackingClick(window)

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
    #Rest

def BodyTrackingClick(window):
    def turnOff():
        #BackTracking
        if window.POSE_LOOP:
            PoseClick(window)

        window.rounded4_3.toggleColor()
        window.hlineWidgetSkeltoBody.toggleColor()
    
    def turnOn():
        window.rounded4_3.toggleColor()
        window.hlineWidgetSkeltoBody.toggleColor()
        if not window.SKELETON_LOOP:
            SkeletonClick(window)
    
    if window.BODY_TRACKING_LOOP:
        window.BODY_TRACKING_LOOP = False
        turnOff()
    else:
        window.BODY_TRACKING_LOOP = True
        turnOn()
    #Rest

def PoseClick(window):
    def turnOff():
        #BackTracking
        if window.POSE_DOMINANCE:
            PoseDominanceClick(window)

        window.circle5_4_inner.toggleColor()
        window.hlineWidgetBodytoPose.toggleColor()
    
    def turnOn():
        window.circle5_4_inner.toggleColor()
        window.hlineWidgetBodytoPose.toggleColor()
        if not window.BODY_TRACKING_LOOP:
            BodyTrackingClick(window)

    if window.POSE_LOOP:
        window.POSE_LOOP = False
        turnOff()
    else:
        window.POSE_LOOP = True
        turnOn()
    #Rest

def PoseDominanceClick(window):
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
    #Rest

# Back Part
    
def FusionClick(window):
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
        #Collector fehlt noch
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

def PlayButtonClick(window):
    print("Play Button Clicked")
    
    window.pipe = AffectPipeline(enable_log_to_console=False,
                      enable_vad_loop=window.MIC_LOOP,
                      enable_ser_loop=False,
                      enable_stt_loop=window.TRANSCRIPT_LOOP,
                      enable_camera_loop=window.CAMERA_LOOP,
                      enable_print_loop=False, #
                      enable_send_udp_loop=window.UDP,
                      enable_send_kafka_loop=window.KAFKA,
                      enable_face_er_loop= False, #
                      enable_face_mesh_loop=False,
                      enable_pose_loop=False,
                      enable_fusion_loop=False,
                      enable_sentiment_loop=False,
                      show_face_mesh=False,
                      face_mesh_show_face_edges=False,
                      face_mesh_show_face_pupils=False,
                      face_mesh_show_face_contour=False,
                      camera_id=window.cam_id,
                      ser_loop_rate=1.0,
                      stt_loop_rate=0.2,
                      sentiment_loop_rate=1.0,
                      vad_loop_rate=4.0,
                      er_loop_rate=2.0,
                      pose_loop_rate=4.0,
                      send_loop_rate=2.0,
                      camera_loop_rate=4.0,
                      face_mesh_rate=4.0,
                      udp_ip=window.UDP_IP,
                      udp_port=window.UDP_PORT,
                      kafka_ip=window.KAFKA_IP,
                      kafka_port=window.KAFKA_PORT,
                      web_app_port=5000,
                      kafka_topic_name=window.KAFKA_TOPIC,
                      sample_rate=16000,
                      vad_threshold=0.25,
                      face_padding=0.2,
                      microphone_chunks=16000,
                      microphone_id=window.mic_id,
                      stt_window_length=5,
                      stt_model_size="base",
                      sentiment_model="germansentiment")
    window.START = False
    if window.CAMERA_LOOP:
        layout = window.bodyContainer.layout()
        x = window.rounded3_3.x()
        y = window.rounded3_3.y()
        layout.removeWidget(window.rounded3_3)
        window.rounded3_3.setParent(None)
        window.image = ImageWindow(window=window)
        window.image.setParent(window.bodyContainer)
        window.image.show()
    if window.MIC_LOOP:
        # window.test = PlotWindow()
        # window.test.playButtonClicked()
        # window.test.show()
        layout = window.bodyContainer.layout()
        layout.removeWidget(window.rounded3_1)
        window.rounded3_1.setParent(None)
        window.audio = PlotWidget(window=window)
        window.audio.setParent(window.bodyContainer)
        window.audio.show()
        window.audio.playButtonClicked()
    if window.TRANSCRIPT_LOOP:
        layout = window.bodyContainer.layout()
        layout.removeWidget(window.rounded3_2)
        window.rounded3_2.setParent(None)
        window.transcript = TranscriptWidget(window=window)
        window.transcript.setParent(window.bodyContainer)
        window.transcript.show()
        
    window.pipe.start(window)

def kafkaClick(window):

    def turnOn():
        window.kafka_button.setStyleSheet("background-color: green")
    
    def turnOff():
        window.kafka_button.setStyleSheet("")

    if window.KAFKA:
        window.KAFKA = False
        turnOff()
    else:
        window.KAFKA = True
        turnOn()

def udpClick(window):
    
        def turnOn():
            window.udp_button.setStyleSheet("background-color: green")
        
        def turnOff():
            window.udp_button.setStyleSheet("")
    
        if window.UDP:
            window.UDP = False
            turnOff()
        else:
            window.UDP = True
            turnOn()
    
def connect(window):
    #Upper
    window.circle2_1.clicked.connect(lambda: headphonesClick(window)) 
    window.rounded3_1.clicked.connect(lambda: AudioClick(window)) 
    window.rounded3_2.clicked.connect(lambda: TranscriptClick(window))
    window.play_button.clicked.connect(lambda: PlayButtonClick(window))
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

    window.kafka_button.leftClicked.connect(lambda: kafkaClick(window))
    window.udp_button.leftClicked.connect(lambda: udpClick(window))

