from cuboid import find_best_cuboid
from layout import generate_layout
from visualize import animate_cuboid

def main():
    N = 1000   # use 10000 for full build, smaller for animation
    best_dims, best_vol = find_best_cuboid(N)
    layout = generate_layout(best_dims, N)

    print("🔹 Best Cuboid Dimensions (mm):", best_dims)
    print("🔹 Best Volume (mm³):", best_vol)
    print("🔹 Bricks Used:", len(layout))

    print("\nFirst 10 bricks:")
    for brick in layout[:100]:
        print(brick)

    # Animate construction
    animate_cuboid(layout, interval=200, limit=200)

if __name__ == "__main__":
    main()
