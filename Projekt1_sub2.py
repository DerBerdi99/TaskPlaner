import customtkinter as ctk
import sqlite3
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageTk
import os

colors = ["#000000", "#0B6623", "#4A5D23", "#18392B","#232023","#B0F338","#231709","#3B1E08","#4A2511","#3C280D","#801818","#151E3D","#0A1172","#F4C430","#371F76","#FFFFFF"]


thick=6
slim=3

def drawIt():
    
    global Top_7,Frame0, Frame1, Frame2, canvas, selected_color, width, paintit, ResultImage, colors, BtnWidth
    global Ent1, Ent2, Ent3, Ent4, Ent5, Ent6
    def draw(event):
        global width
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        canvas.create_oval(x1, y1, x2, y2, fill=selected_color, outline=selected_color, width=width)
        paintit.ellipse([x1, y1, x2, y2], fill=selected_color,width=width)

    def save_plant():
        
        #save_plant
        # Get the plant name from the entry field
        plant_name = Ent1.get()
        plant_latin=Ent2.get()
        plant_family=Ent3.get()
        plant_lifecycle=Ent4.get()
        plant_bloom=Ent5.get()
        plant_usage=Ent6.get()
        value_list=[plant_name,plant_latin,plant_family,plant_lifecycle,plant_bloom,plant_usage]
        # Check if the plant name is not empty
        if plant_name.strip() != "":
            try:
                # Connect to the database
                conn = sqlite3.connect("D:\Programmtests\DB\Beet.db")
                cursor = conn.cursor()
                # Insert the plant name into the database
                sql=("INSERT INTO Pflanzen VALUES (?,?,?,?,?,?)")
                cursor.execute(sql,value_list)
                conn.commit()
                conn.close()
                # Close the window
                Top_7.destroy()
                # Show a success message
                messagebox.showinfo("Gut", "Werte übernommen!")
            except Exception as e:
                messagebox.showerror("Error", f"Error occurred: {str(e)}")
        else:
            messagebox.showwarning("Warnung", "Nur Pflanzennamen!")
        #save as png (#Verzeichnis fehlt)
        
        filename = f"{plant_name}.png"
        ResultImage.save(f'D:\Programmtests\Img\Widgets\{filename}')
        print(f"Drawing saved as {filename}")

    
    Top_70.title("Zeichne deine Pflanze!")
    Top_70.wm_attributes("-topmost",True)
    selected_color = colors[0]
    create_color_buttons()
    BtnSave = ctk.CTkButton(Top_70,fg_color='#FFB90F',text_color='black',text="Save as PNG", command=save_plant)
    BtnSave.grid()
    BtnReset = ctk.CTkButton(Top_70, fg_color='#FFB90F',text_color='black',text="Reset", command=reset)
    BtnReset.grid()
    BtnWidth = ctk.CTkButton(Top_70, fg_color='#FFB90F',text_color='black',text=f"Width = {width}", command=swap_width)
    BtnWidth.grid()
    ResultImage = Image.new("RGB", (120, 120), "white")
    canvas.bind("<B1-Motion>", draw)
    canvas.grid()
    paintit = ImageDraw.Draw(ResultImage)
    ###Buttons Name, Familie, ... auf Frame2###
    Lbl1 = ctk.CTkLabel(Frame2, text="Bezeichnung:")
    Ent1 = ctk.CTkEntry(Frame2)
    Lbl2 = ctk.CTkLabel(Frame2, text="Lateinname:")
    Ent2 = ctk.CTkEntry(Frame2)
    Lbl3 = ctk.CTkLabel(Frame2, text="Familie:")
    Ent3 = ctk.CTkEntry(Frame2)
    Lbl4 = ctk.CTkLabel(Frame2, text="Lebenszyklus:")
    Ent4 = ctk.CTkEntry(Frame2)
    Lbl5 = ctk.CTkLabel(Frame2, text="Blütezeit:")
    Ent5 = ctk.CTkEntry(Frame2)
    Lbl6 = ctk.CTkLabel(Frame2, text="Verwendung:")
    Ent6 = ctk.CTkEntry(Frame2)
    Lbl1.grid()
    Ent1.grid()
    Lbl2.grid()
    Ent2.grid()
    Lbl3.grid()
    Ent3.grid()
    Lbl4.grid()
    Ent4.grid()
    Lbl5.grid()
    Ent5.grid()
    Lbl6.grid()
    Ent6.grid()
    Top_70.protocol("WM_DELETE_WINDOW",onclose)
    Top_70.mainloop()  

