'''
Created on Sep 4, 2017

@author: raul1
'''
from cx_Freeze import setup, Executable
exe = Executable(
    script="FinalizarProcesso.py",
    base="Win32GUI",                           # Retirar comentario se for contruir um executavel para windows
    )
setup(
    name = "setup",
    version = "1",
    description = "Parar processo do winThor depois de 25s de inatividade",
    executables = [exe]
    )