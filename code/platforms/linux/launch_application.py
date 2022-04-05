from talon import Module, Context, actions
import subprocess

mod = Module()
ctx = Context()

ctx.matches = """
os: linux
"""
# Create predefined list of launchable applications. 
# TODO: Make importable from CSV.
mod.list("launch", desc="all launchable applications")
ctx.lists["user.launch"] = {
    "terminal": "gnome-terminal",
    "code": "code",
    "brave": "brave-browser",
    "slack": "slack"
}

@mod.action_class
class Actions:    
    def launch_application(app: str):
        """Hacky way of opening applications in Linux."""
        subprocess.run(app)
