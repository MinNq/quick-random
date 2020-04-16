from numpy.random import *


def genData(N, d, dist, **arg):

	'''
	Parameters:
	- N: int. Sample size.
	- d: int. Vector length.
	- dist and **arg: Distribution name (string) and
	  corresponding parameters. Posible options are
	  
	  - dist = 'beta'
	  	a: float. Shape 1.
	  	b: float. Shape 2.

	  - dist = 'binomial'
	  	n: int.
	  	p: float. >= 0 and <= 1.
	  
	  - dist = 'chisquare'
	  	df: float. Number of DOF, > 0.
	  
	  - dist = 'dirichlet'
	  	alpha: array. d-dimensional for sample
	  	of dimension d.

	  - dist = 'exponential'
	  	scale: float. The scale parameter.

	  - dist = 'f'
	  	dfnum: float. DOF in numerator, > 0.
	  	dfden: float. DOF in denominator, > 0.

	  - dist = 'gamma'
	  	shape: float. > 0.
	  	scale: float. > 0.

	  - dist = 'geometric'
	  	p: float. The probability of success
	  	of an individual trial.

	  - dist = 'hypergeometric'
	  	ngood: int. Number of ways to make a
	  	good selection.
	  	nbad: int. Number of ways to make a
	  	bad selection.
	  	nsample: int. Number of items sampled,
	  	> 0 and <= ngood + nbad.

	  - dist = 'laplace'
	  	loc: float. The position of the
	  	distribution peak.
	  	scale: the exponential decay.

	  - dist = 'logisic'
	  	loc: float.
	  	scale: float. < 0.

	  - dist = 'locnormal'
	  	mean: float. Mean value of the
	  	underlying normal distribution.
	  	sigma: float. Standard deviation of the
	  	underlying normal distribution, > 0.
	
	Returns:
	- out: ndarray. Drawn samples from
	  the desired distribution.
	'''

	dists = [beta, binomial, chisquare,
			dirichlet, exponential, f,
			gamma, geometric, gumble,
			hypergeometric, laplace,
			logistic, lognormal]

	for distribution in dists:
		if dist == distribution.__name__:
			out = distribution(**arg, size = (N,d))
			return out

print(genData(3, 3, 'binomial', p = .5, n = 3))