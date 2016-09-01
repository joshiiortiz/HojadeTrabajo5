#
#Joseline Ortiz

from SimPy.Simulation import *
from random import uniform, Random

#new: el proceso llega al sistema operativo pero debe esperar que se le asigne
#memoria RAM. En nuestra simulación el proceso solicitará una cantidad de memoria
#(número entero al azar entre 1 y 10). Si hay memoria disponible puede pasar al
#estado de ready. En caso contrario permanece haciendo cola, esperando por
#memoria. NOTA: la cantidad de memoria disponible se disminuye con la cantidad
#de memoria que empleará el proceso que logró obtenerla.

#ready: el proceso está listo para correr pero debe esperar que lo atienda el CPU.
#El proceso tiene un contador con la cantidad de instrucciones totales a realizar
#(número entero al azar entre 1 y 10). Cuando se desocupa el CPU puede pasar a
#utilizarlo.

#running: el CPU atiende al proceso por un tiempo limitado, suficiente para
#realizar solamente 3 instrucciones (esto será configurado, ya que podrá crecer
#o reducirse). Al completarse el tiempo de atención el proceso es retirado del
#CPU. Se debe actualizar el contador de instrucciones a realizar, disminuyendo
#las 3 instrucciones que ejecutó en esta oportunidad. Si el proceso tiene menos
#de tres instrucciones que le hace falta procesar, libera el CPU anticipadamente.

#Al finalizar la atención del CPU puede ocurrir:
#a)Terminated: Si el proceso ya no tiene instrucciones por realizar entonces pasa
#al estado “terminated” y sale del sistema.
#b)Waiting: al dejar el CPU se genera un número entero al azar entre 1 y 2 . Si
#es 1 entonces pasa a la cola de Waiting para hacer operaciones de I/O
#(entrada/salida). Al dejar esa cola regresa a “ready”.
#c)Ready: al dejar el CPU y el número generado al azar es 2 entonces se dirige
#nuevamente a la cola de “ready”.

#La creación de procesos sigue una distribución exponencial con intervalo = 10.
#Recordar que entonces se generan los números al azar para simular la llegada de
#procesos con: random.expovariate(1.0 / interval)

#La cantidad de memoria RAM de la computadora es 100. Se usa un recurso tipo
#Container  para simular la memoria. Se debe hacer cola para solicitar la
#cantidad de memoria necesaria y se permanece en la cola hasta que se obtenga esa
#cantidad. Al finalizar un proceso se regresa la cantidad de memoria que utilizó.

#La velocidad del CPU se modela con que atiende un proceso en una 1 unidad de
#tiempo, lo cual permite realizar tres instrucciones. Esto debe ser variable, ya
#que podríamos decir luego que tenemos un procesador más rápido que ejecuta más
#instrucciones en esa unidad de tiempo. El CPU es modelado con una cola tipo
#Resource (capacidad = 1, es decir un solo CPU).

#NOTA: para la generación de los números al azar utilice una semilla para que se
#genere siempre la misma secuencia y así se puedan hacer comparaciones cuando se
#cambien los parámetros de la simulación: random.seed(RANDOM_SEED)

class proceso(Process):
    def __init__(self,id):
        Process.__init__(self)
        self.name=id

    def new(self,tiempoEspera, cpuEspera):
        yield hold,self,tiempoEspera
        self.llega = now()
        #Solicitud de cantidad de memoria
        memoria = random.randint(1, 10)
        #Compara si memoria esta disponible
        if (memoria):
            #Se va a ready
            print "el proceso ",self.id," hace cola "
            yield request,self,
            print "%5.1f %s espera a pasar a ready %d" %(now(),self.id, self.turno)
        else:
            #Sigue esperando
                

        # ya ingreso, ahora a buscar un parqueo:
            yield request,self,cpu
            print "%5.1f %s gets space" %(now(),self.id)
            yield hold,self,cpuEspera
            tiempoTotal = now() - self.llega
            wt.observe(tiempoTotal)
            print "%5.1f %s releases space after %5.1f procesado TTotal= %5.1f" %(now(),self.id,cpuEspera,tiempoTotal)
            yield release,self,cpu 

    def ready():
        #Solicitud de cantidad de intrucciones totales a realizar
        contador = random.randint(1, 10)

    def running():
        #Ir al CPU
        if (contador >= 3):
            #Actualizacion del contador
            contador = contador - 3
        elif(condador < 3):
            #Salir del CPU

            numero = random.randint(1,2)
    
        if (contador <3):
            estado = "terminated"
            #Salir del programa

        elif (numero == 1):

            print "el proceso ",self.id," hace cola "
            yield request,self,
            print "%5.1f %s espera a pasar a ready %d" %(now(),self.id, self.turno)
            #Pasa a la cola de Waiting
            #Al salir ... pasa a Ready

        elif (numero == 2):
            print "el proceso ",self.id," hace cola "
            yield request,self,
            #Pasa a la cola de Ready
            
#cpuEspera = 2


simulate(until=100)
