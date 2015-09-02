#!/usr/bin/env python
# -*- coding: utf-8 -*e

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
	#Método constructor de la clase
	def __init__(self):
		#Iniciar el objeto QMainWindow
		QMainWindow.__init__(self)
		#Cargar la configuración del archivo .ui en el objeto
		uic.loadUi("disenio.ui", self)
		self.setWindowTitle("Cambiando el título de la ventana")

#Instancia para iniciar una aplicación

app = QApplication(sys.argv)
#Crear un objeto de la clase

_ventana = Ventana()

#Mostra la ventana

_ventana.show()

#Ejecutar la aplicación

app.exec_()
