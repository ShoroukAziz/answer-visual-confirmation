# -*- coding: utf-8 -*-
"""
Feedback Visual Confirmation
an Addon for Anki
Github (https://github.com/my-Anki/Feedback-Visual-Confirmation)

Copyright (c) 2020 Shorouk Abdelaziz (https://shorouk.xyz)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Cridets
animated icons from clipart.email (https://www.clipart.email/)
still icons from Flaticon (https://www.flaticon.com/) by Freepik (https://www.flaticon.com/authors/freepik)
"""

import aqt
from aqt.reviewer import Reviewer
from aqt.qt import *
from aqt import mw
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtGui
from anki.hooks import addHook, wrap
import shutil , os
from bs4 import BeautifulSoup
CONFIG = mw.addonManager.getConfig(__name__)

#defaults
theme = 'still'
duration = 1500
duration = CONFIG['duration']
theme = CONFIG['theme']

ADDON = os.path.dirname(os.path.abspath(__file__))
ADDON = ADDON.replace("\\", "/")


if theme == 'animated':
    img = ADDON+"/thumpsUp.gif"
    imgFail = ADDON+"/thumpsDown.gif"
elif theme == 'still':
    img = ADDON+"/like.png"
    imgFail = ADDON+"/heartbreak.png"

ttTimer  = None
ttLabel = None


def myToolTip(type, parent: QWidget = None):
    global ttTimer, ttLabel

    closeTooltip()
    aw = parent or mw.app.activeWindow() or mw
    lab = QLabel(aw,)
    movie = QtGui.QMovie(type)
    lab.setMovie(movie)
    movie.start()
    lab.resize(256, 256)
    parent = mw.web
    center = (parent.frameGeometry().center() - lab.frameGeometry().center())
    lab.move(center)
    lab.show()
    ttTimer = mw.progress.timer(duration, closeTooltip, False)
    ttLabel = lab


def closeTooltip():
    global ttLabel, ttTimer
    if ttLabel:
        try:
            ttLabel.deleteLater()
        except:
            pass
        ttLabel = None
    if ttTimer:
        ttTimer.stop()
        ttTimer = None


def answerCard_before(self, ease):
    l = self._answerButtonList()
    a = [item for item in l if item[0] == ease]
    if len(a) > 0:
        if BeautifulSoup(a[0][1], 'html.parser').get_text() != 'Again':
            myToolTip(img)
        else:
            myToolTip(imgFail)


Reviewer._answerCard = wrap(Reviewer._answerCard, answerCard_before, "before")
