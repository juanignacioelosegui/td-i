import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from typing import List

from fruta import Fruta
from carrito import Carrito
from catalogo import Catalogo
from datetime import date

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class AppFruteria(tk.Frame):
    ''' Esta clase es una interfaz gráfica de usuario (GUI) para usar las 
        clases de nuestra frutería online desarrolladas en clase. '''
        
    def __init__(self, filename:str):
        ''' Construye la ventana de la app, con los elementos del formulario
            para agregar/sacar frutas y consultar el precio.
            Precondición: master es un objeto tkinter.Tk(); filename tiene
            un archivo CSV de frutas con el que se construirá el catálogo. '''
        master = tk.Tk()

        # Inicializamos el frame.
        tk.Frame.__init__(self, master)

        # Guardamos la ventana master y el dataset como atributos.
        self.master = master

        # Creamos un carrito nuevo para el usuario actual.
        self.carrito:Carrito = Carrito()

        # Cargamos el catálogo de frutas del archivo CSV indicado.
        self.catalogo:Catalogo = Catalogo(filename)
        
        # Nos quedamos solamente con las frutas que están disponibles ahora.
        self.frutas_disponibles:List[Fruta] = self.catalogo.frutas_de_estacion(estacion_actual())

        # Le ponemos un titulo a la ventana y elegimos su tamaño.
        self.master.title('Frutería Online - Introducción a la Programación - UTDT') 
        self.master.geometry('600x400')

        # Creamos un marco donde vamos a mostrar el formulario.
        self.marco = tk.Frame(self.master)
        self.marco.pack()

        # Combo para elegir la fruta:
        label_frutas:str = "Frutas disponibles en "+ estacion_actual()+":"
        tk.Label(self.marco, text=label_frutas).grid(row=0, sticky='E')
        self.fruta = tk.StringVar()
        combo_frutas = ttk.Combobox(self.marco, width=27, state="readonly",
                                    textvariable=str(self.fruta))
        combo_frutas['values'] = self.frutas_disponibles
        combo_frutas.grid(row=0, column=1, sticky='W')
        
        # Valores por defecto para mostrar en el form del peso.
        valor_kg = tk.StringVar(self.master, value='1')

        # Input de peso.
        tk.Label(self.marco, text="Peso (en kg):").grid(row=1, sticky='E')
        self.entry_kg = tk.Entry(self.marco, textvariable=valor_kg, width=3)
        self.entry_kg.grid(row=1, column=1, sticky='W')

        # Botón de agregar fruta.
        boton_agregar = tk.Button(self.marco, text="Agregar", bg='lightgreen',
                                  command=self.ejecutar_agregar_fruta)
        boton_agregar.grid(row=2, column=1, sticky="W")

        # Botón de sacar fruta. 
        boton_sacar = tk.Button(self.marco, text="Sacar", bg='orange',
                                command=self.ejecutar_sacar_fruta)
        boton_sacar.grid(row=2, column=1)

        # Botón de calcular precio. 
        boton_sacar = tk.Button(self.marco, text="Precio", bg='white',
                                command=self.ejecutar_calcular_precio)
        boton_sacar.grid(row=2, column=1, sticky="E")
         
        # Cuadro de texto donde se muestra el contenido del carrito.
        tk.Label(self.marco, text="Carrito de compras:").grid(row=3, sticky='W')
        self.output_carrito = tk.Text(self.marco, width=60, height=17)
        self.output_carrito.grid(row=4, columnspan=2)
        self.output_carrito.config(state=tk.DISABLED)

        # Agregamos una barra de scroll al texto.
        scrollb = ttk.Scrollbar(self.marco, command=self.output_carrito.yview)
        scrollb.grid(row=4, column=3, sticky='nsew')
        self.output_carrito['yscrollcommand'] = scrollb.set

        self.mostrar_carrito()
        self.marco.mainloop()

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def mostrar_carrito(self):
        frutas_c:List[Fruta] = list(self.carrito.frutas_en_carrito())
        frutas_c.sort()
        if len(frutas_c) == 0:
            texto:str = 'El carrito de compras está vacío.'
        else:
            texto:str = ''
            for f in frutas_c:
                kg:int = self.carrito.kilos_de_fruta(f)
                texto += f.nombre + ' --> '+ str(kg) +' kilogramos\n'
        
        self.output_carrito.config(state=tk.NORMAL)
        self.output_carrito.delete('1.0', 'end')
        self.output_carrito.insert('1.0', texto)
        self.output_carrito.config(state=tk.DISABLED)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def ejecutar_agregar_fruta(self):
        ''' Este método se invoca cuando se le dio click al botón Agregar.
            Precondición: self.fruta tiene una fruta válida seleccionada 
            en el combo; self.entry_kg tiene un entero positivo. '''
        todo_ok:bool = True

        # Leemos los dos argumentos del formulario.
        try:
            kg:int = int(self.entry_kg.get())
        except:
            messagebox.showinfo(title='Error', message='Por favor, ingrese un peso válido.')
            todo_ok = False
            
        # Revisamos que el peso sea positivo.
        if kg<=0:
            messagebox.showinfo(title='Error', message='Por favor, ingrese un peso válido.')
            todo_ok = False

        # Busco la fruta que fue seleccionada en el combo.
        i:int = 0
        while i < len(self.frutas_disponibles) \
              and self.fruta.get()!=str(self.frutas_disponibles[i]):
            i = i + 1
        if i == len(self.frutas_disponibles):
            # Algo anduvo mal: no encontramos la fruta seleccionada.
            todo_ok = False
        else:
            fru:Fruta = self.frutas_disponibles[i]

        if todo_ok:
            # Agregamos la fruta al carrito
            self.carrito.agregar(fru, kg)
            self.mostrar_carrito()
            messagebox.showinfo(title='Fruta agregada', 
                message='Se agregó '+ fru.nombre +' al carrito.')

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def ejecutar_sacar_fruta(self):
        ''' Este método se invoca cuando se le dio click al botón Sacar.
            Precondición: self.fruta tiene una fruta válida seleccionada
            en el combo; self.entry_kg tiene un entero positivo. 
            Si en el carrito no hay esa cantidad de la fruta, se muetra
            un mensaje de error y no se prosigue. '''
        todo_ok:bool = True

        # Leemos los dos argumentos del formulario.
        try:
            kg:int = int(self.entry_kg.get())
        except:
            messagebox.showinfo(title='Error', 
                    message='Por favor, ingrese un peso válido.')
            todo_ok = False
            
        # Revisamos que el peso sea positivo.
        if kg<=0:
            messagebox.showinfo(title='Error', 
                    message='Por favor, ingrese un peso válido.')
            todo_ok = False

        # Busco la fruta que fue seleccionada en el combo.
        i:int = 0
        while i < len(self.frutas_disponibles) \
              and self.fruta.get()!=str(self.frutas_disponibles[i]):
            i = i + 1
        if i == len(self.frutas_disponibles):
            # Algo anduvo mal: no encontramos la fruta seleccionada.
            todo_ok = False
        else:
            fru:Fruta = self.frutas_disponibles[i]

        if self.carrito.kilos_de_fruta(fru) < kg:
            messagebox.showinfo(title='Error', 
                    message='No hay tantos kg de esa fruta en el carrito.')
            todo_ok = False

        if todo_ok:
            # Sacamos la fruta del carrito
            self.carrito.sacar(fru, kg)
            self.mostrar_carrito()
            messagebox.showinfo(title='Fruta sacada', 
                message='Se sacó '+ fru.nombre +' del carrito.')
    
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def ejecutar_calcular_precio(self):
        ''' Este método se invoca cuando se le dio click al botón Precio.
            Abre una ventana mostrando un mensaje con el precio actual
            del carrito de compras.  Precondición: Ninguna. '''
        precio:float = self.carrito.calcular_precio_total()
        messagebox.showinfo(title='Precio', 
                message="Precio actual del carrito: $ %.2f" % precio)
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def estacion_actual() -> str:
    ''' Devuelve la estación de la fecha de hoy. El valor de retorno 
        es uno de 'primavera', 'verano', 'otoño' o 'invierno'.  '''
    today:date = date.today()
    empieza_otoño:date     = date(today.year, 3, 21)  # 21 de marzo
    empieza_invierno:date  = date(today.year, 6, 21)  # 21 de junio
    empieza_primavera:date = date(today.year, 9, 21)  # 21 de junio
    empieza_verano:date    = date(today.year, 12, 21) # 21 de diciembre
    vr:str
    if today >= empieza_verano:
        vr = 'verano'
    elif today >= empieza_primavera:
        vr = 'primavera'
    elif today >= empieza_invierno:
        vr = 'invierno'
    elif today >= empieza_otoño:
        vr = 'otoño'
    else:
        vr = 'verano'
    return vr

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

app:AppFruteria = AppFruteria('frutas.csv')
