from cuboid import find_best_cuboid, BRICK_VOL
from layout import generate_layout

def main():
    N = 10000
    best_dims, best_vol = find_best_cuboid(N)
    layout = generate_layout(best_dims, N)

    print("🔹 Best Cuboid Dimensions (mm):", best_dims)
    print("🔹 Best Volume (mm³):", best_vol)
    print("🔹 Bricks Used:", len(layout))

    print("\nFirst 10 bricks:")
    for brick in layout[:100]:
        print(brick)

    # Save layout to file for inspection
    with open("brick_layout.txt", "w") as f:
        for brick in layout:
            f.write(str(brick) + "\n")

if __name__ == "__main__":
    main()
