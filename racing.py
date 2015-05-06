class  racing (object):
    a =[]
    carrito =""
    alto = [""]
    bajo =[""]
    medio=[""]
    
    def __init__(self,a):
        print ("el carrito se llama " + a)
        self.carrito=a
    def compras (self,a,  b):
        if  b < 20 and  b<30:
            self.bajo.append(a)
            print ("se agrego  un objeto bajo")
            print (self.bajo)
        elif  b >= 20 and  b <=30:
            self.medio.append(a)
            print ("se agrego un objeto medio")
            print (self.medio)
        elif  b > 20 and  b> 30:
            self.alto.append(a)
            print ("se agrego  un objeto alto")
            print (self.alto)
        pass
    def ordenar (self):
        
        for  b  in self.alto :
            altoT=b + " "
        print ("total de alto "+altoT)
        for  b in self.medio :
            medioT = b + " "
        print ("total de medio "+medioT)
        for  b in self.bajo :
            bajoT = b + " "
        print ("total de bajo"+bajoT)
