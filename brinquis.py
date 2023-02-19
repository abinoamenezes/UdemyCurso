import time

def semaforo():
    while True:
        print("Sinal vermelho")
        time.sleep(5)
        print("Sinal amarelo")
        time.sleep(2)
        print("Sinal verde")
        time.sleep(5)

semaforo()