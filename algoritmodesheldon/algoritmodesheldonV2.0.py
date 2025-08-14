import os
import time

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")
    
def iniciar_amizade():
    print("Inicio de uma amizade!\n")
    time.sleep(1)

def entrada_sn(mensagem):
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta in ["s", "n"]:
            return resposta
        print('Por favor, responda apenas com "s" ou "n".')
        time.sleep(1)

def fluxo_amizade():
    resposta_comida = entrada_sn("Voce gostaria de comer algo (s/n)? ")
    if resposta_comida == "s":
        print ("Entao vamos marcar um horario para comer juntos e conversarmos!")
        iniciar_amizade()
        return True
    else:
        resposta_bebida = entrada_sn("Voce gostaria de uma bebida (s/n) ? ")
        if resposta_bebida == "s":
            bebidas = ["Cafe", "cha", "achocolatado"]
            for bebida in bebidas:
               quer = entrada_sn(f"Voce gostaria de {bebida}? (s/n): ")
               if quer == "s":
                  print(f"vamos sair tomar um {bebida} algum dia entao!, so marcar!")
                  time.sleep(1) 
                  iniciar_amizade()
                  return True
            print("Tudo bem!, vamos pensar e alguma outra coisa para fazer!")
        ultimo_interesse = ""
        for i in range(3):
            interesse = input("Me diga um interesse seu: ")
            compartilhar = entrada_sn(f'Voce gostaria de compartilhar esse interesse ({interesse}) comigo? (s/n): ')
            ultimo_interesse = interesse
            if compartilhar == "s":
                print(f"Vamos marcar um horario pra {interesse} juntos!")
                time.sleep(1)
                iniciar_amizade()
                return True
            else:
                print("Eu insisto!")
                time.sleep(1)
        print(f"Voce insiste, mas mesmo assim vou marcar um horario para fazer {ultimo_interesse} juntos!")
        time.sleep(1)
        iniciar_amizade()
        return True

def uma_ligacao():
    while True:
        limpar_tela()
        em_casa = entrada_sn("voce esta em casa (s/n)? ")
        if em_casa == "n":
                    print("Deixe uma mensagem e, quando chegar em casa, ligue para mim.")
                    print("Espere a ligacao.\n")
        if fluxo_amizade():
            break
                

uma_ligacao()