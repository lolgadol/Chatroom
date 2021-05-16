import socket
import select
import errno
import sys

from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import keyboard
import threading


#threading 

#Logic
HEADER_LENGTH = 10

IP = "176.230.236.159"
PORT = 25565
#Taking the username as input from sg.input
my_username = input("Username: ")
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((IP,PORT))
client_socket.setblocking(False)

username = my_username.encode("utf-8")
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header + username)

#GUI stuff


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



# while True:
#     message = input_text.get()
#     final_message = f"{my_username} >  {input_text.get()}"
# # if the message isn't empty and there are no empty spaces
#     if input_text.get().strip():
#         #make it appear on the screen
#         text_area.config(state = NORMAL)
#         text_area.insert(END,final_message + '\n')
#         text_area.config(state = DISABLED)
#         text_area.yview(END)
#         input_text.delete(0,len(input_text.get()))
#         #send it elsewhere
#         message = message.encode("utf-8")
#         message_header = f"{len(message):< {HEADER_LENGTH}}".encode("utf-8")
#         client_socket.send(message_header + message)

    #message = input(f"{my_username} > ")

    #if message:
        #message = message.encode("utf-8")
        #message_header = f"{len(message):< {HEADER_LENGTH}}".encode("utf-8")
        #client_socket.send(message_header + message)

def receive_messages():
    while True:
        try:
            while True:
                #print("function fucking works")
                username_header = client_socket.recv(HEADER_LENGTH)
                if not len(username_header):
                    print("connection closed by the server")
                    sys.exit()
                username_length = int(username_header.decode("utf-8").strip())
                username = client_socket.recv(username_length).decode("utf-8")

                message_header = client_socket.recv(HEADER_LENGTH)
                message_length = int(message_header.decode("utf-8").strip())
                message = client_socket.recv(message_length).decode("utf-8")
                print(f"{username} > {message}")
                final_message = f"{username} > {message}"

                text_area.config(state = NORMAL)
                text_area.insert(END,final_message + '\n')
                text_area.config(state = DISABLED)
                    
        except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print('Reading error',str(e))
                    sys.exit()
                    continue
                    
        except Exception as e:
            print('Error',str(e))
            sys.exit()


def sendMessage():
    message = input_text.get()
    final_message = f"{my_username} >  {input_text.get()}"
#   if the message isn't empty and there are no empty spaces
    if input_text.get().strip():
        #make it appear on the screen
        text_area.config(state = NORMAL)
        text_area.insert(END,final_message + '\n')
        text_area.config(state = DISABLED)
        text_area.yview(END)
        input_text.delete(0,len(input_text.get()))
        #send it elsewhere
        message = message.encode("utf-8")
        message_header = f"{len(message):< {HEADER_LENGTH}}".encode("utf-8")
        client_socket.send(message_header + message)



send_button = Button(win,text = "send",command = sendMessage).grid(column = 1,row = 1)
text_area.focus()
thread = threading.Thread(target = receive_messages)
thread.start()
win.mainloop()



# Placing cursor in the text area
