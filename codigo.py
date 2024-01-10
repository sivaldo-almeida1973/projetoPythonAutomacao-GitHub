#passo a passo do projeto

#Paso 1 - Entrar no sistema da empresa
    #
#pip install pyautogui
import pyautogui
import time

#clicar -> pyautogui.click (clicar botao)
#escrever -> pyautogui.write (escrever)
#apertar uma tecla -> pyautogui.press  (apertar)
#apertar -> pyautogui.hotkey  (atalho do mac ("comand", "shift", "space"))
#pyautogui.press('win') (abrir o windows)

pyautogui.PAUSE = 0.5 # esperar 1 segundo


#aperta a tecla do windows 
pyautogui.press('win')
#digite o nome do programa
pyautogui.write('chrome')
#apertar enter
pyautogui.press('enter')

#digitar o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)


#apertar enter
pyautogui.press("enter")

#esperar 5 
time.sleep(2) 
#Passo 2 - Fazer login
pyautogui.click(x=1093, y=411)

# #digitar o e-mail
pyautogui.write("vieiralmeida.com")

# #passar para o campo de senha
pyautogui.press('tab')

# #digitar a senha
pyautogui.write("sivaldo")

# #aperta logar

pyautogui.click(x=1272, y=586)
time.sleep(2)

# #Passo 3 - importar base dados
#ptp install pandas
import pandas

tabela = pandas.read_csv("produtos.csv")
# print(tabela)

for linha in tabela.index:

    #Passo 4 - cadastrar produto
    pyautogui.click(x=1138, y=302)
    #codigo
    codigo = tabela.loc[linha, "codigo"] #couxetes
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    pyautogui.write(tabela.loc[linha, "marca"])  #parenteses e couxetes
    pyautogui.press("tab")
    #tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    #categoria (str)
    pyautogui.write(str(tabela.loc[linha, "categoria"])) #("1")
    pyautogui.press("tab")
    #preco (str)
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #custo (str)
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):  # se ele não 
      pyautogui.write(obs) # so vai executar se acima for true

    pyautogui.press("tab")
    #enviar o produto
    pyautogui.click(x=1203, y=956)

    #scroll ->rolar pagina pra cima
    pyautogui.scroll(3000)


#Passo 5 - repetir passo 4 ate acabar a base de dados