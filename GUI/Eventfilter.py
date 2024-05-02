"""This file contains the functions to move the widgets in the main window"""
from PyQt6.QtCore import QEvent
from cv2 import circle

def moveColumn8(window):
    """Function to move the widgets in the 8th column"""
    # window.circle8_1.move(
    #     (window.bodyContainer.width() - int(window.bodyContainer.width() / 8) + int(window.bodyContainer.width() / 16) - window.circle8_1.width() // 2),
    #     (window.column_height_light //2 - window.circle8_1.height() //2) - int(window.circle8_1.height() *1.5)
    # )
    
    window.circle8_1.move(
        window.frames[1].x() + int(window.column_width_title*6.45) - window.circle8_1.width()//2 + 35,
        (window.column_height_light - window.circle8_1.height()) // 2 - int(window.circle8_1.height() *1.5)
    )

    window.circle8_2.move(
        window.circle8_1.x(),
        (window.column_height_light - window.circle8_2.height()) // 2
    )
            
    window.circle8_3.move(
        window.circle8_1.x(),
        (window.column_height_light - window.circle8_3.height()) // 2  + int(window.circle8_2.height() *1.5)
    )

    window.rounded8_1.move(
        window.circle8_1.x() + window.rounded8_1.width() // 8 ,
        (window.column_height_light - window.rounded8_1.height()) // 2 - int(window.circle8_1.height() * 1.5)
    )

    window.rounded8_2.move(
        window.rounded8_1.x(),
        (window.column_height_light - window.rounded8_2.height()) // 2 
    )

    window.rounded8_3.move(
        window.rounded8_1.x(),
        (window.column_height_light - window.rounded8_3.height()) // 2 + int(window.circle8_2.height() * 1.5)
    )

def moveColumn7(window):
    """Function to move the widgets in the 7th column"""
    # window.circle7outer.move(
    #     (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *2) + int(window.bodyContainer.width() / 16) - window.circle7outer.width() // 2),
    #     (window.column_height_light - window.circle7outer.height()) // 2
    # )
    
    window.circle7outer.move(
        window.frames[1].x() + int(window.column_width_title*5.5) - window.circle7outer.width()//2 + 30,
        (window.column_height_light - window.circle7outer.height()) // 2
    )

    window.circle7inner.move(
        window.circle7outer.x() + 7,
        (window.column_height_light - window.circle7inner.height()) // 2
    )

    # window.rounded7.move(
    #     (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *2) + int(window.bodyContainer.width() / 16)) - window.rounded7.width() //2 ,
    #     (window.column_height_light - window.rounded7.height()) // 2
    # )
    
    window.rounded7.move(
        window.frames[1].x() + int(window.column_width_title*5.5) - window.rounded7.width()//2 + 30,
        (window.column_height_light - window.rounded7.height()) // 2
    )

