def uma_ligacao():
    em_casa = input("Você está em casa (s/n)? ").lower()
    if em_casa == "s":
        bebida_quente = input("Poderia ser uma bebida quente (s/n)? ").lower()
        if bebida_quente == "s":
            print("Café, chá ou achocolatado?")
        else:
            print("Ofereça qualquer outra bebida.")
        print("Início de uma amizade!")
    else:
        print("Deixe uma mensagem.")
        print("Espere ligação.")
        print("Início de uma amizade!")
def atividade_recreacionista():
    for i in range(3):
        interesse = input("me diga um interrese seu:")
        compartilhar_interesse = input(f"Voce gostaria de compartilhar esse interesse ({interesse}) comigo?")
        if compartilhar_interesse == "s":
            print(f"participe do interesse {interesse}!")
            print("Inicio de uma amizade!")
            return
    print("LOA-Laco de oportunidade amizade encerrado.")
def algoritmo_de_amizade():
    primeira_parte = input("Voce gostaria de comecar com uma bebida (s/n)?").lower()
    if primeira_parte == "s":
      uma_ligacao()
    else:
        atividade_recreacionista()

algoritmo_de_amizade()