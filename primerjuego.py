from tkinter import*
import time
import random
import MySQLdb


class Pelota:
    def __init__(self,canvas,raqueta,color,linea):
        self.canvas=canvas
        self.raqueta= raqueta
        self.id=canvas.create_oval(10,10,25,25,fill=color,outline=linea)
        self.canvas.move(self.id,245,200)
        empezar=[-3,-2,-1,1,2,3]
        random.shuffle(empezar)
        self.pepe=[]
        self.x=0
        self.y=3
        self.p=0
        self.p1=0
        self.canvas_height =self.canvas.winfo_height()
        self.canvas_whidth =self.canvas.winfo_width()
        self.golpea_fondo=False
        self.reinicio=False
        self.z=0
        self.c=0
        self.num2=canvas.create_text(270,390,text=self.c,fill="white",font=("Courier",10))
        self.num1=canvas.create_text(80,390,text=self.z,fill="white",font=("Courier",10))
        self.arriba=canvas.create_text(240,390,text="Lados: ",fill="white",font=("Courier",10))
        self.raque=canvas.create_text(40,390,text="Raqueta: ",fill="white",font=("Barbieri-Book",10))
        self.canvas.bind_all('<KeyPress-a>',self.devuelta)
        self.canvas.bind_all('<KeyPress-A>',self.devuelta)
        
    
    def golpea_raqueta(self,pos):
        self.raqueta_pos=self.canvas.coords(self.raqueta.id)
        if pos[2]>= self.raqueta_pos[0] and pos[0] <= self.raqueta_pos[2]:
            if pos[3] >= self.raqueta_pos[1]and pos[3] <=self.raqueta_pos[3]:
                self.x+=self.raqueta.x
                return True
        return False
    def golpea_raqueta2(self,pos):
        self.raqueta_pos2=self.canvas.coords(self.raqueta.ida)
        if pos[2]>=self.raqueta_pos2[0] and pos[0]<=self.raqueta_pos2[2]: 
           if pos[1]<= self.raqueta_pos2[3] and pos [1] >= self.raqueta_pos2[1]:
               
              return True
        return False
    
    def devuelta(self,evt):
        if self.golpea_fondo==True:
            self.pos=canvas.coords(fefe.id,230,200,245,215)
            self.raqueta_pos2=self.canvas.coords(self.raqueta.ida,200,50,300,60)
            self.raqueta_pos=self.canvas.coords(self.raqueta.id,200,350,300,360)
            self.y=2
            
            self.x=0
            self.reinicio=True
            self.golpea_fondo=False
                
            
        
        
    def dibujar (self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        self.canvas.move(self.raqueta.ida,self.x,0)
        """if self.y >= 0:
            self.e=0
        if self.y<=0:
            self.e=self.x
        if pos[1] <=0:
            self.golpea_fondo=True
        if self.x >=2:
            self.p =2
        if self.x<=-2:
            self.p=-2"""
    
        if pos[3] >= self.canvas_height:
            canvas.delete(self.num1)
            self.canvas.delete(self.num2)
            if (self.z>0):
                self.pepe.append(self.z)
            self.y=0
            self.x=0
            self.z=0
            self.c=0
            self.num1=canvas.create_text(80,390,text=self.z,fill="white",font=("Barbieri-Book",10))
            self.num2=canvas.create_text(270,390,text=self.c,fill="white",font=("Courier",10))
            
            
            self.golpea_fondo=True
            self.reinicio=False
            
        if pos[3] == 275:
            canvas.itemconfig(self.id,fill="red",outline="purple")
        if pos[1] == 200:
            canvas.itemconfig(self.id,fill="blue",outline="purple")
        if pos[1]== 150:
            canvas.itemconfig(self.id,fill="white",outline="purple")
            
         
        if self.golpea_raqueta(pos)== True:
            canvas.itemconfig(self.id,fill="purple",outline="purple")
            self.y=-3
            self.x=random.randrange(-3,3)
            canvas.delete(self.num1)
            self.z=self.z+1
            self.num1=canvas.create_text(80,390,text=self.z+1,fill="white",font=("Barbieri-Book",10))
            self.p=self.p+1
            self.p1=self.p1+1
           
   
        if self.golpea_raqueta2(pos)==True:
            self.y=3
            self.x=random.randrange(-3,3)
            canvas.itemconfig(self.id,fill="orange",outline="orange")
            self.p=self.p+1
            self.p1=self.p1+1
            
        if pos[2] >= self.canvas_whidth:
            self.canvas.delete(self.num2)
            self.x= -2
            self.c= self.c+1
            self.num2=canvas.create_text(270,390,text=self.c,fill="white",font=("Courier",10))
            
        if pos[0] <=0:
            self.x=2 
            self.canvas.delete(self.num2)
            self.c= self.c+1
            self.num2=canvas.create_text(270,390,text=self.c,fill="white",font=("Courier",10))
            
 
                
        
        
       

        
class Raqueta:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id =canvas.create_rectangle(0,0,100,10,fill=color,outline ="white")
        self.canvas.move(self.id,200,350)
        self.ida=canvas.create_rectangle(0,0,100,10, fill="dark grey",outline="yellow")
        self.canvas.move(self.ida,200,50)
        self.x=0
        self.canvas_width =self.canvas.winfo_width()
        self.empezado = False
        
        self.canvas.bind_all('<KeyPress-Left>',self.ir_izq)
        self.canvas.bind_all('<KeyPress-Right>',self.ir_der)
        self.canvas.bind_all('<Button-1>',self.empezar_juego)
        
    def ir_izq (self,evt):
        self.x=-3
    def ir_der(self,evt):
        self.x= 3
        
    def empezar_juego(self,evt):
        self.empezado = True
        
    def dibujar(self):
        self.canvas.move(self.id,self.x,0)
        self.pos=self.canvas.coords(self.id)
        
        if self.pos[0] ==0:
            self.x=0       
        elif self.pos[0] <0:
            self.x=1
        elif self.pos[2]==self.canvas_width:
            self.x=0
        elif self.pos[2] > self.canvas_width:
            self.x=-1

            
class Bloque:
    def __init__(self,canvas,color,fefe):
        self.pelota=fefe
        
        self.canvas=canvas
        self.id1 = canvas.create_rectangle(0,0,70,10,fill=color,state="normal")
        self.id2 = canvas.create_rectangle(0,0,70,10,fill=color,state="normal")
      
        self.moveb1=self.canvas.move(self.id1,random.randrange(0,200),200)
        self.moveb2=self.canvas.move(self.id2,random.randrange(200,400),200)
        self.l=0
        self.i=0
    def golpe_bloque(self,bloque1):
        self.pelota.pos=self.canvas.coords(self.pelota.id)
        if self.pelota.pos[2]>= self.bloque1[0] and self.pelota.pos[0] <= self.bloque1[2]:
            if self.pelota.pos[3] >= self.bloque1[1]and self.pelota.pos[3] <=self.bloque1[3]:
                return True
        return False
    def golpe_bloque1(self,bloque1):
        if self.pelota.pos[2]>= self.bloque1[0] and self.pelota.pos[0] <= self.bloque1[2]:
            if self.pelota.pos[1] <= self.bloque1[3]and self.pelota.pos[1] >=self.bloque1[1]:
                
                return True
        return False
    def golpe_b(self,bloque2):
        self.pelota.pos=self.canvas.coords(self.pelota.id)
        if self.pelota.pos[2]>= self.bloque2[0] and self.pelota.pos[0] <= self.bloque2[2]:
            if self.pelota.pos[3] >= self.bloque2[1]and self.pelota.pos[3] <=self.bloque2[3]:
                
                return True
        return False
        
    def golpe_b1 (self,bloque2):
        
        if self.pelota.pos[2]>= self.bloque2[0] and self.pelota.pos[0] <= self.bloque2[2]:
            if self.pelota.pos[1] <= self.bloque2[3]and self.pelota.pos[1] >=self.bloque2[1]:
                
                return True
        return False

        
        
        
        

    def dibujar (self):
        self.bloque1=self.canvas.coords(self.id1)
        self.bloque2=self.canvas.coords(self.id2)

        
        if self.golpe_b(self.bloque2)== True:
            self.pelota.y=-2
            self.i=self.i+1
        
        if self.golpe_b1(self.bloque2)== True:
            self.pelota.y=2
            self.i=self.i+1
        if self.i==1:
            canvas.itemconfig(self.id2,fill="white")
            
        if self.i==2:
            canvas.itemconfig(self.id2,fill="purple")
        if self.i==3:
            canvas.itemconfig(self.id2,fill="yellow")
        if self.i==4:
            canvas.itemconfig(self.id2,fill="red")
        if self.i>=5:
            canvas.move(self.id2,500,500)
            
                    
        if self.golpe_bloque(self.bloque1)== True:
            self.pelota.y=-2
            self.l=self.l+1
        if self.golpe_bloque1(self.bloque1)==True:
            self.pelota.y=2
            self.l=self.l+1

            
            
        if self.l==1:
            canvas.itemconfig(self.id1,fill="white")
            
        if self.l==2:
            canvas.itemconfig(self.id1,fill="purple")
        if self.l==3:
            canvas.itemconfig(self.id1,fill="yellow")
        if self.l==4:
            canvas.itemconfig(self.id1,fill="red")
        if self.l>=5:
            canvas.move(self.id1,500,500)
        if self.pelota.p >=35 and self.l>=5:
            self.q=random.randrange(0,200)
            self.canvas.coords(self.id1,self.q,200,(self.q+70),210)
            canvas.itemconfig(self.id1,fill="green")
            self.l=0
            self.pelota.p=0
            
            
        if self.pelota.p1 >=35 and self.i>=5:
            self.h=random.randrange(self.q+100,400)
            self.canvas.coords(self.id2,self.h,200,(self.h+70),210)
            canvas.itemconfig(self.id2,fill="green")
            self.i=0
            self.pelota.p1=0
            


        pass

tk = Tk()
tk.title("Mijuego")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas =Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.config(bg="white")
imagen=PhotoImage(file='c:\\racing_avellaneda_422969489.gif')

racing=canvas.create_image(110,0,anchor=NW,image=imagen)

canvas.pack()
tk.update()

raqueta=Raqueta(canvas,"dark blue")
fefe =Pelota(canvas,raqueta,"blue","blue")
bloque = Bloque(canvas,"green",fefe)
texto_fin_juego = canvas.create_text(250,200 ,font =("Barbieri-Book",34),text="Has Perdido",\
state="hidden")
texto=canvas.create_text(250,200,font = ("Barbieri-Book",34),text="Has Click para comenzar",fill="blue",\
                         state="normal")
presionara=canvas.create_text(250,250,font =("Barbieri-Book",24),text="Presiona ''a'' para reiniciar el juego",fill="white",state="hidden")
entrada=StringVar()
txtUsuario=Entry(canvas,textvariable=entrada).place(x=70,y=20)
entrada.set("escrbe tu nombre")
canvas.itemconfig(txtUsuario,state="hidden")



while 1:
    if  raqueta.empezado == True :
        canvas.config(bg="black")
        fefe.dibujar()
        raqueta.dibujar()
        bloque.dibujar()
        canvas.itemconfig(texto,state="hidden")
        canvas.itemconfig(bloque.id1,state="normal")
        canvas.itemconfig(bloque.id2,state="normal")
        canvas.delete(racing)
        
    if raqueta.empezado==False:
        canvas.itemconfig(bloque.id1,state="hidden")
        canvas.itemconfig(bloque.id2,state="hidden")
        texto
        
        
        
        
    elif fefe.golpea_fondo == True:
        
        time.sleep(0.03)
        canvas.itemconfig(texto_fin_juego,state="normal",fill="white")
        canvas.config(bg="red")
        canvas.itemconfig(presionara,state="normal")
        canvas.itemconfig(bloque.id1,state="hidden")
        canvas.itemconfig(bloque.id2,state="hidden")
        canvas.itemconfig(raqueta.id,state="hidden")
        canvas.itemconfig(raqueta.ida,state="hidden")
        canvas.itemconfig(fefe.id,state="hidden")
       
      
       
    elif fefe.reinicio==True:
        canvas.itemconfig(texto_fin_juego,state="hidden")
        canvas.config(bg="black")
        canvas.itemconfig(presionara,state="hidden")
        canvas.itemconfig(raqueta.id,state="normal")
        canvas.itemconfig(raqueta.ida,state="normal")
        canvas.itemconfig(fefe.id,state="normal")
        

    tk.update_idletasks()    
    tk.update()
    time.sleep(0.01)

    
 
