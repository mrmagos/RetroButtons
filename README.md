# RetroButtons
Scripts and systemd unit files to add physical Power and Reset buttons to your Raspberry Pi mini retro console. Intended for use with RetroPie, but probably works with RecalBox as well.

Power button waits for momentary switch press on pins 5 and 6, then gracefully shuts down. The Raspberry Pi listens to these pins when shutdown, so another press will boot it back up.

Reset button waits for momentary switch press on pins 37 and 39, then exits emulator, returning to the EmulationStation menu.

Option fan control pin to turn a fan on/off on startup/shutdown.

# Installation
Clone the repository to <code>/home/pi</code>:
<pre>
<code>
$ git clone https://github.com/mrmagos/RetroButtons.git
</code>
</pre>
Copy systemd unit files, resgister them, start them and enable them at startup:
<pre>
<code>
$ sudo cp RetroButtons/system/* /etc/systemd/system/
$ sudo systemctl daemon-reload
$ sudo systemctl start powerbtn resetbtn
$ sudo systemctl enable powerbtn resetbtn
</code>
</pre>
