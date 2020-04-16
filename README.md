# quick-random

We introduce `genData()` - a universal function for `numpy.random`. Instead of specific functions for
individual distributions, you can now indicate the distribution name and corresponding parameters inside
a single `genData()`.

## Syntax

The function is called as follow:

```
genData(N, d, dist, **arg)
```

Parameters:
- `N`: int. Sample size.
- `d`: int. Vector length.
- `dist` and `**arg`: Distribution name (string) and
  corresponding parameters. Read [NumPy documentation] to
  learn possible options.

## Examples

```python
>>> genData(3, 3, 'binomial', n = 3, p =.5)
array([[1, 1, 1],
       [1, 1, 2],
       [3, 1, 1]])
```

```python
>>> genData(3, 3, 'beta', a = 6, b = 7)
array([[0.38453819, 0.55604113, 0.40391136],
       [0.66146869, 0.5959965 , 0.49430322],
       [0.16217435, 0.42316647, 0.51540831]])
```

[NumPy documentation]: https://docs.scipy.org/doc/numpy-1.15.1/reference/routines.random.html
