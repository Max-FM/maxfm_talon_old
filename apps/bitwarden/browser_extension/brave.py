from talon import Module, Context, actions

ctx = Context()
ctx.matches = r"""
app: brave
"""

@ctx.action("user.bitwarden_extension_activate")
def bitwarden_extension_activate_brave():
    """Activate Bitwarden extension."""
    actions.key("ctrl-shift-u")
