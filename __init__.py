# -*- coding: utf-8 -*-
"""
Answer Visual Confirmation
an Addon for Anki
Github (https://github.com/my-Anki/Feedback-Visual-Confirmation)
Copyright (c) 2020 Shorouk Abdelaziz (https://shorouk.xyz)
"""
#################################################################################
# Permission is hereby granted, free of charge, to any person obtaining a copy  #
# of this software and associated documentation files (the "Software"), to deal #
# in the Software without restriction, including without limitation the rights  #
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell     #
# copies of the Software, and to permit persons to whom the Software is         #
# furnished to do so, subject to the following conditions:                      #
#                                                                               #
# The above copyright notice and this permission notice shall be included       #
# in all copies or substantial portions of the Software.                        #
# copies or substantial portions of the Software.                               #
#                                                                               #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR    #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,      #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE   #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER        #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, #
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE #
# SOFTWARE.                                                                     #
#                                                                               #
# Cridets                                                                       #
# animated icons from clipart.email (https://www.clipart.email/)                #
# still icons from Flaticon (https://www.flaticon.com/)                         #
# by Freepik (https://www.flaticon.com/authors/freepik)                         #
#################################################################################

import aqt
from aqt.reviewer import Reviewer
from aqt.qt import *
from aqt import mw
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtGui
from anki.hooks import addHook, wrap
import shutil , os , glob , random , sys
from bs4 import BeautifulSoup
CONFIG = mw.addonManager.getConfig(__name__)
from aqt.utils import showInfo , askUser , showText , tooltip

#defaults
theme = 'animated'
mode ="random"
interval = 100
duration = 1400
# get configs
duration = CONFIG['duration']
theme = CONFIG['theme']
mode = CONFIG['mode']
interval = CONFIG['gradual_interval']
ADDON = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")

def prepImages():
    iamges_list=[]
    for extension in ['png','gif']:
        lists = [glob.glob(ADDON+'/images/'+extension+'/'+level+'/*.'+extension) for level in ['easy' , 'good' , 'hard' , 'again'] ]

        ready_lists=[]
        for list in lists:
            difficulty_list = []
            for item in list:
                item = item.replace("\\", "/")
                difficulty_list.append(item)
            ready_lists.append(difficulty_list)
        iamges_list.append(ready_lists)
    return iamges_list

images = prepImages()

if theme == 'animated':
    imgs = images[1]
elif theme == "still":
    imgs = images[0]


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
    parent = mw.web
    img = QPixmap(type)
    w = img.width()
    h = img.height()

    lab.resize(w , h)
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


def display_answer_confirmation(self, ease ):
    count = len(self._answeredIds)
    selcted_pics = []
    if mode == 'random':
        for category in imgs:
            imgs_count = len(category)
            selector =random.randint(0, imgs_count-1)
            selcted_pics.append(category[selector])
    elif mode == 'gradual':
        lengths = [len(category) for category in imgs]
        imgs_count = min(lengths)
        for category in imgs:
            index = int(count / interval)
            if index > imgs_count-1:
                index = index % imgs_count
            selcted_pics.append(category[index])

    l = self._answerButtonList()
    a = [item for item in l if item[0] == ease]
    if len(a) > 0:
        status = BeautifulSoup(a[0][1], 'html.parser').get_text()
        if status == 'Again':
            myToolTip(selcted_pics[3])
        elif status == 'Hard':
            myToolTip(selcted_pics[2])
        elif status == 'Good':
            myToolTip(selcted_pics[1])
        elif status == 'Easy':
            myToolTip(selcted_pics[0])

Reviewer._answerCard = wrap(Reviewer._answerCard, display_answer_confirmation, "before")
