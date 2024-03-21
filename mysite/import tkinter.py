import tkinter
from tkinter import ttk
from  docxtpl import DocxTemplate
import datetime
def Generate_invoice():
    doc = DocxTemplate("invoice_template.docx")
    name=firstname_entry.get()+lastname_entry.get()
    phone=phone_entry.get()
    subtotal=sum(item[3] for item in invoice_list)
    salestax=0.1
    total=subtotal*(1-salestax)

    doc.render({"name":name,
                "phone":phone,
                "invoice_list":invoice_list,
                "subtotal":subtotal,
                "salestax":str(salestax*100)+"%",
                "total":total})
    doc_name="new_invoice" + name +datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S" + ".docx")
    doc.save(doc_name)
    new_invoice()

def new_invoice():
    firstname_entry.delete(0,tkinter.END)
    lastname_entry.delete(0,tkinter.END)
    phone_entry.delete(0,tkinter.END)
    clear_item()
    tree.delete(*tree.get_children())
    invoice_list.clear()
def clear_item():
    qnt_spinbox.delete(0,tkinter.END)
    qnt_spinbox.insert(0,"1")
    descrp_entry.delete(0,tkinter.END)
    unitpr_spinbox.delete(0,tkinter.END)
    unitpr_spinbox.insert(0,"0.0")

invoice_list=[]
def add_item():
    Quantity=int(qnt_spinbox.get())
    Description=descrp_entry.get()
    Price=float(unitpr_spinbox.get())
    line_total=Quantity*Price
    invoice_item=[Quantity,Description,Price,line_total]
    tree.insert('',0,values=invoice_item)
    clear_item()
    invoice_list.append(invoice_item)

window=tkinter.Tk()
window.title("invoice Generator form")

frame=tkinter.Frame(window)
frame.pack()
firstname_label=tkinter.Label(frame,text="First Name")
firstname_label.grid(row=0,column=0)
lastname_label=tkinter.Label(frame,text="Last Name")
lastname_label.grid(row=0,column=1)
phone_label=tkinter.Label(frame,text="Phone")
phone_label.grid(row=0,column=2)
firstname_entry=tkinter.Entry(frame)
lastname_entry=tkinter.Entry(frame)
phone_entry=tkinter.Entry(frame)
firstname_entry.grid(row=1,column=0)
lastname_entry.grid(row=1,column=1)
phone_entry.grid(row=1,column=2)
qnt_label=tkinter.Label(frame,text="Quantity")
qnt_label.grid(row=2,column=0)
descrp_label=tkinter.Label(frame,text="Description")
descrp_label.grid(row=2,column=1)
unitpr_label=tkinter.Label(frame,text="Unit Price")
unitpr_label.grid(row=2,column=2)
qnt_spinbox=tkinter.Spinbox(frame,from_=1, to=100)
descrp_entry=tkinter.Entry(frame)
unitpr_spinbox=tkinter.Spinbox(frame,from_=0.0,to=500,increment=0.5)
qnt_spinbox.grid(row=3,column=0)
descrp_entry.grid(row=3,column=1)
unitpr_spinbox.grid(row=3,column=2)
additem_button=tkinter.Button(frame,text="Add item",command=add_item)
additem_button.grid(row=4,column=2,pady=5)
columns=('Quantity','Description','Price','Total')
tree=ttk.Treeview(frame,columns=columns,show="headings")
tree.heading('Quantity',text='Quantity')
tree.heading('Description',text="Decsription")
tree.heading('Price',text='Price')
tree.heading('Total',text='Total')


tree.grid(row=5,column=0,columnspan=3,pady=10,padx=20)
generateinvoice_button=tkinter.Button(frame,text="Generate Invoice",command=Generate_invoice)
generateinvoice_button.grid(row=6,column=0,columnspan=3,sticky="news",padx=20,pady=5)
newwinvoice_button=tkinter.Button(frame,text="New Invoice",command=new_invoice)
newwinvoice_button.grid(row=7,columnspan=3,column=0,sticky="news",pady=5,padx=20)



window.mainloop()