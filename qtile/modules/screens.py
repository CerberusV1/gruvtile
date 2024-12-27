#        _   _ _                                         
#   __ _| |_(_) | ___   ___  ___ _ __ ___  ___ _ __  ___ 
#  / _` | __| | |/ _ \ / __|/ __| '__/ _ \/ _ \ '_ \/ __|
# | (_| | |_| | |  __/ \__ \ (__| | |  __/  __/ | | \__ \
#  \__, |\__|_|_|\___| |___/\___|_|  \___|\___|_| |_|___/
#     |_|                                                
# --------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------
from libqtile.config import Screen
from libqtile import bar
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.groupbox2 import GroupBoxRule
from plugins.notifications import Notifier
from popups.powermenu import power_menu
from popups.start_menu import start_menu
from popups.mpris2_layout import MPRIS2_LAYOUT
from popups.volume_notification import VOL_POPUP
from popups.brightness_notification import BRIGHTNESS_NOTIFICATION
from res.themes.colors import gruvbox_dark

# --------------------------------------------------------
# Default GroupBox2 rules
# --------------------------------------------------------
def get_groupbox_rules(monitor_specific=False):
    # Base rules applied to all GroupBoxes
    rules = [
        GroupBoxRule(text_colour=gruvbox_dark["bg3"]).when(focused=False, occupied=True),
        GroupBoxRule(text_colour=gruvbox_dark["bg0_hard"]).when(focused=False, occupied=False),
        GroupBoxRule(text_colour=gruvbox_dark["fg3"]).when(focused=True),
        GroupBoxRule(text_colour=gruvbox_dark["red"]).when(focused=False, occupied=True, urgent=True),
    ]
    
    # Add extra rule for a specific monitor (e.g., show "X" as label)
    if monitor_specific:
        rules.append(GroupBoxRule(text="󰹞"))     #
    
    return rules 

# --------------------------------------------------------
# Widget Defaults
# --------------------------------------------------------
widget_defaults = dict(
    font="Open Sans",
    fontsize=18,
    foreground=gruvbox_dark["fg1"]
)
extension_defaults = widget_defaults.copy()

# --------------------------------------------------------
# Screens
# --------------------------------------------------------
bar.Bar
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    fontsize=24,                                                                                                    # PopUp-Toolkit? 
                    text="",
                    mouse_callbacks={"Button1": lazy.function(start_menu)},
                ),
                # widget.WidgetBox(
                #     fontsize=24,                                                                                                    # PopUp-Toolkit? 
                #     text_closed="",                                                                                                # Python Logo 
                #     text_open="",                                                                                                  # Arrow
                #     widgets=[
                #         widget.WidgetBox(
                #             text_closed="Settings",
                #             text_open="",                                                                                          # Arrow
                #             widgets=[
                #                 widget.TextBox(text='󰹑', mouse_callbacks={"Button1": lazy.spawn("arandr")},),                       # arandr
                #                 widget.TextBox(text='󰸉', mouse_callbacks={"Button1": lazy.spawn("nitrogen")},),                     # nitrogen
                #             ]
                #         ),
                #         widget.WidgetBox(
                #             text_closed="Connections",
                #             text_open="",                                                                                          # Arrow
                #         widgets=[                               
                #                 widget.TextBox(text='󰛳', mouse_callbacks={"Button1": lazy.spawn("nm-connection-editor")},),         # Network
                #                 widget.TextBox(text='󰂯', mouse_callbacks={"Button1": lazy.spawn("blueman-manager")},),              # BT
                #                 widget.TextBox(text='', mouse_callbacks={"Button1": lazy.spawn("wireguird")},),                    # VPN
                #             ]
                #         ),
                #     ]
                # ),
                widget.GroupBox2(
                    fontsize=30,
                    fontshadow=gruvbox_dark["fg1"],
                    center_aligned=True,
                    visible_groups=['1', '2', '3', '4', '5', '6', '7'],
                    padding=5,
                    rules=get_groupbox_rules(monitor_specific=True),
                ),
                widget.Spacer(length=20),
                widget.Mpris2(
                    name="mpris2",
                    width=350,
                    scroll=True,
                    scroll_clear=True,
                    format='{xesam:title} - {xesam:artist}',
                    paused_text='{track}   ',
                    popup_layout=MPRIS2_LAYOUT,
                    poll_interval=15,
                    popup_show_args={'relative_to': 2, 'relative_to_bar': True, 'y': 3},
                    mouse_callbacks={'Button1': lazy.widget["mpris2"].toggle_player()},
                ),
                widget.Spacer(),
                widget.Battery(
                    format='  {percent:2.0%}',
                    low_percentage=0.25,
                    low_foreground=gruvbox_dark["orange"],
                ),
                widget.Memory(
                    format='  {MemPercent}%',
                ),
                widget.CPU(
                    format='  {load_percent}%',
                ),
                widget.Spacer(
                    length=2
                ),
                widget.Systray(
                    icon_size=21,
                    # mask=gruvbox_dark["fg1"],
                    # icon_theme="gruvbox"
                ),
                widget.Spacer(
                    length=6
                ),
                widget.Clock(
                ),
                widget.Spacer(
                    length=2
                ),
                widget.TextBox(
                    fontsize=20,
                    text=" ",
                    mouse_callbacks={"Button1": lazy.function(power_menu)},
                ),
                # Invisible widgets for popup notifications at value change
                widget.BrightnessControl(
                    mode="popup",
                    popup_layout=BRIGHTNESS_NOTIFICATION,
                    device='/sys/class/backlight/intel_backlight',
                    brightness_path='brightness',
                    max_brightness_path='max_brightness',
                    popup_show_args={'relative_to': 8, 'y': -70},
                ),
                widget.PulseVolumeExtra(
                    mode='popup',
                    fmt="",
                    popup_layout=VOL_POPUP,
                    popup_hide_timeout=3,
                    popup_show_args={'relative_to': 8, 'y': -70},
                    ),
            ],
            background=gruvbox_dark["bg0_hard"],
            opacity=0.75,
            size=32,
            margin=[3, 3, 0, 3],
        ),
    ),
]

notifier = Notifier(
    x=835,
    y=38,
    width=250,
    height=96,
    format='<b>{summary}</b>\n{app_name}\n{body}',
    # file_name='/home/cerberus/.config/qtile/normal.png',    # Not working
    foreground=gruvbox_dark["fg1"],
    background=(gruvbox_dark["bg0_hard"], 
                gruvbox_dark["bg0_hard"], 
                gruvbox_dark["orange"]
                ),
    horizontal_padding=8,
    vertical_padding=8,
    opacity=0.65,
    border_width=0,
    font='Open Sans',
    font_size=16,
    # overflow='more_width',
    fullscreen='queue',
    screen=0,
    actions=True,
    # wrap=True
)