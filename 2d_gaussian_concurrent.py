import time
import numpy as np
import matplotlib.pyplot as plt
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed


STEP = .0005

def gaussian2D(x, y, sigma):
    """
    gaussian2D distribution.

    parameters: x, y, sigma (standard deviation)
    output: gaussian value
    
    """
    return (
         1 
         / (2 * np.pi * sigma ** 2) 
         * np.exp(-1 * (x ** 2 + y ** 2) / (2 * sigma ** 2))
        )

def plot(z):
    """
    plots gaussian values as a 2D raster image.

    parameter:
    z, takes a 2D array of gaussian values
    
    """
    plt.imshow(z.T)
    plt.gca().invert_yaxis()  # flip axes to get imshow to plot representatively
    plt.xlabel("X"); plt.ylabel("Y"); plt.title(f"{z.shape} points")
    plt.gca().set_aspect(1)

def main(quad_bounds, sigma=1):
    """
    creates a 2D array of Gaussian values
    
    parameters:
    xmin, minimum x value
    xmax, maximum x value
    ymin, minimum y value
    ymax, maximum y value

    sigma, standard deviation

    returns 2D array to plot()
    """
    xmin, xmax, ymin, ymax = quad_bounds

    X = np.arange(float(xmin), float(xmax), STEP) # array of x-coords
    Y = np.arange(float(ymin), float(ymax), STEP) # array of y-coords
    Z = []                                        # 1D array to hold gaussian 
                                                  # values
    for x in X:                                   # looping over x values
        for y in Y:                               # looping over y values
            Z.append(gaussian2D(x, y, sigma))
    ZZ = np.array(Z).reshape(len(X), len(Y))  # 2D array
    return ZZ


if __name__ == "__main__":
    start = time.time()

    quad_bounds = [[-2, 0, -2, 0], [0, 2, -2, 0], [-2, 0, 0, 2], [0, 2, 0, 2]]
    results = []

    with ProcessPoolExecutor(max_workers = 32500) as executor:
        futures = [executor.submit(main, list) for list in quad_bounds]
  

    for future in as_completed(futures):
        results.append(future.result())

    elapsed = time.time() - start
    print(f"Elapsed Time: {elapsed}s")
    
    # using np.block to create a final array of nested blocks.
    finalfig = np.block([[results[0], results[1]], [results[2], results[3]]])

    plot(finalfig)
    
    plt.show()