import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from datetime import date
import customtkinter as ctk
from PIL import ImageTk,Image 
import sqlite3
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('Agg')
import subprocess
from subprocess import Popen


         

root=ctk.CTk()
root_Frame_0 = ctk.CTkFrame(root, fg_color="#FFFFFF")

custom_font=("Helvetica",15)

class Segment_Buttons(): 

    def __init__(self,button_text,button_color):
        btn_project= ctk.CTkButton(root_Frame_0, text=button_text,fg_color=button_color,hover_color="#EF9912",height=100,width=100,font=custom_font, command=lambda:[self.onbtnclick(btn_project),open_Top_0()])
        #Buttons.bind("<Button-1>",onbtnclick)
        btn_project._text_label.configure(wraplength=110)
        btn_project.grid()
        
    def onbtnclick(self, btn_project):
        global button_text
        button_text=btn_project.cget("text")
        print(button_text)

class Segment_Mimes():
    def __init__(self,button_text,button_color):
        
        btn_project_mime= ctk.CTkButton(root_Frame_0, text=button_text,fg_color=button_color,hover_color="#EF9912",height=100,width=100,font=custom_font, command=lambda:[self.confirm_delete(btn_project_mime,button_text,button_color)])
        btn_project_mime._text_label.configure(wraplength=110)
        btn_project_mime.grid()
    def confirm_delete(self,btn_project_mime,button_text,button_color):
        result=messagebox.askyesno("Confirm","Projekt erfolgreich?")
        if result:
            success = "Y"
            btn_project_mime.destroy()
            self.delete_project(button_text)
            add_log_file(button_text,success,button_color)
        else:
            success = "N"
            btn_project_mime.destroy()
            self.delete_project(button_text)
            add_log_file(button_text,success,button_color)
    
    def delete_project(self,button_text):
        self.delete_databases_by_name(button_text)

    def delete_databases_by_name(self, button_text):
        conn = sqlite3.connect("D:\Programmtests\DB\Buttons.db")
        cur = conn.cursor()
        try:
            sql=(f"DELETE FROM BUTTONS WHERE NAMES = '{button_text}'")
            cur.execute(sql)
            print("Single button erased")
        except:
            print("None buttons left")
        conn.commit()
        conn.close()
        conn = sqlite3.connect("D:\Programmtests\DB\Materials.db")
        cur = conn.cursor()
        try:
            sql=(f"DROP TABLE {button_text}")
            cur.execute(sql)
            print("Materials erased")
        except:
            print("No Material left")
        conn.commit()
        conn.close()
        conn = sqlite3.connect("D:\Programmtests\DB\Flow.db")
        cur = conn.cursor()
        try:
            sql=(f"DROP TABLE {button_text}")
            cur.execute(sql)
            print("Flow erased")
        except:
            print("No Flow left")
        conn.commit()
        conn.close()
     
def add_btn_project(name_value,prio_color):
    Segment_Buttons(name_value,prio_color) 

def add_btn_mime(name_value,prio_color):
    Segment_Mimes(name_value,prio_color)

def add_label_mat_values(name_value,sum_value):
    add_labels_to_Frame_0(name_value,sum_value)

def add_label_flow_values(flow_value):
    add_labels_to_Frame_1(flow_value)

def add_log_file(project_name,success,prio):
    time=datetime.now()
    timestamp=time.strftime("%Y-%m-%d")
    value_list=[project_name,success,timestamp,prio]
    conn = sqlite3.connect("D:\Programmtests\DB\Log.db") 
    cur = conn.cursor()
    try: 
        sql="CREATE TABLE IF NOT EXISTS Log ("\
            "NAMES TEXT,"\
            "SUCCESS TEXT,"\
            "TIMESTAMP TEXT,"\
            "PRIO TEXT)"
        cur.execute(sql)
        sql=("INSERT INTO Log VALUES (?,?,?,?)")
        cur.execute(sql,value_list)
        conn.commit()
        conn.close()
    except:
        sql=("INSERT INTO Log VALUES (?,?,?,?)")
        cur.execute(sql,value_list)
        conn.commit()
        conn.close() 

