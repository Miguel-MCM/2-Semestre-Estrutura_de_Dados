def destrava(origem, destino, num_op):
    opc = [(abs(origem-destino), origem, "")]
    vistos = []
    while len(opc[0][2]) <= num_op:
        atual = min(opc)
        opc.remove(atual)
        if atual[1] == destino:
            return atual[2]
        if atual[1] not in vistos:
            vistos.append(atual[1])
            if len(atual[2]) < num_op-1:
                opc.append([abs(int(''.join(list(reversed(str(atual[1]))))) - destino) ,int(''.join(list(reversed(str(atual[1]))))), f"{atual[2]}I"])
                if atual[1] + 1 < 100000:
                    opc.append([abs(atual[1] * 2 - destino) ,atual[1] * 2, f"{atual[2]}D"])
                if atual[1] * 2 < 100000:
                    opc.append([abs(atual[1] + 1 - destino) ,atual[1] + 1, f"{atual[2]}+"])

# def destrava(origem, destino):
#     opc = [(origem, "")]
#     vistos = []
#     while (len(opc[-1][1]) < 21):
#         atual = opc.pop(0)
#         if atual[0] == destino:
#             return atual[1]
#         if atual[0] not in vistos:
#             vistos.append(atual[0])
#             opc.append([int(''.join(list(reversed(str(atual[0]))))), f"{atual[1]}I"])
#             opc.append([atual[0] * 2, f"{atual[1]}D"])
#             opc.append([atual[0] + 1, f"{atual[1]}+"])

print(destrava(4132,9361, 20))

def destravarPainel(painel, origem, objetivo):
    caminho = destrava(origem, objetivo, painel.verificaAcoesRestantes())
    while painel.verificaPainel() != objetivo:
        for op in caminho:
            if op == "I":
                painel.inverterValor()
            elif op == "D":
                painel.dobrarValor()
            elif op == "+":
                painel.incrementarValor()
    return painel.abrirArtefato()
