from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from student import Student
#open the records csv file students.csv if not present create it with the attributes (roll, dept code, name, address and phone)
try:
    with open("students.csv","r") as f:
        pass
except:
    with open("students.csv","w") as f:
        f.write("roll,dept,name,address,phone number \n")

# A tkinter based GUI where user may add/search/edit/delete/display all student record. Open windows for each operation.

#class
class StudentGUI(Student):
    #constructor
    def __init__(self):
        self.dept={"CSE":"01","ECE":"02","EEE":"03","MECH":"04","CIVIL":"05","MME":"06","CHEM":"07","META":"08","PROD":"09"}
        #create a window
        self.window=Tk()
        self.window.geometry("400x200")
        #set the title
        self.window.title("Student Records")
        #create a frame
        self.frame=Frame(self.window)
        #pack the frame
        self.frame.pack()
        #create a button to add a record
        self.add=Button(self.frame,text="Add",command=self.add)
        #pack the button
        self.add.pack(side=LEFT)
        #create a button to search a record
        self.search=Button(self.frame,text="Search",command=self.search)
        #pack the button
        self.search.pack(side=LEFT)
        #create a button to edit a record
        self.edit=Button(self.frame,text="Edit",command=self.edit)
        #pack the button
        self.edit.pack(side=LEFT)
        #create a button to delete a record
        self.delete=Button(self.frame,text="Delete",command=self.delete)
        #pack the button
        self.delete.pack(side=LEFT)
        #create a button to display all the records
        self.display=Button(self.frame,text="Display",command=self.display)
        #pack the button
        self.display.pack(side=LEFT)
        #create a button to exit the program
        self.exit=Button(self.frame,text="Exit",command=self.exit)
        #pack the button
        self.exit.pack(side=LEFT)
        #create a mainloop
        self.window.mainloop()
    def exit(self):
        #destroy the window
        self.window.destroy()
    #open a new window to add a record. The window must have entry boxes for roll, dept, name, address and phone number. Display the depts with their codes. The user can Cancel or Add the record.
    def add(self):
        #create a window
        self.add_window=Tk()
        #set the title
        self.add_window.title("Add Record")
        #create a frame
        self.add_frame=Frame(self.add_window)
        #pack the frame
        self.add_frame.pack()
        #create a label for roll
        self.roll_label=Label(self.add_frame,text="Roll")
        #pack the label
        self.roll_label.pack(side=LEFT)
        #create an entry box for roll
        self.roll_entry=Entry(self.add_frame)
        #pack the entry box
        self.roll_entry.pack(side=LEFT)
        #create a label for dept
        self.dept_label=Label(self.add_frame,text="Dept")
        #pack the label
        self.dept_label.pack(side=LEFT)
        #create an entry box for dept
        self.dept_entry=Entry(self.add_frame)
        #pack the entry box
        self.dept_entry.pack(side=LEFT)
        #create a label for name
        self.name_label=Label(self.add_frame,text="Name")
        #pack the label
        self.name_label.pack(side=LEFT)
        #create an entry box for name
        self.name_entry=Entry(self.add_frame)
        #pack the entry box
        self.name_entry.pack(side=LEFT)
        #create a label for address
        self.address_label=Label(self.add_frame,text="Address")
        #pack the label
        self.address_label.pack(side=LEFT)
        #create an entry box for address
        self.address_entry=Entry(self.add_frame)
        #pack the entry box
        self.address_entry.pack(side=LEFT)
        #create a label for phone number
        self.phone_label=Label(self.add_frame,text="Phone")
        #pack the label
        self.phone_label.pack(side=LEFT)
        #create an entry box for phone number
        self.phone_entry=Entry(self.add_frame)
        #pack the entry box
        self.phone_entry.pack(side=LEFT)
        #create a button to add the record
        self.add_button=Button(self.add_frame,text="Add",command=self.add_record)
        #pack the button
        self.add_button.pack(side=LEFT)
        #create a button to cancel the operation
        self.cancel_button=Button(self.add_frame,text="Cancel",command=self.cancel)
        #pack the button
        self.cancel_button.pack(side=RIGHT)
        #Show the dept and code from Student.dept dictionary 
        #create a menu
        self.dept_menu=Menu(self.add_window)
        #iterate through the dept dictionary
        for dept in self.dept:
            #add the dept and code to the menu
            self.dept_menu.add_command(label=dept+":"+self.dept[dept])
        #create a button to show the menu
        self.show_dept=Button(self.add_frame,text="Show Dept",command=self.show_dept)
        #pack the button
        self.show_dept.pack(side=LEFT)
        #create a mainloop
        self.add_window.mainloop()
    def show_dept(self):
        #show the menu in the same frame
        self.dept_menu.post(self.show_dept.winfo_rootx(),self.show_dept.winfo_rooty()+self.show_dept.winfo_height())
        #Select an option from the menu and display the dept code in the dept entry box
        self.dept_menu.bind("<Button-1>",self.select_dept)
    def select_dept(self,event):
        #get the dept
        dept=event.widget.entrycget("active","label")
        #get the code
        code=dept.split(":")[0]
        #display the code in the dept entry box
        self.dept_entry.delete(0,END)
        self.dept_entry.insert(0,code)
        
    def add_record(self):
        #get the roll number
        roll=self.roll_entry.get()
        #get the dept
        dept=self.dept_entry.get()
        #get the name
        name=self.name_entry.get()
        #get the address
        address=self.address_entry.get()
        #get the phone number
        phone=self.phone_entry.get()
        #add the record
        kemp=Student.add(self,roll,dept,name,address,phone)
        #add the record
        if not (kemp):
            #show a message
            messagebox.showerror("Error","Record already exists")
        #destroy the window
        else:
            #show a message
            messagebox.showinfo('Record Added')
        self.add_window.destroy()
        
    def cancel(self):
        #destroy the current window
        self.add_window.destroy()
    #open a new window to search the record. To search only roll number is required. The user can Cancel or Search the record.
    def search(self):
        #create a window
        self.search_window=Tk()
        #set the title
        self.search_window.title("Search Record")
        #create a frame
        self.search_frame=Frame(self.search_window)
        #pack the frame
        self.search_frame.pack()
        #create a label for roll
        self.roll_label=Label(self.search_frame,text="Roll")
        #pack the label
        self.roll_label.pack(side=LEFT)
        #create an entry box for roll
        self.roll_entry=Entry(self.search_frame)
        #pack the entry box
        self.roll_entry.pack(side=LEFT)
        #create a button to search the record
        self.search_button=Button(self.search_frame,text="Search",command=self.search_record)
        #pack the button
        self.search_button.pack(side=LEFT)
        #create a button to cancel the operation
        self.cancel_button=Button(self.search_frame,text="Cancel",command=self.search_window.destroy)
        #pack the button
        self.cancel_button.pack(side=RIGHT)
        #create a mainloop
        self.search_window.mainloop()
    def search_record(self):
        #get the roll number
        roll=self.roll_entry.get()
        rec=Student.search(self,roll)
        #search the record
        if not (rec):
            #show a message
            messagebox.showerror("Error","Record not found")
        #show the searched record in a new window
        else:
            #create a window
            self.searched_window=Tk()
            #set the title
            self.searched_window.title("Searched Record")
            #create a frame
            self.searched_frame=Frame(self.searched_window)
            #pack the frame
            self.searched_frame.pack()
            #create a label for roll
            self.roll_label=Label(self.searched_frame,text="Roll")
            #pack the label
            self.roll_label.pack(side=LEFT)
            #create an entry box for roll
            self.roll_entry=Entry(self.searched_frame)
            #pack the entry box
            self.roll_entry.pack(side=LEFT)
            #display the roll number
            self.roll_entry.insert(0,rec[0])
            #create a label for dept
            self.dept_label=Label(self.searched_frame,text="Dept")
            #pack the label
            self.dept_label.pack(side=LEFT)
            #create an entry box for dept
            self.dept_entry=Entry(self.searched_frame)
            #pack the entry box
            self.dept_entry.pack(side=LEFT)
            #display the dept
            self.dept_entry.insert(0,rec[1])
            #create a label for name
            self.name_label=Label(self.searched_frame,text="Name")
            #pack the label
            self.name_label.pack(side=LEFT)
            #create an entry box for name
            self.name_entry=Entry(self.searched_frame)
            #pack the entry box
            self.name_entry.pack(side=LEFT)
            #display the name
            self.name_entry.insert(0,rec[2])
            #create a label for address
            self.address_label=Label(self.searched_frame,text="Address")
            #pack the label
            self.address_label.pack(side=LEFT)
            #create an entry box for address
            self.address_entry=Entry(self.searched_frame)
            #pack the entry box
            self.address_entry.pack(side=LEFT)
            #display the address
            self.address_entry.insert(0,rec[3])
            #create a label for phone number
            self.phone_label=Label(self.searched_frame,text="Phone")
            #pack the label
            self.phone_label.pack(side=LEFT)
            #create an entry box for phone number
            self.phone_entry=Entry(self.searched_frame)
            #pack the entry box
            self.phone_entry.pack(side=LEFT)
            #display the phone number
            self.phone_entry.insert(0,rec[4])
            #exit button
            self.exit_button=Button(self.searched_frame,text="Exit",command=self.searched_window.destroy)

            #mainloop
            self.searched_window.mainloop()

        #destroy the window
        self.search_window.destroy()
    #open a new window to delete the record. To delete only roll number is required. The user can Cancel or Delete the record.
    def delete(self):
        #create a window
        self.delete_window=Tk()
        #set the title
        self.delete_window.title("Delete Record")
        #create a frame
        self.delete_frame=Frame(self.delete_window)
        #pack the frame
        self.delete_frame.pack()
        #create a label for roll
        self.roll_label=Label(self.delete_frame,text="Roll")
        #pack the label
        self.roll_label.pack(side=LEFT)
        #create an entry box for roll
        self.roll_entry=Entry(self.delete_frame)
        #pack the entry box
        self.roll_entry.pack(side=LEFT)
        #create a button to delete the record
        self.delete_button=Button(self.delete_frame,text="Delete",command=self.delete_record)
        #pack the button
        self.delete_button.pack(side=LEFT)
        #create a button to cancel the operation
        self.cancel_button=Button(self.delete_frame,text="Cancel",command=self.delete_window.destroy)
        #pack the button
        self.cancel_button.pack(side=RIGHT)
        #create a mainloop
        self.delete_window.mainloop()
    def delete_record(self):
        #get the roll number
        roll=self.roll_entry.get()
        #delete the record
        if not (Student.delete(self,roll)):
            #show a message
            messagebox.showerror("Error","Record not found")
        else:
            #show a message
            messagebox.showinfo("Success","Record deleted")
        #destroy the window
        self.delete_window.destroy()
    
    #open a new window to edit the record. To update only roll number is required. The roll number cannot be updated. The user can Cancel or Update the record.
    def edit(self):
        #create a window
        self.edit_window=Tk()
        #set the title
        self.edit_window.title("Edit Record")
        #create a frame
        self.edit_frame=Frame(self.edit_window)
        #pack the frame
        self.edit_frame.pack()
        #create a label for roll
        self.roll_label=Label(self.edit_frame,text="Roll")
        #pack the label
        self.roll_label.pack(side=LEFT)
        #create an entry box for roll
        self.roll_entry=Entry(self.edit_frame)
        #pack the entry box
        self.roll_entry.pack(side=LEFT)
        #create a button to search the record
        self.search_button=Button(self.edit_frame,text="Search",command=self.search_record)
        #pack the button
        self.search_button.pack(side=LEFT)
        #create a button to cancel the operation
        self.cancel_button=Button(self.edit_frame,text="Cancel",command=self.cancel_button.destroy)
        #pack the button
        self.cancel_button.pack(side=RIGHT)
        #create a mainloop
        self.edit_window.mainloop()
    def search_record(self):
        #get the roll number
        roll=self.roll_entry.get()
        #search the record
        rec=Student.search(self,roll)
        print(rec)
        if not rec:
            #show a message
            messagebox.showerror("Error","Record not found")
        else:
            # #destroy the window
            # self.edit_window.destroy()
            #create a window
            self.searched_window=Tk()
            #set the title
            self.searched_window.title("Search Record")
            #create a frame
            self.searched_frame=Frame(self.searched_window)
            #pack the frame
            self.searched_frame.pack()
            #create a label for roll
            self.roll_label=Label(self.searched_frame,text="Roll")
            #pack the label
            self.roll_label.pack(side=LEFT)
            #create an entry box for roll
            self.roll_entry=Entry(self.searched_frame)
            #pack the entry box
            self.roll_entry.pack(side=LEFT)
            #display the roll number
            self.roll_entry.insert(0,rec[0])
            #create a label for dept
            self.dept_label=Label(self.searched_frame,text="Dept")
            #pack the label
            self.dept_label.pack(side=LEFT)
            #create an entry box for dept
            self.dept_entry=Entry(self.searched_frame)
            #pack the entry box
            self.dept_entry.pack(side=LEFT)
            #display the dept
            self.dept_entry.insert(0,rec[1])
            #create a label for name
            self.name_label=Label(self.searched_frame,text="Name")
            #pack the label
            self.name_label.pack(side=LEFT)
            #create an entry box for name
            self.name_entry=Entry(self.searched_frame)
            #pack the entry box
            self.name_entry.pack(side=LEFT)
            #display the name
            self.name_entry.insert(0,rec[2])
            #create a label for address
            self.address_label=Label(self.searched_frame,text="Address")
            #pack the label
            self.address_label.pack(side=LEFT)
            #create an entry box for address
            self.address_entry=Entry(self.searched_frame)
            #pack the entry box
            self.address_entry.pack(side=LEFT)
            #display the address
            self.address_entry.insert(0,rec[3])
            #display the phone number
            #create label for phone
            self.phone_label=Label(self.searched_frame,text="Phone")
            #pack the label
            self.phone_label.pack(side=LEFT)
            #create an entry box for phone
            self.phone_entry=Entry(self.searched_frame)
            #pack the entry box
            self.phone_entry.pack(side=LEFT)
            #display the phone number
            self.phone_entry.insert(0,rec[4])
            # create a button to update the record
            self.update_button=Button(self.searched_frame,text="Update",command=self.update_record)
            #pack the button
            self.update_button.pack(side=LEFT)
            #create a button to cancel the operation
            self.cancel_button=Button(self.searched_frame,text="Cancel",command=self.searched_window.destroy)
            #pack the button
            self.cancel_button.pack(side=RIGHT)
            #create a mainloop
            self.searched_window.mainloop()
    def update_record(self):
        #get the roll number
        roll=self.roll_entry.get()
        #get the dept
        dept=self.dept_entry.get()
        #get the name
        name=self.name_entry.get()
        #get the address
        address=self.address_entry.get()
        #get the phone number
        phone=self.phone_entry.get()
        #update the record
        if not (Student.edit(self,roll,dept,name,address,phone)):
            #show a message
            messagebox.showerror("Error","Record not found")
        else:
            #show a message
            messagebox.showinfo("Success","Record updated")
        #destroy the window
        self.searched_window.destroy()
    #open a new window to display the records. List the records and display them 5 at a time. The user can go to the next 5 records or previous 5 records.
    def display(self):
        self.cnt=0
        self.recs=Student.display(self)
        self.recs=[self.recs[i:i + 5] for i in range(0, len(self.recs), 5)]
        #create a window
        self.display_window=Tk()
        #set the title
        self.display_window.title("Display Records")
        #create a frame
        self.display_frame=Frame(self.display_window)
        #pack the frame
        self.display_frame.pack()
        #create a button to go to the next 5 records
        self.next_button=Button(self.display_frame,text="Next",command=self.next)
        #pack the button
        self.next_button.pack(side=RIGHT)
        #create a button to go to the previous 5 records
        self.previous_button=Button(self.display_frame,text="Previous",command=self.previous)
        #pack the button
        self.previous_button.pack(side=RIGHT)
        #create a button to cancel the operation
        self.cancel_button=Button(self.display_frame,text="Cancel",command=self.display_window.destroy)
        #pack the button
        self.cancel_button.pack(side=RIGHT)
        #create a mainloop
        self.display_window.mainloop()
    def next(self):
        #Create table to show 5 records at a time
        self.table=ttk.Treeview(self.display_frame,columns=("Roll","Dept","Name","Address","Phone"))
        #pack the table
        self.table.pack()
        #create a scrollbar
        self.scrollbar=Scrollbar(self.display_frame,orient=VERTICAL,command=self.table.yview)
        #pack the scrollbar
        self.scrollbar.pack(side=RIGHT,fill=Y)
        #configure the table
        self.table.configure(yscrollcommand=self.scrollbar.set)
        #define headings
        self.table.heading("#0",text="S.No")
        self.table.heading("Roll",text="Roll")
        self.table.heading("Dept",text="Dept")
        self.table.heading("Name",text="Name")
        self.table.heading("Address",text="Address")
        self.table.heading("Phone",text="Phone")
        #define column
        self.table.column("#0",width=50)
        self.table.column("Roll",width=100)
        self.table.column("Dept",width=100)
        self.table.column("Name",width=100)
        self.table.column("Address",width=100)
        self.table.column("Phone",width=100)
        #insert records
        for i in range(0,self.recs[self.cnt].__len__()):
            self.table.insert('',i,text=i+1,values=(self.recs[i][0],self.recs[i][1],self.recs[i][2],self.recs[i][3],self.recs[i][4]))
        self.cnt+=1
        self.delete_frame.destroy()
    def previous(self):
        #Create table to show 5 records at a time
        self.table=ttk.Treeview(self.display_frame,columns=("Roll","Dept","Name","Address","Phone"))
        #pack the table
        self.table.pack()
        #create a scrollbar
        self.scrollbar=Scrollbar(self.display_frame,orient=VERTICAL,command=self.table.yview)
        #pack the scrollbar
        self.scrollbar.pack(side=RIGHT,fill=Y)
        #configure the table
        self.table.configure(yscrollcommand=self.scrollbar.set)
        #define headings
        self.table.heading("#0",text="S.No")
        self.table.heading("Roll",text="Roll")
        self.table.heading("Dept",text="Dept")
        self.table.heading("Name",text="Name")
        self.table.heading("Address",text="Address")
        self.table.heading("Phone",text="Phone")
        #define column
        self.table.column("#0",width=50)
        self.table.column("Roll",width=100)
        self.table.column("Dept",width=100)
        self.table.column("Name",width=100)
        self.table.column("Address",width=100)
        self.table.column("Phone",width=100)
        #insert records
        for i in range(0,self.recs[self.cnt].__len__()):
            self.table.insert('',i,text=i+1,values=(self.recs[i][0],self.recs[i][1],self.recs[i][2],self.recs[i][3],self.recs[i][4]))
        self.cnt-=1
        self.delete_frame.destroy()
                

StudentGUI()

