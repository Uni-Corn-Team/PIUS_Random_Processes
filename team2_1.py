import numpy as np
import random
import math
import matplotlib.pyplot as plt
from team2_2 import Rxx, Kxx
import team3

def noises():
	n = 1000
	# Генерация белого шума
	X = []
	for i in range(n):
		X.append([])
		for j in range(n):
			X[i].append(random.random())
		X[i] = (sum(X[i])/n-0.5)*math.sqrt(12)
	T = 50
	k = math.sqrt(2 * T)
	Y = np.zeros(n)
	# Генерация окрашенного шума
	for number in range(n-1):
		Y[number+1] = (T-1)/T*Y[number]+k/T*X[number+1]
	fig = plt.figure(figsize=(8, 8))
	fig.suptitle("Графики и гистограммы белого и окрашенного шумов\n", fontsize=18, weight='bold')
	fig.patch.set_facecolor('#8DCF91')
	plt.subplot2grid((2, 4), (0, 0), colspan=3)
	# Белый шум
	plt.title('Белый шум')
	plt.xlabel('i')
	plt.ylabel('x2[i]')
	plt.grid(True)
	plt.plot(X, color='#E46C49')
	
	plt.subplot2grid((2, 4), (1, 0), colspan=3)
	# Окрашенный шум
	plt.title('Окрашенный шум')
	plt.xlabel('i')
	plt.ylabel('x3[i]')
	plt.grid(True)
	plt.plot(Y, color='#E46C49')
	
	plt.subplot2grid((2, 4), (0, 3))
	# Гистограмма для белого шума
	plt.hist(X, 20, density=True, facecolor='#E46C49', alpha=0.75,  orientation=u'horizontal')
	plt.axis('off')
	
	plt.subplot2grid((2, 4), (1, 3))
	# Гистограмма для окрашенного шума
	plt.hist(Y, 20, density=True, facecolor='#E46C49', alpha=0.75,  orientation=u'horizontal')
	plt.axis('off')
	plt.tight_layout()
	plt.savefig("graphs_and_histograms_of_white_and_colored_noise.png", dpi=100)
	plt.show(block=False)

	fig = plt.figure(figsize=(8, 8))
	fig.suptitle("Корреляционные функции шумов\n", fontsize=18, weight='bold')
	fig.patch.set_facecolor('#8DCF91')
	plt.subplot2grid((2, 1), (0, 0))
	# Корреляционная функция белого шума
	R, Q = Rxx(X)
	plt.title('Белый шум')
	plt.xlabel('q')
	plt.ylabel('Rxx')
	plt.grid(True)
	plt.fill_between(range(Q), R, np.zeros(Q), color='#E46C49')
	plt.plot(R, color='#E46C49')
	
	plt.subplot2grid((2, 1), (1, 0))
	# Корреляционная функция окрашенного шума
	R, Q = Rxx(Y)
	plt.title('\nОкрашенный шум')
	plt.xlabel('q')
	plt.ylabel('Rxx')
	plt.grid(True)
	plt.fill_between(range(Q), R, np.zeros(Q), color='#E46C49')
	plt.tight_layout()
	plt.plot(R, color='#E46C49')
	plt.savefig("proprietary_signal_characteristics.png", dpi=100)

	team3.run(X, Y, T)
