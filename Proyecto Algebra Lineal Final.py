from tkinter import *
from tkinter import ttk
from tkinter import font

fuente_personalizada =("monserrat", 12, "italic")
fuente_personalizada2=("open sans", 10, "italic")

class Paciente:
    def __init__(self, sexo="", raza="", creatinina=0.0, albumina=0.0, tfg=0.0, diagnostico=""):
        self.sexo = sexo
        self.raza = raza
        self.creatinina = creatinina
        self.albumina = albumina
        self.tfg = tfg
        self.diagnostico = diagnostico
        self.acr_categoria = None
        self.tfg_categoria = None
        self.pronostico = None
    
class Ventana(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.root.title("Nefromatic")
        self.root.geometry("820x460")
        self.root.resizable(False, False)
        self.frame_actual = None
        self.cargar_inicio()

    def cambiar_frame(self, nuevo_frame):
        if self.frame_actual is not None:
            self.frame_actual.destroy()
        self.frame_actual = nuevo_frame
        self.frame_actual.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        

    def cargar_inicio(self):
        fuente_personalizada =("monserrat", 12, "italic")
        frame_inicio = Frame(self.root, bg="#f5f5f5")
        texto_largo = (
            "Este programa está diseñado para ayudar a personas sin conocimiento "
            "médico o recursos para consultas, a determinar posibles riesgos de insuficiencia renal.\n\n"
            "**Advertencia:** Este programa no reemplaza una consulta médica profesional."
        )
        



        Label(frame_inicio, text="Diagnóstico de Insuficiencia Renal Crónica", font=("Roboto",12), bg="#f5f5f5").pack(pady=10)
        Label(frame_inicio, text=texto_largo, font=("roboto ",12), bg="#f5f5f5", wraplength=600, justify="left").pack(pady=20)

        Button(frame_inicio, text="Iniciar programa", font=("Roboto",12), command=self.cargar_riesgos, bg="#007BFF", fg="white", relief=RAISED, padx=10, pady=5).pack(pady=20)

        self.cambiar_frame(frame_inicio)

    def cargar_riesgos(self):
        frame_riesgos = Frame(self.root, bg="#f5f5f5")
        Label(frame_riesgos, text="Seleccione las opciones de riesgo:", font=(fuente_personalizada), bg="#f5f5f5").pack(pady=10)

        opciones_frame = Frame(frame_riesgos, bg="#f5f5f5")
        opciones_frame.pack()

        self.opciones_riesgos = [IntVar() for _ in range(17)]
        self.opciones_texto = [
            "Padezco diabetes mellitus tipo 2", "Padezco hipertensión arterial", "Padezco glomerulonefritis",
            "Consumo medicamentos nefrotóxicos", "Padezco alguna enfermedad autoinmune",
            "Soy de la tercera edad", "Padezco de alcoholismo", "Consumo tabaco",
            "Padezco alguna enfermedad poliquística del riñón", "Padezco alguna lesión renal",
            "Padezco alguna enfermedad cardiovascular", "Padezco litiasis",
            "Tengo algún familiar con insuficiencia renal", "Padezco de hematuria",
            "Alguna vez me han transplantado un riñón", "Soy de tez negra", "No me identifico con ninguna de las anteriores"
        ]
        
        Label(font=fuente_personalizada2)

        for i, texto in enumerate(self.opciones_texto):
            Checkbutton(opciones_frame, text=texto, font=("Roboto",11),variable=self.opciones_riesgos[i], bg="#f5f5f5", anchor="w", justify="left").grid(row=i // 2, column=i % 2, padx=5, pady=2, sticky=W)

        boton_frame = Frame(frame_riesgos, bg="#f5f5f5")
        boton_frame.pack(pady=10)

        self.boton_sintomas = Button(boton_frame, text="Siguiente",font=("Roboto",12), state=DISABLED, command=self.cargar_sintomas, bg="#28a745", fg="white", padx=10, pady=5)
        self.boton_sintomas.pack(side=LEFT, padx=5)

        Button(boton_frame, text="Volver",font=("Roboto",12), command=self.cargar_inicio, bg="#dc3545", fg="white", padx=10, pady=5).pack(side=LEFT, padx=5)

        self.cambiar_frame(frame_riesgos)
        self.verificar_seleccion_riesgos()

    def verificar_seleccion_riesgos(self):
        def on_change(*args):
            if any(opcion.get() == 1 for opcion in self.opciones_riesgos):
                self.boton_sintomas.config(state=NORMAL)
            else:
                self.boton_sintomas.config(state=DISABLED)

        for opcion in self.opciones_riesgos:
            opcion.trace("w", on_change)

    def cargar_sintomas(self):
        frame_sintomas = Frame(self.root, bg="#f5f5f5")
        Label(frame_sintomas, text="Seleccione los síntomas:", font=("Roboto",12), bg="#f5f5f5").pack(pady=10)

        self.opciones_sintomas = [IntVar() for _ in range(7)]
        self.sintomas_texto = [
            "Hinchazón en los pies, tobillos o piernas", "Disminución del volumen de orina",
            "Sensación de asfixia", "Fatiga", "Desorientación", "Náuseas",
            "No tengo ninguno de los síntomas anteriores"
        ]
        Label(text=self.sintomas_texto, font=("Roboto",12))
        for i, texto in enumerate(self.sintomas_texto):
            Checkbutton(frame_sintomas, text=texto,font=("Roboto",11), variable=self.opciones_sintomas[i],command=self.verificar_seleccion_sintomas, bg="#f5f5f5", anchor="w").pack(anchor=W, padx=20)

        boton_frame = Frame(frame_sintomas, bg="#f5f5f5")
        boton_frame.pack(pady=10)

        self.boton_diagnostico = Button(boton_frame, text="Diagnóstico", font=("Lato", 10, "bold"),state=DISABLED, command=self.abrir_ventana_secundaria, bg="#28a745", fg="white", padx=10, pady=5)
        self.boton_diagnostico.pack(side=LEFT, padx=5)

        Button(boton_frame, text="Volver", command=self.cargar_riesgos, bg="#dc3545", fg="white", padx=10, pady=5).pack(side=LEFT, padx=5)

        self.cambiar_frame(frame_sintomas)

    def verificar_seleccion_sintomas(self):
        if any(opcion.get() == 1 for opcion in self.opciones_sintomas):
            self.boton_diagnostico.config(state=NORMAL)
        else:
            self.boton_diagnostico.config(state=DISABLED)

    def obtener_seleccionadosS(self):
        # Obtener síntomas seleccionados como una lista de texto
        seleccionados = [self.sintomas_texto[i] for i, var in enumerate(self.opciones_sintomas) if var.get() == 1]
        return seleccionados

    def obtener_seleccionadosR(self):
        #Obtener riesgos seleccionados como una lista de texto
        seleccionadosr = [self.opciones_texto[i] for i, var in enumerate(self.opciones_riesgos) if var.get() == 1]
        return seleccionadosr

    def abrir_ventana_secundaria(self):
        seleccionados = self.obtener_seleccionadosS()
        seleccionadosr = self.obtener_seleccionadosR()
        self.root.destroy()  # Cierra la ventana actual (VentanaPrincipal)
        nueva_root = Tk()  # Nueva instancia para la VentanaSecundaria
        VentanaSecundaria(nueva_root, seleccionados, seleccionadosr,)

class VentanaSecundaria(Frame):

    def __init__(self, master, seleccionados, seleccionadosr):
        super().__init__(master, width=820, height=460, bg="#8fcef2")
        self.master = master
        self.pack()
        self.paciente = Paciente()
        self.ventana_titulo()
        self.ventana_principal()
        self.ventana_factores_riesgo(seleccionadosr)
        self.ventana_sintomas(seleccionados)
        self.master.title("Nefromatic")

    def ventana_titulo(self):
        self.ventana_nombre = Frame(self, width=695, height=40, bg="white", highlightthickness=2, highlightcolor="#939393")
        self.ventana_nombre.place(x=60, y=5)

        self.lbl_nombre = Label(self.ventana_nombre, text='"Nefromatic"', font=("Dm sans", 14, "italic"), bg="White")
        self.lbl_nombre.place(x=300, y=5)

    def obtener_datos(self):
        try:
            self.paciente.sexo = self.var_sexo.get()
            self.paciente.raza = self.txt_raza.get()
            self.paciente.creatinina = float(self.txt_creatinina.get())
            self.paciente.albumina = float(self.txt_albumina.get())
            self.calcular_TFG()
            self.calcular_CAC()
            self.generar_clasificacion()
        except ValueError:
            self.resultado_TFG.config(text="Error: Verifique los datos ingresados.")
            self.resultado_ACR.config(text="Error: Verifique los datos ingresados.")

    def calcular_TFG(self):
        edad = int(self.txt_edad.get())
        sexo = self.paciente.sexo
        raza = self.paciente.raza
        creatinina = self.paciente.creatinina

        if sexo == "femenino":
            kappa = 0.7
            alpha = -0.329
            factor_sexo = 1.018
        else:  # masculino
            kappa = 0.9
            alpha = -0.411
            factor_sexo = 1

        # Ajustes para raza
        factor_raza = 1.159 if raza.lower() == "negra" else 1

        # Cálculo de TFG usando CKD-EPI
        valor_min = min(creatinina / kappa, 1)
        valor_max = max(creatinina / kappa, 1)
        # Cambiar la potencia de 0.209 a -1.209
        TFG = 141 * (valor_min ** alpha) * (valor_max ** -1.209) * (0.993 ** edad) * factor_sexo * factor_raza

        self.paciente.tfg = TFG
        self.resultado_TFG.config(text=f"{TFG:.2f} mL/min/1.73m²")

    def calcular_CAC(self):
        albumina = self.paciente.albumina
        creatinina = self.paciente.creatinina
        if creatinina == 0:
            self.resultado_ACR.config(text="Error: Creatinina no puede ser 0.")
            return

        cociente = round((albumina * 100) / creatinina, 2)
        if cociente < 30:
            self.paciente.acr_categoria = "A1"
        elif 30 <= cociente <= 300:
            self.paciente.acr_categoria = "A2"
        else:
            self.paciente.acr_categoria = "A3"

        self.resultado_ACR.config(text=f"{cociente} mg/g ({self.paciente.acr_categoria})")

    def generar_clasificacion(self):
        tfg = self.paciente.tfg
        acr = self.paciente.acr_categoria

        if tfg >= 90:
            self.paciente.tfg_categoria = "G1"
        elif 60 <= tfg < 90:
            self.paciente.tfg_categoria = "G2"
        elif 45 <= tfg < 60:
            self.paciente.tfg_categoria = "G3A"
        elif 30 <= tfg < 45:
            self.paciente.tfg_categoria = "G3B"
        elif 15 <= tfg < 30:
            self.paciente.tfg_categoria = "G4"
        else:
            self.paciente.tfg_categoria = "G5"

        combinacion = f"{self.paciente.tfg_categoria}-{acr}"
        color, descripcion = self.obtener_clasificacion_color(combinacion)

        self.lbl_categoria.config(text=f"Categoría: {combinacion}", bg=color)
        self.lbl_descripcion.config(text=f"Descripción: {descripcion}", bg=color)

    def obtener_clasificacion_color(self, combinacion):
        verde = ["G1-A1", "G2-A1"]
        amarillo = ["G1-A2", "G2-A2", "G3A-A1"]
        naranja = ["G1-A3", "G2-A3", "G3A-A2", "G3B-A1"]
        if combinacion in verde:
            return "#90EE90", "No existen marcadores de enfermedad renal, se recomienda consultar a un médico."
        elif combinacion in amarillo:
            return "#FFD700", "Riesgo moderado, existen marcadores de enfermedad renal."
        elif combinacion in naranja:
            return "#FFA500", "Riesgo alto, existen bastantes marcadores de enfermedad renal."
        else:
            return "#FF4500", "Riesgo muy alto, enfermedad renal."

    def ventana_principal(self):

        
        self.ventana_formulario = Frame(self, width=555, height=400, bg="white", highlightthickness=2, highlightcolor="#939393")
        self.ventana_formulario.place(x=250, y=50)

        self.lbl0 = Label(self.ventana_formulario, text= "Cálculo de la tasa de filtrado glomerular y\nel cociente de albumina/creatinina", font= ("Open Sans", 10, "bold"), bg= "#cbe6f5")
        self.lbl0.place(x= 117, y= 0, width= 320, height= 40)

        self.lbl = Label(self.ventana_formulario, text= "Ingrese los datos correspondientes en cada apartado:",bg="white")
        self.lbl.place(x= 20, y= 45, width= 300, height= 32)

        Label(self.ventana_formulario, text="Edad:", bg="#cbe6f5",font=("Roboto",12)).place(x=20, y=80, width=80, height=25)
        self.txt_edad = Entry(self.ventana_formulario, bg="#e4edff")
        self.txt_edad.place(x=120, y=80, width=150, height=25)

        Label(self.ventana_formulario, text="Sexo:", bg="#cbe6f5",font=("Roboto",12)).place(x=20, y=120, width=80, height=25)
        opciones_sexo = ["Femenino", "Masculino"]
        self.var_sexo = StringVar()
        self.combobox_sexo = ttk.Combobox(self.ventana_formulario, textvariable=self.var_sexo, values=opciones_sexo, state="readonly")
        self.combobox_sexo.place(x=120, y=120, width=150, height=25)
        self.combobox_sexo.set("Seleccione")
        
        Label(self.ventana_formulario, text="Raza:", bg="#cbe6f5",font=("Roboto",12)).place(x=20, y=160, width=80, height=25)
        self.txt_raza = Entry(self.ventana_formulario, bg="#e4edff")
        self.txt_raza.place(x=120, y=160, width=150, height=25)

        Label(self.ventana_formulario, text="Creatinina:", bg="#cbe6f5",font=("Roboto",12)).place(x=20, y=200, width=80, height=25)
        self.txt_creatinina = Entry(self.ventana_formulario, bg="#e4edff")
        self.txt_creatinina.place(x=120, y=200, width=150, height=25)

        Label(self.ventana_formulario, text="Albumina:", bg="#cbe6f5",font=("Roboto",12)).place(x=20, y=240, width=80, height=25)
        self.txt_albumina = Entry(self.ventana_formulario, bg="#e4edff")
        self.txt_albumina.place(x=120, y=240, width=150, height=25)

        self.TFG = Label(self.ventana_formulario, text="TFG:", font=("Roboto",12), bg="white")
        self.TFG.place(x=20, y=320)
        self.resultado_TFG = Label(self.ventana_formulario, text="", font=("Roboto",12), bg="white")
        self.resultado_TFG.place(x=60, y=320)

        self.ACR = Label(self.ventana_formulario, text="CAC:", font=("Roboto",12), bg="white")
        self.ACR.place(x=20, y=350)
        self.resultado_ACR = Label(self.ventana_formulario, text="", font=("Roboto",12), bg="white")
        self.resultado_ACR.place(x=60, y=350)

        Button(self.ventana_formulario, text="Calcular", command=self.obtener_datos, bg="#cbe6f5").place(x=170, y=280, width=100, height=30)

        self.ventana_formulario = Frame(self, width=250, height=500, bg="white")
        self.ventana_formulario.place(x=600, y=100)

        Label(self.ventana_formulario, text="Clasificación", font=("monserrat ", 12, "bold"), bg="white").pack(pady=10)

        self.lbl_categoria = Label(self.ventana_formulario, text="", font=("monserrat ", 10), bg="white")
        self.lbl_categoria.pack(padx=0, pady=10)

        self.lbl_descripcion = Label(self.ventana_formulario, text="", font=("monserrat ", 10), bg="white", wraplength=200)
        self.lbl_descripcion.pack(padx=0, pady=10)

        self.btn_notas = Button(self, text= "!", command=self.mostrar_notas)
        self.btn_notas.place(x= 765, y= 80, width= 25, height= 25)

    def mostrar_notas(self):
        ventana_notas = Toplevel(self)
        ventana_notas.title("Notas")
        ventana_notas.geometry("400x200")
        ventana_notas.config(bg= "#8fcef2")

        texto_notas = Text(ventana_notas, wrap= "word", bg= "#e4edff", font=("monserrat ", 10))
        texto_notas.insert("1.0", "Nota: La creatinina en sangre también puede ser llamada creatinina sérica, creatinina, en suero, o creatinina en plasma.\n\n")
        texto_notas.insert("2.0", "Nota: La creatinina en sangre debe ser ingresada usando miligramos por decilitro de sangre (mg/dL).")
        texto_notas.config(state="disabled")
        texto_notas.pack(expand=True, fill="both")

    def ventana_factores_riesgo(self, seleccionadosr):
        self.ventana_riesgo = Frame(self, width=235, height=235, bg= "white", highlightthickness=2, highlightcolor= "#939393")
        self.ventana_riesgo.place(x= 10, y= 50)

        self.lbl_riesgo = Label(self.ventana_riesgo, text= "Factores de Riesgo", font=("monserrat ", 10, "bold"), bg= "White")
        self.lbl_riesgo.place(x= 20, y= 2)

        # Mostrar los factires de riesgo seleccionados en un Label
        sintomas_texto = "\n".join(seleccionadosr)  # Convertir la lista de factores a una cadena
        self.lbl_factores_riesgo = Label(self.ventana_riesgo, text=f"\n{sintomas_texto}\n", bg="White", font=("monserrat ", 7), anchor="w", justify="left")
        self.lbl_factores_riesgo.place(x= 10, y= 22)

    def ventana_sintomas(self, seleccionados):
        self.ventana_riesgo = Frame(self, width=235, height=160, bg="white", highlightthickness=2, highlightcolor="#939393")
        self.ventana_riesgo.place(x= 10, y= 290)

        self.lbl_riesgo = Label(self.ventana_riesgo, text="Síntomas", font=("monserrat ", 10, "bold"), bg="White")
        self.lbl_riesgo.place(x= 20, y= 2)

        # Mostrar los síntomas seleccionados en un Label
        sintomas_texto = "\n".join(seleccionados)  # Convertir la lista de síntomas a una cadena
        self.lbl_sintomas = Label(self.ventana_riesgo, text=f"\n{sintomas_texto}", bg="White", font=("monserrat ", 7), anchor="w", justify="left")
        self.lbl_sintomas.place(x= 10, y= 22)


# Crear ventana principal
root = Tk()
programa = Ventana(root)

# Bucle de la ventana principal
programa.mainloop()

