for _ in range(int(input())):
    plano = list(input())
    estudado = []
    for _ in range(3):
        estudado.extend(list(input()))

    died = False
    for materia in estudado:
        if materia in plano:
            plano.remove(materia)
        else:
            died = True
            break
    

    if died:
        print("You died!")
    elif plano:
        plano.sort()
        estudar = []
        for m in plano:
            if not (m in estudar):
                estudar.append(m)

        print(f"Bora ralar: {''.join(estudar)}")
    else:
        print("It's in the box!")
