import numpy as np
import matplotlib.pyplot as plt

def plot_views(dimensions):
    L, W, H = [d // 100 for d in dimensions]
    top_view = np.ones((W, L))
    side_view = np.ones((H, L))

    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.title("Top View (X-Y)")
    plt.imshow(top_view, cmap="Blues")

    plt.subplot(1, 2, 2)
    plt.title("Side View (X-Z)")
    plt.imshow(side_view, cmap="Greens")

    plt.show()
