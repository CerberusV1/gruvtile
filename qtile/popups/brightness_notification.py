from res.themes.colors import gruvbox_dark
from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupText,
    PopupSlider
)


BRIGHTNESS_NOTIFICATION = PopupRelativeLayout(
    width=150,
    height=150,
    opacity=0.7,
    background=gruvbox_dark["bg0_soft"],
    controls=[
        PopupText(
            text="󰃞",
            fontsize=70,
            foreground=gruvbox_dark["fg1"],
            # name="text",
            pos_x=0,
            pos_y=0,
            height=0.8,
            width=0.8,
            v_align="middle",
            h_align="center",
        ),
        PopupSlider(
            name="brightness",
            pos_x=0.1,
            pos_y=0.7,
            width=0.8,
            height=0.2,
            colour_below=gruvbox_dark["blue"],
            # bar_border_size=2,
            bar_border_margin=1,
            bar_size=8,
            marker_size=0,
            end_margin=0,
        ),
    ],
)