from datetime import timedelta, date
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
import numpy as np

def seir_predict(start_date=date.today(), prediction_period=10, N=331e6, e0=100, i0=0, r0=0, d0=0,
                 virus_params={'alpha': 0.00113, 'beta': 0.219, 'epsilon': 0.5, 'gamma': 0.0714}):
    '''
    This function makes predictions based on classic SEIR model
    :param start_date: date of start of prediction
    :param prediction_period: number of days to predict
    :param N: total population
    :param e0: number of initially exposed people
    :param i0: number of initially infected
    :param r0: number of initially recovered
    :param d0: total number of deaths up to the day of prediction start
    :param virus_params: dictionary with the parameters characterizing epidemic, where
    alpha is the virus-induced fatality rate
    beta is the probability of disease transmission
    epsilon is inversely proportional to the incubation period
    gamma is the recovery rate
    :return:
    '''
    S = [N]
    E = [e0]
    I = [i0]
    R = [r0]
    D = [d0]
    population = [N]
    dates = [start_date]
    for k in range(1, prediction_period):
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

    # return S, E, I, R, D, dates
    return np.concatenate((I, D, S))

def fun(theta):
    virus_params = {'alpha': theta[0], 'beta': theta[1], 'epsilon': theta[2], 'gamma': theta[3]}
    I_real = [13516, 14545, 15478, 15993, 17556, 18645, 20081, 20867, 21462, 22906]
    D_real = [917, 941, 981, 996, 1012, 1042, 1044, 1047, 1070, 1095]
    S_real = [7.278e6 - D_real[0], 7.278e6 - D_real[1], 7.278e6 - D_real[2], 7.278e6 - D_real[3], 7.278e6 - D_real[4],
              7.278e6 - D_real[5], 7.278e6 - D_real[6], 7.278e6 - D_real[7], 7.278e6 - D_real[8], 7.278e6 - D_real[9]]
    data = np.concatenate((I_real, D_real, S_real))
    return seir_predict(start_date=date.today(), prediction_period=10, N=7.278e6, e0=2000, i0=3000, r0=1000, d0=917,
                 virus_params=virus_params) - data

if __name__ == '__main__':
    # S, E, I, R, D, dates = seir_predict()
    # plt.plot(dates, S)
    # plt.show()
#     'alpha': 0.00113, 'beta': 0.219, 'epsilon': 0.5, 'gamma': 0.0714
    theta0 = [0.00113, 0.219, 0.5, 0.0714]
    res = least_squares(fun, theta0, bounds=([0, 0, 0, 0], [2, 2, 2, 2]))
    print(res)
