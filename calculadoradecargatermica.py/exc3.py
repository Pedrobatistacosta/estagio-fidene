import re

def entrada_float(mensagem):
    while True:
        valor = input(mensagem).strip()
        # Aceita apenas números, vírgula ou ponto
        if re.fullmatch(r"[0-9]+([,.][0-9]+)?", valor):
            return float(valor.replace(",", "."))
        else:
            print("Erro: Digite apenas números, usando vírgula ou ponto como separador decimal.")

def entrada_int(mensagem, minimo=None, maximo=None):
    while True:
        valor = input(mensagem).strip()
        if valor.isdigit():
            valor_int = int(valor)
            if (minimo is None or valor_int >= minimo) and (maximo is None or valor_int <= maximo):
                return valor_int
            else:
                print(f"Erro: Digite um número entre {minimo} e {maximo}.")
        else:
            print("Erro: Digite apenas números inteiros.")

def coletar_dados():
    print("Bem vindo à calculadora de carga térmica para prédios!")
    comprimento = entrada_float("Comprimento da sala (m): ")
    largura = entrada_float("Largura da sala (m): ")
    altura = entrada_float("Altura da sala (m): ")
    posicao = entrada_int("A sala está: 1 - Entre andares | 2 - Sob telhado: ", 1, 2)
    
    janelas = entrada_int("Quantidade de janelas: ")
    area_janelas = entrada_float("Área total das janelas (m²): ")
    area_portas = entrada_float("Área total das portas (m²): ")
    pessoas = entrada_int("Quantidade de pessoas que a sala comporta: ")
    voltagem_equipamentos = entrada_float("Potência total dos equipamentos elétricos (W): ")
    
    return {
        "comprimento": comprimento,
        "largura": largura,
        "altura": altura,
        "posicao": posicao,
        "janelas": janelas,
        "area_janelas": area_janelas,
        "area_portas": area_portas,
        "pessoas": pessoas,
        "voltagem_equipamentos": voltagem_equipamentos
    }

def calcular_carga(dados):
    volume = dados["comprimento"] * dados["largura"] * dados["altura"]             
    
    if dados["posicao"] == 1:
        carga_recinto = volume * 16
    else:
        carga_recinto = volume * 22.3

    carga_janelas = dados["area_janelas"] * 200
    carga_portas = dados["area_portas"] * 125
    pessoas = dados["pessoas"] * 125
    carga_equipamentos = dados["voltagem_equipamentos"] * 0.9
        
    carga_total = carga_recinto + carga_janelas + carga_portas + pessoas + carga_equipamentos
    carga_BTU = carga_total * 3.92

    return carga_total, carga_BTU
    
def recomendar_ar(btu):
    if btu <= 9000:
        return "Sugestão: Ar-condicionado de 9.000 BTUs"
    elif btu <= 12000:
        return "Sugestão: Ar-condicionado de 12.000 BTUs"
    elif btu <= 18000:
        return "Sugestão: Ar-condicionado de 18.000 BTUs"
    else:
        return "Sugestão: Ar-condicionado de mais de 18.000 BTUs"

def main():
    dados = coletar_dados()
    carga_total, carga_BTU = calcular_carga(dados)

    print(f"\nCarga térmica total: {carga_total:.2f} kcal/h")
    print(f"Carga térmica em BTUs: {carga_BTU:.2f} BTUs")
    print(recomendar_ar(carga_BTU))
    
if __name__ == "__main__":
    main()