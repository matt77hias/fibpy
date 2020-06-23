[![License][s1]][li]

[s1]: https://img.shields.io/badge/licence-GPL%203.0-blue.svg
[li]: https://raw.githubusercontent.com/matt77hias/fibpy/master/LICENSE.txt

# fibpy

## About
Fibonacci spiral sampling (Quasi-Monte Carlo techniques) utilities.

## Use

### Sampling in unit circle (with jagged boundary)
<p align="center">
<img src="res/circle_mode0_alpha0.png" width="430">
<img src="res/circle_mode1_alpha0.png" width="430">
</p>
<p align="center">Default perturbation - Random perturbation</p>

### Sampling in unit circle (with smooth boundary)
<p align="center">
<img src="res/circle_mode0_alpha2.png" width="429">
<img src="res/circle_mode1_alpha2.png" width="429">
</p>
<p align="center">Default perturbation - Random perturbation</p>

### Sampling on unit hemisphere
<p align="center">
<img src="res/hemisphere_mode0.png" width="429">
<img src="res/hemisphere_mode1.png" width="429">
</p>
<p align="center">Default perturbation - Random perturbation</p>

### Sampling on unit sphere
<p align="center">
<img src="res/sphere_mode0.png" width="429">
<img src="res/sphere_mode1.png" width="429">
</p>
<p align="center">Default perturbation - Random perturbation</p>

### Cosine weighted sampling on unit hemisphere
<p align="center">
<img src="res/cosineweightedhemisphere_mode0.png" width="429">
<img src="res/cosineweightedhemisphere_mode1.png" width="429">
</p>
<p align="center">Default perturbation - Random perturbation</p>

```python
# Code
test.test()
```

## Bibliography
ROBERTS M.: [*Evenly distributing points on a sphere*](http://extremelearning.com.au/evenly-distributing-points-on-a-sphere/), 2018.
