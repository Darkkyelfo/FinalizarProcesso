'''
Created on Sep 4, 2017

@author: raul1
'''
from cx_Freeze import setup, Executable
exe = Executable(
    script="FinalizarProcesso.py",
    base="Win32GUI",                           
    )
setup(
    name = "setup",
    version = "1",
    description = "Parar processo do winThor depois de 30s de inatividade",
    executables = [exe]
    )