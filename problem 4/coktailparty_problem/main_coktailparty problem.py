import numpy as np
import wave
from scipy.io import wavfile
import warnings
from scipy.io import wavfile
import sounddevice as sd
from sklearn.decomposition import FastICA
import matplotlib.pyplot as plt
from pydub import AudioSegment


import sys
from PyQt5 import QtWidgets
from gui_coktaialparty import Ui_MainWindow


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('coktail separation')

        self.ui.loadfile1.clicked.connect(self.loadfile_1)
        self.ui.loadfile2.clicked.connect(self.loadfile_2)
        self.ui.loadfile3.clicked.connect(self.loadfile_3)
        self.ui.sepearation.clicked.connect(self.sepearation1)
        self.ui.playsound1.clicked.connect(self.playsound1_1)
        self.ui.playsound2.clicked.connect(self.playsound1_2)
        self.ui.playsound3.clicked.connect(self.playsound1_3)
        self.ui.save1.clicked.connect(self.save_1)
        self.ui.save2.clicked.connect(self.save_2)
        self.ui.save3.clicked.connect(self.save_3)






        self.veiw1 = self.ui.graphicsView.plotItem.getViewBox()




    def loadfile_1(self):
        fileName_1_ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select Signal', '', '*.wav')
        #mix_1_wave = fileName_1_
        #print(fileName_1_)

        mix_1_wave = wave.open(fileName_1_[0])
        mix_1_wave.getparams()

        #mix_1_wave = AudioSegment.from_file(fileName_1_)
        print(mix_1_wave)

        signal_1_raw = mix_1_wave.readframes(-1)
        self.signal_1 = np.frombuffer(signal_1_raw, 'Int16')
        'length: ', len(self.signal_1), 'first 100 elements: ', self.signal_1[:100]

        self.fs = mix_1_wave.getframerate()
        self.timing = np.linspace(0, len(self.signal_1) / self.fs, num=len(self.signal_1))

        self.ui.graphicsView.plot(self.timing,self.signal_1, c="#3ABFE7")

    def loadfile_2(self):
        fileName_2_ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select Signal', '', '*.wav')
        #mix_1_wave = fileName_1_
        #print(fileName_1_)

        mix_2_wave = wave.open(fileName_2_[0])
        mix_2_wave.getparams()

        #mix_1_wave = AudioSegment.from_file(fileName_1_)
        print(mix_2_wave)

        signal_raw_2 = mix_2_wave.readframes(-1)
        self.signal_2 = np.fromstring(signal_raw_2, 'Int16')
        'length: ', len(self.signal_2), 'first 100 elements: ', self.signal_2[:100]

        self.fs = mix_2_wave.getframerate()
        self.timing = np.linspace(0, len(self.signal_2) / self.fs, num=len(self.signal_2))

        self.ui.graphicsView_2.plot(self.timing,self.signal_2, c="#3ABFE7")
        
    def loadfile_3(self):
        fileName_3_ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select Signal', '', '*.wav')
        #mix_1_wave = fileName_1_
        #print(fileName_1_)

        mix_3_wave = wave.open(fileName_3_[0])
        mix_3_wave.getparams()

        #mix_1_wave = AudioSegment.from_file(fileName_1_)
        print(mix_3_wave)

        signal_raw_3 = mix_3_wave.readframes(-1)
        self.signal_3 = np.fromstring(signal_raw_3, 'Int16')
        'length: ', len(self.signal_3), 'first 100 elements: ', self.signal_3[:100]

        self.fs = mix_3_wave.getframerate()
        self.timing = np.linspace(0, len(self.signal_3) / self.fs, num=len(self.signal_3))

        self.ui.graphicsView_3.plot(self.timing,self.signal_3, c="#3ABFE7")

    def sepearation1(self):
        X = list(zip(self.signal_1, self.signal_2, self.signal_3))

        # Let's peak at what X looks like
        X[:10]

        # Initialize FastICA with n_components=3
        ica = FastICA(n_components=3)

        # Run the FastICA algorithm using fit_transform on dataset X
        ica_result = ica.fit_transform(X)
        ica_result.shape
        result_signal_1 = ica_result[:, 0]
        result_signal_2 = ica_result[:, 1]
        result_signal_3 = ica_result[:, 2]

        # Convert to int, map the appropriate range, and increase the volume a little bit
        self.result_signal_1_int = np.int16(result_signal_1 * 32767 * 100)
        self.result_signal_2_int = np.int16(result_signal_2 * 32767 * 100)
        self.result_signal_3_int = np.int16(result_signal_3 * 32767 * 100)

        #sd.play(result_signal_1_int, self.fs)
        #sd.play(result_signal_2_int, self.fs)
        #sd.play(result_signal_3_int, self.fs)

        self.ui.graphicsView_4.plot(self.timing, result_signal_1)
        self.ui.graphicsView_5.plot(self.timing, result_signal_2)
        self.ui.graphicsView_6.plot(self.timing, result_signal_3)


    def playsound1_1(self):
        sd.play(self.result_signal_1_int, self.fs)


    def playsound1_2(self):
        sd.play(self.result_signal_2_int, self.fs)


    def playsound1_3(self):
        sd.play(self.result_signal_3_int, self.fs)

    def save_1(self):
        wavfile.write("result1.wav", self.fs, self.result_signal_1_int)

    def save_2(self):
        wavfile.write("result2.wav", self.fs, self.result_signal_2_int)

    def save_3(self):
        wavfile.write("result3.wav", self.fs, self.result_signal_3_int)




def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()

if __name__ == "__main__":
    main()