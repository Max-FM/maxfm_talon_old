from talon import Module, Context, actions
from ...user_settings import get_list_from_csv # Not the best way to import this, but it works.
import subprocess

mod = Module()
ctx = Context()

ctx.matches = """
os: linux
"""

# Defaults do not appear to work if not listed in the csv. Is this due to a bug in user_settings.py?
default_applications = {
    "terminal": "gnome-terminal",
    "firefox": "firefox",
    "chrome": "google-chrome",
    "code": "code",
    "slack": "slack"
}

# Create predefined list of launchable applications. 
mod.list("launch", desc="all launchable applications")
ctx.lists["user.launch"] = get_list_from_csv(
    "applications.csv",
    headers=("app_name", "spoken_name"),
    default=default_applications, # Is this functioning correctly?
)

@mod.action_class
class Actions:    
    def launch_application(app: str):
        """Hacky way of opening applications in Linux."""
        subprocess.run(app)
