from ..utility.position import Direction

def test_direction_rotate_left():
    """Single rotate left."""
    direction = Direction.N
    assert(Direction.rotate_left(direction) == Direction.W)

    direction = Direction.E
    assert(Direction.rotate_left(direction) == Direction.N)

    direction = Direction.S
    assert(Direction.rotate_left(direction) == Direction.E)

    direction = Direction.W
    assert(Direction.rotate_left(direction) == Direction.S)

def test_direction_rotate_right():
    """Single rotate right."""
    direction = Direction.N
    assert(Direction.rotate_right(direction) == Direction.E)

    direction = Direction.E
    assert(Direction.rotate_right(direction) == Direction.S)

    direction = Direction.S
    assert(Direction.rotate_right(direction) == Direction.W)

    direction = Direction.W
    assert(Direction.rotate_right(direction) == Direction.N)

def test_direction_full_rotations():
    """Full rotations"""
    # Complete right rotations.
    direction = Direction.N
    for _ in range(4):
        direction = Direction.rotate_right(direction)
    assert(direction == Direction.N)

    direction = Direction.E
    for _ in range(4):
        direction = Direction.rotate_right(direction)
    assert(direction == Direction.E)

    direction = Direction.S
    for _ in range(4):
        direction = Direction.rotate_right(direction)
    assert(direction == Direction.S)

    direction = Direction.W
    for _ in range(4):
        direction = Direction.rotate_right(direction)
    assert(direction == Direction.W)

    # Complete left rotations.
    direction = Direction.N
    for _ in range(4):
        direction = Direction.rotate_left(direction)
    assert(direction == Direction.N)

    direction = Direction.E
    for _ in range(4):
        direction = Direction.rotate_left(direction)
    assert(direction == Direction.E)

    direction = Direction.S
    for _ in range(4):
        direction = Direction.rotate_left(direction)
    assert(direction == Direction.S)

    direction = Direction.W
    for _ in range(4):
        direction = Direction.rotate_left(direction)
    assert(direction == Direction.W)

    # 5 right rotations.
    direction = Direction.N
    for _ in range(5):
        direction = Direction.rotate_right(direction)
    assert(direction == Direction.E)

    direction = Direction.E
    for _ in range(5):
        direction = Direction.rotate_right(direction)
    assert(direction == Direction.S)

    direction = Direction.S
    for _ in range(5):
        direction = Direction.rotate_right(direction)
    assert(direction == Direction.W)

    direction = Direction.W
    for _ in range(5):
        direction = Direction.rotate_right(direction)
    assert(direction == Direction.N)

    # 5 left rotations.
    direction = Direction.N
    for _ in range(5):
        direction = Direction.rotate_left(direction)
    assert(direction == Direction.W)

    direction = Direction.E
    for _ in range(5):
        direction = Direction.rotate_left(direction)
    assert(direction == Direction.N)

    direction = Direction.S
    for _ in range(5):
        direction = Direction.rotate_left(direction)
    assert(direction == Direction.E)

    direction = Direction.W
    for _ in range(5):
        direction = Direction.rotate_left(direction)
    assert(direction == Direction.S)

def test_direction_rotation():
    """Mirror rotations and cancelled rotations."""
    # Mirror rotation.
    direction = Direction.N
    assert(Direction.rotate_right(Direction.rotate_right(direction)) == Direction.S)

    direction = Direction.E
    assert(Direction.rotate_left(Direction.rotate_left(direction))   == Direction.W)

    direction = Direction.W
    assert(Direction.rotate_right(Direction.rotate_right(direction)) == Direction.E)
    
    direction = Direction.S
    assert(Direction.rotate_left(Direction.rotate_left(direction))   == Direction.N)

    # Cancel out rotation.
    direction = Direction.N
    assert(Direction.rotate_right(Direction.rotate_left(direction)) == Direction.N)

    direction = Direction.S
    assert(Direction.rotate_left(Direction.rotate_right(direction)) == Direction.S)