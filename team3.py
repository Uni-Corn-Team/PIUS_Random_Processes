import numpy
import scipy
import scipy.stats
import matplotlib.pyplot as plt


def mean_confidence_interval_uncorrelation_student(data, a=0.05):
    # Вычисляет доверительный интервал для выборки data для доверительной вероятности confidence
    n = len(data)  # размер выборки
    mean = numpy.mean(data)  # среднее
    dev = scipy.stats.sem(data)  # стандартное отклонение
    h = dev * scipy.stats.t.ppf(1 - a / 2., n - 1)  # вычисляем доверительный интервал, t-распределение Стьюдента
    return mean, h


def mean_confidence_interval_uncorrelation_normal(data, a=0.05):
    # Вычисляет доверительный интервал для выборки data для доверительной вероятности confidence
    n = len(data)  # размер выборки
    mean = numpy.mean(data)  # среднее
    dev = scipy.stats.sem(data)  # стандартное отклонение
    h = numpy.sqrt(dev * numpy.sqrt(n)) * scipy.stats.norm.ppf(1 - a / 2.) / numpy.sqrt(n)
    return mean, h


def mean_confidence_interval_correlation_noise_student(data, a=0.05, T=50):
    # размер выборки
    n = len(data)
    mean = numpy.mean(data)
    dev = 0
    for p in range(n - 1):
        dev = dev + (1 - (p + 1) / n) * numpy.exp(-(p + 1) / T) * a  # (1 - (p + 1) / n) - это тау
    dev = dev * 2 / n + 1 / n  # см 6 формулу в методичке
    h = dev * scipy.stats.t.ppf(1 - a / 2., n - 1)  # вычисляем доверительный интервал
    return mean, h


def mean_confidence_interval_correlation_noise_normal(data, a=0.05, T=50):
    # размер выборки
    n = len(data)
    mean = numpy.mean(data)
    dev = 0
    for p in range(n - 1):
        dev = dev + (1 - (p + 1) / n) * numpy.exp(-(p + 1) / T) * a  # (1 - (p + 1) / n) - это тау
    dev = dev * 2 / n + 1 / n  # см 6 формулу в методичке
    h = numpy.sqrt(dev * numpy.sqrt(n)) * scipy.stats.norm.ppf(1 - a / 2.) / numpy.sqrt(n)
    return mean, h


def plot(mx, sx, color1, color2, loc, title):
    plt.subplot2grid((2, 2), loc, rowspan=1, colspan=1)
    plt.title(title)
    plt.xlabel('N')
    plt.ylabel('M[x]')
    plt.grid(True)
    plt.plot(mx, color=color1)
    plt.plot(mx + sx, color=color2)
    plt.plot(mx - sx, color=color2)


def run(data_white, data_color, T):
    """
    :gets \n
    data_white - неокрашенный шум \n
    data_color - окрашенный шум \n
    T - интервал наблюдения \n
    --------------------------------------------------\n
    :returns \n
    (среднее, отступ от среднего в одну сторону) для: \n
    * некорр., Стьюдент \n
    * корр., Стьюдент \n
    * некорр., Нормальн. \n
    * корр., Нормальн. \n
    """
    points = 10
    mx1 = mx2 = mx3 = mx4 = numpy.zeros(len(data_white))
    sx1 = sx2 = sx3 = sx4 = numpy.zeros(len(data_white))

    fig = plt.figure(figsize=(8, 8))
    fig.suptitle("Доверительные интервалы для среднего\n", fontsize=18, weight='bold')
    fig.patch.set_facecolor('#8DCF91')

    for i in range(len(data_white)):
        mx1[i], sx1[i] = mean_confidence_interval_uncorrelation_student(data_white[:i + points])
    plot(mx1, sx1, 'green', 'magenta', (0, 0), 'некорр., Стьюдент')

    for i in range(len(data_color)):
        mx2[i], sx2[i] = mean_confidence_interval_correlation_noise_student(data_color[:i + points], T=T)
    plot(mx2, sx2, 'green', 'red', (1, 0), 'корр., Стьюдент')

    for i in range(len(data_color)):
        mx3[i], sx3[i] = mean_confidence_interval_uncorrelation_normal(data_white[:i + points])
    plot(mx3, sx3, 'green', 'cyan', (0, 1), 'некорр., Нормальн.')

    for i in range(len(data_color)):
        mx4[i], sx4[i] = mean_confidence_interval_correlation_noise_normal(data_color[:i + points], T=T)
    plot(mx4, sx4, 'green', 'blue', (1, 1), 'корр., Нормальн.')

    plt.tight_layout()
    plt.savefig("confidence_intervals_for_the_average.png", dpi=100)
    plt.show(block=False)

    return (mx1, sx1), (mx2, sx2), (mx3, sx3), (mx4, sx4)
