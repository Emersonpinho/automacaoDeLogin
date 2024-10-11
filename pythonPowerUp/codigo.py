# Passo 1: Entrar no sistema de Empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time


# pyautogui.write -> escrever um texto
# pyautogui.click -> Clicar com mause
# pyautogui.press -> Aperta uma tecla
# pyautogui.hotkey -> Aperta um atalho de teclado (ctl + c)

pyautogui.PAUSE = 0.5

# Abrir o Navegador
# Aperta a tecla win
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)

# Entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
 
# Passo 2: Fazer login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# quero dar pausa de 3 segundos

time.sleep(2)
pyautogui.click(x=425, y=372)
pyautogui.write("exemplogmail@gmail.com")

# Passar para o próximo campo
pyautogui.press("tab")
pyautogui.write("minha senha aqui")

# Aperta no botão de logar
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(1)

# Passo 3: Importa base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar um produto
linha = 0

#para cada linha da minha tabela

for linha in tabela.index:

    # selecionar o primeiro campo
    pyautogui.click(x=412, y=257)

    # Codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # Marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # Preço unitario
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    # Custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # Obs
    # nan = not a number = vazio
    obs = tabela.loc[linha, "obs"]

    # se(if) o pandas não ta vazio:
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")

    # Clica no botão enviar
    pyautogui.press("enter")

    # Rolar a tela pra cima
    pyautogui.scroll(500000)

    # Passo 5: Repitir o processo de cadastro até acabar os produtos 