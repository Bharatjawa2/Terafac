import numpy as np

# Brick properties
BRICK = (200, 100, 100)    # mm
BRICK_VOL = np.prod(BRICK)
WALL_THICKNESS = 200

def feasible(L, W, H, N):
    """Check if a cuboid with given dimensions is feasible"""
    bricks_needed = (L * W * H) // BRICK_VOL
    return (bricks_needed <= N and
            L >= 2 * WALL_THICKNESS and
            W >= 2 * WALL_THICKNESS and
            H >= 2 * WALL_THICKNESS)

def find_best_cuboid(N, search_range=1000):
    """Find best cuboid dimensions near cube root volume"""
    total_volume = N * BRICK_VOL
    target_side = round((total_volume) ** (1/3) / 100) * 100

    best_dims = (0, 0, 0)
    best_volume = 0

    for L in range(target_side - search_range, target_side + search_range, 100):
        for W in range(target_side - search_range, target_side + search_range, 100):
            for H in range(target_side - search_range, target_side + search_range, 100):
                if L <= 0 or W <= 0 or H <= 0:
                    continue
                if feasible(L, W, H, N):
                    volume = L * W * H
                    if volume > best_volume:
                        best_volume = volume
                        best_dims = (L, W, H)
    return best_dims, best_volume
