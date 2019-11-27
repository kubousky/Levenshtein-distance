# -*- coding: utf-8 -*-
"""
Created

@author: Jakub Parcheta
"""

import time
import sys



def read_file(name):

    print ("Leyendo {}...".format(name))
    seq = ""
    try:
        file = open(name,"r")
    except:
        print ("El fichero {} no existe.".format(name))
        print ("Cerrando programa.")
        sys.exit()
    else:       
        for line in file:
            if ">" not in line:
                line = line.strip()
                seq += line
        print ("La secuencia de {} ha sido cargada.".format(name))
        file.close()
        return seq

def help_view():
    print()
    print('-h help')
    print('-ld <file.fa> patron.txt')
    print()
    print("Choose a file.fa between the followings:")
    print("                                         - B_lambda.fa")
    print("                                         - M_pharaonis.fa")
    print("                                         - P_falciparum.fa")
    print()




def levenshtein(seq1, seq2):

    rows = len(seq1)+1  # porque el index empieza de 0
    cols = len(seq2)+1
    matrix = [[0 for x in range(cols)] for x in range(rows)] # crea la matriz  de 'zeros'
                                                                                                #[1,     0,..]
    for i in range(1, rows): #  crea la primera columna, de 0 hasta la longitud de la seq1 + 1: #[2,     0,..], 
        matrix[i][0] = i                                                                        #[..,    0,..],
                                                                                                #[seq1+1,0,..], etc.
    for i in range(1, cols): # crea primer entero row. A partir de segundo zero, los sustituye con 1, 2, 3, y asi sucesivamente creando [0, 1, 2, 3, 4, .., len(seq2)+1 ]
        matrix[0][i] = i
    #print(matrix)    
    for col in range(1, cols):
        for row in range(1, rows):
            if seq1[row-1] == seq2[col-1]:
                cost = 0
            else:
                cost = 1
            matrix[row][col] = min(matrix[row-1][col] + 1,      # deletion
                                 matrix[row][col-1] + 1,        # insertion
                                 matrix[row-1][col-1] + cost)   # substitution
 
    return matrix[row][col]

def main():    
	if len(sys.argv) == 4:
		print('*' * 80)    
		print('Algoritmo Levensthein para búsqueda de similitudes entre sequencias'.center(80))
		print('Versión Secuencial'.center(80))
		print('*' * 80)

		seq1 = read_file(sys.argv[2]) # row
		seq2 = read_file(sys.argv[3]) # column

		print('')
		print('Calculando la distancia de Levensthein...')
		print('')

		start_time = time.time()
		D = levenshtein(seq1, seq2)        
		L = max(len(seq1), len(seq2))
		print("La distancia de Levenshtein es: " + str(D))
		print("Porcentaje de similitud entre las secuencias es: " + str(D/L*100))
		print('Time: %2.5f seconds' % (time.time() - start_time))
	else:
		help_view()    

if __name__ == "__main__":
    
    main()

