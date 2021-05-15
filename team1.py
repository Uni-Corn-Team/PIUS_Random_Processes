import numpy as np
import matplotlib.pyplot as plt

count_of_numbers = 1000


# Корреляционная функция для весовых функций
def corel_weight_func(X, D=5):
    N = len(X)
    Q = int(N / D)
    R = np.zeros(Q)
    for q in range(Q):
        for i in range(N - Q):
            R[q] = R[q] + X[i] * X[i + q]
    R = R / (N - Q)
    return R, Q


# Расчет выходных сигналов на основе входных
def transform_sig(X, H):
    outp = np.zeros(len(H))
    for j in range(len(H)):
        for i in range(j + 1):
            outp[j] = outp[j] + X[i] * H[j - i]
    return outp


def non_inertial_link(Xsin, Ysin):
    # Non-inertial link
    N = count_of_numbers
    X = np.array(range(N))
    Y = np.zeros(N)
    Y[0] = 1

    fig = plt.figure(figsize=(8, 16))
    fig.suptitle("Безинерционное звено\n", fontsize=18, weight='bold')
    fig.patch.set_facecolor('#8DCF91')
    plt.subplot2grid((4, 1), (0, 0), colspan=1)
    plt.title("\nВесовая функция", fontsize=15)
    plt.xlabel("t", fontsize=13, fontstyle="italic")
    plt.ylabel("h(t)", fontsize=13, fontstyle="italic")
    plt.grid(True)
    plt.plot(X, Y, color='#E46C49', markerfacecolor='#E46C49',
             linewidth=3, markersize=6)

    # fig.patch.set_alpha(0.6)

    plt.subplot2grid((4, 1), (1, 0))
    # Correlation function of the inertia-free link
    R, Q = corel_weight_func(Y)
    plt.title("\nКорреляционная функция весовой функции", fontsize=15)
    plt.xlabel("q", fontsize=13, fontstyle="italic")
    plt.ylabel("Rxx", fontsize=13, fontstyle="italic")
    plt.grid(True)
    plt.fill_between(range(Q), R, np.zeros(Q), color='#E46C49')
    plt.plot(R, color='#E46C49', markerfacecolor='#E46C49',
             linewidth=3, markersize=6)

    plt.subplot2grid((4, 1), (2, 0), colspan=1)
    plt.title("\nВходной сигнал", fontsize=15)
    plt.xlabel("x", fontsize=13, fontstyle="italic")
    plt.ylabel("sin(x)", fontsize=13, fontstyle="italic")
    plt.grid(True)
    plt.plot(X, Ysin, color='#E46C49', markerfacecolor='#E46C49',
             linewidth=3, markersize=6)

    outp = transform_sig(Ysin, Y)
    plt.subplot2grid((4, 1), (3, 0), colspan=1)
    plt.title("\nВыходной сигнал", fontsize=15)
    plt.xlabel("x", fontsize=13, fontstyle="italic")
    plt.ylabel("sin(x)", fontsize=13, fontstyle="italic")
    plt.grid(True)
    plt.plot(X, outp, color='#E46C49', markerfacecolor='#E46C49',
             linewidth=3, markersize=6)
    plt.tight_layout()
    plt.savefig("non_inertial_link.png", dpi=100)
    return plt


