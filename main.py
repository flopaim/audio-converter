import os
from tkinter import *
from tkinter import filedialog
from pydub import AudioSegment

# made by flopaim on github

root = Tk()
root.title("Audio Converter | flopaim")

def browse_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, END)
    file_entry.insert(0, file_path)

def convert_audio():
    file_path = file_entry.get()
    file_name, file_ext = os.path.splitext(file_path)
    output_format = format_var.get()
    output_path = file_name + "." + output_format

    if output_format == "mp3":
        AudioSegment.from_file(file_path).export(output_path, format="mp3")
    elif output_format == "wav":
        AudioSegment.from_file(file_path).export(output_path, format="wav")
    elif output_format == "ogg":
        AudioSegment.from_file(file_path).export(output_path, format="ogg")

    status_label.config(text="Conversion Complete, Saved to Audio File Directory!")

file_label = Label(root, text="Select file to convert:")
file_label.pack()

file_entry = Entry(root, width=50)
file_entry.pack()

browse_button = Button(root, text="Browse", command=browse_file)
browse_button.pack()

format_label = Label(root, text="Select output format:")
format_label.pack()

formats = ["mp3", "wav", "ogg"]
format_var = StringVar(root)
format_var.set(formats[0])

format_menu = OptionMenu(root, format_var, *formats)
format_menu.pack()

convert_button = Button(root, text="Convert", command=convert_audio)
convert_button.pack()

status_label = Label(root, text="")
status_label.pack()

root.mainloop()