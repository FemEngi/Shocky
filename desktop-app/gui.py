
import threading

from struct import *

import unittest

import serial
import sys
import glob
import serial.tools.list_ports

import logging


from mttkinter import mtTkinter as tkinter

root_tk = tkinter.Tk()

import subprocess


# import tkinter
import customtkinter
import random
import main as main
import socket
import requests
import logging

import esptool
import multiprocessing
from multiprocessing import freeze_support

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)







sock.setblocking(0)
URL1="http://esp32.local"
def hello():
    print("success")
    

def nbrq2(args):
    global start
    start=True
    thread_list = []
    
    def executemainloop():
        global root_tk
        global start
        while start:
            root_tk.mainloop()
    def threader(argsy):
        global start
        requests.get(URL1+argsy)
        start=False
    thread = threading.Thread(target=threader, args=(args,))
    thread_list.append(thread) 
    thread.start()
    thread = threading.Thread(target=executemainloop)
    thread_list.append(thread) 
    thread.start()
    


    
acceptcodetog = False




def init_customtkinter():
    global toggle
    toggle = False 
    global durationindex
    durationindex=0
    global acceptcodetog
    acceptcodetog = False





# root_tk = tkinter.Tk()


# TkThread.install(tkt)





def run(func, name=None):
    threading.Thread(target=func, name=name).start()
        
        
root_tk.configure(background="#4d4d4d")
root_tk.geometry("800x950")

frame = customtkinter.CTkFrame(master=root_tk)
frame.grid(row=0,column=0, padx=20, pady=20)



def get_work_data():
    return 'data'



def button():
    global acceptcodetog
    acceptcodetog = not acceptcodetog
    if acceptcodetog:
        global clientpub, keypub
        clientpub, keypub = main.init(entry1.get())
        print(shockpower)
        print(vibratepower)
        acceptcode.configure(fg_color="green")
    else:
        acceptcode.configure(fg_color="red")
        # main.publish(clientpub, "mqtt/python/mqtt/" + key)

        
        
    

    

    
    

def shock():
    global clientpub, keypub
    shockvalue=int(sliders.get())
    print(shockvalue)
    url = (str("/1/"+str(rounded)+"/"+str(shockvalue)+"/"))
    if not acceptcodetog:
        
        nbrq2(url)
    else:
        main.senddata(clientpub, keypub, url)

    #url = (URL1+"/1/"+str(durations[durationindex])+"/"+str(shockvalue)+"/")
    
        

def vibrate():
    global clientpub, keypub
    vibratevalue=int(sliderv.get())
    print(vibratevalue)
    url = (str("/2/"+str(rounded)+"/"+str(vibratevalue)+"/"))
    if not acceptcodetog:
        
        nbrq2(url)
    else:
        main.senddata(clientpub, keypub, url)

def codegen():
    global toggle
    toggle = not toggle
    if toggle:
        # givecode.color=str("green")
        key = str(random.randint(0, 9999))
        print(key)
        # givecode._text=str(key)
        givecode.configure(text=str(key), fg_color="green")
        root_tk.update()
        
        client, key = main.init(key)
        main.subscribesys(client, key)
    else:
        givecode.configure(fg_color="red")
        main.unsubscribe(client, key)


shockpower = tkinter.IntVar()
vibratepower = tkinter.IntVar()

    


label = customtkinter.CTkLabel(master=frame, text="Shocky", font=("Roboto", 30))
label.grid(row=1,column=0, padx=20, pady=20)
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="shock code")
entry1.grid(row=1,column=2, padx=20, pady=20)
acceptcode=customtkinter.CTkButton(master=frame, text="go", command=button, fg_color="red")
acceptcode.grid(row=1,column=3, padx=20, pady=20)
labelbcd = customtkinter.CTkLabel(master=frame, text="shock", font=("Roboto", 30))
labelbcd.grid(row=2,column=0, padx=20, pady=20)
labelabc = customtkinter.CTkLabel(master=frame, text="vibrate", font=("Roboto", 30))
labelabc.grid(row=2,column=3, padx=20, pady=20)


sliders = customtkinter.CTkSlider(master=frame, from_=1, to=99, orientation="vertical", height=550, width=50, variable=shockpower, number_of_steps=98)
sliders.grid(row=3,column=0, padx=20, pady=20)
sliders_val = customtkinter.CTkLabel(master=frame, textvariable=shockpower, width=10, font=("Roboto", 20),anchor='w', compound='left')
sliders_val.grid(row=3,column=1, padx=20, pady=20, sticky = 'W')

