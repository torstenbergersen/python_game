#!/usr/bin/env python3
import tcod

# define variables for screen size
def main() -> None:
    screen_width = 80
    screen_height = 50

    #keep track of player position
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    # telling tcod which font to use
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    # create screen and title
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Rogue-o-matic",
        # enables vsync if needed
        vsync=True,
    ) as context:
        # creates 'console'
        root_console = tcod.Console(screen_width, screen_height, order="F")
        # change order of y,x to x,y in numpy
        
        # game loop
        while True:
            
            # create @ symbol and put in place
            root_console.print(x=1, y=1, string="@")

            # update screen with current information
            context.present(root_console)

            #create way to exit program
            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit()


if __name__ == "__main__":
    main()