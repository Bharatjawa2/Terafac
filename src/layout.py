from cuboid import BRICK

ORIENTATIONS = [
    (200, 100, 100),
    (100, 200, 100),
    (100, 100, 200)
]

def generate_layout(dimensions, N):
    """Place bricks only for vertical walls, 200mm thick, no top/bottom"""
    L, W, H = dimensions
    bricks = []
    brick_id = 1
    first_occurrence = {}

    for z in range(0, H, 100):
        for y in range(0, W, 100):
            for x in range(0, L, 100):
                for orient in ORIENTATIONS:
                    l, w, h = orient
                    if x + l <= L and y + w <= W and z + h <= H:
                        if 200 <= x <= L-200-l and 200 <= y <= W-200-w:
                            continue
                        # Skip top and bottom
                        if z == 0 or z + h >= H:
                            continue

                        bricks.append({
                            "id": brick_id,
                            "x": x, "y": y,
                            "z": z,
                            "orientation": orient
                        })

                        if orient not in first_occurrence:
                            first_occurrence[orient] = (x, y, z)

                        brick_id += 1
                        if brick_id > N:
                            return bricks, first_occurrence
                        break
    return bricks, first_occurrence

def remove(layout, x, y, z):
    """Remove a brick at a specific coordinate"""
    return [brick for brick in layout if (brick["x"], brick["y"], brick["z"]) != (x, y, z)]
