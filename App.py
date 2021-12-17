from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
from DetectarEmociones import detectionEmotion
import cv2
import imutils
from Gui import *

## Reconoce la entrada del video
# def video_de_entrada():
#     global cap
#     ## Seleccion un video local
#     if selected.get() == 1:
#         ## IDentificamos el tipo de archivo
#         path_video = filedialog.askopenfilename(filetypes = [
#             ("all video format", ".mp4"),
#             ("all video format", ".avi")])
#         if len(path_video) > 0:
#             btnEnd.configure(state="active")
#             rad1.configure(state="disabled")
#             rad2.configure(state="disabled")

#             pathInputVideo = "..." + path_video[-20:]
#             lblInfoVideoPath.configure(text=pathInputVideo)
#             cap = cv2.VideoCapture(path_video)
#             visualizar()
#     ## Activa la camara web
#     if selected.get() == 2:
#         btnEnd.configure(state="active")
#         rad1.configure(state="disabled")
#         rad2.configure(state="disabled")
#         lblInfoVideoPath.configure(text="")
#         ## Abrimos la camara
#         try:
#             cap = cv2.VideoCapture(0)
#         except:
#             cap = cv2.VideoCapture(1)
#         visualizar()
        
# def visualizar():
#     global cap
#     ret, frame = cap.read()
#     if ret == True:
#         frame = imutils.resize(frame, width=600)
#         frame = detectionEmotion(frame)
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         im = Image.fromarray(frame)
#         img = ImageTk.PhotoImage(image=im)

#         lblVideo.configure(image=img)
#         lblVideo.image = img
#         lblVideo.after(10, visualizar)
#     else:
#         lblVideo.image = ""
#         lblInfoVideoPath.configure(text="")
#         rad1.configure(state="active")
#         rad2.configure(state="active")
#         selected.set(0)
#         btnEnd.configure(state="disabled")
#         cap.release()
        

# def finalizar_limpiar():
#     lblVideo.image = ""
#     lblInfoVideoPath.configure(text="")
#     rad1.configure(state="active")
#     rad2.configure(state="active")
#     selected.set(0)
#     cap.release()
    
def addFaces():
    global root
    # root.withdraw()
    print("addFaces")
    pass

def useDetector():
    global root
    root.destroy()
    mainGui()
    pass
    
def finalizar():
    print("finalizar")
    pass

root = None
def mainApp():
    global root
    root = Tk() ## Crear la ventana
    root.title("Bienvenido") ## Titulo de la ventana
    lblInfo1 = Label(root, text="¿Cómo quiere usar?", font="bold") ## Agregar una etiqueta
    lblInfo1.grid(column=0, row=0, columnspan=2) ## Ubicar la etiqueta

    btnAddFaces = Button(root, text="Agregar fotos conm tus emociones",  command=addFaces) ## Crear un Radiobutton
    btnUseDetector = Button(root, text="Usar el detector de emociones", command=useDetector) ## Crear un Radiobutton
    btnAddFaces.grid(column=0, row=1)  ## Ubicar el Radiobutton
    btnUseDetector.grid(column=1, row=1) ## Ubicar el Radiobutton


    btnEnd = Button(root, text="Salir",  command=finalizar)
    btnEnd.grid(column=0, row=4, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    mainApp()
