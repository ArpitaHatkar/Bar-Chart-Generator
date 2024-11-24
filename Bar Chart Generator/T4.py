from tkinter import*
from tkinter.messagebox import*
import matplotlib.pyplot as plt
from re import*

root = Tk()
root.title("Bar Chart Generator")
root.geometry("2000x1000+500+400")
root.configure(bg="#c99789")
f = ("Times New Roman", 40, "bold")

lab_name = Label(root, text="Enter Name", font=f,  bg="#c99789")
ent_name = Entry(root, font=f)
lab_name.pack(pady=10)
ent_name.pack(pady=10)

lab_phy = Label(root, text="Enter Physics Marks", font=f, bg="#c99789")
ent_phy = Entry(root, font=f)
lab_phy.pack(pady=10)
ent_phy.pack(pady=10)

lab_chem = Label(root, text="Enter Chemistry Marks", font=f, bg="#c99789")
ent_chem = Entry(root, font=f)
lab_chem.pack(pady=10)
ent_chem.pack(pady=10)

lab_maths = Label(root, text="Enter Maths Marks", font=f,  bg="#c99789")
ent_maths = Entry(root, font=f)
lab_maths.pack(pady=10)
ent_maths.pack(pady=10)

def f1():
	ent_name.delete(0, END)
	ent_phy.delete(0, END)
	ent_chem.delete(0, END)
	ent_maths.delete(0, END)
	
	root.after(100, lambda: ent_name.focus())
    
    

def show_bar():
	name = ent_name.get().strip()
        # name checking
	if name == "":
            showerror("name issue", "u did not enter name")
            ent_name.delete(0, END)
            ent_name.focus()
            return
	name_pattern = compile("^[A-Za-z]+$")
	if not name_pattern.match(name):
            showerror("name issue", "name shud be alphabets only")
            ent_name.delete(0, END)
            ent_name.focus()
            return


	if ent_phy.get() == "":
            showerror("Marks issue", "u did not enter phy marks")
            ent_phy.focus()
            return
	try:
            phy = int(ent_phy.get())
	except ValueError:
            showerror("Marks issue", "Physics marks should be integers only")
            ent_phy.delete(0, END)
            ent_phy.focus()
            return
	if phy < 1 or phy > 100:
            showerror("Marks issue", "Physics marks should be between 0 and 100")
            ent_phy.delete(0, END)
            ent_phy.focus()
            return


	if ent_chem.get() == "":
            showerror("Marks issue", "u did not enter chem marks")
            ent_chem.focus()
            return
	try:
            chem = int(ent_chem.get())
	except ValueError:
            showerror("Marks issue", "Chemistry marks should be integers only")
            ent_chem.delete(0, END)
            ent_chem.focus()
            return
	if chem < 1 or chem > 100:
            showerror("Marks issue", "Chemistry marks should be between 0 and 100")
            ent_chem.delete(0, END)
            ent_chem.focus()
            return

	if ent_maths.get() == "":
            showerror("Marks issue", "u did not enter maths marks")
            ent_maths.focus()
            return
	try:
            maths = int(ent_maths.get())
	except ValueError:
            showerror("Marks issue", " Maths marks should be integers only")
            ent_maths.delete(0, END)
            ent_maths.focus()
            return
	if maths < 0 or maths > 100:
            showerror("Marks issue", "Maths marks should be between 0 and 100")
            ent_maths.delete(0, END)
            ent_maths.focus()
            return



	subjects = ["phy", "chem", "maths"]
	marks = [phy, chem, maths]
	plt.bar(subjects, marks, width=0.3)
	plt.xlabel("Subjects")
	plt.ylabel("Marks")
	plt.title(name +"'s Performance")
	plt.show()

	f1()

btn_bar = Button(root, text="Generate Bar Chart", font=f, width=15, command=show_bar, activebackground="#ffa472")
btn_bar.pack(pady=10)

root.mainloop()

