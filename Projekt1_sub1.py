from tkinter import *
import sqlite3
from datetime import date 
import customtkinter as ctk
from tkinter import *  
from PIL import Image   

AnzahlBo=0;AnzahlBr=0;AnzahlE=0;AnzahlF=0;AnzahlG=0;AnzahlK=0;AnzahlKh=0;AnzahlKr=0;AnzahlL=0;AnzahlM=0;AnzahlP=0;AnzahlR=0;AnzahlSa=0;AnzahlSp=0;AnzahlT=0;AnzahlZ=0
wid1= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Bohnen.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Bohnen.png'),size=(30,30))
wid2= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Brokkoli.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Brokkoli.png'),size=(30,30))
wid3= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Erbse.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Erbse.png'),size=(30,30))
wid4= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Gurke.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Gurke.png'),size=(30,30))


def insertBohne():
    global AnzahlBo
    AnzahlBo=AnzahlBo+1
def insertBrokkoli():
    global AnzahlBr
    AnzahlBr=AnzahlBr+1
def insertErbse():
    global AnzahlE
    AnzahlE=AnzahlE+1
def insertFeldsalat():
    global AnzahlF
    AnzahlF=AnzahlF+1
def insertGurke():
    global AnzahlG
    AnzahlG=AnzahlG+1
def insertKartoffel():
    global AnzahlK
    AnzahlK=AnzahlK+1
def insertKohl():
    global AnzahlKh
    AnzahlKh=AnzahlKh+1
def insertKohlrabi():
    global AnzahlKr
    AnzahlKr=AnzahlKr+1
def insertLauch():
    global AnzahlL
    AnzahlL=AnzahlL+1
def insertMoehre():
    global AnzahlM
    AnzahlM=AnzahlM+1
def insertPaprika():
    global AnzahlP
    AnzahlP=AnzahlP+1
def insertRadieschen():
    global AnzahlR
    AnzahlR=AnzahlR+1
def insertSalat():
    global AnzahlSa
    AnzahlSa=AnzahlSa+1
def insertSpinat():
    global AnzahlSp
    AnzahlSp=AnzahlSp+1
def insertTomate():
    global AnzahlT
    AnzahlT=AnzahlT+1
def insertZwiebel():
    global AnzahlZ
    AnzahlZ=AnzahlZ+1


def speichern(cur,conn):

    
    print("SPEICHERN")
    global AnzahlBo, AnzahlBr, AnzahlE, AnzahlF, AnzahlG,AnzahlK,AnzahlKh,AnzahlKr,AnzahlL,AnzahlM,AnzahlP,AnzahlR,AnzahlSa,AnzahlSp,AnzahlT,AnzahlZ
    Beetset2 = [AnzahlBo,AnzahlBr,AnzahlE,AnzahlF,AnzahlG,AnzahlK,AnzahlKh,AnzahlKr,AnzahlL,AnzahlM,AnzahlP,AnzahlR,AnzahlSa,AnzahlSp,AnzahlT,AnzahlZ]
    cur.execute("INSERT INTO Beet VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",Beetset2)
    conn.commit()
    conn.close()
    AnzahlBo=0;AnzahlBr=0;AnzahlE=0;AnzahlF=0;AnzahlG=0;AnzahlK=0;AnzahlKh=0;AnzahlKr=0;AnzahlL=0;AnzahlM=0;AnzahlP=0;AnzahlR=0;AnzahlSa=0;AnzahlSp=0;AnzahlT=0;AnzahlZ=0
    opendashboard()

