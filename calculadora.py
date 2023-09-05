#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("#==============Calculadora Simples==============")
print(' 1) Soma (+)')
print(' 2) Subtração (-)')
print(' 3) Multiplicação (*)')
print(' 4) Divisão (/)')

operacao = int(input("Qual a operação que deseja fazer?(1, 2, 3, 4):" ))

valor1 = int(input("Qual o 1º valor deseja informar?:" ))
valor2 = int(input("Qual o 2º valor que deseja?:" ))

soma = int(valor1 + valor2)
subtracao = int(valor1 - valor2)
multiplicacao = int(valor1 * valor2)  
divisao = int(valor1 / valor2)  

if operacao == 1:
    print("O resultado da operação é:", (soma))
elif operacao == 2:
    print("O resultado da operação é:", (subtracao))
elif operacao == 3:
    print("O resultado da operação é:", (multiplicacao))
elif operacao == 4:
    print("O resultado da operação é:", (divisao))
else:
    print("Por favor retorne um número de 1 a 4")

