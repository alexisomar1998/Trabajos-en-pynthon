#!/usr/bin/pynthon
from crypto.crypto import encipher_shift,decipher_shift
texto=input("ingrese su clave")
cifrado=encipher_shift(texto,1)
print(cifrado)

