# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Group, Key, Match, Screen
from libqtile.lazy import lazy

import colors as c

# God save my soul from these nasty imports, but I have to...
from mapping import *
from hooks import *


groups = [Group(i) for i in "1234567"]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus=c.COLOR_BORDER_PRIMARY,
        border_normal=c.COLOR_BORDER_SECONDARY,
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=3, margin=5
    ),
    layout.Max( border_focus=c.COLOR_BORDER_PRIMARY,
        border_normal=c.COLOR_BORDER_SECONDARY,
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=3, margin=5
    ),
    layout.MonadTall(
        border_focus=c.COLOR_BORDER_PRIMARY,
        border_normal=c.COLOR_BORDER_SECONDARY,
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=3, margin=0
    ),
    layout.MonadWide(
        border_focus=c.COLOR_BORDER_PRIMARY,
        border_normal=c.COLOR_BORDER_SECONDARY,
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=3, margin=0
    ),
    layout.Tile(
        border_focus=c.COLOR_BORDER_PRIMARY,
        border_normal=c.COLOR_BORDER_SECONDARY,
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=3, margin=5
    )
    # layout.RatioTile(),
    # layout.Stack(num_stacks=3),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

bar_size = 30
bar_icon_size = 20

widget_defaults = {
    "font": "Maple Mono",
    "fontsize": 25,
    "padding": 4
}

extension_defaults = widget_defaults.copy()

separator_defaults = {
    "font": widget_defaults["font"],
    "fontsize": widget_defaults["fontsize"],
    "padding": 0
}

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(
                    background=c.COLOR_BORDER_PRIMARY,
                    foreground=c.COLOR_BAR_BACKGROUND),
                widget.TextBox(
                    "",
                    **separator_defaults,
                    background=c.COLOR_BAR_BACKGROUND,
                    foreground=c.COLOR_BORDER_PRIMARY),
                widget.GroupBox(
                    active=c.COLOR_BORDER_PRIMARY,
                    inactive=c.COLOR_BORDER_PRIMARY,
                    this_current_screen_border=c.COLOR_BAR_BACKGROUND,
                    block_highlight_text_color=c.COLOR_BORDER_PRIMARY,
                    highlight_color=c.COLOR_BAR_BACKGROUND,
                    foreground=c.COLOR_BAR_BACKGROUND,
                    highlight_method="line",
                    disable_drag=True),
                widget.WindowName(
                    foreground=c.COLOR_BORDER_PRIMARY),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(icon_size=bar_icon_size),
                widget.TextBox(
                    " ",
                    **separator_defaults,
                    background=c.COLOR_BAR_BACKGROUND,
                    foreground=c.COLOR_BORDER_PRIMARY),
                widget.Backlight(
                    background=c.COLOR_BORDER_PRIMARY,
                    foreground=c.COLOR_BAR_BACKGROUND,
                    format="󱄄 {percent:2.0%}",
                    backlight_name="nvidia_wmi_ec_backlight"),
                widget.TextBox(
                    "",
                    **separator_defaults,
                    background=c.COLOR_BORDER_PRIMARY,
                    foreground=c.COLOR_BAR_BACKGROUND),
                widget.TextBox(
                    "",
                    **separator_defaults,
                    background=c.COLOR_BAR_BACKGROUND,
                    foreground=c.COLOR_BORDER_PRIMARY),
                widget.TextBox(
                    " ",
                    background=c.COLOR_BORDER_PRIMARY,
                    foreground=c.COLOR_BAR_BACKGROUND),
                widget.Volume(
                    background=c.COLOR_BORDER_PRIMARY,
                    foreground=c.COLOR_BAR_BACKGROUND),
                widget.TextBox(
                    "",
                    **separator_defaults,
                    background=c.COLOR_BORDER_PRIMARY,
                    foreground=c.COLOR_BAR_BACKGROUND),
                widget.TextBox(
                    "",
                    **separator_defaults,
                    background=c.COLOR_BAR_BACKGROUND,
                    foreground=c.COLOR_BORDER_PRIMARY),
                widget.Battery(
                    background=c.COLOR_BORDER_PRIMARY,
                    foreground=c.COLOR_BAR_BACKGROUND,
                    format="{char} {percent:2.0%}",
                    full_char="󰁹",
                    charge_char="󰂄",
                    empty_char="󱉞",
                    show_short_text=False),
                widget.TextBox(
                    "",
                    **separator_defaults,
                    background=c.COLOR_BORDER_PRIMARY,
                    foreground=c.COLOR_BAR_BACKGROUND),
                widget.TextBox(
                    "",
                    **separator_defaults,
                    background=c.COLOR_BAR_BACKGROUND,
                    foreground=c.COLOR_BORDER_PRIMARY),
                widget.Clock(
                    background=c.COLOR_BORDER_PRIMARY,
                    foreground=c.COLOR_BAR_BACKGROUND,
                    mouse_callbacks={
                        "Button1": lazy.spawn("gsimplecal"),
                    },
                    format=" %I:%M %p"),
            ],
            size=bar_size,
            background=c.COLOR_BAR_BACKGROUND,
            margin=[4, 4, 4, 4],
            border_width=[4, 4, 4, 4],
            border_color=[c.COLOR_BAR_BACKGROUND] * 4
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=c.COLOR_BORDER_PRIMARY,
    border_normal=c.COLOR_BORDER_SECONDARY,
    border_width=6,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(title="branchdialog"),  # gitk
        Match(wm_class="ssh-askpass"),
        Match(wm_class="pinentry-gtk"),
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

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
