"""
@Furkan Güven
"""
from tkinter import *  #kütüphane dahil edildi
gui=Tk()
gui.title("Hesap Makinesi    *Furkan Güven Tarafından Yazıldı.*")
gui.geometry("350x250")


def press(num): #metin giriş kutusuna basılınca

    global expression
    expression = expression + str(num) #dizileri birleştirme işlemi
    equation.set(expression) #set yöntemini kullanarak ifadeyi güncelleyin

def equalpress(): #eşittir ifadesini değerlendirme işlemi
    try:
   	    global expression
   	    total = str(eval(expression))
   	    equation.set(total)
   	    expression = ""
    except:
   	    equation.set(" HATA ")
   	    expression = ""

def clear(): #temizleme fonksiyonu
    global expression
    expression = ""
    equation.set("")

equation = StringVar()

expression_field = Entry(gui, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=65,padx=10)

expression = "" #ifade değişkeni global olarak belirtildi

equation.set('ISLEM YAPIN')

sil = Button(gui,text="C",width=5,height=2, command=clear)
sil.grid(column=4,row=0)
sil.grid(padx=10,pady=10)

yedi = Button(gui,text="7",width=10,height=2, command=lambda: press(7))
yedi.grid(column=1,row=1)

sekiz = Button(gui,text="8",width=10,height=2, command=lambda: press(8))
sekiz.grid(column=2,row=1)

dokuz = Button(gui,text="9",width=10,height=2, command=lambda: press(9))
dokuz.grid(column=3,row=1)
bolme = Button(gui,text="/",width=5,height=2, command=lambda: press("/"))
bolme.grid(column=4,row=1)

dort = Button(gui,text="4",width=10,height=2, command=lambda: press(4))
dort.grid(column=1,row=2)
bes = Button(gui,text="5",width=10,height=2, command=lambda: press(5))
bes.grid(column=2,row=2)
alti = Button(gui,text="6",width=10,height=2, command=lambda: press(6))
alti.grid(column=3,row=2)
carpma = Button(gui,text="*",width=5,height=2, command=lambda: press("*"))
carpma.grid(column=4,row=2)

bir = Button(gui,text="1",width=10,height=2, command=lambda: press(1))
bir.grid(column=1,row=3)
iki = Button(gui,text="2",width=10,height=2, command=lambda: press(2))
iki.grid(column=2,row=3)
uc = Button(gui,text="3",width=10,height=2, command=lambda: press(3))
uc.grid(column=3,row=3)
eksi = Button(gui,text="-",width=5,height=2, command=lambda: press("-"))
eksi.grid(column=4,row=3)

sifir = Button(gui,text="0",width=10,height=2, command=lambda: press(0))
sifir.grid(column=1,row=4)
nokta = Button(gui,text=".",width=10,height=2, command=lambda: press("."))
nokta.grid(column=2,row=4)
esittir = Button(gui,text="=",width=10,height=2, command=equalpress)
esittir.grid(column=3,row=4)
arti = Button(gui,text="+",width=5,height=2, command=lambda: press("+"))
arti.grid(column=4,row=4)

gui.mainloop()
