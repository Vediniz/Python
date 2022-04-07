import tkinter as tk
import random, string, subprocess
from tkinter import messagebox

def gerarSenha():
    try:
        tamanhoSenha = int(entradaDados.get())
        gerandoSenha = string.ascii_letters + string.digits + '!@#$&*()-=+/\."'
        escolher = random.SystemRandom()

        global senha
        senha = (''.join(escolher.choice(gerandoSenha) for i in range(tamanhoSenha)))

        global senhaFinal 
        senhaFinal = tk.Label(janela, text = senha, bg = '#808080', fg = 'white', height = 2, font = 'bold', relief = 'groove')
        
        global copiandoSenha
        copiandoSenha = tk.Button(janela, text = 'Copiar Senha', command = copiarSenha)
        copiandoSenha.pack(side = 'bottom', pady = 1)
        senhaFinal.pack(side = 'bottom', pady = 5)
    except:
        messagebox.showerror(title = 'Error', message = 'Digite o tamanho de sua senha utilizando números!')

      #limpar a entrada do usuario
    entradaDados.delete('0', tk.END)

def limparTela():
    try:
        senhaFinal.destroy()
        copiandoSenha.destroy()

    except:
        pass

def copiarSenha():
    subprocess.run(['clip.exe'], input = senha.strip().encode('utf-16'), check = True)
      
janela = tk.Tk()

janela.title('GERADOR DE SENHA')
janela.geometry('300x200')

tk.Label(janela, text='Tamanho da senha: ').pack()

entradaDados = tk.Entry()
entradaDados.pack()

botaoGerarSenha = tk.Button(janela, text = 'Gerar Senha', command = lambda: [limparTela(), gerarSenha()])
botaoGerarSenha.pack(pady = 5)

botaoLimparTela = tk.Button(janela, text = 'Limpar Tela', command = lambda: [limparTela(), entradaDados.delete('0', tk.END)])
botaoLimparTela.pack(pady = 5)

janela.mainloop()