def onclose(event=None):
    if Top_7.winfo_exists():
        Top_7.destroy()

def create_color_buttons():
    global colors
    color_count=len(colors)
    num_rows=int(color_count**0.5)
    num_columns=(color_count + num_rows -1)// num_rows

    for i, color in enumerate(colors):
        row=i//num_rows
        column=i%num_columns
        btn = ctk.CTkButton(Frame0, fg_color=color, width=2, text=' ',corner_radius=30,command=lambda c=color:set_color(c))
        btn.grid(row=row,column=column)

def set_color(color):
    global selected_color
    selected_color = color
    
def reset():
    global canvas, ResultImage, paintit
    canvas.delete("all")
    ResultImage = Image.new("RGB", (120, 120), "white")
    paintit = ImageDraw.Draw(ResultImage)

def swap_width():
    global slim, width
    if width == thick:
        width = slim
    else: 
        width = thick

    BtnWidth.configure(text=f"Dicke = {width}")

def update_option_list():
    conn = sqlite3.connect("D:\Programmtests\DB\Beet.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Name FROM Pflanzen")
    plant_names = [row[0] for row in cursor.fetchall()]
    print(plant_names)
    plant_dict={}
    
    for name in plant_names:
        first_letter = name[0].upper()
        if first_letter in plant_dict:
            plant_dict[first_letter].append(name)
        else:
            plant_dict[first_letter]=[name]
    print(plant_dict)
    for first_letter, plant_names in plant_dict.items():
        value_list=[]
        optionmenu_name=f"option_menu_{first_letter}"
        optionmenu=globals().get(optionmenu_name)
        for plant_name in plant_names:
            value_list.append(plant_name)
            optionmenu.configure(values=value_list)
    conn.close()

def open_plant(choice):
    print(choice)
    Top_60=ctk.CTkToplevel(Top_7)
    
    plant_image=ImageTk.PhotoImage(Image.open(f'D:\Programmtests\Img\Widgets\{choice}.png').resize((150,150)))
    Frame3=ctk.CTkFrame(Top_60)
    LblImage=ctk.CTkLabel(Frame3, text="",image=plant_image,height=100,width=100)
    
    conn = sqlite3.connect("D:\Programmtests\DB\Beet.db")
    cursor = conn.cursor()
    sql=f"SELECT * FROM Pflanzen WHERE Name = ?"
    row=cursor.execute(sql,(choice,))
    row=row.fetchone()
    LblName=ctk.CTkLabel(Top_60,text=row[0])
    LblLatin=ctk.CTkLabel(Top_60,text=row[1])
    LblFamily=ctk.CTkLabel(Top_60,text=row[2])
    LblCycle=ctk.CTkLabel(Top_60,text=row[3])
    LblBloom=ctk.CTkLabel(Top_60,text=row[4])
    LblUsage=ctk.CTkLabel(Top_60,text=row[5])
    Frame3.grid()
    LblImage.grid()
    LblName.grid()
    LblLatin.grid()
    LblFamily.grid()
    LblCycle.grid()
    LblBloom.grid()
    LblUsage.grid()
    Top_60.wm_attributes("-topmost",True)
    Top_60.mainloop()

