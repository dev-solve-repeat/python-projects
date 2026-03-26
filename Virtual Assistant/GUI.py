from tkinter import *
from PIL import Image, ImageTk
import action
import speech2text as st

root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#693085")

def ask():
    user_val = st.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END, 'User -->' + user_val + "\n")
    if bot_val != None:
        text.insert(END, "BOT <--" + str(bot_val) + "\n")
    
    if bot_val == "Sure. Good Day":
        root.destroy()
    
def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, 'User -->' + send + "\n")
    if bot != None:
        text.insert(END, "BOT <--" + str(bot) + "\n")
    
    if bot == "Sure. Good Day":
        root.destroy()

def del_text():
    text.delete("1.0", "end")

#Making Frame

frame = LabelFrame(root, padx = 100, pady = 7, borderwidth = 3, relief = "raised")
frame.config(bg = "#403085")
frame.grid(row = 0, column = 1, padx = 55, pady = 10)

#Text Label

text_label = Label(frame, text = "AI Assistant", font = ("comic sans ms", 14, "bold"), bg = "#7F5A92")
text_label.grid(row = 0, column = 0, padx = 20, pady = 10)

#Image - TO use Image we need pillow package which I am not installing because of vulnerability due to LiteLLM

image = ImageTk.PhotoImage(Image.open("Image/assitant.png"))
image_label = Label(frame, image = image)
image_label.grid(row = 1, column = 0, pady = 20)

#Adding a text Widget

text = Text(root, font = ('courier 10 bold'), bg = "#ADBF27")
text.grid(row = 2, column = 0)
text.place(x = 100, y = 375, width = 375, height =100)

#Entry Widget

entry = Entry(root, justify = CENTER)
entry.place(x = 100, y = 500, width = 390, height = 30)

#Button 1

button1 = Button(root, text="ASK", bg = "#9DB9DE", pady = 16, padx = 40, 
                 borderwidth = 3, relief = SOLID, command = ask)
button1.place(x = 70, y = 575)

#Button 2
button2 = Button(root, text="SEND", bg = "#9DB9DE", pady = 16, padx = 40, 
                 borderwidth = 3, relief = SOLID, command = send)
button2.place(x = 400, y = 575)

#Button 3

button3 = Button(root, text="Delete", bg = "#9DB9DE", pady = 16, padx = 40, 
                 borderwidth = 3, relief = SOLID, command = del_text)
button3.place(x = 225, y = 575)

root.mainloop()
