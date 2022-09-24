n = int(input())

for _ in range(n):
    abrir = "([{"
    fechar = ")]}"

    dup = False
    exp = input()
    pilha = []
    uf = -1

    for i in range(len(exp)):
        if exp[i] in abrir:
            pilha.append(i)        
        if exp[i] in fechar:
            f = pilha.pop()
            if (uf == f + 1) and (exp[i] == exp[i-1]):
                dup = True
                break
            uf = f
    
    if dup:
        print('A expressão possui duplicata.')
    else:
        print('A expressão não possui duplicata.')



            



    # try:
    #     for i in exp:
    #         if exp[i] in abrir:
    #             if foi_a and (exp[i] == exp[i-1]):
    #                 pilha.append(exp[i])
    #             foi_a = True
    #         elif (exp[i] in fechar):
    #             if(exp[i] != exp[i+1]) and (fechar.index(exp[i]) == abrir.index(pilha[-1])):
    #                 pilha.pop()
    #             elif (exp[i] == exp[i+1]) and (fechar.index(exp[i]) == abrir.index(pilha[-1])):
    #                 dup = True
    #                 break
        



    # except:
    #     print('A expressão não possui duplicata.')