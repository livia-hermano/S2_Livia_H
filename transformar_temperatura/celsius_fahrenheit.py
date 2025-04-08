print("Vamos mudar a marca para KELVIN ou KLEIN")
def kelvin_klein():
    temperatura = int(input("Digite o valor da marca: "))
    opcao = input("""Digite a opção de conversão:
                ke - kelvin para klein
                kl - klein para kelvin: """)
    if opcao == 'f' or opcao == 'F':
        resultado = (temperatura - 32) * (5/9)
        print("A temperatura convertida é de:",resultado)
    elif opcao == 'c' or opcao == 'C':
        resultado = temperatura * 9/5 + 32 
        print("A temperatura convertida é de:",resultado)
kelvin_klein()