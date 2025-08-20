from cuboid import BRICK

ORIENTATIONS = [
    (200, 100, 100),
    (100, 200, 100),
    (100, 100, 200)
]

def generate_layout(dimensions, N):
    """Greedy layer-by-layer brick placement"""
    L, W, H = dimensions
    bricks = []
    brick_id = 1

    for z in range(0, H, 100):  # smallest brick step
        for y in range(0, W, 100):
            for x in range(0, L, 100):
                for orient in ORIENTATIONS:
                    l, w, h = orient
                    if (x + l <= L and y + w <= W and z + h <= H):
                        bricks.append({
                            "id": brick_id,
                            "x": x, "y": y, "z": z,
                            "orientation": orient
                        })
                        brick_id += 1
                        if brick_id > N:
                            return bricks
                        break
    return bricks
