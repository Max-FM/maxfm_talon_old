window (new|open): app.window_open()
window next: app.window_next()
window last: app.window_previous()
window close: app.window_close()
window maximize: user.window_maximize()
window minimize: user.window_minimize()
window split left: user.window_split_left()
window split right: user.window_split_right()
window tile: user.toggle_window_tiling()

workspace (up | above): user.workspace_up()
workspace (down | below): user.workspace_down()

focus <user.running_applications>: user.switcher_focus(running_applications)
running list: user.switcher_toggle_running()
running close: user.switcher_hide_running()
launch <user.launch_applications>: user.switcher_launch(launch_applications)

snap <user.window_snap_position>: user.snap_window(window_snap_position)
snap next [screen]: user.move_window_next_screen()
snap last [screen]: user.move_window_previous_screen()
snap (up | above): user.move_window_previous_workspace()
snap (down | below): user.move_window_next_workspace()
snap screen <number>: user.move_window_to_screen(number)
snap <user.running_applications> <user.window_snap_position>:
    user.snap_app(running_applications, window_snap_position)
snap <user.running_applications> [screen] <number>:
    user.move_app_to_screen(running_applications, number)
