from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
from DetectarEmociones import detectionEmotion
import cv2
import imutils
import App
from SaveFaceFromVideo import safeFaceForVideo

## Reconoce la entrada del video
def video_de_entrada():
    global webCam
    global cap
    global lblVideo
    global lblInfoVideoPath
    global rad1, rad2
    global selected
    global btnEnd
    ## Seleccion un video local
    if selected.get() == 1:
        ## IDentificamos el tipo de archivo
        path_video = filedialog.askopenfilename(filetypes = [
            ("all video format", ".mp4"),
            ("all video format", ".avi")])
        if len(path_video) > 0:
            btnEnd.configure(state="active")
            rad1.configure(state="disabled")
            rad2.configure(state="disabled")

            pathInputVideo = "..." + path_video[-20:]
            lblInfoVideoPath.configure(text=pathInputVideo)
            cap = cv2.VideoCapture(path_video)
            webCam = False
            visualizar()
    ## Activa la camara web
    if selected.get() == 2:
        btnEnd.configure(state="active")
        rad1.configure(state="disabled")
        rad2.configure(state="disabled")
        lblInfoVideoPath.configure(text="")
        ## Abrimos la camara
        try:
            cap = cv2.VideoCapture(1)
        except:
            cap = cv2.VideoCapture(0)
        webCam = True
        visualizar()
        
def visualizar():
    global webCam
    global cap
    global lblVideo
    global lblInfoVideoPath
    global rad1, rad2
    global selected
    global btnEnd
    ## Emotion
    emotion = "Angry"
    
    ret, frame = cap.read()
    if ret == True:
        frame = imutils.resize(frame, width=600)
        frame = safeFaceForVideo(frame, emotion=emotion)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(frame)
        if (not(webCam)):
            ancho, alto = im.size
            withRedi = 500*ancho//alto
            im = im.resize((withRedi,500), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image=im)

        lblVideo.configure(image=img)
        lblVideo.image = img
        lblVideo.after(10, visualizar)
    else:
        lblVideo.image = ""
        lblInfoVideoPath.configure(text="")
        rad1.configure(state="active")
        rad2.configure(state="active")
        selected.set(0)
        btnEnd.configure(state="disabled")
        cap.release()
        

def finalizar_limpiar():
    
    lblVideo.image = ""
    lblInfoVideoPath.configure(text="")
    rad1.configure(state="active")
    rad2.configure(state="active")
    selected.set(0)
    cap.release()
 
def goFrameApp():
    global root
    root.destroy()
    App.mainApp()
    
webCam = False
cap = None
lblVideo = None
lblInfoVideoPath = None
rad1, rad2 = None, None
selected = None
btnEnd = None
root = None

def mainAddData():
    global cap
    global lblVideo
    global lblInfoVideoPath
    global rad1, rad2
    global selected
    global btnEnd
    global root
    root = Tk() ## Crear la ventana
    root.title("Agregar Datos") ## Titulo de la ventana
    lblInfo1 = Label(root, text="Detección de Emociones", font="bold") ## Agregar una etiqueta
    lblInfo1.grid(column=0, row=0, columnspan=2) ## Ubicar la etiqueta

    selected = IntVar()  ## Crear una variable de tipo IntVar
    rad1 = Radiobutton(root, text="Elegir video", width=20, value=1, variable=selected, command=video_de_entrada) ## Crear un Radiobutton
    rad2 = Radiobutton(root, text="Video en directo", width=20, value=2, variable=selected, command=video_de_entrada) ## Crear un Radiobutton
    rad1.grid(column=0, row=1)  ## Ubicar el Radiobutton
    rad2.grid(column=1, row=1) ## Ubicar el Radiobutton


    lblInfoVideoPath = Label(root, text="", width=20) ## Agregar una etiqueta para identificar la ruta del video
    lblInfoVideoPath.grid(column=0, row=2) ## Ubicar la etiqueta

    lblVideo = Label(root) ## Agregar una etiqueta para visualizar el video
    lblVideo.grid(column=0, row=3, columnspan=2) ## Ubicar la etiqueta

    btnEnd = Button(root, text="Finalizar visualización y limpiar", state="disabled", command=finalizar_limpiar)
    btnEnd.grid(column=0, row=4, columnspan=2, pady=10)
    
    btnGoApp = Button(root, text="Ir a la pantalla principal", command=goFrameApp)
    btnGoApp.grid(column=0, row=5, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    mainAddData()
