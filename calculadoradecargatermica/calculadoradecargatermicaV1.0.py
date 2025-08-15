def coletar_dados():
    print("Bem vindo a calculadora de carga termica para predios, vamos coletar alguns dados para selecionar o ar-condicionado indicado para o seu ambiente.")
    comprimento = float(input("Me diga o comprimento da sala designada (em metros): ").replace(",", "."))
    largura = float(input("Agora me diga a largura dessa sala ( em metros): ").replace(",", "."))
    altura = float(input("E por fim, me diga a altura da sala ( em metros): ").replace(",","."))
    posicao = int(input("A sala esta: 1 - Entre andares, 2- Sob telhado: "))
    
    janelas = int(input("Quantas janelas existem na sala? "))
    area_janelas = float(input("Qual a area total das janelas (em metros quadrados)? ").replace(",","."))

    area_portas = float(input("Qual a area total da(s) porta(s) (em metros quadrados)? ").replace(",","."))
    pessoas = int(input("Quantas pessoas esta sala comporta? "))
    voltagem_equipamentos = float(input("Qual a potencia total que os equipamentos eletricos da sala comportam (em Watts)? ").replace(",","."))
    
    return {
        "comprimento": comprimento,
        "Largura": largura,
        "altura": altura,
        "posicao": posicao,
        "janelas": janelas,
        "area_janelas": area_janelas,
        "area_portas": area_portas,
        "pessoas": pessoas,
        "voltagem_equipamentos": voltagem_equipamentos
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
        return "Sugestao: Ar-condicionado de 9.000 BTUs, link de sugestao de ar-condicionado: https://www.amazon.com.br/Condicionado-Samsung-WindFree-Inverter-12-000/dp/B0DSLQP69S/ref=sr_1_1?crid=157AU9YFYK77W&dib=eyJ2IjoiMSJ9.GYk6RbriC7DOivKsnOzT3R_ZaQMw3Iq9b-1vuWzsqAhXwfpu9kf-_F26yI9A9lR42wRbRoU1R6Ji6hU-tLu9c73FJ1uShWfzLVLhrz6hu8hlhPiqBvVnICd53AiCr5W8sPH2OqNN2lIcV5rWmiuYjAXbvFeow_TPHioTeMmSjSDUfsiS4SrS9_XI_w3Tml26uhD774ld2dPTxr8fm5RU6FbqLbWYuPO0BzH46AaUaJcUw7tD7YuZuRCtdoR3owi_270u2LZKw9_YvMeWkboyXd-_gJH6Z9Dh9Mb1ylGT9Cc.k6IKAUMvzjFYXMqKOGXOJiOWj0JipWSmbt8O_N2gdRg&dib_tag=se&keywords=ar+condicionado+9000+btus&qid=1755112135&sprefix=arcondicionado+9000%2Caps%2C349&sr=8-1&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147" 
    elif btu <= 12000:
        return "Sugestao: Ar-condicionado de 12.000 BTUs, link de sugestao de ar-condicionado: https://www.amazon.com.br/Condicionado-Samsung-WindFree-Inverter-12-000/dp/B0DSLQP69S/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dib=eyJ2IjoiMSJ9.meR5NWEDAjk-XagRUCXJpta3Ct2LX_FNzOVfXgI25OQgTVc7huYalwDvVqMyLEorK4NXSybHfZeMjrcqdBzR0qG2JItl8dC1liPhb65vNqtvUQhdDmo2vG50rQde5dk8vjghvhmqe8NTDaZCQnWx_-KW-oURqXOrz9JxEOAlF0nMK80VwOq4W7xUdoikpx59R2Cj21QXv9eHiliHfnGgTIV1dtan1moPlTio6Ap7ItbDEXCyiKTF4T8A0ZcY-mcyHb_MzZrltQO3KZWcJ3UsrbI-FTyoLzyGW1-eOBaOCn8.r0HNX-JagvwTx6wP3j61rwxAUlrWmNV0XVjt2OO14Xc&dib_tag=se&keywords=ar+condicionado+12000+btus&qid=1755112723&sr=8-1&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147"
    elif btu <= 18000:
        return "Sugestao: Ar-condicionado de 18.000 BTUs, link de sugestao de ar-condicionado: https://www.amazon.com.br/Samsung-Ar-condicionado-Inverter-WindFree-AR18DYFAAWKNAZ/dp/B0DM6ZF1H9/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1BRM4XHU9P7KC&dib=eyJ2IjoiMSJ9.op73D1RziBkSc-YWDqqidUmSUM-MZeFVbYrMdRHzkKtsE3gqa8ZCX4ZzRmmXrdUqdGwr6SPcxgh50Ql8AirEiKuH6h0SG391oSBw_N59RDSGFwQo1XOHajwCVCw6TgfKijl4dw-DLdN2SImb6n3C3A9SNO7-iNGiD1F_IiYIxvaqu7aFUD2TDFbhQcWRbR6t1xMw48invCSkhjctET_u5nN8Y-n0mEyGllkRslAzOSNML-KiXq6hW8KHk5-8utuHVSVp8qGJNOIs41TiPpKJI8L_SAzUG_NxC6EiWC4orfo.-yA2-lAOeBH5MjstpiJn0KELR3BQM8qk6-DE5LLrtFA&dib_tag=se&keywords=ar+condicionado+18000+btus&qid=1755112891&sprefix=ar+condicionado+18000+btus%2Caps%2C433&sr=8-1&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147"
    elif btu > 18000:
        return "Sugestao, Ar-condicionado de mais de 18.000 BTUs, link de sugestao de ar-condicionado: https://www.amazon.com.br/Condicionado-32000-Split-Inverter-Elite/dp/B0FCST91HK/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=936BZCR6IQG&dib=eyJ2IjoiMSJ9.lWs9nObIZUwPp3gqcIYY5V1ERRloLADcDDFplfkwGsgeQM6nQNUPB3Lj5pMCSpxo4RiqD5LddXApzfhEZ9j8kNu1paI2bw2KS4ZaW4bAGqI.RQbvrWoRBd5rzsx9h8L1NDg3ugPXnJQmQ83l68-9RdQ&dib_tag=se&keywords=ar+condicionado+com+mais+de+32000+btus&qid=1755113208&refinements=p_n_g-101014854522111%3A117970948011&rnid=117970887011&s=home&sprefix=ar+condicionado+com+mais+de+32000+btus%2Chome%2C318&sr=1-1&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147" 
    else:
        return "Erro: Carga BTU invalida."

def main():
    dados = coletar_dados()
    carga_total, carga_BTU = calcular_carga(dados)

    print(f"Carga termica total: {carga_total:.2f} kcal/h")
    print(f"Carga termica de BTUs: {carga_BTU:.2f} Btus")
    recomendo = recomendar_ar(carga_BTU)
    print(recomendo)
    
if __name__ == "__main__":
    main()