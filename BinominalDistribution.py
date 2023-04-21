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
# コインを50回投げて，ちょうどi回表が出る確率を求める
y = np.array([binomial(50, i, 0.5) for i in x])
# 当たり確率p=1/6
y2 = np.array([binomial(50, i, 1/6) for i in x])
# 当たり確率p=3/4
y3 = np.array([binomial(50, i, 3/4) for i in x])

# plt.style.use('cyberpunk') # Set the style to cyberpunk
plt.figure(figsize = (6,4))

plt.scatter(x, y, marker = 'o', label='B(50; 0.5)')
plt.scatter(x, y2, marker = 'o', c='lime', label='B(50; 1/6)')
plt.scatter(x, y3, marker = 'o', c='red', label='B(50; 3/4)')

# 平均値
# n回試行したときの当たり回数の期待値
plt.vlines(expection(50, 0.5), 0, 0.16, colors='blue', linestyles='dashed', label=f'E(X)={expection(50, 0.5):.2f}')
plt.vlines(expection(50, 1/6), 0, 0.16, colors='lime', linestyles='dashed', label=f'E(X)={expection(50, 1/6):.2f}')
plt.vlines(expection(50, 3/4), 0, 0.16, colors='red', linestyles='dashed', label=f'E(X)= {expection(50, 3/4):.2f}')

plt.xlabel('Number of Successes')
plt.ylabel('Probability')

plt.legend()
plt.grid()

plt.show()