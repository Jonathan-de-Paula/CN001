import sympy as smp
import metNum as mn


x = smp.Symbol("x")

while True :
    expr_str = input("Digite a função f(x), digite 0 para sair: ")
    state = 1
    if(expr_str == "0"):
        exit()

    try:
        fun_sym = smp.sympify(expr_str, locals={'e': smp.E})
        f = smp.lambdify(x, fun_sym, modules=["numpy"])
    except smp.SympifyError:
        print("Expressão inválida")
        continue

    a = float(input("Digite o limite inferior (a): "))
    b = float(input("Digite o limite superior (b): "))
    try:
        if a >= b:
            print("O limite inferior deve ser menor que o superior.")
            continue
        if f(a) * f(b) >= 0:
            print("Não há raizes no intervalo")
            continue
        else:
            tolero = float(input("Digite a tolerância: "))
            inter = int(input("Digite o número máximo de iterações: "))
    except ValueError:
        print("Inválido")
        continue

##Vai pegar a função fun_sym e vai tranformar em uma função numerica f, facilitando o entendimento do python e possibilitando o loop


    metodo = int(input("Deseja achar o zero real pelo metodo de Newton-Raphson (1) ou pelo método da bisseção (2)? "))
    if metodo == 1:
        try:
            x0 = float(input("Digite o chute inicial (x0): "))
        except ValueError:
            print("Inválido")
            continue
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nIniciando o método de Newton-Raphson...\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        if x0 < a or x0 > b:
            print("O chute inicial deve estar dentro do intervalo [a, b].")
            continue

        mn.newton_raphson(x0, tolero, inter,expr_str)

    elif metodo == 2:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nIniciando o método da bisseção...\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        mn.bissecao(a, b, tolero, inter,expr_str)

    else:
        print("Opção inválida.")
        continue