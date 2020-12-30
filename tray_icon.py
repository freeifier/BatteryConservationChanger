import os
from gi.repository import Gtk, AppIndicator3 as appindicator

#import Haupt_Window

def main():
    indicator = appindicator.Indicator.new("customtray",os.path.abspath('/home/andreas/Dokumente/BatteryConservationChanger/BattChangerIcon.png'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(menu())
    Gtk.main()

def menu():
    menu = Gtk.Menu()

    #haupt = Gtk.MenuItem('Open')
    #haupt.connect('activate', open_haupt)
    #menu.append(haupt)

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
#def open_haupt(_):
#    Haupt_Window.Bat_Main()

if __name__ == "__main__":
    main()