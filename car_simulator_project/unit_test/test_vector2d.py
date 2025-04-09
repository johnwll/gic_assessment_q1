from ..utility.position import Vector2D, Direction

def test_vector2d_direction_addition():
    """Vector2D and direction addition"""
    # Test direction one step addition.
    vector    = Vector2D(0, 0)
    direction = Direction.N
    assert(vector + direction == Vector2D(0, 1))
    
    vector    = Vector2D(0, 0)
    direction = Direction.E
    assert(vector + direction == Vector2D(1, 0))
    
    vector    = Vector2D(0, 0)
    direction = Direction.S
    assert(vector + direction == Vector2D(0, -1))
    
    vector    = Vector2D(0, 0)
    direction = Direction.W
    assert(vector + direction == Vector2D(-1, 0))

    # Test direction two step addition.
    vector    = Vector2D(0, 0)
    direction = Direction.N
    assert(vector + direction + direction == Vector2D(0, 2))
    
    vector    = Vector2D(0, 0)
    direction = Direction.E
    assert(vector + direction + direction == Vector2D(2, 0))
    
    vector    = Vector2D(0, 0)
    direction = Direction.S
    assert(vector + direction + direction == Vector2D(0, -2))
    
    vector    = Vector2D(0, 0)
    direction = Direction.W
    assert(vector + direction + direction == Vector2D(-2, 0))

def test_vector2d_different_direction_addition():
    """Vector2D and different directions addition"""
    # Adding different directions to a vector.
    vector = Vector2D(-3, 4)
    assert(vector + Direction.N + Direction.E + Direction.S == Vector2D(-2, 4))

    vector = Vector2D(101, -10)
    assert(vector + Direction.E + Direction.E + Direction.N == Vector2D(103, -9))