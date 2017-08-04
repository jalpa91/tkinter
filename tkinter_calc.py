#========================== Notpad using Tkinter Assignment ==============================##

## DATE : 11/16/2016
## STUDENT NAME : Jalpa S.
## ASSIGNMENT NO # 5

##============================================================================##

## imports all the features of tkinter

from tkinter import *
from tkinter import messagebox as tkMessageBox
from tkinter import filedialog as tkFileDialog
from tkinter import  simpledialog as tkSimpleDialog
import os               # import os for os related functions
import random

root =Tk()                           # creates the window
root.geometry("651x481+51+51")       #dimensions of the window
root.title("Tkinter Notepad")        #name of window

## Create Label for four side of window

label1=Label(root,bg="grey",height=60,width=100)
label1.pack(side=TOP,expand=NO, fill=X)
mp=PhotoImage(file='C:\\Users\\Nirjalpa\\Downloads\\jns.GIF')
label1.config(image=mp)

label2=Label(root,bg="grey" , height=800 , width=2)
label2.pack(side=LEFT,expand=NO, fill=Y)


label3=Label(root,bg="black",height=1,width=1200)
label3.pack(side=BOTTOM, expand=NO, fill=X )


label4=Label(root,bg="grey",height=800,width=2)
label4.pack(side=RIGHT,expand=NO, fill=Y)

## Create textpad for notepad

textPad=Text(root,undo=TRUE, bg='pink',padx=10,pady=10)
textPad.pack(expand=YES,fill=BOTH)

## craete function for smart calculator

def jalpa():
    label=Label(textPad,text= "Enter your expresion")
    label.pack()
    def evaluate(event):
        
        data=e.get()
        ans.configure(text='Answer = '+ str(eval(data)))
    
    e=Entry(textPad)
    e.bind('<Return>',evaluate)
    e.pack()

    ans=Label(textPad)
    ans.pack()
    return jalpa
b1= Button(label3,text='Smart calculator',command=jalpa)
b1.pack()

## create a function for about menu

def who_created():
    lb=Listbox(textPad,height=7,width=200)
    lb.pack()
    lb.insert(END,"This window is created by JALPA SUTHAR")
    lb.insert(END,"Student Of International Technological University")
    lb.insert(END,"Student ID number : 92205")
    lb.insert(END,"Created DATE : 11/1/2016")
    lb.insert(END,"Created TIME : 11:59 PM")
    lb.insert(END,"Version: Python 3.5.2 |Anaconda 4.2.0 (64-bit)")
    lb.insert(END,k)

## create function for file menu
#the new function  
def new_file():
    # the ok cancel function of the messagebox
    if tkMessageBox.askokcancel("Save","Do you want to save current file"):
        root.title("CS 520")
    global filename
    filename = None 
    textPad.delete(1.0,END)

#the open function
def open_file():
    global filename
    filename=tkFileDialog.askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
    if filename=='':
        filename=None;
    else:
        root.title(os.path.basename(filename)+" -TextEditor")
        textPad.delete(1.0,END)
        fh=open(filename,"r")
        textPad.insert(1.0,fh.read())
        fh.close()

#the save function
def save():
    global filename
    try:
        f=open(filename,'w')
        letter = textPad.get(1.0, 'end')
        f.write(letter)
        f.close()
    except:
        save_as()

#the saveas function
def save_as():

    try:
        f=tkFileDialog.asksaveasfilename(**textPad.file_opt)
        fh = open(f, 'w')
        textoutput = textPad.get(1.0, END)
        fh.write(textoutput)
        fh.close()
        root.title(os.path.basename(f))
    except:
        pass

#the exit function
def exit_editor(event=None):
    if tkMessageBox.askokcancel("quit","Do you Want to quit?"):
        root.destroy()
    root.protocol('WM_DELETE_WINDOW', exit_command) # override close

## create a function for formula menu

# The addition function
def add_function():
    value1= tkSimpleDialog.askinteger('Value1','Enter 1st value')
    value2= tkSimpleDialog.askinteger('Value2','Enter 2nd value')
    total = value1+value2
    output = ' Your total is  %d'  %(total)
    tkMessageBox.showinfo('result',output)

# the subtraction function
def sub_function():
    value1= tkSimpleDialog.askinteger('Value1','Enter 1st value')
    value2= tkSimpleDialog.askinteger('Value2','Enter 2nd value')
    total = value1-value2
    output = ' Your total is  %d'  %(total)
    tkMessageBox.showinfo('result',output)

#The multiplication function
def multi_function():
    value1= tkSimpleDialog.askinteger('Value1','Enter 1st value')
    value2= tkSimpleDialog.askinteger('Value2','Enter 2nd value')
    total = value1*value2
    output = ' Your total is  %d'  %(total)
    tkMessageBox.showinfo('result',output)

