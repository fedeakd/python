from tkinter import*
import random
import time
class Pelota:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,0)
        self.x=0
        self.y=0
        self.canvas_height=self.canvas.winfo_height()
        self.canvas.bind_all("<KeyPress-Left>",self.ir_izq)
        self.canvas.bind_all("<KeyPress-Right>",self.ir_der)
        self.canvas.bind_all("<KeyPress-a>",self.tirar)
        
    def ir_izq (self,evt):
        self.x=-2
    def ir_der (self,evt):
        self.x=2
    def tirar(self,evt):
        self.y=3
        self.x=0
        
    def dibujar(self):
        self.canvas.move(self.id,self.x,self.y)
        self.pos =self.canvas.coords(self.id)
        
        if self.pos[3]>=self.canvas_height:
            self.y=0
        

















tk=Tk()
tk.title("Canasta")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.config(bg="black")
canvas.pack()
tk.update()
pelota=Pelota(canvas,"blue")
while 1:
    pelota.dibujar()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
