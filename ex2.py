def iniciar_amizade():
    print("Início de uma amizade!\n")

def fluxo_amizade():
    resposta_comida = input("Você gostaria de comer algo (s/n)? ").lower()
    if resposta_comida == "s":
        iniciar_amizade()
        return True
    else:
        resposta_bebida = input("Você gostaria de uma bebida (s/n)? ").lower()
        if resposta_bebida == "s":
            bebida_quente = input("Poderia ser uma bebida quente (s/n)? ").lower()
            if bebida_quente == "s":
                print("Café, chá ou achocolatado?")
            else:
                print("Ofereça a bebida favorita dele, se souber.")
            iniciar_amizade()
            return True
        else:
            ultimo_interesse = ""
            for i in range(3):
                interesse = input("Me diga um interesse seu: ")
                compartilhar = input(f"Você gostaria de compartilhar esse interesse ({interesse}) comigo? (s/n): ").lower()
                ultimo_interesse = interesse
                if compartilhar == "s":
                    print(f"Vamos marcar um horário para fazer {interesse} juntos!")
                    iniciar_amizade()
                    return True
                else:
                    print("Tudo bem, vamos tentar outro...")
            # Após 3 tentativas, assume o último interesse
            print(f"Vamos marcar um horário para fazer {ultimo_interesse} juntos!")
            iniciar_amizade()
            return True

def uma_ligacao():
    while True:
        em_casa = input("Você está em casa (s/n)? ").lower()
        if em_casa == "n":
            print("Deixe uma mensagem e, quando chegar em casa, ligue para mim.")
            print("Espere ligação.")
        
        if fluxo_amizade():
            break  # Sai do loop quando amizade for iniciada

uma_ligacao()
