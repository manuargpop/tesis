from datetime import datetime
from functools import partial
from math import log
import pickle
from PyQt6 import QtCore, QtGui, QtWidgets, Qt6
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QParallelAnimationGroup, QRegularExpression
from PyQt6.QtWidgets import QMessageBox, QSpinBox, QHeaderView, QApplication
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QRegularExpressionValidator
from dateutil.relativedelta import relativedelta

porcent_grasa = 12 + 15 + 8 + 28 ##63 = 63
porcent_grasa_con_log = log(63, 10) ##1.7993405494535815

dato6 = 1.1581 - (0.0720 * porcent_grasa_con_log) ## -0.12955251956065788278176358868741 1.0285474804393421172182364113126
dato7 = ((4.95 / dato6) - 4.50) * 100 ##31.261205159495100012521912737939
print(dato7)
##91.4 * ((100 - dato7 / 100) + 6.1 * (1.8 * 1.74)) / 1.74 ** 2
indice_mlg1 = 100 - dato7 / 100 ##99.9 sin parentesis 0.687
print(indice_mlg1)
indice_mlg2 = 1.8 * 1.74
print(indice_mlg2)
indice_mlg3 = indice_mlg1 + 6.1 * indice_mlg2
print(indice_mlg3)
indice_mlg4 = 91.4 * indice_mlg3
print(indice_mlg4)
indice_mlg = indice_mlg4 / 1.74 ** 2
print(indice_mlg)
imc = 91.4 / (1.745 ** 2)

