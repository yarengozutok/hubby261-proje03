
from tkinter import *

pencere = Tk()
pencere.title("Gensim Kütüphanesi")
pencere.geometry("600x200")

etiket=Label(pencere, text="Gensim Kütüphanesine Hoşgeldiniz",fg="green", font="8")
etiket.pack()


def kelimelerial():
    etiket2["text"]=entry.get()

etiket2 = Label(text="Kelimeler")
etiket2.pack()

entry=Entry()
entry.pack()

buton=Button(pencere, text= "Anahtar Kelime Girişi", command=kelimelerial)
buton.pack()



pencere.mainloop()