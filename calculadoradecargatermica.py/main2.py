import re
from fpdf import FPDF

# Função de entrada validando apenas números com vírgula ou ponto
def entrada_float(mensagem):
    while True:
        valor = input(mensagem).strip()
        if re.fullmatch(r"[0-9]+([,.][0-9]+)?", valor):
            return float(valor.replace(",", "."))
        else:
            print("Erro: Digite apenas números, usando vírgula ou ponto.")

def entrada_int(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor.isdigit():
            return int(valor)
        else:
            print("Erro: Digite apenas números inteiros.")

# Coletar dados do ambiente
def coletar_dados():
    print("=== Calculadora de Carga Térmica ===")
    comprimento = entrada_float("Comprimento da sala (m): ")
    largura = entrada_float("Largura da sala (m): ")
    altura = entrada_float("Altura da sala (m): ")
    posicao = entrada_int("1 - Entre andares, 2 - Sob telhado: ")
    janelas = entrada_int("Quantidade de janelas: ")
    area_janelas = entrada_float("Área total das janelas (m²): ")
    area_portas = entrada_float("Área total das portas (m²): ")
    pessoas = entrada_int("Quantidade de pessoas: ")
    potencia_equip = entrada_float("Potência total dos equipamentos (W): ")
    horas_uso = entrada_float("Horas de uso diário do ar-condicionado: ")

    return {
        "comprimento": comprimento,
        "largura": largura,
        "altura": altura,
        "posicao": posicao,
        "janelas": janelas,
        "area_janelas": area_janelas,
        "area_portas": area_portas,
        "pessoas": pessoas,
        "potencia_equip": potencia_equip,
        "horas_uso": horas_uso
    }

# Calcular carga térmica
def calcular_carga(dados):
    volume = dados["comprimento"] * dados["largura"] * dados["altura"]
    carga_recinto = volume * (16 if dados["posicao"] == 1 else 22.3)
    carga_janelas = dados["area_janelas"] * 200
    carga_portas = dados["area_portas"] * 125
    carga_pessoas = dados["pessoas"] * 125
    carga_equip = dados["potencia_equip"] * 0.9

    carga_total = carga_recinto + carga_janelas + carga_portas + carga_pessoas + carga_equip
    carga_BTU = carga_total * 3.92
    return carga_total, carga_BTU

# Recomendar ar-condicionado com links encurtados
def recomendar_ar(btu):
    if btu <= 9000:
        return "Sugestão: 9.000 BTUs -> https://bit.ly/ar9000"
    elif btu <= 12000:
        return "Sugestão: 12.000 BTUs -> https://bit.ly/ar12000"
    elif btu <= 18000:
        return "Sugestão: 18.000 BTUs -> https://bit.ly/ar18000"
    else:
        return "Sugestão: acima de 18.000 BTUs -> https://bit.ly/ar32000"

# Calcular custo mensal
def calcular_custo(btu, horas_uso, tarifa=0.95):
    consumo_kw = (btu / 3412) * horas_uso * 30  # BTU → kWh
    custo = consumo_kw * tarifa
    return consumo_kw, custo

# Gerar relatório em PDF
def gerar_pdf(dados, carga_total, carga_BTU, recomendacao, consumo_kw, custo):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Relatório de Carga Térmica", ln=True, align="C")
    pdf.set_font("Arial", '', 12)

    for chave, valor in dados.items():
        pdf.cell(0, 8, f"{chave.capitalize()}: {valor}", ln=True)

    pdf.cell(0, 8, f"Carga térmica total: {carga_total:.2f} kcal/h", ln=True)
    pdf.cell(0, 8, f"Carga térmica em BTUs: {carga_BTU:.2f}", ln=True)
    pdf.cell(0, 8, recomendacao, ln=True)
    pdf.cell(0, 8, f"Consumo mensal: {consumo_kw:.2f} kWh", ln=True)
    pdf.cell(0, 8, f"Custo estimado: R$ {custo:.2f}", ln=True)

    pdf.output("relatorio_carga_termica.pdf")
    print("\nRelatório salvo como 'relatorio_carga_termica.pdf'.")

# Função principal
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
