import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(2)
pyautogui.click(x=425, y=372)
pyautogui.write("exemplogmail@gmail.com")

pyautogui.press("tab")
pyautogui.write("minha senha aqui")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(1)


import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)


linha = 0



for linha in tabela.index:

    
    pyautogui.click(x=412, y=257)

    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # Obs
    # nan = not a number = vazio
    obs = tabela.loc[linha, "obs"]

    
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")

    
    pyautogui.press("enter")

    
    pyautogui.scroll(500000)

    # Repitir o processo de cadastro até acabar os produtos 