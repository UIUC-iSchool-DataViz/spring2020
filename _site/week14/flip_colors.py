import numpy as np

# little function that formats colors in way we want
def flip_colors(color,r):
    #colors = np.array([])
    # repeat colors for every particle
    colors = []
    for i in range(r.shape[2]):
        colors.append(color)
    
    colors = np.array(colors)

    # order should be (times, points, colors)
    colors = np.transpose(colors, (0, 2, 1)) # flip the last axes
    
    colors = np.transpose(colors, (0, 2, 1)) # flip the last axes, again? because reasons?

    return colors
