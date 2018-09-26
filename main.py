import Tkinter as tk
app = tk.Tk()
app.geometry('500x500')
app.title('MrMixxy')

button = tk.Button(app, text = 'go away', width = 25, command = app.destroy)
button.pack(fill = 'both', expand = True)

app.mainloop()