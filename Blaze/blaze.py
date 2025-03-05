import random
import tkinter as tk
from tkinter import messagebox

saldo = 50
multiplicadores = {"preto": 2, "vermelho": 2, "branco": 14, "laranja": 100}
cores_disponiveis = list(multiplicadores.keys())

root = tk.Tk()
root.title("Mini Cassino")
root.geometry("400x500")

def girar_roleta():
    global saldo
    try:
        aposta = float(entry_aposta.get())
        cor_escolhida = var_cor.get()

        if aposta > saldo:
            messagebox.showerror("Erro", "Saldo insuficiente!")
            return
        if cor_escolhida not in multiplicadores:
            messagebox.showerror("Erro", "Escolha uma cor válida!")
            return

        cor_sorteada = random.choice(cores_disponiveis)
        label_resultado.config(text=f"A roleta girou... caiu na cor: {cor_sorteada.upper()}!", fg="blue")

        if cor_escolhida == cor_sorteada:
            ganho = aposta * multiplicadores[cor_escolhida]
            saldo += ganho
            messagebox.showinfo("Parabéns!", f"Você ganhou R${ganho:.2f}!")
        else:
            saldo -= aposta
            messagebox.showinfo("Que pena...", f"Você perdeu R${aposta:.2f}!")

        label_saldo.config(text=f"Saldo: R${saldo:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Insira um valor de aposta válido!")

def Depositar():
    global saldo
    try:
        valor_deposito = float(entry_deposito.get())
        if valor_deposito > 0:
            saldo += valor_deposito
            label_saldo.config(text=f"Saldo: R${saldo:.2f}")
            messagebox.showinfo("Depósito", f"Você depositou R${valor_deposito:.2f}!")
        else:
            messagebox.showerror("Erro", "O valor precisa ser maior que zero!")
    except ValueError:
        messagebox.showerror("Erro", "Insira um valor válido para o depósito!")

def sair():
    messagebox.showinfo("Obrigado!", f"Saldo final: R${saldo:.2f}\nObrigado por jogar no Mini Cassino!")
    root.quit()

label_saldo = tk.Label(root, text=f"Saldo: R${saldo:.2f}", font=("Arial", 14))
label_saldo.pack(pady=10)

tk.Label(root, text="Quanto deseja apostar?", font=("Arial", 12)).pack()
entry_aposta = tk.Entry(root)
entry_aposta.pack()

tk.Label(root, text="Valor do depósito:", font=("Arial", 12)).pack()
entry_deposito = tk.Entry(root)
entry_deposito.pack()

tk.Label(root, text="Escolha a cor:", font=("Arial", 12)).pack()
var_cor = tk.StringVar(value="preto")
for cor in multiplicadores.keys():
    tk.Radiobutton(root, text=cor.capitalize(), variable=var_cor, value=cor).pack()

btn_girar = tk.Button(root, text="Girar Roleta", command=girar_roleta)
btn_girar.pack(pady=10)

btn_depositar = tk.Button(root, text="Depositar", command=Depositar)
btn_depositar.pack(pady=10)

label_resultado = tk.Label(root, text="", font=("Arial", 12))
label_resultado.pack()

btn_sair = tk.Button(root, text="Sair", command=sair)
btn_sair.pack(pady=10)

root.mainloop()
