import os
import socket
import subprocess
#import pulseaudio

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, extension,hook
from libqtile.config import Click, Drag, Group, Key, Screen, Match
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

#PALERA DE COLORES 1
colorAzul = "#053B52"
colorNaranja1 = "#EF4C1E"
colorAmarrillo = "#F9BD2D"

#PALETA DE COLORES 2
colorMarrillo2 = "#FDEB6C"
colorNaranja2 = "#D94C2A"
colorNegro1 = "#262223"

#colores default
colorBlanco = "#ffffff"
colorNegro = "#000000"

mod = "mod4"
terminal = guess_terminal()


keys = [   
 Key([mod], "k", lazy.layout.down(), desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(), desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.run_extension(extension.DmenuRun(
        dmenu_prompt="Ejecutar",
        dmenu_font="Ubuntu-18",
        background=colorAzul,
        foreground=colorNaranja1,
        selected_background=colorNaranja1,
        selected_foregorund=colorAmarrillo,
        ))),
    Key([mod,"shift"], "l", lazy.layout.grow()),
    Key([mod, "shift" ], "h", lazy.layout.shrink()),

    Key([mod, "shift" ], "f", lazy.window.toggle_floating()),
     Key([], "Print", lazy.spawn("gnome-screenshot -i")),
        Key([mod], "Print", lazy.spawn("gnome-screenshot -p")),
        #  Key([],"XF86AudioLowerVolumen", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
        #Key([mod], "-", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
]

__groups = {
    1: Group("TER "),
    2: Group("WWW 爵", matches=[Match(wm_class=["brave"])]),
    3: Group("DEV "),
    4: Group("BD "),
    5: Group("IDE "),
    0: Group("HTTP "),
}
groups = [__groups[i] for i in __groups]


def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]
 

for i in groups:
    keys.extend([
        Key([mod], str(get_group_key(i.name)), lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod, "shift"], str(get_group_key(i.name)),
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])
layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": colorNaranja1,
                "border_normal": colorAzul
                }


layouts = [
   layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 10,
         sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
         section_fontsize = 10,
         border_width = 2,
         bg_color = colorAzul,
         active_bg = colorNaranja1,
         active_fg = colorAzul,
         inactive_bg = colorAzul,
         inactive_fg = colorAmarrillo,
         padding_left = 0,
         padding_x = 0,
         padding_y = 5,
         section_top = 10,
         section_bottom = 20,
         level_shift = 8,
         vspace = 3,
         panel_width = 200
         ),
    layout.Floating(**layout_theme)

]



prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())



widget_defaults = dict(
    font='UbuntuMono Nerd Font Bold',
     fontsize=16,
    padding=3,

)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
            widget.GroupBox(
                      font = "UbuntuBold Nerd Font",
                       fontsize = 13,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colorAmarrillo,
                       inactive = colorNaranja1,
                       rounded = False,
                       highlight_color = colorAzul,
                       highlight_method = "line",
                       this_current_screen_border = colorAmarrillo,
                       this_screen_border = colorAmarrillo,
                       other_current_screen_border = colorNaranja1,
                       other_screen_border = colorNaranja1,
                       foreground = colorNaranja1,
                       background = colorAzul

                ),
                widget.Prompt(
                 prompt = prompt,
                       font = "UbuntuMono Nerd Font",
                       padding = 5,
                       foreground = colorNaranja1,
                       background = colorAzul
                        ),
                 widget.Sep(
                       linewidth = 0,
                       padding = 5,
                        foreground = colorNaranja1,
                       background = colorAzul
                       ),
                 widget.WindowName(
                        foreground = colorAmarrillo,
                       background = colorAzul,
                       padding = 0
                       ),
                 widget.Systray(
                       background = colorAzul,
                       padding = 5
                       ),
                 widget.Sep(
                       linewidth = 0,
                       padding = 5,
                        foreground = colorAzul,
                       background = colorAzul,
                       ),
             widget.TextBox(
                       text = '',
                        foreground = colorAmarrillo,
                       background = colorAzul,
                       padding = -3,
                       fontsize = 37
                       ),
             widget.Net(
                       interface = "enp1s0",
                       format = '{down} ↓↑ {up}',
                       foreground = colorAzul,
                       background = colorAmarrillo,
                       padding = 5
                       ),
            widget.TextBox(
                       text = '',
                        foreground = colorNaranja1,
                       background = colorAmarrillo,
                       padding = -3,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = "",
                       padding = 2,
                        foreground = colorAzul,
                       background = colorNaranja1,
                       fontsize = 11
                       ),
                       widget.ThermalSensor(
                         foreground = colorAzul,
                       background = colorNaranja1,
                        threshold = 90,
                        padding = 5
                        ),
                       widget.TextBox(
                       text = '',
                        foreground = colorAmarrillo,
                       background = colorNaranja1,
                       padding = -3,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = "  ",
                        foreground = colorAzul,
                       background = colorAmarrillo,
                       padding = 0,
                       fontsize = 14
                       ),
              widget.Memory(
                        foreground = colorAzul,
                       background = colorAmarrillo,
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       foreground = colorNaranja1,
                       background = colorAmarrillo,
                       padding = -3,
                       fontsize = 37
                       ),
              widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colorAzul,
                       background = colorNaranja1,
                       padding = 0,
                       scale = 0.7
                       ),
              widget.CurrentLayout(
                       foreground = colorAzul,
                       background = colorNaranja1,
                       padding = 5
                       ),

              widget.TextBox(
                       text = '',
                      foreground = colorAmarrillo,
                       background = colorNaranja1,
                       padding = -3,
                       fontsize = 37
                       ),
              widget.Clock(
                       foreground = colorAzul,
                       background = colorAmarrillo,
                       format='%A, %B %d - %H:%M'
                       ),
             widget.TextBox(
                       text = '',
                     foreground = colorNaranja1,
                       background = colorAmarrillo,
                       padding = -3,
                       fontsize = 37
                       ),
                widget.QuickExit(
                    default_text=" Salir",
                      foreground = colorAzul,
                       background = colorNaranja1,
                    countdown_format="[ {} ]"
                ),
            ],
          20,
            background=colorAzul,
            opacity=1
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'gnome-screenshot'},
    {'wmclass': 'gnome-calculator'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"




@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])



# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
