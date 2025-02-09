import tkinter as tk
from tkinter import *
from customtkinter import *
import webbrowser
import customtkinter as customtkinter
from tkinter.messagebox import askokcancel, showerror, showinfo, askyesnocancel, askyesno
from tkinter.simpledialog import askstring
from PIL import Image, ImageTk
import csv
from tkcalendar import *
from ttkthemes import ThemedStyle
from tkinter import ttk
import os
from tkinter import font
from datetime import datetime, timedelta

class sign_up:
    def __init__(self, master_):
        self.master_ = master_
        self.master_.title("SIGN UP")
        self.master_.geometry("870x700+300+30")
        self.master_.resizable(width=tk.FALSE, height=tk.FALSE)
        self.master_.config(bg='#222328')
        self.background_image2 = Image.open("background register.jpg")
        self.background_photo2 = ImageTk.PhotoImage(self.background_image2)
        self.bg2 = Label(self.master_, image=self.background_photo2)
        self.bg2.pack()

        def _on_closing():
            self.master_.destroy()
            top.deiconify()
        self.master_.protocol("WM_DELETE_WINDOW", _on_closing)

        self.nama_entry = Entry(self.master_, relief='flat', bg="#aaaaaa", fg="black", font=("consolas", 11), width=35)
        self.nama_entry.place(x=50, y=170, height=40)

        self.username_entry = Entry(self.master_, relief='flat', bg="#aaaaaa", fg="black", font=("consolas", 11), width=35)
        self.username_entry.place(x=50, y=240, height=40)

        self.password_entry = Entry(self.master_, show='*', relief=tk.FLAT, bg="#aaaaaa", fg="#f8fbfd",font=("consolas", 11), width=35)
        self.password_entry.place(x=50, y=310, height=40)

        self.password_entry_confirm = Entry(self.master_, show='*', relief=tk.FLAT, bg="#aaaaaa", fg="#f8fbfd",font=("consolas", 11), width=35)
        self.password_entry_confirm.place(x=50, y=390, height=40)

        self.dob_entry = DateEntry(self.master_, relief='flat',font=("consolas", 11), width=30, date_pattern='dd/mm/yyyy', showweeknumbers=True,
                                    selectbackground='#2196F3', selectforeground='white',
                                    normalbackground='white', normalforeground='black',
                                    weekendbackground='lightblue', weekendforeground='black',
                                    headersbackground='#2196F3', headersforeground='white',
                                    sundaybackground='red', sundayforeground='white')
        self.dob_entry.place(x=50, y=470, height=40)

        self.button = Button(self.master_,bg="blue", cursor="hand2", width=30, height=2, fg="white", text="Sign Up",borderwidth=0, relief="flat", bd=0, font=("consolas", 9, 'bold'), command=self.sign_up_)
        self.button.place(x=90, y=600)

        checkpassword = Button(master_, text="👁️",relief='flat', cursor="hand2", bg="white", bd=0,activebackground="white", command=lambda: show_pass())
        checkpassword.place(x=340, y=310, width=30,height=30)

        self.gender=StringVar()
        self.gender_button=Radiobutton(master_, text="Female", value="Female",variable=self.gender)
        self.gender_button.place(x=90, y=530)
        self.gender_button_=Radiobutton(master_, text="Male", value="Male", variable=self.gender)
        self.gender_button_.place(x=90, y=570)

        def show_pass():
            if self.password_entry.cget("show") == "":
                self.password_entry.config(show="*")
            else:
                self.password_entry.config(show="")

    def sign_up_(self):
        nama = self.nama_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        dob = self.dob_entry.get_date()
        gender= self.gender.get()

        if nama and username and password and dob and gender:
            if 6 <= len(username) <= 20 and 6 <= len(password) <= 20:
                if  any(c.islower() for c in password) \
                    and any(c.isupper() for c in password)\
                    and any(c.isdigit() for c in password)\
                    and any(cq.islower() for cq in username) \
                    and any(cq.isupper() for cq in username):
                    if  any(c1.islower() for c1 in nama) \
                        and any(c1.isupper() for c1 in nama)\
                        and not any(c1.isdigit() for c1 in nama):                     
                        data = {'Nama': nama, 'Username': username, 'Password': password, 'DateOfBirth': dob, "Gender": gender, "Pesan":"no"}
                        if self.password_entry.get() == self.password_entry_confirm.get():
                            try:
                                with open('datapengguna.csv', 'r') as file:
                                    reader = csv.DictReader(file)
                                    existing_data = list(reader)
                            except FileNotFoundError:
                                existing_data = []                  
                            existing_data.append(data)
                            try:
                                with open('datapengguna.csv', 'r') as file:
                                    reader = csv.DictReader(file)
                                    for row in reader:
                                        if row['Username']==username and row['Password']==password:
                                            showerror("Error","Account already exist")
                                            return
                                        elif not row['Username']==username and not row['Password']==password:
                                            continue
                                    else:
                                            with open('datapengguna.csv', 'w', newline='') as file:
                                                kolom = ['Nama', 'Username', 'Password', 'DateOfBirth', "Gender", "Pesan", "TanggalPesan"]
                                                writer = csv.DictWriter(file, fieldnames=kolom)
                                                writer.writeheader()
                                                writer.writerows(existing_data)
                                                showinfo("Success", "Account created successfully!")
                                                self.master_.destroy()
                                                top.deiconify()
                            except FileNotFoundError:
                                with open('datapengguna.csv', 'w', newline='') as file:
                                    kolom = ['Nama', 'Username', 'Password', 'DateOfBirth', "Gender", "Pesan", "TanggalPesan"]
                                    writer = csv.DictWriter(file, fieldnames=kolom)
                                    writer.writeheader()
                                    writer.writerows(existing_data)                          

                        else:
                            showerror("Error", "Password not valid")
                    else:
                        showerror("Error","Name must only consist of uppercase letters and lowercase letters")        
                else:
                    showerror("Error","Password must consist of uppercase letters, lowercase letters, numbers and username must consist of uppercase letters dan lowercase letters ")
            else:
                showerror("Error", "Username must be at least 4 characters, and password must be between 6 and 20 characters.")
        else:
            showerror("Error", "All fields must be filled!")
            
