#  Copyright (c) 2019 Phil Birkelbach
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *

import fix
from .abstract import AbstractGauge
from .verticalBar import VerticalBar

class EGTGroup(QWidget):
    def __init__(self, parent=None, cylinders = 4, dbkeys = ["EGT11", "EGT12", "EGT13", "EGT14"]):
        super(EGTGroup, self).__init__(parent)
        self.setMinimumSize(50, 100)
        self.bars = []
        self.conversionFunction = lambda x: x * (9.0/5.0) + 32.0
        for i in range(cylinders):
            bar = VerticalBar(self)
            bar.name = str(i+1)
            bar.decimalPlaces = 0
            bar.showUnits = False
            self.bars.append(bar)
        self.smallFontPercent = 0.08
        self.bigFontPercent = 0.10



    def resizeEvent(self, event):
        cylcount = len(self.bars)
        barwidth = self.width() / cylcount
        barheight = self.height()
        x = 0
        for bar in self.bars:
            bar.resize(barwidth, barheight)
            bar.move(barwidth * x, 0)
            x += 1
        # self.barWidth = self.width() * self.barWidthPercent
        # self.lineWidth = self.width() * self.lineWidthPercent
        # self.bigFont = QFont()
        # self.bigFont.setPixelSize(self.height() * self.bigFontPercent)
        # self.smallFont = QFont()
        # self.smallFont.setPixelSize(self.height() * self.smallFontPercent)
        # if self.showName:
        #     self.barTop = self.smallFont.pixelSize() + self.textGap
        # else:
        #     self.barTop = 1
        # self.barBottom = self.height()
        # if self.showValue:
        #     self.barBottom -= (self.bigFont.pixelSize() + self.textGap)
        # if self.showUnits:
        #     self.barBottom -= (self.smallFont.pixelSize() + self.textGap)
        #
        # self.barLeft = (self.width() - self.barWidth) / 2
        # self.barRight = self.barLeft + self.barWidth
        # self.lineLeft = (self.width() - self.lineWidth) / 2
        # self.lineRight = self.lineLeft + self.lineWidth
        # self.barHeight = self.barBottom - self.barTop
        #
        # self.nameTextRect = QRectF(0, 0, self.width(), self.smallFont.pixelSize())
        # self.valueTextRect = QRectF(0, self.barBottom + self.textGap, self.width(), self.bigFont.pixelSize())
        # self.unitsTextRect = QRectF(0, self.height() - self.smallFont.pixelSize() - self.textGap, self.width(), self.smallFont.pixelSize())
        # self.ballRadius = self.barWidth * 0.40
        # self.ballCenter = QPointF(self.barLeft + (self.barWidth / 2), self.barBottom - (self.barWidth/2))

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        pen = QPen()
        pen.setWidth(1)
        pen.setCapStyle(Qt.FlatCap)
        p.setPen(pen)
        # opt = QTextOption(Qt.AlignCenter)
        # if self.showName:
        #     pen.setColor(self.textColor)
        #     p.setPen(pen)
        #     p.setFont(self.smallFont)
        #     p.drawText(self.nameTextRect, self.name, opt)
        # if self.showValue:
        #     # Draw Value
        #     pen.setColor(self.valueColor)
        #     p.setPen(pen)
        #     p.setFont(self.bigFont)
        #     p.drawText(self.valueTextRect, self.valueText, opt)
        # if self.showUnits:
        #     # Units
        #     pen.setColor(self.textColor)
        #     p.setPen(pen)
        #     p.setFont(self.smallFont)
        #     p.drawText(self.unitsTextRect, self.units, opt)
        #
        #
        # # Draws the bar
        # p.setRenderHint(QPainter.Antialiasing, False)
        # pen.setColor(self.safeColor)
        # brush = self.safeColor
        # p.setPen(pen)
        # p.setBrush(brush)
        # p.drawRect(self.barLeft, self.barTop, self.barWidth, self.barHeight)
        #
        # # Draw Warning Bands
        # pen.setColor(self.warnColor)
        # brush = self.warnColor
        # p.setPen(pen)
        # p.setBrush(brush)
        # if(self.lowWarn and self.lowWarn >= self.lowRange):
        #     x = self.interpolate(self.lowWarn, self.barHeight)
        #     p.drawRect(self.barLeft, self.barBottom - x,
        #                self.barWidth,
        #                x + 1)
        # if(self.highWarn and self.highWarn <= self.highRange):
        #     p.drawRect(self.barLeft, self.barTop,
        #                self.barWidth,
        #                self.barHeight - self.interpolate(self.highWarn, self.barHeight))
        #
        # pen.setColor(self.alarmColor)
        # brush = self.alarmColor
        # p.setPen(pen)
        # p.setBrush(brush)
        # if(self.lowAlarm and self.lowAlarm >= self.lowRange):
        #     x = self.interpolate(self.lowAlarm, self.barHeight)
        #     p.drawRect(self.barLeft, self.barBottom - x,
        #                self.barWidth,
        #                x + 1)
        # if(self.highAlarm and self.highAlarm <= self.highRange):
        #     p.drawRect(self.barLeft, self.barTop,
        #                self.barWidth,
        #                self.barHeight - self.interpolate(self.highAlarm, self.barHeight))
        #
        # # Highlight Ball
        # if self.highlight:
        #     pen.setColor(Qt.black)
        #     pen.setWidth(1)
        #     p.setPen(pen)
        #     p.setBrush(self.highlightColor)
        #     p.drawEllipse(self.ballCenter, self.ballRadius, self.ballRadius)
        #
        # # Indicator Line
        # pen.setColor(self.penColor)
        # brush = QBrush()
        # pen.setWidth(4)
        # p.setPen(pen)
        # p.setBrush(brush)
        # x = self.barTop + (self.barHeight - self.interpolate(self._value, self.barHeight))
        # if x < self.barTop: x = self.barTop
        # if x > self.barBottom: x = self.barBottom
        # p.drawLine(self.lineLeft, x,
        #            self.lineRight, x)
