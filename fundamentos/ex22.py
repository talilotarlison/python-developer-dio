def soma(a, b):
    return a + b
    
    
def subitrair(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def dividir(a, b):
    return a/b

def show_resultado(a, b, callback):
    # Chama a função de callback (soma) com os argumentos a e b
    resultado = callback(a, b)
    print("resultado: ", resultado)

# Chama show_resultado passando a função soma como callback
show_resultado(5, 5, soma)
show_resultado(5, 5, subitrair)
show_resultado(5, 5, multiplica)
show_resultado(5, 5, dividir)


# soma(a, b): Função de callback que realiza a soma.
# show_resultado(a, b, callback): a, b e uma função (callback) como parâmetros, 
# chama essa função e imprime o resultado.