class Dashboard():
    def __init__(self, _master_):

        self._master_=_master_
        self._master_.state("zoomed")
        self._master_.title("Yohan Kos")
        # self._master_.resizable(width=tk.FALSE, height=tk.FALSE)
        self.screen_width = self._master_.winfo_screenwidth()
        self.screen_height = self._master_.winfo_screenheight()
        self.screen_width2 = int(self.screen_width*3/4)
        self.screen_height2 =int( self.screen_height*3/4)

        self.menu_bar = Menu(_master_)
        _master_.config(menu=self.menu_bar)

        menu_file = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Home", command=self.home)
        self.menu_bar.add_cascade(label="Boarding List", command=self.filterr)
        self.menu_bar.add_cascade(label="About Yohan Kos", command=self.aboutyohankos)
        self.menu_bar.add_cascade(label="User Profil", command=self.userprofil)
        menu_file.add_separator()

        self.current_slide = 1
        self.home()
    def userprofil(self):
        try:
            self.filter_framee.destroy()
        except:
            pass
        try:
            self.boarding_listt.destroy()
        except:
            pass
        try:
            self.label_background.destroy()
        except:
            pass
        try:
            self.bglabel.destroy()
        except:
            pass
        try:
            self.label_backgroundt.destroy()
        except:
            pass
        self.menu_bar.entryconfigure("Home", state="active")
        self.menu_bar.entryconfigure("About Yohan Kos", state="active")
        self.menu_bar.entryconfigure("Boarding List", state="active")
        self.menu_bar.entryconfigure("User Profil", state="disabled")
        with open ("datapengguna.csv","r") as fili:
            data_user=csv.DictReader(fili)
            data_user=list(data_user)
            for row in data_user:
                Namaa=row["Nama"]
                Usernamee=row["Username"]
                Passwordd=row["Password"]
                if usernameeee==row["Username"]:
                     
                    self.userbg=Image.open("kamar-serba-biru2.png")
                    self.userbg=self.userbg.resize((self.screen_width,self.screen_height))
                    self.photouserbg=ImageTk.PhotoImage(self.userbg)
                    self.labelphotouserbg=Label(self._master_,image=self.photouserbg)
                    self.labelphotouserbg.place(x=0,y=0)

                    self.topanframe=Frame(self.labelphotouserbg,bg="#FFEFE8")
                    self.topanframe.place(relx=0.30,rely=0.15,relwidth=0.40,relheight=0.70)


                    self.button_submit = CTkButton(self.topanframe, text="Submit", command=lambda: simpan(), bg_color="#FFEFE8", corner_radius=70)
                    self.button_submit.place(x=370, y=460)                    

                    def cret_label_entry(label_text, velyuawal, yposition):
                        label = Label(self.topanframe, text=label_text, font=("Consolas", 11) ,bg="#FFEFE8")
                        label.place(x=48, y=yposition)

                        entrywiget = Entry(self.topanframe, width=30, fg='black', bd=0, bg='white', font=('consolas', 11))
                        entrywiget.place(x=48, y=yposition + 30, height=30)
                        entrywiget.insert(0, velyuawal)
                        entrywiget.bind('<FocusIn>', lambda eg: on_enter(eg, entrywiget, velyuawal))
                        entrywiget.bind('<FocusOut>', lambda eg: on_leave(eg, entrywiget, velyuawal))
                        return entrywiget
                    
                    def cret_pw_entry(label_text, velyuawal, yposition):
                        label = Label(self.topanframe, text=label_text, font=("Consolas", 11), bg="#FFEFE8")
                        label.place(x=48, y=yposition)

                        entrywiget = Entry(self.topanframe,show="*", width=30, fg='black', bd=0, bg='white', font=('consolas', 11))
                        entrywiget.place(x=48, y=yposition + 30, height=30)
                        entrywiget.insert(0, velyuawal)
                        entrywiget.bind('<FocusIn>', lambda eg: on_enter(eg, entrywiget, velyuawal))
                        entrywiget.bind('<FocusOut>', lambda eg: on_leave(eg, entrywiget, velyuawal))

                        bglabelcheck=Label(self.topanframe, bg="#FFEFE8",width=15,text="SHOW PASSWORD", font=("consolas", 8, "bold" ))
                        bglabelcheck.place(x=63, y=315)
                        checkpassword = Checkbutton(self.topanframe, width=0, height=0, cursor="hand2", bg="#FFEFE8",relief="flat", bd=0, selectcolor='lightgrey', command=lambda: show_pass())
                        checkpassword.place(x=48, y=315)

                        def show_pass():
                            if entrywiget.cget("show") == "":
                                entrywiget.config(show="*")
                            else:
                                entrywiget.config(show="")
                        return entrywiget
                    
                    gnti_nama=cret_label_entry("Nama", Namaa, 50)
                    gnti_username=cret_label_entry("Username",Usernamee, 140)
                    gnti_pw=cret_pw_entry("Password",Passwordd, 250)        
                    
                    def on_enter(eg, entrywiget, teksawal):
                        entrywiget.delete(0, "end")

                    def on_leave(eg, entrywiget, teksawal):
                        if entrywiget.get() == '':
                            entrywiget.insert(0, teksawal)

                    def simpan():
                        nonlocal gnti_nama
                        nama_baru = gnti_nama.get()
                        usn_baru = gnti_username.get()
                        pw_baru = gnti_pw.get()

                        if nama_baru!="" and usn_baru!="" and pw_baru!="":
                            if 6 <= len(usn_baru) <= 20 and 6 <= len(pw_baru) <= 20:
                                if  any(c.islower() for c in pw_baru) \
                                    and any(c.isupper() for c in pw_baru)\
                                    and any(c.isdigit() for c in pw_baru)\
                                    and any(cq.islower() for cq in usn_baru) \
                                    and any(cq.isupper() for cq in usn_baru):
                                    if  any(c1.islower() for c1 in nama_baru) \
                                        and any(c1.isupper() for c1 in nama_baru)\
                                        and not any(c1.isdigit() for c1 in nama_baru):                     
                                        
                                                with open('datapengguna.csv', 'r') as file:
                                                    reader = csv.DictReader(file)
                                                    reader=list(reader)
                                                    for row in reader:
                                                        if row["Username"]==username:
                                                            break
                                                        if row["Username"]==usn_baru:
                                                            showerror("Error","Tolong masukkan nama kos yang berbeda")
                                                            return
                                                    else:
                                                            with open('datapengguna.csv', 'w', newline='') as file:
                                                                kolom = ['Nama', 'Username', 'Password', 'DateOfBirth', "Gender", "Pesan", "TanggalPesan"]
                                                                writer = csv.DictWriter(file, fieldnames=kolom)
                                                                writer.writeheader()
                                                                writer.writerows(reader)
                                                                showinfo("Success", "Account berhasil diupdate")                                                   
                                    else:
                                        showerror("Error","Name must only consist of uppercase letters and lowercase letters")        
                                else:
                                    showerror("Error","Password must consist of uppercase letters, lowercase letters, numbers and username must consist of uppercase letters dan lowercase letters ")
                            else:
                                showerror("Error", "Username must be at least 4 characters, and password must be between 6 and 20 characters.")
                        else:
                            showerror("Error", "All fields must be filled!")
    def send_(self):
        # try:
            global order_button
            global underline_canvas
            with open('datapengguna.csv', "r", newline='') as file:
                data_boarding = csv.DictReader(file)
                data_boarding=list(data_boarding)
                for row in data_boarding:
                    if row["Username"]==username:
                        currenday=datetime.now()
                        lastorder = datetime.strptime(row["TanggalPesan"], "%Y-%m-%d")

                        if (currenday - lastorder).days < 20:
                            order_button.config(state="disabled")
                            order_button.config(text="Order Sent")
                            infobutton=CTkButton(pop_up, text="i", command=lambda: infobutonn(), bg_color="white", fg_color="blue",corner_radius=180
                                                    , border_width=0, border_color="white",width=17,height=17)
                            infobutton.place(x=765, y=605)
                            underline_canvas.destroy()
                            def infobutonn():
                                    showinfo("Info","You can order after 20 days")
                            showinfo("Order Sent", "Order has been sent successfully!")
                        elif (currenday- lastorder).days > 20:
                                order_button = tk.Button(pop_up, text="Order", command=self.konfirmasi_order, bg="white", fg="black",
                                activebackground="white",activeforeground="blue", relief="flat", bd=0, border=0,justify=LEFT)
                                order_button.place(x=700, y=600, width=60,height=30)
                                underline_canvas = Canvas(pop_up, height=1, width=order_button.winfo_reqwidth(), bg="black",highlightthickness=0)
                                underline_canvas.place(x=713, y=600 + order_button.winfo_reqheight())
                                underline_canvas.create_line(0, 0, 0, 0, width=2, fill="black")
            
            
        # except Exception as e:
        #     print("Error:", str(e))
            
            # showerror("Error", "Failed to send order. Please try again.")


    def konfirmasi_order(self):
        konfirmasi = askyesno("Confirmation", "Are you sure you want to place the order?")
        if konfirmasi:
            konfirmasi = askyesno("Confirmation", "Saya ingatkan sekali lagi jika anda menekan tombol ok order button akan disable selama 20 hari")
            if konfirmasi:
                konfirmasi = askyesno("Confirmation", "Anda yakin?")
                if konfirmasi:
                        with open('datapengguna.csv', "r", newline='') as file:
                            data_boarding = csv.DictReader(file)
                            data_boarding=list(data_boarding)
                            for row in data_boarding:
                                if row["Username"]==username:
                                        row["Pesan"]='yes'
                                        row["TanggalPesan"]=datetime.now()
                                        row["TanggalPesan"]=row["TanggalPesan"].date()
                                        break
                                else:
                                    continue
                        with open('datapengguna.csv', 'w', newline='') as file:
                            fieldnames = ['Nama', 'Username', 'Password', 'DateOfBirth', "Gender", "Pesan", "TanggalPesan"]
                            writer = csv.DictWriter(file, fieldnames=fieldnames)
                            writer.writeheader()
                            writer.writerows(data_boarding)
                        self.send_()
            
    def home(self):
        try:
            self.filter_framee.destroy()
        except:
            pass
        try:
            self.boarding_listt.destroy()
        except:
            pass
        try:
            self.label_background.destroy()
        except:
            pass
        try:
            self.bglabel.destroy()
        except:
            pass
        try:
            self.labelphotouserbg.destroy()
        except:
            pass
        self.menu_bar.entryconfigure("Home", state="disabled")
        self.menu_bar.entryconfigure("About Yohan Kos", state="active")
        self.menu_bar.entryconfigure("Boarding List", state="active")
        self.menu_bar.entryconfigure("User Profil", state="active")

        self.label_backgroundt = Frame(self._master_)
        self.label_backgroundt.pack(fill=BOTH, expand=YES)

        self.image_path="C:\\Users\\ANDRO\\OneDrive\\Pictures\\PROJEK SEM 1\\beritagui\\home1.png"
        image = Image.open(self.image_path)
        image = image.resize((self.screen_width, self.screen_height))  
        self.photto = ImageTk.PhotoImage(image)
 
        self.image_label = Label(self.label_backgroundt, image=self.photto)
        self.image_label.image = self.photto 
        self.image_label.pack(fill=BOTH, expand=YES)

        next_slide_button = Button(self.label_backgroundt, text=">", command=self.next_slide, relief="flat", bd=0, font=("consolas",16,"bold"))
        next_slide_button.place(x=self.screen_width-30,y=0, width=30,relheight=1)

        next_slide_button2 = Button(self.label_backgroundt, text="<", command=self.next_slide2, relief="flat", bd=0, font=("consolas",16,"bold"))
        next_slide_button2.place(x=0,y=0,width=30,relheight=1)



    def next_slide(self):

        if self.current_slide == 1:
            image_path = self.read_content_and_image("C:\\Users\\ANDRO\\OneDrive\\Pictures\\PROJEK SEM 1\\beritagui\\home2.png")
        elif self.current_slide == 2:
            image_path = self.read_content_and_image("C:\\Users\\ANDRO\\OneDrive\\Pictures\PROJEK SEM 1\\beritagui\\home3.png")
        else:
            self.current_slide=0
            image_path = self.read_content_and_image("C:\\Users\\ANDRO\\OneDrive\\Pictures\\PROJEK SEM 1\\beritagui\\home1.png")

        self.image_path=image_path
        self.image_label.config(image=self.photto)
        self.current_slide += 1

    def next_slide2(self):

        if self.current_slide == 2:
            image_path = self.read_content_and_image("C:\\Users\\ANDRO\\OneDrive\\Pictures\\PROJEK SEM 1\\beritagui\\home2.png")
        elif self.current_slide == 1:
            image_path = self.read_content_and_image("C:\\Users\\ANDRO\\OneDrive\\Pictures\PROJEK SEM 1\\beritagui\\home3.png")
        else:
            self.current_slide=0
            image_path = self.read_content_and_image("C:\\Users\\ANDRO\\OneDrive\\Pictures\\PROJEK SEM 1\\beritagui\\home1.png")

        self.image_path=image_path
        self.image_label.config(image=self.photto)
        self.current_slide += 1

    def read_content_and_image(self,image_path):
        self.image_path=image_path

        try:
            image = Image.open(self.image_path)
            image = image.resize((self.screen_width, self.screen_height))   
            self.photto = ImageTk.PhotoImage(image)
        except FileNotFoundError:
            print(f"Image file not found: {self.image_path}")
            self.photto = None

        return image_path


    def aboutyohankos(self):
        try:
            self.filter_framee.destroy()
        except:
            pass
        try:
            self.boarding_listt.destroy()  
        except:
            pass
        try:
            self.label_backgroundt.destroy()
        except:
            pass
        try:
            self.bglabel.destroy()
        except:
            pass
        try:
            self.labelphotouserbg.destroy()
        except:
            pass
        self.menu_bar.entryconfigure("Home", state="active")
        self.menu_bar.entryconfigure("About Yohan Kos", state="disabled")
        self.menu_bar.entryconfigure("Boarding List", state="active")
        self.menu_bar.entryconfigure("User Profil", state="active")

        self.foto=Image.open("aboutyohankos.png")
        self.foto=self.foto.resize((self.screen_width,self.screen_height))
        self.photoo=ImageTk.PhotoImage(self.foto)
        self.label_background = Label(self._master_, image=self.photoo)
        self.label_background.pack(fill=BOTH, expand=YES)
        self.label_background.photo = self.photoo


    def filterr(self):
        try:
            self.label_background.destroy()
        except:
            pass
        try:
            self.label_backgroundt.destroy()

        except:
            pass
        try:
            self.labelphotouserbg.destroy()
        except:
            pass
        self.menu_bar.entryconfigure("Home", state="active")
        self.menu_bar.entryconfigure("Boarding List", state="disabled")
        self.menu_bar.entryconfigure("About Yohan Kos", state="active")
        self.menu_bar.entryconfigure("User Profil", state="active")

        self.foto=Image.open("bigdata.jpg")
        self.foto=self.foto.resize((self.screen_width,self.screen_height))
        self.photoo=ImageTk.PhotoImage(self.foto)
        self.bglabel=Label(self._master_,image=self.photoo).place(x=0,y=0)

        self.filter_framee=LabelFrame(self.bglabel,text="Filter",font=("Consolas", 16, "bold"), bd=7, borderwidth=7, fg="dark blue", bg="#C9EEFF")
        self.filter_framee.place(x=20,y=50,width=(self.screen_width2/2)-150,height=self.screen_height-550)
        
        tk.Label(self.filter_framee, text="Jenis Kos", bg="#C9EEFF",font=("consolas", 12, "bold"), relief="flat", bd=0, activebackground="#C9EEFF").place(y=5,x=35)

        self.combobox1 = ttk.Combobox(self.filter_framee, values=["Laki Laki dan Perempuan", "Laki Laki", "Perempuan"], state="readonly")
        self.combobox1.place(x=35, y=30, height=25, width=150)

        self.acvar=BooleanVar()
        self.wifivar=BooleanVar()
        self.kmvar=BooleanVar()

        self.ac=Checkbutton(self.filter_framee, text="AC",variable=self.acvar,bg="#C9EEFF", relief="flat", bd=0, activebackground="#C9EEFF",font=("consolas", 12, "bold"))
        self.ac.place(x=35, y=75)

        self.km=Checkbutton(self.filter_framee, text="Kamar Mandi Dalam ",variable=self.kmvar,bg="#C9EEFF", relief="flat", bd=0, activebackground="#C9EEFF",font=("consolas", 12, "bold"))
        self.km.place(x=35, y=130)

        tk.Label(self.filter_framee, text="Harga", bg="#C9EEFF",font=("consolas", 12, "bold"), relief="flat", bd=0, activebackground="#C9EEFF").place(y=5,x=230)

        self.wf=Checkbutton(self.filter_framee, text="Wi-Fi",variable=self.wifivar,bg="#C9EEFF", relief="flat", bd=0, activebackground="#C9EEFF",font=("consolas", 12, "bold"))
        self.wf.place(x=35, y=185)

        self.combobox2 = ttk.Combobox(self.filter_framee, values=["<500.000", "500.000 - 1.000.000", "1.000.000-1.500.000", ">1.500.000"], state="readonly")
        self.combobox2.place(x=230, y=30, height=25, width=150)

        self.infotabel=LabelFrame(self.bglabel, text="Information", font=("Consolas", 16, "bold"), bd=7, borderwidth=7, fg="dark blue", bg="#C9EEFF")
        self.infotabel.place(x=20,y=400,width=(self.screen_width2/2)-150, height=350)

        self.info_canvas = Canvas(self.infotabel, bg="#C9EEFF", highlightthickness=0)
        self.info_canvas.place(relx=0, rely=0, relwidth=0.95, relheight=1)

        self.info_scrollbar = Scrollbar(self.infotabel, orient="vertical", command=self.info_canvas.yview)
        self.info_scrollbar.place(relx=0.95, y=0, width=15, relheight=1)
        self.info_canvas.configure(yscrollcommand=self.info_scrollbar.set)

        self.info_frame = Frame(self.info_canvas, bg="#C9EEFF")
        self.info_canvas.create_window((0, 0), window=self.info_frame, anchor="nw")


        self.add_information_widgets()

        self.info_canvas.bind("<Configure>", self.on_canvas_configure)
        self.info_frame.update_idletasks()  
        self.info_canvas.configure(scrollregion=self.info_canvas.bbox("all"))
    def add_information_widgets(self):
        with open ("informasi.txt","r") as fili:
            fili=fili.read()
            label = ttk.Label(self.info_frame, text=fili, font=("Consolas", 10), background="#C9EEFF")
            label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

    def on_canvas_configure(self, event):
        self.info_canvas.configure(scrollregion=self.info_canvas.bbox("all"))        
        daftarkos.data_kos(self)
