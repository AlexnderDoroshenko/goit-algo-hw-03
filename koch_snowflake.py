import turtle


def koch_curve(t: turtle.Turtle, order: int, size: float) -> None:
    """
    Draw a Koch snowflake fractal using recursion.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        order (int): The recursion depth.
        size (float): The length of the snowflake's sides.
    """
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)  # Recursive call
            t.left(angle)


def main() -> None:
    """
    Main function to set up the turtle and draw the Koch snowflake.
    """
    order = int(input("Enter the recursion level for the Koch snowflake: "))

    window = turtle.Screen()
    window.title("Koch Snowflake")
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed

    for _ in range(3):
        koch_curve(t, order, 300)  # Draw one side of the snowflake
        t.right(120)

    window.mainloop()


if __name__ == "__main__":
    main()
