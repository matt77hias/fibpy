import numpy as np

def fibonacci_spiral_samples_in_unit_circle(nb_samples, mode=0, alpha=2):
    shift = 1.0 if mode == 0 else nb_samples * np.random.random()
 
    ga = np.pi * (3.0 - np.sqrt(5.0))
    # Boundary points
    np_boundary = round(alpha * np.sqrt(nb_samples))
    
    ss = np.zeros((nb_samples,2))
    j = 0
    for i in range(nb_samples):
        if i > nb_samples - (np_boundary + 1):
            r = 1.0
        else:
            r = np.sqrt((i + 0.5) / (nb_samples - 0.5 * (np_boundary + 1)))
        phi   = ga * (i + shift)
        ss[j,:] = np.array([r * np.cos(phi), r * np.sin(phi)])
        j += 1
    return ss

def fibonacci_spiral_samples_on_unit_hemisphere(nb_samples, mode=0, up=True):
    n = 2 * nb_samples
    rn = range(nb_samples, n) if up else range(nb_samples) 
    
    shift = 1.0 if mode == 0 else n * np.random.random()
 
    ga = np.pi * (3.0 - np.sqrt(5.0))
    offset = 1.0 / nb_samples
    
    ss = np.zeros((nb_samples,3))
    j = 0
    for i in rn:
        phi   = ga * ((i + shift) % n)
        cos_phi = np.cos(phi)
        sin_phi = np.sin(phi)
        cos_theta = ((i + 0.5) * offset) - 1.0
        sin_theta = np.sqrt(1.0 - cos_theta*cos_theta)
        ss[j,:] = np.array([cos_phi * sin_theta, sin_phi * sin_theta, cos_theta])
        j += 1
    return ss
    
def fibonacci_spiral_samples_on_unit_sphere(nb_samples, mode=0):
    shift = 1.0 if mode == 0 else nb_samples * np.random.random()
 
    ga = np.pi * (3.0 - np.sqrt(5.0))
    offset = 2.0 / nb_samples
    
    ss = np.zeros((nb_samples,3))
    j = 0
    for i in range(nb_samples):
        phi   = ga * ((i + shift) % nb_samples)
        cos_phi = np.cos(phi)
        sin_phi = np.sin(phi)
        cos_theta = ((i + 0.5) * offset) - 1.0
        sin_theta = np.sqrt(1.0 - cos_theta*cos_theta)
        ss[j,:] = np.array([cos_phi * sin_theta, sin_phi * sin_theta, cos_theta])
        j += 1
    return ss
      
def fibonacci_spiral_cosine_weighted_samples_on_unit_hemisphere(nb_samples, mode=0):
    shift = 1.0 if mode == 0 else nb_samples * np.random.random()
 
    ga = np.pi * (3.0 - np.sqrt(5.0))
    
    ss = np.zeros((nb_samples,3))
    j = 0
    for i in range(nb_samples):
        sin_theta = np.sqrt((i + 0.5) / (nb_samples - 0.5))
        cos_theta = np.sqrt(1.0 - sin_theta*sin_theta)
        phi   = ga * (i + shift)
        cos_phi = np.cos(phi)
        sin_phi = np.sin(phi)
        ss[j,:] = np.array([cos_phi * sin_theta, sin_phi * sin_theta, cos_theta])
        j += 1
    return ss