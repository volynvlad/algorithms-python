import numpy as np

from genetic_algorithm.equations import first_equation, second_equation, third_equation

# seed = 42
# np.random.seed(42)

# hyper params
population_size = 40
old_generation_rate = 0.7
mutation_rate = 0.09


# 1, 2, 3, 2, 2
# random [-100, 100]
# пропорциональная селекция
# скрещивание: пропорциональное вероятностное

# мутация:   Каждый бит некоторых наименее
#            пригодных потомков
#            мутирует с некоторой
#            вероятностью p

# замещение: Наименее пригодных
#            особей старой популяции заменить на
#            наиболее пригодных особей из потомков"

# u^powU * w^powW * x^powX * y^powY * z^powZ +
# u^powU1 * w^powW1 * x^powX1 * y^powY1 * z^powZ1 +
# u^powU2 * w^powW2 * x^powX2 * y^powY2 * z^powZ2 +
# u^powU3 * w^powW3 * x^powX3 * y^powY3 * z^powZ3 +
# u^powU4 * w^powW4 * x^powX4 * y^powY4 * z^powZ4
# = Result


def random_params(low, high):
    params_num = 5
    return np.random.randint(low, high + 1, (params_num, population_size))


def function_result(param, pows):
    pows = np.array(pows).reshape(5, 5)

    return sum([param[0] ** pows[0][i] *
               param[1] ** pows[1][i] *
               param[2] ** pows[2][i] *
               param[3] ** pows[3][i] *
               param[4] ** pows[4][i] for i in range(5)])


def absolute_error(param, equation):
    *coefficients, result = equation()
    return np.abs((result - function_result(param, coefficients)))


def count_percents(errors):
    reverse_errors = [1 / err for err in errors]
    reverse_errors_sum = sum(reverse_errors)
    return [reverse_error / reverse_errors_sum for reverse_error in reverse_errors]


def selection(p, remain_rate):
    p = [a for a in sorted(p, key=lambda item: item[0], reverse=True)]
    return p[0:int(len(p) * remain_rate) + 1]


def crossing(p):
    result = []
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            new = [p[i][1][k] if np.random.rand() < p[i][0]/(p[i][0] + p[j][0]) else p[j][1][k] for k in range(5)]
            result.append(new)

    return result


def mutation(p, rate, low, high):
    for child in p[-len(p)//2:]:
        for i in range(len(child[1])):
            if np.random.rand() < rate:
                child[1][i] = np.random.randint(low, high + 1)


# generation
u, w, x, y, z = random_params(-100, 100)

params = [[u[i], w[i], x[i], y[i], z[i]] for i in range(population_size)]

while True:
    absolute_errors = [absolute_error(param, first_equation) for param in params]

    if absolute_errors.count(0) != 0:
        print(f"result - {params[absolute_errors.index(0)]}")
        best_params = params[absolute_errors.index(0)]
        break

    percents = count_percents(absolute_errors)

    percents_params = zip(percents, params)

    # selection
    percents_params = selection(percents_params, old_generation_rate)

    # crossing
    new_params = crossing(percents_params)
    absolute_errors = [absolute_error(param, first_equation) for param in new_params]

    if absolute_errors.count(0) != 0:
        print(f"result - {params[absolute_errors.index(0)]}")
        best_params = params[absolute_errors.index(0)]
        break

    new_percents = count_percents(absolute_errors)
    new_percents_params = zip(new_percents, new_params)

    new_percents_params = sorted(new_percents_params, key=lambda item: item[0], reverse=True)

    # mutation
    mutation(new_percents_params, mutation_rate, -100, 100)

    new_percents, new_params = map(list, zip(*new_percents_params))

    new_params_absolute_errors = [absolute_error(param, first_equation) for param in new_params]
    new_percents = count_percents(new_params_absolute_errors)
    new_percents_params = list(zip(new_percents, new_params))

    percents_params = new_percents_params + percents_params

    percents_params = sorted(percents_params, key=lambda item: item[0], reverse=True)

    percents, params = map(list, zip(*percents_params))

    absolute_errors = [absolute_error(param, first_equation) for param in params]

    params = params[:population_size]

    print(f"best param - {params[0]}, error - {absolute_error(params[0], first_equation)}")

print(f"result: best_param - {best_params}, error - {absolute_error(best_params, first_equation)}")