import customtkinter
import tkinter












def  scrollbar(frame):

    

    my_canvas=tkinter.Canvas(frame,bg='white')
    my_canvas.pack(side=tkinter.LEFT,fill=tkinter.BOTH,expand=1)
    my_scroolbar=customtkinter.CTkScrollbar(frame,
                                            orientation="vertical",
                                            button_color='black',
                                            fg_color='white',
                                            button_hover_color='#528AAE',
                                            hover=True,
                                            command=my_canvas.yview
                                            )
    my_scroolbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
    my_canvas.configure(yscrollcommand=my_scroolbar.set)
    my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox('all')))
    


    return my_canvas
