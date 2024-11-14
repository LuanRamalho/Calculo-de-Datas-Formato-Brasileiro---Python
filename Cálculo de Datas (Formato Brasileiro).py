import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calcular_diferenca():
    # Pega as datas inseridas nas caixas de texto
    data1_str = entrada_data1.get()
    data2_str = entrada_data2.get()
    
    try:
        # Converte as strings para objetos de data
        data1 = datetime.strptime(data1_str, '%d-%m-%Y')
        data2 = datetime.strptime(data2_str, '%d-%m-%Y')

        # Calcula a diferença
        if data1 > data2:
            data1, data2 = data2, data1  # Garante que data1 seja a menor

        diff = data2 - data1
        
        # Calcula anos, meses e dias
        anos = data2.year - data1.year
        meses = data2.month - data1.month
        dias = data2.day - data1.day

        if dias < 0:
            dias += (data1.replace(month=data1.month % 12 + 1, day=1) - data1).days
            meses -= 1
        if meses < 0:
            meses += 12
            anos -= 1

        # Exibe o resultado
        resultado = f'Diferença: {anos} anos, {meses} meses e {dias} dias.'
        messagebox.showinfo("Resultado", resultado)
    
    except ValueError:
        messagebox.showerror("Erro", "Formato de data inválido. Use DD-MM-YYYY.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Calculadora de Diferença de Datas")
janela.geometry("400x200")
janela.configure(bg="#ADD8E6")  # Cor de fundo azul-claro

# Criação dos widgets
label_data1 = tk.Label(janela, text="Data 1 (DD-MM-YYYY):", bg="#ADD8E6", fg="purple", font=("Times new Roman", 11))
label_data1.pack()

entrada_data1 = tk.Entry(janela, width=27)
entrada_data1.pack()

label_data2 = tk.Label(janela, text="Data 2 (DD-MM-YYYY):" , bg="#ADD8E6", fg="purple", font=("Times new Roman", 11))
label_data2.pack()

entrada_data2 = tk.Entry(janela, width=27)
entrada_data2.pack()

botao_calcular = tk.Button(janela, text="Calcular Diferença", bg="darkblue", fg="white", font=("Times new Roman", 14), command=calcular_diferenca)
botao_calcular.pack()

# Iniciar a interface
janela.mainloop()
