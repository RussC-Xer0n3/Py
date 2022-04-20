#! /usr/bin/env/ python3

from tkinter import *
window = TK()
window.title('UltraSound GUI')

#image = Canvas(window, image = image_index)
#image.pack(side = LEFT, padx = 10, pady = 10)
start_ultra = Button(window , height = 2 , width = 10 , justify = CENTER , text = 'Start ultrasound' , command = exit'''#startfunction''') # just type the name of the function no ()'s
start_ultra.pack(side = RIGHT , padx = 10)
stop_ultra = Button(window, height = 2 , width = 10 , justify = CENTER , text = 'Stop ultrasound' , command = exit '''#stopfunction''')
stop_ultra.pack(side = RIGHT , padx = 10)
start_rfid = Button(window , height = 2 , width = 5 , justify = CENTER , text = 'Start RFID' , command = exit'''#startfunction''')
start_rfid.pack(side = RIGHT , padx = 10)
stop_rfid = Button(window , height = 2 , width = 5 , justify = CENTER , text = 'Stop RFID' , command = exit'''#stopfunction''')
stop_rfid.pack(side = RIGHT , padx = 10)
btn = Button(window , text = 'Exit' , command = exit)
btn.pack(side = RIGHT , padx = 10)

window.mainloop()