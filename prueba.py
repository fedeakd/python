from tkinter  import*
master = Tk()
canvas = Canvas(master,width=500,height=400)

e = Entry(canvas)
b = Entry(canvas)
e.place(x=20,y=20)

e.config(bg="blue",state="normal",disabledbackground="CadetBlue1",insertbackground ="green",
         highlightbackground ="orange")
           
e.select_clear()
print(e.focus())

e.place(x=200,y=200)

canvas.pack()
def callback():
    print (e.get())
    print(a)

b = Button(master, text="get", width=10, command=callback)

