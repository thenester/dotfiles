# A list of available commands that can be bound to keys can be found
# at https://docs.qtile.org/en/latest/manual/config/lazy.html

from libqtile.config import Key, Drag, Click
from libqtile.lazy import lazy

mod = "mod4"

def latest_group(qtile):
    qtile.current_screen.set_group(qtile.current_screen.previous_group)


keys = [
    # Widnows navigation
    Key([mod], "h",
        lazy.layout.left(),
        desc="Move focus to left"),

    Key([mod], "l",
        lazy.layout.right(),
        desc="Move focus to right"),

    Key([mod], "j",
        lazy.layout.down(),
        desc="Move focus down"),

    Key([mod], "k",
        lazy.layout.up(),
        desc="Move focus up"),

    Key([mod], "space",
        lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),

    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),

    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),

    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Move window up"),

    # Switch between last groups
    Key([mod], "Tab", lazy.function(latest_group)),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left"),

    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right"),

    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        desc="Grow window down"),

    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        desc="Grow window up"),

    Key([mod], "n",
        lazy.layout.normalize(),
        desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    Key([mod], "d",
        lazy.spawn("rofi -show drun"),
        desc="Launch rofi"),

    Key([mod], "Return",
        lazy.spawn("alacritty"),
        desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod, "shift"], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"),

    Key([mod], "w",
        lazy.window.kill(),
        desc="Kill focused window"),

    Key([mod], "m",
        lazy.layout.maximize(),
        desc="Maximize focused window"),

    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window"),

    Key([mod], "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window"),

    Key([mod], "b",
        lazy.hide_show_bar(),
        desc="Toggle bar"),

    Key([mod, "control"], "r",
        lazy.reload_config(),
        desc="Reload the config"),

    Key([mod, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"),

    Key([mod, "control"], "x",
        lazy.spawn("poweroff"),
        desc="Shutdown machine"),

    Key([mod, "control"], "z",
        lazy.spawn("reboot"),
        desc="Reboot machine"),

    Key([mod, "control"], "c",
        lazy.spawn("systemctl hibernate"),
        desc="Hibernate machine"),

    # Screenshot
    Key([mod], "p",
        lazy.spawn("maim ~/Images/Screenshots/$(date +%s).png", shell=True),
        desc="Make screenshot"),

    Key([mod, "shift"], "p",
        lazy.spawn("maim -s | xclip -selection clipboard -t image/png",
                   shell=True),
        desc="Make screenshot"),

    # Audio control
    Key([], "XF86AudioMute",
        lazy.spawn("amixer sset Master toggle"),
        desc="Volume mute"),

    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer sset Master 5%+"),
        desc="Volume increase"),

    Key([], "XF86AudioLowerVolume",
        lazy.spawn("amixer sset Master 5%-"),
        desc="Volume decrease"),

    # Brightness control
    Key([], "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl set 5%+"),
        desc="Brightness increase"),

    Key([], "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl set 5%-"),
        desc="Brightness decrease"),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
