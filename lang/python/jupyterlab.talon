title: /JupyterLab/
-

tag(): user.python

[insert] cell below: key("escape b")
[insert] cell above: key("escape a")
cell (delete | wipe | clear): key("escape d d")
cell markdown: key("escape m")
cell code: key("escape y")
cell copy: key("escape c")
cell paste: key("escape v")
cell undo: key("escape z")
cell redo: key("escape shift-z")

run cell: key("ctrl-enter")
run cell next: key("shift-enter")
run cell insert: key("alt-enter")
run all cells: key("escape ctrl-a ctrl-enter")
run all [cells] above: key("escape shift-home ctrl-enter")
run all [cells] below: key("escape shift-end ctrl-enter")

select all cells: key("escape ctrl-a")
select all [cells] above: key("escape shift-home")
select all [cells] below: key("escape shift-end")

split cell: key("ctrl-shift--")
merge below: key("escape M")
merge above: key("escape shift-up M")

(sidebar | cyber): key("ctrl-b")
line numbers: key("escape L")

save notebook: key("ctrl-s")
save notebook as: key("ctrl-shift-s")

panel next: key("ctrl-shift-]")
panel last: key("ctrl-shift-[")
panel previous: key("ctrl-shift-#")

line comment: key("ctrl-/")
line indent: key("ctrl-]")
line (outdent | dedent): key("ctrl-[")

kernel restart: key("escape 0 0")
kernel interrupt: key("escape i i")

command palate: key("ctrl-shift-c")
simple interface: key("ctrl-shift-d")

go [line] <number>:
    key("alt-g")
    insert(number)
    key("enter")
