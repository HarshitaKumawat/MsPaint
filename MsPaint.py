from tkinter import *
from tkinter import Scale
from tkinter import colorchooser,filedialog,messagebox
import PIL.ImageGrab as ImageGrab
window = Tk()
window .state("zoomed")
window.title("Paint Application")

#variable
pen_color="black"
eraser_color="white"
#Canvas

canvas=Canvas(window,bg="white",bd=5,relief=GROOVE,height=600,width=1325)
canvas.place(x=10,y=100)

#Function


def canvas_color():
    color=colorchooser.askcolor()
    canvas.configure(bg=color[1])
    eraser_color=color[1]
def Save():
    file_name = filedialog.asksaveasfilename(defaultextension=".jpg")
    x=window.winfo_rootx()+canvas.winfo_x()
    y=window.winfo_rooty()+canvas.winfo_y()


    x1=x+canvas.winfo_width()
    y1=y+canvas.winfo_width()

    ImageGrab.grab().crop((x,y,x1,y1)).save(file_name)
    messagebox.showinfo("paint notification","Image is saved as "+str(file_name))

    
def Eraser():
    global pen_color
    pen_color=eraser_color
def Clear():
    canvas.delete("all")
def paint(event):
    x1,y1=(event.x-2),(event.y-2)
    x2,y2 = (event.x+2),(event.y+2)
    canvas.create_oval(x1,y1,x2,y2,fill=pen_color,outline=pen_color,width=pen_size.get())
canvas.bind("<B1-Motion>",paint) 
    
#Frame
color_frame = LabelFrame(window,text="Color",relief = RIDGE,bg="white",font = ("arial",15,"bold"))
color_frame.place(x=10,y=10,width = 600 , height = 60)

tool_frame = LabelFrame(window,text="Tool",relief = RIDGE,bg="white",font = ("arial",15,"bold"))
tool_frame.place(x=620,y=10,width = 300, height = 60)

pen_size= LabelFrame(window,text="Size",relief = RIDGE,bg="white",font = ("arial",15,"bold"))
pen_size.place(x=950,y=10,width = 400, height = 70)


 #color
 #	White	Silver Gray Black Red	Maroon	Yellow Olive Lime Green Aqua Teal Blue Navy Fuchsia Purple
colors = ["#FFFFFF","#C0C0C0","#C0C0C0","#808080","#000000","#FF0000","#800000","#FFFF00","#808000","#00FF00","#008000","#00FFFF","#008080","#0000FF","#000080","#FF00FF","#800080"]
 
 #Button
i = j = 0
for color in colors:
    Button(color_frame,bd = 3,bg = color,relief=RIDGE,width=3).grid(row=j,column=i,padx = 1)
    i = i+1

#Tool_Button
canvas_color_b1 = Button(tool_frame,text ="Canvas",bd=4,bg="white",command=canvas_color,relief=RIDGE)
canvas_color_b1.grid(row=0,column = 0,padx=3)

save_b2 = Button(tool_frame,text = "Save",bd=4,bg="white",command=Save,relief=RIDGE)
save_b2.grid(row=0,column=1,padx=3)

eraser_b3 = Button(tool_frame,text = "Eraser",bd=4,bg="white",command=Eraser,relief=RIDGE)
eraser_b3.grid(row=0,column=2,padx=3)

clear_b4 = Button(tool_frame,text="Clear",bd=4,bg="white",command=Clear,relief=RIDGE)
clear_b4.grid(row=0,column=3,padx=3)

#pen and eraser Size

pen_size= Scale(pen_size,orient=HORIZONTAL,from_=0,to=50,length=170)
pen_size.set(1)
pen_size.grid(row=0,column=0)

window.mainloop()