import turtle
import time
from typing import Dict, List


def draw_pole(t: turtle.Turtle, x: float, y: float, height: float) -> None:
    """
    Draw a pole for the Tower of Hanoi.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        x (float): The x-coordinate for the base of the pole.
        y (float): The y-coordinate for the base of the pole.
        height (float): The height of the pole.
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(90)  # Point upwards
    t.pensize(3)
    t.forward(height)
    t.pensize(1)


def draw_disk(t: turtle.Turtle, x: float, y: float, size: float) -> None:
    """
    Draw a disk for the Tower of Hanoi.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        x (float): The x-coordinate for the center of the disk.
        y (float): The y-coordinate for the top of the disk.
        size (float): The width of the disk.
    """
    # Draw the disk
    t.penup()
    t.goto(x, y)  # Center the disk
    t.setheading(0)  # Point to the right
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    t.forward(size / 2)
    t.right(90)
    t.forward(20)  # Height of the disk
    t.right(90)
    t.forward(size)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(size / 2)
    t.end_fill()


def hanoi_visual(t: turtle.Turtle, n: int, source: str, target: str, auxiliary: str, positions: Dict[str, List[int]]) -> None:
    """
    Visualize the Tower of Hanoi moves using turtle graphics.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        n (int): The number of disks to move.
        source (str): The name of the source peg.
        target (str): The name of the target peg.
        auxiliary (str): The name of the auxiliary peg.
        positions (Dict[str, List[int]]): Current positions of disks on each peg.
    """
    if n == 1:
        disk = positions[source].pop()  # Get the top disk from the source
        positions[target].append(disk)  # Move the disk to the target

        # Draw the move
        t.clear()
        draw_poles(t)
        draw_all_disks(t, positions)
        turtle.update()
        time.sleep(1)  # Delay for visualization
        return

    hanoi_visual(t, n - 1, source, auxiliary, target, positions)
    disk = positions[source].pop()
    positions[target].append(disk)

    # Draw the move
    t.clear()
    draw_poles(t)
    draw_all_disks(t, positions)
    turtle.update()
    turtle.delay(60)  # Delay for visualization

    hanoi_visual(t, n - 1, auxiliary, target, source, positions)


def draw_poles(t: turtle.Turtle) -> None:
    """
    Draw all poles for the Tower of Hanoi.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
    """
    draw_pole(t, -150, -150, 100)  # Left pole
    draw_pole(t, 0, -150, 100)      # Middle pole
    draw_pole(t, 150, -150, 100)    # Right pole


def draw_all_disks(t: turtle.Turtle, positions: Dict[str, List[int]]) -> None:
    """
    Draw all disks based on their current positions.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        positions (Dict[str, List[int]]): Current positions of disks on each peg.
    """
    for i, (pole, disks) in enumerate(positions.items()):
        for j, disk in enumerate(disks):
            draw_disk(t, -150 + i * 150, -150 + j * 20, disk)


def main() -> None:
    """
    Main function to set up the Turtle graphics and execute the Tower of Hanoi algorithm.
    """
    n = int(input("Enter the number of disks: "))

    # Initialize positions for each pole
    positions = {
        # Starting from largest to smallest
        'A': [i * 20 for i in range(n, 0, -1)],
        'B': [],
        'C': []
    }

    # Set up turtle
    turtle.tracer(0)  # Disable automatic screen updates for performance
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed

    draw_poles(t)  # Draw the initial poles
    draw_all_disks(t, positions)  # Draw the initial disks
    turtle.update()  # Update the screen to show initial state

    # Start the visualized Tower of Hanoi algorithm
    hanoi_visual(t, n, 'A', 'C', 'B', positions)

    turtle.done()  # Finish drawing


if __name__ == "__main__":
    main()
