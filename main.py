#!/usr/bin/env python3
import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

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

    event_handler = EventHandler()

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
            root_console.print(x=player_x, y=player_y, string="@")

            # update screen with current information
            context.present(root_console)

            for event in tcod.event.wait():
                # send event to event_handler "dispatch" method
                action = event_handler.dispath(event)

                if action is None:
                    continue

                # update user coordinates with movement action
                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy
                
                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()