def link_with_net_lag(Xsin, Ysin):
    # A link with a net lag
    N = count_of_numbers
    X = (np.array(range(N)) - 0.2 * N)
    Y = np.zeros(N)
    Y[100] = 1

    fig = plt.figure(figsize=(8, 16))
    fig.suptitle("Звено с чистым запаздыванием\n", fontsize=18, weight='bold')
    fig.patch.set_facecolor('#8DCF91')
    plt.subplot2grid((4, 1), (0, 0), colspan=1)
    plt.title("Весовая функция", fontsize=15)
    plt.xlabel("t", fontsize=13, fontstyle="italic")
    plt.ylabel("h(t)", fontsize=13, fontstyle="italic")
    plt.grid(True)
    plt.plot(X, Y, color='#E46C49', markerfacecolor='#E46C49',
             linewidth=3, markersize=6)

    plt.subplot2grid((4, 1), (1, 0), colspan=1)
    # Correlation function of a link with a net delay
    R, Q = corel_weight_func(Y)
    plt.title("\nКорреляционная функция весовой функции", fontsize=15)
    plt.xlabel("q", fontsize=13, fontstyle="italic")
    plt.ylabel("Rxx", fontsize=13, fontstyle="italic")
    plt.grid(True)
    plt.fill_between(range(Q), R, np.zeros(Q), color='#E46C49')
    plt.plot(R, color='#E46C49', markerfacecolor='#E46C49',
             linewidth=3, markersize=6)

    plt.subplot2grid((4, 1), (2, 0), colspan=1)
    plt.title("Входной сигнал", fontsize=15)
    plt.xlabel("x", fontsize=13, fontstyle="italic")
    plt.ylabel("sin(x)", fontsize=13, fontstyle="italic")
    plt.grid(True)
    plt.plot(X, Ysin, color='#E46C49', markerfacecolor='#E46C49',
             linewidth=3, markersize=6)

    outp = transform_sig(Ysin, Y)
    plt.subplot2grid((4, 1), (3, 0), colspan=1)
    plt.title("Выходной сигнал", fontsize=15)
    plt.xlabel("x", fontsize=13, fontstyle="italic")
    plt.ylabel("sin(x)", fontsize=13, fontstyle="italic")
    plt.grid(True)
    plt.plot(X, outp, color='#E46C49', markerfacecolor='#E46C49',
             linewidth=3, markersize=6)
    plt.tight_layout()
    plt.savefig("link_with_net_lag.png", dpi=100)
    return plt


def aperiodic_link_1st_order(Xsin, Ysin):
    # The aperiodic link of the 1st order
    T = 15
    N = count_of_numbers
    X = (np.array(range(N)))
    Y = np.zeros(N)
    for i in range(N):
        if X[i] >= 0:
            Y[i] = np.exp(-X[i] / T) / T

    fig = plt.figure(figsize=(8, 16))
    fig.suptitle("Апериодическое звено 1-го порядка\n", fontsize=18, weight='bold')
    fig.patch.set_facecolor('#8DCF91')
    plt.subplot2grid((4, 1), (0, 0), colspan=1)
    plt.title("Весовая функция", fontsize=15)
    plt.xlabel("t", fontsize=13, fontstyle="italic")
    plt.ylabel("h(t)", fontsize=13, fontstyle="italic")
    plt.grid(True)
    plt.plot(X, Y, color='#E46C49', markerfacecolor='#E46C49',
             linewidth=3, markersize=6)

    plt.subplot2grid((4, 1), (1, 0), colspan=1)
    # Correlation function of the 1st-order aperiodic link
    R, Q = corel_weight_func(Y)
    plt.title("\nКорреляционная функция весовой функции", fontsize=15)
    plt.xlabel("q", fontsize=13, fontstyle="italic")
    plt.ylabel("Rxx", fontsize=13, fontstyle="italic")
    plt.grid(True)
    plt.fill_between(range(Q), R, np.zeros(Q), color='#E46C49')
    plt.plot(R, color='#E46C49', markerfacecolor='#E46C49',
             linewidth=3, markersize=6)

    plt.subplot2grid((4, 1), (2, 0), colspan=1)
    plt.title("Входной сигнал", fontsize=15)
    plt.xlabel("x", fontsize=13, fontstyle="italic")
    plt.ylabel("sin(x)", fontsize=13, fontstyle="italic")
    plt.grid(True)
    plt.plot(Xsin, Ysin, color='#E46C49', markerfacecolor='#E46C49',
             linewidth=3, markersize=6)

    outp = transform_sig(Ysin, Y)
    plt.subplot2grid((4, 1), (3, 0), colspan=1)
    plt.title("Выходной сигнал", fontsize=15)
    plt.xlabel("x", fontsize=13, fontstyle="italic")
    plt.ylabel("sin(x)", fontsize=13, fontstyle="italic")
    plt.grid(True)
    plt.plot(X, outp, color='#E46C49', markerfacecolor='#E46C49',
             linewidth=3, markersize=6)
    plt.tight_layout()
    plt.savefig("aperiodic_link_1st_order.png", dpi=100)
    return plt


