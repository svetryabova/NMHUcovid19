from datetime import timedelta, date

def seir_predict(start_date=date.today(), prediction_period=10, s0=0, e0=0, i0=0, r0=0, d0=0,
                 virus_params={'alpha': 0.00113, 'beta': 0.219, 'epsilon': 0.5, 'gamma': 0.0714}):
    S = []
    E = []
    I = []
    R = []
    D = []
    dates = [start_date]
    for i in range(1, prediction_period + 1):
        day = start_date + timedelta(i)
        dates.append(day)

    print(dates)

if __name__ == '__main__':
    seir_predict()