def add_all_to_log_file(project_name,success,prio):
    time=datetime.now()
    timestamp=time.strftime("%Y-%m-%d")
    value_list=[project_name,success,timestamp,prio]
    conn = sqlite3.connect("D:\Programmtests\DB\Log.db") 
    cur = conn.cursor()
    try: 
        sql="CREATE TABLE IF NOT EXISTS Log ("\
            "NAMES TEXT,"\
            "SUCCESS TEXT,"\
            "TIMESTAMP TEXT,"\
            "PRIO TEXT)"
        cur.execute(sql)
        sql=("INSERT INTO Log VALUES (?,?,?,?)")
    except:
        sql=("INSERT INTO Log VALUES (?,?,?,?)")

    cur.execute(sql,value_list)
    conn.commit()
    

def read_database_buttons():
    try:
        conn = sqlite3.connect("D:\Programmtests\DB\Buttons.db")         #1.R DB Abfrage
        cur = conn.cursor()                                              # 
        sql="SELECT NAMES,PRIOS FROM Buttons"                            
        cur.execute(sql)                                                 #                                               #
        data = cur.fetchall()                                           
        conn.close()
        return data
    except:
        return 0
    
def read_database_materials():
    try:
        conn = sqlite3.connect("D:\Programmtests\DB\Materials.db")         
        cur = conn.cursor()                                              
        sql=f"SELECT NAMES,SUMS FROM {button_text}"                                  
        cur.execute(sql)                                                 
        data = cur.fetchall()  
        conn.close()                                          
        return data    
    except:
        return 0
    
def read_database_flow():
    try:
        conn = sqlite3.connect("D:\Programmtests\DB\Flow.db")         
        cur = conn.cursor()                                               
        sql=f"SELECT FLOW FROM {button_text}"                                  
        cur.execute(sql)                                                 
        data = cur.fetchall()
        conn.close()
        return data   
    except:
        return 0

def write_database_buttons(button_value_list):
    conn = sqlite3.connect("D:\Programmtests\DB\Buttons.db")    #W Buttons.db
    cur = conn.cursor()                                         #
    try:                                                        #wenn noch keine Table da add Table
        sql="CREATE TABLE IF NOT EXISTS Buttons ("\
            "NAMES TEXT,"\
            "PRIOS TEXT,"\
            "DESCR TEXT )"
        cur.execute(sql)
        cur.execute("INSERT INTO Buttons VALUES(?,?,?)",button_value_list)           #und füge names,prios hinzu
        conn.commit()
    except:                                                     #sonst
        print("EXCEPT")                                         #füge ohne weiteres name, prios hinzu 
        cur.execute("INSERT INTO Buttons VALUES(?,?,?)",button_value_list)
        conn.commit()

def load_saved_buttons():
    data=read_database_buttons()
    if data == 0:
        pass
    else:
        for btn_project in root_Frame_0.winfo_children():                                 #Löschen Buttons
            btn_project.destroy()
        for names,prios in data:
            add_btn_project(names,prios)     

def load_saved_labels():
    data=read_database_materials()
    if data == 0:
        pass
    else:
        for names,sums in data:
            add_label_mat_values(names,sums)                                       #3.C addlbl0
    data=read_database_flow()
    if data == 0:
        pass
    else:
        for names in data:
            names=names[0]
            add_label_flow_values(names)

def load_saved_mimes():
    data=read_database_buttons()
    if data == 0:
        pass
    else:
        for btn_project in root_Frame_0.winfo_children():                                 #Löschen Buttons
            btn_project.destroy()
        for names,prios in data:
            add_btn_mime(names,prios)

def remove_button_single():
    load_saved_mimes()

