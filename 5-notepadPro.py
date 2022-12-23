# CabreraP5
# Programmer: Robert Cabrera
# EMail: rcabrera14@cnm.edu
# Purpose: This program is to demonstrate how to use a GUI
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

#header function
def header():
        print("\nThis function will print a summary explaining the purpose of the program.")
        print("CabreraP4")
        print("Programmer: Robert Cabrera")
        print("EMail: rcabrera14@cnm.edu")
        print("This program is to demonstrate how to use a GUI\n")
 
def open_file():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"),("All Files","*.*")])#file type options including all wildcard.wildcard
    if not filepath: 
        return
    textarea.delete(1.0, tk.END) #fresh display
    with open(filepath, "r") as input_file: #read open file
        text = input_file.read()
        textarea.insert(tk.END, text) #insert file text into text area
    window.title(f"Notepad - {filepath}") #print file path of an open file (in the header)
 
def save_file():
    filepath = asksaveasfilename(defaultextension= "txt", filetypes = [("Text Files", "*.txt"),("All Files","*.*")])  
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text=textarea.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Notepad - {filepath}")


# window settings 
window = tk.Tk()
window.title("Notepad")
window.rowconfigure(0, minsize=600, weight=1)
window.columnconfigure(1,minsize=800,weight=1)
textarea=tk.Text(window)
buttonFrame = tk.Frame(window, relief=tk.RAISED, bd=2)
OpenButton = tk.Button(buttonFrame, relief=tk.SOLID, command=open_file, text='Open')
SaveButton = tk.Button(buttonFrame, relief=tk.SOLID, command=save_file, text='Save as')
OpenButton.grid(row=0, column=0, sticky ="ew", padx=10, pady=10)
SaveButton.grid(row=1, column=0, sticky ="ew", padx=10)
buttonFrame.grid(row=0,column=0,sticky="ns")
textarea.grid(row=0,column=1,sticky="nsew")  
    
def main():
    header()
    window.mainloop() #instantiate and deploy window
    #print('\nmy main method\n')
    
    
    
            
if __name__ == '__main__':
    main()       