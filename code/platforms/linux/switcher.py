from talon import Context, actions
import subprocess

ctx = Context()

ctx.matches = """
os: linux
"""

@ctx.action_class("user")
class SwitcherActions:
    def switcher_menu():
        """Open a menu of running apps to switch to"""
        actions.key('super-s') # Only tested in Ubuntu.
