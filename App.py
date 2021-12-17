from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
from DetectarEmociones import detectionEmotion
import cv2
import imutils
import InterfaceEmociones
import AddData
    
def addFaces():
    global root
    root.destroy()
    AddData.mainAddData()
    print("addFaces")
    pass

def useDetector():
    global root
    root.destroy()
    InterfaceEmociones.mainGui()
    pass
    
def finalizar():
    global root
    print("finalizar")
    root.destroy()
    quit()

root = None
def mainApp():
    global root
    root = Tk() ## Crear la ventana
    root.title("Bienvenido") ## Titulo de la ventana
    lblInfo1 = Label(root, text="¿Cómo quiere usar?", font="bold") ## Agregar una etiqueta
    lblInfo1.grid(column=0, row=0, columnspan=2) ## Ubicar la etiqueta

    btnAddFaces = Button(root, text="Agregar fotos con tus emociones",  command=addFaces) ## Crear un Radiobutton
    btnUseDetector = Button(root, text="Usar el detector de emociones", command=useDetector) ## Crear un Radiobutton
    btnAddFaces.grid(column=0, row=1)  ## Ubicar el Radiobutton
    btnUseDetector.grid(column=1, row=1) ## Ubicar el Radiobutton


    btnEnd = Button(root, text="Salir",  command=finalizar)
    btnEnd.grid(column=0, row=4, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    mainApp()
