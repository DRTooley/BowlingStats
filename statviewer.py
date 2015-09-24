__author__ = 'David'

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from button import menuButton

import sqlite3
import matplotlib.pyplot as pyplot
import CalculateStats as cs
from bowlingentry import BowlingEntry



class statViewer(QGraphicsView):
    def __init__(self):
        super(statViewer, self).__init__()

        self.bgPixmap = QPixmap("images/main_background.png")
        self.getBowlingInfo()
        self.viewSetUp()
        self.sceneCreation()

        self.timer.timeout.connect(self.scene.advance)
        self.timer.start(1)



    def getBowlingInfo(self):
        dbcon = sqlite3.connect("BowlingDatabase.db")
        cursor = dbcon.cursor()
        cursor.execute("SELECT * FROM stats")
        self.bowling_information = [BowlingEntry(row) for row in cursor]
        dbcon.close()

    def viewSetUp(self):
        QShortcut(QKeySequence("Ctrl+Q"), self, self.close)
        self.drawBackground(QPainter(), self.sceneRect())
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pixList = []
        self.timer = QTimer()

    def sceneCreation(self):
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        self.addButtons()

    def addButtons(self):
        buttonParent = QGraphicsRectItem()
        oneButton = menuButton(buttonParent, "Multi-Game Avg")
        oneButton.pressed.connect(self.oneButtonPress)
        twoButton = menuButton(buttonParent, "Hot Streak")
        twoButton.pressed.connect(self.twoButtonPress)
        threeButton = menuButton(buttonParent, "High Games")
        threeButton.pressed.connect(self.threeButtonPress)

        oneButton.setPos(0, 0)
        twoButton.setPos(0, 50)
        threeButton.setPos(200, 0)

        self.scene.addItem(buttonParent)
        buttonParent.setPos(100, 100)
        buttonParent.setZValue(65)

    def pictureRotation(self):
        self.scene.advance()

    def drawBackground(self, painter, QRectF):
        painter.drawPixmap(QRectF.topLeft(), self.bgPixmap)

    def oneButtonPress(self):
        cs.multiple_game_average(self.bowling_information)
        pyplot.show()

    def twoButtonPress(self):
        cs.calculate_longest_hot_streak(self.bowling_information, 200)
        pyplot.show()

    def threeButtonPress(self):
        cs.graph_yearly_high_scores(self.bowling_information)
        pyplot.show()