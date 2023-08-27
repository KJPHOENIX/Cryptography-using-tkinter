import tkinter
from tkinter import *
from tkinter import messagebox
import base64



r = Tk()
r.title("Cryptography")
r.config(bg = "lightgreen")
r.geometry("400x450")


Msg = StringVar() 
key = StringVar() 
mode = StringVar() 
Result = StringVar() 






h1 = Label(r,text = "Encryption and Decryption" ,font = ("optima",12,"bold"),bg = "yellow")
h1.place( x = 100 , y = 50)

l1 =  Label(r,text = "Enter your message :",font = ("optima",10),bd = 5,bg = "lightgreen")
l1.place(x = 20, y = 100)

e1 = Entry(r,textvariable = Msg,justify = "right",bd = 5,width =30,bg ="skyblue",font = ("optima",10))
e1.place(x = 170 , y = 100)

l2 = Label(r,text = "Enter the key :",font = ("optima",10),bd = 5,bg = "lightgreen")
l2.place(x = 20 , y = 150)

e2 = Entry(r,textvariable = key,justify = "right",bd = 5,width = 30,bg ="skyblue",font = ("optima",10))
e2.place(x = 170 , y = 150)

l3 = Label(r, font = ("optima",10), text = "e-encrypt, d-decrypt :",bd = 5,bg = "lightgreen") 
l3.place(x = 20, y= 200)

e3 = Entry(r, font = ('optima',10), textvariable = mode, justify = 'right',bd = 5,width = 30,bg ="skyblue",) 
e3.place(x = 170 , y = 200) 

l4 = Label(r,text = "Result :",font = ("optima",10),bd = 5,bg = "lightgreen")
l4.place(x = 20,y = 250)

e4 = Entry(r,textvariable = Result,bd = 5,width = 30,bg ="skyblue",font = ("optima",10))
e4.place(x = 170,y = 250)




def encode(key, clear): 
	enc = [] 

	for i in range(len(clear)): 
		key_c = key[i % len(key)] 
		enc_c = chr((ord(clear[i]) +ord(key_c)) % 256)
		enc.append(enc_c) 
	return base64.urlsafe_b64encode("".join(enc).encode()).decode() 


def decode(key, enc): 
	dec = [] 

	enc = base64.urlsafe_b64decode(enc).decode() 
	for i in range(len(enc)): 
		key_c = key[i % len(key)] 
		dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
		dec.append(dec_c) 
	return "".join(dec) 


def Ref(): 
	print("Message= ", (Msg.get())) 

	clear = Msg.get() 
	k = key.get() 
	m = mode.get() 

	if (m == 'e'): 
		Result.set(encode(k, clear)) 
	else: 
		Result.set(decode(k, clear))

def Reset(): 
	#rand.set("") 
	Msg.set("") 
	key.set("") 
	mode.set("") 
	Result.set("")

def qExit(): 
	r.destroy() 


b1 = Button(r,text = "Show message",font = ("optima",10),command = Ref,activebackground = "red",activeforeground = "white",bg = "yellow")
b1.place(x = 20, y = 330)

b2 = Button(r,text = "Reset",font = ("optima",10),command = Reset,activebackground = "red",activeforeground = "white",bg = "yellow")
b2.place(x = 170, y = 330)

b3 = Button(r,text = "Quit",font = ("optima",10),command = qExit,activebackground = "red",activeforeground = "white",bg = "yellow")
b3.place(x = 230,y = 330)

banner = Label(r,text = "KJPHOENIX",font = ("optima",12,"bold"),bg = "white")
banner.place(x=150,y =380)




r.mainloop()
