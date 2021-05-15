import numpy as np

def Rxx(X, D = 10):
    """
    Корреляционная функция
    """
    # Среднее значение X
    X_ = np.mean(X)
    N = len(X)
    Q = int(N/D)
    R = np.zeros(Q)
    for q in range(Q):
        for i in range(N - Q):
            R[q] = R[q] + (X[i] - X_) * (X[i + q] - X_)
    R = R / (N - Q)
    return R, Q

def Rxxwf(X, D = 5):
    """
    Корреляционная функция для весовых функций
    """
    N = len(X)
    Q = int(N/D)
    R = np.zeros(Q)
    for q in range(Q):
        for i in range(N - Q):
            R[q] = R[q] + X[i] * X[i + q]
    R = R / (N - Q)
    return R, Q

def Kxx(a):
    """
    Ковариационная функция
    """
    K = np.zeros(100)
    for q in range(100):
        K[q] = np.exp(-a * np.fabs(q))
    return K

def Kxxcn(X, t):
    """
    Ковариационная функция для окрашенного шума
    """
    X_ = np.mean(X)
    M = np.zeros(len(X)-t)
    for q in range(len(M)):
        M[q] = (X[q] - X_) * (X[q + t] - X_)
    return np.mean(M)
