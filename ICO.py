from tkinter import *
from PIL import ImageTk
from PIL import *
import imageio,os
import tkinter.filedialog
from PIL import Image
from tkinter.filedialog import asksaveasfile 
from tkinter import filedialog
import random
from tkinter.filedialog import asksaveasfile 


class ICO:
    def __init__(self,root):
        self.root=root
        self.root.title("ICO CONVERTER")
        self.root.geometry("400x200")
        self.root.iconbitmap("logos.ico")
        self.root.resizable(0,0)

             
        def on_enter1(e):
            But_load_file['background']="black"
            But_load_file['foreground']="cyan"
            
            

        def on_leave1(e):
            But_load_file['background']="SystemButtonFace"
            But_load_file['foreground']="SystemButtonText"


        def on_enter2(e):
            But_Save_file['background']="black"
            But_Save_file['foreground']="cyan"
            
            

        def on_leave2(e):
            But_Save_file['background']="SystemButtonFace"
            But_Save_file['foreground']="SystemButtonText"



        def convert_ico():
            global filename
            file_path = filedialog.askopenfilename(title = "Select file",filetypes = (("png files","*.png"),("all files","*.*"))) 
            filename = file_path
            Lab_select.config(text="file is selected")
            self.root.update()
            return filename
##            img = Image.open(filename)
##            icon_sizes = [(128, 128)]
                      
            #img.save('logo{}.ico'.format(ra))
                        
              
            

        def save_as():
            try:
                
                 Lab_select.config(text="Successfully converted")
                 self.root.update()
                 img = imageio.imread(filename)
                 ra=random.randint(1,1111)
                 imgs=imageio.imwrite('logo{}.ico'.format(ra), img)
            except:
                pass
                
            



#=======================================================================
        MainFrame=Frame(self.root,width=400,height=200,relief="sunken",bd=3)
        MainFrame.place(x=0,y=0)

        self.original1 = Image.open ("C:\\Users\\SHREYAS\\Desktop\\shreyas python\\ico_converter\\icos.png")
        resized1 = self.original1.resize((330, 80),Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(resized1)
        bglab1=Label(MainFrame,image=self.image1,bd=1).place(x=0,y=0)


        Lab_select=Label(MainFrame,text="Select the file",font=('times new roman',12,"bold"))
        Lab_select.place(x=140,y=60)


        But_load_file=Button(MainFrame,text="Open File only png",command=convert_ico,width=15,font=('times new roman',12,'bold'),bd=3,cursor="hand2")
        But_load_file.place(x=30,y=120)
        But_load_file.bind("<Enter>",on_enter1)
        But_load_file.bind("<Leave>",on_leave1)


        But_Save_file=Button(MainFrame,text="Convert Ico",command = lambda : save_as(),width=15,font=('times new roman',12,'bold'),bd=3,cursor="hand2")
        But_Save_file.place(x=220,y=120)
        But_Save_file.bind("<Enter>",on_enter2)
        But_Save_file.bind("<Leave>",on_leave2)





#=======================================================================




if __name__ == "__main__":
    root=Tk()
    app=ICO(root)
    root.mainloop()
