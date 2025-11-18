from typing import TextIO

# Crea un archivo de texto con los 20 primeros números naturales.

f:TextIO = open('primeros_20.txt', 'w')

for i in range(1,21):
    f.write(str(i) + '\n')
    
f.close()
