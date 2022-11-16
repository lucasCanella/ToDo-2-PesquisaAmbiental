print('')
print('-='*13)
print('  CALCULADORA DE AMOSTRA\n(nível de confiança = 95%)')
print('-='*13)
print('')

#  FÓRMULA: tamanho da amostra = ((z**2) * p * (1 - p) / (e**2)) / (1 + ((z**2) * p * (1 - p) / ((e**2) * N)).
#  Margem de erro (decimal) = e
#  Tamanho da população = N

z  =  1.96      #  Como o nível de confiança considerado foi 95%, escore z = 1.96.
p  =  0.5       #  O desvio padrão considerado foi de 50%, portanto, p = 0.5.

populacao      =  int(input('Qual o tamanho da população?\n'))
margem_de_erro =  float(input('Qual a margem de erro? (em porcentagem)\n'))
formula_1      =  (z**2) * p * (1 - p)        #   Como "(z**2) * p * (1 - p)" aparece duas vezes na fórmula, atribui esse cálculo a uma variável.
erro_decimal   =  (margem_de_erro / 100)**2   #   Na fórmula, a margem de erro sempre é elevada a 2, e como é em decimal, foi dividida por 100.

def tamanho_da_amostra(formula_1, erro_decimal, populacao):
    return (formula_1 / erro_decimal) / (1 + (formula_1 / (erro_decimal * populacao)))   #  formula1 = (z**2) * p * (1 - p)   ;   erro_decimal = e**2   ;   populacao = N

resultado = round(tamanho_da_amostra(formula_1, erro_decimal, populacao))   #  Função round() foi utilizada para arredondar o valor.

print(f'TAMANHO DA AMOSTRA NECESSÁRIA: {resultado}\n'
f'TAMANHO DA POPULAÇÃO: {populacao}\n'
f'MARGEM DE ERRO: {margem_de_erro}%')
