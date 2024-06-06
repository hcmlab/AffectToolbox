from GUI.main import MainWindow
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from GUI import ClickEvents
from kafka import KafkaConsumer

def sub_main():
    """Main function to run the application"""
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle("AffectPipeline")
    window.setWindowIcon(QIcon("./GUI/Icons/python.svg"))
    window.show() #Windowed mode
    #window.showFullScreen() #Fullscreen mode

    ClickEvents.PleasureClick(window)
    ClickEvents.ArousalClick(window)
    ClickEvents.DominanceClick(window)
    ClickEvents.ParaPleasureClick(window)
    ClickEvents.ParaArousalClick(window)
    ClickEvents.ParaDominanceClick(window)
    ClickEvents.VoiceActivityClick(window)
    ClickEvents.kafkaClick(window)

    ClickEvents.PlayButtonClick(window)

    app.exec()

def main():
    print("WAITING FOR KAFKA START MESSAGE")
    _KAFKA_IP = "127.0.0.1"
    _KAFKA_PORT = 9092
    kafka_address = _KAFKA_IP + ":" + str(_KAFKA_PORT)
    consumer = KafkaConsumer('MessageVSMLog',
                             bootstrap_servers=kafka_address)
    for message in consumer:

        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        print("%s:%d:%d: key=%s value=%s" % (
        message.topic, message.partition, message.offset, message.key, message.value))
        print(message.value.decode('utf-8'))
        if str(message.value.decode('utf-8')) == '\"Start_AffectToolBox\"':
            # print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key, message.value))
            print('NOW')
            sub_main()
    
if __name__ == "__main__":
    main()