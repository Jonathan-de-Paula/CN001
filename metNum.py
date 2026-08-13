import sympy as smp

x = smp.Symbol("x")


def newton_raphson(x0, tolero, inter,expr_str):
    fun_sym = smp.sympify(expr_str, locals={'e': smp.E})
    f = smp.lambdify(x, fun_sym, modules=["numpy"])
    derivada_prime = smp.diff(fun_sym, x)
    derivada = smp.lambdify(x, derivada_prime, modules='numpy')
    x_prime = x0
    cont0 = 0
    historico_x = []
    historico_f = []
    mostrar_tabela = input("Deseja ver a tabela de iterações? (0-Sim / 1-Não): ").strip() == '0'

    for i in range(inter):
        f_val = f(x_prime)
        f_der = derivada(x_prime)

        if abs(f_der) < 1e-12:
            print("Derivada zerou, impossibilitando o método.")
            return

        novo_x = x_prime - f_val / f_der
        erro = abs(novo_x - x_prime)

        # Armazena o estado atual (antes de atualizar)
        historico_x.append(x_prime)
        historico_f.append(f_val)
        cont0 += 1

        if erro < tolero or abs(f(novo_x)) < tolero:
            if mostrar_tabela:
                print("\nIteração | x | |f(x)|")
                for j in range(cont0):
                    print(f"{j + 1:>3}   | {historico_x[j]:.10f} | {historico_f[j]:.10f}")
                print(f"\nRaiz encontrada: x = {novo_x:.12f}")
            else:
                print(f"Raiz encontrada: x = {novo_x:.12f}")
            print(f"Número de iterações: {cont0}")
            return

        x_prime = novo_x

    print(f"Número máximo de iterações atingido. Último valor: {x_prime:.10f}")
    # Se o loop terminar sem ter encontrado a raiz
    print(f"Número máximo de iterações atingido, ultimo valor obtido: {x_prime:.10f}")

    def bissecao(a, b, tolero, inter):
        cont0 = 0
        historico_a = []
        historico_b = []
        historico_c = []
        historico_f_c = []
        for i in range(inter):
            novo_x = (a + b) / 2
            f_x = f(novo_x)

            # Armazena o estado atual
            historico_a.append(a)
            historico_b.append(b)
            historico_c.append(novo_x)
            historico_f_c.append(f_x)
            cont0 += 1

            if abs(f_x) < tolero or abs(b - a) / 2 < tolero:
                mostrar_tabela = input("Deseja ver a tabela de iterações? (0-Sim / 1-Não): ").strip() == '0'
                if mostrar_tabela:
                    print("\nIteração | a | b | x | f(x)")
                    for j in range(cont0):
                        print(
                            f"{j + 1:>3}   | {historico_a[j]:.10f} | {historico_b[j]:.10f} | {historico_c[j]:.10f} | {historico_f_c[j]:.10f}")
                    print(f"\nRaiz encontrada: x = {novo_x:.12f}")
                else:
                    print(f"Raiz encontrada: x = {novo_x:.12f}")
                print(f"Número de iterações: {cont0}")
                return
            else:
                if f(a) * f_x < 0:
                    b = novo_x
                else:
                    a = novo_x

        print(f"Número máximo de iterações atingido. Último valor: x = {novo_x:.10f}")


def bissecao(a, b, tolero, inter,expr_str):
    fun_sym = smp.sympify(expr_str, locals={'e': smp.E})
    f = smp.lambdify(x, fun_sym, modules=["numpy"])
    derivada_prime = smp.diff(fun_sym, x)
    derivada = smp.lambdify(x, derivada_prime, modules='numpy')
    cont0 = 0
    historico_a = []
    historico_b = []
    historico_c = []
    historico_f_c = []
    for i in range(inter):
        novo_x = (a + b) / 2
        f_x = f(novo_x)

        # Armazena o estado atual
        historico_a.append(a)
        historico_b.append(b)
        historico_c.append(novo_x)
        historico_f_c.append(f_x)
        cont0 += 1

        if abs(f_x) < tolero or abs(b - a) / 2 < tolero:
            mostrar_tabela = input("Deseja ver a tabela de iterações? (0-Sim / 1-Não): ").strip() == '0'
            if mostrar_tabela:
                print("\nIteração | a | b | x | f(x)")
                for j in range(cont0):
                    print(
                        f"{j + 1:>3}   | {historico_a[j]:.10f} | {historico_b[j]:.10f} | {historico_c[j]:.10f} | {historico_f_c[j]:.10f}")
                print(f"\nRaiz encontrada: x = {novo_x:.12f}")
            else:
                print(f"Raiz encontrada: x = {novo_x:.12f}")
            print(f"Número de iterações: {cont0}")
            return
        else:
            if f(a) * f_x < 0:
                b = novo_x
            else:
                a = novo_x

    print(f"Número máximo de iterações atingido. Último valor: x = {novo_x:.10f}")
