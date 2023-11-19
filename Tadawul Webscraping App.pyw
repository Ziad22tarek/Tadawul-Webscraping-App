import customtkinter
import tkinter 
from tkinter import messagebox
from threading import Thread
import datetime
from utilities.scrollbar import scrollbar
from utilities.download_pdf import download_pdf
from tadawul.add_Tadawul_data import add_Tadawul_data
from tadawul.get_tadawul_pdf_links import get_tadawul_pdf_links
from utilities.ChecklistCombobox import ChecklistCombobox

def select():
    try:
        global pdf_dic
        select_buttom.configure(state=tkinter.DISABLED,text='Extracting..')
        pdf_type=[]
        weekly=Weekly_option.get()
        monthly=Monthly_option.get()
        if weekly!='Off':
            pdf_type.append(weekly)
        if monthly!='Off':
            pdf_type.append(monthly)
        

        if isinstance(year_dropdown.get(),str):
            if year_dropdown.get().strip()!='':
                years=year_dropdown.get()
                years=[years]
                
        else:
            years=year_dropdown.get()
        years=[int(i) for i in years]

        if isinstance(month_dropdown.get(),str):
            if month_dropdown.get().strip()!='':
                months=month_dropdown.get()
                months=[months]
            else:
                months=list(range(1,13))
                
        else:
            months=month_dropdown.get()
        
        months=[int(i) for i in months]        

        if len(pdf_type)==0:
            messagebox.showerror('Error',"Please Select the Data Type")

        if len(years)==0:
            messagebox.showerror('Error',"Please Select the PUBLICATION YEAR".title())


        pdf_dic=get_tadawul_pdf_links(pdf_type,years,months)
        
      


    except: 
        messagebox.showerror('Error',"Failed to connect with the server Please try again!".title())


def run_get_reports_name():
        thread=Thread(target=select)
        thread.start()
        return thread
    
        
def create_CB(thread):
    global cb
    if thread.is_alive():
        root.after(1000, lambda: create_CB(thread))
    else:
        select_buttom.configure(state=tkinter.NORMAL,text='Select')
        cb = ChecklistCombobox(PDF_frame,state='readonly',values=list(pdf_dic.keys()))
        cb.place(anchor='w',relx=0.05,rely=0.6,relwidth=0.75)

def get_pdf_names():
    thread=run_get_reports_name()
    if thread.is_alive():
        root.after(1000, lambda: create_CB(thread))


def excute():
    try:
        #disable the run buttom
        Run_buttom.configure(state=tkinter.DISABLED)
        
        #get the starting time
        my_progress=customtkinter.CTkProgressBar(main_frame,
                                                    orientation=tkinter.HORIZONTAL,
                                                    corner_radius=30,
                                                    fg_color='#dfdfdf',
                                                    progress_color='black'
                                                    )
        my_progress.place(anchor='w',relx=0.32,rely=0.85)
        my_progress.set(.05)
        pdf_path=r'.\Tadawul Reports'
        my_progress.set(.15)
        
        
        
        pdf_list=cb.get()
        if isinstance(pdf_list,str):
            if pdf_list.strip()!='':
                pdf_list=[pdf_list]
            else:
                messagebox.showerror('Error',"Please Select The Report Name".title())
        
        progress_num=(70/len(pdf_list))/100
        progress_amount=progress_num
        for pdf in pdf_list:
            download_pdf(pdf_dic[pdf],pdf_path+'\\'+pdf)
            add_Tadawul_data(pdf+'.pdf')
            my_progress.set(0.2+progress_amount)
            progress_amount=progress_amount+progress_num

        
            
        #Set the progress bar to 100%
        my_progress.set(1)
        #destroy the progerss bar
        my_progress.destroy()
        Run_buttom.configure(state=tkinter.NORMAL)
        
    except:
        Run_buttom.configure(state=tkinter.NORMAL)
        my_progress.destroy()
        messagebox.showerror('Error',"Something is wrong. Please contact the specialist")
        








def run_excute():
    thread=Thread(target=excute)
    thread.start() 



# set the appearnace mode and the color them
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme('dark-blue')



# create the root and its settings
root = customtkinter.CTk()
root.title('Tadawul Webscraping App')
root.iconbitmap(r'.\assest_files\icon.ico') 
root.configure(bg='white')
screen_width=root.winfo_screenwidth()*0.6
screen_height=root.winfo_screenheight()*0.8
root.geometry(f'{int(screen_width)}x{int(screen_height)}')
root.resizable(True,True)



title_frame=customtkinter.CTkFrame(root,height=screen_height*0.15,fg_color='black')
title_frame.pack(fill=tkinter.BOTH,expand=1)
title_frame.pack_propagate(0)
company_label=customtkinter.CTkLabel(title_frame,
                                            text='Tadawul Webscraping App',
                                            text_color='white',
                                            fg_color='black',
                                            font=("Poppins", 18,'bold'))
company_label.pack(side='top',anchor='nw',padx=10,pady=15)


title_Label=customtkinter.CTkLabel(title_frame
                                    ,text='Powered by Discover Data Team',
                                    text_color='white',
                                    font=("Poppins", 10),
                                    corner_radius=5)
