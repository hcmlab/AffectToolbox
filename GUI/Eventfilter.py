
from PyQt6.QtCore import QEvent
def handleEventFilter(window, source, event):
    if source == window.bodyContainer and event.type() == QEvent.Type.Resize:
            # Center the CircleWidget within the bodyContainer
            window.circle8_1.move(
                (window.bodyContainer.width() - int(window.bodyContainer.width() / 8) + int(window.bodyContainer.width() / 16) - window.circle8_1.width() // 2),
                (window.column_height_light //2 - window.circle8_1.height() //2) - int(window.circle8_1.height() *1.5)
            )

            window.circle8_2.move(
                (window.bodyContainer.width() - int(window.bodyContainer.width() / 8) + int(window.bodyContainer.width() / 16) - window.circle8_2.width() // 2),
                (window.column_height_light - window.circle8_2.height()) // 2
            )
            
            window.circle8_3.move(
                (window.bodyContainer.width() - int(window.bodyContainer.width() / 8) + int(window.bodyContainer.width() / 16) - window.circle8_3.width() // 2),
                (window.column_height_light - window.circle8_3.height()) // 2  + int(window.circle8_2.height() *1.5)
            )

            window.rounded8_1.move(
                (window.bodyContainer.width() - int(window.bodyContainer.width() / 8) + int(window.bodyContainer.width() / 16)) - window.rounded8_1.width() // 3 ,
                (window.column_height_light - window.rounded8_1.height()) // 2 - int(window.circle8_1.height() * 1.5)
            )

            window.rounded8_2.move(
                (window.bodyContainer.width() - int(window.bodyContainer.width() / 8) + int(window.bodyContainer.width() / 16)) - window.rounded8_2.width() // 3 ,
                (window.column_height_light - window.rounded8_2.height()) // 2 
            )

            window.rounded8_3.move(
                (window.bodyContainer.width() - int(window.bodyContainer.width() / 8) + int(window.bodyContainer.width() / 16)) - window.rounded8_3.width() // 3 ,
                (window.column_height_light - window.rounded8_3.height()) // 2 + int(window.circle8_2.height() * 1.5)
            )

            window.circle7outer.move(
                (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *2) + int(window.bodyContainer.width() / 16) - window.circle7outer.width() // 2),
                (window.column_height_light - window.circle7outer.height()) // 2
            )

            window.circle7inner.move(
                (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *2) + int(window.bodyContainer.width() / 16) - window.circle7inner.width() // 2),
                (window.column_height_light - window.circle7inner.height()) // 2
            )

            window.rounded7.move(
                (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *2) + int(window.bodyContainer.width() / 16)) - window.rounded7.width() //2 ,
                (window.column_height_light - window.rounded7.height()) // 2
            )

            # Column 6
            window.circle6_1.move(
                (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *3) + int(window.bodyContainer.width() / 16) - window.circle6_4.width() // 2) - 20,
                5 + window.circle5_1_outer.height()//2 - window.circle6_1.height()//2
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
                5 + window.circle5_1_outer.height()//2 - window.rounded6_1.height()//2
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

            # Column 5

            window.circle5_1_outer.move(
                (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *4) + int(window.bodyContainer.width() / 16) - window.circle5_1_outer.width() // 2),
                5
            )

            window.circle5_1_inner.move(
                (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *4) + int(window.bodyContainer.width() / 16) - window.circle5_1_inner.width() // 2),
                window.circle5_1_outer.y() + 10 
            )

            window.circle5_2_outer.move(
                (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *4) + int(window.bodyContainer.width() / 16) - window.circle5_2_outer.width() // 2),
                window.circle5_1_outer.y() + window.circle5_1_outer.height() + 20
            )

            window.circle5_2_inner.move(
                (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *4) + int(window.bodyContainer.width() / 16) - window.circle5_2_inner.width() // 2),
                window.circle5_2_outer.y() + 10 
            )

            window.circle5_3_outer.move(
                (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *4) + int(window.bodyContainer.width() / 16) - window.circle5_3_outer.width() // 2),
                window.circle5_2_outer.y() + window.circle5_2_outer.height() + 30
            )

            window.circle5_3_inner.move(
                (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *4) + int(window.bodyContainer.width() / 16) - window.circle5_3_inner.width() // 2),
                window.circle5_3_outer.y() + 10 
            )

            window.circle5_4_outer.move(
                (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *4) + int(window.bodyContainer.width() / 16) - window.circle5_4_outer.width() // 2),
                window.circle5_3_outer.y() + window.circle5_3_outer.height() + 20
            )

            window.circle5_4_inner.move(
                (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *4) + int(window.bodyContainer.width() / 16) - window.circle5_4_inner.width() // 2),
                window.circle5_4_outer.y() + 10 
            )

            # Column 4

            window.circle4_1.move(
                (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *5) + int(window.bodyContainer.width() / 16) - window.circle4_1.width() // 2),
                window.circle5_1_inner.y() + int(1.5* window.circle4_1.radius)
            )

            window.circle4_2.move(
                (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *5) + int(window.bodyContainer.width() / 16) - window.circle4_2.width() // 2),
                window.circle5_3_inner.y() - int(1.5* window.circle4_2.radius) 
            )

            window.circle4_3.move(
                (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *5) + int(window.bodyContainer.width() / 16) - window.circle4_3.width() // 2),
                window.circle5_4_inner.y() + window.circle5_4_inner.height()//2 - window.circle4_3.height()//2
            )

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
                window.circle5_4_inner.y() + window.rounded4_3.height()
            )

            # Column 3
            window.rounded3_1.move(
                (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *6) + int(window.bodyContainer.width() / 16) - window.rounded3_1.width() // 2),
                window.circle5_1_inner.y() + window.rounded3_1.height()
            )

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

            # Column 2
            window.circle2_1.move(
                (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *7) + int(window.bodyContainer.width() / 16) - window.circle2_1.width() // 2),
                window.rounded3_1.y() + window.rounded3_1.height()//2 - window.circle2_1.height()//2
            )

            window.circle2_2.move(
                (window.bodyContainer.width() - (int(window.bodyContainer.width() / 8) *7) + int(window.bodyContainer.width() / 16) - window.circle2_2.width() // 2),
                window.circle2_1.y() + window.circle2_1.height() + int(window.circle2_2.height() * 0.5)
            )

            #Lines from 7 to 8

            hlineFtoA1_Length = abs(window.rounded7.width()//2 - int(0.75*window.column_width // 3))
            window.hlineWidgetFtoA1.setFixedSize(hlineFtoA1_Length, 3)
            window.hlineWidgetFtoA1.move(
                window.rounded7.x() + window.rounded7.width(),
                (window.column_height_light) // 2
            )

            hlineFtoA2_Length = abs(window.circle8_2.x() -( window.hlineWidgetFtoA1.x() + hlineFtoA1_Length))
            window.hlineWidgetFtoA2.setFixedSize(hlineFtoA2_Length, 3)
            window.hlineWidgetFtoA2.move(
                window.hlineWidgetFtoA1.x() + hlineFtoA1_Length,
                (window.column_height_light) // 2
            )

            vlineFtoP_length = abs(window.hlineWidgetFtoA1.y() - (window.rounded8_1.y() + window.rounded8_1.height()//2))  
            window.vlineWidgetFtoP.setFixedSize(3, vlineFtoP_length)
            window.vlineWidgetFtoP.move(
                window.hlineWidgetFtoA1.x() + hlineFtoA1_Length - 3,
                (window.column_height_light) // 2 - window.vlineWidgetFtoP.height() 
            )

            hlineFtoP_length = abs(window.circle8_1.x() - window.vlineWidgetFtoP.x() - 3)
            window.hlineWidgetFtoP.setFixedSize(hlineFtoP_length, 3) 
            window.hlineWidgetFtoP.move(
                window.vlineWidgetFtoP.x() + 3,
                (window.column_height_light) // 2 - window.vlineWidgetFtoP.height() 
            )

            vlineFtoD_length = abs(window.hlineWidgetFtoA1.y() - (window.rounded8_3.y() + window.rounded8_3.height()//2))
            window.vlineWidgetFtoD.setFixedSize(3, vlineFtoD_length )
            window.vlineWidgetFtoD.move(
                window.hlineWidgetFtoA1.x() + hlineFtoA1_Length - 3,
                window.hlineWidgetFtoA1.y() + 3
            )

            hlineFtoD_length = abs(window.circle8_3.x() - window.vlineWidgetFtoD.x() - 3)
            window.hlineWidgetFtoD.setFixedSize(hlineFtoD_length, 3)
            window.hlineWidgetFtoD.move(
                window.vlineWidgetFtoD.x() + 3 ,
                (window.column_height_light) // 2 + window.vlineWidgetFtoD.height()
            )

            # Lines from column 6 to 7
            
            collectorline_length = abs(window.hlineWidgettoCol2.y() - window.hlineWidgettoCol1.y())
            window.collectorLine6to7_1.setFixedSize(3, collectorline_length)
            window.collectorLine6to7_1.move(
                window.rounded7.x() + window.rounded7.width()//2 - int(1.25*window.column_width // 2) ,
                window.hlineWidgettoCol1.y() 
            )

            collectorline_length = abs(window.hlineWidgettoCol3.y() - window.hlineWidgettoCol2.y())
            window.collectorLine6to7_2.setFixedSize(3, collectorline_length)
            window.collectorLine6to7_2.move(
                window.collectorLine6to7_1.x(),
                window.hlineWidgettoCol2.y() 
            )

            collectorline_length = abs(window.hlineWidgettoCol4.y() - window.hlineWidgettoCol3.y()) 
            window.collectorLine6to7_3.setFixedSize(3, collectorline_length)
            window.collectorLine6to7_3.move(
                window.collectorLine6to7_1.x(),
                window.hlineWidgettoCol3.y() 
            )

            collectorline_length = abs(window.hlineWidgetColtoF.y() - window.hlineWidgettoCol4.y())
            window.collectorLine6to7_4.setFixedSize(3, collectorline_length)
            window.collectorLine6to7_4.move(
                window.collectorLine6to7_1.x(),
                window.hlineWidgettoCol4.y() 
            )

            collectorline_length = abs(window.hlineWidgettoCol5.y() - window.hlineWidgetColtoF.y())
            window.collectorLine6to7_5.setFixedSize(3, collectorline_length)
            window.collectorLine6to7_5.move(
                window.collectorLine6to7_1.x(),
                window.hlineWidgetColtoF.y() + 3
            )

            collectorline_length = abs(window.hlineWidgettoCol6.y() - window.hlineWidgettoCol5.y())
            window.collectorLine6to7_6.setFixedSize(3, collectorline_length)
            window.collectorLine6to7_6.move(
                window.collectorLine6to7_1.x(),
                window.hlineWidgettoCol5.y() +3
            )

            collectorline_length = abs(window.hlineWidgettoCol7.y() - window.hlineWidgettoCol6.y())
            window.collectorLine6to7_7.setFixedSize(3, collectorline_length)
            window.collectorLine6to7_7.move(
                window.collectorLine6to7_1.x(),
                window.hlineWidgettoCol6.y() +3
            )

            collectorline_length = abs(window.hlineWidgettoCol8.y() - window.hlineWidgettoCol7.y())
            window.collectorLine6to7_8.setFixedSize(3, collectorline_length)
            window.collectorLine6to7_8.move(
                window.collectorLine6to7_1.x(),
                window.hlineWidgettoCol7.y() +3
            )
        
            hlinetocol_length = abs(window.collectorLine6to7_1.x() - (window.rounded6_1.x() + window.rounded6_1.width()))
            window.hlineWidgettoCol1.setFixedSize(int(hlinetocol_length) + 3, 3)
            window.hlineWidgettoCol1.move(
                window.rounded6_1.x() + window.rounded6_1.width(),
                window.rounded6_1.y() + window.rounded6_1.height()//2
            )

            window.hlineWidgettoCol2.setFixedSize(int(hlinetocol_length), 3)
            window.hlineWidgettoCol2.move(
                window.rounded6_2.x() + window.rounded6_2.width(),
                window.rounded6_2.y() + window.rounded6_2.height()//2
            )

            window.hlineWidgettoCol3.setFixedSize(int(hlinetocol_length), 3)
            window.hlineWidgettoCol3.move(
                window.rounded6_3.x() + window.rounded6_3.width(),
                window.rounded6_3.y() + window.rounded6_3.height()//2
            )

            window.hlineWidgettoCol4.setFixedSize(int(hlinetocol_length), 3)
            window.hlineWidgettoCol4.move(
                window.rounded6_4.x() + window.rounded6_4.width(),
                window.rounded6_4.y() + window.rounded6_4.height()//2
            )

            window.hlineWidgettoCol5.setFixedSize(int(hlinetocol_length), 3)
            window.hlineWidgettoCol5.move(
                window.rounded6_5.x() + window.rounded6_5.width(),
                window.rounded6_5.y() + window.rounded6_5.height()//2
            )

            window.hlineWidgettoCol6.setFixedSize(int(hlinetocol_length), 3)
            window.hlineWidgettoCol6.move(
                window.rounded6_6.x() + window.rounded6_6.width(),
                window.rounded6_6.y() + window.rounded6_6.height()//2
            )

            window.hlineWidgettoCol7.setFixedSize(int(hlinetocol_length), 3)
            window.hlineWidgettoCol7.move(
                window.rounded6_7.x() + window.rounded6_7.width(),
                window.rounded6_7.y() + window.rounded6_7.height()//2
            )

            window.hlineWidgettoCol8.setFixedSize(int(hlinetocol_length), 3)
            window.hlineWidgettoCol8.move(
                window.rounded6_8.x() + window.rounded6_8.width(),
                window.rounded6_8.y() + window.rounded6_8.height()//2
            )

            hlinefromcol_length = abs(window.rounded7.x() - window.collectorLine6to7_1.x())
            window.hlineWidgetColtoF.setFixedSize(hlinefromcol_length, 3)
            window.hlineWidgetColtoF.move(
                window.collectorLine6to7_1.x() ,
                window.rounded7.y() + window.rounded7.height()//2
            )

            # Lines from column 5 to 6
           
            hlinetocol_length =  -window.circle5_1_outer.width()//2 + int(1.75*window.column_width//3) #abs(window.collectorLine5to6_1.x() - (window.circle5_1_outer.x() + window.circle5_1_outer.width() ))
            window.hlinetoCol5to6_1.setFixedSize(hlinetocol_length + 3, 3)
            window.hlinetoCol5to6_1.move(
                window.circle5_1_outer.x() + window.circle5_1_outer.width(),
                window.circle5_1_outer.y() + window.circle5_1_outer.height()//2
            )
            
            collectorLine5to6_1_length = window.circle5_1_outer.y() + window.circle5_1_outer.height()//2 - (window.rounded6_2.y() + window.rounded6_2.height()//2)
            window.collectorLine5to6_1.setFixedSize(window.LINEWIDTH, abs(collectorLine5to6_1_length) + 3)
            window.collectorLine5to6_1.move(
                window.hlinetoCol5to6_1.x() + hlinetocol_length,
                window.circle5_1_outer.y() + window.circle5_1_outer.height()//2
            )

            collectorLine5to6_1_1_length = window.collectorLine5to6_1.y() - collectorLine5to6_1_length - (window.rounded6_3.y() + window.rounded6_3.height()//2)
            window.collectorLine5to6_1_1.setFixedSize(3, abs(collectorLine5to6_1_1_length))
            window.collectorLine5to6_1_1.move(
                window.collectorLine5to6_1.x(),
                window.rounded6_2.y() + window.rounded6_2.height()//2 + 3
            )

            hlinefromcol_length = abs(window.circle6_1.x() - window.collectorLine5to6_1.x())
            window.hline1fromCol5to6_1.setFixedSize(hlinefromcol_length, 3)
            window.hline1fromCol5to6_1.move(
                window.collectorLine5to6_1.x(),
                window.rounded6_1.y() + window.rounded6_1.height()//2
            )

            window.hline2fromCol5to6_1.setFixedSize(hlinefromcol_length - 3, 3)
            window.hline2fromCol5to6_1.move(
                window.collectorLine5to6_1.x() + 3,
                window.rounded6_2.y() + window.rounded6_2.height()//2
            )

            window.hline3fromCol5to6_1.setFixedSize(hlinefromcol_length, 3)
            window.hline3fromCol5to6_1.move(
                window.collectorLine5to6_1.x(),
                window.rounded6_3.y() + window.rounded6_3.height()//2
            )

            verLineWidgetSertoP_length = (window.rounded6_4.y() + window.rounded6_4.height()//2) - (window.circle5_2_outer.y() + window.circle5_1_outer.height()//2 )
            window.verlineWidgetSertoP.setFixedSize(3, verLineWidgetSertoP_length)
            window.verlineWidgetSertoP.move(
                window.circle5_2_outer.x() + window.circle5_2_outer.width()//2 + int(1.25*window.column_width//3),
                window.circle5_2_outer.y() + window.circle5_2_outer.height()//2
            )

            hLineFromSertoVer_length = abs(window.verlineWidgetSertoP.x() - (window.circle5_2_outer.x() + window.circle5_2_outer.width()))
            window.horLineWidgetSertoVer.setFixedSize(hLineFromSertoVer_length, 3)
            window.horLineWidgetSertoVer.move(
                window.circle5_2_outer.x() + window.circle5_2_outer.width(),
                window.circle5_2_outer.y() + window.circle5_2_outer.height()//2
            )

            hlineVertoP_length = window.circle6_4.x() - window.verlineWidgetSertoP.x() 
            window.hlineWidgetVertoP.setFixedSize(hlineVertoP_length, 3)
            window.hlineWidgetVertoP.move(
                window.verlineWidgetSertoP.x() ,
                window.rounded6_4.y() + window.rounded6_4.height()//2
            )

            window.hlinetoCol5to6_2.setFixedSize(hlinetocol_length, 3)
            window.hlinetoCol5to6_2.move(
                window.circle5_3_outer.x() + window.circle5_3_outer.width(),
                window.circle5_3_outer.y() + window.circle5_3_outer.height()//2
            )

            collectorLine5to6_2_length = window.circle5_3_outer.y() + window.circle5_3_outer.height()//2 - (window.rounded6_5.y() + window.rounded6_5.height()//2)
            window.collectorLine5to6_2.setFixedSize(3, abs(collectorLine5to6_2_length) + 3)
            window.collectorLine5to6_2.move(
                window.hlinetoCol5to6_2.x() + hlinetocol_length,
                window.circle5_3_outer.y() + window.circle5_3_outer.height()//2
            )

            collectorLine5to6_2_2_length = window.collectorLine5to6_2.y() - collectorLine5to6_2_length - (window.rounded6_6.y() + window.rounded6_6.height()//2)
            window.collectorLine5to6_2_2.setFixedSize(3, abs(collectorLine5to6_2_2_length))
            window.collectorLine5to6_2_2.move(
                window.collectorLine5to6_2.x(),
                window.rounded6_5.y() + window.rounded6_5.height()//2 + 3
            )

            collectorLine5to6_2_3_length = window.collectorLine5to6_2_2.y() - collectorLine5to6_2_2_length - (window.rounded6_7.y() + window.rounded6_7.height()//2)
            window.collectorLine5to6_2_3.setFixedSize(3, abs(collectorLine5to6_2_3_length))
            window.collectorLine5to6_2_3.move(
                window.collectorLine5to6_2.x(),
                window.rounded6_6.y() + window.rounded6_6.height()//2 + 3
            )

            window.hline1fromCol5to6_2.setFixedSize(hlinefromcol_length - 3, 3)
            window.hline1fromCol5to6_2.move(
                window.collectorLine5to6_2.x() + 3,
                window.rounded6_5.y() + window.rounded6_5.height()//2
            )

            window.hline2fromCol5to6_2.setFixedSize(hlinefromcol_length - 3, 3)
            window.hline2fromCol5to6_2.move(
                window.collectorLine5to6_2.x() + 3,
                window.rounded6_6.y() + window.rounded6_6.height()//2 
            )

            window.hline3fromCol5to6_2.setFixedSize(hlinefromcol_length , 3)
            window.hline3fromCol5to6_2.move(
                window.collectorLine5to6_2.x(),
                window.rounded6_7.y() + window.rounded6_7.height()//2
            )

            verLineWidgetPosetoD_length = (window.rounded6_8.y() + window.rounded6_8.height()//2) - (window.circle5_4_outer.y() + window.circle5_4_outer.height()//2 )
            window.verlineWidgetPosetoD.setFixedSize(3, verLineWidgetPosetoD_length)
            window.verlineWidgetPosetoD.move(
                window.verlineWidgetSertoP.x(),
                window.circle5_4_outer.y() + window.circle5_4_outer.height()//2
            )

            hLineFromPosetoVer_length = abs(window.verlineWidgetPosetoD.x() - (window.circle5_4_outer.x() + window.circle5_4_outer.width()))
            window.hLineWidgetPosetoVer.setFixedSize(hLineFromPosetoVer_length, 3)
            window.hLineWidgetPosetoVer.move(
                window.circle5_4_outer.x() + window.circle5_4_outer.width(),
                window.circle5_4_outer.y() + window.circle5_4_outer.height()//2
            )

            hlineVertoD_length = window.circle6_8.x() - window.verlineWidgetPosetoD.x()
            window.hlineWidgetVertoD.setFixedSize(hlineVertoD_length, 3)
            window.hlineWidgetVertoD.move(
                window.verlineWidgetPosetoD.x() ,
                window.rounded6_8.y() + window.rounded6_8.height()//2
            )

            #Lines from 3 to 4 and 5
            hlineLength3to5 = abs(window.circle5_1_outer.x() - (window.rounded3_1.x() + window.rounded3_1.width()))
            hlineAudioToPara_length1 = int(1.25* window.column_width//3) + 2 - window.rounded3_1.width()//2 #(window.rounded3_1.x() + window.rounded3_1.width()//2 + window.column_width//2 + 2) - (window.rounded3_1.x() + window.rounded3_1.width())
            window.hlineWidgetAudiotoPara1.setFixedSize(hlineAudioToPara_length1 + window.LINEWIDTH, 3)
            window.hlineWidgetAudiotoPara1.move(
                window.rounded3_1.x() + window.rounded3_1.width(),
                window.rounded3_1.y() + window.rounded3_1.height()//2
            )

            window.hlineWidgetAudiotoPara2.setFixedSize(hlineLength3to5 - hlineAudioToPara_length1 - window.LINEWIDTH, 3)
            window.hlineWidgetAudiotoPara2.move(
                window.hlineWidgetAudiotoPara1.x() + hlineAudioToPara_length1 + window.LINEWIDTH,
                window.rounded3_1.y() + window.rounded3_1.height()//2
            )

            verLineWidgetAudiotoVoice_length = abs(window.hlineWidgetAudiotoPara1.y() - (window.rounded4_1.y() + window.rounded4_1.height()//2))
            window.verLineWidgetAudiotoVoice.setFixedSize(3, verLineWidgetAudiotoVoice_length - window.LINEWIDTH)
            window.verLineWidgetAudiotoVoice.move(
                window.hlineWidgetAudiotoPara1.x() + hlineAudioToPara_length1,
                window.hlineWidgetAudiotoPara1.y() + window.LINEWIDTH
            )

            hlineWidget_length = abs(window.rounded4_1.x() - window.verLineWidgetAudiotoVoice.x() )
            window.hlineWidgetAudiotoVoice.setFixedSize(hlineWidget_length, window.LINEWIDTH)
            window.hlineWidgetAudiotoVoice.move(
                window.verLineWidgetAudiotoVoice.x() ,
                window.verLineWidgetAudiotoVoice.y() + window.verLineWidgetAudiotoVoice.height()
            )

            window.hlineWidgetVoicetoPara.setFixedSize(hlineWidget_length + window.LINEWIDTH, 3)
            window.hlineWidgetVoicetoPara.move(
                window.rounded4_1.x() + window.rounded4_1.width() ,
                window.rounded4_1.y() + window.rounded4_1.height()//2
            )

            window.verLineWidgetVoicetoPara.setFixedSize(window.LINEWIDTH, verLineWidgetAudiotoVoice_length - window.LINEWIDTH)
            window.verLineWidgetVoicetoPara.move(
                window.hlineWidgetVoicetoPara.x() + hlineWidget_length,
                window.hlineWidgetAudiotoPara1.y() + 3
            )

            window.hlinewidgetTratoSen.setFixedSize(hlineLength3to5 , 3)
            window.hlinewidgetTratoSen.move(
                window.rounded3_2.x() + window.rounded3_2.width(),
                window.rounded3_2.y() + window.rounded3_2.height()//2
            )

            verlineWidgetAudiotoTra_length = abs(window.rounded3_2.y() - (window.rounded3_1.y() + window.rounded3_1.height()))
            window.verlineWidgetAudioToTra.setFixedSize(3, verlineWidgetAudiotoTra_length)
            window.verlineWidgetAudioToTra.move(
                window.rounded3_1.x() + window.rounded3_1.width()//2 ,
                window.rounded3_1.y() + window.rounded3_1.height()
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
            window.verlineWidgetVideotoFace.setFixedSize(3, verlineWidgetVideotoFace_length)
            window.verlineWidgetVideotoFace.move(
                window.verLineWidgetAudiotoVoice.x(),
                window.hlineWidgetVideotoFacial1.y() - window.verlineWidgetVideotoFace.height()
            )

            hlineWidget_length = abs(window.rounded4_2.x() - window.verlineWidgetVideotoFace.x() )
            window.hlineWidgetVideotoFace.setFixedSize(hlineWidget_length, 3)
            window.hlineWidgetVideotoFace.move(
                window.verlineWidgetVideotoFace.x() ,
                window.verlineWidgetVideotoFace.y() 
            )

            window.verlineWidgetFacetoFacial.setFixedSize(3, verlineWidgetVideotoFace_length)
            window.verlineWidgetFacetoFacial.move(
                window.verLineWidgetVoicetoPara.x(),
                window.hlineWidgetVideotoFacial1.y() - window.verlineWidgetFacetoFacial.height()
            )

            window.hlineWidgetFacetoFacial.setFixedSize(hlineWidget_length +1, 3)
            window.hlineWidgetFacetoFacial.move(
                window.rounded4_2.x() + window.rounded4_2.width() ,
                window.verlineWidgetFacetoFacial.y() 
            )

            verlineWidgetVideotoSkel_length = abs(window.rounded3_4.y() - (window.rounded3_3.y() + window.rounded3_3.height()))
            window.verlineWidgetVideotoSkel.setFixedSize(3, verlineWidgetVideotoSkel_length)
            window.verlineWidgetVideotoSkel.move(
                window.rounded3_3.x() + window.rounded3_3.width()//2 ,
                window.rounded3_3.y() + window.rounded3_3.height()
            )

            hlineWidgetSkeltoBody_length = abs(window.rounded4_3.x() - (window.rounded3_4.x() + window.rounded3_4.width()))
            window.hlineWidgetSkeltoBody.setFixedSize(hlineWidgetSkeltoBody_length, 3)
            window.hlineWidgetSkeltoBody.move(
                window.rounded3_4.x() + window.rounded3_4.width(),
                window.rounded3_4.y() + window.rounded3_4.height()//2
            )

            hlineWidgetBodytoPose_length = abs(window.circle5_4_outer.x() - (window.rounded4_3.x() + window.rounded4_3.width()))
            window.hlineWidgetBodytoPose.setFixedSize(hlineWidgetBodytoPose_length,3 )
            window.hlineWidgetBodytoPose.move(
                window.rounded4_3.x() + window.rounded4_3.width(),
                window.rounded4_3.y() + window.rounded4_3.height()//2
            )

            # Lines from 2 to 3

            hlineWidget_length = abs(window.rounded3_1.x() - (window.circle2_1.x() + window.circle2_1.width()))
            window.hlineWidgetHeadsettoAudio.setFixedSize(hlineWidget_length, 3)
            window.hlineWidgetHeadsettoAudio.move(
                window.circle2_1.x() + window.circle2_1.width(),
                window.circle2_1.y() + window.circle2_1.height()//2
            )                                

            verlineWidgetCamToVideo_length = abs((window.rounded3_3.y() + window.rounded3_3.height()//2 ) - (window.circle2_2.y() + window.circle2_2.height()//2))
            window.verlineWidgetCamToVideo.setFixedSize(3, verlineWidgetCamToVideo_length)
            window.verlineWidgetCamToVideo.move(
                window.circle2_2.x() + window.circle2_2.width()//2 + window.column_width//3 + 3,
                window.circle2_2.y() + window.circle2_2.height()//2
            )

            hlineWidgetCamtoVer_length = abs(window.verlineWidgetCamToVideo.x() - (window.circle2_2.x() + window.circle2_2.width()))
            window.hlineWidgetCamtoVer.setFixedSize(hlineWidgetCamtoVer_length, 3)
            window.hlineWidgetCamtoVer.move(
                window.circle2_2.x() + window.circle2_2.width(),
                window.verlineWidgetCamToVideo.y()
            )

            hlineWidgetVertoVideo_length = abs((window.rounded3_3.x()) - window.verlineWidgetCamToVideo.x())
            window.hlineWidgetVertoVideo.setFixedSize(hlineWidgetVertoVideo_length, 3)
            window.hlineWidgetVertoVideo.move(
                window.verlineWidgetCamToVideo.x(),
                window.rounded3_3.y() + window.rounded3_3.height()//2
            )

            #Buttons

            window.play_button.move(
                  window.column_width//2 - window.play_button.width()//2,
                    window.bodyContainer.height() - (3*window.play_button.height())
            )

            window.stop_button.move(
                  window.play_button.x() + window.play_button.width() + 10,
                    window.play_button.y())

            window.kafka_button.move(
                  window.stop_button.x() + window.stop_button.width() + 10,
                    window.play_button.y())
            
            window.udp_button.move(
                  window.kafka_button.x() + window.kafka_button.width() + 10,
                    window.play_button.y())

            window.console.move(
                    window.play_button.x(),
                        window.play_button.y() - window.console.height() - 10)
            
            return True
    return super(window.__class__, window).eventFilter(source, event)