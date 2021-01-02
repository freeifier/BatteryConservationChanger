
import os
from gi.repository import Gtk, AppIndicator3 as appindicator
import sys

def main():
    print("Path give is",os.path.abspath(sys.argv[1]))
    indicator = appindicator.Indicator.new("customtray",os.path.abspath(sys.argv[1]), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(menu())
    Gtk.main()

def menu():
    menu = Gtk.Menu()

    command_sw=Gtk.CheckMenuItem("Battery conservation mode")
    command_sw.set_active(get_current_state())
    command_sw.connect("activate",switch_state)
    menu.append(command_sw)

    exittray = Gtk.MenuItem('Exit')
    exittray.connect('activate', quit)
    menu.append(exittray)

    menu.show_all()
    return menu


def get_current_state()->str:
    state=open("/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode","r")
    state=state.read()
    if "1" in state:
        return True
    else:
        return False

def quit(_):
    Gtk.main_quit()

def switch_state(_):
    f=open("/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode","w")
    if get_current_state():
        f.write("0")
        f.close()
    else:
        f.write("1")
        f.close()

if __name__ == "__main__":
    main()

