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
from fpdf import FPDF


##nota para si queda tiempo, muchos de los conjuntos para calcular diferentes cosas usan
# el "for position, datos in enumerate(data): cosa que despues se pueden unir a un solo loop for para reducirla cantidad
# de lineas que usa el programa, no es obligatorio pero es una opcion para mayor eficiencia
def inicio():
    def getedad(fnac, fmed):
        fecha_nacimiento = datetime.strptime(fnac, "%d/%m/%Y")
        fecha_ultima_cita = datetime.strptime(fmed, "%d/%m/%Y")
        edad = float(relativedelta(fecha_nacimiento, fecha_ultima_cita))
        return edad

    def cambio_paciente(contenido):
        for position, datos in enumerate(data):
            if str(datos.__dict__.get('t_pac')) == "Adulto":
                contadores[0] += 1
                contadores[2] += 1
            elif str(datos.__dict__.get('t_pac')) == "Atleta":
                contadores[1] += 1
                contadores[2] += 1

    data = []
    ##el contador contiene = pacientes adultos, pacientes atletas, pacientes totales, hombres, mujeres
    contadores = [0, 0, 0, 0, 0]
    edad_total = 0
    edad_prom = 0
    ##esto lee los pacientes del txt y los saca
    with open(f'pacientes.txt', 'rb') as file_new_d:
        while True:
            try:
                info = pickle.load(file_new_d)
                data.append(info)
            except EOFError:
                break
    ##esto llama a los pacientes y los cuenta el total ademas de contar por tipos de paciente y los asigna en sus label
    for position, datos in enumerate(data):
        if str(datos.__dict__.get('t_pac')) == "Adulto":
            contadores[0] += 1
            contadores[2] += 1
        elif str(datos.__dict__.get('t_pac')) == "Atleta":
            contadores[1] += 1
            contadores[2] += 1
        else:
            print("error")
    # self.lbl_patient_adulto_count.setText(contadores[0])
    # self.lbl_patient_atleta_count.setText(contadores[1])
    # self.lbl_patient_total.setText(contadores[2])

    ##esto calcula la edad promedio de los pacientes (no esta listo) y lo asigna en su label
    # for position, datos in enumerate(data):
    #     edad_total += getedad(str(datos.__dict__.get('fnacimiento')), str(datos.__dict__.get('fecha')))
    # edad_prom = edad_total / contadores[2]
    # self.lbl_edad_promedio.setText(edad_prom)

    ##esto calcula cuantos pacientes hombres y mujeres hay en el sistema y los coloca en sus labels
    for position, datos in enumerate(data):
        if str(datos.__dict__.get('sex')) == "Hombre":
            contadores[3] += 1
        elif str(datos.__dict__.get('sex')) == "Mujer":
            contadores[4] += 1
    # self.lbl_cant_hombres.setText(contadores[3])
    # self.lbl_cant_mujeres.setText(contadores[4])

    ##falta citas totales, se requiere un txt con minimo: 1 paciente con 1 cita y 1 paciente con 2 citas

    # for position, datos in enumerate(data):
    #     ##combobox_paciente1.addItem(str(datos.__dict__.get('name')), str(datos.__dict__.get('doc')))
    #
    # contenido = combobox_paciente1.currentText()
    # ##a este le hace falta un self.
    # combobox_paciente1.currentTextChanged.connect(cambio_paciente(contenido))


class Patient:
    def __init__(self, id, name, doc, t_pac, sex, country, fnacimiento, fecha, hora, medidas, act_deporte):
        self.id = id
        self.name = name
        self.doc = doc
        self.t_pac = t_pac
        self.sex = sex
        self.country = country
        self.fnacimiento = fnacimiento
        self.fecha = fecha
        self.hora = hora
        self.medidas = medidas
        self.act_deporte = act_deporte

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_doc(self):
        return self.doc

    def get_t_pac(self):
        return self.t_pac

    def get_sex(self):
        return self.sex

    def get_country(self):
        return self.country

    def get_fnacimiento(self):
        return self.fnacimiento

    def get_fecha(self):
        return self.fecha

    def get_hora(self):
        return self.hora

    def get_medidas(self):
        return self.medidas

    def get_actdeporte(self):
        return self.act_deporte


if __name__ == "__main__":
    inicio()