title_Label.place(anchor='sw',relx=0.8,rely=0.9)

#main frame
main_frame=customtkinter.CTkFrame(root,fg_color='white',width=600,height=720)
main_frame.pack(fill=tkinter.BOTH,expand=1)
main_frame.pack_propagate(0)


my_canvas = scrollbar(main_frame)
second_frame = customtkinter.CTkFrame(my_canvas,
                                            width=screen_width,
                                            height=screen_height*0.8,
                                            fg_color='white')
    
my_canvas.create_window((0, 0), window=second_frame, anchor='nw')


data_type_frame=customtkinter.CTkFrame(second_frame,
                                        border_width=2,
                                        border_color='#dfdfdf',
                                        corner_radius=20,
                                        fg_color='white')


data_type_frame.place(anchor='w',relx=0.01,rely=0.33,relwidth=0.35,relheight=0.6)

data_type_label=customtkinter.CTkLabel(data_type_frame,
                                    text='Data Type',
                                    fg_color='white',
                                    text_color='black',
                                    corner_radius=0,
                                    font=("Poppins", 13,"bold"))

data_type_label.place(anchor='w',relx=0.05,rely=0.1)

data_type_Option=['Monthly','Weekly']

Monthly_option=customtkinter.CTkCheckBox(data_type_frame,
                                text='Monthly',
                                onvalue='Monthly',
                                offvalue='Off',
                                corner_radius=20,
                                border_width=2,
                                bg_color='white',
                                border_color='black',
                                checkbox_width=18,
                                checkbox_height=18,
                                text_color='black',
                                font=("Poppins", 12),
                                fg_color='black')
    
Monthly_option.place(anchor='w',relx=0.05,rely=0.2)

Weekly_option=customtkinter.CTkCheckBox(data_type_frame,
                                text='Weekly',
                                onvalue='Weekly',
                                offvalue='Off',
                                corner_radius=20,
                                border_width=2,
                                bg_color='white',
                                border_color='black',
                                checkbox_width=18,
                                checkbox_height=18,
                                text_color='black',
                                font=("Poppins", 12),
                                fg_color='black')


Weekly_option.place(anchor='w',relx=0.4,rely=0.2)

latest_year=datetime.datetime.today()
latest_year=latest_year.year
year_list=list(range(2015,latest_year+1))
year_list.sort(reverse=True)
year_list=[str(i) for i in year_list]
year_label=customtkinter.CTkLabel(data_type_frame,
                                    text='SELECT PUBLICATION YEAR'.title(),
                                    fg_color='white',
                                    text_color='black',
                                    width=.05,
                                    height=.05,
                                    corner_radius=0,
                                    font=("Poppins", 14,"bold"))

year_label.place(anchor='w',relx=0.05,rely=0.4)



year_dropdown=ChecklistCombobox(data_type_frame,state='readonly',values=year_list)
year_dropdown.place(anchor='w',relx=0.05,rely=0.5,relwidth=0.7)



month_label=customtkinter.CTkLabel(data_type_frame,
                                    text='SELECT PUBLICATION Month (Optional)'.title(),
                                    fg_color='white',
                                    text_color='black',
                                    width=.05,
                                    height=.05,
                                    corner_radius=0,
                                    font=("Poppins", 14,"bold"))

month_label.place(anchor='w',relx=0.05,rely=0.65)
month_list=[str(int(i)) for i in range(1,13)]
month_dropdown=ChecklistCombobox(data_type_frame,state='readonly',values=month_list)
month_dropdown.place(anchor='w',relx=0.05,rely=0.75,relwidth=0.7)


select_buttom=customtkinter.CTkButton(data_type_frame,
                                            text='Select',
                                            fg_color='black',
                                            text_color='white',
                                            corner_radius=20,
                                            font=("Poppins", 10,'bold'),
                                            command=lambda:get_pdf_names()
                                            )
select_buttom.place(relx=.4,rely=0.9,relwidth=0.25,relheight=0.07,anchor='w')

PDF_frame=customtkinter.CTkFrame(second_frame,
                               
                                border_width=2,
                                border_color='#dfdfdf',
                                corner_radius=20,
                                fg_color='white')
PDF_frame.place(anchor='w',relx=0.38,rely=0.11,relwidth=0.5,relheight=0.15)
PDF_Label=customtkinter.CTkLabel(PDF_frame,
                                    text='PDF Name :',
                                    fg_color='white',
                                    text_color='black',

                                    corner_radius=0,
                                    font=("Poppins", 14,"bold"))

PDF_Label.place(anchor='w',relx=.05,rely=.30)


cb = ChecklistCombobox(PDF_frame,state='readonly')
cb.place(anchor='w',relx=0.05,rely=0.6,relwidth=0.75)



Run_buttom=customtkinter.CTkButton(second_frame,
                                            text='Run',
                                            fg_color='black',
                                            text_color='white',
                                            corner_radius=40,
                                            font=("Poppins", 10,'bold'),
                                            command=lambda:run_excute() 
                                            )

Run_buttom.place(relx=0.35,rely=0.8,anchor='w')




root.mainloop()
