


class Persona(object):

    def __init__(self, nom, hobs, ed):
        self.nombre = nom
        self.hobbies = hobs
        self.edad = ed
        
    def __str__(self):
        return "Persona " + self.nombre

    

class Rancho(object):

    def __init__(self, pers):
        self.personas = pers

    def __str__(self):
        return str(len(self.personas))

    def hobbies(self):
        h = []
        for pers in self.personas:
            h.extend(pers.hobbies)

        hobs = set(h)
        #print("Los hobbies son {}".format(hobs))

        totales = {}
        for hob in hobs:
            cant = h.count(hob)
            totales[hob] = cant

        return totales
            
        


class Plaza(object):

    def __init__(self, direc, rancho):
        self.rancho = rancho
        self.direccion = direc
        print("Inicializando")

    def __str__(self):
        return "Plaza en " + self.direccion

    def potencialidad(self, pers):
        hobs = self.rancho.hobbies()

        l = []
        for h in pers.hobbies:
            if h in hobs:
                l.append(h)

        if len(l) == 0:
            print('Meh...')

        if len(l) == 1:
            print('Ah puede ser')

        if len(l) == 2:
            print('De una wachin bienvenidx')

        return l
        

    def dir(self):
        print(self.direccion)


vladi = Persona("Vladi",['malabarear','programar','cubo'],26)
chino = Persona("Chino",['malabarear','skate','cubo'],25)
enzo  = Persona("Enzo", ['cubo','jardineria'],30)
mart  = Persona("Martina", ['skate','fotografia','indumentaria'],32)

ran = Rancho([vladi,chino,enzo,mart])

p = Plaza("Las casas y Congreso", ran)



chaboncito_bien = Persona("Marcos",['fotografia','cubo'],16)
chaboncito_cualca = Persona("Andrea", ['danza','folklore'],37)



#p.potencialidad(chaboncito_bien)
#p.potencialidad(chaboncito_cualca)
