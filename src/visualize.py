# visualize.py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation

def draw_brick(ax, brick, color="red", alpha=0.9):
    x, y, z = brick["x"], brick["y"], brick["z"]
    l, w, h = brick["orientation"]
    vertices = [
        [x, y, z], [x+l, y, z], [x+l, y+w, z], [x, y+w, z],
        [x, y, z+h], [x+l, y, z+h], [x+l, y+w, z+h], [x, y+w, z+h]
    ]
    faces = [
        [vertices[j] for j in [0,1,2,3]],
        [vertices[j] for j in [4,5,6,7]],
        [vertices[j] for j in [0,1,5,4]],
        [vertices[j] for j in [2,3,7,6]],
        [vertices[j] for j in [1,2,6,5]],
        [vertices[j] for j in [0,3,7,4]]
    ]
    ax.add_collection3d(Poly3DCollection(faces, alpha=alpha, facecolor=color, edgecolor="black"))

def animate_cuboid(bricks, interval=200, limit=200):
    fig = plt.figure(figsize=(12,6))
    ax3d = fig.add_subplot(1, 2, 1, projection="3d")
    ax_top = fig.add_subplot(1, 2, 2, projection="3d")

    def update(frame):
        ax3d.cla()
        ax_top.cla()
        ax3d.set_title("3D View (Walls Only, Hollow, No Top/Bottom)")
        ax_top.set_title("Top View (Walls Only)")
        for ax in [ax3d, ax_top]:
            ax.set_xlabel("X (mm)")
            ax.set_ylabel("Y (mm)")
            ax.set_zlabel("Z (mm)")
        ax_top.view_init(90, 90)

        for brick in bricks[:frame]:
            draw_brick(ax3d, brick, color="red", alpha=0.9)
            draw_brick(ax_top, brick, color="red", alpha=0.6)

        ax3d.text2D(0.05, 0.95, f"Bricks Placed: {frame}/{len(bricks)}", transform=ax3d.transAxes, color="blue")
        ax_top.text2D(0.05, 0.95, f"Bricks Placed: {frame}/{len(bricks)}", transform=ax_top.transAxes, color="blue")

    ani = FuncAnimation(fig, update, frames=min(limit, len(bricks))+1, interval=interval, repeat=False)
    plt.show()
