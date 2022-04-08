# EV3Dev-USB-Connection
Control the EV3 Brick installed with ev3dev over an USB Client-Server-Connection.

# Windows Version
The code in this repository is inspired by the repository https://github.com/lichiukenneth/EV3Dev-Python-Socket-Connection, which provides an client server socket connection application, that can be controlled via Windows Forms. 

# Linux Version
However, this repository contains the code for establishing a client-server socket connection between a Linux computer and the EV3 (as client).

## Note 
The repository contains only the instructions for establishing a connection via USB. The connection setup via Wifi and Bluetooth can be read via the official website (https://www.ev3dev.org/docs/tutorials/ or https://github.com/lichiukenneth/EV3Dev-Python-Socket-Connection). 

# Prerequisites

* EV3 Brick
* USB cable (EV3 <-> PC connection)
* Ubuntu LTS 20.04 (only tested on this)
* flashed SD card with the ev3dev OS (https://www.ev3dev.org/downloads/)
* a sensor or motor for testing 

# Getting Started 

## Setup 

* Boot the EV3 computer with the ev3dev OS installed on an SD card. (tested with ev3dev-stretch-ev3-generic-2020-04-10).
Instructions: https://www.ev3dev.org/docs/getting-started/)
* connect the EV3 brick with your linux computer

## Verify the connection

* On the EV3 Brick the menu item Gadget can be activated via the menu: **Wireless and Networks** > **Tethering**. 
Afterwards the IP address of the EV3 can be queried in the same menu level in the menu item **Network Info**.  
* Open the terimal (Ctrl+Alt+T) and type in `lsusb`. Among other things, the following entry should appear in the response: `Lego Group Mindstorms EV3`
* On the Linux computer, you can find out the IP address of your Linux computer by typing `ifconfig`. (The IP address range should be similar to the one on the EV3). 

## Development 

For development, Visual Studio Code with the **ev3dev-browser** extension is recommended, which is used to easily deploy the created scripts to the EV3.