sliderv = customtkinter.CTkSlider(master=frame, from_=1, to=99, orientation="vertical", height=550, width=50, variable=vibratepower, number_of_steps=98)
sliderv.grid(row=3,column=3, padx=20, pady=20)
sliderv_val = customtkinter.CTkLabel(master=frame, textvariable=vibratepower, width=10, font=("Roboto", 20))
sliderv_val.grid(row=3,column=2, padx=20, pady=20)
# sliders = customtkinter.CTkSlider(master=root_tk, command=slider_shock, orientation="vertical", number_of_steps=99)

shock=customtkinter.CTkButton(master=frame, text="shock!", command=shock)
shock.grid(row=4,column=0, padx=20, pady=20)

vibrate=customtkinter.CTkButton(master=frame, text="vibrate", command=vibrate)
vibrate.grid(row=4,column=3, padx=20, pady=20)


givecode=customtkinter.CTkButton(master=frame, text="0000", command=codegen, fg_color="red")
givecode.grid(row=1,column=1, padx=20, pady=20)



sliderv_val = customtkinter.CTkLabel(master=frame, text="duration = 0s", width=10, font=("Roboto", 20))
sliderv_val.grid(row=5,column=3, padx=20, pady=20)

sliderda = tkinter.DoubleVar()
rounded=0

def callback(value=None):
    global rounded
    rounded=round(sliderda.get(),2)
    sliderv_val.configure(text='duration = '+str(rounded)+"s")

sliderd = customtkinter.CTkSlider(master=frame, from_=0.1, to=15, orientation="horizontal", height=50, width=550, variable=sliderda, number_of_steps=149, command=callback)
sliderd.grid(row=5,column=0, padx=20, pady=20, columnspan = 3)



mp_context = multiprocessing.get_context('spawn')


from multiprocessing import Process

def esptoolnonblock(args, func):
    global top
    global start
    global startesptool
    start=True
    thread_list = []
    startesptool=True
    def executemainloop():
        global startesptool1
        global startesptool
        global top
        
        while True:
            root_tk.mainloop()
        print("gay123")
        top.destroy()
    def threader(argsy, top):
        esptool.main(argsy)
        # top.destroy()
    # thready = multiprocessing.Process(target=executemainloop)
    # thready.start()
    

    
    executors_list = []

    esptool.main(args,)
    
    top.destroy()
    
    
    # thready.terminate()
    startesptool=False
    # top.destroy()
    startesptool1=False
    

    

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result



def esp32c3f():
    global port
    global esp32c3f1
    esp32c3f1.configure(fg_color="red")
    global startesptool1
    startesptool1= True
    command = ['--port', str(port.get()),
               '--baud','115200',
			   '--after', 'no_reset', 'write_flash',
			   '--flash_mode', 'dout', '0x00000', 'esp32c3.bin']
    print('Using command %s' % ' '.join(command))
    if startesptool1:
        esptoolnonblock(command,esp32f)
    return
def esp32f():
    global port
    print(port.get())
    global esp32f1
    esp32f1.configure(fg_color="red")
    global startesptool1
    startesptool1= True
    command = ['--port', str(port.get()),'--baud', '460800', 'read_flash', '0', '0x200000', 'esp32f.bin']
    print('Using command %s' % ' '.join(command))
    if startesptool1:
        esptoolnonblock(command,esp32f)
    
        
    

def flash():
    global port
    global esp32c3f1
    global esp32f1
    print(serial.tools.list_ports.comports())
    comlist = serial.tools.list_ports.comports()
    connected = []
    for element in comlist:
        connected.append(element.device)
    print("Connected COM ports: " + str(connected))
    
    global top
    global startesptool
    top= tkinter.Toplevel(root_tk)
    port=customtkinter.StringVar(top)
    port.set(connected[0])
    w = tkinter.OptionMenu(top, port, *connected)
    w.grid(row=1, column=1)
    top.geometry("450x150")
    top.title("flash")
    top.configure(background="#4d4d4d")
    flashlabel=tkinter.Label(top, text= "Flash")
    flashlabel.grid(row=0, column=1)
    esp32c3f1=customtkinter.CTkButton(master=top, text="flash esp32c3 (p6)", command=esp32c3f)
    esp32c3f1.grid(row=1,column=0, padx=20, pady=20)
    esp32f1=customtkinter.CTkButton(master=top, text="flash esp32 (p13)", command=esp32f)
    esp32f1.grid(row=1,column=3, padx=20, pady=20)
    
    
flash=customtkinter.CTkButton(master=frame, text="flash", command=flash)
flash.grid(row=4,column=1, padx=20, pady=20, columnspan=2)



def customtkinterloop():
    global sliderdd
    global sliderda
    
    # sliderdd=tkinter.DoubleVar(master=root_tk,value=rounded)
    root_tk.mainloop()
    
