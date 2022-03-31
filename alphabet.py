from talon import Context
ctx = Context()

# TODO: The "help alphabet" menu does not update to show the new alphabet and instead shows the original alphabet. Need to find a workaround. 

# Need to make the file context more specific than knausj_talon\code\keys.py file in order to successfully override.
ctx.matches = r"""
os: windows
os: mac
os: linux
"""

# default_alphabet = "air bat cap drum each fine gust harp sit jury crunch look made near odd pit quench red sun trap urge vest whale plex yank zip".split(" ")
new_alphabet = "air bat cap drum each fine gust heart ink jury crunch look made near oval pit quench red sun trap urge vest whale plex yank zip".split(" ")
letters_string = "abcdefghijklmnopqrstuvwxyz"
alphabet = dict(zip(new_alphabet, letters_string))
ctx.lists["self.letter"] = alphabet
