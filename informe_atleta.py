from fpdf import FPDF
from dateutil.relativedelta import relativedelta
from datetime import datetime

def create_pdf_atleta(filename):
    apellidos = "rodriguez ralei"
    nombres = "gustavo alexander"
    sexo = "hombre"
    tipo_doc = "CI"
    id_doc = "29502268"
    lugar_nac = "Venezuela, Zulia, Maracaibo"
    deporte = "caminar"
    tipo_pa = "atleta"
    fecha_me = "31/8/2023"
    fecha_nac = "10/10/1998"
    estatura = "180"
    peso = "65"

    imc = "20.00"
    por_grasa = "%grasa"
    mlg = "18"
    camb = "camb pls"
    iamb = "32"
    complexion = "10.0"
    ##somatotipo =
    endomorfo = 0
    mesomorfo = 0
    ectomorfo = 0

    pdf = FPDF('P', 'pt', (2067, 2756))
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 64)
    pdf.image("formato_atleta_1.jpg", 0, 0)
    ## 7 espacios en blanco para primera
    top = pdf.y
    offset = pdf.x + 40
    pdf.multi_cell(0, 10, f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{apellidos}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{nombres}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{sexo}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{tipo_doc}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{id_doc}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{lugar_nac}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{deporte}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{tipo_pa}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{fecha_me}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{fecha_nac}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{estatura}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{peso}")

    pdf.y = top
    pdf.x = offset

    pdf.multi_cell(0, 9, f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"                                                            "
                          f"{imc}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"\n"
                          f"                                                            "
                          f"{por_grasa}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"\n\n\n"
                          f"                                                            "
                          f"{mlg}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"                                                            "
                          f"{camb}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"\n"
                          f"                                                            "
                          f"{iamb}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"\n"
                          f"                                                            "
                          f"{complexion}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"\n\n\n\n\n\n             "
                          f"                                                            "
                          f"{endomorfo}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"             "
                          f"                                                            "
                          f"{mesomorfo}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"             "
                          f"                                                            "
                          f"{ectomorfo}")

    ##fraccionamiento cororal =
    masa_piel = 0
    masa_osea = 0
    tegido_adiposo = 0
    masa_muscular = 0
    masa_residual = 0
    masa_total = 0

    indice_cormico = 0
    longitud_relativa = 0
    ##longitud relativa de la extremidad superior
    indice_esqueletico = 0
    envergadura_relativa = 0

    pdf.add_page()
    pdf.set_font("Helvetica", "B", 64)
    pdf.image("formato_atleta_2.jpg", 0, 0)
    pdf.y = top
    pdf.x = offset

    pdf.multi_cell(0, 9, f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"                                   "
                          f"{masa_piel}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"                              "
                          f"{masa_osea}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"                                   "
                          f"{tegido_adiposo}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"                                   "
                          f"{masa_muscular}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"                                 "
                          f"{masa_residual}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"                             "
                          f"{masa_total}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"               "
                          f"{indice_cormico}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"               "
                          f"{longitud_relativa}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"               "
                          f"{indice_esqueletico}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"               "
                          f"{envergadura_relativa}")

    pdf.add_page()
    pdf.set_font("Helvetica", "B", 64)
    pdf.image("formato_atleta_3.jpg", 0, 0)
    pdf.y = top
    pdf.x = offset

    def imc_medic(imc):
        fimc = float(imc)
        if fimc < 18.5:
            print("peso bajo")
            return "peso bajo"
        elif 18.5 < fimc < 24.9:
            print("Peso saludable")
            return "peso saludable"
        elif 18.5 < fimc < 24.9:
            print("Sobre peso")
            return "sobre peso"
        elif 18.5 < fimc < 24.9:
            print("Obesidad, grado 1")
            return "obesidad, grado 1"
        elif 18.5 < fimc < 24.9:
            print("Obesidad, grado 2")
            return "obesidad, grado 2"
        elif 18.5 < fimc < 24.9:
            print("Obesidad, grado 3, obesidad morbida")
            return "obesidad, grado 3, obesidad morbida"
        else:
            print("error final1bonus1")
            return "error imc"

    def mlg_medic(mlg, sexo):
        fmlg = float(mlg)
        if sexo == "hombre":
            mlgh = [18, 20, 22, 25]
            dato2 = min(mlgh, key=lambda x: abs(x - fmlg))
            if dato2 == 18:
                print("Complexión ligera con poca musculatura")
                return "con complexion ligera con poca musculatura"
            if dato2 == 20:
                print("Musculatura promedio")
                return "con musculatura promedio"
            if dato2 == 22:
                print("Marcadamente musculoso ")
                return "marcadamente musculoso"
            if dato2 == 25:
                print("No se logra normalmente sin levantar pesas / Límite superior de la musculatura obtenida sin "
                      "uso de agentes fármaco-lógicos, por lo que el MLG podría llegar a 40")
                return f"en un rango que no se logra normalmente sin \n\n\n       " \
                       f"levantar pesas / límite superior de la \n\n\n       " \
                       f"musculatura obtenida sin uso de agentes \n\n\n       " \
                       f"fármaco-lógicos, por loque el MLG podría  \n\n\n       " \
                       f"llegar a 40"
            else:
                print("error final2bonus1")
                return "error mlg"
        elif sexo == "mujer":
            mlgm = [13, 15, 17, 22]
            dato2 = min(mlgm, key=lambda x: abs(x - fmlg))
            if dato2 == 13:
                print("Complexión ligera con poca musculatura")
                return "con complexion ligera con poca musculatura"
            if dato2 == 15:
                print("Musculatura promedio")
                return "con musculatura promedio"
            if dato2 == 17:
                print("Marcadamente musculoso ")
                return "marcadamente musculosa"
            if dato2 == 22:
                print(
                    "No se logra normalmente sin levantar pesas / Límite superior de la musculatura obtenida sin uso "
                    "de agentes fármaco-lógicos, por lo que el MLG podría llegar a 40")
                return "con medidas que no se logran normalmente \n\n\n      " \
                       "sin levantar pesas / límite superior de \n\n\n      " \
                       "la musculatura obtenida sin uso de \n\n\n      " \
                       "agentes fármaco-lógicos, por lo que el \n\n\n      " \
                       "MLG podría llegar a 40"
            else:
                print("error final2bonus1")

    def iamb_medic(iamb):
        fiamb = float(iamb)
        if fiamb < 5:
            print("Bajo nivel de musculatura o disminución")
            return "un bajo nivel de musculatura o disminucion"
        elif fiamb in range(5, 15):
            print("Masa muscular debajo del promedio")
            return "una masa muscular debajo del promedio"
        elif fiamb in range(16, 85):
            print("Masa muscular promedio")
            return "una masa muscular promedio"
        elif fiamb in range(86, 95):
            print("Masa muscular arriba del promedio o hipertrofia muscular")
            return "una masa muscular arriba del promedio o \n\n\n      " \
                   "hièrtrofia muscular"
        elif fiamb > 95:
            print("Masa muscular alta - hipertrofia muscular")
            return "una masa muscular alta - hipertrofia \n\n\n      " \
                   "muscular"
        else:
            print("error iamb")
            return "error iamb"

    def complexion_medic(complexion, sexo):
        fcomplexion = float(complexion)
        if sexo == "hombre":
            if fcomplexion > 10.4:
                print("complexion pequeña")
                return "complexion pequeña"
            elif 9.6 < fcomplexion < 10.3:
                print("complexion mediana")
                return "complexion mediana"
            elif fcomplexion < 9.5:
                print("complexion grande")
                return "complexion grande"
        elif sexo == "mujer":
            if fcomplexion > 10.9:
                print("complexion pequeña")
                return "complexion pequeña"
            elif 9.9 < fcomplexion < 10.8:
                print("complexion mediana")
                return "complexion mediana"
            elif fcomplexion < 9.8:
                print("complexion grande")
                return "complexion grande"

    def indice_cormico_medic(sexo, indice_cormico):
        if sexo == "hombre":
            if indice_cormico <= 51:
                return "Braquicórmico (Tronco corto)"
            elif 51.1 < indice_cormico < 53:
                return "Metricórmico (Tronco medio)"
            elif indice_cormico >= 53.1:
                return "Macrocórmico (Tronco largo)"
        elif sexo == "mujer":
            if indice_cormico <= 52:
                return "Braquicórmico (Tronco corto)"
            elif 52.1 < indice_cormico < 54:
                return "Metricórmico (Tronco medio)"
            elif indice_cormico >= 54.1:
                return "Macrocórmico (Tronco largo)"

    def longitud_relativa_medic(lonitud_relativa):
        if longitud_relativa <= 44.9:
            return "Braquibraquial (extremidad superior corta)"
        elif 45 < indice_cormico < 46.9:
            return "Mesobraquial (extremidad superior intermedia)"
        elif indice_cormico >= 47:
            return "Macrobraquial (extremidad superior larga)"

    def indice_esqueletico_medic(indice_esqueletico):
        if indice_esqueletico <= 84.9:
            return "Braquiesquélico (extremidad inferior corta)"
        elif 85 < indice_esqueletico < 89.9:
            return "Mesoesquélico (extremidad inferior mediana)"
        elif indice_esqueletico >= 90:
            return "Macroesquélico (extremidad inferior larga)"

    imc_info = imc_medic(imc)
    mlg_info = mlg_medic(mlg, sexo)
    iamb_info = iamb_medic(iamb)
    complexion_info = complexion_medic(complexion, sexo)
    cormico_info = indice_cormico_medic(sexo, indice_cormico)
    long_info = longitud_relativa_medic(longitud_relativa)
    icor_info = indice_esqueletico_medic(indice_esqueletico)

    valorx = 3
    valory = -2

    pdf.multi_cell(0, 10, f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"Con un índice de masa corporal de "
                          f"{imc} usted califica que \n\n\n\n\n\n\n\n       posee {imc_info}"
                          f"\n\n\n\n\n\n\n\n\n\n\n       "
                          f"Con un índice de masa libre de grasa de {mlg} usted esta \n\n\n\n\n\n\n\n       "
                          f"{mlg_info}\n\n\n\n\n\n\n\n\n\n\n       "
                          f"Con un índice del área muscular del brazo de {iamb} \n\n\n\n\n\n\n\n       "
                          f"en percentiles se puede afirmar que usted posee \n\n\n\n\n\n\n\n       "
                          f"{iamb_info}\n\n\n\n\n\n\n\n\n\n\n       "
                          f"Con un índice de complexión de {complexion} usted posee una \n\n\n\n\n\n\n\n       "
                          f"{complexion_info}\n\n\n\n\n\n\n\n\n\n\n       "
                          f"Con un índice cormico de {indice_cormico} usted posee una \n\n\n\n\n\n\n\n       "
                          f"{cormico_info}\n\n\n\n\n\n\n\n\n\n\n       "
                          f"Con una longitud relativa de {longitud_relativa} usted posee una \n\n\n\n\n\n\n       "
                          f"{long_info}\n\n\n\n\n\n\n\n\n\n\n       "
                          f"Con un índice esquelético de {indice_esqueletico} usted posee una \n\n\n\n\n\n\n\n       "
                          f"{icor_info}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"                                                            "
                          f"Valor en X: {valorx}\n\n\n\n\n\n\n\n\n\n\n"
                          f"                                                            "
                          f"Valor en Y: {valory}")


    ix = 400
    iy = 2000

    pdf.image("basura/big_good.png", ix, iy)

    ##el 3 y el -2 son valores que coloque de ejemplo y deben remplazarse por los valores que da logica de atleta para
    ##saber el posicionamiento en la grafica del somatotipo

    x = valorx * 25
    y = (valory * 25) * -1
    imgx = x + (ix + 300 - 12.5)
    imgy = y + (iy + 300 - 12.5)

    pdf.image("basura/dot.png", ix + 300, iy + 300)
    pdf.image("basura/dot.png", imgx, imgy)

    dia = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S_")
    docname = dia + "reporte.pdf"

    pdf.output(docname, "F")

if __name__ == "__main__":
    create_pdf_atleta("new.pdf")

def create_pdf_atleta(self, data, medidas):

    apellidos = data[1]
    nombres = data[2]
    sexo = data[3]
    tipo_doc = data[4]
    id_doc = data[5]
    lugar_nac = data[6]
    deporte = data[7]
    tipo_pa = data[8]
    fecha_me = data[10]
    fecha_nac = data[9]

    estatura = float(medidas[0][0])
    peso = float(medidas[0][1])
    triceps = float(medidas[0][6])
    subescapular = float(medidas[0][7])
    cresta_ili = float(medidas[0][9])
    supraespinal = float(medidas[0][10])
    abdominal = float(medidas[0][11])
    muslo_frontal = float(medidas[0][12])
    pantorrilla = float(medidas[0][13])
    per_cefalico = float(medidas[0][14])
    per_brazo_rela = float(medidas[0][16])
    per_muneca = float(medidas[0][20])
    estatura_sentado = float(medidas[0][2])
    longitud_acromio_dedal = float(medidas[0][5])
    envergadura = float(medidas[0][3])
    per_torax = float(medidas[0][21])
    per_muslo_medio = float(medidas[0][27])
    per_maximo_antebr_der = float(medidas[0][18])
    per_pantorrilla = float(medidas[0][28])
    diam_biacromial = float(medidas[0][38])
    diam_biiliocristal = float(medidas[0][39])
    per_min_cintura = float(medidas[0][22])
    anchura_torax_transverso = float(medidas[0][41])
    prof_torax_ante_poste = float(medidas[0][42])
    diam_biepicondilar_humero = float(medidas[0][43])
    diam_biepicondilar_femur = float(medidas[0][44])

    imc = self.logica_imc_atl(estatura, peso)
    por_grasa = self.logica_porcentaje_grasa_atl(sexo, triceps, subescapular, cresta_ili,
                                                     abdominal, muslo_frontal,
                                                     pantorrilla)
    mlg = self.logica_mlg_atl(peso, por_grasa, estatura)
    result_camb_iamb = self.logica_camb__iamb_atl(sexo, per_brazo_rela, triceps)
    camb = result_camb_iamb[0]
    iamb = result_camb_iamb[1]
    complexion = self.complexion_atl(estatura, per_muneca)
    somatotipo = self.somatotipo_atl(estatura, triceps, subescapular, supraespinal, diam_biepicondilar_humero,
                                        diam_biepicondilar_femur, per_brazo_rela, per_pantorrilla, pantorrilla, peso)
    endomorfo = somatotipo[0]
    mesomorfo = somatotipo[1]
    ectomorfo = somatotipo[2]

    pdf = FPDF('P', 'pt', (2067, 2756))
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 64)
    pdf.image("images/formato_atleta_1.jpg", 0, 0)
    top = pdf.y
    offset = pdf.x + 40
    pdf.multi_cell(0, 10, f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{apellidos}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{nombres}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{sexo}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{tipo_doc}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{id_doc}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{lugar_nac}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{deporte}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{tipo_pa}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{fecha_me}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{fecha_nac}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{estatura}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{peso}")

    pdf.y = top
    pdf.x = offset

    pdf.multi_cell(0, 9, f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                         f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                         f"                                                            "
                         f"{imc}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                         f"\n"
                         f"                                                            "
                         f"{por_grasa}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                         f"\n\n\n"
                         f"                                                            "
                         f"{mlg}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                         f"                                                            "
                         f"{camb}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                         f"\n"
                         f"                                                            "
                         f"{iamb}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                         f"\n"
                         f"                                                            "
                         f"{complexion}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                         f"\n\n\n\n\n\n             "
                         f"                                                            "
                         f"{endomorfo}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                         f"             "
                         f"                                                            "
                         f"{mesomorfo}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                         f"             "
                         f"                                                            "
                         f"{ectomorfo}")

    fracc_corporal = self.fraccionamiento_corporal_atl(sexo, peso, estatura, per_cefalico,
                                                       diam_biacromial, diam_biiliocristal,
                                                       diam_biepicondilar_humero,
                                                       diam_biepicondilar_femur, triceps, subescapular,
                                                       supraespinal,
                                                       abdominal, muslo_frontal, pantorrilla, per_brazo_rela,
                                                       per_maximo_antebr_der,
                                                       per_muslo_medio, per_pantorrilla, per_torax,
                                                       prof_torax_ante_poste,
                                                       anchura_torax_transverso, per_min_cintura, estatura_sentado)
    masa_piel = fracc_corporal[0]
    masa_osea = fracc_corporal[1]
    tegido_adiposo = fracc_corporal[2]
    masa_muscular = fracc_corporal[3]
    masa_residual = fracc_corporal[4]
    masa_total = fracc_corporal[5]

    indice_cormico = self.indice_cormico_atl(estatura, estatura_sentado)
    longitud_relativa = self.longitud_relativa_extremidad_superior_atl(longitud_acromio_dedal,
                                                                                        estatura)
    ##longitud relativa de la extremidad superior
    indice_esqueletico = self.indice_esqueletico_atl(estatura, estatura_sentado)
    envergadura_relativa = self.envergadura_relativa_atl(envergadura, estatura)

    pdf.add_page()
    pdf.set_font("Helvetica", "B", 64)
    pdf.image("images/formato_atleta_2.jpg", 0, 0)
    pdf.y = top
    pdf.x = offset

    pdf.multi_cell(0, 9, f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                         f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                         f"                                   "
                         f"{masa_piel}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                         f"                              "
                         f"{masa_osea}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                         f"                                   "
                         f"{tegido_adiposo}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                         f"                                   "
                         f"{masa_muscular}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                         f"                                 "
                         f"{masa_residual}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                         f"                             "
                         f"{masa_total}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                         f"               "
                         f"{indice_cormico}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                         f"               "
                         f"{longitud_relativa}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                         f"               "
                         f"{indice_esqueletico}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                         f"               "
                         f"{envergadura_relativa}")

    pdf.add_page()
    pdf.set_font("Helvetica", "B", 64)
    pdf.image("images/formato_atleta_3.jpg", 0, 0)
    pdf.y = top
    pdf.x = offset

    def imc_medic(imc):
        fimc = float(imc)
        if fimc < 18.5:
            print("peso bajo")
            return "peso bajo"
        elif 18.5 < fimc < 24.9:
            print("Peso saludable")
            return "peso saludable"
        elif 18.5 < fimc < 24.9:
            print("Sobre peso")
            return "sobre peso"
        elif 18.5 < fimc < 24.9:
            print("Obesidad, grado 1")
            return "obesidad, grado 1"
        elif 18.5 < fimc < 24.9:
            print("Obesidad, grado 2")
            return "obesidad, grado 2"
        elif 18.5 < fimc < 24.9:
            print("Obesidad, grado 3, obesidad morbida")
            return "obesidad, grado 3, obesidad morbida"
        else:
            print("error final1bonus1")
            return "error imc"

    def mlg_medic(mlg, sexo):
        fmlg = float(mlg)
        if sexo == "Masculino":
            mlgh = [18, 20, 22, 25]
            dato2 = min(mlgh, key=lambda x: abs(x - fmlg))
            if dato2 == 18:
                print("Complexión ligera con poca musculatura")
                return "con complexion ligera con poca musculatura"
            if dato2 == 20:
                print("Musculatura promedio")
                return "con musculatura promedio"
            if dato2 == 22:
                print("Marcadamente musculoso ")
                return "marcadamente musculoso"
            if dato2 == 25:
                print("No se logra normalmente sin levantar pesas / Límite superior de la musculatura obtenida sin "
                      "uso de agentes fármaco-lógicos, por lo que el MLG podría llegar a 40")
                return f"en un rango que no se logra normalmente sin \n\n\n       " \
                       f"levantar pesas / límite superior de la \n\n\n       " \
                       f"musculatura obtenida sin uso de agentes \n\n\n       " \
                       f"fármaco-lógicos, por loque el MLG podría  \n\n\n       " \
                       f"llegar a 40"
            else:
                print("error final2bonus1")
                return "error mlg"
        elif sexo == "Femenino":
            mlgm = [13, 15, 17, 22]
            dato2 = min(mlgm, key=lambda x: abs(x - fmlg))
            if dato2 == 13:
                print("Complexión ligera con poca musculatura")
                return "con complexion ligera con poca musculatura"
            if dato2 == 15:
                print("Musculatura promedio")
                return "con musculatura promedio"
            if dato2 == 17:
                print("Marcadamente musculoso ")
                return "marcadamente musculosa"
            if dato2 == 22:
                print(
                    "No se logra normalmente sin levantar pesas / Límite superior de la musculatura obtenida sin uso "
                    "de agentes fármaco-lógicos, por lo que el MLG podría llegar a 40")
                return "con medidas que no se logran normalmente \n\n\n      " \
                       "sin levantar pesas / límite superior de \n\n\n      " \
                       "la musculatura obtenida sin uso de \n\n\n      " \
                       "agentes fármaco-lógicos, por lo que el \n\n\n      " \
                       "MLG podría llegar a 40"
            else:
                print("error final2bonus1")

    def iamb_medic(iamb):
        fiamb = float(iamb)
        if fiamb < 5:
            print("Bajo nivel de musculatura o disminución")
            return "un bajo nivel de musculatura o disminucion"
        elif fiamb in range(5, 15):
            print("Masa muscular debajo del promedio")
            return "una masa muscular debajo del promedio"
        elif fiamb in range(16, 85):
            print("Masa muscular promedio")
            return "una masa muscular promedio"
        elif fiamb in range(86, 95):
            print("Masa muscular arriba del promedio o hipertrofia muscular")
            return "una masa muscular arriba del promedio o \n\n\n      " \
                   "hièrtrofia muscular"
        elif fiamb > 95:
            print("Masa muscular alta - hipertrofia muscular")
            return "una masa muscular alta - hipertrofia \n\n\n      " \
                   "muscular"
        else:
            print("error iamb")
            return "error iamb"

    def complexion_medic(complexion, sexo):
        fcomplexion = float(complexion)
        if sexo == "Masculino":
            if fcomplexion > 10.4:
                print("complexion pequeña")
                return "complexion pequeña"
            elif 9.6 < fcomplexion < 10.3:
                print("complexion mediana")
                return "complexion mediana"
            elif fcomplexion < 9.5:
                print("complexion grande")
                return "complexion grande"
        elif sexo == "Femenino":
            if fcomplexion > 10.9:
                print("complexion pequeña")
                return "complexion pequeña"
            elif 9.9 < fcomplexion < 10.8:
                print("complexion mediana")
                return "complexion mediana"
            elif fcomplexion < 9.8:
                print("complexion grande")
                return "complexion grande"

    def indice_cormico_medic(sexo, indice_c):
        if sexo == "Masculino":
            if indice_c <= 51:
                return "Braquicórmico (Tronco corto)"
            elif 51.1 < indice_c < 53:
                return "Metricórmico (Tronco medio)"
            elif indice_c >= 53.1:
                return "Macrocórmico (Tronco largo)"
        elif sexo == "Femenino":
            if indice_c <= 52:
                return "Braquicórmico (Tronco corto)"
            elif 52.1 < indice_c < 54:
                return "Metricórmico (Tronco medio)"
            elif indice_c >= 54.1:
                return "Macrocórmico (Tronco largo)"

    def longitud_relativa_medic(longitud_relativa):
        if longitud_relativa <= 44.9:
            return "Braquibraquial (extremidad superior corta)"
        elif 45 < indice_cormico < 46.9:
            return "Mesobraquial (extremidad superior intermedia)"
        elif indice_cormico >= 47:
            return "Macrobraquial (extremidad superior larga)"

    def indice_esqueletico_medic(indice_esqueletico):
        if indice_esqueletico <= 84.9:
            return "Braquiesquélico (extremidad inferior corta)"
        elif 85 < indice_esqueletico < 89.9:
            return "Mesoesquélico (extremidad inferior mediana)"
        elif indice_esqueletico >= 90:
            return "Macroesquélico (extremidad inferior larga)"

    imc_info = imc_medic(imc)
    mlg_info = mlg_medic(mlg, sexo)
    iamb_info = iamb_medic(iamb)
    complexion_info = complexion_medic(complexion, sexo)
    cormico_info = indice_cormico_medic(sexo, indice_cormico)
    long_info = longitud_relativa_medic(longitud_relativa)
    icor_info = indice_esqueletico_medic(indice_esqueletico)

    valorx = 3
    valory = -2

    pdf.multi_cell(0, 10, f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"Con un índice de masa corporal de "
                          f"{imc} usted califica que \n\n\n\n\n\n\n\n       posee {imc_info}"
                          f"\n\n\n\n\n\n\n\n\n\n\n       "
                          f"Con un índice de masa libre de grasa de {mlg} usted esta \n\n\n\n\n\n\n\n       "
                          f"{mlg_info}\n\n\n\n\n\n\n\n\n\n\n       "
                          f"Con un índice del área muscular del brazo de {iamb} \n\n\n\n\n\n\n\n       "
                          f"en percentiles se puede afirmar que usted posee \n\n\n\n\n\n\n\n       "
                          f"{iamb_info}\n\n\n\n\n\n\n\n\n\n\n       "
                          f"Con un índice de complexión de {complexion} usted posee una \n\n\n\n\n\n\n\n       "
                          f"{complexion_info}\n\n\n\n\n\n\n\n\n\n\n       "
                          f"Con un índice cormico de {indice_cormico} usted posee una \n\n\n\n\n\n\n\n       "
                          f"{cormico_info}\n\n\n\n\n\n\n\n\n\n\n       "
                          f"Con una longitud relativa de {longitud_relativa} usted posee una \n\n\n\n\n\n\n       "
                          f"{long_info}\n\n\n\n\n\n\n\n\n\n\n       "
                          f"Con un índice esquelético de {indice_esqueletico} usted posee una \n\n\n\n\n\n\n\n       "
                          f"{icor_info}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"                                                            "
                          f"Valor en X: {valorx}\n\n\n\n\n\n\n\n\n\n\n"
                          f"                                                            "
                          f"Valor en Y: {valory}")

    ix = 400
    iy = 2000

    #pdf.image("basura/big_good.png", ix, iy)

    ##el 3 y el -2 son valores que coloqu de ejemplo y deben remplazarse por los valores que da logica de atleta para
    ##saber el posicionamiento en la grafica del somatotipo

    x = valorx * 25
    y = (valory * 25) * -1
    imgx = x + (ix + 300 - 12.5)
    imgy = y + (iy + 300 - 12.5)

    #pdf.image("basura/dot.png", ix + 300, iy + 300)
    #pdf.image("basura/dot.png", imgx, imgy)

    msg = QMessageBox()
    QMessageBox.information(msg, "Informe",
                            "El informe fue realizado con exito.")
    
    dia = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S_")
    docname = dia + "reporte.pdf"

    pdf.output(docname, "F")