def remove_button_all():
    result=messagebox.askyesno("Confirm","Projekt erfolgreich?")
    conn = sqlite3.connect("D:\Programmtests\DB\Buttons.db")
    cur = conn.cursor()
    if result:
        success = "Y"
    else:
        success = "N"
    try: 
        sql="SELECT NAMES FROM BUTTONS"
        cur.execute(sql)
        all_buttons=[row[0]for row in cur.fetchall()]
        sql="SELECT PRIOS FROM BUTTONS"
        cur.execute(sql)
        all_prios=[row[0]for row in cur.fetchall()]
        
    except:
        print("No Buttons left")
        return
    
    for btn_project in root_Frame_0.winfo_children():                                 #Löschen Buttons
        btn_project.destroy()
    try:
        Top_0.destroy()
    except:
        print("window has been closed")
    try:
        sql = "DROP TABLE Buttons"
        cur.execute(sql)
        conn.close()
    except:
        print("Deletion error")
        conn.close()
    for button,prio in zip(all_buttons,all_prios):
        add_all_to_log_file(button,success,prio)
    conn.close()

    conn = sqlite3.connect("D:\Programmtests\DB\Materials.db")
    cur=conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables=cur.fetchall()
    for table in tables:
        table_name=table[0]
        cur.execute(f"DROP TABLE IF EXISTS {table_name};")
    conn.commit()
    conn.close()
    conn = sqlite3.connect("D:\Programmtests\DB\Flow.db")
    cur=conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables=cur.fetchall()
    for table in tables:
        table_name=table[0]
        cur.execute(f"DROP TABLE IF EXISTS {table_name};")
    conn.commit()
    conn.close()

def open_Top_0():
    global Top_0
    global Top_0_Frame_0
    global Top_0_Frame_1
    Top_0=Toplevel()
    Top_0.title(button_text)
    Top_0.geometry("700x700")
    btn_mat=ctk.CTkButton(Top_0,text="Mat Add",fg_color="#573827",hover_color="#EF9912",command=lambda:open_Top_00())
    btn_flow=ctk.CTkButton(Top_0,text="Flow Add",fg_color="#573827",hover_color="#EF9912",command=lambda:openTop_01())
    btn_calc=ctk.CTkButton(Top_0,text="Calc",fg_color="#573827",hover_color="#EF9912",command=None)
    btn_desc=ctk.CTkButton(Top_0,text="Beschreibung",fg_color="#573827",hover_color="#EF9912",command=lambda:openTop_02())
    Top_0_Frame_0=ctk.CTkFrame(Top_0,fg_color="#EF9912",height=300,border_width=5,border_color="#573827")
    Top_0_Frame_1=ctk.CTkFrame(Top_0,fg_color="#EF9912",height=300,border_width=5,border_color="#573827") 
    btn_mat.grid(row=1,column=0)
    btn_flow.grid(row=1,column=3)
    btn_calc.grid(row=3,column=0)
    btn_desc.grid(row=3,column=3)
    Top_0_Frame_0.grid(row=6,column=0)
    Top_0_Frame_1.grid(row=6,column=3)
    load_saved_labels()
    Top_0.mainloop()