class daftarkos(Dashboard):
    def __init__(self, _master_):
         super().__init__(_master_)


    def data_kos(self):
        button_filter=ttk.Button(self.filter_framee, text="Filter", command=lambda: filter_data())
        button_filter.place(relx=0.36, rely=0.8, width=90,height=35)

        self.boarding_listt = LabelFrame(self.bglabel, bd=7, borderwidth=7, border=8, relief="groove", text="Boarding list", font="consolas 16 bold", fg="dark blue", bg="#C9EEFF")
        self.boarding_listt.place(x=(self.screen_width2/2)-30, y=25, width=self.screen_width2-200, height=self.screen_height-90)

        canvas = Canvas(self.boarding_listt, bg="#C9EEFF", highlightthickness=0)
        canvas.place(relx=0, rely=0, relwidth=0.95, relheight=1)

        scrollbar = Scrollbar(self.boarding_listt, orient="vertical", width=20, command=canvas.yview, troughcolor="light gray")
        scrollbar.place(x=910, y=0, width=25, relheight=1)
        canvas.configure(yscrollcommand=scrollbar.set)

        self.wdw_frame = Frame(canvas, bg="#C9EEFF")
        canvas.create_window((0, 0), window=self.wdw_frame, anchor="nw")

        def on_canvas_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        canvas.bind("<Configure>", on_canvas_configure)
        for widget in self.wdw_frame.winfo_children():
            widget.destroy()
        with open('data_kos.csv', "r", newline='') as file:
            data_boarding = csv.DictReader(file,delimiter=";")

            for i, row in enumerate(data_boarding):
                nama=row["nama"]
                harga = row['harga']
                jenis_kos = row['jenis_kos']
                no_hp_pemilik = row['no_hp_pemilik']
                ac = row['ac']
                kamar_mandi_dalam = row['kamar_mandi_dalam']
                wifi = row['wifi']
                image_path2 = row['image_path']
                kamar_dipakai=row['kamar_dipakai']
                total=row["total_ketersediaan"]
                lokasi=row["lokasi"]
                
                formatted_harga = "{:,.0f}".format(float(harga))

                boarding_image = Image.open(image_path2)
                boarding_image = boarding_image.resize((230,230))
                _photo = ImageTk.PhotoImage(boarding_image)

                location_info=CTkButton(self.wdw_frame, corner_radius=90,width=860,height=300,bg_color="#C9EEFF", text="", fg_color="#97DEFF", state="disable", border_width=7,border_color="white")
                location_info.grid(row=i, column=0,pady=10,padx=20)

                italic_font = font.Font(family="consolas", size=17, slant="italic")
                info_label5 = Button(location_info, text=f"{nama}",
                font=italic_font, bg="#97DEFF", fg="Blue",relief="flat",activebackground="#97DEFF",bd=0,border=0,cursor="hand2", command=lambda nama=nama, no_hp_pemilik=no_hp_pemilik: tampilan_deskripsi(nama, no_hp_pemilik))
                info_label5.place(x=305, y=25)

                italic_font2 = font.Font(family="consolas", size=17, slant="roman")
                info_label = Label(location_info, text=f"Harga: Rp{formatted_harga}\nJenis Kos: {jenis_kos}\nNo HP Pemilik: {no_hp_pemilik}\nAC: {ac}\nKamar Mandi Dalam: {kamar_mandi_dalam}\nWiFi: {wifi}",
                font=italic_font2, bg="#97DEFF", fg="black", justify=LEFT)
                info_label.place(x=310, y=60)

                info_label2 = Label(location_info, text=f"sisa kamar: {int(total)-int(kamar_dipakai)}",
                font=("Consolas", 15), bg="#97DEFF", fg="darkred", justify=LEFT)
                info_label2.place(x=310, y=230)

                info_label4 = Button(location_info, text=f"📍 lokasi",
                font=("Consolas", 15), bg="#97DEFF", justify=LEFT, command=lambda nama=nama: tampilkan_lokasi(nama), relief="flat", bd=0, activebackground="#97DEFF", cursor="hand2", fg="darkgreen")
                info_label4.place(x=610, y=227)

                image_label_boarding_image = Button(location_info, width=230,height=230,image=_photo, bg="#9ca9b0", cursor="hand2", relief="flat", bd=0, activebackground="#9ca9b0")
                image_label_boarding_image.image = _photo
                image_label_boarding_image.place(x=50, y=30)

            def tampilkan_lokasi(nama):
                with open('data_kos.csv', "r", newline='') as file:
                    data_boarding = csv.DictReader(file,delimiter=";")
                    for i, row in enumerate(data_boarding):
                        if row["nama"] == nama:
                            lokasi = row["lokasi"]
                            alamat_Unesa = lokasi
                            gmaps_url = f"https://www.google.com/maps/search/?api=1&query={alamat_Unesa}"
                            webbrowser.open(gmaps_url)
                            break

            def tampilan_deskripsi(nama, no_hp_pemilik):
                global order_button
                global pop_up
                global underline_canvas
                with open('data_kos.csv', "r", newline='') as file:
                    data_boarding = csv.DictReader(file, delimiter=";")
                    for row in data_boarding:
                            if nama == row["nama"]:
                                potopat=row["photopath1"]
                                potopat2=row["photopath2"]
                                potopat3=row["photopath3"]
                              
                                self._master_.withdraw()
                                pop_up = Toplevel()
                                pop_up.title(f"Deskripsi {nama}")
                                # pop_up.overrideredirect(True)
                                pop_up.geometry("870x700+300+30")
                                pop_up.resizable(width=tk.FALSE, height=tk.FALSE)
                                pop_up.config(bg="white")

                                self.frm=LabelFrame(pop_up, text="Photo dan Deskripsi kos",font=("consolas", 16, "bold"))
                                self.frm.place(x=0,y=20,width=870,height=300)
                                try:
                                    img=Image.open(f"{potopat}")
                                    img=img.resize((870,300))
                                    photoimg=ImageTk.PhotoImage(img)
                                    img_label=Label(self.frm, image=photoimg)
                                    img_label.pack(fill="both", expand=True) 
                                    img_label.photo=photoimg
                                except AttributeError:
                                    img_label = Label(self.frm, text="Image belum di upload")
                                    img_label.pack(fill="both", expand=True, anchor="center")                                   
                                def _on_closing():
                                    pop_up.destroy()
                                    self._master_.deiconify()
                                    self._master_.state("zoomed")
                                pop_up.protocol("WM_DELETE_WINDOW", _on_closing)
                                self.slide=1
                                def slide_gambar():
                                    nonlocal img_label
                                    self.slide += 1
                                    if self.slide > 3:  
                                        self.slide = 1
                                    if self.slide == 1:
                                        try:
                                            img_path = f"{potopat}"
                                            img = Image.open(img_path)
                                            img = img.resize((870, 300))
                                            photo_img = ImageTk.PhotoImage(img)

                                            img_label.destroy()
                                            img_label = Label(self.frm, image=photo_img)
                                            img_label.image = photo_img 
                                            img_label.pack(fill="both", expand=True)
                                        except AttributeError:
                                            img_label.destroy()
                                            img_label = Label(self.frm, text="Image belum di upload")
                                            img_label.pack(fill="both", expand=True, anchor="center")
                                    if self.slide == 2:
                                        try:
                                            img_path = f"{potopat2}"
                                            img = Image.open(img_path)
                                            img = img.resize((870, 300))
                                            photo_img = ImageTk.PhotoImage(img)

                                            img_label.destroy()
                                            img_label = Label(self.frm, image=photo_img)
                                            img_label.image = photo_img 
                                            img_label.pack(fill="both", expand=True)
                                        except AttributeError:
                                            img_label.destroy()
                                            img_label = Label(self.frm, text="Image belum di upload")
                                            img_label.pack(fill="both", expand=True, anchor="center")
                                    if self.slide == 3:
                                        try:
                                            img_path = f"{potopat3}"
                                            img = Image.open(img_path)
                                            img = img.resize((870, 300))
                                            photo_img = ImageTk.PhotoImage(img)

                                            img_label.destroy()
                                            img_label = Label(self.frm, image=photo_img)
                                            img_label.image = photo_img 
                                            img_label.pack(fill="both", expand=True)
                                        except AttributeError:
                                            img_label.destroy()
                                            img_label = Label(self.frm, text="Image belum di upload")
                                            img_label.pack(fill="both", expand=True, anchor="center")
                                    pop_up.after(9000, slide_gambar)


                                slide_gambar()
                                tk.Button(pop_up, text=">", command=slide_gambar, bg="yellow", fg="black", activebackground="yellow",
                                relief="flat", bd=0, border=0, width=25, height=25).place(relx=0.965, rely=0.22, width=25, height=25)
                                
                                canvas1 = tk.Canvas(pop_up, bg="black",width=550)
                                canvas1.place(x=50, y=370, relheight=0.0065)
                                canvas1.create_line(0, 0, 650, 0, fill="black", width=2)

                                frem=Frame(pop_up,bd=0,borderwidth=0,border=0)
                                frem.place(x=50,y=375,width=545,height=300)

                                lteks=Text(frem,wrap="word",state="normal",bd=0,borderwidth=0,border=0)
                                lteks.insert("1.0", row["Deskripsi"])
                                lteks.config(state="disabled")
                                lteks.place(x=0,y=0,relheight=1,relwidth=1)

                                canvas2 = tk.Canvas(pop_up, bg="black",width=550)
                                canvas2.place(x=50, y=680, relheight=0.0065)
                                canvas2.create_line(0, 0, 650, 0, fill="black", width=2)

                                label_info=CTkButton(pop_up,width=200,height=220,bg_color="white", text="", fg_color="white", state="disable", border_width=7,border_color="#C69774")
                                label_info.place(x=640,y=360)

                                info=Label(label_info, text="jika sudah klik order\nsilahkan chat pemilik\nkos melalui link\nWA di bawah\nuntuk konfirmasi\npembayaran\ndan pemesanan.\n\nSilahkan masuk\nke menu ini lagi\nuntuk memunculkan\nno WA pemilik\ntepat setelah order.",
                                font=("consolas", 9), fg="black",bg="white", justify=LEFT)
                                info.place(x=13,y=12)
                                
                                order_button = tk.Button(pop_up, text="Order", command=self.konfirmasi_order, bg="white", fg="black",
                                activebackground="white",activeforeground="blue", relief="flat", bd=0, border=0,justify=LEFT)
                                order_button.place(x=700, y=600, width=60,height=30)
                                underline_canvas = Canvas(pop_up, height=1, width=order_button.winfo_reqwidth(), bg="black",highlightthickness=0)
                                underline_canvas.place(x=713, y=600 + order_button.winfo_reqheight())
                                underline_canvas.create_line(0, 0, 0, 0, width=2, fill="black")

                                no_hp_pemilik=str(no_hp_pemilik)
                                no_hp_pemilik=no_hp_pemilik.replace(no_hp_pemilik[0],"+62",1)    
                                wabutton=Button(pop_up,text=f"https://wa.me/{no_hp_pemilik}",fg="black",bg="white",cursor="hand2",activebackground="white",activeforeground="blue", font=("consolas", 10), command=lambda: wa(), relief="flat",border=0,bd=0)
                                wabutton.place(x=640, y=645)
                                def wa():
                                    whatsapp_link = f"https://wa.me/{no_hp_pemilik}"  
                                    webbrowser.open(whatsapp_link)
                                with open('datapengguna.csv', "r", newline='') as file:
                                    data_boarding_user = csv.DictReader(file)
                                    data_boarding_user=list(data_boarding_user)
                                    for row in data_boarding_user:
                                        if row["Username"]==username:
                                            if row["Pesan"]=="yes":
                                                underline_canvas.destroy()
                                                order_button.config(state="disabled")
                                                order_button.config(text="Order Sent")
                                                infobutton=CTkButton(pop_up, text="i", command=lambda: infobutonn(), bg_color="white", fg_color="blue",corner_radius=180
                                                ,border_width=0, border_color="white",width=17,height=17)
                                                infobutton.place(x=765, y=605)

                                                def infobutonn():
                                                    showinfo("Info","You can order after 20 days")
                                                currenday=datetime.now()
                                                lastorder = datetime.strptime(row["TanggalPesan"], "%Y-%m-%d")

                                                if (currenday - lastorder).days < 20:
                                                    order_button.config(state="disabled")
                                                    order_button.config(text="Order Sent")
                                                    infobutton=CTkButton(pop_up, text="i", command=lambda: infobutonn(), bg_color="white", fg_color="blue",corner_radius=180
                                                                            , border_width=0, border_color="white",width=17,height=17)
                                                    infobutton.place(x=765, y=605)
                                                    underline_canvas.destroy()
                                                    def infobutonn():
                                                            showinfo("Info","You can order after 20 days")
                                                    
                                                else:
                                                    row["Pesan"]="no"
                                                    row["TanggalPesan"]=""
                                                    infobutton.destroy()
                                                    order_button.config(state="active",text="Order")
                                                    underline_canvas = Canvas(pop_up, height=1, width=order_button.winfo_reqwidth(), bg="black",highlightthickness=0)
                                                    underline_canvas.place(x=713, y=600 + order_button.winfo_reqheight())
                                                    underline_canvas.create_line(0, 0, 0, 0, width=2, fill="black")

                                with open('datapengguna.csv', 'w', newline='') as file:
                                    kolom = ['Nama', 'Username', 'Password', 'DateOfBirth', "Gender", "Pesan", "TanggalPesan"]
                                    writer = csv.DictWriter(file, fieldnames=kolom)
                                    writer.writeheader()
                                    writer.writerows(data_boarding_user)                          

        self.wdw_frame.update_idletasks()  
        canvas.configure(scrollregion=canvas.bbox("all"))

        def filter_data():

            jenis_kos = self.combobox1.get()
            ac_checked = self.acvar.get()
            km_checked = self.kmvar.get()
            wf_checked = self.wifivar.get()
            harga_range = self.combobox2.get() 

            filtered_data = []  
            with open('data_kos.csv', "r", newline='') as file:
                data_boarding = csv.DictReader(file, delimiter=";")

                for row in data_boarding:
                    
                    jenis_kos_match = jenis_kos == row['jenis_kos'] or jenis_kos==""
                    ac_match = not ac_checked or row['ac'] == 'yes'
                    km_match = not km_checked or row['kamar_mandi_dalam'] == 'yes'
                    wf_match = not wf_checked or row['wifi'] == 'yes'

                    if jenis_kos_match and ac_match and km_match and wf_match:
                        harga = float(row['harga'])

                        if harga_range == "<500.000" and harga < 500000:
                            filtered_data.append(row)
                        elif harga_range == "500.000 - 1.000.000" and 500000 <= harga <= 1000000:
                            filtered_data.append(row)
                        elif harga_range == "1.000.000-1.500.000" and 1000000 <= harga <= 1500000:
                            filtered_data.append(row)
                        elif harga_range == ">1.500.000" and harga > 1500000:
                            filtered_data.append(row)
                        elif harga_range=="":
                            filtered_data.append(row)

            def display_filtered_data():

                for widget in self.wdw_frame.winfo_children():
                    widget.destroy()

                for i, row in enumerate(filtered_data):
                    nama=row["nama"]
                    harga = row['harga']
                    jenis_kos = row['jenis_kos']
                    no_hp_pemilik = row['no_hp_pemilik']
                    ac = row['ac']
                    kamar_mandi_dalam = row['kamar_mandi_dalam']
                    wifi = row['wifi']
                    image_path2 = row['image_path']
                    kamar_dipakai=row['kamar_dipakai']
                    total=row["total_ketersediaan"]
                    lokasi=row["lokasi"]
                    
                    formatted_harga = "{:,.0f}".format(float(harga))

                    boarding_image = Image.open(image_path2)
                    boarding_image = boarding_image.resize((230,230))
                    _photo = ImageTk.PhotoImage(boarding_image)

                    location_info=CTkButton(self.wdw_frame, corner_radius=90,width=860,height=300,bg_color="#C9EEFF", text="", fg_color="#97DEFF", state="disable", border_width=7,border_color="white")
                    location_info.grid(row=i, column=0,pady=10,padx=20)

                    italic_font = font.Font(family="consolas", size=17, slant="italic")
                    info_label5 = Button(location_info, text=f"{nama}",
                    font=italic_font, bg="#97DEFF", fg="Blue",relief="flat",activebackground="#97DEFF",bd=0,border=0,cursor="hand2", command=lambda nama=nama, no_hp_pemilik=no_hp_pemilik: tampilan_deskripsi(nama, no_hp_pemilik))

                    info_label5.place(x=305, y=25)
                    italic_font2 = font.Font(family="consolas", size=17, slant="roman")
                    info_label = Label(location_info, text=f"Harga: Rp{formatted_harga}\nJenis Kos: {jenis_kos}\nNo HP Pemilik: {no_hp_pemilik}\nAC: {ac}\nKamar Mandi Dalam: {kamar_mandi_dalam}\nWiFi: {wifi}",
                                    font=italic_font2, bg="#97DEFF", fg="black", justify=LEFT)
                    info_label.place(x=310, y=60)

                    info_label2 = Label(location_info, text=f"sisa kamar: {int(total)-int(kamar_dipakai)}",
                    font=("Consolas", 15), bg="#97DEFF", fg="darkred", justify=LEFT)
                    info_label2.place(x=310, y=230)

                    info_label4 = Button(location_info, text=f"📍 lokasi",
                    font=("Consolas", 15), bg="#97DEFF", justify=LEFT, command=lambda nama=nama: tampilkan_lokasi(nama), relief="flat", bd=0, activebackground="#97DEFF", cursor="hand2", fg="darkgreen")
                    info_label4.place(x=610, y=227)

                    image_label_boarding_image = Button(location_info, width=230,height=230,image=_photo, bg="#9ca9b0", cursor="hand2", relief="flat", bd=0, activebackground="#9ca9b0")
                    image_label_boarding_image.image = _photo
                    image_label_boarding_image.place(x=50, y=30)
        
                    def tampilkan_lokasi(nama):
                        with open('data_kos.csv', "r", newline='') as file:
                            data_boarding = csv.DictReader(file, delimiter=";")
                            for i, row in enumerate(data_boarding):
                                if row["nama"] == nama:
                                    lokasi = row["lokasi"]
                                    alamat_Unesa = lokasi
                                    gmaps_url = f"https://www.google.com/maps/search/?api=1&query={alamat_Unesa}"
                                    webbrowser.open(gmaps_url)
                                    break

                    def tampilan_deskripsi(nama, no_hp_pemilik):
                        global order_button
                        global pop_up
                        global underline_canvas
                        with open('data_kos.csv', "r", newline='') as file:
                            data_boarding = csv.DictReader(file, delimiter=";")
                            for row in data_boarding:
                                    if nama == row["nama"]:
                                        potopat=row["photopath1"]
                                        potopat2=row["photopath2"]
                                        potopat3=row["photopath3"]                                        
                                        self._master_.withdraw()
                                        pop_up = Toplevel()
                                        pop_up.title(f"Deskripsi {nama}")
                                        # pop_up.overrideredirect(True)
                                        pop_up.geometry("870x700+300+30")
                                        pop_up.resizable(width=tk.FALSE, height=tk.FALSE)
                                        pop_up.config(bg="white")
                                        self.frm=LabelFrame(pop_up, text="Photo dan Deskripsi kos",font=("consolas", 16, "bold"))
                                        self.frm.place(x=0,y=20,width=870,height=300)
                                        try:
                                            img=Image.open(f"{potopat}")
                                            img=img.resize((870,300))
                                            photoimg=ImageTk.PhotoImage(img)
                                            img_label=Label(self.frm, image=photoimg)
                                            img_label.pack(fill="both", expand=True) 
                                            img_label.photo=photoimg
                                        except AttributeError:
                                            img_label = Label(self.frm, text="Image belum di upload")
                                            img_label.pack(fill="both", expand=True, anchor="center")                                   
                                        def _on_closing():
                                            pop_up.destroy()
                                            self._master_.deiconify()
                                            self._master_.state("zoomed")
                                        pop_up.protocol("WM_DELETE_WINDOW", _on_closing)
                                        self.slide=1
                                        def slide_gambar():
                                            nonlocal img_label
                                            self.slide += 1
                                            if self.slide > 3:  
                                                self.slide = 1
                                            if self.slide == 1:
                                                try:
                                                    img_path = f"{potopat}"
                                                    img = Image.open(img_path)
                                                    img = img.resize((870, 300))
                                                    photo_img = ImageTk.PhotoImage(img)

                                                    img_label.destroy()
                                                    img_label = Label(self.frm, image=photo_img)
                                                    img_label.image = photo_img 
                                                    img_label.pack(fill="both", expand=True)
                                                except AttributeError:
                                                    img_label.destroy()
                                                    img_label = Label(self.frm, text="Image belum di upload")
                                                    img_label.pack(fill="both", expand=True, anchor="center")
                                            if self.slide == 2:
                                                try:
                                                    img_path = f"{potopat2}"
                                                    img = Image.open(img_path)
                                                    img = img.resize((870, 300))
                                                    photo_img = ImageTk.PhotoImage(img)

                                                    img_label.destroy()
                                                    img_label = Label(self.frm, image=photo_img)
                                                    img_label.image = photo_img 
                                                    img_label.pack(fill="both", expand=True)
                                                except AttributeError:
                                                    img_label.destroy()
                                                    img_label = Label(self.frm, text="Image belum di upload")
                                                    img_label.pack(fill="both", expand=True, anchor="center")
                                            if self.slide == 3:
                                                try:
                                                    img_path = f"{potopat3}"
                                                    img = Image.open(img_path)
                                                    img = img.resize((870, 300))
                                                    photo_img = ImageTk.PhotoImage(img)

                                                    img_label.destroy()
                                                    img_label = Label(self.frm, image=photo_img)
                                                    img_label.image = photo_img 
                                                    img_label.pack(fill="both", expand=True)
                                                except AttributeError:
                                                    img_label.destroy()
                                                    img_label = Label(self.frm, text="Image belum di upload")
                                                    img_label.pack(fill="both", expand=True, anchor="center")
                                            pop_up.after(9000, slide_gambar)


                                        slide_gambar()
                                        tk.Button(pop_up, text=">", command=slide_gambar, bg="yellow", fg="black", activebackground="yellow",
                                        relief="flat", bd=0, border=0, width=25, height=25).place(relx=0.965, rely=0.22, width=25, height=25)
                                        
                                        canvas1 = tk.Canvas(pop_up, bg="black",width=550)
                                        canvas1.place(x=50, y=370, relheight=0.0065)
                                        canvas1.create_line(0, 0, 650, 0, fill="black", width=2)

                                        frem=Frame(pop_up,bd=0,borderwidth=0,border=0)
                                        frem.place(x=50,y=375,width=545,height=300)

                                        lteks=Text(frem,wrap="word",state="normal",bd=0,borderwidth=0,border=0)
                                        lteks.insert("1.0", row["Deskripsi"])
                                        lteks.config(state="disabled")
                                        lteks.place(x=0,y=0,relheight=1,relwidth=1)

                                        canvas2 = tk.Canvas(pop_up, bg="black",width=550)
                                        canvas2.place(x=50, y=680, relheight=0.0065)
                                        canvas2.create_line(0, 0, 650, 0, fill="black", width=2)

                                        label_info=CTkButton(pop_up,width=200,height=220,bg_color="white", text="", fg_color="white", state="disable", border_width=7,border_color="#C69774")
                                        label_info.place(x=640,y=360)

                                        info=Label(label_info, text="jika sudah klik order\nsilahkan chat admin\nmelalui link WA di bawah\nuntuk konfirmasi pembayaran.\n\nSilahkan chat pemilik kos\nno WA tertera pada\nbagian boarding list.\n\nSilahkan melakukan deal\nkepada pemilik mengenai\npembayaran lalu konfirmasi\nke WA admin di bawah jangan\nlupa kirim bukti pembayran",
                                        font=("consolas", 8), fg="black",bg="white", justify=LEFT)
                                        info.place(x=13,y=10)
                      
                                        order_button = tk.Button(pop_up, text="Order", command=self.konfirmasi_order, bg="white", fg="black",
                                        activebackground="white",activeforeground="blue", relief="flat", bd=0, border=0,justify=LEFT)
                                        order_button.place(x=700, y=600, width=60,height=30)
                                        underline_canvas = Canvas(pop_up, height=1, width=order_button.winfo_reqwidth(), bg="black",highlightthickness=0)
                                        underline_canvas.place(x=713, y=600 + order_button.winfo_reqheight())
                                        underline_canvas.create_line(0, 0, 0, 0, width=2, fill="black")

                                        no_hp_pemilik=str(no_hp_pemilik)
                                        no_hp_pemilik=no_hp_pemilik.replace(no_hp_pemilik[0],"+62",1)    
                                        wabutton=Button(pop_up,text=f"https://wa.me/{no_hp_pemilik}",fg="black",bg="white",cursor="hand2",activebackground="white",activeforeground="blue", font=("consolas", 10), command=lambda: wa(), relief="flat",border=0,bd=0)
                                        wabutton.place(x=640, y=645)
                                        def wa():
                                            whatsapp_link = f"https://wa.me/{no_hp_pemilik}"  
                                            webbrowser.open(whatsapp_link)
                                        with open('datapengguna.csv', "r", newline='') as file:
                                            data_boarding_user = csv.DictReader(file)
                                            data_boarding_user=list(data_boarding_user)
                                            for row in data_boarding_user:
                                                if row["Username"]==username:
                                                    if row["Pesan"]=="yes":
                                                        underline_canvas.destroy()
                                                        order_button.config(state="disabled")
                                                        order_button.config(text="Order Sent")
                                                        infobutton=CTkButton(pop_up, text="i", command=lambda: infobutonn(), bg_color="white", fg_color="blue",corner_radius=180
                                                        ,border_width=0, border_color="white",width=17,height=17)
                                                        infobutton.place(x=765, y=605)

                                                        def infobutonn():
                                                            showinfo("Info","You can order after 20 days")
                                                        currenday=datetime.now()
                                                        lastorder = datetime.strptime(row["TanggalPesan"], "%Y-%m-%d")

                                                        if (currenday - lastorder).days < 20:
                                                            order_button.config(state="disabled")
                                                            order_button.config(text="Order Sent")
                                                            infobutton=CTkButton(pop_up, text="i", command=lambda: infobutonn(), bg_color="white", fg_color="blue",corner_radius=180
                                                                                    , border_width=0, border_color="white",width=17,height=17)
                                                            infobutton.place(x=765, y=605)
                                                            underline_canvas.destroy()
                                                            def infobutonn():
                                                                    showinfo("Info","You can order after 20 days")
                                                            
                                                        else:
                                                            row["Pesan"]="no"
                                                            row["TanggalPesan"]=""
                                                            infobutton.destroy()
                                                            order_button.config(state="active",text="Order")
                                                            underline_canvas = Canvas(pop_up, height=1, width=order_button.winfo_reqwidth(), bg="black",highlightthickness=0)
                                                            underline_canvas.place(x=713, y=600 + order_button.winfo_reqheight())
                                                            underline_canvas.create_line(0, 0, 0, 0, width=2, fill="black")
                                                            
                                        with open('datapengguna.csv', 'w', newline='') as file:
                                            kolom = ['Nama', 'Username', 'Password', 'DateOfBirth', "Gender", "Pesan", "TanggalPesan"]
                                            writer = csv.DictWriter(file, fieldnames=kolom)
                                            writer.writeheader()
                                            writer.writerows(data_boarding_user)   
            display_filtered_data()
