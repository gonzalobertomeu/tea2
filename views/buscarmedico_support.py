#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.23a
#  in conjunction with Tcl version 8.6
#    Jul 10, 2019 01:51:30 PM -03  platform: Windows NT

import sys
import controllers.Medico as ctrl

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

def set_Tk_var():
    global medico_search
    medico_search = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
def getAll():
    return ctrl.buscarAllMedicos()

def getPorApellido(apellido):
    medicos = ctrl.buscarMedicosPorApellido(apellido)
    if (medicos == None):
        print("Error en la busqueda")
    else:
        print("Se buscaron los medicos por apellido")
        import views.buscarmedico as vista
        vista.top.insertar(medicos)
def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None





