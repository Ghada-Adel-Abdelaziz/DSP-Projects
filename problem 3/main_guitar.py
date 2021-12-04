import sys
import sounddevice as sd
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import pygame

from PyQt5 import QtWidgets
from guitar import Ui_MainWindow


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('guitar')

        self.ui.pushButton.clicked.connect(self.pushButton__1)
        self.ui.pushButton_2.clicked.connect(self.pushButton__2)
        self.ui.pushButton_3.clicked.connect(self.pushButton__3)
        self.ui.pushButton_4.clicked.connect(self.pushButton__4)
        self.ui.pushButton_5.clicked.connect(self.pushButton__5)
        self.ui.pushButton_6.clicked.connect(self.pushButton__6)

        self.freq = [329.63, 246.94, 246.94, 146.83, 110.00, 82.41]
        self.fs = 44100
    def karplus_strong(self,wavetable, n_samples):

        samples = []
        current_sample = 0
        previous_value = 0
        while len(samples) < n_samples:
            wavetable[current_sample] = 0.5 * (wavetable[current_sample] + previous_value)
            samples.append(wavetable[current_sample])
            previous_value = samples[-1]
            current_sample += 1
            current_sample = current_sample % wavetable.size
        return np.array(samples)


    def pushButton__1(self):
        wavetable_size =  self.fs //int (self.freq[0])
        wavetable = (2 * np.random.randint(0, 2, wavetable_size) - 1).astype(np.float)
        plt.plot(wavetable)
        #plt.show()

        sample1 = self.karplus_strong(wavetable, 2 * self.fs)

        sd.play(sample1,self.fs)

    def pushButton__2(self):
        wavetable_size =  self.fs //int (self.freq[1])
        wavetable = (2 * np.random.randint(0, 2, wavetable_size) - 1).astype(np.float)
        plt.plot(wavetable)
        #plt.show()

        sample1 = self.karplus_strong(wavetable, 2 * self.fs)

        sd.play(sample1,self.fs)

    def pushButton__3(self):
        wavetable_size =  self.fs //int (self.freq[2])
        wavetable = (2 * np.random.randint(0, 2, wavetable_size) - 1).astype(np.float)
        plt.plot(wavetable)
        #plt.show()

        sample1 = self.karplus_strong(wavetable, 2 * self.fs)

        sd.play(sample1,self.fs)

    def pushButton__4(self):
        wavetable_size =  self.fs //int (self.freq[3])
        wavetable = (2 * np.random.randint(0, 2, wavetable_size) - 1).astype(np.float)
        plt.plot(wavetable)
        #plt.show()

        sample1 = self.karplus_strong(wavetable, 2 * self.fs)

        sd.play(sample1,self.fs)

    def pushButton__5(self):
        wavetable_size =  self.fs //int (self.freq[4])
        wavetable = (2 * np.random.randint(0, 2, wavetable_size) - 1).astype(np.float)
        plt.plot(wavetable)
        #plt.show()

        sample1 = self.karplus_strong(wavetable, 2 * self.fs)

        sd.play(sample1,self.fs)

    def pushButton__6(self):
        wavetable_size =  self.fs //int (self.freq[5])
        wavetable = (2 * np.random.randint(0, 2, wavetable_size) - 1).astype(np.float)
        plt.plot(wavetable)
        #plt.show()

        sample1 = self.karplus_strong(wavetable, 2 * self.fs)

        sd.play(sample1,self.fs)

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()

if __name__ == "__main__":
    main()