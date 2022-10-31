"""from tkinter import *

app=Tk()
app.title("My page")
app.geometry("500x500")
app.configure(background="#9200F5")

txt1 = Label(app, text="Olá mundo", background="#F0F200", foreground="#000000")
txt1.place(x=150, y=5, width=200, height= 20)

txt2 = Label(app, text="Vamos jogar", background="#00F0F9", foreground="#000000")
txt2.place(x=150, y=50, width=200, height= 20)

app.mainloop()"""

from tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack ()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Clique aqui"
        self.sair["font"] = ("Calibri", "9")
        self.sair["width"] = 10
        self.sair.bind("<Button-1>", self.mudarTexto)
        self.sair.pack ()

    def mudarTexto(self, event):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"


root = Tk()
Application(root)
root.mainloop()