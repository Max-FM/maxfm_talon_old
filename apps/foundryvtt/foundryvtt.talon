title: /Foundry Virtual Tabletop/
-
# Rolling dice
roll <number> d <number> [<user.dice_modifier_sign> <number>] [with <user.dice_advantage>]:
    user.roll_dice(number_1, number_2, user.dice_modifier_sign or "", number_3 or 0, user.dice_advantage or "")