def open_Top_1(choice):
    if choice == "Neues Projekt":
        load_saved_buttons()     
        
    def get_all_values():
        
        global names
        global prios
        global prio_value
        global name_value
        global prio_color
        prio_state=False
        name_state=False
        prio_value=lbl_info_1.cget("text")  
        name_value=name_var.get()
        text_value=tex_desc.get("0.0",END)                                #text nicht belegt
        if prio_value != ("Priorität wählen"):          
            prio_state = True
        else:
            prio_state=False
        if name_value != (""):
            name_state = True
        else:
            name_state=False
        if ((prio_state == True) and (name_state == True)):
            if prio_value == "hoch":
                prio_color = "red"
            elif prio_value =="normal":
                prio_color = "yellow"
            else:
                prio_color="green"    
            names = name_value
            prios = prio_color
            descr = text_value
            button_value_list = [(names),(prios),(descr)]
            write_database_buttons(button_value_list)                                                    #Call Addbtn
            add_btn_project(names,prios)
    def red():                                                          #Farbübersetzung, C über jeweiliges Lbl
        lbl_info_1.configure(text="hoch")
    def yellow():
        lbl_info_1.configure(text="normal")
    def green():
        lbl_info_1.configure(text="niedrig")

    
    if choice == "Projekte laden":
        load_saved_buttons()     
        return
    if choice == "Ein Projekt abschließen":
        print("Ein Projekt abschließen")
        remove_button_single()
        return
    if choice == "Projekte löschen":
        print("Projekte löschen")
        remove_button_all()                                                       
        return
    Top_1=Toplevel()
    lbl_info_0=ctk.CTkLabel(Top_1,text="Projektname eingeben")
    ent_name=ctk.CTkEntry(Top_1,textvariable=name_var)
    lbl_info=ctk.CTkLabel(Top_1,text="Beschreibung eingeben")
    tex_desc=ctk.CTkTextbox(Top_1,width=200,height=100)
    btn_save=ctk.CTkButton(Top_1,text="Speichern",command=get_all_values)
    btn_red=ctk.CTkButton(Top_1,text="",fg_color="red", width=20, height=40,command=red)
    btn_yellow=ctk.CTkButton(Top_1,text="",fg_color="yellow", width=20, height=40,command= yellow)
    btn_green=ctk.CTkButton(Top_1,text="",fg_color="green", width=20, height=40,command= green)
    lbl_info_1=ctk.CTkLabel(Top_1,text="Priorität wählen")
    lbl_info_0.grid(row=0,column=0)
    ent_name.grid(row=0,column=1)
    lbl_info.grid(row=1,column=0)
    tex_desc.grid(row=1,column=1)
    btn_save.grid(row=2,column=1)
    btn_red.grid(row=0,column=3)
    btn_yellow.grid(row=1,column=3)
    btn_green.grid(row=2,column=3)
    lbl_info_1.grid(row=2,column=0)
    Top_1.mainloop()


def display_data(values):
    Top_2=Toplevel()
    Top_2.columnconfigure(index=1,weight=1)
    Top_2.columnconfigure(index=2,weight=1)
    Top_2_Frame_0=ctk.CTkScrollableFrame(Top_2)
    for data in values:
        lbl=ctk.CTkLabel(Top_2_Frame_0,text=data)
        lbl.grid(column=1)
    Top_2_Frame_0.grid(column=1)   
    Top_2.mainloop()

def open_Top_2(choice):
    if choice == "Protokoll laden":
        open_log_file()     
        return
    if choice == "Protokoll löschen":
        delete_log_file()
        return
    if choice == "Daten Analysieren":
        open_data_table()

def open_Top_3(choice):
    if choice =="Pflanzenmanager":
        
        subprocess.Popen(["python","D:\Programmtests\Projekt1_sub1.py"])
        
    if choice =="Pflanzenlexikon":
        subprocess.Popen(["python","D:\Programmtests\Projekt1_sub2.py"])

def open_log_file():
    
    conn = sqlite3.connect("D:\Programmtests\DB\Log.db")
    cur=conn.cursor()
    try:
        sql=("SELECT * FROM Log")
        cur.execute(sql)
        data=cur.fetchall()
        display_data(data)
    except:
        print("Datafetch Error: Log leer")
        messagebox.showinfo("Information","Die Protokolldatei ist leer")
        return
    
def delete_log_file():
    conn = sqlite3.connect("D:\Programmtests\DB\Log.db")
    cur=conn.cursor()   
    try:
        sql=("DROP TABLE Log")
        cur.execute(sql)
        sql=("CREATE TABLE Log(NAMES TEXT,SUCCESS TEXT,TIMESTAMP TEXT);")
    except:
        print("Delete Error: Log leer")