def open_Top_40():
    global wid1,wid2,wid3,wid4,wid5,wid6,wid7,wid8,wid9,wid10,wid11,wid12,wid13,wid14,wid15,wid16
    wid1= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Bohnen.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Bohnen.png'),size=(30,30))
    wid2= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Brokkoli.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Brokkoli.png'),size=(30,30))
    wid3= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Erbse.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Erbse.png'),size=(30,30))
    wid4= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Feldsalat.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Feldsalat.png'),size=(30,30))
    wid5= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Gurke.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Gurke.png'),size=(30,30))
    wid6= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Kartoffel.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Kartoffel.png'),size=(30,30))
    wid7= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Kohl.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Kohl.png'),size=(30,30))
    wid8= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Kohlrabi.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Kohlrabi.png'),size=(30,30))
    wid9= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Lauch.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Lauch.png'),size=(30,30))
    wid10= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Moehre.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Moehre.png'),size=(30,30))
    wid11= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Paprika.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Paprika.png'),size=(30,30))
    wid12= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Radieschen.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Radieschen.png'),size=(30,30))
    wid13= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Salat.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Salat.png'),size=(30,30))
    wid14= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Spinat.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Spinat.png'),size=(30,30))
    wid15= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Tomate.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Tomate.png'),size=(30,30))
    wid16= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Zwiebel.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Zwiebel.png'),size=(30,30))

    
    Top_40 = ctk.CTk()
    Top_40.title("Wählen Sie Ihre Pflanzen")
    
    Bo = ctk.CTkButton(Top_40,image=wid1,text="Bohne",command=insertBohne) #image = wid1..
    Br = ctk.CTkButton(Top_40,image=wid2,text="Brokkoli", command=insertBrokkoli)
    E = ctk.CTkButton(Top_40,image=wid3,text="Erbse", command=insertErbse)
    F = ctk.CTkButton(Top_40,image=wid4,text="Feldsalat", command=insertFeldsalat)
    G = ctk.CTkButton(Top_40,image=wid5,text="Gurke", command=insertGurke)
    K = ctk.CTkButton(Top_40,image=wid6,text="Kartoffel", command=insertKartoffel)
    Kh = ctk.CTkButton(Top_40,image=wid7,text="Kohl", command=insertKohl)
    Kr = ctk.CTkButton(Top_40,image=wid8,text="Kohlrabi", command=insertKohlrabi)
    L = ctk.CTkButton(Top_40,image=wid9,text="Lauch", command=insertLauch)
    M = ctk.CTkButton(Top_40,image=wid10,text="Möhre", command=insertMoehre)
    P = ctk.CTkButton(Top_40,image=wid11,text="Paprika", command=insertPaprika)
    R = ctk.CTkButton(Top_40,image=wid12,text="Radieschen", command=insertRadieschen)
    Sa = ctk.CTkButton(Top_40,image=wid13,text="Salat", command=insertSalat)
    Sp = ctk.CTkButton(Top_40,image=wid14,text="Spinat", command=insertSpinat)
    T = ctk.CTkButton(Top_40,image=wid15,text="Tomate", command=insertTomate)
    Z = ctk.CTkButton(Top_40,image=wid16,text="Zwiebel", command=insertZwiebel)
    
    Submit = ctk.CTkButton(Top_40, text="Speichern", font=('Helvetica',10),width=8, text_color='black',fg_color='#FFB90F',command=lambda:[Top_40.destroy(),speichern(cursor,conn)])
    Bo.grid(row=0,column=0)
    Br.grid(row=0,column=1)
    E.grid(row=0,column=2)
    F.grid(row=0,column=3)
    G.grid(row=1,column=0)
    K.grid(row=1,column=1)
    Kh.grid(row=1,column=2)
    Kr.grid(row=1,column=3)
    L.grid(row=2,column=0)
    M.grid(row=2,column=1)
    P.grid(row=2,column=2)
    R.grid(row=2,column=3)
    Sa.grid(row=3,column=0)
    Sp.grid(row=3,column=1)
    T.grid(row=3,column=2)
    Z.grid(row=3,column=3)
    Submit.grid(row=4,column=2)
    Top_40.mainloop()
