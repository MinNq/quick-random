# quick-random

A universal function for numpy.random

## Examples

```python
>>> samples = genData(3, 3, 'binomial', n = 3, p =.5)
>>> print(samples)
>>> [[0 2 1]
 [1 1 3]
 [1 0 3]]
```

```python
>>> samples = genData(3, 3, 'beta', a = 6, b = 7)
>>> print(samples)
>>> [[0.53849598 0.21853685 0.53845973]
 [0.37739179 0.44551544 0.47010355]
 [0.37671391 0.60242096 0.47367311]]
```