def open_data_table():

    def show_statistics():
        try:
            fig, axs = plt.subplots(2, 2, figsize=(10, 10))
            df_sorted_alpha = df.sort_values(by='names')
            df_sorted_chrono = df.sort_values(by='timestamp')
            # Plot 1: Alphabetical sorting
            axs[0,0].plot(df_sorted_alpha['names'],df_sorted_alpha['timestamp'], marker='o', linestyle='-',color='green')
            axs[0,0].set_title('Abschluss Alphabetisch')
            axs[0,0].set_xlabel('Namen')
            axs[0,0].set_ylabel('Zeitpunkt')
            axs[0,0].tick_params(axis='x', rotation=45)
            # Plot 2: Chronological sorting
            axs[0,1].plot(df_sorted_chrono['timestamp'], df_sorted_chrono['names'], marker='o', linestyle='-')
            axs[0,1].set_title('Abschluss Chronologisch')
            axs[0,1].set_xlabel('Zeitpunkt')
            axs[0,1].set_ylabel('Anzahl Projekte')
            axs[0,1].tick_params(axis='x', rotation=45)
            # Plot 3: Individual Success sorting
            axs[1,0].plot(df_sorted_chrono['timestamp'],plotdata_prio, marker='o', linestyle='-',color='grey')
            axs[1,0].axhline(0,color='red',linestyle='--')
            axs[1,0].set_title('Einzelner Erfolg')
            axs[1,0].set_xlabel('Zeitpunkt')
            axs[1,0].set_ylabel('Erfolg')
            axs[1,0].tick_params(axis='x', rotation=45)
            # Plot 4: Cumulative Success sorting
            axs[1,1].plot(df_sorted_chrono['timestamp'], plotdata_cum, marker='o', linestyle='-',color='purple')
            axs[1,0].axhline(0,color='red',linestyle='--')
            axs[1,1].set_title('Gesamterfolg')
            axs[1,1].set_xlabel('Zeitpunkt')
            axs[1,1].set_ylabel('Erfolg')
            axs[1,1].tick_params(axis='x', rotation=45)

            # Show the plots
            plt.tight_layout()  # Adjust layout to prevent overlap
            canvas = FigureCanvasTkAgg(fig, master=Top_3)
            canvas.draw()
            canvas.get_tk_widget().grid()

        except Exception as e:
            print("An error occurred:", str(e))
            return

    conn = sqlite3.connect("D:\Programmtests\DB\Log.db")
    cur=conn.cursor()   
    cur.execute("SELECT * FROM Log")
    data=cur.fetchall()
    sum_value=len(data)
    cur.execute("SELECT * FROM Log WHERE SUCCESS ='Y' ")
    data=cur.fetchall()
    sum_success_value=len(data)

    cur.execute("SELECT TIMESTAMP FROM Log")
    plotdata_timestamp=[row[0]for row in cur.fetchall()]
    cur.execute("SELECT NAMES FROM Log")
    plotdata_names=[row[0]for row in cur.fetchall()]
    cur.execute("SELECT SUCCESS FROM Log")
    plotdata_success=[row[0]for row in cur.fetchall()]
    cur.execute("SELECT PRIO FROM Log")
    plotdata_prio=[row[0]for row in cur.fetchall()]
    plotdata_cum=[]
    cum_value=0
    for i in range(len(plotdata_prio)):
        if plotdata_prio[i]=='red':
            plotdata_prio[i]=3
            if plotdata_success[i]=='N':
                plotdata_prio[i]=-3
        if plotdata_prio[i]=='yellow':
             plotdata_prio[i]=2
             if plotdata_success[i]=='N':
                plotdata_prio[i]=-2
        if plotdata_prio[i]=='green':
            plotdata_prio[i]=1
            if plotdata_success[i]=='N':
                plotdata_prio[i]=-1
        cum_value+=plotdata_prio[i]
        plotdata_cum.append(cum_value)

    plotdata={'timestamp':plotdata_timestamp,
              'names':plotdata_names,
              'success':plotdata_success,
              'prio':plotdata_prio,
              'cumulative':plotdata_cum}
    conn.close()
    
    df=pd.DataFrame(plotdata)

    Top_3=Toplevel()
    frame=ctk.CTkFrame(Top_3,width=400,height=200)
    frame.pack_propagate(False)
    frame.grid()
    btn_eval=ctk.CTkButton(frame,text="Analyse",fg_color="blue",bg_color="grey",width=40,height=40,command=show_statistics)
    lbl_sum=ctk.CTkLabel(frame,text=f'Gesamt abgeschlossen: {sum_value}',fg_color='#FFB90F', width=125, height=40,corner_radius=8) 
    lbl_sum_success=ctk.CTkLabel(frame,text=f'Erfolgreich abgeschlossen: {sum_success_value}',fg_color="green", width=25, height=40,corner_radius=8) 
    lbl_sum_failure=ctk.CTkLabel(frame,text=f'ohne Erfolg abgeschlossen: {sum_value-sum_success_value}',fg_color="red", width=45, height=40,corner_radius=8) 
    lbl_sum.grid(row=0,column=0)
    lbl_sum_success.grid(row=1,column=0)
    lbl_sum_failure.grid(row=2,column=0)
    btn_eval.grid(row=0,column=1)
    Top_3.mainloop()


