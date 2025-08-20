from cuboid import BRICK, BRICK_VOL, WALL_THICKNESS

def generate_layout(dimensions, N):
    """
    Generate brick placement with location + orientation.
    Walls must be at least 200mm thick.
    """
    L, W, H = dimensions
    bricks = []
    brick_id = 1

    for z in range(0, H, 100):
        for y in range(0, W, 100):
            for x in range(0, L, 100):

                # Wall check: within 200mm from any face
                if (x < WALL_THICKNESS or x >= L - WALL_THICKNESS or
                    y < WALL_THICKNESS or y >= W - WALL_THICKNESS or
                    z < WALL_THICKNESS or z >= H - WALL_THICKNESS):

                    # Orient bricks along X-axis if possible
                    if x + 200 <= L:
                        orientation = (200, 100, 100)
                    else:
                        orientation = (100, 200, 100)

                    bricks.append({
                        "id": brick_id,
                        "x": x,
                        "y": y,
                        "z": z,
                        "orientation": orientation
                    })
                    brick_id += 1

                    if brick_id > N:
                        return bricks
    return bricks
