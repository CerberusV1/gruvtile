from libqtile.config import Group, Key, Match, re, DropDown, ScratchPad
from libqtile.lazy import lazy
from modules.keys import keys, mod

groups = [
    Group(name="1"),
    Group(name="2"),
    Group(name="3"),
    Group(name="4"),
    Group(name="5"),
    Group(name="6"),
    Group(name="7"),  
    Group(name="8", matches=[Match(wm_class=re.compile(r"^(firefox)$"))]),
    Group(name="9", matches=[Match(wm_class=re.compile(r"^(triliumnext notes)$"))]),
]

for i in groups:
    keys.extend(
        [
            Key([mod], i.name, lazy.group[i.name].toscreen(toggle=True), desc=f"Switch to group {i.name}",),
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc=f"Switch to & move focused window to group {i.name}",),
        ]
    )

groups.append(
    ScratchPad(
        'scratchpad',
        [
            DropDown(
                'term',
                'alacritty',
                width=0.4,
                height=0.5,
                x=0.3,
                y=0.25,
                opacity=1,
                on_focus_lost_hide=True,

            ),
            DropDown(
                "discord",
                "discord",
                match=Match(title=re.compile(r".*Discord$")),
                opacity=1,
                x=0.1,
                y=0.05,
                width=0.8,
                height=0.9,
                on_focus_lost_hide=True,
            ),
            DropDown(
                'files',
                'nemo',
                width=0.6,
                height=0.6,
                x=0.2,
                y=0.2,
                opacity=1,
                on_focus_lost_hide=False,
            ),
            DropDown(
                'calc',
                'qalculate-gtk',
                width=0.3,
                height=0.6,
                x=0.35,
                y=0.2,
                opacity=1,
                on_focus_lost_hide=False,
            ),
            
        ]
    )
)
