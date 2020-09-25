from datetime import timedelta, date
import matplotlib.pyplot as plt

def seir_predict(start_date=date.today(), prediction_period=10, N=331e6, s0=331e6, e0=100, i0=0, r0=0, d0=0,
                 virus_params={'alpha': 0.00113, 'beta': 0.219, 'epsilon': 0.5, 'gamma': 0.0714}):
    S = [s0]
    E = [e0]
    I = [i0]
    R = [r0]
    D = [d0]
    population = [N]
    dates = [start_date]
    for k in range(1, prediction_period + 1):
        day = start_date + timedelta(k)
        dates.append(day)
        s = S[k - 1] - virus_params['beta'] * S[k - 1] * I[k - 1] / population[k - 1]
        e = E[k - 1] + virus_params['beta'] * S[k - 1] * I[k - 1] / population[k - 1] - virus_params['epsilon'] * E[k - 1]
        i = I[k - 1] + virus_params['epsilon'] * E[k - 1] - (virus_params['alpha'] + virus_params['gamma']) * I[k - 1]
        r = R[k - 1] + virus_params['gamma'] * I[k - 1]
        d = D[k - 1] + virus_params['alpha'] * I[k - 1]
        population.append(population[k - 1] - d)
        S.append(s)
        E.append(e)
        I.append(i)
        R.append(r)
        D.append(d)

    return S, E, I, R, D, dates

if __name__ == '__main__':
    S, E, I, R, D, dates = seir_predict()
    plt.plot(dates, S)
    plt.show()
