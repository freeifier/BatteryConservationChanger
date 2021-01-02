#!/bin/bash

echo "Type in your local user account:"
read username
path=$(pwd)

echo "Copying programm files to: $path/BatteryConservationChanger"
cp -r $path"/BatteryConservationChanger" "/home/$username/BatteryConservationChanger"

sleep 1s
echo "Changing user rights"
chown -R $username:$username "/home/$username/BatteryConservationChanger"
chmod -R 700 "/home/$username/BatteryConservationChanger"

sleep 1s
echo "Adding crontab entry"
echo "@reboot root sleep 15s; chmod 646 /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode;" >> /etc/crontab

sleep 1s
echo "Creating auto-start menu entry"
echo "[Desktop Entry]
      Name=BatteryConservationChanger
      Exec=/bin/python3.8 /home/$username/BatteryConservationChanger/tray_icon.py /home/$username/BatteryConservationChanger/BattChangerIcon.png
      Type=Application
      Comment=BatteryConservationChanger" > /home/$username/.config/autostart/battery-conservation-changer.desktop

echo "fixing ownership of autostart entry"
chown -R $username:$username "/home/$username/.config/autostart/battery-conservation-changer.desktop"
