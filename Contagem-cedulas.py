def din(a):
    val = int(a)
    notas = [200, 100, 50, 20, 10, 5, 2, 1]
    notas.sort()
    notas.reverse()
    numNotas = []
    for i in notas:
        numNotas.append(val/i)
        val %= i
    for i in range(len(notas)):
        print("Notas de %d:%d" % (notas[i], numNotas[i]))
    return a
val = int(input("Digite o valor: "))
print(din(val))