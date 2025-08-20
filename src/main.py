from cuboid import find_best_cuboid
from layout import generate_layout
from visualize import animate_cuboid
from layout import remove

def main():
    N = 100
    best_dims, best_vol = find_best_cuboid(N)
    layout = generate_layout(best_dims, N)

    print("Best Cuboid Dimensions (mm):", best_dims)
    print("Best Volume (mm³):", best_vol)
    print("Bricks Used:", len(layout))

    for brick in layout[:100]:
        print(brick)
    
    layout=remove(layout,100,300,400)

    animate_cuboid(layout, interval=200, limit=100)

if __name__ == "__main__":
    main()