def try_choose_plants():
    try:
        global cursor,conn
        conn=sqlite3.connect("D:\Programmtests\DB\Beet.db")
        cursor=conn.cursor()   
        cursor.execute("SELECT name FROM sqlite_master WHERE type ='table' AND name ='Beet'")
        result = cursor.fetchone()
        if result is not None:
            conn.close()
            opendashboard()
        
        else:
            sql = "CREATE TABLE IF NOT EXISTS Beet("\
                 "AnzahlBo INTEGER,"\
                 "AnzahlBr INTEGER,"\
                 "AnzahlE INTEGER,"\
                 "AnzahlF INTEGER,"\
                 "AnzahlG INTEGER,"\
                 "AnzahlK INTEGER,"\
                 "AnzahlKh INTEGER,"\
                 "AnzahlKr INTEGER,"\
                 "AnzahlL INTEGER,"\
                 "AnzahlM INTEGER,"\
                 "AnzahlP INTEGER,"\
                 "AnzahlR INTEGER,"\
                 "AnzahlSa INTEGER,"\
                 "AnzahlSp INTEGER,"\
                 "AnzahlT INTEGER,"\
                 "AnzahlZ INTEGER)"
                           
            cursor.execute(sql)
            open_Top_40()
               
            
    except Exception as e:
        print("Exception with DB-opening", e)

