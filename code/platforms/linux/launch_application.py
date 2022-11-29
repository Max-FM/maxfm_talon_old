from talon import Module, Context, actions
from ...user_settings import get_list_from_csv # Probably not the best way to import this, but it works.
import subprocess

mod = Module()
ctx = Context()

# Written specifically for Ubuntu.
ctx.matches = """
os: linux
"""

default_applications = {
    "firefox": "firefox",
    "chrome": "google-chrome",
    "brave": "brave-browser",
    "text editor": "gedit",
    "code": "code",
    "slack": "slack",
    "discord": "discord",
    "files": "nautilus",
    "settings": "gnome-control-center",
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
    def launch_menu():
        """Open a menu of running apps to open."""
        actions.key('super')
    def launch_terminal():
        """Launch gnome-terminal."""
        actions.key("super-t")
    def launch_chrome_application(app_id: str, driver: str="brave-browser", profile: str="Profile 1"):
        """Launch Chrome application."""
        subprocess.run(
            [driver, f"--app-id={app_id}", f"--profile-directory={profile}"],
            start_new_session=True
        )
