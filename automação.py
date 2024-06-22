import pyautogui
import time
pyautogui.PAUSE = 0.7
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("enter")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=674, y=359)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.press("enter")
time.sleep(2)
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)
for linha in tabela.index:
    pyautogui.click(x=681, y=240)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): 
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)





































































