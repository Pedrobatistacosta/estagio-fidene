import re
from fpdf import FPDF

def entrada_float(mensagem):
    while True:
        valor = input(mensagem).strip()
        if re.fullmatch(r"[0-9]+([,.][0-9]+)?", valor):
            return float(valor.replace(",","."))
        else:
            print("Erro: Por favor, digite apenas numeros, usando virgula ou ponto como separador decimal.")

def entrada_int(mensagem, minimo=None, maximo=None):
    while True:
        valor = input(mensagem).strip()
        if valor.isdigit():
            valor_int = int(valor)
            if (minimo is None or valor_int >= minimo) and (maximo is None or valor_int <= maximo):
                return valor_int
            else:
                print(f"Erro: Por favor, digite um numero entre {minimo} e {maximo}.")
        else:
            print("Erro: Por favor, digite apenas numeros inteiros.")

def coletar_dados():
    print("Bem vindo a calculadora de carga termica para predios, vamos coletar alguns dados para selecionar o ar-condicionado indicado para o seu ambiente.")
    comprimento = entrada_float(input("Me diga o comprimento da sala designada (em metros): ").replace(",", "."))
    largura = entrada_float(input("Agora me diga a largura dessa sala ( em metros): ").replace(",", "."))
    altura = entrada_float(input("E por fim, me diga a altura da sala ( em metros): ").replace(",","."))
    posicao = entrada_int(input("A sala esta: 1 - Entre andares, 2- Sob telhado: "), 1, 2)
    janelas = entrada_int(input("Quantas janelas existem na sala? "))
    area_janelas = entrada_float(input("Qual a area total das janelas (em metros quadrados)? ").replace(",","."))
    area_portas = entrada_float(input("Qual a area total da(s) porta(s) (em metros quadrados)? ").replace(",","."))
    pessoas = entrada_int(input("Quantas pessoas esta sala comporta? "))
    voltagem_equipamentos = entrada_float(input("Qual a potencia total que os equipamentos eletricos da sala comportam (em Watts)? ").replace(",","."))
    horas_uso = entrada_float(input("Quantas horas por dia voce planeja usar o ar-condicionado? ").replace(",", "."))

    return {
        "comprimento": comprimento,
        "Largura": largura,
        "altura": altura,
        "posicao": posicao,
        "janelas": janelas,
        "area_janelas": area_janelas,
        "area_portas": area_portas,
        "pessoas": pessoas,
        "voltagem_equipamentos": voltagem_equipamentos,
        "horas_uso": horas_uso
    }
        
                                       
def calcular_carga(dados):
    volume = dados["comprimento"] * dados["Largura"] * dados["altura"]             
    
    if dados["posicao"] == 1:
        carga_recinto = volume *16
    else:
        carga_recinto = volume * 22.3

    carga_janelas = dados["area_janelas"] * 200
    carga_portas = dados["area_portas"] *125
    pessoas = dados["pessoas"] * 125

    carga_equipamentos = dados["voltagem_equipamentos"] *0.9
        
    carga_total = carga_recinto + carga_janelas + carga_portas + pessoas + carga_equipamentos
    carga_BTU = carga_total * 3.92

    return carga_total, carga_BTU
    
def recomendar_ar(btu):
    if btu <= 9000:
        return "Sugestao: Ar-condicionado de 9.000 BTUs, link de sugestao de ar-condicionado:https://amzn.to/4oCHYn2" 
    elif btu <= 12000:
        return "Sugestao: Ar-condicionado de 12.000 BTUs, link de sugestao de ar-condicionado: https://amzn.to/3JhDYIA"
    elif btu <= 18000:
        return "Sugestao: Ar-condicionado de 18.000 BTUs, link de sugestao de ar-condicionado: https://amzn.to/4mBKYy6"
    elif btu > 18000:
        return "Sugestao, Ar-condicionado de mais de 18.000 BTUs, link de sugestao de ar-condicionado: https://amzn.to/4mNiEZT" 
    else:
        return "Erro: Carga BTU invalida."

def calcular_custo(btu, horas_uso, tarifa=0.95):
    consumo_diario = (btu / 1000) * horas_uso 
    consumo_mensal = consumo_diario * 30
    custo = consumo_mensal *tarifa
    return consumo_mensal, custo

def gerar_pdf(dados, carga_total, carga_BTU, recomendacao, consumo_mensal, custo):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0,10, "Relatorio de Carga Termica", ln=True, align="c")
    pdf.set_font("arial", '', 12)
    
    for chave, valor in dados.items():
        pdf.cell(0,8, f"{chave.capitalize()}: {valor}", ln=True)
        pdf.cell(0,8, f"Carga termica total: {carga_total:.2f} kcal/h", ln=True)
        pdf.cell(0,8, f"Carga termica em Btus: {carga_BTU:.2f}", ln=True)
        pdf.cell(0,8, recomendacao, ln=True)
        pdf.cell(0,8, f"Consumo mensal: {consumo_mensal:.2f} kWh", ln=True)
        pdf.cell(0,8, f"Custo estimado: R$ {custo:.2f}", ln=True)

        pdf.output("relatorio_carga_termica.pdf")
        print("\nRelatorio gerado com sucesso: relatorio_carga_termica.pdf")

def main():
    dados = coletar_dados()
    carga_total, carga_BTU = calcular_carga(dados)
    recomendacao = recomendar_ar(carga_BTU)
    consumo_kw, custo = calcular_custo(carga_BTU, dados["horas_uso"])

    print(f"\nCarga térmica total: {carga_total:.2f} kcal/h")
    print(f"Carga térmica em BTUs: {carga_BTU:.2f}")
    print(recomendacao)
    print(f"Consumo mensal: {consumo_kw:.2f} kWh")
    print(f"Custo mensal estimado: R$ {custo:.2f}")

    gerar_pdf(dados, carga_total, carga_BTU, recomendacao, consumo_kw, custo)

if __name__ == "__main__":
    main()