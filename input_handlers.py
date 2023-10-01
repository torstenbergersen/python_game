# python type hinting system
from typing import Optional

# import tcod's event system
import tcod.event

# import action class and subclasses
from actions import Action, EscapeAction, MovementAction

class EventHandler(tcod.event.EventDispatch[Action]):
    #event for quitting program
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()
    
    #method for receiving key presses
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        acton: Optional[Action] = None

        #holds pressed key
        key = event.sym

        #define movement actions
        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)

        #define escape action
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        # No valid key was pressed
        return action