def add_labels_to_Frame_0(name_value,sum_value):
    global Top_0_Frame_0 
    lbl_name=ctk.CTkLabel(Top_0_Frame_0,text=name_value)
    lbl_sum=ctk.CTkLabel(Top_0_Frame_0,text=sum_value)
    lbl_name.grid()
    lbl_sum.grid()
    
def add_labels_to_Frame_1(flow_value):
    global Top_0_Frame_1
    lbl_flow=ctk.CTkLabel(Top_0_Frame_1,text=flow_value)
    lbl_space=ctk.CTkLabel(Top_0_Frame_1,text=None)
    lbl_flow.grid()
    lbl_space.grid()

def open_Top_00():
    Top_00=Toplevel()
    Top_00.title("Add Material")
    Top_00.geometry("440x130")
    def plus():
            p=ent_count.get()
            pInt=int(p)
            pInt+=1
            ent_count.delete(0,"end")
            ent_count.insert(0,pInt)
    def minus():
            m=ent_count.get()
            mInt=int(m)
            mInt-=1
            ent_count.delete(0,"end")
            ent_count.insert(0,mInt)
    def get_both_mat_values():
        material_names=ent_material.get()
        print(material_names)
        material_sum=(int(ent_price.get())*int(ent_count.get()))
        add_label_mat_values(material_names,material_sum)                                  #c addlbl0                           
        mat_list = [(material_names),(material_sum)]                        
        conn = sqlite3.connect("D:\Programmtests\DB\Materials.db")    #W Materials.db
        cur = conn.cursor()                                         #
        try:                                                        #wenn noch keine Table da add Table
            sql=f"CREATE TABLE IF NOT EXISTS {button_text} ("\
                "NAMES TEXT,"\
                "SUMS INTEGER )"
            cur.execute(sql)
            sql=f"INSERT INTO {button_text} VALUES(?,?)"           #und füge Names,Sum hinzu
            cur.execute(sql,mat_list)
            conn.commit()
            conn.close()
        except:                                                     #sonst
            print("EXCEPT")                                         #füge ohne weiteres Names,Sum hinzu 
            sql=f"INSERT INTO {button_text} VALUES(?,?)"
            cur.execute(sql,mat_list)
            conn.commit()
            conn.close()
    Top_00.columnconfigure(0,weight=1)
    Top_00.columnconfigure(1,weight=1)
    Top_00.columnconfigure(2,weight=1)
    Top_00.columnconfigure(3,weight=1)
    Top_00.columnconfigure(4,weight=1)
    lbl_info_0=ctk.CTkLabel(Top_00,text= "Material")
    lbl_info_1=ctk.CTkLabel(Top_00,text= "Preis")
    lbl_info_2=ctk.CTkLabel(Top_00,text= "Menge")
    ent_material= ctk.CTkEntry(Top_00,width=100)
    ent_price= ctk.CTkEntry(Top_00,width=50)
    ent_count= ctk.CTkEntry(Top_00,width=25)
    btn_plus= ctk.CTkButton(Top_00,text="+",width=50,command=lambda:plus())
    btn_minus= ctk.CTkButton(Top_00,text="-",width=20,command=lambda:minus())
    btn_add= ctk.CTkButton(Top_00,text="Hinzufügen",fg_color="#573827",hover_color="#EF9912",width=100,command=lambda:get_both_mat_values())
    lbl_info_0.grid(row=0,column=0)
    lbl_info_1.grid(row=0,column=1)
    lbl_info_2.grid(row=0,column=2)
    ent_material.grid(row=1,column=0)
    ent_price.grid(row=1,column=1)
    ent_count.grid(row=1,column=3)
    btn_plus.grid(row=1,column=2)
    btn_minus.grid(row=1,column=4)
    btn_add.grid(row=3,column=1)
    ent_count.insert(0,"0")
    Top_00.mainloop()
    
