import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation

def draw_brick(ax, x, y, z, l, w, h, color="red", alpha=0.9):
    """Draw a single cuboid brick"""
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
    """Animate cuboid construction brick-by-brick (3D + Top view)"""
    fig = plt.figure(figsize=(12,6))

    # Two views
    ax3d = fig.add_subplot(1, 2, 1, projection="3d")
    ax_top = fig.add_subplot(1, 2, 2, projection="3d")

    def update(frame):
        ax3d.cla()
        ax_top.cla()

        # Titles
        ax3d.set_title("3D View (Bricks in Red)")
        ax_top.set_title("Top View (Layer Filling)")

        # Labels
        for ax in [ax3d, ax_top]:
            ax.set_xlabel("X (mm)")
            ax.set_ylabel("Y (mm)")
            ax.set_zlabel("Z (mm)")

        # Top view camera
        ax_top.view_init(90, 90)

        # Draw placed bricks
        for brick in bricks[:frame]:
            x, y, z = brick["x"], brick["y"], brick["z"]
            l, w, h = brick["orientation"]
            draw_brick(ax3d, x, y, z, l, w, h, color="red")
            draw_brick(ax_top, x, y, z, l, w, h, color="red")

        # Brick counter text
        count_text = f"Bricks Placed: {frame}/{len(bricks)}"
        ax3d.text2D(0.05, 0.95, count_text, transform=ax3d.transAxes, fontsize=12, color="blue")
        ax_top.text2D(0.05, 0.95, count_text, transform=ax_top.transAxes, fontsize=12, color="blue")

    ani = FuncAnimation(fig, update, frames=min(limit, len(bricks))+1, interval=interval, repeat=False)
    plt.show()