def CheckPlantCompatible():


    wid1= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Bohnen.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Bohnen.png'),size=(30,30))
    wid2= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Brokkoli.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Brokkoli.png'),size=(30,30))
    wid3= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Erbse.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Erbse.png'),size=(30,30))
    wid4= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Feldsalat.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Feldsalat.png'),size=(30,30))
    wid5= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Gurke.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Gurke.png'),size=(30,30))
    wid6= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Kartoffel.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Kartoffel.png'),size=(30,30))
    wid7= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Kohl.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Kohl.png'),size=(30,30))
    wid8= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Kohlrabi.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Kohlrabi.png'),size=(30,30))
    wid9= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Lauch.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Lauch.png'),size=(30,30))
    wid10= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Moehre.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Moehre.png'),size=(30,30))
    wid11= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Paprika.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Paprika.png'),size=(30,30))
    wid12= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Radieschen.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Radieschen.png'),size=(30,30))
    wid13= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Salat.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Salat.png'),size=(30,30))
    wid14= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Spinat.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Spinat.png'),size=(30,30))
    wid15= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Tomate.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Tomate.png'),size=(30,30))
    wid16= ctk.CTkImage(light_image=Image.open('D:\Programmtests\Img\Widgets\Zwiebel.png'),dark_image=Image.open('D:\Programmtests\Img\Widgets\Zwiebel.png'),size=(30,30))

    Top_41 = ctk.CTk()
    Top_41.title("Mischkultur")
    
    def Bohne():
        E.configure(state=DISABLED,fg_color="grey")
        Z.configure(state=DISABLED,fg_color="grey")
        L.configure(state=DISABLED,fg_color="grey")
    def Brokkoli():
        Z.configure(state=DISABLED,fg_color="grey")
    def Erbse():
        Bo.configure(state=DISABLED,fg_color="grey")
        K.configure(state=DISABLED,fg_color="grey")
        P.configure(state=DISABLED,fg_color="grey")
        L.configure(state=DISABLED,fg_color="grey")
    def Gurke():
        T.configure(state=DISABLED,fg_color="grey")
        R.configure(state=DISABLED,fg_color="grey")
    def Kartoffel():
        T.configure(state=DISABLED,fg_color="grey")
        Kh.configure(state=DISABLED,fg_color="grey")
        E.configure(state=DISABLED,fg_color="grey")
        Sa.configure(state=DISABLED,fg_color="grey")
        P.configure(state=DISABLED,fg_color="grey")
        Z.configure(state=DISABLED,fg_color="grey")
    def Kohl():
        K.configure(state=DISABLED,fg_color="grey")
        Kr.configure(state=DISABLED,fg_color="grey")
        Z.configure(state=DISABLED,fg_color="grey")
    def Kohlrabi():
        Kh.configure(state=DISABLED,fg_color="grey")
    def Lauch():
        Bo.configure(state=DISABLED,fg_color="grey")
        E.configure(state=DISABLED,fg_color="grey")
        Z.configure(state=DISABLED,fg_color="grey")
    def Paprika():
        K.configure(state=DISABLED,fg_color="grey")
        E.configure(state=DISABLED,fg_color="grey")
    def Radieschen():
        G.configure(state=DISABLED,fg_color="grey")
    def Salat():
        K.configure(state=DISABLED,fg_color="grey")    
    def Tomate():
        G.configure(state=DISABLED,fg_color="grey")
        K.configure(state=DISABLED,fg_color="grey")
    def Zwiebel():
        Bo.configure(state=DISABLED,fg_color="grey")
        K.configure(state=DISABLED,fg_color="grey")
        Kh.configure(state=DISABLED,fg_color="grey")
        Br.configure(state=DISABLED,fg_color="grey")
        L.configure(state=DISABLED,fg_color="grey")
    def Reset():
        Bo.configure(fg_color="#3B8ED0",state = NORMAL); Br.configure(fg_color="#3B8ED0",state = NORMAL)
        E.configure(fg_color="#3B8ED0",state = NORMAL); F.configure(fg_color="#3B8ED0",state = NORMAL)
        G.configure(fg_color="#3B8ED0",state = NORMAL); K.configure(fg_color="#3B8ED0",state = NORMAL)
        Kh.configure(fg_color="#3B8ED0",state = NORMAL); Kr.configure(fg_color="#3B8ED0",state = NORMAL)
        L.configure(fg_color="#3B8ED0",state = NORMAL); M.configure(fg_color="#3B8ED0",state = NORMAL)
        P.configure(fg_color="#3B8ED0",state = NORMAL); R.configure(fg_color="#3B8ED0",state = NORMAL)
        Sa.configure(fg_color="#3B8ED0",state = NORMAL); Sp.configure(fg_color="#3B8ED0",state = NORMAL)
        T.configure(fg_color="#3B8ED0",state = NORMAL); Z.configure(fg_color="#3B8ED0",state = NORMAL)
    #Mk=Mischkultur, zeigt beste Mischkulturen an in On-Top Fenster
    
    Bo = ctk.CTkButton(Top_41,image=wid1, command=Bohne);Br = ctk.CTkButton(Top_41,image=wid2, command=Brokkoli)
    E = ctk.CTkButton(Top_41,image=wid3, command=Erbse);F = ctk.CTkButton(Top_41,image=wid4, command=None)
    G = ctk.CTkButton(Top_41,image=wid5, command=Gurke);K = ctk.CTkButton(Top_41,image=wid6, command=Kartoffel)
    Kh = ctk.CTkButton(Top_41,image=wid7, command=Kohl);Kr = ctk.CTkButton(Top_41,image=wid8, command=Kohlrabi)
    L = ctk.CTkButton(Top_41,image=wid9, command=Lauch);M = ctk.CTkButton(Top_41,image=wid10, command=None)
    P = ctk.CTkButton(Top_41,image=wid11, command=Paprika);R = ctk.CTkButton(Top_41,image=wid12, command=Radieschen)
    Sa = ctk.CTkButton(Top_41,image=wid13, command=Salat);Sp = ctk.CTkButton(Top_41,image=wid14, command=None)
    T = ctk.CTkButton(Top_41,image=wid15, command=Tomate);Z = ctk.CTkButton(Top_41,image=wid16, command=Zwiebel)
    Resetbtn = ctk.CTkButton(Top_41,text="Zurücksetzen",text_color='black',fg_color='#FFB90F', command= Reset)                 
    Bo.grid(row=0,column=0);Br.grid(row=0,column=1);E.grid(row=0,column=2);F.grid(row=0,column=3)
    G.grid(row=1,column=0);K.grid(row=1,column=1);Kh.grid(row=1,column=2);Kr.grid(row=1,column=3)
    L.grid(row=2,column=0);M.grid(row=2,column=1);P.grid(row=2,column=2);R.grid(row=2,column=3)
    Sa.grid(row=3,column=0);Sp.grid(row=3,column=1);T.grid(row=3,column=2);Z.grid(row=3,column=3)
    Resetbtn.grid(row=4, column=3)
    
    Top_41.mainloop()       
      

