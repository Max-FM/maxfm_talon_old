from talon import Module, Context, actions
from ...user_settings import get_list_from_csv # Probably not the best way to import this, but it works.

mod = Module()
ctx = Context()

ctx.matches = """
os: linux
"""

default_applications = {
    "firefox": "firefox",
    "chrome": "google-chrome",
    "brave": "brave-browser",
    "text editor": "gedit",
    "code": "code", # vscode
    "settings": "gnome-control-center",
    "slack": "slack"
}

# Define list of launchable applications to be passed to knausj_talon.
# TODO: See if is is worth automating, if so, find out how.
mod.list("launch", desc="all launchable applications")
ctx.lists["user.launch"] = get_list_from_csv(
    "applications.csv",
    headers=("app_name", "spoken_name"),
    default=default_applications,
)

@mod.action_class
class Actions:
    def launch_terminal():
        """Launch gnome-terminal in Linux (specifically Ubuntu)."""
        actions.key("ctrl-alt-t")