def black_box(Xsin, Ysin):
    # Black Box
    N = count_of_numbers
    X = np.array(range(N))
    Y = np.zeros(N)
    for i in range(N):
        if X[i] > 0 and X[i] < 100 * np.pi:
            Y[i] = np.sin(X[i] / 100) / 200

    fig = plt.figure(figsize=(8, 16))
    fig.suptitle("Чёрный ящик\n", fontsize=18, weight='bold')
    fig.patch.set_facecolor('#8DCF91')
    plt.subplot2grid((4, 1), (0, 0), colspan=1)
    plt.title("Весовая функция", fontsize=15)
    plt.xlabel("t", fontsize=13, fontstyle="italic")
    plt.ylabel("h(t)", fontsize=13, fontstyle="italic")
    plt.grid(True)
    plt.plot(X, Y, color='#E46C49', markerfacecolor='#E46C49',
             linewidth=3, markersize=6)

    plt.subplot2grid((4, 1), (1, 0), colspan=1)
    # Black box correlation function
    R, Q = corel_weight_func(Y)
    plt.title("\nКорреляционная функция весовой функции", fontsize=15)
    plt.xlabel("q", fontsize=13, fontstyle="italic")
    plt.ylabel("Rxx", fontsize=13, fontstyle="italic")
    plt.grid(True)
    plt.fill_between(range(Q), R, np.zeros(Q), color='#E46C49')
    plt.plot(R, color='#E46C49', markerfacecolor='#E46C49',
             linewidth=3, markersize=6)

    plt.subplot2grid((4, 1), (2, 0), colspan=1)
    plt.title("Входной сигнал", fontsize=15)
    plt.xlabel("x", fontsize=13, fontstyle="italic")
    plt.ylabel("sin(x)", fontsize=13, fontstyle="italic")
    plt.grid(True)
    plt.plot(Xsin, Ysin, color='#E46C49', markerfacecolor='#E46C49',
             linewidth=3, markersize=6)

    outp = transform_sig(Ysin, Y)
    plt.subplot2grid((4, 1), (3, 0), colspan=1)
    plt.title("Выходной сигнал", fontsize=15)
    plt.xlabel("x", fontsize=13, fontstyle="italic")
    plt.ylabel("sin(x)", fontsize=13, fontstyle="italic")
    plt.grid(True)
    plt.plot(X, outp, color='#E46C49', markerfacecolor='#E46C49',
             linewidth=3, markersize=6)
    plt.tight_layout()
    plt.savefig("black_box.png", dpi=100)
    return plt


def generate_input_signal():
    # Generating a signal of the form sin(x)
    N = count_of_numbers
    Xsin = np.array(range(N))
    Ysin = np.zeros(N)
    for i in range(N):
        Ysin[i] = np.sin(Xsin[i] * 0.02)

    return Xsin, Ysin


if __name__ == "__main__":
    Xsin, Ysin = generate_input_signal()
    flag = True
    while (flag):
        print("""
        1:  Non-inertial link
        2:  A link with a net lag
        3:  The aperiodic link of the 1st order
        4:  Black box correlation function
        """)
        num = input("Choose function: ")
        print(num)
        if num == "1":
            non_inertial_link(Xsin, Ysin).show()
        elif num == "2":
            link_with_net_lag(Xsin, Ysin).show()
        elif num == "3":
            aperiodic_link_1st_order(Xsin, Ysin).show()
        elif num == "4":
            black_box(Xsin, Ysin).show()
        elif num == "0":
            flag = False
