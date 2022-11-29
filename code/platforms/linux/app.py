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
    def window_tiling():
        """Toggle Pop_OS! window tiling."""
        actions.key("super-y")
    def workspace_next():
        """Switch to the next workspace."""
        actions.key("super-ctrl-down")
    def workspace_previous():
        """Switch to the previous workspace."""
        actions.key("super-ctrl-up")
    def move_window_previous_workspace():
        """Move window to the previous workspace."""
        actions.key("super-shift-up")
    def move_window_next_workspace():
        """Move window to the next workspace."""
        actions.key("super-shift-down")
