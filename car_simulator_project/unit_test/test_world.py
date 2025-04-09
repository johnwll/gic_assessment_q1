from ..car_simulator.world import World
from ..car_simulator.car   import Car
from ..utility.position    import Vector2D, Direction

def test_world_car():
    """Test car in the world."""
    world = World()
    world.dimension = Vector2D(10, 10)
    
    # Check car before adding.
    assert(world.has_car_at_position(Vector2D(3, 3)) == False)

    # Check car added correctly.
    world.add_car(Car("A", Vector2D(3, 3), Direction.N, []))
    assert(len(world.cars) == 1)
    assert(world.has_car_at_position(Vector2D(3, 3)) == True)
    assert(world.has_car_at_position(Vector2D(0, 0)) == False)

def test_world_out_of_bounds():
    """Test world boundary."""
    world = World()
    world.dimension = Vector2D(100, 50)

    # Inside boundary
    assert(world.out_of_bounds(Vector2D(0, 1))   == False)
    assert(world.out_of_bounds(Vector2D(1, 0))   == False)
    assert(world.out_of_bounds(Vector2D(0, 0))   == False)
    assert(world.out_of_bounds(Vector2D(1, 1))   == False)
    assert(world.out_of_bounds(Vector2D(50, 25)) == False)
    assert(world.out_of_bounds(Vector2D(98, 48)) == False)
    assert(world.out_of_bounds(Vector2D(99, 49)) == False)
    assert(world.out_of_bounds(Vector2D(99, 0))  == False)
    assert(world.out_of_bounds(Vector2D(0, 49))  == False)

    # Out of boundary
    assert(world.out_of_bounds(Vector2D(-1, 0))     == True)
    assert(world.out_of_bounds(Vector2D(0, -1))     == True)
    assert(world.out_of_bounds(Vector2D(-1, -1))    == True)
    assert(world.out_of_bounds(Vector2D(-100, -50)) == True)
    assert(world.out_of_bounds(Vector2D(-100, 0))   == True)
    assert(world.out_of_bounds(Vector2D(0, -50))    == True)
    assert(world.out_of_bounds(Vector2D(100, 50))   == True)
    assert(world.out_of_bounds(Vector2D(101, 51))   == True)
    assert(world.out_of_bounds(Vector2D(101, 0))    == True)
    assert(world.out_of_bounds(Vector2D(0, 51))     == True)
    assert(world.out_of_bounds(Vector2D(1000, 500)) == True)