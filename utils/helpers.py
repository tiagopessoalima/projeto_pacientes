def obter_int(pergunta: str, minimo=0, maximo=10):
    while True:
        try:
            valor = int(input(pergunta))
            if minimo <= valor <= maximo:
                return valor
            print(f"Valor deve estar entre {minimo} e {maximo}.")
        except ValueError:
            print("Digite um número válido.")