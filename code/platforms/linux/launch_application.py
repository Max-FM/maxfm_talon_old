from talon import Module, Context, actions
import subprocess

mod = Module()
ctx = Context()

ctx.matches = """
os: linux
"""

@mod.action_class
class Actions:
    def launch_gnome_terminal():
        """Hacky way of opening a terminal in Linux."""
        subprocess.run("gnome-terminal")
    def launch_vscode():
        """Hacky way of launching VS Code in Linux."""
        subprocess.run("code")
    def launch_brave():
        """Hacky way of launching Brave Browser in Linux."""
        subprocess.run("brave-browser")
    def launch_slack():
        """Hacky way of launching Slack in Linux."""
        subprocess.run("slack")
