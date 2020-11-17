import matplotlib.pyplot as plt
import numpy as np


def SIR(beta, gamma, pop, kvacc=0, soc_dist=False, reduce_beta=0):
    N = pop
    I = [1 / N]
    S = [1.0 - I[0]]
    R = [0]
    T = [0]

    for t in range(300):
        # for new day
        s = S[t] - I[t] * beta * S[t] - kvacc * S[t]
        i = I[t] + I[t] * beta * S[t] - I[t] * gamma
        r = R[t] + I[t] * gamma + kvacc * S[t]

        # appending to lists
        S.append(s)
        I.append(i)
        R.append(r)
        T.append(t + 1)

        if soc_dist == True and t == 30:
            beta = beta / reduce_beta

    _ = plt.figure(figsize=(10, 10))
    plt.plot(T, S, 'green')
    plt.plot(T, I, 'red')
    plt.plot(T, R, 'black')
    plt.xlabel('Days')
    plt.ylabel('Fraction')
    plt.title('SIR model: kvacc={}, gamma={}, beta={:.3f} reduced by {}'
              .format(kvacc, gamma, beta, reduce_beta))
    plt.grid(True)
    plt.xticks(np.arange(min(T), max(T) + 1, 10))
    plt.yticks(np.arange(0, 1, 0.05))
    plt.show()

    return (I, T)


if __name__ == '__main__':

    # question 5-6
    list = [0, 0.0025, 0.005, 0.01, 0.02, 0.04]
    if False:
        for el in list:
            inf, time = SIR(beta=0.2, gamma=1 / 20, pop=120000, kvacc=el)
            max_inf = max(inf)
            max_inf_ind = inf.index(max_inf)
            max_inf_time = time[max_inf_ind]
            print('kvacc: {}\n peak infected: {}, day: {}'.format(el, max_inf, max_inf_time))

    # question 7
    if False:
        print(max(SIR(beta=0.2, gamma=2 / 20, pop=120000)[0]))

    # question 8
    reduce_values = [1, 1.5, 1.7, 2, 2.5, 3]
    for val in reduce_values:
        inf, time = SIR(beta=0.2, gamma=1 / 20, pop=120000, soc_dist=True, reduce_beta=val)
        max_inf = max(inf)
        max_inf_ind = inf.index(max_inf)
        max_inf_time = time[max_inf_ind]
        print('reduce value: {}\n peak infected: {}, day: {}'.format(val, max_inf, max_inf_time))
