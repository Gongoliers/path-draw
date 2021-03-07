import zones
import turtle
from draw_utils import *
import power_cells
import markers

galactic_search_a_red = 1
galactic_search_a_blue = 2
galactic_search_b_red = 3
galactic_search_b_blue = 4
barrel_racing = 5
slalom = 6
bounce = 7


def draw_map(map):
    turtle.tracer(False)
    if map == galactic_search_a_red:
        start_zone = zones.galactic_search_start
        end_zone = zones.galactic_search_end
        stars = power_cells.galactic_a_red
        star_color = "red"
        my_markers = markers.galactic_search
    elif map == galactic_search_a_blue:
        start_zone = zones.galactic_search_start
        end_zone = zones.galactic_search_end
        stars = power_cells.galactic_a_blue
        star_color = "blue"
        my_markers = markers.galactic_search
    elif map == galactic_search_b_red:
        start_zone = zones.galactic_search_start
        end_zone = zones.galactic_search_end
        stars = power_cells.galactic_b_red
        star_color = "red"
        my_markers = markers.galactic_search
    elif map == galactic_search_b_blue:
        start_zone = zones.galactic_search_start
        end_zone = zones.galactic_search_end
        stars = power_cells.galactic_b_blue
        star_color = "blue"
        my_markers = markers.galactic_search
    elif map == barrel_racing:
        start_zone = zones.barrel_racing_start
        end_zone = zones.barrel_racing_end
        stars = []
        star_color = "blue"
        my_markers = markers.barrel_racing
    elif map == slalom:
        start_zone = zones.slalom_start
        end_zone = zones.slalom_end
        stars = []
        star_color = "blue"
        my_markers = markers.slalom
    elif map == bounce:
        start_zone = zones.bounce_start
        end_zone = zones.bounce_end
        stars = power_cells.bounce
        star_color = "green"
        my_markers = markers.bounce

    move(0, 0)
    turtle.setheading(0)
    turtle.speed(speed=0)

    move(0, 15)
    draw_rectangle(30, 15, 'white')

    # Start zone
    move(start_zone[0][0], start_zone[0][1])
    draw_rectangle(start_zone[1], start_zone[2], 'green')

    # End zone
    move(end_zone[0][0], end_zone[0][1])
    draw_rectangle(end_zone[1], end_zone[2], 'red')

    # Draw markers
    for marker in my_markers:
        move(marker[0] - 0.125, marker[1] + 0.125)
        draw_rectangle(0.25, 0.25, 'gray')

    # Draw power cells
    for star in stars:
        move(star[0] - 0.25, star[1] + 0.25)
        draw_rectangle(0.5, 0.5, star_color)
