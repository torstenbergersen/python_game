#!/usr/bin/env python3
import tcod

from actions import EscapeAction, MovementAction
from entity import Entity
from input_handlers import EventHandler

# define variables for screen size
def main() -> None:
    screen_width = 80
    screen_height = 50

  
    # telling tcod which font to use
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    # entity handling
    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

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
            
            # Draw function
            root_console.print(x=player.x, y=player.y, string=player.char, fg=player.color)

            # update screen with current information
            context.present(root_console)

            # clear console after movement
            root_console.clear()

            for event in tcod.event.wait():
                # send event to event_handler "dispatch" method
                action = event_handler.dispatch(event)

                if action is None:
                    continue

                # update coordinates with movement action
                if isinstance(action, MovementAction):
                    player.move(dx=action.dx, dy=action.dy)
                
                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()