
import tkinter as tk

root = tk.Tk()           # Create the window
root.title("Мое окно")   # Set the window title

root.geometry("200x400-100-100") # Размер окна 200х400

# Цвет окна begraund
# root.config(bg="blue")

# Иконка
photo = tk.PhotoImage(file=r"C:\Users\USER\Desktop\MyPy\ProjectTK\2.png")
root.iconphoto(False, photo)

# background image
photo2 = tk.PhotoImage(file=r"C:\Users\USER\Desktop\MyPy\ProjectTK\1.png")
background_label = tk.Label(root, image=photo2)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.mainloop()





