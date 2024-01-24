import os
# import re
import socket
import subprocess

from libqtile import bar, layout, widget, extension, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# PALERA DE COLORES 1
colorAzul = "#1D2B53"
colorNaranja1 = "#7E2553"
colorAmarrillo = "#FF004D"

background = '#1D2B53'
foreground1 = '#7E2553'
foreground2 = '#FF004D'
details = '#FAEF5D'

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Switch focus of monitors

    Key([mod], "period", lazy.next_screen(), desc='Move focus to next monitor'),
    Key([mod], "comma", lazy.prev_screen(), desc='Move focus to prev monitor'),

    # ScreenShot "Cambiar la ruta donde se guarda la captura de pantalla"
    Key([], "Print",
        lazy.spawn("scrot -s $HOME/Imàgenes/Captura_$(date '+%Y-%m-%d_%H-%M-%S').png")),

    # Dmenu control
    Key(
        [mod], "r",  # Dmenu Run Launcher
        lazy.run_extension(extension.DmenuRun(
            dmenu_prompt="Ejecutar",
            dmenu_font="Ubuntu-18",
            background=colorAzul,
            foreground=colorNaranja1,
            selected_background=colorNaranja1,
            selected_foregorund=colorAmarrillo,
        )),
        desc='Run Launcher'
    ),

]

groups = []
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", ]
group_labels = ["", "", "", "", "", "", "", "", "", ]
group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",
                 "monadtall"]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {
    "border_width": 2,
    "margin": 8,
    "border_focus": foreground1,
    "border_normal": background
}

layouts = [
    layout.Max(
        border_width=0,
        margin=0,
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    layout.RatioTile(**layout_theme),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

##### PROMPT #####

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
                    font="UbuntuBold Nerd Font",
                    fontsize=13,
                    margin_y=3,
                    margin_x=0,
                    padding_y=5,
                    padding_x=3,
                    borderwidth=3,
                    active=details,
                    inactive=foreground2,
                    rounded=False,
                    highlight_color=background,
                    highlight_method="line",
                    this_current_screen_border=details,
                    this_screen_border=foreground2,
                    other_current_screen_border=details,
                    other_screen_border=foreground1,
                    foreground=foreground1,
                    background=background
                ),
                widget.Prompt(
                    prompt=prompt,
                    font="Ubuntu Mono",
                    padding=14,
                    foreground=foreground1,
                    background=background
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=foreground1,
                    background=background
                ),
                widget.WindowName(
                    foreground=details,
                    background=background,
                    padding=5,
                    max_chars=40
                ),
                widget.Systray(
                    background=background,
                    padding=5
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=details,
                    background=background,
                ),
                widget.TextBox(
                    text='',
                    foreground=foreground1,
                    background=background,
                    padding=-3,
                    fontsize=37
                ),
                widget.TextBox(
                    text="🖴",
                    foreground=details,
                    background=foreground1,
                    padding=2,
                    fontsize=14
                ),
                widget.DF(
                    update_interval=60,
                    foreground=details,
                    background=foreground1,
                    partition='/',
                    format='{uf}{m} free',
                    fmt='Disk: {}',
                    visible_on_warn=False,
                ),
                widget.TextBox(
                    text='',
                    foreground=foreground2,
                    background=foreground1,
                    padding=-3,
                    fontsize=37
                ),
                widget.TextBox(
                    text="",
                    foreground=details,
                    background=foreground2,
                    padding=2,
                    fontsize=14
                ),
                widget.ThermalSensor(
                    foreground=details,
                    background=foreground2,
                    threshold=90,
                    padding=5
                ),
                widget.TextBox(
                    text='',
                    foreground=foreground1,
                    background=foreground2,
                    padding=-3,
                    fontsize=37
                ),
                widget.TextBox(
                    text="  ",
                    foreground=details,
                    background=foreground1,
                    padding=0,
                    fontsize=14
                ),
                widget.Memory(
                    foreground=details,
                    background=foreground1,
                    padding=5
                ),
                widget.TextBox(
                    text='',
                    foreground=foreground2,
                    background=foreground1,
                    padding=-3,
                    fontsize=37
                ),
                widget.TextBox(
                    text=" ☵ ",
                    foreground=details,
                    background=foreground2,
                    padding=0,
                    fontsize=14
                ),
                widget.CurrentLayout(
                    foreground=details,
                    background=foreground2,
                    padding=5
                ),
                widget.TextBox(
                    text='',
                    foreground=foreground1,
                    background=foreground2,
                    padding=-3,
                    fontsize=37
                ),
                widget.Clock(
                    foreground=details,
                    background=foreground1,
                    format="%A,%B-%d/%H:%M"
                ),
                widget.TextBox(
                    text='',
                    foreground=foreground2,
                    background=foreground1,
                    padding=-3,
                    fontsize=37
                ),
                widget.QuickExit(
                    default_text=" Salir",
                    foreground=details,
                    background=foreground2,
                    countdown_format="[ {} ]"
                ),
            ],
            20,
            opacity=0.95
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    font="UbuntuBold Nerd Font",
                    fontsize=13,
                    margin_y=3,
                    margin_x=0,
                    padding_y=5,
                    padding_x=3,
                    borderwidth=3,
                    active=details,
                    inactive=foreground2,
                    rounded=False,
                    highlight_color=background,
                    highlight_method="line",
                    this_current_screen_border=details,
                    this_screen_border=foreground2,
                    other_current_screen_border=details,
                    other_screen_border=foreground1,
                    foreground=foreground1,
                    background=background
                ),
                widget.Prompt(
                    prompt=prompt,
                    font="Ubuntu Mono",
                    padding=14,
                    foreground=foreground1,
                    background=background
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=foreground1,
                    background=background
                ),
                widget.WindowName(
                    foreground=details,
                    background=background,
                    padding=5,
                    max_chars=40
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    foreground=details,
                    background=background,
                ),
                widget.TextBox(
                    text='',
                    foreground=foreground1,
                    background=background,
                    padding=-3,
                    fontsize=37
                ),
                widget.TextBox(
                    text=" ☵ ",
                    foreground=details,
                    background=foreground1,
                    padding=0,
                    fontsize=14
                ),
                widget.CurrentLayout(
                    foreground=details,
                    background=foreground1,
                    padding=5
                ),
                widget.TextBox(
                    text='',
                    foreground=foreground2,
                    background=foreground1,
                    padding=-3,
                    fontsize=37
                ),
                widget.Clock(
                    foreground=details,
                    background=foreground2,
                    format="%A, %B %d - %H:%M"
                ),
                widget.TextBox(
                    text='',
                    foreground=foreground1,
                    background=foreground2,
                    padding=-3,
                    fontsize=37
                ),
                widget.QuickExit(
                    default_text=" Salir",
                    foreground=details,
                    background=foreground1,
                    countdown_format="[ {} ]"
                ),
            ],
            20,
            opacity=2
        ),
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


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
