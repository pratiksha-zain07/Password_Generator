import random
import tkinter

main_window=tkinter.Tk()
main_window.title("Password Gnerator")
main_window.geometry('500x300')

padd = 200
main_window['padx'] = padd
chk1=tkinter.IntVar()
chk2=tkinter.IntVar()
chk3=tkinter.IntVar()

def password_generate(length):
    valid_char= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#&*_"
    password= "".join(random.sample(valid_char, length))
    display_result.delete(0,tkinter.END)
    display_result.insert(0,password)

def checkbox_check():
    if chk1.get()==6:
        password_generate(6)
    elif chk2.get()==10:
        password_generate(10)
    elif chk3.get()==12:
        password_generate(12)
    else:
        password_generate(8)


title_text=tkinter.Label(text='Password Generator')
title_text.grid(padx=(0,0), pady=(30,0))
display_result=tkinter.Entry()
display_result.grid(padx=(0,0), pady=(10,0))

chkone=tkinter.Checkbutton(text='8 Character', onvalue= 8,  offvalue= 0 , variable=chk1)
chkone.grid(padx=(0,0), pady=(10,0))

chktwo=tkinter.Checkbutton(text='10 Character', onvalue= 10 , offvalue= 0 , variable=chk2)
chktwo.grid(padx=(0,0), pady=(10,0))

chkthree=tkinter.Checkbutton( text= '12 Character', onvalue=12, offvalue=0 , variable=chk3)
chkthree.grid(padx=(0,0), pady=(10,0))

pass_generate = tkinter.Button(text = 'Generate', command=checkbox_check)
pass_generate.grid(padx=(0,0), pady=(30,0))
main_window.mainloop()
