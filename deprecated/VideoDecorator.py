import cv2
import threading


class VideoShow:
    """
    Class that continuously shows a frame using a dedicated thread.
    """

    def __init__(self, name, x, y, w, h, frame=None):
        self.frame = frame
        self.stopped = False
        self.id = name
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def start(self):
        # threading.Thread(target=self.show, args=[self.id]).start()
        threading.Thread(target=self.show, args="").start()
        return self

    def show(self):
        while not self.stopped:
            try:
                # cv2.imshow(str(id), self.frame)
                cv2.namedWindow(str(self.id), cv2.WINDOW_NORMAL)
                cv2.imshow(str(self.id), self.frame)
                cv2.resizeWindow(str(self.id), self.w, self.h)
                cv2.moveWindow(str(self.id), self.x, self.y)
            except:
                pass
                #print("CV stream type error")
                #print(self.frame)
            if cv2.waitKey(1) == ord("q"):
                self.stopped = True

    def stop(self):
        self.stopped = True