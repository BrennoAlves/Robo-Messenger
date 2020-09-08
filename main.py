import pyautogui as pg
import time as t

#script de teste da PyAutoGUI
#ele foi feito pensado em uma tela FullHD de notebook (1920 x 1080)
#ele envia mensagem iguais repetidamente pelo messenger.com

pg.moveTo(x=1836,y=42)
pg.click()
#minimizando o vscode
#o navegador deve estar aberto em um plano atrás do vscode

pg.moveTo(x=114, y=43)
pg.click()
#abrindo a aba do facebook (messenger)
#vai enviar para a conversa que estiver aberta

pg.moveTo(x=641, y=1056)
pg.click()
t.sleep(0.3)
#abrindo a area de digitação

n = 0
while n < 50:
    pg.write('Teste', interval= 0)
    t.sleep(0.2)
    pg.moveTo(x=1473, y=1054)
    t.sleep(0.2)
    pg.click()
    n += 1
#enviar a mensagem 'teste' n vezes

pg.write('Enviado automaticamente por TravaZAP', interval= 0.2)
pg.click()
#enviar uma mensagem de desfecho 

pg.alert('Trabalho feito')
