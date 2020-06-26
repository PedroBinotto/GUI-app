# -*- coding: utf-8 -*-
import tkinter as tk

def main():
	try:
		cabs = [
			int(entry_field1.get()),
			int(entry_field2.get())
		]
		dec = int(entry_field3.get())
		vent = int(entry_field4.get())
	except:
		erro = "\nINPUT INVÁLIDO\nUTILIZE NÚMEROS INTEIROS"
		display.delete('1.0', tk.END)
		display.insert(tk.END, erro)

	ang_final = dec + vent

	results = []

	for i in cabs:
		if i > ang_final:
			results.append(i - ang_final)
		else:
			results.append(ang_final - i)

	result_final = results[0]

	for i in results:
		if i < result_final:
			result_final = i

	cab_final = cabs[results.index(result_final)]

	display.delete('1.0', tk.END)
	display.insert(tk.END, cab_final)

win = tk.Tk()
win.geometry("400x300")
win.resizable(False, False)
win.title("App") 

aviso = tk.Label(text="Informe o ângulo utilizando números inteiros\nEx.: 180")
aviso.pack()

cab1_lab = tk.Label(text="Cabeçeira 1:")
cab1_lab.pack()
entry_field1 = tk.Entry()
entry_field1.pack()

cab2_lab = tk.Label(text="Cabeçeira 2:")
cab2_lab.pack()
entry_field2 = tk.Entry()
entry_field2.pack()

dec_lab = tk.Label(text="Declinação Magnética:")
dec_lab.pack()
entry_field3 = tk.Entry()
entry_field3.pack()

ven_lab = tk.Label(text="Ângulo do vento:")
ven_lab.pack()
entry_field4 = tk.Entry()
entry_field4.pack()

enter = tk.Button(text="OK", command=main)
enter.pack()

display = tk.Text(master=win, height=1, width=10)
display.pack(padx=(10, 2))

win.mainloop()
