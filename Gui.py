from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
from DetectarEmociones import detectionEmotion
import cv2
import imutils

# faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# emotion_recognozer = getEmotion_recognozer()

def video_de_entrada():
    global cap
    if selected.get() == 1:
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
            visualizar()
    if selected.get() == 2:
        btnEnd.configure(state="active")
        rad1.configure(state="disabled")
        rad2.configure(state="disabled")
        lblInfoVideoPath.configure(text="")
        try:
            cap = cv2.VideoCapture(0)
        except:
            cap = cv2.VideoCapture(1)
        visualizar()
        
def visualizar():
    global cap
    ret, frame = cap.read()
    if ret == True:
        frame = imutils.resize(frame, width=600)
        frame = detectionEmotion(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(frame)
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
    
    
cap = None
root = Tk()
root.title("Deteccion de Rostros")
lblInfo1 = Label(root, text="Detección de Emociones", font="bold")
lblInfo1.grid(column=0, row=0, columnspan=2)

selected = IntVar()
rad1 = Radiobutton(root, text="Elegir video", width=20, value=1, variable=selected, command=video_de_entrada)
rad2 = Radiobutton(root, text="Video en directo", width=20, value=2, variable=selected, command=video_de_entrada)
rad1.grid(column=0, row=1)
rad2.grid(column=1, row=1)


lblInfoVideoPath = Label(root, text="", width=20)
lblInfoVideoPath.grid(column=0, row=2)

lblVideo = Label(root)
lblVideo.grid(column=0, row=3, columnspan=2)

btnEnd = Button(root, text="Finalizar visualización y limpiar", state="disabled", command=finalizar_limpiar)
btnEnd.grid(column=0, row=4, columnspan=2, pady=10)

root.mainloop()

