import time
import tkinter as tk
from datetime import datetime
import datetime
##from playsound import playsound
from setuptools.command.setopt import option_base

def alarm():
    while True:
        set_alarm_time = f'{hour.get()}:{minute.get()}:{second.get()}'
        time.sleep((1))
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(current_time, set_alarm_time)
        aud = '/home/notgabe/PycharmProjects/ProjetosInterfaceGrafica/phone-anime-209351.mp3'

        if current_time == set_alarm_time:
            playsound(aud)
            break


root = tk.Tk()
root.geometry("400x200")
root.title('Alarme Python')

tk.Label(root, text='Alarme Python', font=('Heveltica 20 bold')).pack(pady=10)
tk.Label(root, text='Definir alarme').pack(pady=5)

frame = tk.Frame(root)
frame.pack()


def option(value):
    opt = tk.StringVar(root)
    options = [str(i).zfill(2) for i in range(value)]
    opt.set(options[0])
    tk.OptionMenu(frame, opt, *options).pack(side=tk.LEFT)
    return opt

hour = option(24)
minute = option(60)
second = option(60)


tk.Button(root, text='Definir', font=('Helvetica 15'), command=alarm).pack(pady=20)


root.mainloop()