def opendashboard():       
                                              
    Today=date.today()
    Pflanzenliste=["Bohne","Brokkoli","Erbse","Feldsalat","Gurke","Kartoffel","Kohl","Kohlrabi",
                   "Lauch","Möhre","Paprika","Radieschen","Salat","Spinat","Tomate","Zwiebel"]
    Pflanzliste=[]                                                                                    
     #ReadPlantDb=Pflanzendatenbanklesen zeigt früheste Aussaat aller Pflanzen an: Pflanzen aus DB entnommen die vorher ausgewählt, früheste Aussaat aller pflanzen
    def ReadPlantDb():
        lauf=0 
                                                             
        conn1=sqlite3.connect("D:\Programmtests\DB\Beet.db")                  
        conn2=sqlite3.connect("D:\Programmtests\DB\Plants.db")  
        cur1=conn1.cursor()                                     
        cur2=conn2.cursor()
        cur3=conn2.cursor()   
        sql1="SELECT * FROM Beet"                        
        sql2="SELECT frühesteAussaat FROM Pflanzen"
        sql3="SELECT spätesteAussaat FROM Pflanzen"
        cur1.execute(sql1)                                     
        cur2.execute(sql2)
        cur3.execute(sql3)

        for i in cur1:                                       
            Auswahlliste=list(i)

        Fruehesteaussliste=list(j[0]for j in(cur2.fetchall()))
        Spaetesteaussliste=list(k[0]for k in(cur3.fetchall()))
        print(Fruehesteaussliste)

        for i in range (len(Auswahlliste)):                            
            if (Auswahlliste[lauf]>0):  
                if(Fruehesteaussliste[lauf]==Today.month):
                    Pflanzliste.append(Pflanzenliste[lauf])
                if((Today.month>Fruehesteaussliste[lauf])and(Today.month<=Spaetesteaussliste[lauf])):
                    Pflanzliste.append(Pflanzenliste[lauf])

            lauf=lauf+1

        separator=','                                           
        Lbl20.configure(text=str(separator.join(Pflanzliste)))         
        lauf=0
        conn1.close()
        conn2.close()
    

    def newplantselection():
        conn = sqlite3.connect("D:\Programmtests\DB\Beet.db")
        cur = conn.cursor()
        sql = "DROP TABLE Beet"
        cur.execute(sql)
        conn.commit()
        conn.close()
        
        try_choose_plants()

    Top_4 = ctk.CTk()
    Top_4.title("Pflanzenmanager")
    Top_4.geometry('500x400')
    Top_42=ctk.CTkFrame(Top_4)
    conn = sqlite3.connect("D:\Programmtests\DB\Beet.db")
    cur = conn.cursor()
    sql = "SELECT * FROM Beet"
    cur.execute(sql)
    L=-1
    for I2 in cur:
        L=L+1

        Lbl0=ctk.CTkLabel(Top_42, text='Bohne: '+ str(I2[0]),font=('Helvetica',20),text_color='black',fg_color='#FFB90F',width=12)
        Lbl0.grid(row=5,column=2)
        L=L+1
        Lbl1=ctk.CTkLabel(Top_42, text='Brokkoli: '+ str(I2[1]),font=('Helvetica',20),text_color='black',fg_color='#FFB90F',width=12)
        Lbl1.grid(row=6,column=2)
        L=L+1
        Lbl2=ctk.CTkLabel(Top_42, text='Erbse: '+ str(I2[2]),font=('Helvetica',20),text_color='black',fg_color='#FFB90F',width=12)
        Lbl2.grid(row=7,column=2)
        L=L+1         
        Lbl3=ctk.CTkLabel(Top_42, text='Feldsalat: '+ str(I2[2]),font=('Helvetica',20),text_color='black',fg_color='#FFB90F',width=12)
        Lbl3.grid(row=8,column=2)
        L=L+1         
        Lbl4=ctk.CTkLabel(Top_42, text='Gurke: '+ str(I2[2]),font=('Helvetica',20),text_color='black',fg_color='#FFB90F',width=12)
        Lbl4.grid(row=5,column=3)
        L=L+1         
        Lbl5=ctk.CTkLabel(Top_42, text='Kartoffel: '+ str(I2[2]),font=('Helvetica',20),text_color='black',fg_color='#FFB90F',width=12)
        Lbl5.grid(row=6,column=3)
        L=L+1         
        Lbl6=ctk.CTkLabel(Top_42, text='Kohl: '+ str(I2[2]),font=('Helvetica',20),text_color='black',fg_color='#FFB90F',width=12)
        Lbl6.grid(row=7,column=3)
        L=L+1 
        Lbl7=ctk.CTkLabel(Top_42, text='Kohlrabi: '+ str(I2[2]),font=('Helvetica',20),text_color='black',fg_color='#FFB90F',width=12)
        Lbl7.grid(row=8,column=3)
        L=L+1      
        Lbl8=ctk.CTkLabel(Top_42, text='Lauch: '+ str(I2[2]),font=('Helvetica',20),text_color='black',fg_color='#FFB90F',width=12)
        Lbl8.grid(row=5,column=4)
        L=L+1   
        Lbl9=ctk.CTkLabel(Top_42, text='Möhre: '+ str(I2[2]),font=('Helvetica',20),text_color='black',fg_color='#FFB90F',width=12)
        Lbl9.grid(row=6,column=4)
        L=L+1 
        Lbl10=ctk.CTkLabel(Top_42, text='Paprika: '+ str(I2[2]),font=('Helvetica',20),text_color='black',fg_color='#FFB90F',width=12)
        Lbl10.grid(row=7,column=4)
        L=L+1  
        Lbl11=ctk.CTkLabel(Top_42, text='Radieschen: '+ str(I2[2]),font=('Helvetica',20),text_color='black',fg_color='#FFB90F',width=12)
        Lbl11.grid(row=8,column=4)
        L=L+1         
        Lbl12=ctk.CTkLabel(Top_42, text='Salat: '+ str(I2[2]),font=('Helvetica',20),text_color='black',fg_color='#FFB90F',width=12)
        Lbl12.grid(row=5,column=5)
        L=L+1 
        Lbl13=ctk.CTkLabel(Top_42, text='Spinat: '+ str(I2[2]),font=('Helvetica',20),text_color='black',fg_color='#FFB90F',width=12)
        Lbl13.grid(row=6,column=5)
        L=L+1      
        Lbl14=ctk.CTkLabel(Top_42, text='Tomate: '+ str(I2[2]),font=('Helvetica',20),text_color='black',fg_color='#FFB90F',width=12)
        Lbl14.grid(row=7,column=5)
        L=L+1   
        Lbl15=ctk.CTkLabel(Top_42, text='Zwiebel: '+ str(I2[2]),font=('Helvetica',20),text_color='black',fg_color='#FFB90F',width=12)
        Lbl15.grid(row=8,column=5)
        L=L+1  
    Top_42.pack()
        

    conn.close()            

    Lblbr1=ctk.CTkLabel(Top_4, text='',width=12)

    Btn1=ctk.CTkButton(Top_4, text="Jetzt einpflanzen: ",font=('Helvetica',20),text_color='#FFB90F',fg_color='#573827',width=14, command=lambda:ReadPlantDb())    
    Lbl20=ctk.CTkLabel(Top_4, text="",font=('Helvetica',20),text_color='#FFB90F',fg_color='#573827',width=24)                        

    Btn2=ctk.CTkButton(Top_4, text="Mischkultur",font=('Helvetica',20),text_color='#FFB90F',fg_color='#573827',width=14, command=lambda:[Top_4.destroy(),CheckPlantCompatible()])
    Btn3=ctk.CTkButton(Top_4, text="Neupflanzenwahl",font=('Helvetica',20),text_color='#FFB90F',fg_color='#573827',width=14, command=lambda:[Top_4.destroy(),newplantselection()])
    Lbl21=ctk.CTkLabel(Top_4, text="Charge aktiv",font=('Helvetica',20),text_color='#FFB90F',fg_color='#573827',width=14)
    
    Lblbr1.pack()
    Btn1.pack()
    Lbl20.pack()

    Btn2.pack()
    Btn3.pack()
    Lbl21.pack()
    
    Top_4.mainloop()

        
try_choose_plants()