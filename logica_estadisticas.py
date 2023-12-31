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


# nota para si queda tiempo, muchos de los conjuntos para calcular diferentes cosas usan
# el "for position, datos in enumerate(data): cosa que despues se pueden unir a un solo loop for para reducirla cantidad
# de lineas que usa el programa, no es obligatorio pero es una opcion para mayor eficiencia

def inicio():
    def getedad(fnac, fmed):
        fecha_nacimiento = datetime.strptime(fnac, "%d/%m/%Y")
        fecha_ultima_cita = datetime.strptime(fmed, "%d/%m/%Y")
        edad = float(relativedelta(fecha_nacimiento, fecha_ultima_cita))
        return edad

    # funcion para llenar la lista de cita 1 y 2 y la lista de datos a comparar
    def cambio_paciente(max):
        contenido_raw = combobox_paciente1.currentText()
        contenido_split = contenido_raw.split
        contenido = contenido_split[1]
        tipo = contenido_split[2]
        datos_adulto = ("0 ESTATURA", "1 PESO", "2 PROFUNDIDAD ABDOMINAL", "3 PLIEGUES TRICEPS",
                        "4 PLIEGUES SUBESCAPULAR", "5 PLIEGUES BICEPS", "6 PLIEGUES CRESTA ILIACA",
                        "7 PERIMETRO BRAZO RELAJADO", "8 PERIMETRO BRAZO FLEXIONADO CONTRAIDO", "9 PERIMETRO MUÑECA",
                        "10 PERIMETRO MINIMO CINTURA", "11 PERIMETRO ABDOMINAL", "12 PERIMETRO CADERAS")
        datos_atleta = ("0 ESTATURA", "1 PESO", "2 PROFUNDIDAD ABDOMINAL",
                        "3 PLIEGUES TRICEPS", "4 PLIEGUES CRESTA ILIACA", "5 PERIMETRO CINTURA MINIMA"
                        "6 PLIEGUES ABDOMINAL", "7 PERIMETRO BRAZO FLEXIONADO CONTRAIDO",
                        "8 PERIMETRO ABDOMINAL", "9 PERIMETRO MUSLO MEDIO")
    
        if tipo == "Adulto":
            contador_tipo = 0
            while contador_tipo < 13:
                combobox_dato.addItem(datos_adulto[contador_tipo])
                print(datos_adulto[contador_tipo])
                contador_tipo += 1
            print("done")
        elif tipo == "Atleta":
            contador_tipo = 0
            while contador_tipo < 11:
                combobox_dato.addItem(datos_atleta[contador_tipo])
                print(datos_adulto[contador_tipo])
                contador_tipo += 1
            print("done")
        contador_p = 0
        contador_c = 0
        while contador_p < max:
            if contenido == all_data[contador_p][3]:
                print("good paciente")
                while contador_c < len(all_data[contador_p][1]):
                    if contador_c != 0:
                        combobox_cita1.addItem(str(contador_c),str(all_data[contador_p][1][contador_c][13]),
                        str(all_data[contador_p][1][contador_c][14]))
                        combobox_cita2.addItem(str(contador_c),str(all_data[contador_p][1][contador_c][13]),
                        str(all_data[contador_p][1][contador_c][14]))
                        contador_c += 1
                    else:
                        combobox_cita1.addItem(str(contador_c)str(all_data[contador_p][4]),
                        str(all_data[contador_p][5]))
                        combobox_cita2.addItem(str(contador_c)str(all_data[contador_p][4]),
                        str(all_data[contador_p][5]))
                        contador_c += 1
                else:
                    contador_p += 1
            else:
                contador_p += 1
                print("no es el paciente")

    def comparar():
        fix_atl = [0, 1, 2, 6, 9, 11, 15, 17, 18, 27]
        paciente = self.combobox_paciente1.currentIndex()
        cita1 = self.combobox_cita1.currentIndex()
        cita2 = self.combobox_cita2.currentIndex()
        dato = self.combobox_dato.currentIndex()
        tipo = str(all_data[paciente][2])
        if tipo == "Atleta":
            dato = fix_atl[dato]
        dato1 = all_data[paciente][1][cita1][dato]
        dato2 = all_data[paciente][1][cita2][dato]
        self.label_dato1.setText(dato1)
        self.label_dato2.setText(dato2)


    data = []
    # el contador contiene = pacientes adultos, pacientes atletas, pacientes totales, hombres, mujeres
    contadores = [0, 0, 0, 0, 0, 0]
    edad_total = 0
    edad_prom = 0
    # esto lee los pacientes del txt y los saca
    with open(f'pacientes.txt', 'rb') as file_new_d:
        while True:
            try:
                info = pickle.load(file_new_d)
                data.append(info)
            except EOFError:
                break
    row_data = []
    all_data = []
    med = []
    contador = 0
    for position, datos in enumerate(data):
        str(datos.__dict__.get('name'))
        str(datos.__dict__.get('medidas'))
        str(datos.__dict__.get('t_pac'))
        str(datos.__dict__.get('fecha'))
        str(datos.__dict__.get('doc'))

        row_data = [datos.__dict__.get('name'), datos.__dict__.get('medidas'), datos.__dict__.get('t_pac'),
                    datos.__dict__.get('doc'), datos.__dict__.get('fecha'), datos.__dict__.get('hora')]
        all_data.append(row_data)
        contador += 1

    # primero paciente (de momento hay 2, primo jose y segundo joestar)
    # segundo es dato del row_data (0 nombre completo, 1 todas las medidas de entrada, 2 tipo de paciente,
    # 3 documento, 4 fecha de cita)
    # tercero depende del anterior:
    # si es 0 es una letra del nombre completo,
    # si es 1 son todos los datos de una cita,
    # si es 2 son las letras de tipo de paciente
    # el cuarto dato es solo para medidas de citas, te da una medida e particular de la cita seleccionada anteriormente
    # nota: no tienes que usar los 4, solo usa los nesezarios
    # print(all_data[0][1][0][1])
    # por ejemplo arriba llamame a primo josue, dame todas sus medidas, solo las de la cita 1, solo su peso
    # print(all_data[1][2])

    #esto llama a los pacientes y los cuenta el total ademas de contar por tipos de paciente y los asigna en sus label
    for position, datos in enumerate(data):
        if str(datos.__dict__.get('t_pac')) == "Adulto":
            contadores[0] += 1
            contadores[2] += 1
        elif str(datos.__dict__.get('t_pac')) == "Atleta":
            contadores[1] += 1
            contadores[2] += 1
        else:
            print("error")
    self.lbl_patient_adulto_count.setText(contadores[0])
    self.lbl_patient_atleta_count.setText(contadores[1])
    self.lbl_patient_total.setText(contadores[2])

    #esto calcula la edad promedio de los pacientes (no esta listo) y lo asigna en su label

    for position, datos in enumerate(data):
        edad_total += getedad(str(datos.__dict__.get('fnacimiento')), str(datos.__dict__.get('fecha')))
    edad_prom = edad_total / contadores[2]
    self.lbl_edad_promedio.setText(edad_prom)

    #esto calcula cuantos pacientes hombres y mujeres hay en el sistema y los coloca en sus labels
    for position, datos in enumerate(data):
        if str(datos.__dict__.get('sex')) == "Hombre":
            contadores[3] += 1
        elif str(datos.__dict__.get('sex')) == "Mujer":
            contadores[4] += 1
    self.lbl_cant_hombres.setText(contadores[3])
    self.lbl_cant_mujeres.setText(contadores[4])

    #calcula la cantidad total de citas y la escribe en su label

    for position, datos in enumerate(data):
        if str(datos.__dict__.get('t_pac')) == "Adulto":
            contadores[5] += len(datos.get_medidas())
        elif str(datos.__dict__.get('t_pac')) == "Atleta":
            contadores[5] += len(datos.get_medidas())
        else:
            print("error")
    self.lbl_cita_total.setText(contadores[4])

    #esto llena la combobox de paciente con los pacientes

    for position, datos in enumerate(data):
        combobox_paciente1.addItem(str(datos.__dict__.get('name')), str(datos.__dict__.get('doc')),
        str(datos.__dict__.get('t_pac')))

    # al seleccionar un paciente empieza a cargar las citas de este y que datos puede comparar

    combobox_paciente1.currentTextChanged.connect(self.cambio_paciente(contador[2]))

    cambio_paciente(contadores[2])

    self.btn_comparar.clicked.connect(comparar())


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
