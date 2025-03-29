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
print(pyautogui.locateCenterOnScreen('nome.PNG'))
pyautogui.click(1094,447)
pyautogui.typewrite('Victor Gaia')

## 3) Clique em alerta, para gerar a alerta
print(pyautogui.locateCenterOnScreen('alerta.PNG'))
pyautogui.click(1057,485)
sleep(0.5)

## 4) Feche a alerta
pyautogui.press('enter')

## 5) Suba a página totalmente para cima
pyautogui.hotkey('ctrl','home')

## 6) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos 
# para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
## --> Vamos encontrar o text e depois mover o mouse até o botão de download, não podemos localizar pois os botões
# são exatamente iguais

pyautogui.hotkey('ctrl','f')
sleep(2)
pyautogui.typewrite('Planilha Excel')
pyautogui.press('esc')
print(pyautogui.locateCenterOnScreen('excel.PNG'))
pyautogui.click(198,404+50)
sleep(2)
pyautogui.press('enter')
sleep(1)
pyautogui.press('esc')

pyautogui.hotkey('ctrl','f')
sleep(2)
pyautogui.typewrite('Arquivo PDF')
pyautogui.press('esc')
print(pyautogui.locateCenterOnScreen('arquivo_pdf.PNG'))
pyautogui.click(384,404+50)
sleep(2)
pyautogui.press('enter')
sleep(1)
pyautogui.press('esc')


pyautogui.hotkey('ctrl','f')
sleep(2)
pyautogui.typewrite('Arquivo Docx')
pyautogui.press('esc')
print(pyautogui.locateCenterOnScreen('arquivo_docx.PNG'))
pyautogui.click(579,404+50)
sleep(2)
pyautogui.press('enter')
sleep(1)
pyautogui.press('esc')

pyautogui.hotkey('ctrl','f')
sleep(2)
pyautogui.typewrite('Arquivo de Texto')
pyautogui.press('esc')
print(pyautogui.locateCenterOnScreen('arquivo_de.PNG'))
pyautogui.click(757,404+60)
sleep(2)
pyautogui.press('enter')
sleep(1)
pyautogui.press('esc')

pyautogui.hotkey('ctrl','f')
sleep(2)
pyautogui.typewrite('Arquivo CSV')
pyautogui.press('esc')
print(pyautogui.locateCenterOnScreen('csv.PNG'))
pyautogui.click(953,404+50)
sleep(2)
pyautogui.press('enter')
sleep(1)
pyautogui.press('esc')

pyautogui.hotkey('ctrl','f')
sleep(2)
pyautogui.typewrite('Arquivo JSON')
pyautogui.press('esc')
print(pyautogui.locateCenterOnScreen('json.PNG'))
pyautogui.click(1121,418+60)
sleep(2)
pyautogui.press('enter')
sleep(1)
pyautogui.press('esc')

## 7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"
pyautogui.alert('VOCÊ TERMINOU, Parabéns! Valeu Johnatan')