import sys
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from piano import Ui_MainWindow



class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('piano')

        self.ui.pushButton.clicked.connect(self.pushButton_1)
        self.ui.pushButton_2.clicked.connect(self.pushButton__2)
        self.ui.pushButton_3.clicked.connect(self.pushButton__3)
        self.ui.pushButton_4.clicked.connect(self.pushButton__4)
        self.ui.pushButton_5.clicked.connect(self.pushButton__5)
        self.ui.pushButton_6.clicked.connect(self.pushButton__6)
        self.ui.pushButton_7.clicked.connect(self.pushButton__7)
        self.ui.pushButton_8.clicked.connect(self.pushButton__8)
        self.ui.pushButton_9.clicked.connect(self.pushButton__9)
        self.ui.pushButton_10.clicked.connect(self.pushButton__10)
        self.ui.pushButton_11.clicked.connect(self.pushButton__11)
        self.ui.pushButton_12.clicked.connect(self.pushButton__12)
        self.ui.pushButton_13.clicked.connect(self.pushButton__13)
        self.ui.pushButton_14.clicked.connect(self.pushButton__14)
        self.ui.pushButton_15.clicked.connect(self.pushButton__15)

        self.sampling = 44100
        self.freq = [130.8128, 146.8324, 164.8138, 174.6141,195.9977,
                     220.0000, 246.9417, 261.6256, 293.6648, 329.6276, 349.2282, 391.9954, 440.0000,
                     493.8833,523.2511]
        self.time = 2
    def pushButton_1(self):

        t = np.linspace(0,self.time,self.sampling)
        y = np.sin (2 * np.pi * self.freq[0] * t) * np.exp(-0.0004 * 2 * np.pi * self.freq[0] * t)
        print(y)
        plt.plot(t, y, '-o')
        #plt.show()
        sd.play(y,self.sampling)

    def pushButton__2(self):

        t = np.linspace(0,self.time,self.sampling)
        y = np.sin (2 * np.pi * self.freq[1] * t) * np.exp(-0.0004 * 2 * np.pi * self.freq[1] * t)
        print(y)
        plt.plot(t, y, '-o')
        #plt.show()
        sd.play(y,self.sampling)

    def pushButton__3(self):

        t = np.linspace(0,self.time,self.sampling)
        y = np.sin (2 * np.pi * self.freq[2] * t) * np.exp(-0.0004 * 2 * np.pi * self.freq[2] * t)
        print(y)
        plt.plot(t, y, '-o')
        #plt.show()
        sd.play(y,self.sampling)

    def pushButton__4(self):

        t = np.linspace(0,self.time,self.sampling)
        y = np.sin (2 * np.pi * self.freq[3] * t) * np.exp(-0.0004 * 2 * np.pi * self.freq[3] * t)
        print(y)
        plt.plot(t, y, '-o')
        #plt.show()
        sd.play(y,self.sampling)

    def pushButton__5(self):

        t = np.linspace(0,self.time,self.sampling)
        y = np.sin (2 * np.pi * self.freq[4] * t) * np.exp(-0.0004 * 2 * np.pi * self.freq[4] * t)
        print(y)
        plt.plot(t, y, '-o')
        #plt.show()
        sd.play(y,self.sampling)

    def pushButton__6(self):

        t = np.linspace(0,self.time,self.sampling)
        y = np.sin (2 * np.pi * self.freq[5] * t) * np.exp(-0.0004 * 2 * np.pi * self.freq[5] * t)
        print(y)
        plt.plot(t, y, '-o')
        #plt.show()
        sd.play(y,self.sampling)

    def pushButton__7(self):

        t = np.linspace(0,self.time,self.sampling)
        y = np.sin (2 * np.pi * self.freq[6] * t) * np.exp(-0.0004 * 2 * np.pi * self.freq[6] * t)
        print(y)
        plt.plot(t, y, '-o')
        #plt.show()
        sd.play(y,self.sampling)

    def pushButton__8(self):

        t = np.linspace(0,self.time,self.sampling)
        y = np.sin (2 * np.pi * self.freq[7] * t) * np.exp(-0.0004 * 2 * np.pi * self.freq[7] * t)
        print(y)
        plt.plot(t, y, '-o')
        #plt.show()
        sd.play(y,self.sampling)

    def pushButton__9(self):

        t = np.linspace(0,self.time,self.sampling)
        y = np.sin (2 * np.pi * self.freq[8] * t) * np.exp(-0.0004 * 2 * np.pi * self.freq[8] * t)
        print(y)
        plt.plot(t, y, '-o')
        #plt.show()
        sd.play(y,self.sampling)

    def pushButton__10(self):

        t = np.linspace(0,self.time,self.sampling)
        y = np.sin (2 * np.pi * self.freq[9] * t) * np.exp(-0.0004 * 2 * np.pi * self.freq[9] * t)
        print(y)
        plt.plot(t, y, '-o')
        #plt.show()
        sd.play(y,self.sampling)

    def pushButton__11(self):

        t = np.linspace(0,self.time,self.sampling)
        y = np.sin (2 * np.pi * self.freq[10] * t) * np.exp(-0.0004 * 2 * np.pi * self.freq[10] * t)
        print(y)
        plt.plot(t, y, '-o')
        #plt.show()
        sd.play(y,self.sampling)

    def pushButton__12(self):

        t = np.linspace(0,self.time,self.sampling)
        y = np.sin (2 * np.pi * self.freq[11] * t) * np.exp(-0.0004 * 2 * np.pi * self.freq[11] * t)
        print(y)
        plt.plot(t, y, '-o')
        #plt.show()
        sd.play(y,self.sampling)

    def pushButton__13(self):

        t = np.linspace(0,self.time,self.sampling)
        y = np.sin (2 * np.pi * self.freq[12] * t) * np.exp(-0.0004 * 2 * np.pi * self.freq[12] * t)
        print(y)
        plt.plot(t, y, '-o')
        #plt.show()
        sd.play(y,self.sampling)

    def pushButton__14(self):

        t = np.linspace(0,self.time,self.sampling)
        y = np.sin (2 * np.pi * self.freq[13] * t) * np.exp(-0.0004 * 2 * np.pi * self.freq[13] * t)
        print(y)
        plt.plot(t, y, '-o')
        #plt.show()
        sd.play(y,self.sampling)

    def pushButton__15(self):

        t = np.linspace(0,self.time,self.sampling)
        y = np.sin (2 * np.pi * self.freq[14] * t) * np.exp(-0.0004 * 2 * np.pi * self.freq[14] * t)
        print(y)
        plt.plot(t, y, '-o')
        #plt.show()
        sd.play(y,self.sampling)

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()

if __name__ == "__main__":
    main()
