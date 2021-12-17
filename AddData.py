from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
from DetectarEmociones import detectionEmotion
import cv2
import imutils
import App
from SaveFaceFromVideo import safeFaceForVideo
from SaveFaceFromWebCam import safeFaceForVideoWebcam, saveFace, getListEmotion


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
       
def accion(event):
    global frame
    global emocion
    global btnEntrenar
    print("Hola")
    guardar = saveFace(frame, emocion)
    
    if(guardar):
        btnEntrenar.configure(state="active")
    
        
def visualizar():
    global bxbEmotion
    global webCam
    global cap
    global lblVideo
    global lblInfoVideoPath
    global rad1, rad2
    global selected
    global btnEnd
    global frame
    global emocion
    global btnEntrenar
    ## Emotion
    
    
    ret, frame = cap.read()
    if ret == True:
        frame = imutils.resize(frame, width=600)
        if(webCam):
            frame, rostro = safeFaceForVideoWebcam(frame, emotion=emocion)
            # cv2.imshow("rostro", rostro)
            root.bind('<Return>', accion)

        else:
            frame = safeFaceForVideo(frame, emotion=emocion)
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
        # btnEntrenar.configure(state="desable")
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
frame = None
bxbEmotion = None
emocion = ""
btnEntrenar = None

def mainAddData():
    global bxbEmotion
    global cap
    global lblVideo
    global lblInfoVideoPath
    global rad1, rad2
    global selected
    global btnEnd
    global root
    global btnEntrenar
    root = Tk() ## Crear la ventana
    root.title("Agregar Datos") ## Titulo de la ventana
    lblInfo1 = Label(root, text="Detección de Emociones", font="bold") ## Agregar una etiqueta
    lblInfo1.grid(column=0, row=0, columnspan=2) ## Ubicar la etiqueta

    selected = IntVar()  ## Crear una variable de tipo IntVar
    # bxbEmotion = Combobox(root, textvariable=selected, values=emotionOption, state="readonly") ## Crear una caja de seleccion
    # bxbEmotion.current(0)
    # bxbEmotion.grid(column=1, row=2)
    
    emotionOption = getListEmotion()
    print("emotionOption: "+str(emotionOption))

    bxbEmotion = Combobox(root, textvariable=selected, values=emotionOption, state="readonly") ## Crear una caja de seleccion
    bxbEmotion.grid(column=1, row=2)
    bxbEmotion.current(0)
    bxbEmotion.bind("<<ComboboxSelected>>", identificarEmotion)
    
    rad1 = Radiobutton(root, text="Elegir video", width=20, value=1, variable=selected, command=video_de_entrada) ## Crear un Radiobutton
    rad2 = Radiobutton(root, text="Video en directo", width=20, value=2, variable=selected, command=video_de_entrada) ## Crear un Radiobutton
    rad1.grid(column=0, row=1)  ## Ubicar el Radiobutton
    rad2.grid(column=1, row=1) ## Ubicar el Radiobutton


    lblInfoVideoPath = Label(root, text="", width=20) ## Agregar una etiqueta para identificar la ruta del video
    lblInfoVideoPath.grid(column=0, row=2) ## Ubicar la etiqueta

    lblVideo = Label(root) ## Agregar una etiqueta para visualizar el video
    lblVideo.grid(column=0, row=3, columnspan=2) ## Ubicar la etiqueta

    btnEnd = Button(root, text="Finalizar visualización \ny limpiar", state="disabled", command=finalizar_limpiar)
    btnEnd.grid(column=0, row=4, columnspan=2)
    
    btnEntrenar = Button(root, text="Entrenar el modelo", state="disabled", command=entrenar)
    btnEntrenar.grid(column=1, row=5)
    
    
    btnGoApp = Button(root, text="Ir a la pantalla principal", command=goFrameApp)
    btnGoApp.grid(column=0, row=5)

    root.mainloop()

def entrenar():
    global root
    global btnEntrenar
    print("Entrenando el modelo")
    btnEntrenar.configure(state="disabled")

def identificarEmotion(event):
    global bxbEmotion
    global emocion
    
    print("emotion: "+bxbEmotion.get())
    emocion = bxbEmotion.get()
    
if __name__ == "__main__":
    mainAddData()
