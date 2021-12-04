from __future__ import print_function
import sys
from PyQt5 import QtWidgets
from gui_vocabseperation import Ui_MainWindow
import numpy as np
import librosa
import sounddevice as sd
import librosa.display




class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('vocal separation')

        self.ui.seperation.clicked.connect(self.load_seperation)
        self.ui.play_sound.clicked.connect(self.play__music)
        self.ui.play_vocab.clicked.connect(self.play__vocab)
        self.ui.pushButton.clicked.connect(self.save__music)
        self.ui.pushButton_2.clicked.connect(self.save__vocab)
        self.ui.pushButton_3.clicked.connect(self.stop_sound)

        self.veiw1 = self.ui.graphicsView.plotItem.getViewBox()
        self.veiw2 = self.ui.graphicsView_2.plotItem.getViewBox()





    def load_seperation(self ):
        #y, sr = librosa.load('C:/Users/cd/Desktop/test/problem 4/Felo.Haylman.El.Baba.El.Gded.mp3', duration=120)
        #write code that load song and seperate it and plot each music and vocabe

        # Load song.
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '', '*.mp3')
        print(filename)


        #print(y)
        y, sr = librosa.load(filename, duration=120)
        print(y)
        self.sr =sr


        # And compute the spectrogram magnitude and phase
        S_full, phase = librosa.magphase(librosa.stft(y))

        S_filter = librosa.decompose.nn_filter(S_full,
                                               aggregate=np.median,
                                               metric='cosine',
                                               width=int(librosa.time_to_frames(2, sr=sr)))

        S_filter = np.minimum(S_full, S_filter)

        margin_i, margin_v = 2, 9
        power = 2

        mask_i = librosa.util.softmask(S_filter,
                                       margin_i * (S_full - S_filter),
                                       power=power)

        mask_v = librosa.util.softmask(S_full - S_filter,
                                       margin_v * S_filter,
                                       power=power)
        # to separate the components

        S_foreground = mask_v * S_full
        S_background = mask_i * S_full
        D_foreground = S_foreground * phase
        self.y_foreground = librosa.istft(D_foreground)

        D_background = S_background * phase
        self.y_background = librosa.istft(D_background)

        Time_1 = np.linspace(0, len(self.y_foreground) / sr, num=len(self.y_foreground))
        Time_2 = np.linspace(0, len(self.y_background) / sr, num=len(self.y_background))

        self.ui.graphicsView.clear()
        self.ui.graphicsView.plot(Time_1, self.y_foreground)
        self.ui.graphicsView_2.plot(Time_2, self.y_background)

        return self.sr , self.y_foreground ,self.y_background



    def play__music(self):
        sd.play(self.y_background, self.sr)
        print("pass1")


    #write code that make music play after seperation

    def play__vocab(self):
        sd.play(self.y_foreground * 100, self.sr)
        print("pass2")


    # write code that make vocab play after seperation


    def save__music(self):
        librosa.output.write_wav('music.wav', self.y_background, self.sr)


    def save__vocab(self):
        librosa.output.write_wav('voice.wav', self.y_foreground * 100, self.sr)


    def stop_sound(self):
        sd.stop()

        # write code that make vocab save after seperation






'''
# Load song.
#y, sr = librosa.load('/Users/Saiko-Store/Desktop/dsp/task4/secrettttt.mp3', duration=120)

# And compute the spectrogram magnitude and phase
#S_full, phase = librosa.magphase(librosa.stft(y))

#S_filter = librosa.decompose.nn_filter(S_full,
                                       aggregate=np.median,
                                       metric='cosine',
                                       width=int(librosa.time_to_frames(2, sr=sr)))

This is a multiline
comment.

S_filter = np.minimum(S_full, S_filter)

margin_i, margin_v = 2, 9
power = 2

mask_i = librosa.util.softmask(S_filter,
                               margin_i * (S_full - S_filter),
                               power=power)

mask_v = librosa.util.softmask(S_full - S_filter,
                               margin_v * S_filter,
                               power=power)
# to separate the components

S_foreground = mask_v * S_full
S_background = mask_i * S_full
D_foreground = S_foreground * phase
y_foreground = librosa.istft(D_foreground)

D_background = S_background * phase
y_background = librosa.istft(D_background)

# Save foreground in .wav format
Time = np.linspace(0, len(y_foreground) / sr, num=len(y_foreground))
plt.plot(Time, y_foreground)

plt.show()
librosa.output.write_wav('voice.wav', y_foreground * 100, sr)

sd.play(y_foreground * 100, sr)
sd.stop()

# Save background in .wav format
Time = np.linspace(0, len(y_background) / sr, num=len(y_background))
plt.plot(Time, y_background)
plt.show()
sd.play(y_background, sr)

librosa.output.write_wav('music.wav', y_background *100, sr)
sd.play(y_background* 100, sr)
sd.stop()
'''

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()

if __name__ == "__main__":
    main()