# The division function    
def div_function():
    value1= tkSimpleDialog.askinteger('Value1','Enter 1st value')
    value2= tkSimpleDialog.askinteger('Value2','Enter 2nd value')
    total = value1//value2
    k = textPad.get(1.0, 'end')
    output = ' Your total is  %d'  %(total)
    tkMessageBox.showinfo('result',output)

    
# create a function for encryption & decryption

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' +\
        'abcdefghijklmnopqrstuvwxyz'+\
        '0123456789' + \
        ':.;,?!@#$%&()+=-*/_<> []{}`~^"\'\\'

lockkey = None
encrypted = None
decrypted = None

def generate_key():
    """Generate an key for our cipher"""
    shuffled = sorted(chars, key=lambda k: random.random())
    global lockkey
    lockkey = dict(zip(chars, shuffled))
    return lockkey

def encrypt(key, plaintext):
    """Encrypt the string and return the ciphertext"""
    convert = []
    for i in plaintext:
        if i in '\n':
            pass
        else:
           convert.append(key[i])
    encrypted = ''.join(convert)
    return encrypted
    

def decrypt(ciphertext):
    """Decrypt the string and return the plaintext"""
    key = lockkey
    flipped = {v: k for k, v in key.items()}
    converted = []
    for l in ciphertext:
        converted.append(flipped[l])
    decrypted = ''.join(converted)
    return decrypted

def enc(plaintext):
    """Generate a resulting cipher with elements shown"""
    lockkey = generate_key()
    global encrypted
    encrypted = encrypt(lockkey, plaintext)
    return "Encrypted : " + encrypted  

def dec(encrypted):
    """Generate a resulting decrypted val with elements shown"""
    decrypted = decrypt(encrypted)
    return "Decryption : " + decrypted + " \n of Encrypted Value: " +  encrypted 

def encButton():
    plainttext = textPad.get(1.0,'end')
    result = enc(plainttext)
    tkMessageBox.showinfo('result',result)

def decButton():
    plainttext = textPad.get(1.0,'end')
    result = dec(encrypted)
    tkMessageBox.showinfo('result',result)
    



    
clrschms = {
'1.  White': '000000.FFFFFF',
'2.  Grey': '83406A.D1D4D1',
'3.  Lavender': '202B4B.E1E1FF' ,
'4. Aquamarine': '5B8340.D1E7E0',
'5.  Beige': '4B4620.FFF0E1',
'6.  Blue': 'ffffBB.3333aa',
'7.  Green': 'D1E7E0.5B8340',
}

#the theme function
def theme():
    global bgc,fgc
    
    val = themechoice.get()
    clrs = clrschms.get(val)
    fgc,bgc = clrs.split('.')
    fgc, bgc = '#'+fgc, '#'+bgc
    textPad.config(bg=bgc, fg=fgc)


## create a Menubar
menubar=Menu(root)

#The file menu
filemenu=Menu(menubar,tearoff=1)
filemenu.add_command(label="New",accelerator="Ctrl+N", command=new_file)
filemenu.add_command(label="Open",accelerator="Ctrl+O", command=open_file)
filemenu.add_command(label="Save",accelerator="Ctrl+S", command=save)
filemenu.add_command(label="Save As",accelerator="Shift+Ctrl+S", command=save_as)
filemenu.add_separator()
filemenu.add_command(label="exit",accelerator="Alt+F4", command=exit_editor)
menubar.add_cascade(label="File",menu=filemenu)

#the formula menu
formulamenu=Menu(menubar,tearoff=1)
menubar.add_cascade(label="formula",menu=formulamenu)
formulamenu.add_command(label='Addition',command=add_function)
formulamenu.add_command(label='Sabtraction',command=sub_function)
formulamenu.add_command(label='Multiplication',command=multi_function)
formulamenu.add_command(label='Division',command=div_function)

#the encrypt & decrypt menu
encryptermenu=Menu(menubar,tearoff=1)
menubar.add_cascade(label='Encypter',menu=encryptermenu)
encryptermenu.add_command(label='encryption',command=encButton)
encryptermenu.add_command(label='decryption', command=decButton)

#The colour menu
colourmenu=Menu(menubar,tearoff=1)
menubar.add_cascade(label="Colour",menu=colourmenu)

thememenu=Menu(colourmenu)
themechoice= StringVar()
colourmenu.add_cascade(label='background colour',menu=thememenu)

for k in sorted(clrschms):
    thememenu.add_radiobutton(label=k, variable=themechoice,command=theme)

#the about menu
aboutmenu=Menu(menubar,tearoff=1)
aboutmenu.add_command(label='Who created',command=who_created)
menubar.add_cascade(label="About",menu=aboutmenu)



root.config(menu=menubar)

root.mainloop()

