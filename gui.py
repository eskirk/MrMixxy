import Tkinter as tk
from effects import snare, bass, loop

app = tk.Tk()
app.geometry('800x400')
app.title('MrMixxy')

# exit button
exit = tk.Button(app, text = 'exit', width = 15, command = app.destroy)
exit.pack()

# snare button
snare = tk.Button(app, text = 'snare', width = 15, command = snare)
snare.pack()

# snare button
bass = tk.Button(app, text = 'bass', width = 15, command = bass)
bass.pack()

# loop button
loop = tk.Button(app, text = 'loop', width = 15, command = loop)
loop.pack()

app.mainloop()