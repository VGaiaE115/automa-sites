#Desafio - criar uma automação para navegador usando pyautogui
## DESAFIO 🥇
## 1) Navegue até o site https://cursoautomacao.netlify.app/
## 2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
## 3) Clique em alerta, para gerar a alerta
## 4) Feche a alerta
## 5) Suba a página totalmente para cima
## 6) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
## 7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"

#Importar pyautogui
import pyautogui
#Importar função sleep para pausas
from time import sleep

#1) Navegue até o site https://cursoautomacao.netlify.app/ --> importar funções de navegador
import webbrowser
webbrowser.open_new_tab('https://cursoautomacao.netlify.app/')
sleep(4)

#2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
pyautogui.hotkey('ctrl','f')
sleep(2)
pyautogui.typewrite('Exemplos Alertas')
sleep(0.5)
pyautogui.press('esc')
sleep(0.5)
digite_nome = pyautogui.locateCenterOnScreen('nome.PNG')
pyautogui.click(digite_nome[0],digite_nome[1],duration=1)
pyautogui.typewrite('Victor Gaia')

## 3) Clique em alerta, para gerar a alerta
botao_alerta = pyautogui.locateCenterOnScreen('alerta.PNG')
pyautogui.click(botao_alerta[0],botao_alerta[1])
sleep(0.5)

## 4) Feche a alerta
pyautogui.press('enter')

## 5) Suba a página totalmente para cima
pyautogui.hotkey('ctrl','home')

## 6) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos 
# para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.

pyautogui.hotkey('ctrl','f')
sleep(2)
pyautogui.typewrite('Planilha Excel')
pyautogui.press('esc')
excel = pyautogui.locateCenterOnScreen('excel.PNG')
pyautogui.click(excel[0],excel[1]+50)
sleep(2)
pyautogui.press('enter')
sleep(1)
pyautogui.press('esc')

pyautogui.hotkey('ctrl','f')
sleep(2)
pyautogui.typewrite('Arquivo PDF')
pyautogui.press('esc')
pdf = pyautogui.locateCenterOnScreen('arquivo_pdf.PNG')
pyautogui.click(pdf[0],pdf[1]+50)
sleep(2)
pyautogui.press('enter')
sleep(1)
pyautogui.press('esc')


pyautogui.hotkey('ctrl','f')
sleep(2)
pyautogui.typewrite('Arquivo Docx')
pyautogui.press('esc')
docx = pyautogui.locateCenterOnScreen('arquivo_docx.PNG')
pyautogui.click(docx[0],docx[1]+50)
sleep(2)
pyautogui.press('enter')
sleep(1)
pyautogui.press('esc')

pyautogui.hotkey('ctrl','f')
sleep(2)
pyautogui.typewrite('Arquivo de Texto')
pyautogui.press('esc')
png = pyautogui.locateCenterOnScreen('arquivo_de.PNG')
pyautogui.click(png[0],png[1]+60)
sleep(2)
pyautogui.press('enter')
sleep(1)
pyautogui.press('esc')

pyautogui.hotkey('ctrl','f')
sleep(2)
pyautogui.typewrite('Arquivo CSV')
pyautogui.press('esc')
csv = pyautogui.locateCenterOnScreen('csv.PNG')
pyautogui.click(csv[0],csv[1]+50)
sleep(2)
pyautogui.press('enter')
sleep(1)
pyautogui.press('esc')

pyautogui.hotkey('ctrl','f')
sleep(2)
pyautogui.typewrite('Arquivo JSON')
pyautogui.press('esc')
json= pyautogui.locateCenterOnScreen('json.PNG')
pyautogui.click(json[0],json[1]+60)
sleep(2)
pyautogui.press('enter')
sleep(1)
pyautogui.press('esc')

## 7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"
pyautogui.alert('VOCÊ TERMINOU, Parabéns! Valeu Johnatan')