title: /JupyterLab/
-
tag(): user.python

insert [cell] below: key("escape b")
insert [cell] above: key("escape a")
(delete | wipe | clear | chuck) cell: key("escape d d")
markdown cell: key("escape m")
code cell: key("escape y")
copy cell: key("escape c")
paste cell: key("escape v")
undo cell: key("escape z")
redo cell: key("escape shift-z")

run [cell]: key("ctrl-enter")
run [cell] next: key("shift-enter")
run [cell] insert: key("alt-enter")
run all [cells]: key("escape ctrl-a ctrl-enter")
run all [cells] [above]: key("escape shift-home ctrl-enter")
run all [cells] below: key("escape shift-end ctrl-enter")

select [cell] above: key("escape shift-up")
select [cell] below: key("escape shift-down")
select all [cells]: key("escape ctrl-a")
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

comment line: key("ctrl-/")
indent line: key("ctrl-]")
(outdent | dedent) line: key("ctrl-[")

restart kernel: key("escape 0 0")
interrupt kernel: key("escape i i")

command palate: key("ctrl-shift-c")
simple interface: key("ctrl-shift-d")

go [line] <number>:
    key("alt-g")
    insert(number)
    key("enter")
