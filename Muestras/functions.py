import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def fourier(datos, f_value):
    x = np.fft.rfft(datos, axis=0)
    ones = np.ones(f_value)
    zeros = np.zeros(x.shape[0] - f_value)
    c = np.concatenate((ones, zeros))
    clean = x * c.reshape(x.shape[0], 1)
    x = np.fft.irfft(clean, axis=0)
    return x


def resampler(data, lim_inf, lim_sup):
    x = data.copy()
    a = x[lim_inf:lim_sup, :]
    busqueda = 300 - a.shape[0]
    razon = (a.shape[0] / busqueda)
    g = np.flip(np.arange(1, a.shape[0], razon), 0)
    g = g.astype('int')
    copy = a.copy()

    for i in g:
        aux1 = copy[i]
        aux2 = copy[i - 1]
        valor = (aux1 + aux2) / 2
        copy = np.insert(copy, i, valor, axis=0)

    plt.plot(copy)
    plt.show()
    while(copy.shape[0]<300):
        last=copy[-1].reshape(1,6)
        copy=np.append(copy,last,axis=0)
    return copy


def analizar(df):
    # Order,True,Max_Delay,17,Out_Range,0,,
    # Tiempo,Contador,Acx,Acy,Acz,Gx,Gy,Gz
    order = df['Contador'].values.astype(str)[0]
    if order == 'False':
        print('Esta muestra tuvo problemas \n', df)


def get_sample(n, df):
    sample = df[(df.index >= n * 301) & (df.index < (n + 1) * 301)]
    print(sample)
    print(sample.shape)
    analizar(sample.tail(1))
    return sample[sample.index <300].astype(float)

def save(data, name: str, columns):
    df = pd.DataFrame(data=data, columns=columns)
    df_prime = pd.concat([df, pd.DataFrame([[np.nan] * df.shape[1]], columns=df.columns)], ignore_index=True)
    try:
        df = pd.read_csv(name)
        df = df.append(df_prime, ignore_index=True)
        print('Read csv sucesfully')
    except:
        df = df_prime
        print('creating new csv')
    df.to_csv(name, index=False)


def saludo():
    print('Saludo')
