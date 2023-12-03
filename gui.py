import os
from tkinter import END, Tk, filedialog, messagebox
from tkinter.ttk import Button, Entry, Frame, Label, Style

from utils import compress, decompress


# Define subclass App
class App(Frame):

    # Init App 
    def __init__(self, master: Tk):
        # Set title
        master.title("Huffman")
        # Set window size
        master.geometry("600x540")
        # Disallow resizing
        master.resizable(False, False)
        # Inherit Frame to create gui
        Frame.__init__(self, master)
        # Pack gui
        self.pack()
        # Create widgets
        self.__create_widgets()
    
    # Create all the widgets
    def __create_widgets(self):
        # Configure styles
        style = Style()
        # Buttons style
        style.configure("TButton", padding=6, relief="flat", background="#FAD6A5", font=('Helvetica', 22))
		# Frame style
        style.configure("TFrame", background="#567189")
        # Labels style
        style.configure("TLabel", background="#567189", foreground="black", font=('Helvetica', 22))
        # Entries style
        style.configure("TEntry", background="#FAD6A5", foreground="black")
        # Create quit button
        self.quit_button = Button(self, text="Quit", command=self.quit, width=10)
        # Pack the quit button
        self.quit_button.pack(padx=10, pady=10)
        # Create browse button
        self.browse_button = Button(self, text="Browse", command=self.__browse, width=10)
        # Pack browse button
        self.browse_button.pack(pady=10)
        # Create input label
        self.input_label = Label(self, text="Input file")
        # Pack input label
        self.input_label.pack(padx=10, pady=10)
        # Create input entry
        self.input_entry = Entry(self, width=70, justify="center", font=('Helvetica', 18))
        # Pack input entry
        self.input_entry.pack(padx=10, pady=10, ipady=7)
        # Create output label
        self.output_label = Label(self, text="Output file")
        # Pack output label
        self.output_label.pack(padx=10, pady=10)
        # Create output entry
        self.output_entry = Entry(self, width=70, justify="center", font=('Helvetica', 18))
        # Pack output entry
        self.output_entry.pack(padx=10, pady=10, ipady=7)
        # Create compress button
        self.cmp_button = Button(self, text="Compress", command=self.__cmp, width=10)
        # Pack compress button
        self.cmp_button.pack(padx=10, pady=10)
        # Create decompress button
        self.dcmp_button = Button(self, text="Decompress", command=self.__dcmp, width=13)
        # Pack decompress button
        self.dcmp_button.pack(padx=10, pady=10)
    
            
    # Ask user to pick a file
    def __browse(self):
        # Ask open file dialog 
        file_dir = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file", filetypes=(("all files", "*.*"), ("text files", "*.txt"), ("cmp files", "*.cmp")))
        # Delete existing input in input entry
        self.input_entry.delete(0, END)
        # Insert selected path in input entry
        self.input_entry.insert(0, file_dir)
        # Get directory path of selected file
        dir_path = os.path.dirname(file_dir)
        # Get base filename
        base_filename = os.path.basename(file_dir)
        # Get filename and extension separately
        filename, ext = os.path.splitext(base_filename)
        # Delete existing output in output entry
        self.output_entry.delete(0, END)
        # If the file is a text file 
        if ext == ".txt":
            # Insert compressed path in output entry
            self.output_entry.insert(0, os.path.join(dir_path, f"{filename}.cmp"))
        # Else for a cmp file
        else:
            # Insert decompressed path in output entry
            self.output_entry.insert(0, os.path.join(dir_path, f"dcmp_{filename}.txt"))        
        
        
    # Compress File
    def __cmp(self):
        # Get input path
        input_path = self.input_entry.get()
        # Get output path
        output_path = self.output_entry.get()
        # Split input path to get filename and extension separately
        input_path_name, input_path_ext = os.path.splitext(input_path)
        # Split output path to get filename and extension separately
        _, output_path_ext = os.path.splitext(output_path)
        # If input is empty
        if not input_path:
            # Show error message
            messagebox.showerror("Error", "Input path is empty")
            # Return without compressing
            return
        # If output is empty
        if not output_path:
            # Assign compressed path  output based on input name
            output_path = f"/home/erfan/Desktop/{input_path_name}.cmp"
        # If input file is not a text file
        if input_path_ext != ".txt":
            # Show error message
            messagebox.showerror("Error", "Input file must be text")
            # Return without compressing
            return
        # If output file is not a cmp file
        if output_path_ext != ".cmp":
            # Show error message
            messagebox.showerror("Error", "Output file must be cmp")
            # Return without compressing
            return
        # Perform compression
        compress(input_path, output_path)
        # Show success message
        messagebox.showinfo("Done", "Compression is done")


    # Decompress File
    def __dcmp(self):
        # Get input path
        input_path = self.input_entry.get()
        # Get output path
        output_path = self.output_entry.get()
        # Split input path to get filename and extension separately
        input_path_name, input_path_ext = os.path.splitext(input_path)
        # Split output path to get filename and extension separately
        _, output_path_ext = os.path.splitext(output_path)
        # If input is empty
        if not input_path:
            # Show error message
            messagebox.showerror("Error", "Input path is empty")
            # Return without decompressing
            return
        # If output is empty
        if not output_path:
            # Assign decompressed path  output based on input name
            output_path = f"/home/erfan/Desktop/dcmp_{input_path_name}.txt"
        # If input file is not a cmp file
        if input_path_ext != ".cmp":
            # Show error message
            messagebox.showerror("Error", "Input file must be cmp")
            # Return without decompressing
            return
        # If output file is not a txt file
        if output_path_ext != ".txt":
            # Show error message
            messagebox.showerror("Error", "Output file must be txt")
            # Return without decompressing
            return
        # Perform decompression
        decompress(input_path, output_path)
        # Show success message
        messagebox.showinfo("Done", "Decompression is done")