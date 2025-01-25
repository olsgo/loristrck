import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction, QVBoxLayout, QWidget, QLabel, QPushButton, QSlider, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from . import util, _core

class AudioAnalysisApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Audio Analysis and Resynthesis')
        self.setGeometry(100, 100, 800, 600)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout(self.main_widget)

        self.load_button = QPushButton('Load Audio File', self)
        self.load_button.clicked.connect(self.load_audio_file)
        self.layout.addWidget(self.load_button)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.slider_label = QLabel('Analysis Resolution:', self)
        self.layout.addWidget(self.slider_label)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(30)
        self.slider.setMaximum(200)
        self.slider.setValue(60)
        self.slider.valueChanged.connect(self.update_analysis)
        self.layout.addWidget(self.slider)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')

        loadAct = QAction(QIcon('load.png'), 'Load', self)
        loadAct.setShortcut('Ctrl+L')
        loadAct.triggered.connect(self.load_audio_file)
        fileMenu.addAction(loadAct)

        saveAct = QAction(QIcon('save.png'), 'Save', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.triggered.connect(self.save_audio_file)
        fileMenu.addAction(saveAct)

        self.show()

    def load_audio_file(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Load Audio File", "", "Audio Files (*.wav *.aif *.aiff)", options=options)
        if fileName:
            self.audio_data, self.sr = util.sndreadmono(fileName)
            self.update_analysis()

    def save_audio_file(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save Audio File", "", "Audio Files (*.wav *.aif *.aiff)", options=options)
        if fileName:
            util.sndwrite(self.processed_audio, self.sr, fileName)

    def update_analysis(self):
        resolution = self.slider.value()
        self.partials = _core.analyze(self.audio_data, self.sr, resolution)
        self.visualize_partials()

    def visualize_partials(self):
        self.ax.clear()
        util.plot_partials(self.partials, ax=self.ax)
        self.canvas.draw()

    def apply_transformation(self, transformation):
        self.partials = transformation(self.partials)
        self.visualize_partials()

    def time_stretch(self, factor):
        self.apply_transformation(lambda p: util.partials_stretch(p, factor))

    def frequency_shift(self, shift):
        self.apply_transformation(lambda p: util.partials_transpose(p, shift))

    def harmonic_remap(self, mapping):
        self.apply_transformation(lambda p: util.partials_transpose(p, mapping))

    def playback(self):
        self.processed_audio = _core.synthesize(self.partials, self.sr)
        util.play(self.processed_audio, self.sr)

    def export(self, filename):
        util.sndwrite(self.processed_audio, self.sr, filename)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AudioAnalysisApp()
    sys.exit(app.exec_())
