from tkinter import filedialog, messagebox, Button, Tk, Label
import shutil
import os
import easygui

def file_open_box():
    path = easygui.fileopenbox()
    return path

def directory_open_box():
    path = filedialog.askdirectory()
    return path

def open_file():
    path = file_open_box()
    try:
        os.startfile(path)
    except TypeError:
        messagebox.showinfo("Error!", "Can't find the selected file!")


def copy_file():
    source = file_open_box()
    destination = directory_open_box()
    try:
        shutil.copy(source, destination)
        messagebox.showinfo("Done!", "Copied the file successfully.")
    except:
        messagebox.showinfo("Error!", "Copy failed!")


def delete_file():
    path = file_open_box()
    try:
        os.remove(path)
    except:
        messagebox.showinfo("Error!", "File hasn't been deleted!")


def rename_file():
    try:
        file = file_open_box()
        path1 = os.path.dirname(file)
        extention = os.path.splitext(path1)[1]
        new_name = input("new name: ")
        path2 = os.path.join(path1, new_name + extention)
        os.rename(file, path2)
        messagebox.showinfo("Done!", "File has been renamed successfully.")
    except:
        messagebox.showinfo("Error!", "Renaming file has been failed!")


def move_file():
    source = file_open_box()
    destination = directory_open_box()
    if source == destination:
        messagebox.showinfo("Error!", "Destination is same as current directory!")
    else:
        try:
            shutil.move(source, destination)
            messagebox.showinfo("Done!", "File has been moved successfully.")
        except:
            messagebox.showinfo("Error!", "Moving file has been failed!")


def make_directory():
    path = directory_open_box()
    name = input("Name: ")
    new_path = os.path.join(path, name)
    try:
        os.mkdir(new_path)
        messagebox.showinfo("Done!", "Directory has been made successfully.")
    except:
        messagebox.showinfo("Error!", "Making new directory has been failed!")


def remove_directory():
    path = directory_open_box()
    try:
        os.rmdir(path)
        messagebox.showinfo("Done!", "Directory has been deleted successfully.")
    except:
        messagebox.showinfo("Error!", "Deleting directory has been failed!")


def list_files():
    path = directory_open_box()
    file_list = sorted(os.listdir(path))
    for i in file_list:
        print(i)


window = Tk()
window.title("File Manager")
window.configure(bg="black")
window.geometry("300x400")
Label(window, text="What do you want to do?").pack()
Button(window, command=open_file, text="Open file", fg="blue", activebackground="red", bg="white").pack()
Button(window, command=copy_file, text="Copy file", fg="blue", activebackground="red", bg="white").pack()
Button(window, command=delete_file, text="Delete file", fg="blue", activebackground="red", bg="white").pack()
Button(window, command=move_file, text="Move file", fg="blue", activebackground="red", bg="white").pack()
Button(window, command=open_file, text="Open file", fg="blue", activebackground="red", bg="white").pack()
Button(window, command=make_directory, text="Make directory", fg="blue", activebackground="red", bg="white").pack()
Button(window, command=remove_directory, text="Remove Directory", fg="blue", activebackground="red", bg="white").pack()
Button(window, command=list_files, text="List files", fg="blue", activebackground="red", bg="white").pack()




window.mainloop()
