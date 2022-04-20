#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.23a
#  in conjunction with Tcl version 8.6
#    Jun 26, 2019 01:16:33 AM -03  platform: Windows NT

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

import views.historial_support as historial_support
import views.estudios as estudios

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    historial_support.set_Tk_var()
    top = historia (root)
    historial_support.init(root, top)
    root.mainloop()

w = None
def create_historia(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    historial_support.set_Tk_var()
    top = historia (w)
    historial_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_historia():
    global w
    w.destroy()
    w = None

class historia:
    def __init__(self, top=None):
        self.estudios = []
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 24 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+436+167")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#ffffff")

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.233, rely=0.089, relheight=0.096
                , relwidth=0.55)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(font=font9)
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Historial de estudios''')
        self.Message1.configure(width=330)

        self.paciente = ttk.Label(top)
        self.paciente.place(relx=0.067, rely=0.244, height=19, width=66)
        self.paciente.configure(background="#d9d9d9")
        self.paciente.configure(foreground="#000000")
        self.paciente.configure(font="TkDefaultFont")
        self.paciente.configure(relief="flat")
        self.paciente.configure(text='''Paciente''')

        self.nombrepac = ttk.Entry(top)
        self.nombrepac.place(relx=0.192, rely=0.233, relheight=0.047
                , relwidth=0.21)
        self.nombrepac.configure(takefocus="")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.salir = ttk.Button(top)
        self.salir.place(relx=0.667, rely=0.8, height=25, width=76)
        self.salir.configure(command=historial_support.destroy_window)
        self.salir.configure(takefocus="")
        self.salir.configure(text='''Salir''')

        self.graba = ttk.Button(top)
        self.graba.place(relx=0.458, rely=0.8, height=25, width=76)
        self.graba.configure(takefocus="")
        self.graba.configure(text='''Guardar''')

        self.procesar = ttk.Button(top)
        self.procesar.place(relx=0.15, rely=0.8, height=25, width=80)
        self.procesar.configure(takefocus="")
        self.procesar.configure(text='''Procesar''')
        self.procesar.configure(command=estudios.vp_start_gui)

        self.lista = ScrolledListBox(top)
        self.lista.place(relx=0.133, rely=0.333, relheight=0.389
                , relwidth=0.735)
        self.lista.configure(background="white")
        self.lista.configure(disabledforeground="#a3a3a3")
        self.lista.configure(font="TkFixedFont")
        self.lista.configure(foreground="black")
        self.lista.configure(highlightbackground="#d9d9d9")
        self.lista.configure(highlightcolor="#d9d9d9")
        self.lista.configure(selectbackground="#c4c4c4")
        self.lista.configure(selectforeground="black")
        self.lista.configure(width=10)
        self.lista.configure(listvariable=historial_support.pacientes)
        self.actualizarLista()

    def actualizarLista(self):
        self.estudios = historial_support.getEstudios()
        for index, est in enumerate(self.estudios):
            #print(est)
            self.lista.insert(index,"Paciente: {}, {} - {}".format(est.paciente.apellido,est.paciente.nombre,est.fecha))

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()




