# main.py
from cuboid import find_best_cuboid
from layout import generate_layout
from visualize import animate_cuboid

def main():
    N = 10000  # number of bricks
    best_dims, best_vol = find_best_cuboid(N)
    layout, firsts = generate_layout(best_dims, N)

    print("Best Cuboid Dimensions (mm):", best_dims)
    print("Best Volume (mm³):", best_vol)
    print("Bricks Used:", len(layout))

    for brick in layout[:10000]:
        print(brick)
    for orient, coords in firsts.items():
        print(f"Orientation {orient} → first at {coords}")

    animate_cuboid(layout, interval=200, limit=10000)

if __name__ == "__main__":
    main()
