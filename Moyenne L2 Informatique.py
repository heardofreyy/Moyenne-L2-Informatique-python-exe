import customtkinter 

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("1200x620")


def mo():

    #------------------ get entry to var --------------------------

    global asdmo_entr
    asdmo= float(asdmo_entr.get())

    global aomo_entr
    aomo= float(aomo_entr.get())

    global simo_entr
    simo= float(simo_entr.get())

    global thgmo_entr
    thgmo= float(thgmo_entr.get())

    global lmmo_entr
    lmmo= float(lmmo_entr.get())

    global mnmo_entr
    mnmo= float(mnmo_entr.get())

    global angmo_entr
    angmo= float(angmo_entr.get())

    #------------------ co's --------------------------

    asdco = 3
    aoco = 3
    sico = 3 
    thgco = 2
    lmco = 2
    mnco = 2
    angco = 1 

    #------------------ co's X mo's --------------------------

    asdmco = float(asdco * asdmo)
    aomco = float(aoco * aomo)
    simco =  float(sico * simo)
    thgmco = float(thgco * thgmo)
    lmmco = float(lmco * lmmo)
    mnmco = float(mnco * mnmo)
    angmco = float(angco * angmo)

    #------------------ all co's --------------------------

    allco = float(asdco + aoco + sico + thgco + lmco + mnco + angco)

    #------------------ all mo's --------------------------

    allmo = float(asdmco + aomco + simco + thgmco + lmmco + mnmco + angmco)
    print(allmo)
    #------------------ calcul mo --------------------------
    
    mo = allmo/allco

    #------------------ print mo --------------------------

    mo_lbl.configure(text=f"Votre moyenne generale = {mo}")

    #------------------ print all mo's --------------------------

    allmo_lbl.configure(text=f"Votre totale = {allmo}")

    
frame_top = customtkinter.CTkFrame(master=root, height=70)
frame_top.pack(pady=5, padx=10, fill="both", side="top")

frame_left = customtkinter.CTkFrame(master=root, width=500)
frame_left.pack(pady=10, padx=10, fill="both", expand=True, side="left")

frame_right = customtkinter.CTkFrame(master=root, width=500)
frame_right.pack(pady=10, padx=10, fill="both", expand=True, side="left")

#-----------------------------------------------MO Title----------------------------------------------------------------------------------

label = customtkinter.CTkLabel(master=frame_top, text="Moyenne L2 Informatique", width=400, height=50, font=("Roboto", 22, "bold"))
label.pack(pady=12, padx=10)

#-----------------------------------------------MO Entry----------------------------------------------------------------------------------

asdmo_entr = customtkinter.CTkEntry(master=frame_left, placeholder_text="ASD3", width=400, height=50, corner_radius=10, font=("Roboto", 18))
asdmo_entr.pack(pady=10, padx=5)

aomo_entr = customtkinter.CTkEntry(master=frame_left, placeholder_text="AO", width=400, height=50, corner_radius=10, font=("Roboto", 18))
aomo_entr.pack(pady=10, padx=5)

simo_entr = customtkinter.CTkEntry(master=frame_left, placeholder_text="SI", width=400, height=50, corner_radius=10, font=("Roboto", 18))
simo_entr.pack(pady=10, padx=5)

thgmo_entr = customtkinter.CTkEntry(master=frame_left, placeholder_text="THG", width=400, height=50, corner_radius=10, font=("Roboto", 18))
thgmo_entr.pack(pady=10, padx=5)

lmmo_entr = customtkinter.CTkEntry(master=frame_left, placeholder_text="LM", width=400, height=50, corner_radius=10, font=("Roboto", 18))
lmmo_entr.pack(pady=10, padx=5)

mnmo_entr = customtkinter.CTkEntry(master=frame_left, placeholder_text="MN", width=400, height=50, corner_radius=10, font=("Roboto", 18))
mnmo_entr.pack(pady=10, padx=5)

angmo_entr = customtkinter.CTkEntry(master=frame_left, placeholder_text="ANG2", width=400, height=50, corner_radius=10, font=("Roboto", 18))
angmo_entr.pack(pady=10, padx=5)

#----------------------------------------------- Warning ----------------------------------------------------------------------------------

label_wanr = customtkinter.CTkLabel(master=frame_right, width=400, height=150, text='- Entrez les moyennes des modules à gauche en chiffres!!!\n- N\'ajoutez pas d\'autres caractères ou espaces!!!\n- Clickez a la bouton "Calculer" pour avoir votre moyenne. \n- Votre moyenne generale et le totale seront sur le bas.', justify="left", fg_color=("grey12"),corner_radius=10, font=("Roboto", 20, "bold"),  text_color=('white'))
label_wanr.pack(pady=12, padx=10)
#----------------------------------------------- submit btn ----------------------------------------------------------------------------------

button = customtkinter.CTkButton(master=frame_right, text="Calculer", width= 200, height=60, font=("Roboto", 22), command=mo)
button.pack(pady=50, padx=50)

#-----------------------------------------------MO Label ----------------------------------------------------------------------------------

allmo_lbl = customtkinter.CTkLabel(master=frame_right, text="", width=400, height=50, corner_radius=8, fg_color=("white", "gray75"), text_color=('black'), font=("arial", 22))
allmo_lbl.pack(pady=12, padx=10)

mo_lbl = customtkinter.CTkLabel(master=frame_right, text="", width=400, height=50, corner_radius=8, fg_color=("white", "gray75"), text_color=('black'), font=("arial", 22))
mo_lbl.pack(pady=12, padx=10)

#----------------------------------------------- end ----------------------------------------------------------------------------------

root.mainloop()