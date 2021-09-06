import os
import sys

def carpetas(dir, pos, lista):
    a=os.listdir(dir)
    for i in a:
            string=agregar_espacio(pos)    
            if os.path.isfile(dir+"/"+str(i))==True:
                print(string+i+" -- archivo")
            if os.path.isdir(dir+"/"+str(i))==True:
                print(string+i)
                carpetas(dir+"/"+i,pos+1,lista) 
                if dir_vacio(dir+"/"+i) == 1:
                    print(agregar_espacio(pos)+"Eliminado<────┘")
                    os.rmdir(dir+"/"+i)
                    lista.append("1")
    return len(lista)

def dir_vacio(dir):
    a=os.listdir(dir)
    if not a:
        return 1
    return 0

def agregar_espacio(cantidad):
    espacio = []
    if cantidad>=0:
        for i in range(cantidad):
            espacio.append("      ")
        espacio.append("└────>")
        return ''.join(espacio)
    else:
        return ""
        
if __name__ == '__main__': 
    if len(sys.argv) > 1:  
        a=carpetas(str(sys.argv[1]),0,[])    
    else:
        path = os.getcwd()
        a=carpetas(path,0,[])
    print("\nSe eliminaron: "+str(a)+" carpetas vacias")