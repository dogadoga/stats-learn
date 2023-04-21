import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk
import math

# 何かを行ったときに起こる結果が2つしかない試行のことを「ベルヌーイ試行」という．
# ベルヌーイ試行をn回行って、成功する回数Xが従う確率分布を「二項分布」という．
# X ~ Bin(n, p) と表す．
# 二項分布の確率関数は以下の通り．
# f(x=k) = nCx p^x (1-p)^(n-x)
# この式はベルヌーイ試行をn回行って，ちょうどk回成功する確率を表している．
# 例えば，コインをn回投げて，表がちょうどk回出る確率は，nCk p^k (1-p)^(n-k) で表される(p=0.5)．

N = 50 # 試行回数
Ps = [0.1, 0.5, 1/6, 3/4] # 成功確率
COLORS = ['blue', 'lime', 'red', 'pink']
YMIN = 0
YMAX = 0.2

def binomial(n, k, p):
	""" 
	二項分布の確率関数
	ベルヌーイ試行をn回行って，ちょうどk回成功する確率を返す．
	
	Parameters
	----------
	n : int
		試行回数
	k : int
		成功回数
	p : float
		成功確率
	"""
	return math.comb(n, k) * p**k * (1-p)**(n-k)

def expection(n, p):
	""" 
	期待値
	ベルヌーイ試行をn回行ったときの成功回数の期待値を返す．
	
	Parameters
	----------
	n : int
		試行回数
	p : float
		成功確率
	"""
	return n * p

# Generate x values
x = np.arange(0, 51, 1)

# Generate y values
# 50回試行したときにちょうどi回あたる確率を求める
ys = []
for p in Ps:
	ys.append(np.array([binomial(50, i, p) for i in x]))

# plt.style.use('cyberpunk') # Set the style to cyberpunk
plt.figure(figsize = (6,4))

# 二項分布
for i,p in enumerate(Ps):
	plt.scatter(x,ys[i], marker = 'o', label=f'B(50; {p})', c=COLORS[i])
	# 平均値
	# n回試行したときの当たり回数の期待値
	plt.vlines(expection(N, p), YMIN, YMAX,linestyles='dashed', label=f'E(X)={expection(N, p):.2f}', colors=COLORS[i])

plt.xlabel('Number of Successes')
plt.ylabel('Probability')

plt.legend()
plt.grid()
plt.ylim(YMIN, YMAX)

plt.show()