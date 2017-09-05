#-*-coding:utf-8-*-
u'''
Created on Sep 1, 2017

@author: Raul Sousa
Codigo responsavel por finalizar um processo apos um tempo de inatitividade do usuario(Funciona somente no windows) 
'''

import os
import sys
from ctypes import cdll
import time
import threading

class FinalizarProcesso(object):
    
    def __init__(self,processo = "PCINF000",tempoFechar = 30):
        self.tempo = 0
        self.tempoFechar = tempoFechar
        self.processo = processo
        self.keys = list(range(2,54))
        t = threading.Thread(target=self.__worker)
        t.start()
        self.detectarEvento()
        
    def __worker(self):
        while(True):
            time.sleep(1)
            self.tempo = self.tempo + 1
            if(self.tempo == self.tempoFechar):# se atingir o tempo fecha o winthor
                os.system("taskkill /im  %s.EXE"%self.processo)
                self.__zerarTempo()
            #print (self.tempo)
            
    def __zerarTempo(self):
        self.tempo = 0
    
    def detectarEvento(self):#Fonte: https://gist.github.com/inaz2/541da967ad04d06b975e
        GetAsyncKeyState = cdll.user32.GetAsyncKeyState
        special_keys = {0x08: "BS", 0x09: "Tab", 0x0d: "Enter", 0x10: "Shift", 0x11: "Ctrl", 0x12: "Alt", 0x14: "CapsLock", 0x1b: "Esc", 0x20: "Space", 0x2e: "Del"}
        # reset key states
        for i in range(256):
            GetAsyncKeyState(i)
        while True:
            for i in range(256):
                if GetAsyncKeyState(i) & 1:
                    if i in special_keys:#teclas especiais 
                        self.__zerarTempo()
                       # print ("<%s>" % special_keys[i])
                    elif 0x30 <= i <= 0x5a:#Teclas letras
                        self.__zerarTempo()
                       # print ("%c" % i)
                    else:#click do mouse
                        self.__zerarTempo()
                       # print ("[%02x]" % i)
            sys.stdout.flush()  
            time.sleep(0.001)
    
a = FinalizarProcesso("PCINF000")


    
