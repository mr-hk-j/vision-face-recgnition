
import sys
import back as bk

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import newvision_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    newvision_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    newvision_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:

    def __init__(self, top=None):
        x = IntVar()

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font12 = "-family {Colonna MT} -size 48 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font18 = "-family {Colonna MT} -size 17 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font19 = "-family {Segoe UI} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font20 = "-family {Bookman Old Style} -size 13 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"

        top.geometry("408x495")
        top.title("VISION")
        top.configure(background="#d9d9d9")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.02)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#333333")
        self.Frame1.configure(width=415)

        self.Button1 = Button(self.Frame1,command=lambda :bk.trainer(x.get()))
        self.Button1.place(relx=0.07, rely=0.69, height=54, width=107)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Trainer''')
        self.Button1.configure(width=107)

        self.Button1_1 = Button(self.Frame1,command=lambda :bk.attendance())
        self.Button1_1.place(relx=0.7, rely=0.69, height=54, width=107)
        self.Button1_1.configure(activebackground="#d9d9d9")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#d9d9d9")
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Realtime Monitor''')

        self.Button1_2 = Button(self.Frame1,command=lambda :bk.snap())
        self.Button1_2.place(relx=0.39, rely=0.69, height=54, width=107)
        self.Button1_2.configure(activebackground="#d9d9d9")
        self.Button1_2.configure(activeforeground="#000000")
        self.Button1_2.configure(background="#d9d9d9")
        self.Button1_2.configure(disabledforeground="#a3a3a3")
        self.Button1_2.configure(foreground="#000000")
        self.Button1_2.configure(highlightbackground="#d9d9d9")
        self.Button1_2.configure(highlightcolor="black")
        self.Button1_2.configure(pady="0")
        self.Button1_2.configure(text='''Snap''')

        self.Message1 = Message(self.Frame1)
        self.Message1.place(relx=0.07, rely=0.55, relheight=0.11, relwidth=0.89)
        self.Message1.configure(background="#333333")
        self.Message1.configure(font=font20)
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text="Hello")
        self.Message1.configure(width=370)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.12, rely=0.2, height=101, width=334)
        self.Label1.configure(background="#333333")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font12)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Vision''')
        self.Label1.configure(width=334)

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.02, rely=0.44, height=31, width=394)
        self.Label2.configure(background="#333333")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font18)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Face Recognition Attendance System''')
        self.Label2.configure(width=394)

        self.Entry1 = Entry(self.Frame1)
        self.Entry1.place(relx=0.12, rely=0.83,height=20, relwidth=0.11)
        self.Entry1.configure(textvariable=x)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=44)

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.07, rely=0.83, height=23, width=24)
        self.Label3.configure(background="#333333")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font19)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''ID:''')

        self.Button1_3 = Button(self.Frame1,command=lambda :bk.report())
        self.Button1_3.place(relx=0.39, rely=0.83, height=54, width=107)
        self.Button1_3.configure(activebackground="#d9d9d9")
        self.Button1_3.configure(activeforeground="#000000")
        self.Button1_3.configure(background="#d9d9d9")
        self.Button1_3.configure(disabledforeground="#a3a3a3")
        self.Button1_3.configure(foreground="#000000")
        self.Button1_3.configure(highlightbackground="#d9d9d9")
        self.Button1_3.configure(highlightcolor="black")
        self.Button1_3.configure(pady="0")
        self.Button1_3.configure(text='''Open Report''')


        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.7, rely=0.95, height=21, width=114)
        self.Label4.configure(background="#333333")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''©Harikrishnan_J''')
        self.Label4.configure(width=114)






if __name__ == '__main__':
    vp_start_gui()