def openTop_01():
    def get_flow_value():
        flow_names=tex_flow.get("1.0",END)
        add_label_flow_values(flow_names)
        flow_list = [(flow_names)]                        
        conn = sqlite3.connect("D:\Programmtests\DB\Flow.db")    
        cur = conn.cursor()                                         
        try:                                                        
            sql=f"CREATE TABLE IF NOT EXISTS {button_text} ("\
                "FLOW TEXT )"
            cur.execute(sql)
            sql=f"INSERT INTO {button_text} VALUES(?)"           
            cur.execute(sql,flow_list)
            conn.commit()
        except:                                                  
            print("EXCEPT")                                       
            sql=f"INSERT INTO {button_text} VALUES(?)"           
            cur.execute(sql,flow_list)
            conn.commit()
        
    Top_01=Toplevel()
    Top_01.title("Prozeßablauf")
    Top_01.geometry("440x440")
    lbl_info=ctk.CTkLabel(Top_01,text= "Geben Sie hier Ihren Prozeßablauf ein")
    tex_flow=ctk.CTkTextbox(Top_01)
    btn_submit=ctk.CTkButton(Top_01,text="speichern",command=lambda:get_flow_value())
    lbl_info.grid()
    tex_flow.grid()
    btn_submit.grid()
    Top_01.mainloop()

def openTop_02():
    global button_text
    Top_02=Toplevel()
    Top_02.title("Beschreibung")
    Top_02.geometry("400x550")
    conn = sqlite3.connect("D:\Programmtests\DB\Buttons.db")
    cur=conn.cursor()
    sql=f"SELECT DESCR FROM Buttons WHERE NAMES='{button_text}'"
    cur.execute(sql)
    description=cur.fetchall()
    description=str(description[0][0])
    tex_flow_show=ctk.CTkTextbox(Top_02,width=250,height=300)
    tex_flow_show.insert(END,description)
    tex_flow_show.grid()
    Top_02.mainloop()

root.geometry("600x600")
name_var=tk.StringVar()
menu_options_0=ctk.CTkOptionMenu(root,values=["Projekte laden","Neues Projekt","Ein Projekt abschließen","Projekte löschen"],fg_color=["grey","red"],button_color="#573827",button_hover_color="#EF9912",text_color="white",corner_radius=0,width=200,command=open_Top_1)
menu_options_0.set("Projekt")
menu_options_0.grid(row=0,column=0,sticky="N")
menu_options_1=ctk.CTkOptionMenu(root,values=["Protokoll laden","Daten Analysieren","Protokoll löschen"],fg_color=["grey","red"],button_color="#573827",button_hover_color="#EF9912",text_color="white",corner_radius=0,width=200,command=open_Top_2)
menu_options_1.set("Daten")
menu_options_1.grid(row=0,column=2,sticky="N")
menu_options_2=ctk.CTkOptionMenu(root,values=["Pflanzenmanager","Pflanzenlexikon"],fg_color=["grey","red"],button_color="#573827",button_hover_color="#EF9912",text_color="white",corner_radius=0,width=200,command=open_Top_3)
menu_options_2.set("Pflanzen")
menu_options_2.grid(row=0,column=4,sticky="N")


root_Frame_0.grid()

root.mainloop()