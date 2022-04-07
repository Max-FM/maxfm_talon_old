from talon import Module, Context, actions

ctx = Context()
mod = Module()

mod.apps.brave = "app.name: Brave Browser"
mod.apps.brave = """
os: windows
and app.exe: brave.exe
"""
mod.apps.brave = """
os: mac
and app.bundle: com.brave.Browser
"""
mod.apps.brave = """
os: linux
and app.name: Brave-browser
"""
ctx.matches = r"""
app: brave
"""

@mod.action_class
class BrowserActions:
    def bitwarden_activate():
        """Activate Bitwarden extension."""
        actions.key("ctrl-shift-u")
    def bitwarden_autofill():
        """Auto-fill the last used login for the current website."""
        actions.key("ctrl-shift-l")
    def bitwarden_generate():
        """Generate and copy a new random password to the clipboard."""
        actions.key("ctrl-shift-9")
