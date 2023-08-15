import matplotlib.pyplot as plt
import numpy as np

'''
    N : the number of sample points, suggestion: > 10000
    VARIANCE : the variance in Gaussian distribution to sample points
    MEAN : the mean in Gaussian distribution to sample points
    COLORBAR : the color which you want to show, suggestion: hsv, bone
    GAMMA : the parameter in Gauusian pancakes, suggestion: 1 ~ 10
    BETA : the parameter in Gauusian pancakes, suggestion: 0 ~ 0.25
    MODE:
        'compare' : compare the color between gaussian and gaussian pancake
        'fix' : fix the w vector ((1,0) and (0,1))
        'multi' : compare the differet w vector between two gaussian pancakes
    CLIP : whether fix the all colors to only two colors, suggestion: False to 'hsv', True to 'bone'
'''
N = 10000
VARIANCE = 0.25
MEAN = 0
COLORBAR = 'hsv'
GAMMA = 10
BETA = 0.01
MODE = 'compare'
CLIP = False

def draw(n, mean, variance, gamma, beta, colorbar, mode, clip):
    x1 = np.random.normal(mean, variance, (2, n))
    gamma = gamma
    beta = beta
    
    if mode == 'compare':
        z1 = np.random.uniform(0, 1, n)
        
        w = np.random.normal(mean, variance, (2, 1))
        w = w / np.sqrt(sum(np.square(w)))
        w = 2 * np.sqrt(2) * w
        e = np.random.normal(0, beta , n)
        z2 = ((x1.T @ w).reshape(1, n) * gamma + e) % 1

        titles = ['Gaussian', 'Pancakes']
        
    elif mode == 'fix':
        w = np.array([1, 0])
        w = w / np.sqrt(sum(np.square(w)))
        w = 2 * np.sqrt(2) * w
        e = np.random.normal(0, beta , n)
        z1 = ((x1.T @ w).reshape(1, n) * gamma + e) % 1

        w = np.array([0, 1])
        w = w / np.sqrt(sum(np.square(w)))
        w = 2 * np.sqrt(2) * w
        z2 = ((x1.T @ w).reshape(1, n) * gamma + e) % 1
        
        titles = ['w = (0, 1)', 'w = (1, 0)']
        
    elif mode == 'multi':
        w = np.random.normal(mean, variance, (2, 1))
        w = w / np.sqrt(sum(np.square(w)))
        w = 2 * np.sqrt(2) * w
        e = np.random.normal(0, beta , n)
        z1 = ((x1.T @ w).reshape(1, n) * gamma + e) % 1

        w = np.random.normal(mean, variance, (2, 1))
        w = w / np.sqrt(sum(np.square(w)))
        w = 2 * np.sqrt(2) * w
        e = np.random.normal(0, beta , n)
        z2 = ((x1.T @ w).reshape(1, n) * gamma + e) % 1

        titles = ['Pancakes 1', 'Pancakes 2']
    
    else:
        raise NameError
    
    fig, axes = plt.subplots(1, 2, figsize = (12, 4))

    for axs, color, title in zip(axes, [z1, z2], titles):
        if clip:
            color[color > 0.5] = 1
            color[color <= 0.5] = 0
        im = axs.scatter(x1[0],x1[1], s=3, c=color, cmap=colorbar)
        axs.set_title(title)
        axs.set_xlim([-1, 1])
        axs.set_ylim([-1, 1])
        axs.set_xticks([-1, -0.5, 0, 0.5, 1])
        axs.set_yticks([-1, -0.5, 0, 0.5, 1])
        axs.set_aspect('equal')
        plt.colorbar(im, ax=axs)
        
draw(N, MEAN, VARIANCE, GAMMA, BETA, COLORBAR, MODE)