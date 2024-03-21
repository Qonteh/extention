from tkinter import *
import tkinter
import PyPDF2

from tkinter import filedialog
window=Tk()
window.title("PDF text extractor")
window.geometry("500x500")
def OpenFile():
    filename=filedialog.askopenfile(title="Open PDF File",initialdir='D:\SETUPS',filetypes=[('PDF Files','*.pdf')])
    reader=PyPDF2.PdfReader(filename)

    for i in range(reader.numPages):
        current_text=reader.getPage(i).extractText()
        print(current_text)

file_name=tkinter.Label(window,text="No File selected")
output_file=tkinter.Text(window)
openfile_button=tkinter.Button(window,text="Open PDF File",command=OpenFile)



file_name.pack()
output_file.pack()
openfile_button.pack()
window.mainloop()