#!/bin/bash
#   ___ _____ ___ _     _____   ____  _             _    
#  / _ \_   _|_ _| |   | ____| / ___|| |_ __ _ _ __| |_  
# | | | || |  | || |   |  _|   \___ \| __/ _` | '__| __| 
# | |_| || |  | || |___| |___   ___) | || (_| | |  | |_  
#  \__\_\|_| |___|_____|_____| |____/ \__\__,_|_|   \__| 
#                                                        
# by cerberus 
# ----------------------------------------------------- 

# -----------------------------------------------------
# Autostart Services
# -----------------------------------------------------



# Load compositor
picom &

# Load polkit agent
gnome-keyring-daemon --start --components=pkcs11,secrets,ssh &
/usr/lib/mate-polkit/polkit-mate-authentication-agent-1 &

# Set Wallpaper after restart
nitrogen --restore &

qtile cmd-obj -o cmd -f restart

# Load Clipboardmanager
copyq &

# Load power manager
 xfce4-power-manager &


# -----------------------------------------------------
# Autostart Apps
# -----------------------------------------------------
# Configure Screen Layout
$HOME/.screenlayout/screen1.sh
# Start flameshot
flameshot &

# Load discord
firefox &
nm-applet &
$HOME/.trilium/trilium &
sleep 10
# discord &