def moveColumn6(window):
    """Function to move the widgets in the 6th column"""
    # window.circle6_1.move(
    #     (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *3) + int(window.bodyContainer.width() / 16) - window.circle6_4.width() // 2) - 20,
    #     5 + window.circle5_1_outer.height()//2 - window.circle6_1.height()//2
    #  )
    window.circle6_1.move(
        window.frames[1].x() + int(window.column_width_title*4.3) - window.circle6_1.width()//2 + 25,
        10 + window.circle5_1_outer.height()//2 - window.circle6_1.height()//2
    )

    window.circle6_2.move(
        window.circle6_1.x(),
        window.circle6_1.y() + window.circle6_2.height() + 5
    )

    window.circle6_3.move(
        window.circle6_1.x(),
        window.circle6_2.y() + window.circle6_3.height() + 5
    )

    window.circle6_4.move(
        window.circle6_1.x(),
        window.circle6_3.y() + int(window.circle6_4.height()*1.5)
    )

    window.circle6_5.move(
        window.circle6_1.x(),
        window.circle6_4.y() + int(window.circle6_5.height() * 1.5)
    )

    window.circle6_6.move(
        window.circle6_1.x(),
        window.circle6_5.y() + window.circle6_6.height() + 5
    )

    window.circle6_7.move(
        window.circle6_1.x(),
        window.circle6_6.y() + window.circle6_7.height() + 5
    )

    window.circle6_8.move(
        window.circle6_1.x(),
        window.circle6_7.y() + int(window.circle6_8.height() * 1.5)
    )

    window.rounded6_1.move(
        window.circle6_4.x() + int(window.rounded6_1.width() // 8),
        10 + window.circle5_1_outer.height()//2 - window.rounded6_1.height()//2
    )

    window.rounded6_2.move(
        window.rounded6_1.x(),
        window.circle6_2.y() + window.circle6_2.radius - window.rounded6_2.height()//2
    )

    window.rounded6_3.move(
        window.rounded6_1.x(),
        window.circle6_3.y() + window.circle6_3.radius - window.rounded6_3.height()//2
    )

    window.rounded6_4.move(
        window.rounded6_1.x(),
        window.circle6_4.y() + window.circle6_4.radius - window.rounded6_4.height()//2
    )

    window.rounded6_5.move(
        window.rounded6_1.x(),
        window.circle6_5.y() + window.circle6_5.radius - window.rounded6_5.height()//2
    )

    window.rounded6_6.move(
        window.rounded6_1.x(),
        window.circle6_6.y() + window.circle6_6.radius - window.rounded6_6.height()//2
    )

    window.rounded6_7.move(
        window.rounded6_1.x(),
        window.circle6_7.y() + window.circle6_7.radius - window.rounded6_7.height()//2
    )

    window.rounded6_8.move(
        window.rounded6_1.x(),
        window.circle6_8.y() + window.circle6_8.radius - window.rounded6_8.height()//2
    )

def moveColumn5(window):
    """Function to move the widgets in the 5th column"""
    # window.circle5_1_outer.move(
    #     (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *4) + int(window.bodyContainer.width() / 16) - window.circle5_1_outer.width() // 2),
    #     5
    # )
    
    window.circle5_1_outer.move(
        window.frames[1].x() + int(window.column_width_title*3.5) - window.circle5_1_outer.width()//2 + 20,
        10)

    window.circle5_1_inner.move(
        window.circle5_1_outer.x() + 7,
        window.circle5_1_outer.y() + 7 #10
    )

    window.circle5_2_outer.move(
        window.circle5_1_outer.x(),
        window.circle5_1_outer.y() + window.circle5_1_outer.height() + 20
    )

    window.circle5_2_inner.move(
        window.circle5_1_inner.x(),
        window.circle5_2_outer.y() + 7 
    )

    window.circle5_3_outer.move(
        window.circle5_1_outer.x(),
        window.circle5_2_outer.y() + window.circle5_2_outer.height() + 30
    )

    window.circle5_3_inner.move(
        window.circle5_1_inner.x(),
        window.circle5_3_outer.y() + 7
    )

    window.circle5_4_outer.move(
        window.circle5_1_outer.x(),
        window.circle5_3_outer.y() + window.circle5_3_outer.height() + 20
    )

    window.circle5_4_inner.move(
        window.circle5_1_inner.x(),
        window.circle5_4_outer.y() + 7 
    )

def moveColumn4(window):
    """Function to move the widgets in the 4th column"""
    window.circle4_1.move(
        window.frames[1].x() + int(window.column_width_title*2.5) - window.circle4_1.width()//2 + 15,
        window.circle5_1_inner.y() + int(1.5* window.circle4_1.radius)
    )
    # window.circle4_1.move(
    #     (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *5) + int(window.bodyContainer.width() / 16) - window.circle4_1.width() // 2),
    #     window.circle5_1_inner.y() + int(1.5* window.circle4_1.radius)
    # )

    window.circle4_2.move(
        window.circle4_1.x(),
        window.circle5_3_inner.y() - int(1.5* window.circle4_2.radius) 
    )

    window.circle4_3.move(
        window.circle4_1.x(),
        window.circle5_4_inner.y() - int(1.5* window.circle4_3.radius)
    )
    
    # window.circle4_3.move(
    #     (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *5) + int(window.bodyContainer.width() / 16) - window.circle4_3.width() // 2),
    #     window.circle5_4_inner.y() + window.circle5_4_inner.height()//2 - window.circle4_3.height()//2
    # )

    window.rounded4_1.move(
        window.circle4_1.x() + window.circle4_1.radius - window.rounded4_1.width()//2,
        window.circle4_1.y() + window.circle4_1.radius - window.rounded4_1.height()//2
    )

    window.rounded4_2.move(
        window.circle4_2.x() + window.circle4_2.radius - window.rounded4_2.width()//2,
        window.circle4_2.y() + window.circle4_2.radius - window.rounded4_2.height()//2
    )

    window.rounded4_3.move(
        window.circle4_3.x() + window.circle4_3.radius - window.rounded4_3.width()//2,
        window.circle4_3.y() + window.circle4_3.radius - window.rounded4_3.height()//2
    )
    
    # window.rounded4_3.move(
    #     window.circle4_3.x() + window.circle4_3.radius - window.rounded4_3.width()//2,
    #     window.circle5_4_inner.y() + window.rounded4_3.height()
    # )

def moveColumn3(window):
    """Function to move the widgets in the 3rd column"""
    window.rounded3_1.move(
        window.frames[1].x() + int(window.column_width_title*1.5) - window.rounded3_1.width()//2 + 5,
        window.circle5_1_inner.y() + window.rounded3_1.height())
    # window.rounded3_1.move(
    #     (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *6) + int(window.bodyContainer.width() / 16) - window.rounded3_1.width() // 2),
    #     window.circle5_1_inner.y() + window.rounded3_1.height()
    # )

    window.rounded3_2.move(
        window.rounded3_1.x(),
        window.circle5_2_inner.y() + window.rounded3_2.height()
    )

    window.rounded3_3.move(
        window.rounded3_1.x(),
        window.circle5_3_inner.y() + window.rounded3_3.height()
    )

    window.rounded3_4.move(
        window.rounded3_1.x(),
        window.circle5_4_inner.y() + window.rounded3_4.height()
    )

def moveColumn2(window):
    """Function to move the widgets in the 2nd column"""
    window.circle2_1.move(
        window.frames[1].x() + window.column_width_title//2 - window.circle2_1.width()//2,
        window.rounded3_1.y() + window.rounded3_1.height()//2 - window.circle2_1.height()//2)
    # window.circle2_1.move(
    #     (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *7) + int(window.bodyContainer.width() / 16) - window.circle2_1.width() // 2),
    #     window.rounded3_1.y() + window.rounded3_1.height()//2 - window.circle2_1.height()//2
    # )

    window.circle2_2.move(
       window.circle2_1.x(),
        window.circle2_1.y() + window.circle2_1.height() + int(window.circle2_2.height() * 0.5)
    )    

def moveButtons(window):
    """Function to move the buttons in the main window"""
    window.play_button.move(
        window.column_width//2 - window.play_button.width()//2,
        window.bodyContainer.height() - (3*window.play_button.height())
    )

    # window.stop_button.move(
    #     window.play_button.x() + window.play_button.width() + 10,
    #     window.play_button.y()
    # )

    window.kafka_button.move(
    #     window.stop_button.x() + window.stop_button.width() + 10,
        window.play_button.x() + window.play_button.width() + 10,
        window.play_button.y()
    )
            
    window.udp_button.move(
        window.kafka_button.x() + window.kafka_button.width() + 10,
        window.play_button.y()
    )

    # window.console.move(
    #     window.play_button.x(),
    #     window.play_button.y() - window.console.height() - 10
    # )

def moveLinesFrom7to8(window):
    """Function to move the lines from the 7th column to the 8th column"""
    hlineFtoA1_Length = abs(window.rounded7.width()//2 - int(0.75*window.column_width // 3))
    window.hlineWidgetFtoA1.setFixedSize(hlineFtoA1_Length, window.LINEWIDTH)
    window.hlineWidgetFtoA1.move(
        window.rounded7.x() + window.rounded7.width(),
        (window.column_height_light) // 2
    )

    hlineFtoA2_Length = abs(window.circle8_2.x() -( window.hlineWidgetFtoA1.x() + hlineFtoA1_Length))
    window.hlineWidgetFtoA2.setFixedSize(hlineFtoA2_Length, window.LINEWIDTH)
    window.hlineWidgetFtoA2.move(
        window.hlineWidgetFtoA1.x() + hlineFtoA1_Length,
        (window.column_height_light) // 2
    )

    vlineFtoP_length = abs(window.hlineWidgetFtoA1.y() - (window.rounded8_1.y() + window.rounded8_1.height()//2))  
    window.vlineWidgetFtoP.setFixedSize(window.LINEWIDTH, vlineFtoP_length)
    window.vlineWidgetFtoP.move(
        window.hlineWidgetFtoA1.x() + hlineFtoA1_Length - window.LINEWIDTH,
        (window.column_height_light) // 2 - window.vlineWidgetFtoP.height() 
    )

    hlineFtoP_length = abs(window.circle8_1.x() - window.vlineWidgetFtoP.x() - window.LINEWIDTH)
    window.hlineWidgetFtoP.setFixedSize(hlineFtoP_length, window.LINEWIDTH) 
    window.hlineWidgetFtoP.move(
        window.vlineWidgetFtoP.x() + window.LINEWIDTH,
        (window.column_height_light) // 2 - window.vlineWidgetFtoP.height() 
    )

    vlineFtoD_length = abs(window.hlineWidgetFtoA1.y() - (window.rounded8_3.y() + window.rounded8_3.height()//2))
    window.vlineWidgetFtoD.setFixedSize(window.LINEWIDTH, vlineFtoD_length )
    window.vlineWidgetFtoD.move(
        window.hlineWidgetFtoA1.x() + hlineFtoA1_Length - window.LINEWIDTH,
        window.hlineWidgetFtoA1.y() + window.LINEWIDTH
    )

    hlineFtoD_length = abs(window.circle8_3.x() - window.vlineWidgetFtoD.x() - window.LINEWIDTH)
    window.hlineWidgetFtoD.setFixedSize(hlineFtoD_length, window.LINEWIDTH)
    window.hlineWidgetFtoD.move(
        window.vlineWidgetFtoD.x() + window.LINEWIDTH ,
        (window.column_height_light) // 2 + window.vlineWidgetFtoD.height()
    )

def moveLinesFrom6to7(window):
    """Function to move the lines from the 6th column to the 7th column"""
    collectorline_length = abs(window.hlineWidgettoCol2.y() - window.hlineWidgettoCol1.y())
    window.collectorLine6to7_1.setFixedSize(window.LINEWIDTH, collectorline_length)
    window.collectorLine6to7_1.move(
        window.rounded7.x() + window.rounded7.width()//2 - int(1.25*window.column_width // 2) ,
        window.hlineWidgettoCol1.y() 
    )

    collectorline_length = abs(window.hlineWidgettoCol3.y() - window.hlineWidgettoCol2.y())
    window.collectorLine6to7_2.setFixedSize(window.LINEWIDTH, collectorline_length)
    window.collectorLine6to7_2.move(
        window.collectorLine6to7_1.x(),
        window.hlineWidgettoCol2.y() 
    )

    collectorline_length = abs(window.hlineWidgettoCol4.y() - window.hlineWidgettoCol3.y()) 
    window.collectorLine6to7_3.setFixedSize(window.LINEWIDTH, collectorline_length)
    window.collectorLine6to7_3.move(
        window.collectorLine6to7_1.x(),
        window.hlineWidgettoCol3.y() 
    )

    collectorline_length = abs(window.hlineWidgetColtoF.y() - window.hlineWidgettoCol4.y())
    window.collectorLine6to7_4.setFixedSize(window.LINEWIDTH, collectorline_length)
    window.collectorLine6to7_4.move(
        window.collectorLine6to7_1.x(),
        window.hlineWidgettoCol4.y() 
    )

    collectorline_length = abs(window.hlineWidgettoCol5.y() - window.hlineWidgetColtoF.y())
    window.collectorLine6to7_5.setFixedSize(window.LINEWIDTH, collectorline_length)
    window.collectorLine6to7_5.move(
        window.collectorLine6to7_1.x(),
        window.hlineWidgetColtoF.y() + window.LINEWIDTH
    )

    collectorline_length = abs(window.hlineWidgettoCol6.y() - window.hlineWidgettoCol5.y())
    window.collectorLine6to7_6.setFixedSize(window.LINEWIDTH, collectorline_length)
    window.collectorLine6to7_6.move(
        window.collectorLine6to7_1.x(),
        window.hlineWidgettoCol5.y() + window.LINEWIDTH
    )

    collectorline_length = abs(window.hlineWidgettoCol7.y() - window.hlineWidgettoCol6.y())
    window.collectorLine6to7_7.setFixedSize(window.LINEWIDTH, collectorline_length)
    window.collectorLine6to7_7.move(
        window.collectorLine6to7_1.x(),
        window.hlineWidgettoCol6.y() + window.LINEWIDTH
    )

    collectorline_length = abs(window.hlineWidgettoCol8.y() - window.hlineWidgettoCol7.y())
    window.collectorLine6to7_8.setFixedSize(window.LINEWIDTH, collectorline_length)
    window.collectorLine6to7_8.move(
        window.collectorLine6to7_1.x(),
        window.hlineWidgettoCol7.y() + window.LINEWIDTH
    )
        
    hlinetocol_length = abs(window.collectorLine6to7_1.x() - (window.rounded6_1.x() + window.rounded6_1.width()))
    window.hlineWidgettoCol1.setFixedSize(int(hlinetocol_length) + window.LINEWIDTH, window.LINEWIDTH)
    window.hlineWidgettoCol1.move(
        window.rounded6_1.x() + window.rounded6_1.width(),
        window.rounded6_1.y() + window.rounded6_1.height()//2
    )

    window.hlineWidgettoCol2.setFixedSize(int(hlinetocol_length), window.LINEWIDTH)
    window.hlineWidgettoCol2.move(
        window.rounded6_2.x() + window.rounded6_2.width(),
        window.rounded6_2.y() + window.rounded6_2.height()//2
    )

    window.hlineWidgettoCol3.setFixedSize(int(hlinetocol_length), window.LINEWIDTH)
    window.hlineWidgettoCol3.move(
        window.rounded6_3.x() + window.rounded6_3.width(),
        window.rounded6_3.y() + window.rounded6_3.height()//2
    )

    window.hlineWidgettoCol4.setFixedSize(int(hlinetocol_length), window.LINEWIDTH)
    window.hlineWidgettoCol4.move(
        window.rounded6_4.x() + window.rounded6_4.width(),
        window.rounded6_4.y() + window.rounded6_4.height()//2
    )

    window.hlineWidgettoCol5.setFixedSize(int(hlinetocol_length), window.LINEWIDTH)
    window.hlineWidgettoCol5.move(
        window.rounded6_5.x() + window.rounded6_5.width(),
        window.rounded6_5.y() + window.rounded6_5.height()//2
    )

    window.hlineWidgettoCol6.setFixedSize(int(hlinetocol_length), window.LINEWIDTH)
    window.hlineWidgettoCol6.move(
        window.rounded6_6.x() + window.rounded6_6.width(),
        window.rounded6_6.y() + window.rounded6_6.height()//2
    )

    window.hlineWidgettoCol7.setFixedSize(int(hlinetocol_length), window.LINEWIDTH)
    window.hlineWidgettoCol7.move(
        window.rounded6_7.x() + window.rounded6_7.width(),
        window.rounded6_7.y() + window.rounded6_7.height()//2
    )

    window.hlineWidgettoCol8.setFixedSize(int(hlinetocol_length), window.LINEWIDTH)
    window.hlineWidgettoCol8.move(
        window.rounded6_8.x() + window.rounded6_8.width(),
        window.rounded6_8.y() + window.rounded6_8.height()//2
    )

    hlinefromcol_length = abs(window.rounded7.x() - window.collectorLine6to7_1.x())
    window.hlineWidgetColtoF.setFixedSize(hlinefromcol_length, window.LINEWIDTH)
    window.hlineWidgetColtoF.move(
        window.collectorLine6to7_1.x() ,
        window.rounded7.y() + window.rounded7.height()//2
    )

def moveLinesFrom5to6(window):
    """Function to move the lines from the 5th column to the 6th column"""
    hlinetocol_length =  abs(-window.circle5_1_outer.width()//2 + int(1.75*window.column_width//3)) #abs(window.collectorLine5to6_1.x() - (window.circle5_1_outer.x() + window.circle5_1_outer.width() ))
    window.hlinetoCol5to6_1.setFixedSize(hlinetocol_length + window.LINEWIDTH, window.LINEWIDTH)
    window.hlinetoCol5to6_1.move(
        window.circle5_1_outer.x() + window.circle5_1_outer.width(),
        window.circle5_1_outer.y() + window.circle5_1_outer.height()//2
    )
            
    collectorLine5to6_1_length = abs(window.circle5_1_outer.y() + window.circle5_1_outer.height()//2 - (window.rounded6_2.y() + window.rounded6_2.height()//2))
    window.collectorLine5to6_1.setFixedSize(window.LINEWIDTH, abs(collectorLine5to6_1_length) + window.LINEWIDTH)
    window.collectorLine5to6_1.move(
        window.hlinetoCol5to6_1.x() + hlinetocol_length,
        window.circle5_1_outer.y() + window.circle5_1_outer.height()//2
    )
    
    collectorLine5to6_1_1_length = abs(window.collectorLine5to6_1.y() + collectorLine5to6_1_length - (window.rounded6_3.y() + window.rounded6_3.height()//2))
    window.collectorLine5to6_1_1.setFixedSize(window.LINEWIDTH, abs(collectorLine5to6_1_1_length))
    window.collectorLine5to6_1_1.move(
        window.collectorLine5to6_1.x(),
        window.rounded6_2.y() + window.rounded6_2.height()//2 + window.LINEWIDTH
    )

    hlinefromcol_length = abs(window.circle6_1.x() - window.collectorLine5to6_1.x())
    window.hline1fromCol5to6_1.setFixedSize(hlinefromcol_length, window.LINEWIDTH)
    window.hline1fromCol5to6_1.move(
        window.collectorLine5to6_1.x(),
        window.rounded6_1.y() + window.rounded6_1.height()//2
    )

    window.hline2fromCol5to6_1.setFixedSize(hlinefromcol_length - window.LINEWIDTH, window.LINEWIDTH)
    window.hline2fromCol5to6_1.move(
        window.collectorLine5to6_1.x() + window.LINEWIDTH,
        window.rounded6_2.y() + window.rounded6_2.height()//2
    )

    window.hline3fromCol5to6_1.setFixedSize(hlinefromcol_length, window.LINEWIDTH)
    window.hline3fromCol5to6_1.move(
        window.collectorLine5to6_1.x(),
        window.rounded6_3.y() + window.rounded6_3.height()//2
    )

    verLineWidgetSertoP_length = (window.rounded6_4.y() + window.rounded6_4.height()//2) - (window.circle5_2_outer.y() + window.circle5_1_outer.height()//2 )
    window.verlineWidgetSertoP.setFixedSize(window.LINEWIDTH, verLineWidgetSertoP_length)
    window.verlineWidgetSertoP.move(
        window.circle5_2_outer.x() + window.circle5_2_outer.width()//2 + int(1.25*window.column_width//3),
        window.circle5_2_outer.y() + window.circle5_2_outer.height()//2
    )

    hLineFromSertoVer_length = abs(window.verlineWidgetSertoP.x() - (window.circle5_2_outer.x() + window.circle5_2_outer.width()))
    window.horLineWidgetSertoVer.setFixedSize(hLineFromSertoVer_length, window.LINEWIDTH)
    window.horLineWidgetSertoVer.move(
        window.circle5_2_outer.x() + window.circle5_2_outer.width(),
        window.circle5_2_outer.y() + window.circle5_2_outer.height()//2
    )

    hlineVertoP_length = abs(window.circle6_4.x() - window.verlineWidgetSertoP.x()) 
    window.hlineWidgetVertoP.setFixedSize(hlineVertoP_length, window.LINEWIDTH)
    window.hlineWidgetVertoP.move(
        window.verlineWidgetSertoP.x() ,
        window.rounded6_4.y() + window.rounded6_4.height()//2
    )

    window.hlinetoCol5to6_2.setFixedSize(hlinetocol_length, window.LINEWIDTH)
    window.hlinetoCol5to6_2.move(
        window.circle5_3_outer.x() + window.circle5_3_outer.width(),
        window.circle5_3_outer.y() + window.circle5_3_outer.height()//2
    )

    collectorLine5to6_2_length = window.circle5_3_outer.y() + window.circle5_3_outer.height()//2 - (window.rounded6_5.y() + window.rounded6_5.height()//2)
    window.collectorLine5to6_2.setFixedSize(window.LINEWIDTH, abs(collectorLine5to6_2_length) + window.LINEWIDTH)
    window.collectorLine5to6_2.move(
        window.hlinetoCol5to6_2.x() + hlinetocol_length,
        window.circle5_3_outer.y() + window.circle5_3_outer.height()//2
    )

    collectorLine5to6_2_2_length = window.collectorLine5to6_2.y() - collectorLine5to6_2_length - (window.rounded6_6.y() + window.rounded6_6.height()//2)
    window.collectorLine5to6_2_2.setFixedSize(window.LINEWIDTH, abs(collectorLine5to6_2_2_length))
    window.collectorLine5to6_2_2.move(
        window.collectorLine5to6_2.x(),
        window.rounded6_5.y() + window.rounded6_5.height()//2 + window.LINEWIDTH
    )

    collectorLine5to6_2_3_length = window.collectorLine5to6_2_2.y() - collectorLine5to6_2_2_length - (window.rounded6_7.y() + window.rounded6_7.height()//2)
    window.collectorLine5to6_2_3.setFixedSize(window.LINEWIDTH, abs(collectorLine5to6_2_3_length))
    window.collectorLine5to6_2_3.move(
        window.collectorLine5to6_2.x(),
        window.rounded6_6.y() + window.rounded6_6.height()//2 + window.LINEWIDTH
    )

    window.hline1fromCol5to6_2.setFixedSize(hlinefromcol_length - window.LINEWIDTH, window.LINEWIDTH)
    window.hline1fromCol5to6_2.move(
        window.collectorLine5to6_2.x() + window.LINEWIDTH,
        window.rounded6_5.y() + window.rounded6_5.height()//2
    )

    window.hline2fromCol5to6_2.setFixedSize(hlinefromcol_length - window.LINEWIDTH, window.LINEWIDTH)
    window.hline2fromCol5to6_2.move(
        window.collectorLine5to6_2.x() + window.LINEWIDTH,
        window.rounded6_6.y() + window.rounded6_6.height()//2 
    )

    window.hline3fromCol5to6_2.setFixedSize(hlinefromcol_length , window.LINEWIDTH)
    window.hline3fromCol5to6_2.move(
        window.collectorLine5to6_2.x(),
        window.rounded6_7.y() + window.rounded6_7.height()//2
    )

    verLineWidgetPosetoD_length = (window.rounded6_8.y() + window.rounded6_8.height()//2) - (window.circle5_4_outer.y() + window.circle5_4_outer.height()//2 )
    window.verlineWidgetPosetoD.setFixedSize(window.LINEWIDTH, verLineWidgetPosetoD_length)
    window.verlineWidgetPosetoD.move(
        window.verlineWidgetSertoP.x(),
        window.circle5_4_outer.y() + window.circle5_4_outer.height()//2
    )

    hLineFromPosetoVer_length = abs(window.verlineWidgetPosetoD.x() - (window.circle5_4_outer.x() + window.circle5_4_outer.width()))
    window.hLineWidgetPosetoVer.setFixedSize(hLineFromPosetoVer_length, window.LINEWIDTH)
    window.hLineWidgetPosetoVer.move(
        window.circle5_4_outer.x() + window.circle5_4_outer.width(),
        window.circle5_4_outer.y() + window.circle5_4_outer.height()//2
    )

    hlineVertoD_length = abs(window.circle6_8.x() - window.verlineWidgetPosetoD.x())
    window.hlineWidgetVertoD.setFixedSize(hlineVertoD_length, window.LINEWIDTH)
    window.hlineWidgetVertoD.move(
        window.verlineWidgetPosetoD.x() ,
        window.rounded6_8.y() + window.rounded6_8.height()//2
    )

def moveLinesFrom3to4to5(window):
    """Function to move the lines from the 3rd column to the 4th and 5th column"""
    hlineLength3to5 = abs(window.circle5_1_outer.x() - (window.rounded3_1.x() + window.rounded3_1.width()))
    hlineAudioToPara_length1 = int(1.25* window.column_width//3) + 2 - window.rounded3_1.width()//2 #(window.rounded3_1.x() + window.rounded3_1.width()//2 + window.column_width//2 + 2) - (window.rounded3_1.x() + window.rounded3_1.width())
    window.hlineWidgetAudiotoPara1.setFixedSize(hlineAudioToPara_length1 + window.LINEWIDTH, window.LINEWIDTH)
    window.hlineWidgetAudiotoPara1.move(
        window.rounded3_1.x() + window.rounded3_1.width(),
        window.rounded3_1.y() + window.rounded3_1.height()//2
    )

    window.hlineWidgetAudiotoPara2.setFixedSize(hlineLength3to5 - hlineAudioToPara_length1 - window.LINEWIDTH, window.LINEWIDTH)
    window.hlineWidgetAudiotoPara2.move(
        window.hlineWidgetAudiotoPara1.x() + hlineAudioToPara_length1 + window.LINEWIDTH,
        window.rounded3_1.y() + window.rounded3_1.height()//2
    )
    
    verLineWidgetAudiotoVoice_length = abs(window.hlineWidgetAudiotoPara1.y() - (window.rounded4_1.y() + window.rounded4_1.height()//2))
    window.verLineWidgetAudiotoVoice.setFixedSize(window.LINEWIDTH, verLineWidgetAudiotoVoice_length - window.LINEWIDTH)
    window.verLineWidgetAudiotoVoice.move(
        window.hlineWidgetAudiotoPara1.x() + hlineAudioToPara_length1,
        window.hlineWidgetAudiotoPara1.y() + window.LINEWIDTH
    )

    hlineWidget_length = abs(window.rounded4_1.x() - window.verLineWidgetAudiotoVoice.x() )
    hlineWidget_length2 = abs(hlineWidget_length + window.LINEWIDTH - 10)
    window.hlineWidgetAudiotoVoice.setFixedSize(hlineWidget_length, window.LINEWIDTH)
    window.hlineWidgetAudiotoVoice.move(
        window.verLineWidgetAudiotoVoice.x() ,
        window.verLineWidgetAudiotoVoice.y() + window.verLineWidgetAudiotoVoice.height()
    )

    window.hlineWidgetVoicetoPara.setFixedSize(hlineWidget_length2, window.LINEWIDTH)
    window.hlineWidgetVoicetoPara.move(
        window.rounded4_1.x() + window.rounded4_1.width() ,
        window.rounded4_1.y() + window.rounded4_1.height()//2
    )

    window.verLineWidgetVoicetoPara.setFixedSize(window.LINEWIDTH, verLineWidgetAudiotoVoice_length - window.LINEWIDTH)
    window.verLineWidgetVoicetoPara.move(
        window.hlineWidgetVoicetoPara.x() + hlineWidget_length2 - window.LINEWIDTH,
        window.hlineWidgetAudiotoPara1.y() + window.LINEWIDTH
    )

    window.hlinewidgetTratoSen.setFixedSize(hlineLength3to5 , window.LINEWIDTH)
    window.hlinewidgetTratoSen.move(
        window.rounded3_2.x() + window.rounded3_2.width(),
        window.rounded3_2.y() + window.rounded3_2.height()//2
    )

    window.hlineWidgetVideotoFacial1.setFixedSize(hlineAudioToPara_length1 + window.LINEWIDTH, window.LINEWIDTH)
    window.hlineWidgetVideotoFacial1.move(
        window.rounded3_3.x() + window.rounded3_3.width(),
        window.rounded3_3.y() + window.rounded3_3.height()//2
    )

    window.hlineWidgetVideotoFacial2.setFixedSize(hlineLength3to5 - hlineAudioToPara_length1 - window.LINEWIDTH, window.LINEWIDTH)
    window.hlineWidgetVideotoFacial2.move(
        window.hlineWidgetVideotoFacial1.x() + hlineAudioToPara_length1 + window.LINEWIDTH,
        window.rounded3_3.y() + window.rounded3_3.height()//2
    )

    verlineWidgetVideotoFace_length = abs(window.hlineWidgetVideotoFacial1.y() - (window.rounded4_2.y() + window.rounded4_2.height()//2))
    window.verlineWidgetVideotoFace.setFixedSize(window.LINEWIDTH, verlineWidgetVideotoFace_length)
    window.verlineWidgetVideotoFace.move(
        window.verLineWidgetAudiotoVoice.x(),
        window.hlineWidgetVideotoFacial1.y() - window.verlineWidgetVideotoFace.height()
    )

    hlineWidget_length = abs(window.rounded4_2.x() - window.verlineWidgetVideotoFace.x() )
    window.hlineWidgetVideotoFace.setFixedSize(hlineWidget_length, window.LINEWIDTH)
    window.hlineWidgetVideotoFace.move(
        window.verlineWidgetVideotoFace.x() ,
        window.verlineWidgetVideotoFace.y() 
    )

    window.verlineWidgetFacetoFacial.setFixedSize(window.LINEWIDTH, verlineWidgetVideotoFace_length)
    window.verlineWidgetFacetoFacial.move(
        window.verLineWidgetVoicetoPara.x(),
        window.hlineWidgetVideotoFacial1.y() - window.verlineWidgetFacetoFacial.height()
    )

    window.hlineWidgetFacetoFacial.setFixedSize(hlineWidget_length2 , window.LINEWIDTH)
    window.hlineWidgetFacetoFacial.move(
        window.rounded4_2.x() + window.rounded4_2.width() ,
        window.verlineWidgetFacetoFacial.y() 
    )

    #hlineWidgetSkeltoBody_length = abs(window.rounded4_3.x() - (window.rounded3_4.x() + window.rounded3_4.width()))
    window.hlineWidgetSkeltoPose.setFixedSize(hlineAudioToPara_length1 + window.LINEWIDTH, window.LINEWIDTH)
    window.hlineWidgetSkeltoPose.move(
        window.rounded3_4.x() + window.rounded3_4.width(),
        window.rounded3_4.y() + window.rounded3_4.height()//2
    )

    #hlineWidgetBodytoPose_length = abs(window.circle5_4_outer.x() - (window.rounded4_3.x() + window.rounded4_3.width()))
    window.hlineWidgetSkeltoPose2.setFixedSize(hlineLength3to5 - hlineAudioToPara_length1 - window.LINEWIDTH, window.LINEWIDTH)
    window.hlineWidgetSkeltoPose2.move(
        window.hlineWidgetSkeltoPose.x() + hlineAudioToPara_length1 + window.LINEWIDTH,
        window.rounded3_4.y() + window.rounded3_4.height()//2
    )
    
    vlineSkeltotoPose_length = abs(window.hlineWidgetSkeltoPose.y() - (window.rounded4_3.y() + window.rounded4_3.height()//2))
    window.verlineWidgetSkeltoBody.setFixedSize(window.LINEWIDTH, vlineSkeltotoPose_length)
    window.verlineWidgetSkeltoBody.move(
        window.hlineWidgetSkeltoPose.x() + hlineAudioToPara_length1,
        window.hlineWidgetSkeltoPose.y() - vlineSkeltotoPose_length
    )
    
    hlineSkeltoBody_length = abs(window.rounded4_3.x() - window.verlineWidgetSkeltoBody.x()) 
    window.hlineWidgetSkeltoBody.setFixedSize(hlineSkeltoBody_length, window.LINEWIDTH)
    window.hlineWidgetSkeltoBody.move(
        window.verlineWidgetSkeltoBody.x(),
        window.verlineWidgetSkeltoBody.y()
    )
    
    window.verlineWidgetBodytoPose.setFixedSize(window.LINEWIDTH, vlineSkeltotoPose_length)
    window.verlineWidgetBodytoPose.move(
        window.verlineWidgetFacetoFacial.x(),
        window.hlineWidgetSkeltoPose.y() - vlineSkeltotoPose_length
    )
    
    window.hlineWidgetBodytoPose.setFixedSize(hlineWidget_length2, window.LINEWIDTH)
    window.hlineWidgetBodytoPose.move(
        window.rounded4_3.x() + window.rounded4_3.width(),
        window.verlineWidgetBodytoPose.y()
    )

def moveLinesFrom3to3(window):
    """Function to move the lines from the 3rd column to the 3rd column"""
    verlineWidgetAudiotoTra_length = abs(window.rounded3_2.y() - (window.rounded3_1.y() + window.rounded3_1.height()))
    window.verlineWidgetAudioToTra.setFixedSize(window.LINEWIDTH, verlineWidgetAudiotoTra_length)
    window.verlineWidgetAudioToTra.move(
        window.rounded3_1.x() + window.rounded3_1.width()//2 ,
        window.rounded3_1.y() + window.rounded3_1.height()
    )

    verlineWidgetVideotoSkel_length = abs(window.rounded3_4.y() - (window.rounded3_3.y() + window.rounded3_3.height()))
    window.verlineWidgetVideotoSkel.setFixedSize(window.LINEWIDTH, verlineWidgetVideotoSkel_length)
    window.verlineWidgetVideotoSkel.move(
        window.rounded3_3.x() + window.rounded3_3.width()//2 ,
        window.rounded3_3.y() + window.rounded3_3.height()
    )

def moveLinesFrom2to3(window):
    """Function to move the lines from the 2nd column to the 3rd column"""
    hlineWidget_length = abs(window.rounded3_1.x() - (window.circle2_1.x() + window.circle2_1.width()))
    window.hlineWidgetHeadsettoAudio.setFixedSize(hlineWidget_length, window.LINEWIDTH)
    window.hlineWidgetHeadsettoAudio.move(
        window.circle2_1.x() + window.circle2_1.width(),
        window.circle2_1.y() + window.circle2_1.height()//2
    )                                

    verlineWidgetCamToVideo_length = abs((window.rounded3_3.y() + window.rounded3_3.height()//2 ) - (window.circle2_2.y() + window.circle2_2.height()//2))
    window.verlineWidgetCamToVideo.setFixedSize(window.LINEWIDTH, verlineWidgetCamToVideo_length)
    window.verlineWidgetCamToVideo.move(
        window.circle2_2.x() + window.circle2_2.width()//2 + window.column_width//3 + window.LINEWIDTH,
        window.circle2_2.y() + window.circle2_2.height()//2
    )

    hlineWidgetCamtoVer_length = abs(window.verlineWidgetCamToVideo.x() - (window.circle2_2.x() + window.circle2_2.width()))
    window.hlineWidgetCamtoVer.setFixedSize(hlineWidgetCamtoVer_length, window.LINEWIDTH)
    window.hlineWidgetCamtoVer.move(
        window.circle2_2.x() + window.circle2_2.width(),
        window.verlineWidgetCamToVideo.y()
    )

    hlineWidgetVertoVideo_length = abs((window.rounded3_3.x()) - window.verlineWidgetCamToVideo.x())
    window.hlineWidgetVertoVideo.setFixedSize(hlineWidgetVertoVideo_length, window.LINEWIDTH)
    window.hlineWidgetVertoVideo.move(
        window.verlineWidgetCamToVideo.x(),
        window.rounded3_3.y() + window.rounded3_3.height()//2
    )

def handleEventFilter(window, source, event):
    """Function to handle the event filter for the main window"""
    if source == window.bodyContainer and event.type() == QEvent.Type.Resize:
        moveColumn8(window)
        moveColumn7(window)
        moveColumn6(window)
        moveColumn5(window)
        moveColumn4(window)
        moveColumn3(window) 
        moveColumn2(window)
        moveButtons(window)
        moveLinesFrom7to8(window)   
        moveLinesFrom6to7(window)
        moveLinesFrom5to6(window)
        moveLinesFrom3to4to5(window)
        moveLinesFrom3to3(window)
        moveLinesFrom2to3(window)    
        return True
    return super(window.__class__, window).eventFilter(source, event)