from numpy.random import default_rng
rng = default_rng()


def genData(N, d, dist, **arg):

	'''
	Parameters:
	- N: int. Sample size.
	- d: int. Vector length.
	- dist and **arg: Distribution name (string) and
	  corresponding parameters. Read NumPy documentation
	  (https://docs.scipy.org/doc/numpy-1.15.1/reference/routines.random.html)
	  to learn about possible options.
	'''

	out = getattr(rng, dist)(**arg, size = (N,d))
	return out
