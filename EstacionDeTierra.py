import tkinter as tk
from dronLink.Dron import Dron

dron = Dron()

ventana = tk.Tk()
ventana.geometry ('350x400')
ventana.title("Pequeña estación de tierra")

# La interfaz tiene 10 filas y una columna

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)
ventana.rowconfigure(3, weight=1)
ventana.rowconfigure(4, weight=1)
ventana.rowconfigure(5, weight=1)
ventana.rowconfigure(6, weight=1)
ventana.rowconfigure(7, weight=1)
ventana.rowconfigure(8, weight=1)
ventana.rowconfigure(9, weight=1)

ventana.columnconfigure(0, weight=1)

# Disponemos ahora los 9 botones
connectBtn = tk.Button(ventana, text="Conectar", bg="dark orange", command = lambda: dron.connect('tcp:127.0.0.1:5763', 115200))
connectBtn.grid(row=0, column=0, padx=3, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

armBtn = tk.Button(ventana, text="Armar", bg="dark orange", command=lambda: dron.arm())
armBtn.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

takeOffBtn = tk.Button(ventana, text="Despegar", bg="dark orange", command=lambda: dron.takeOff(3))
takeOffBtn.grid(row=2, column=0,  padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

NorthBtn = tk.Button(ventana, text="Norte", bg="dark orange", command=lambda: dron.go('North'))
NorthBtn.grid(row=3, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

SouthBtn = tk.Button(ventana, text="Sur", bg="dark orange", command=lambda: dron.go('South'))
SouthBtn.grid(row=4, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

EastBtn = tk.Button(ventana, text="Este", bg="dark orange", command=lambda: dron.go('East'))
EastBtn.grid(row=5, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

WestBtn = tk.Button(ventana, text="Oeste", bg="dark orange", command=lambda: dron.go('West'))
WestBtn.grid(row=6, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

StopBtn = tk.Button(ventana, text="Para", bg="dark orange", command=lambda: dron.go('Stop'))
StopBtn.grid(row=7, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

RTLBtn = tk.Button(ventana, text="RTL", bg="dark orange", command=lambda: dron.RTL())
RTLBtn.grid(row=8, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

disconnectBtn = tk.Button(ventana, text="Desconectar", bg="dark orange", command=lambda: dron.disconnect())
disconnectBtn.grid(row=9, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

ventana.mainloop()