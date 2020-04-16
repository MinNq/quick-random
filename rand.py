from numpy.random import default_rng
rng = default_rng()


def genData(N, d, dist, **arg):

	'''
	Parameters:
	- N: int. Sample size.
	- d: int. Vector length.from numpy.random import default_rng
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

	Return:
	- out: Drawn samples from desired distribution.
	'''
	
	# ignore repeated size
	try:
		del arg['size']
	except:
		pass
		
	out = getattr(rng, dist)(**arg, size = (N,d))


	return out
	- dist and **arg: Distribution name (string) and
	  corresponding parameters. Read NumPy documentation
	  (https://docs.scipy.org/doc/numpy-1.15.1/reference/routines.random.html)
	  to learn about possible options.

	Return:
	- out: Drawn samples from desired distribution.
	'''

	out = getattr(rng, dist)(**arg, size = (N,d))
	return out
