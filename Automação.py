# importando bibliotecas necessárias

import pyautogui
import pandas as pd
import time

# Acessando o navegador e acessando o site

pyautogui.PAUSE = 0.4
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")  
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

# fazendo login no sistema

pyautogui.click(x=747, y=356)
pyautogui.write("testeautomacao@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhadeteste")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# importando a base de dados dos produtos

tabela = pd.read_csv("produtos.csv")

# cadastrando os produtos 

for linha in tabela.index:
    pyautogui.click(x=823, y=242)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    if not pd.isna(tabela.loc[linha, "obs"]):               # condição para que não seja cadastrado no sistema "NaN" nos valores vazios de "Obs" da tabela
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)