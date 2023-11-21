import tkinter as tk

root = tk.Tk()
root.title("Signboard Detection")
root.geometry("500x500")

upload_button = tk.Button(root, text="Upload image", font=("Helvetica", 18))
# upload_button.pack()

l = tk.Label(root, text="Hey")
l.pack()

# root.mainloop()