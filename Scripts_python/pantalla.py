from tkinter import *
from tkinter import ttk
import tkinter.font as font

# La clase 'Aplicacion' ha crecido. En el ejemplo se incluyen
# nuevos widgets en el método constructor __init__(): Uno de
# ellos es el botón 'Info'  que cuando sea presionado llamará 
# al método 'verinfo' para mostrar información en el otro 
# widget, una caja de texto: un evento ejecuta una acción: 

class Aplicacion():
    def __init__(self):
        
        # En el ejemplo se utiliza el prefijo 'self' para
        # declarar algunas variables asociadas al objeto 
        # ('mi_app')  de la clase 'Aplicacion'. Su uso es 
        # imprescindible para que se pueda acceder a sus
        # valores desde otros métodos:
        
        self.raiz = Tk()
        ancho = 600
        alto = 600
        self.raiz.geometry('%sx%s'%(ancho,alto))
        
        # Impide que los bordes puedan desplazarse para
        # ampliar o reducir el tamaño de la ventana 'self.raiz':
        
        self.raiz.resizable(width=False,height=False)
        self.raiz.title('MARP')
        
        # Define el widget Text 'self.tinfo ' en el que se
        # pueden introducir varias líneas de texto:
        
        self.tinfo = Text(self.raiz, width=40, height=16) #40, 10

        # Tamaño fuente
        self.tinfo['font'] = font.Font(size=20)

        # Sitúa la caja de texto 'self.tinfo' en la parte
        # superior de la ventana 'self.raiz':
        
        self.tinfo.pack(side=TOP)
        
        # Define el widget Button 'self.binfo' que llamará 
        # al metodo 'self.verinfo' cuando sea presionado
        
        self.binfo = ttk.Button(self.raiz, text='Actualizar')
        
        # Coloca el botón 'self.binfo' debajo y a la izquierda
        # del widget anterior
                                
        self.binfo.pack(side=LEFT)
        
        # Define el botón 'self.bsalir'. En este caso
        # cuando sea presionado, el método destruirá o
        # terminará la aplicación-ventana 'self.raíz' con 
        # 'self.raiz.destroy'
        
        self.bsalir = ttk.Button(self.raiz, text='Salir', 
                                 command=self.raiz.destroy)
                                 
        # Coloca el botón 'self.bsalir' a la derecha del 
        # objeto anterior.
                                 
        self.bsalir.pack(side=RIGHT)
        
        # El foco de la aplicación se sitúa en el botón
        # 'self.binfo' resaltando su borde. Si se presiona
        # la barra espaciadora el botón que tiene el foco
        # será pulsado. El foco puede cambiar de un widget
        # a otro con la tecla tabulador [tab]
        
        self.binfo.focus_set()
        #self.raiz.mainloop()
        self.raiz.update_idletasks()
        self.raiz.update()
    
    def verinfo(self,info):
        
        # Borra el contenido que tenga en un momento dado
        # la caja de texto
        
        self.tinfo.delete("1.0", END)
        
        # Obtiene información de la ventana 'self.raiz':
        
        info1 = self.raiz.winfo_class()
        info2 = self.raiz.winfo_geometry()
        info3 = str(self.raiz.winfo_width())
        info4 = str(self.raiz.winfo_height())
        info5 = str(self.raiz.winfo_rootx())
        info6 = str(self.raiz.winfo_rooty())
        info7 = str(self.raiz.winfo_id())
        info8 = self.raiz.winfo_name()
        info9 = self.raiz.winfo_manager()
        
        # Construye una cadena de texto con toda la
        # información obtenida:
        texto_info = "========== VALORES ==========\n"
        texto_info += "Humedad: %s"%(info["humedad"]) + "%\n"
        texto_info += "Temperatura: %s°C"%info["temp"] + "\n"
        texto_info += "========== AVISOS ==========\n"
        if info["0"]:
            texto_info += "Maquina sin pintura." + "\n"
        if info["1"]:
            texto_info += "Nivel de pintura bajo." + "\n"
        if info["2"]:
            texto_info += "Paro de emergencia activo." + "\n"
        if info["3"]:
            texto_info += "Tiempo de ciclo excedido." + "\n"
        if info["4"]:
            texto_info += "Puerta de estación abierta." + "\n"
        if info["5"]:
            texto_info += "Robot en fallo." + "\n"
        if info["6"]:
            texto_info += "Robot desconectado." + "\n"
        if info["7"]:
            texto_info += "Boquilla obstruida." + "\n"
        if info["8"]:
            texto_info += "Pieza no ha alcanzado posición." + "\n"
        if info["9"]:
            texto_info += "Pieza terminada en espera." + "\n"
        if info["10"]:
            texto_info += "Máquina parada, falta de piezas de entrada." + "\n"

        # Inserta la información en la caja de texto:
        self.tinfo.insert("1.0", texto_info)

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()