# sebaiknya selalu tetap menetapkan encoding secara eksplisit untuk memastikan kestabilan dan konsistensi dalam membaca file.
class Dashboard_pemilik:
    def __init__(self,mmasster):
        self.mmasster=mmasster
        self.mmasster.title("Yohan Kos")
        self.mmasster.state("zoomed")
        self.mmasster.resizable(width=tk.FALSE, height=tk.FALSE)
        self.menu_bar = Menu(self.mmasster)
        self.mmasster.config(menu=self.menu_bar)

        self.screen_widthh = self.mmasster.winfo_screenwidth()
        self.screen_heightt = self.mmasster.winfo_screenheight()

        menu_file = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Boarding Edit", command=self.Boarding_edit)
        self.menu_bar.add_cascade(label="About Yohan Kos", command=self.aboutyohankos)
        menu_file.add_separator()

        self.Boarding_edit()
    def Boarding_edit(self):
        try:
            self.label_background.destroy()
        except:
            pass       
        self.menu_bar.entryconfigure("Boarding Edit", state="disabled")
        self.menu_bar.entryconfigure("About Yohan Kos", state="active")

        self.bgmaster=Frame(self.mmasster)
        self.bgmaster.place(x=0,y=0,width=self.screen_widthh,height=self.screen_heightt)

        self.screen_widthh_frame = self.bgmaster.winfo_screenwidth()
        self.screen_heightt_frame = self.bgmaster.winfo_screenheight()

        self.foto=Image.open("bigdata.jpg")
        self.foto=self.foto.resize((self.screen_widthh_frame,self.screen_heightt_frame*2))
        self.foto=self.foto.rotate(180)
        self.photoo=ImageTk.PhotoImage(self.foto)
        self.bglabel=Label(self.bgmaster,image=self.photoo).place(x=0,y=0,relwidth=0.5)

        self.fotodesk=Image.open("bigdata.jpg")
        self.fotodesk=self.fotodesk.resize((self.screen_widthh_frame,self.screen_heightt_frame*2))
        self.fotodesk=self.fotodesk.rotate(180)
        self.photoo1=ImageTk.PhotoImage(self.fotodesk)
        self.bglabel1=Label(self.bgmaster,image=self.photoo1).place(relx=0.5000001,y=0,relwidth=0.5)

        self.prame_label=LabelFrame(self.bglabel, text="Edit Data Kos", background="#EEF5FF",font=("consolas",20,"bold"))
        self.prame_label.place(relx=0.05,rely=0.05,relwidth=0.40,relheight=0.90)

        self.framedesk=LabelFrame(self.bglabel1,background="#EEF5FF",text="Edit Deskripsi Kos",font=("consolas",20,"bold"))
        self.framedesk.place(relx=0.55,rely=0.05,relwidth=0.40,relheight=0.90)

        
        with open ("data_kos.csv","r") as fille:
            boardinglist=csv.DictReader(fille, delimiter=";")
            for row in boardinglist:
                if username_pemilik == row["Username"]:
                    nama=row["nama"]
                    harga = row['harga']
                    jenis_kos = row['jenis_kos']
                    no_hp_pemilik = row['no_hp_pemilik']
                    ac = row['ac']
                    kamar_mandi_dalam = row['kamar_mandi_dalam']
                    wifi = row['wifi']
                    image_path2 = row['image_path']
                    kamar_dipakai=row['kamar_dipakai']
                    total=row["total_ketersediaan"]
                    lokasi=row["lokasi"]
                    desk=row["Deskripsi"]
                    photoimage1=row["photopath1"]
                    photoimage2=row["photopath2"]
                    photoimage3=row["photopath3"]

                    formatted_harga = "{:,.0f}".format(float(harga))

                    boarding_image = Image.open(image_path2)
                    boarding_image = boarding_image.resize((230,230))
                    _photo = ImageTk.PhotoImage(boarding_image)

                    location_info=CTkButton(self.prame_label, corner_radius=90,width=510,height=350,bg_color="#EEF5FF", text="", fg_color="#EEF5FF", state="disable", border_width=7,border_color="white")
                    location_info.place(x=50,y=320)          

                    buton_edit=Button(self.prame_label,justify=LEFT, text="Edit data",font="consolas 12", bd=0,relief="flat",border=0,bg="#EEF5FF", cursor="hand2", activebackground="#EEF5FF",activeforeground="blue",command=self.editdata)
                    buton_edit.place(x=305,y=200)
                    underline_canvas1 = tk.Canvas(self.prame_label, height=1, width=82, bg="black", highlightthickness=0)
                    underline_canvas1.place(x=310, y=193 + buton_edit.winfo_reqheight())
                    underline_canvas1.create_line(0, 0, 0, 0, width=2, fill="black")

                    info_label5 = CTkButton(self.prame_label, text=f"nama kos:\n{nama}",font=("consolas",20),
                    bg_color="#EEF5FF", fg_color="#EEF5FF",border_width=7,border_color="white",text_color="black",text_color_disabled="black", state="disabled",corner_radius=30,width=280,height=110)
                    info_label5.place(x=305, y=80)

                    italic_font2 = font.Font(family="consolas", size=12, slant="roman")
                    info_label = Label(self.prame_label, text=f"Harga: Rp{formatted_harga}\nJenis Kos: {jenis_kos}\nNo HP Pemilik: {no_hp_pemilik}\nAC: {ac}\nKamar Mandi Dalam: {kamar_mandi_dalam}\nWiFi: {wifi}\nKoordinat: {lokasi}",
                    font=italic_font2, bg="#EEF5FF", fg="black", justify=LEFT)
                    info_label.place(x=95, y=370)

                    info_label2 = Label(self.prame_label, text=f"Kamar dipakai: {kamar_dipakai}\nTotal kamar: {total}",
                    font=("Consolas", 13), bg="#EEF5FF", fg="darkred", justify=LEFT)
                    info_label2.place(x=95, y=540)

                    info_label4 = Button(self.prame_label, text=f"📍 google maps lokasi",
                    font=("Consolas", 12), bg="#EEF5FF", justify=LEFT,command=lambda nama=nama :tampilkan_lokasi(nama), relief="flat", bd=0, activebackground="#EEF5FF", cursor="hand2", fg="darkgreen")
                    info_label4.place(x=305, y=255)

                    image_label_boarding_image = Button(self.prame_label, width=230,height=230,image=_photo, bg="#9ca9b0", cursor="hand2", relief="flat", bd=0, activebackground="#9ca9b0")
                    image_label_boarding_image.image = _photo
                    image_label_boarding_image.place(x=50, y=50)

                    buton_kamar=Button(self.prame_label,command=lambda: edit_kamar2(), text="update ketersediaan",font="consolas 12", bd=0,relief="flat",border=0,bg="#EEF5FF", cursor="hand2", activebackground="#EEF5FF",activeforeground="blue")
                    buton_kamar.place(x=200,y=600)
                    underline_canvas = tk.Canvas(self.prame_label, height=1, width=174, bg="black", highlightthickness=0)
                    underline_canvas.place(x=205, y=594 + buton_kamar.winfo_reqheight())
                    underline_canvas.create_line(0, 0, 0, 0, width=2, fill="black")


                    editbuton=Button(self.framedesk,text="Edit",command=lambda :tekss())
                    editbuton.place(relx=0.45,rely=0.35)

                    teksprame=Frame(self.framedesk)
                    teksprame.place(relx=0.08,rely=0.05,relwidth=0.84,relheight=0.3)

                    deskripsi_kos= tk.Text(teksprame,wrap="word", state="normal")
                    deskripsi_kos.place(x=0,y=0, relwidth=1)
                    deskripsi_kos.insert("1.0", desk)
                    deskripsi_kos.config(state="disabled")

                    image_kamar_dalam=Button(self.framedesk,command=lambda file_path=photoimage1, xfield=20:upload_image(file_path,xfield), text="Image kamar dalam kost",)
                    image_kamar_dalam.place(x=20,y=320)

                    image_kamar_mandi=Button(self.framedesk,command=lambda file_path=photoimage2,xfield=230:upload_image(file_path,xfield),text="Image kamar mandi kost",)
                    image_kamar_mandi.place(x=230,y=320)

                    image_parkiran_motor=Button(self.framedesk,command=lambda file_path=photoimage3,xfield=430:upload_image(file_path,xfield),text="Image parkiran motor kost",)
                    image_parkiran_motor.place(x=430,y=320)
                    def nampil(file_path,xfield):
                            try:
                                self.image_path = file_path
                                image = Image.open(self.image_path)
                                image=image.resize((150,150))
                                photodalam = ImageTk.PhotoImage(image)
                                self.image_label = Label(self.framedesk, image=photodalam)
                                self.image_label.image = photodalam
                                self.image_label.place(x=xfield, y=400) 
                            except AttributeError:
                                pass
                            except FileNotFoundError:
                                showerror("Error","File tidak ditemukan")
                    nampil(photoimage1,20)
                    nampil(photoimage2,230)
                    nampil(photoimage3,430)
                    def upload_image(file_path, xfield):
                        konfirmmm=askyesno("Simpan gambar","Anda yakin akan menyimpan gambar ini pada bagian deskripsi kos anda?")
                        if konfirmmm:
                            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
                            if file_path:
                                
                                image = Image.open(file_path)
                                image=image.resize((150,150))
                                photodalam = ImageTk.PhotoImage(image)
                                self.image_label = Label(self.framedesk, image=photodalam)
                                self.image_label.image = photodalam
                                self.image_label.place(x=xfield, y=400) 
                                with open('data_kos.csv', 'r') as file:
                                    reader = csv.DictReader(file, delimiter=";")
                                    reader=list(reader)
                                    for row in reader:
                                        if username_pemilik==row["Username"]:
                                            if xfield == 20:
                                                row["photopath1"]=file_path
                                            if xfield== 230:
                                                row["photopath2"]=file_path
                                            if xfield == 430:
                                                row["photopath3"]=file_path
                                with open('data_kos.csv', 'w', newline='') as file:
                                    kolom = ['nama','harga','jenis_kos','no_hp_pemilik','ac','kamar_mandi_dalam','wifi','image_path','kamar_dipakai','total_ketersediaan','lokasi','Username','Password','Deskripsi',"photopath1","photopath2","photopath3"]
                                    writer = csv.DictWriter(file, fieldnames=kolom,delimiter=";")
                                    writer.writeheader()
                                    writer.writerows(reader)
                        
                    def tekss(): 
                        submbuton=Button(self.framedesk,text="Submit",command=lambda :save_to_label())
                        submbuton.place(relx=0.45,rely=0.35)

                        deskripsi_kos.config(state="normal")

                        
                        def save_to_label():

                            text_content = deskripsi_kos.get("1.0", tk.END)
                            text_content = text_content.strip("\n").rstrip()
                            text_content = text_content.replace("\n", " ")
                            deskripsi_kos.config(state="disabled")

                            with open('data_kos.csv', "r", newline='') as file:
                                data_boarding = csv.DictReader(file,delimiter=";")
                                data_boarding=list(data_boarding)
                                for row in data_boarding:
                                    if row["Username"]==username_pemilik:
                                        row["Deskripsi"]=text_content
                            with open('data_kos.csv', 'w', newline='') as file:
                                kolom = ['nama','harga','jenis_kos','no_hp_pemilik','ac','kamar_mandi_dalam','wifi','image_path','kamar_dipakai','total_ketersediaan','lokasi','Username','Password','Deskripsi',"photopath1","photopath2","photopath3"]
                                writer = csv.DictWriter(file, fieldnames=kolom,delimiter=";")
                                writer.writeheader()
                                writer.writerows(data_boarding)
                                                        
                            nonlocal submbuton
                            submbuton.destroy()

                    def edit_kamar2():
                        global entrytotal
                        global kamar
                        kamar=Toplevel()
                        kamar.geometry("300x250+600+200")
                        kamar.title("Edit Kamar")
                        kamar.config(bg="#EEF5FF")
                        buton_kamar.config(state="disabled")

                        tk.Label(kamar,font=("consolas", 15),bg="#EEF5FF",justify=LEFT,text=f"kamar dipakai: {kamar_dipakai}\n\n\nTotal ketersediaan: {total}").place(x=12,y=12)
                        tk.Button(kamar, text="△",command=lambda nama=nama: edit_kamar_tambah(nama)).place(x=220,y=12)
                        tk.Button(kamar, text="▽",command=lambda nama=nama: edit_kamar_kurang(nama)).place(x=240,y=12)
                        entrytotal=Entry(kamar)
                        entrytotal.place(relx=0.36,rely=0.50,width=77)
                        tk.Button(kamar,text="Ubah total\nketersediaan",command=lambda nama=nama: edit_total_kamar(nama)).place(relx=0.36,rely=0.60)

                        def on_closing():
                            buton_kamar.config(state="active")
                            kamar.destroy()
                        kamar.protocol("WM_DELETE_WINDOW", on_closing) 

                    def edit_total_kamar(nama):
                        kofirm=askyesno("Confirmation", f"Anda yakin akan mengganti total ketersediaan menjadi {entrytotal.get()} ?")
                        if kofirm:
                            with open ("data_kos.csv","r") as fille:
                                boardinglist2=csv.DictReader(fille, delimiter=";")
                                boardinglist2=list(boardinglist2)
                                for row in boardinglist2:
                                    if row["nama"]==nama:
                                        row['total_ketersediaan']=entrytotal.get()
                                        if int(row["total_ketersediaan"])>=int(row["kamar_dipakai"]):
                                            with open('data_kos.csv', 'w', newline='') as file:
                                                kolom = ['nama','harga','jenis_kos','no_hp_pemilik','ac','kamar_mandi_dalam','wifi','image_path','kamar_dipakai','total_ketersediaan','lokasi','Username','Password','Deskripsi',"photopath1","photopath2","photopath3"]
                                                writer = csv.DictWriter(file, fieldnames=kolom,delimiter=";")
                                                writer.writeheader()
                                                writer.writerows(boardinglist2)
                                                showinfo("Success", "Total ketersediaan berhasil diubah")
                                        else:
                                            showerror("Error","Tidak bisa diubah")
                                            buton_kamar.config(state="active")
                                            return   
                            buton_kamar.config(state="active")
                            kamar.destroy()
                            self.bgmaster.destroy()
                            self.Boarding_edit()                                         
                        else:
                            buton_kamar.config(state="active") 
                            kamar.destroy()
                    def edit_kamar_tambah(nama):
                        kofirm=askyesno("Confirmation", "Anda yakin akan menambah kamar yang dipakai?")
                        if kofirm:
                            with open ("data_kos.csv","r") as fille:
                                boardinglist3=csv.DictReader(fille, delimiter=";")
                                boardinglist3=list(boardinglist3)
                                for row in boardinglist3:
                                    if row["nama"]==nama:
                                        if 0 <int(row["total_ketersediaan"])-int(row["kamar_dipakai"]):
                                            kamardinggo=int(row['kamar_dipakai'])+1
                                            row["kamar_dipakai"]=str(kamardinggo)
                                        else:
                                            showerror("Error","Tidak bisa ditambah")
                                            buton_kamar.config(state="active")
                                            return
                            with open('data_kos.csv', 'w', newline='') as file:
                                kolom = ['nama','harga','jenis_kos','no_hp_pemilik','ac','kamar_mandi_dalam','wifi','image_path','kamar_dipakai','total_ketersediaan','lokasi','Username','Password','Deskripsi',"photopath1","photopath2","photopath3"]
                                writer = csv.DictWriter(file, fieldnames=kolom,delimiter=";")
                                writer.writeheader()
                                writer.writerows(boardinglist3)
                                showinfo("Success", "Kamar yang dipakai berhasil diubah")
                            buton_kamar.config(state="active") 
                            kamar.destroy()
                            self.bgmaster.destroy()
                            self.Boarding_edit() 
                        else:
                            buton_kamar.config(state="active") 
                            kamar.destroy()
                    def edit_kamar_kurang(nama):
                        kofirm=askyesno("Confirmation", "Anda yakin akan mengurang kamar yang dipakai?")
                        if kofirm:
                            with open ("data_kos.csv","r") as fille:
                                boardinglist3=csv.DictReader(fille, delimiter=";")
                                boardinglist3=list(boardinglist3)
                                for row in boardinglist3:
                                    if row["nama"]==nama:
                                        if 0 < int(row["kamar_dipakai"]):
                                            kamardinggo=int(row['kamar_dipakai'])-1
                                            row["kamar_dipakai"]=str(kamardinggo)
                                        else:
                                            showerror("Error","Tidak bisa dikurang")
                                            buton_kamar.config(state="active")
                                            return
                            with open('data_kos.csv', 'w', newline='') as file:
                                kolom = ['nama','harga','jenis_kos','no_hp_pemilik','ac','kamar_mandi_dalam','wifi','image_path','kamar_dipakai','total_ketersediaan','lokasi','Username','Password','Deskripsi',"photopath1","photopath2","photopath3"]
                                writer = csv.DictWriter(file, fieldnames=kolom,delimiter=";")
                                writer.writeheader()
                                writer.writerows(boardinglist3)
                                showinfo("Success", "Kamar yang dipakai berhasil diubah")
                            buton_kamar.config(state="active") 
                            kamar.destroy()
                            self.bgmaster.destroy()
                            self.Boarding_edit() 
                        else:
                            buton_kamar.config(state="active")
                            kamar.destroy() 
                    def tampilkan_lokasi(nama):
                        with open('data_kos.csv', "r", newline='') as file:
                            data_boarding = csv.DictReader(file, delimiter=";")
                            for i, row in enumerate(data_boarding):
                                if row["nama"] == nama:
                                    lokasi = row["lokasi"]
                                    alamat_Unesa = lokasi
                                    gmaps_url = f"https://www.google.com/maps/search/?api=1&query={alamat_Unesa}"
                                    webbrowser.open(gmaps_url)
                                    break
        infodeskbutton=CTkButton(self.framedesk,text="i",width=20,height=20,bg_color="#EEF5FF",command=lambda: inpone(),fg_color="blue",corner_radius=90,border_width=0)
        infodeskbutton.place(x=15,y=15)
        def inpone():
            showinfo("Info","Sebaiknya jangan menggunakan enter")

    def editdata(self):
        self.prame_edit=Frame(self.bglabel, background="#EEF5FF")
        self.prame_edit.place(relx=0.05,rely=0.05,relwidth=0.40,relheight=0.90)
        with open('data_kos.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter=";")
            reader=list(reader)
            for row in reader:
                if username_pemilik == row["Username"]:
                    nama=row["nama"]
                    harga = row['harga']
                    jenis_kos = row['jenis_kos']
                    no_hp_pemilik = row['no_hp_pemilik']
                    ac = row['ac']
                    kamar_mandi_dalam = row['kamar_mandi_dalam']
                    wifi = row['wifi']
                    image_path2 = row['image_path']
                    kamar_dipakai=row['kamar_dipakai']
                    total=row["total_ketersediaan"]
                    lokasi=row["lokasi"]

                    previusbuton=Button(self.prame_edit,text="Previous Slide",command=lambda:balik())
                    previusbuton.place(x=48,y=685)

                    def balik():
                        self.prame_edit.destroy()

                    self.gnti_nama=cret_label_entry("Nama", nama, 50)
                    self.gnti_harga=cret_label_entry("Harga", harga, 140)
                    self.gnti_nohp=cret_label_entry("No HP Pemilik", no_hp_pemilik, 250)
                    self.gntijeniskos=cret_label_combobox("Jenis Kos", jenis_kos, ["Laki Laki", "Perempuan", "Laki Laki dan Perempuan"], 340)
                    self.gntac=cret_label_combobox("AC", ac, ["Yes", "No"], 430)
                    self.gntkm=cret_label_combobox("Kamar Mandi Dalam", kamar_mandi_dalam, ["Yes", "No"], 520)
                    self.gntwifi=cret_label_combobox("WiFi", wifi, ["Yes", "No"], 610)

                    label = Label(self.prame_edit, text="Lokasi", font=("Consolas", 11), background="#EEF5FF")
                    label.place(x=330, y=50)

                    self.button_upload_image = Button(self.prame_edit, text="Upload Image", command=lambda: upload_image())
                    self.button_upload_image.place(x=330, y=340)

                    self.entrylokation = Entry(self.prame_edit, width=30, fg='black', bd=0, bg='white', font=('consolas', 11))
                    self.entrylokation.place(x=330, y=80, height=30)
                    self.entrylokation.insert(0, lokasi)
                    self.entrylokation.bind('<FocusIn>', lambda eg: on_enter(eg, self.entrylokation, lokasi))
                    self.entrylokation.bind('<FocusOut>', lambda eg: on_leave(eg, self.entrylokation, lokasi))

                    self.image_pathht = image_path2
                    image = Image.open(self.image_pathht)
                    image=image.resize((250,150))
                    photo = ImageTk.PhotoImage(image)
                    self.image_label = Label(self.prame_edit, image=photo)
                    self.image_label.image = photo
                    self.image_label.place(x=330 ,y=150)                    

                    self.button_submit = CTkButton(self.prame_edit, text="Submit", command=lambda: simpan(), bg_color="#EEF5FF", corner_radius=70)
                    self.button_submit.place(x=370, y=460)                    

                def upload_image():
                    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
                    if file_path:
                        if askyesno("Ganti Foto","Apa anda yakin ingin mengganti foto depan anda?"):
                            self.image_pathht = file_path
                            image = Image.open(self.image_pathht)
                            image=image.resize((250,150))
                            photo = ImageTk.PhotoImage(image)
                            self.image_label = Label(self.prame_edit, image=photo)
                            self.image_label.image = photo
                            self.image_label.place(x=330 ,y=150) 

                def cret_label_entry(label_text, velyuawal, yposition):
                    label = Label(self.prame_edit, text=label_text, font=("Consolas", 11), background="#EEF5FF")
                    label.place(x=48, y=yposition)

                    entrywiget = Entry(self.prame_edit, width=30, fg='black', bd=0, bg='white', font=('consolas', 11))
                    entrywiget.place(x=48, y=yposition + 30, height=30)
                    entrywiget.insert(0, velyuawal)
                    entrywiget.bind('<FocusIn>', lambda eg: on_enter(eg, entrywiget, velyuawal))
                    entrywiget.bind('<FocusOut>', lambda eg: on_leave(eg, entrywiget, velyuawal))
                    return entrywiget
                

                def cret_label_combobox(label_text, velyuawal, velyu, yposition):
                    label = Label(self.prame_edit, text=label_text, font=("Consolas", 11), background="#EEF5FF")
                    label.place(x=48, y=yposition)

                    comboboxxx = ttk.Combobox(self.prame_edit, values=velyu, state="readonly", width=35)
                    comboboxxx.place(x=48, y=yposition + 30)
                    comboboxxx.set(velyuawal)

                    return comboboxxx
                
                def on_enter(eg, entrywiget, teksawal):
                    entrywiget.delete(0, "end")

                def on_leave(eg, entrywiget, teksawal):
                    if entrywiget.get() == '':
                        entrywiget.insert(0, teksawal)

                def simpan():
                    nama_baru = self.gnti_nama.get()
                    harga_baru = self.gnti_harga.get()
                    no_hp_baru = self.gnti_nohp.get()
                    jenis_kos_baru = self.gntijeniskos.get()
                    ac_baru = self.gntac.get()
                    ac_baru=ac_baru.lower()
                    km_baru = self.gntkm.get()
                    km_baru=km_baru.lower()
                    wifi_baru = self.gntwifi.get()
                    wifi_baru=wifi_baru.lower()
                    lokasi_baru = self.entrylokation.get()

                    lokassi=lokasi_baru.split(",")
                    if nama_baru!="" and harga_baru !="" and no_hp_baru!="" and lokasi_baru!="": 
                        try:
                            location1=float(lokassi[0])
                            location2=float(lokassi[1])
                            if -90 <= location1 <= 90 and -180 <= location2 <= 180:
                                    with open ("data_kos.csv","r") as databording:
                                        databordingg=csv.DictReader(databording, delimiter=";")
                                        for row in databordingg:
                                            if row["Username"]==username_pemilik:
                                                break
                                            if nama_baru.lower() == row["nama"].lower():
                                                showerror("Error","Tolong masukkan nama kos yang berbeda")
                                                return
                                    if harga_baru.isdigit():
                                        if no_hp_baru.isdigit() and 11 <= len(no_hp_baru) <= 13:                   
                                                                with open('data_kos.csv', 'r') as file:
                                                                    reader = csv.DictReader(file, delimiter=";")
                                                                    existing_data = list(reader)
                                                                    for row in existing_data:
                                                                        if username_pemilik==row["Username"]:
                                                                            row["nama"]=nama_baru
                                                                            row['harga']=harga_baru
                                                                            row['jenis_kos']=jenis_kos_baru
                                                                            row['no_hp_pemilik']=no_hp_baru
                                                                            row['ac']=ac_baru
                                                                            row['kamar_mandi_dalam']=km_baru
                                                                            row['wifi']=wifi_baru
                                                                            row['image_path']=self.image_pathht
                                                                            row["lokasi"]=lokasi_baru
                                                                with open('data_kos.csv', 'w', newline='') as file:
                                                                    kolom = ['nama','harga','jenis_kos','no_hp_pemilik','ac','kamar_mandi_dalam','wifi','image_path','kamar_dipakai','total_ketersediaan','lokasi','Username','Password','Deskripsi',"photopath1","photopath2","photopath3"]
                                                                    writer = csv.DictWriter(file, fieldnames=kolom,delimiter=";")
                                                                    writer.writeheader()
                                                                    writer.writerows(existing_data)
                                                                    showinfo("Success", "Data sudah diedit")                                                                                                           
                                                                                                                                                    
                                        else:
                                            showerror("Error","No_hp must only consist digit and len No_hp must 11-13")
                                    else:
                                        showerror("Error", " harga must be digit")                      
                            else:
                                showerror("Error","Harap masukan lokasi seusai dengan ketetapan")
                                    
                        except ValueError:
                            showerror("Error","Harap masukan lokasi seusai dengan ketetapan")
                    else:
                        showerror("Error","Entry jangan kosong")

    def aboutyohankos(self):
        try:
            self.bgmaster.destroy()
        except:
            pass
        self.menu_bar.entryconfigure("Boarding Edit", state="active")
        self.menu_bar.entryconfigure("About Yohan Kos", state="disabled")

        self.foto=Image.open("aboutyohankos.png")
        self.foto=self.foto.resize((self.screen_widthh,self.screen_heightt))
        self.photoo=ImageTk.PhotoImage(self.foto)
        self.label_background = Label(self.mmasster, image=self.photoo)
        self.label_background.pack(fill=BOTH, expand=YES)
        self.label_background.photo = self.photoo
class sign_in:
    def __init__(self, master):
        self.master = master
        self.master.title("SIGN IN")
        master.geometry("700x400+400+100")
        master.resizable(width=tk.FALSE, height=tk.FALSE)
        master.config(bg='#222328')
        # ico = Image.open('yohankos.png')
        # photoicon = ImageTk.PhotoImage(ico)
        # top.wm_iconphoto(self, photoicon)

        def on_closing():
                if askokcancel("Quit?", "Do you want to quit?"):
                    master.destroy()

        master.protocol("WM_DELETE_WINDOW", on_closing)

        self.background_image = Image.open("backgrounnew.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        bg = Label(master, image=self.background_photo)
        bg.pack()

        bglabelcheck = Label(master, bg="#f8fbfd", width=15, text="SHOW PASSWORD", font=("consolas", 8, "bold"))
        bglabelcheck.place(x=65, y=250)

        self.signinimage = Image.open("signin.jpg")
        self.signinimage = self.signinimage.resize((250, 30))
        self.signinimagephoto = ImageTk.PhotoImage(self.signinimage)
        sign_inbutton = Button(master, cursor="hand2", width=200, height=30, image=self.signinimagephoto,borderwidth=0, relief="flat", bd=0, font=("consolas", 9, 'bold'), command=self.signin)
        sign_inbutton.place(x=120, y=290)

        label1 = Label(master, text='SIGN IN WITH USERNAME', font=("consolas", 9, 'bold'), fg="#39A7FF",bg='white', relief='flat')
        label1.place(x=50, y=110)
        self.username_entry = Entry(master, relief='flat', bg="#aaaaaa", fg="black", font=("consolas", 11), width=35)
        self.username_entry.place(x=50, y=130, height=40)
        
        label2 = Label(master, text='PASSWORD', font=("consolas", 9, 'bold'), fg="black", bg='white', justify="left",relief='flat')
        label2.place(x=50, y=190)
        self.password_entry = Entry(master, show='*', relief=tk.FLAT, bg="#aaaaaa", fg="#f8fbfd",font=("consolas", 11), width=35)
        self.password_entry.place(x=50, y=210, height=40)

        bglabelcheck=Label(master, bg="#f8fbfd",width=15,text="SHOW PASSWORD", font=("consolas", 8, "bold" ))
        bglabelcheck.place(x=65, y=250)
        checkpassword = Checkbutton(master, width=0, height=0, cursor="hand2", bg="#f8fbfd",relief="flat", bd=0, selectcolor='lightgrey', command=lambda: show_pass())
        checkpassword.place(x=50, y=250)

        buttonsignup = Button(master, text="Don't have a yohankos account?", bg="#ecf4f9", cursor='hand2',relief='flat', border=0, 
                             activebackground="#eaf3f9", font=("consolas 8 bold"),
                             command=self.create_account, activeforeground="blue")
        buttonsignup.place(x=450, y=290)
        underline_canvas_ = Canvas(master, height=1, width=buttonsignup.winfo_reqwidth(), bg="#ecf4f9",highlightthickness=0)
        underline_canvas_.place(x=450, y=285 + buttonsignup.winfo_reqheight())
        underline_canvas_.create_line(0, 0, buttonsignup.winfo_reqwidth(), 0, width=2, fill="black")

        def show_pass():
            if self.password_entry.cget("show") == "":
                self.password_entry.config(show="*")
            else:
                self.password_entry.config(show="")

    def signin(self):
        global username
        global usernameeee
        usernameeee=self.username_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()   
        def validate():
            try:
                with open('datapengguna.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['Username']==username and row['Password']==password:
                            showinfo("Success", "Login successful!")
                            return True
            except FileNotFoundError:           
                showerror("Error", "Invalid username or password!")
            return False
        validation=validate()
        if validation:
            self.master.destroy()
            _top_=Tk()
            Dashboard(_top_)
            _top_.mainloop()
        else:
            showerror("Error", "Invalid username or password!")


    def create_account(self):
        self.master.withdraw()
        top_ = Toplevel()
        sign_up(top_)
        top_.mainloop()
class sign_up_pemilik:
    def __init__(self,_m_aster_):
        self._m_aster_=_m_aster_
        self._m_aster_.title("SIGN UP")
        self._m_aster_.geometry("1000x700+300+30")
        self._m_aster_.resizable(width=tk.FALSE, height=tk.FALSE)

        self.background_image2 = Image.open("register_pemilik1.png")
        self.background_photo2 = ImageTk.PhotoImage(self.background_image2)
        self.bg2 = Label(self._m_aster_, image=self.background_photo2)
        self.bg2.place(x=0,y=0)

        def _on_closing():
            try:
                self.signupframe2.destroy()
            except:
                pass
            self._m_aster_.destroy()
            to_p.deiconify()
        self._m_aster_.protocol("WM_DELETE_WINDOW", _on_closing)

        

        self.nama_entry = Entry(self._m_aster_, relief='flat', bg="#aaaaaa", fg="black", font=("consolas", 11), width=35)
        self.nama_entry.place(x=160, y=170, height=40)

        self.username_entry = Entry(self._m_aster_, relief='flat', bg="#aaaaaa", fg="black", font=("consolas", 11), width=35)
        self.username_entry.place(x=160, y=270, height=40)

        self.password_entry = Entry(self._m_aster_, show='*', relief=tk.FLAT, bg="#aaaaaa", fg="#f8fbfd",font=("consolas", 11), width=35)
        self.password_entry.place(x=160, y=390, height=40)

        self.password_entry_confirm = Entry(self._m_aster_, show='*', relief=tk.FLAT, bg="#aaaaaa", fg="#f8fbfd",font=("consolas", 11), width=35)
        self.password_entry_confirm.place(x=160, y=520, height=40)

        
        checkpassword = Button(self._m_aster_, text=" 👁️ ",relief='flat', cursor="hand2", bg="#eef8f8", bd=0,activebackground="#eef8f8", command=lambda: show_pass())
        checkpassword.place(x=450, y=390, width=40,height=40)


        self.No_HP = Entry(self._m_aster_, relief='flat', bg="#aaaaaa", fg="black", font=("consolas", 11), width=35)
        self.No_HP.place(x=665, y=170, height=40)

        infobutton12=CTkButton(self._m_aster_, text="i", command=lambda: infobuton12(), bg_color="#eef8f8", fg_color="#068FFF",corner_radius=180
                                , border_width=0, border_color="#eef8f8",width=17,height=17)
        infobutton12.place(x=640, y=180)
        def infobuton12():
                showinfo("Info","Penulisan no hp menggunakan angka saja\ncontoh: 0812276713")

        self.Harga = Entry(self._m_aster_, relief='flat', bg="#aaaaaa", fg="black", font=("consolas", 11), width=35)
        self.Harga.place(x=665, y=270, height=40)
        infobutton1=CTkButton(self._m_aster_, text="i", command=lambda: infobuton1(), bg_color="#eef8f8", fg_color="#068FFF",corner_radius=180
                                , border_width=0, border_color="#eef8f8",width=17,height=17)
        infobutton1.place(x=640, y=280)
        def infobuton1():
                showinfo("Info","Penulisan harga menggunakan angka saja")
        
        self.Jenis_Kos =  ttk.Combobox(self._m_aster_, values=["Laki Laki dan Perempuan", "Laki Laki", "Perempuan"], state="readonly")
        self.Jenis_Kos.place(x=670, y=390, height=25, width=180)

        self.Ac=StringVar()
        self.Ac_button=Radiobutton(self._m_aster_, text="YES", value="yes",variable=self.Ac,background="#eef8f8")
        self.Ac_button.place(x=670, y=520,height=30)
        self.Ac_button_=Radiobutton(self._m_aster_, text="NO", value="no", variable=self.Ac,background="#eef8f8")
        self.Ac_button_.place(x=730, y=520,height=30)
        
        self.next_slide_button = Button(self._m_aster_, text="Next Slide", relief='flat', cursor="hand2", bg="white", bd=0, activebackground="white", command=self.next_slide)
        self.next_slide_button.place(x=600, y=600, width=100, height=40)
        self.slide=0
        def show_pass():
            if self.password_entry.cget("show") == "":
                self.password_entry.config(show="*")
            else:
                self.password_entry.config(show="")
    def next_slide(self):
        if self.slide==0:
            self._m_aster_.withdraw()
            self.signupframe2=Toplevel(self._m_aster_)
            self.signupframe2.title("SIGN UP")
            self.signupframe2.geometry("1000x700+300+30")
            self.signupframe2.resizable(width=tk.FALSE, height=tk.FALSE)

            def _on_closing():
                self._m_aster_.destroy()
                self.signupframe2.destroy()
                to_p.deiconify()
            self.signupframe2.protocol("WM_DELETE_WINDOW", _on_closing)

            self.background_image3 = Image.open("register_pemilik2.png")
            self.background_photo3 = ImageTk.PhotoImage(self.background_image3)
            self.bg3 = Label(self.signupframe2, image=self.background_photo3)
            self.bg3.place(x=0,y=0)

            self.previous_button = Button(self.signupframe2, text="Previous Slide", relief='flat', cursor="hand2", bg="white", bd=0, activebackground="white", command=self.bbbb)
            self.previous_button.place(x=130, y=500, width=100, height=40)

            self.wifi=StringVar()
            self.wifi_button=Radiobutton(self.signupframe2, text="YES", value="yes",variable=self.wifi,background="#eef8f8")
            self.wifi_button.place(x=130, y=160,height=30)

            self.wifi_button_=Radiobutton(self.signupframe2, text="NO", value="no", variable=self.wifi,background="#eef8f8")
            self.wifi_button_.place(x=200, y=160,height=30)

            self.total_kamar = Entry(self.signupframe2, relief='flat', bg="#aaaaaa", fg="black", font=("consolas", 11), width=35)
            self.total_kamar.place(x=130, y=390, height=40)

            self.kapasitas_kos = Entry(self.signupframe2 ,relief='flat', bg="#aaaaaa", fg="black", font=("consolas", 11), width=35)
            self.kapasitas_kos.place(x=130, y=270, height=40)

            self.km=StringVar()
            self.km_button=Radiobutton(self.signupframe2, text="YES", value="yes",variable=self.km,background="#eef8f8")
            self.km_button.place(x=560, y=160,height=30)

            self.km_button_=Radiobutton(self.signupframe2, text="NO", value="no", variable=self.km,background="#eef8f8")
            self.km_button_.place(x=630, y=160,height=30)

            self.lokasi = Entry(self.signupframe2, relief='flat', bg="#aaaaaa", fg="black", font=("consolas", 11), width=35)
            self.lokasi.place(x=550, y=270, height=40)
            info_label4 = Button(self.signupframe2, text="📍",
            font=("Consolas", 15), bg="#eef8f8", justify=LEFT, command=self.tampilkan_lokasi, relief="flat", bd=0, activebackground="#eef8f8", cursor="hand2", fg="darkgreen")
            info_label4.place(x=845, y=270,height=40)

            infobutton=CTkButton(self.signupframe2, text="i", command=lambda: infobutton(), bg_color="#eef8f8", fg_color="#068FFF",corner_radius=180
                                    , border_width=0, border_color="#eef8f8",width=17,height=17)
            infobutton.place(x=515, y=280)
            def infobutton():
                windowww=Toplevel()
                windowww.title("SIGN UP")
                windowww.geometry("1000x700+300+30")
                windowww.resizable(width=tk.FALSE, height=tk.FALSE)
                self.background_image4 = Image.open("tutorial_lokasi.png")
                self.background_photo4 = ImageTk.PhotoImage(self.background_image4)
                self.bg4 = Label(windowww, image=self.background_photo4)
                self.bg4.place(x=0,y=0)

                
            self.upload_button = Button(self.signupframe2, text="Upload Image", relief='flat', cursor="hand2", bg="white", bd=0, activebackground="white", command=lambda: self.upload_image())
            self.upload_button.place(x=550, y=350, width=100, height=40)
            sign_inbutton=CTkButton(self.signupframe2, corner_radius=90,width=170,height=45,bg_color="#eef8f8", text="KONFIRMASI KOS", fg_color="#7492A6", state="normal", border_width=0,border_color="#7492A6",command=self.sign_up_pemilik_)
            sign_inbutton.place(x=450, y=610)
            self.slide+=1
        elif self.slide==1:
            self._m_aster_.withdraw()
            self.signupframe2.deiconify()
            self.slide=1
    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        if file_path:

            self.image_path = file_path
            image = Image.open(self.image_path)
            image=image.resize((250,150))
            photo = ImageTk.PhotoImage(image)
            self.image_label = Label(self.signupframe2, image=photo)
            self.image_label.image = photo
            self.image_label.place(x=550, y=400) 
    def bbbb(self):
        self.signupframe2.withdraw()
        self._m_aster_.deiconify()
    def tampilkan_lokasi(self):
        gmaps_url = f"https://www.google.com/maps/search/?api=1&query=-7.313153307419301, 112.72732984003206"
        webbrowser.open(gmaps_url)
    def sign_up_pemilik_(self):
        nama = self.nama_entry.get()
        Ussername = self.username_entry.get()
        password = self.password_entry.get()

        wifi = self.wifi.get()
        kapasitas_kos = self.kapasitas_kos.get()
        total_kamar = self.total_kamar.get()
        km = self.km.get()
        ac=self.Ac.get()
        harga = self.Harga.get()
        no_hp = self.No_HP.get()
        jenis_kos= self.Jenis_Kos.get()
        lokasi = self.lokasi.get()
        try:
            image_path3 = self.image_path
        except AttributeError:
            showerror("Error","upload image must be filled")
        lokassi=lokasi.split(",")
        try:
            location1=float(lokassi[0])
            location2=float(lokassi[1])

            if nama and Ussername and password and wifi and kapasitas_kos and total_kamar and km and ac and harga and no_hp and jenis_kos and lokasi and image_path3:
                if -90 <= location1 <= 90 and -180 <= location2 <= 180:
                    with open ("data_kos.csv","r") as databording:
                        databordingg=csv.DictReader(databording, delimiter=";")
                        for row in databordingg:
                            if nama.lower() == row["nama"].lower():
                                showerror("Error","Tolong masukkan nama kos yang berbeda")
                                return
                    if harga.isdigit():
                    
                        if no_hp.isdigit() and 11 <= len(no_hp) <= 13:
                            if 6 <= len(Ussername) <= 20 and 6 <= len(password) <= 20:
                                if  any(c.islower() for c in password) \
                                    and any(c.isupper() for c in password)\
                                    and any(c.isdigit() for c in password)\
                                    and any(cq.islower() for cq in Ussername) \
                                    and any(cq.isupper() for cq in Ussername):
                                    if  any(c1.islower() for c1 in nama) \
                                        and any(c1.isupper() for c1 in nama)\
                                        and not any(c1.isdigit() for c1 in nama):                     
                                        data = {'nama' : nama, 'harga' : harga, 'jenis_kos' : jenis_kos, 'no_hp_pemilik' : no_hp, 'ac' : ac, 'kamar_mandi_dalam' : km, 'wifi' :  wifi, 'image_path' : image_path3, 'kamar_dipakai' : total_kamar, 'total_ketersediaan' : kapasitas_kos, 'lokasi' : lokasi, 'Username' : Ussername, 'Password' : password}

                                        if self.password_entry.get() == self.password_entry_confirm.get():
                                            try:
                                                with open('data_kos.csv', 'r') as file:
                                                    reader = csv.DictReader(file, delimiter=";")
                                                    existing_data = list(reader)
                                            except FileNotFoundError:
                                                existing_data = []                  
                                            existing_data.append(data)
                                            try:
                                                with open('data_kos.csv', 'r') as file:
                                                    reader = csv.DictReader(file, delimiter=";")
                                                    for row in reader:
                                                        if row['Username']==Ussername and row['Password']==password:
                                                            showerror("Error","Account already exist")
                                                            return
                                                        elif not row['Username']==Ussername and not row['Password']==password:
                                                            continue
                                                    else:
                                                            with open('data_kos.csv', 'w', newline='') as file:
                                                                kolom = ['nama','harga','jenis_kos','no_hp_pemilik','ac','kamar_mandi_dalam','wifi','image_path','kamar_dipakai','total_ketersediaan','lokasi','Username','Password','Deskripsi',"photopath1","photopath2","photopath3"]
                                                                writer = csv.DictWriter(file, fieldnames=kolom,delimiter=";")
                                                                writer.writeheader()
                                                                writer.writerows(existing_data)
                                                                showinfo("Success", "Account created successfully!")
                                                                self._m_aster_.destroy()
                                                                to_p.deiconify()
                                            except FileNotFoundError:
                                                with open('data_kos.csv', 'w', newline='') as file:
                                                    kolom = ['nama','harga','jenis_kos','no_hp_pemilik','ac','kamar_mandi_dalam','wifi','image_path','kamar_dipakai','total_ketersediaan','lokasi','Username','Password','Deskripsi',"photopath1","photopath2","photopath3"]
                                                    writer = csv.DictWriter(file, fieldnames=kolom,delimiter=";")
                                                    writer.writeheader()
                                                    writer.writerows(existing_data)
                                        
                                        else:
                                            showerror("Error", "Password not valid")
                                    else:
                                        showerror("Error","Name must only consist of uppercase letters and lowercase letters")
                                else:
                                    showerror("Error","Password must consist of uppercase letters, lowercase letters, numbers and username must consist of uppercase letters dan lowercase letters ")
                            else:
                                showerror("Error", "Username must be at least 4 characters, and password must be between 6 and 20 characters.")
                        else:
                            showerror("Error","No_hp must only consist digit and len No_hp must 11-13")
                    else:
                        showerror("Error", " harga must be digit")                      
                else:
                    showerror("Error","Harap masukan lokasi seusai dengan ketetapan")
            else:
                showerror("Error", "All fields must be filled!")                        
        except ValueError:
            showerror("Error","Harap masukan lokasi seusai dengan ketetapan")     
class sign_in_pemilik:
    def __init__(self, mas_ter_):
        self.mas_ter_ = mas_ter_
        self.mas_ter_.title("Sign In")
        mas_ter_.geometry("700x400+400+100")
        mas_ter_.resizable(width=tk.FALSE, height=tk.FALSE)

        def on_closing():
                if askokcancel("Quit?", "Do you want to quit?"):
                    mas_ter_.destroy()

        mas_ter_.protocol("WM_DELETE_WINDOW", on_closing)

        self.background_image = Image.open("loginpemilik.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        bg = Label(mas_ter_, image=self.background_photo)
        bg.pack()

        bglabelcheck = Label(mas_ter_, bg="#f8fbfd", width=15, text="SHOW PASSWORD", font=("consolas", 8, "bold"))
        bglabelcheck.place(x=65, y=250)
        self.username_entry_pemilik = Entry(mas_ter_, relief=tk.FLAT, bg="#aaaaaa", fg="#f8fbfd",font=("consolas", 11), width=35)
        self.username_entry_pemilik.place(x=50, y=160,height=40)
        self.password_entry_pemilik = Entry(mas_ter_, show='*', relief=tk.FLAT, bg="#aaaaaa", fg="#f8fbfd",font=("consolas", 11), width=35)
        self.password_entry_pemilik.place(x=50, y=230, height=40)

        bglabelcheck=Label(mas_ter_, bg="#f8fbfd",fg="black",width=15,text="SHOW PASSWORD", font=("consolas", 8, "bold" ))
        bglabelcheck.place(x=90, y=280)
        checkpassword = Checkbutton(mas_ter_, width=0, height=0, cursor="hand2", bg="#f8fbfd",relief="flat", bd=0, selectcolor='lightgrey', command=lambda: show_pass())
        checkpassword.place(x=65, y=280)
        sign_inbutton=CTkButton(mas_ter_, corner_radius=90,width=100,height=45,bg_color="#e9f4fa", text="KONFIRMASI KOS", fg_color="#7492A6", state="normal", border_width=0,border_color="#7492A6",command=self.signin)
        sign_inbutton.place(x=110, y=310)
        buttonsignup = Button(mas_ter_, text="Don't have a yohankos account?", bg="white", cursor='hand2',relief='flat', border=0, 
                             activebackground="white", font=("consolas 8 bold"),
                             command=self.create_account, activeforeground="blue")
        buttonsignup.place(x=450, y=300)
        underline_canvas = Canvas(mas_ter_, height=1, width=buttonsignup.winfo_reqwidth(), bg="#ecf4f9",highlightthickness=0)
        underline_canvas.place(x=450, y=296 + buttonsignup.winfo_reqheight())
        underline_canvas.create_line(0, 0, buttonsignup.winfo_reqwidth(), 0, width=2, fill="black")
        def show_pass():
            if self.password_entry_pemilik.cget("show") == "":
                self.password_entry_pemilik.config(show="*")
            else:
                self.password_entry_pemilik.config(show="")

    def signin(self):
        global username_pemilik
        username_pemilik = self.username_entry_pemilik.get()
        password_pemilik = self.password_entry_pemilik.get()   
        def validate():
            try:
                with open('data_kos.csv', 'r') as file:
                    reader = csv.DictReader(file, delimiter=";")
                    for row in reader:
                        if row['Username']==username_pemilik and row['Password']==password_pemilik:
                            showinfo("Success", "Login successful!")
                            return True
            except FileNotFoundError:           
                showerror("Error", "Invalid username or password!")
            return False
        validation=validate()
        if validation:
            self.mas_ter_.destroy()
            _tttop_=Tk()
            Dashboard_pemilik(_tttop_)
            _tttop_.mainloop()
        else:
            showerror("Error", "Invalid username or password!")
    def create_account(self):
        self.mas_ter_.withdraw()
        _t_op_ = Toplevel()
        sign_up_pemilik(_t_op_)
        _t_op_.mainloop()
class Log_In_As:
    def __init__(self, masster):
        self.masster = masster
        self.masster.title("Yohan Kos")
        masster.geometry("700x400+400+100")
        masster.resizable(width=tk.FALSE, height=tk.FALSE)

        ico = Image.open('yohankos.png')
        photoicon = ImageTk.PhotoImage(ico)
        toppp.wm_iconphoto(self, photoicon)

        self.background_image = Image.open("Masuk ke YohanKos.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        bg = Label(masster, image=self.background_photo)
        bg.pack()

        self.buttonpenggunaimage = Image.open("butonpengguna.png")
        self.buttonpenggunaimage=self.buttonpenggunaimage.resize((350,63))
        self.background_photo_pengguna = ImageTk.PhotoImage(self.buttonpenggunaimage)
        buttonpengguna=Button(masster,image=self.background_photo_pengguna,relief="flat",bd=0,border=0, command=lambda: pengguna())
        buttonpengguna.photo=self.background_photo_pengguna
        buttonpengguna.place(x=120,y=165, width=350, height=63)

        self.buttonpemiliimage = Image.open("butonpemilik.png")
        self.buttonpemiliimage=self.buttonpemiliimage.resize((350,63))
        self.background_photo_pemilik = ImageTk.PhotoImage(self.buttonpemiliimage)
        buttonpemilik=Button(masster,image=self.background_photo_pemilik,relief="flat",bd=0,border=0, command=lambda:pemilik())
        buttonpemilik.photo=self.background_photo_pengguna
        buttonpemilik.place(x=120,y=265, width=350, height=63)  

        def pengguna():
            global top
            toppp.destroy()          
            top = tk.Tk()
            gui = sign_in(top)
            top.mainloop()
        def pemilik():
            global to_p
            toppp.destroy()
            to_p=tk.Tk()
            sign_in_pemilik(to_p)
            to_p.mainloop()
            
toppp = tk.Tk()
gui = Log_In_As(toppp)
toppp.mainloop()


