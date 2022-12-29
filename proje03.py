from tkinter import *
from tkinter import messagebox
from gensim.models import KeyedVectors


kelimeVektoru = KeyedVectors.load_word2vec_format('trModel100', binary=True)
print(kelimeVektoru)

pencere= Tk()
pencere.title("Gensim Kütüphanesi")
canvas= Canvas(pencere, height=450, width=750)
canvas.pack()



frame_ust= Frame(pencere, bg="light blue")
frame_ust.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

frame_alt_sol= Frame(pencere, bg="light blue")
frame_alt_sol.place(relx=0.1, rely=0.21, relwidth=0.23, relheight=0.5)

frame_alt_sag= Frame(pencere, bg="light blue")
frame_alt_sag.place(relx=0.34, rely=0.21, relwidth=0.56, relheight=0.5)

hatirlatma_tipi_etiket= Label(frame_ust,bg="light blue", text="Gensim Kütüphanesi", font="Verdana 10 bold")
hatirlatma_tipi_etiket.pack(padx=10, pady=10, side=LEFT)


etiket1= Label(frame_alt_sol, text="Seçenekler:", bg="light blue", font="Verdana 9 bold")
etiket1.pack(padx=10, pady=10, anchor=NW)

pencere2= Tk()
pencere2.title("Arama Sonuçları")
pencere2.geometry("500x750")
def benzerKelimeler():
    anahtarKelimeler = entry.get().lower().split()
    etiket5= Label(text="Girdiğiniz kelimeler: " + ", ".join(anahtarKelimeler))
    etiket5.pack()
    if anahtarKelimeler:
        try:
            oneriler = kelimeVektoru.most_similar(positive=anahtarKelimeler)
            for oneri in oneriler:
                if not any(keyword in oneri[0] for keyword in anahtarKelimeler):

                    etiket3 = Label(pencere2,text="Benzer Kelime:" +oneri[0])
                    etiket3.pack(anchor=S)
                    etiket4 = Label(pencere2, text="https://www.google.com.tr/search?q=" + oneri[0])
                    etiket4.pack(anchor=S)
        except KeyError:
            messagebox.showwarning(pencere,"Girdiğiniz kelime kütüphanede yok!")


var= IntVar()

R1= Radiobutton(frame_alt_sol, text="Kelime gir", variable=var, value=1,bg="light blue", font="Verdana 8",command=benzerKelimeler)
R1.pack(padx=15, pady=5, anchor=NW)


var1= IntVar()
C2= Checkbutton(frame_alt_sol, text="Çıkış", variable=var1, onvalue=1, offvalue=0, bg="light blue", font="Verdana 9 bold", command=pencere.destroy)
C2.pack(padx=25, pady=2, anchor=NW)


metin_alani= Text(frame_alt_sag, height=9, width=50)
metin_alani.pack()


frame_alt_sag= Frame(pencere, bg="light blue")
frame_alt_sag.place(relx=0.34, rely=0.21, relwidth=0.56, relheight=0.5)

entry = Entry(frame_alt_sag, width=50, bg = "white")
entry.pack(padx=50, pady=50)

buton= Button(frame_alt_sag,text="Ara", command=benzerKelimeler)
buton.pack(anchor=S)

pencere.mainloop()