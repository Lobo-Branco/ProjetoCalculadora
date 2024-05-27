import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        messagebox.showerror("Erro", "Entrada inválida")
        entrada.delete(0, tk.END)

def inserir_texto(texto):
    entrada.insert(tk.END, texto)

def limpar():
    entrada.delete(0, tk.END)

def ao_apertar_enter(event):
    calcular()

def fechar_programa():
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, "Obrigado por testar!")
    root.after(3000, root.destroy)  # Fecha o programa depois de 3 segundos

root = tk.Tk()
root.title("Calculadora Lobo")
root.configure(bg='gray20')
root.iconbitmap(r'P:\VsCode\Projetos\CalculadoraPython\icon.ico')
root.resizable(False, False)  # Para manter o tamanho da calculadora fixo evitando deformações

# Configuração da entrada
entrada = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=0, relief='solid', bg='gray35', fg='white', insertbackground='white')
entrada.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipady=15)
entrada.bind('<Return>', ao_apertar_enter)  # Vincula a função de pressionar Enter = resultado

# Função para piscar o cursor no campo onde se insere os números, só frescurite minha mesmo...kk
def piscar_cursor():
    if entrada['insertbackground'] == 'white':
        entrada.config(insertbackground='gray20')
    else:
        entrada.config(insertbackground='white')
    root.after(500, piscar_cursor)

piscar_cursor()

# Definindo os botões
botoes = [
    ('/', 1, 0), ('*', 1, 1), ('-', 1, 2), ('+', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('%', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('√', 3, 3), #( botão '√' = raiz quadrada)
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('(', 4, 3),
    ('0', 5, 0), ('.', 5, 1),
]

# Aparência dos botões numéricos
num_estilo = {
    'font': ('Arial', 18),
    'bg': 'white',  # Branco
    'fg': 'black',
    'borderwidth': 4,  #  espessura do contorno
    'relief': 'solid',  # Usando 'solid' pra simular bordas arredondadas
    'width': 5,
    'height': 2,
    'highlightthickness': 4,  # espessura do contorno pra simular bordas arredondadas
}

# Aparência dos botões de operação
op_estilo = {
    'font': ('Arial', 18),
    'bg': '#6495ED',  # Azul claro
    'fg': 'black',
    'borderwidth': 4,  #  espessura do contorno
    'relief': 'solid',  # Usando 'solid' pra simular bordas arredondadas
    'width': 5,
    'height': 2,
    'highlightthickness': 4,  #  espessura do contorno pra simular bordas arredondadas
}

# Aparência dos botões especiais
esp_estilo = {
    'font': ('Arial', 18),
    'bg': '#AB82FF', # Roxo claro
    'fg': 'black',
    'borderwidth': 4,  # espessura do contorno
    'relief': 'solid',  # Usando 'solid' pra simular bordas arredondadas
    'width': 5,
    'height': 2,
    'highlightthickness': 4,  # espessura do contorno pra simular bordas arredondadas
}

for (texto, linha, coluna) in botoes:
    if texto in ['+', '-', '*', '/', '=', '%', '√', '(', ')']:  #( botão '√' = raiz quadrada)
        estilo = op_estilo if texto in ['=', 'Sair'] else esp_estilo
    else:
        estilo = num_estilo
    if texto == '=':
        btn = tk.Button(root, text=texto, command=calcular, **op_estilo)
    else:
        btn = tk.Button(root, text=texto, command=lambda t=texto: inserir_texto(t), **estilo)
    btn.grid(row=linha, column=coluna, padx=5, pady=5)

# Botão para limpar "C"
btn_limpar = tk.Button(root, text='C', command=limpar, **esp_estilo)
btn_limpar.grid(row=5, column=2, padx=5, pady=5)

# Botão para sair
btn_sair = tk.Button(root, text='Sair', command=fechar_programa, **op_estilo)
btn_sair.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky='we')

# Botão de parênteses direito
btn_parenteses = tk.Button(root, text=')', command=lambda: inserir_texto(')'), **esp_estilo)
btn_parenteses.grid(row=5, column=3, padx=5, pady=5)

# Botão de igual
btn_igual = tk.Button(root, text='=', command=calcular, **op_estilo)
btn_igual.grid(row=6, column=2, columnspan=2, padx=5, pady=5, sticky='we')

root.mainloop()
