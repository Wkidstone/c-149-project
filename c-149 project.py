from tkinter import *
import random
root=Tk()
root.title("Random word generator")
root.geometry("800x500")

r_w=Label(root)
def rwg():
    alpha_list=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    random_no1= random.randint(1,26)
    random_no2= random.randint(6,10)
    random_no3= random.randint(3,20)
    random_no4= random.randint(12,26)
    random_no5= random.randint(4,26)

    random_alpha1= alpha_list[random_no1]
    random_alpha2= alpha_list[random_no2]
    random_alpha3= alpha_list[random_no3]
    random_alpha4= alpha_list[random_no4]
    random_alpha5= alpha_list[random_no5]

    r_w["text"] =  random_alpha1 + random_alpha2 + random_alpha3 + random_alpha4 + random_alpha5

btn=Button(root, text= "Generate random word", command = rwg)
btn.place(relx=0.5,rely=0.4, anchor = CENTER)
r_w.place(relx=0.5,rely=0.5, anchor = CENTER)

root.mainloop()