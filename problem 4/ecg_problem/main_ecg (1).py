import numpy as np
from sklearn.decomposition import  FastICA
import sys
from PyQt5 import QtWidgets
from gui_ecg import Ui_MainWindow


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('ecg separation')

        self.ui.seperation.clicked.connect(self.load)
        self.ui.pushButton_3.clicked.connect(self.seperation)


        self.signals_ica = 0
    
    def load(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '', '*.txt')
        X = np.loadtxt(filename)

        # Plotting input signal
        for i in range(X.shape[1]):
            self.ui.graphicsView.plot(X[:,i])
            
        # Compute ICA
        ica = FastICA(n_components=5)

        # Reconstruct the signals
        self.signals_ica = ica.fit_transform(X)

    def seperation(self):
        # Plotting ICA signals     
        self.ui.graphicsView_2.plot(self.signals_ica[:,0])
        self.ui.graphicsView_3.plot(self.signals_ica[:,1])
        self.ui.graphicsView_4.plot(self.signals_ica[:,2])
        self.ui.graphicsView_5.plot(self.signals_ica[:,3])        

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()

if __name__ == "__main__":
    main()
