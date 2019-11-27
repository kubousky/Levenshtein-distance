 # -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 12:49:45 2018

@author: kuba
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
    

def generate_next_row(previous_row, seq1, seq2):   
    next_row = [previous_row[0] + 1] # previous_row es la primera fila de la matriz, simpre empieza por zero, entonces su primer elemento[0] es 0. La siguiente fila empieza entonces por 1.
    for i in range(len(seq2)): #numero de columnas, o sea va a ir añadiendo siguientes elementos de la fila, numero veces de la longitud de patron - 35 veces.
        
        if seq1[previous_row[0]] == seq2[i]:
            cost = 0
        else:
            cost = 1
            
        next_int = min(
                previous_row[i + 1] + 1,
                next_row[i] + 1,
                previous_row[i] + cost
                )
        next_row.append(next_int)        
    
    return next_row

def last_row(seq1, seq2):      
    actual_row  = list(range(len(seq2)+1))
    for i in range(len(seq1)): #  numero de rows
        actual_row = generate_next_row(actual_row, seq1, seq2)         
    return actual_row[-1] # ultimo elemento (numero entero) de la ultima fila de la matriz



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
		D = last_row(seq1, seq2)        
		L = max(len(seq1), len(seq2))
		print("La distancia de Levenshtein es: " + str(D))
		print("Porcentaje de similitud entre las secuencias es: " + str(D/L*100))
		print('Time: %2.5f seconds' % (time.time() - start_time))

	else:
		help_view()    

if __name__ == "__main__":
    
    main()