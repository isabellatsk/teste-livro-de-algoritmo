# (RECURSÃO - CAP 3 PG 58)
# Precisa encontrar a chave, ela está em algum lugar dentro de uma caixa que tem várias caixas dentro e assim por diante

"""
#primeira forma - sem recursão
def procure_pela_chave(caixa_principal):
    pilha = main_box.crie_uma_pilha_para_busca()
    while pilha is not vazia:
        caixa = pilha.pegue_caixa()
        for item in caixa:
            if item.e_uma_caixa():
                pilha.append(item)
            elif item.e_uma_chave():
                print ("Achei a chave!")
                
                
                
                
#segundaforma - com recursão
def procure_pela_chave(caixa):
    for item in caixa:
        if item.e_uma_caixa():
            procure_pela_chave(item)
        elif item.e_uma_chave():
            print ("Achei a chave!")
            
"""     
# função recursiva com caso-base

def regressiva(i):
    print (i)
    if i <= 1: 
        return
    else: 
        regressiva(i-1)   
        


def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x-1)
    
fat(3)
# fat(x-1) é uma chamada recursiva
# agora o valor de x é 2