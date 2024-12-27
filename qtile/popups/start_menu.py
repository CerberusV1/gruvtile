from libqtile import qtile
from libqtile.lazy import lazy
from res.themes.colors import gruvbox_dark
from qtile_extras import widget
from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupGridLayout,
    PopupImage,
    PopupText,
    PopupWidget,
    PopupSlider
)

def start_menu(qtile):
    layout = PopupRelativeLayout(
        qtile,
        rows=7,
        cols=9,
        width=450,
        height=550,   
        opacity=0.7,
        hide_on_mouse_leave=True,
        close_on_click=False,
        border_width=0,
        background=gruvbox_dark["bg0_normal"],
        controls=[
            PopupImage(
                filename='/home/cerberus/.config/qtile/res/images/standby_rotated.png',
                mask=True,
                colour=gruvbox_dark["blue"],
                pos_x=0.06,
                pos_y=0.02,
                height=0.17,
                width=0.17,
            ),
            PopupWidget(
                pos_x=0.495,
                pos_y=0.04,
                height=0.06,
                width=0.4,
                v_align="middle",
                h_align="center",
                widget=widget.Clock(
                    font='Open Sans',
                    fontsize=28,
                    format='%H:%M'
                )
            ),
            PopupWidget(
                pos_x=0.395,
                pos_y=0.1,
                height=0.06,
                width=0.8,
                widget=widget.Clock(
                    font='Open Sans',
                    fontsize=28,
                    format='%d.%m.%Y'
                    )
            ),
            PopupWidget(
                pos_x=0.05,
                pos_y=0.25,
                height=0.08,
                width=0.9,
                can_focus=True,
                # mouse_callbacks={"Button1": lazy.spawncmd()},
                widget=widget.Prompt(
                    font='Open Sans',
                    fontsize=18,
                    background=gruvbox_dark["bg3"],
                    cuser=True,
                    curser_color=gruvbox_dark["blue"],
                    foreground=gruvbox_dark["bg1"],
                    prompt='Run: {prompt}',
                    mouse_callbacks={"Button1": lazy.spawncmd()},
                    )
            ),
        ]
    )
    layout.show(relative_to=1, 
                relative_to_bar=True, 
                y=3, 
                x=3, 
                )