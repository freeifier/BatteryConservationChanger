#!/bin/bash

echo "Type in your local user"
read username
path=$(pwd)

cp -r $path"/BatteryConservationChanger" "/home/$username/BatteryConservationChanger"
echo "@reboot root sleep 15s; chmod 646 /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode;" >> /etc/crontab
echo "@reboot $username /bin/python3.8 /home/"$username"/BatteryConservationChanger/tray_icon.py" >> /etc/crontab
