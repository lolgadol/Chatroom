from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import keyboard


my_username = input("Username: ")

win = Tk()
win.title("Chill Room")
  
# Title Label
ttk.Label(win, 
          text = "Eyalol's Chatroom",
          font = ("Times New Roman", 15), 
          background = 'green', 
          foreground = "white").grid(column = 0,
                                     row = 0)
  
# Creating scrolled text 
# area widget
text_area = scrolledtext.ScrolledText(win, 
                                      wrap = WORD, 
                                      width = 40, 
                                      height = 5, 
                                      font = ("Times New Roman",
                                              15))
  
text_area.grid(column = 0, pady = 1, padx = 10)
text_area.config(state = DISABLED)
input_text = Entry(win,width = 50)
input_text.grid(column = 0, row = 1)

def myClick():

    message = f"{my_username} >  {input_text.get()}"
# if the message isn't empty and there are no empty spaces
    if input_text.get().strip():
        text_area.config(state = NORMAL)
        text_area.insert(END,message + '\n')
        text_area.config(state = DISABLED)
        text_area.yview(END)
        input_text.delete(0,len(input_text.get()))
    

send_button = Button(win,text = "send",command = myClick).grid(column = 1,row = 1)



  
# Placing cursor in the text area
text_area.focus()
win.mainloop()










