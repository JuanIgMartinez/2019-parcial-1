#Juan I. Martinez, Legajo 57018

resto = [] 

def hexa (num):    
    for nro in str(num):
        if num < 10: 
                if num == 0:
                        pass
                else:
                        return resto.append(str(num))
        else:
                aux = num % 16
                resto.append(conversor(aux))
                return hexa(num // 16) 


def conversor(num):
        if num < 10:
                return str(num)
        elif num == 10:
                return 'A'
        elif num == 11:
                return 'B'
        elif num == 12:
                return 'C'
        elif num == 13:
                return 'D' 
        elif num == 14:
                return 'E'
        elif num == 15:
                return 'F'
            
def completo(num):
        global resto
        vacio = ''
        hexa(num)
        resto.reverse()
        final = ""
        final = vacio.join(resto)
        resto = []
        return final


#print(completo(1234))
#Borrar el comentario anterior para probar el programa