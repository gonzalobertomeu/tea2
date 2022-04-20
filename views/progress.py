import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Progress (root)
    root.mainloop()

def create_progress(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Progress (w)
    return (w, top)

class Progress:
    def __init__(self, top= None):
        top.geometry('400x150')
        top.title("Procesando estudio")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#ffffff")


        self.titulo = tk.Label(top)
        self.titulo.config(text="Estudio: (nombre estudio)")
        self.titulo.pack(fill=tk.X, pady=10)

        self.progressbar = ttk.Progressbar(top)
        self.progressbar.pack(fill=tk.X, pady=10, padx=10)
        
        self.cancelar = ttk.Button(top)
        self.cancelar.config(text="Cancelar")
        self.cancelar.pack(fill=tk.X,side=tk.RIGHT,pady=10,padx=10)
    
    def setMaximo(self,maximo):
        self.progressbar.configure(maximum=maximo)
    
    def updateProgress(self,update):
        self.progressbar.step(update)


if __name__ == '__main__':
    vp_start_gui()