def remove_plant():
    global EntRemove
    plant_name=EntRemove.get()
    path="D:\Programmtests\Img\Widgets"
    try:
        file_path=os.path.join(path,plant_name + '.png')
        if os.path.exists(file_path):
            os.remove(file_path)
            print("DeletedImage")
        else:
            print("FileNotFound")
    except Exception as e:
        print(f"Error: {e}")
    conn = sqlite3.connect("D:\Programmtests\DB\Beet.db")
    cursor = conn.cursor()
    try:
        sql=f"DELETE FROM Pflanzen WHERE Name = ?"
        cursor.execute(sql,(plant_name, ))
    except Exception as e:
        print(f"Error: {e}")

    conn.commit()
    conn.close()


width = thick
Top_7 = ctk.CTk()
Top_70 = ctk.CTkToplevel(Top_7)
Frame0=ctk.CTkFrame(master=Top_70)
Frame1=ctk.CTkFrame(master=Top_70)
Frame2=ctk.CTkFrame(master=Top_70)
Frame0.grid()
Frame1.grid()
Frame2.grid()
canvas = ctk.CTkCanvas(Frame1, width=120, height=120, background="white")
# Create Frames
Top_50 = ctk.CTkFrame(Top_7, fg_color="#000000", height=100, width=100)
Top_51 = ctk.CTkFrame(Top_7, fg_color="#000000", height=100, width=100)

global EntRemove
# Create Button to open the window for adding a new plant
add_plant_button = ctk.CTkButton(Top_50, text="Pflanze hinzufügen", command=drawIt)
EntRemove= ctk.CTkEntry(Top_50,placeholder_text="Pflanze löschen")
rem_plant_button = ctk.CTkButton(Top_50, text="Pflanze löschen", command=remove_plant)
option_menu_A = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_A.set("A")
option_menu_B = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_B.set("B")
option_menu_C = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_C.set("C")
option_menu_D = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_D.set("D")
option_menu_E = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_E.set("E")
option_menu_F = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_F.set("F")
option_menu_G = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_G.set("G")
option_menu_H = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_H.set("H")
option_menu_I = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_I.set("I")
option_menu_J = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_J.set("J")
option_menu_K = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_K.set("K")
option_menu_L = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_L.set("L")
option_menu_M = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_M.set("M")
option_menu_N = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_N.set("N")
option_menu_O = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_O.set("O")
option_menu_P = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_P.set("P")
option_menu_Q = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_Q.set("Q")
option_menu_R = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_R.set("R")
option_menu_S = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_S.set("S")
option_menu_T = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_T.set("T")
option_menu_U = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_U.set("U")
option_menu_V = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_V.set("V")
option_menu_W = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_W.set("W")
option_menu_X = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_X.set("X")
option_menu_Y = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_Y.set("Y")
option_menu_Z = ctk.CTkOptionMenu(Top_51,values=[],command=open_plant)
option_menu_Z.set("Z")
add_plant_button.grid()
rem_plant_button.grid()
EntRemove.grid()
option_menu_A.grid(row=0,column=0)
option_menu_B.grid(row=0,column=1)
option_menu_C.grid(row=0,column=2)
option_menu_D.grid(row=0,column=3)
option_menu_E.grid(row=0,column=4)
option_menu_F.grid(row=1,column=0)
option_menu_G.grid(row=1,column=1)
option_menu_H.grid(row=1,column=2)
option_menu_I.grid(row=1,column=3)
option_menu_J.grid(row=1,column=4)
option_menu_K.grid(row=2,column=0)
option_menu_L.grid(row=2,column=1)
option_menu_M.grid(row=2,column=2)
option_menu_N.grid(row=2,column=3)
option_menu_O.grid(row=2,column=4)
option_menu_P.grid(row=3,column=0)
option_menu_Q.grid(row=3,column=1)
option_menu_R.grid(row=3,column=2)
option_menu_S.grid(row=3,column=3)
option_menu_T.grid(row=3,column=4)
option_menu_U.grid(row=4,column=0)
option_menu_V.grid(row=4,column=1)
option_menu_W.grid(row=4,column=2)
option_menu_X.grid(row=4,column=3)
option_menu_Y.grid(row=4,column=4)
option_menu_Z.grid(row=5,column=0)

# Grid Frames
Top_50.grid(padx=20, pady=20)
Top_51.grid()

update_option_list()

Top_7.mainloop()