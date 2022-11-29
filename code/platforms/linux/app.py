from talon import Module, Context, actions

mod = Module()

ctx = Context()
ctx.matches = r"""
os: linux
"""

@mod.action_class
class AppActions:
    def window_maximize():
        """Maximize the active window."""
        actions.key("super-m")
    def window_minimize():
        """Minimize the active window."""
        actions.key("super-m")
    def window_split_left():
        """Maximize the window to the left side of the screen."""
        actions.key("super-ctrl-left")
    def window_split_right():
        """Maximize the window to the right side of the screen."""
        actions.key("super-ctrl-right")
