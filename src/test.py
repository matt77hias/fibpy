from plot_utils import vis_samples_2D, vis_samples_3D
from sampling import fibonacci_spiral_samples_in_unit_circle, fibonacci_spiral_samples_on_unit_hemisphere, fibonacci_spiral_samples_on_unit_sphere, fibonacci_spiral_cosine_weighted_samples_on_unit_hemisphere

def test(nb_samples=256):
    # mode 0: default
    # mode 1: random perturbation
    for mode in [0, 1]:
        vis_samples_2D(fibonacci_spiral_samples_in_unit_circle(nb_samples=nb_samples, mode=mode, alpha=0.0))
        vis_samples_2D(fibonacci_spiral_samples_in_unit_circle(nb_samples=nb_samples, mode=mode, alpha=2.0))
        vis_samples_3D(fibonacci_spiral_samples_on_unit_hemisphere(nb_samples=nb_samples, mode=mode))
        vis_samples_3D(fibonacci_spiral_samples_on_unit_sphere(nb_samples=nb_samples, mode=mode))
        vis_samples_3D(fibonacci_spiral_cosine_weighted_samples_on_unit_hemisphere(nb_samples=nb_samples, mode=mode))