from subprocess import getstatusoutput, Popen
from typing import Optional

from libqtile import hook
from libqtile import qtile
from libqtile.backend.base import Window


@hook.subscribe.setgroup
def setgroup():
    for group in qtile.groups:
        if group == qtile.current_group:
            group.label = "󱨇" if group.windows else "󱓻"
            continue

        group.label = "󱨈" if group.windows else "󱓼"


@hook.subscribe.startup_once
def autostart():
    def setup_monitor_cmd() -> Optional[str]:
        cmd = None
        err_code, out = getstatusoutput("xrandr | grep ' connected'")
        if err_code:
            return None

        if len(out.splitlines()) > 1:
            cmd = ("xrandr "
                   "--output eDP-1 --off "
                   "--output HDMI-1-0 --mode 1920x1080 --pos 0x0 --rotate normal")

        return cmd

    cmd_list = [
        "nitrogen --restore",
        "setxkbmap -layout us,ru,ua -option grp:alt_shift_toggle",
        "gxkb",
        "telegram-desktop",
        "firefox"
    ]

    monitor_cmd = setup_monitor_cmd()
    if monitor_cmd:
        cmd_list.insert(0, monitor_cmd)

    for cmd in cmd_list:
        Popen(cmd.split())


@hook.subscribe.client_new
def spawn_client(window: Window):
    to_group_name = {
        "telegram-desktop": "4",
        "zen-bin": "5",
        "gimp": "6",
    }

    window_class = window.get_wm_class()[0]
    group_name = to_group_name.get(window_class)
    if not group_name:
        return

    window.togroup(group_name)
