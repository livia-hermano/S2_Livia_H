print("Vamos converter a temperatura para CELSIUS ou FAHRENHEIT")
def celsius_fahrenheit():
    temperatura = int(input("Digite o valor da temperatura: "))
    opcao = input("""Digite a opção de conversão:
                C - Celsius para fahrenheit
                f - fahrenheit para celcius: """)
    if opcao == 'f' or opcao == 'F':
        resultado = (temperatura - 32) * (5/9)
        print("A temperatura convertida é de:",resultado)
    elif opcao == 'c' or opcao == 'C':
        resultado = temperatura * 9/5 + 32 
        print("A temperatura convertida é de:",resultado)
celsius_fahrenheit()