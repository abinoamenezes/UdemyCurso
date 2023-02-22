import time

# Define as cores dos semáforos
VERMELHO = 'vermelho'
AMARELO = 'amarelo'
VERDE = 'verde'

# Define o tempo que cada cor ficará acesa (em segundos)
TEMPO_VERMELHO = 5
TEMPO_AMARELO = 2
TEMPO_VERDE = 5

# Função para acender uma cor e apagar as outras duas
def acender_cor(cor):
    if cor == VERMELHO:
        print('Semáforo: vermelho')
        time.sleep(TEMPO_VERMELHO)
    elif cor == AMARELO:
        print('Semáforo: amarelo')
        time.sleep(TEMPO_AMARELO)
    elif cor == VERDE:
        print('Semáforo: verde')
        time.sleep(TEMPO_VERDE)

# Loop infinito para manter o semáforo funcionando
while True:
    acender_cor(VERMELHO)
    acender_cor(AMARELO)
    acender_cor(VERDE)
