This is the DesignatedFreeCadDevice, a moduar cyberdeck primarily designed to run FreeCad.

![DSCF1779](https://github.com/user-attachments/assets/cbbf986b-326c-486f-9e77-3bc8181b262e)
**what does it do?**
It runs freecad of course :) i developed it mostly to be able to open and modify CAD files while in the workshop, but i also use it to browse the web and genral computing. it has a keyboard hidden under the sliden screen, as i rarley use a keyboard, but i did want to have a full depth mechanical keyboard whenever i actually use one. The machine is modular so that one can build modules that fits your personal needs.I hope people feel inspired to make their own modules.
![DSCF1786](https://github.com/user-attachments/assets/df5e4cd6-41c9-4f8a-bc78-de39ea63718a)

**How is the modules powered?**
Cables run on the backside, transfering USB betweeen the modules.
![DSCF1748](https://github.com/user-attachments/assets/afb27bba-86a3-4399-81f9-8e598e65027f)
**overview of the device**
The cyberdeck consist of a central core where one can attach both modules that works as input devices and modules that deliver power to the device.
<img width="1832" height="1294" alt="ISO view" src="https://github.com/user-attachments/assets/12b63319-b272-4477-903d-1e9d93bc4031" />
The modules are connected with power and signals to the bottom rails.
<img width="1829" height="1293" alt="Back" src="https://github.com/user-attachments/assets/be32baf5-b2c4-4133-a6e2-7bccc4060113" />
On the left side you can find ports to connect to external devices, and a handle for scrolling both verticaly, and horizontally.
<img width="2291" height="1023" alt="Left side v" src="https://github.com/user-attachments/assets/64f4529a-c84d-498f-8eb2-19e468357d24" />
On the rigth side we find a the trackball module, and the power module. the powermodule accept NP-F batteries, and send the 7.2 volts to the chassis, where it is converted to 5.1 volts for the rasberry pi. 
<img width="2426" height="1209" alt="Rigth side view" src="https://github.com/user-attachments/assets/c1157ec0-485c-40a9-a0c1-c5f0736cd357" />
On the forward facing modules you find mounting points for a shoulder strap. On the rear of the central unit you find the lever for releasing the sliding screen,
<img width="1831" height="1295" alt="Front back" src="https://github.com/user-attachments/assets/2266037e-72e4-4f89-a2b0-ca8d05e22ae0" />


**What is the current status on this project?**
Screen is working, keyboad types and trackball rolls. what i have not done yet is to wire up the scrolling handle and connection module on the left. The trackball electronics is currently 
harvested from a logiteck trackball marble, meaning you need to source one to build one of these, wich is not optimal. so i want to build my own trackball electronics in the future.

**Build instructions**
These are the builing instructions for the current version of this cyberdeck:
First, the chassis has to be assembled, and we start with the upper chasssis, where the linear bearings are inserted in its holders, that are then inserted in the upper chassis sections.
<img width="2554" height="1362" alt="Upper frame 1" src="https://github.com/user-attachments/assets/490e57c0-1b0a-4ef2-aa2d-dbe46fbe2d24" />
The screen release switch is mounted, the pin is made by cutting a screw or threaded rod.
<img width="2554" height="1362" alt="upperframe 7" src="https://github.com/user-attachments/assets/8e3df6ab-9178-462e-ab04-d1d602c753be" />
A spring must be sourced from a ballpen and inserted into the screen release switch

Completed upper frame
<img width="2554" height="1362" alt="upper frame 8" src="https://github.com/user-attachments/assets/7cc1866b-b1f1-4ee4-a216-bb92f9728981" />
Bottom chasssis halves must be welded togheter with a soldering iron. You can add material while soldering by melting a piece of filaent into the crack between the parts to be soldered.
ventilation frames and mounting points for rails is inserted into the lowered chassis.
<img width="2554" height="1362" alt="lower chassis 2" src="https://github.com/user-attachments/assets/bebf0a33-de76-45ac-8325-3aa8efbf4c23" />
The lower rails is carriying power and usb signals must be wired up. The Three EXT plugs should have one USB cablewired to each one, so they can be plugged in to the rasberry pi.the power plug should have the DC power + and - connected to one pair of wires, the othe pair of wire should then be connected as a power on button on the power module, going to the rasberry pi.After verifying correct soldering, hot glue can be applied onto the solder points.
<img width="2554" height="1362" alt="Powered rail internal view" src="https://github.com/user-attachments/assets/b483a1e5-1746-41c0-b977-000d067de51c" />
The rails can then be assembled to bottom chassis.
<img width="2554" height="1362" alt="Bottom rails mounted" src="https://github.com/user-attachments/assets/7234a84f-699b-458a-9666-f3833a506232" />
Feed the wires through the cutouts in the chassis:
<img width="2554" height="1362" alt="Chassis wire feed through" src="https://github.com/user-attachments/assets/1a64cf63-36d6-4a94-8956-8699a7fbc38c" />
Tthen upper and lower chassis are stacked and screwed down.
<img width="2554" height="1362" alt="chassis stacked" src="https://github.com/user-attachments/assets/f919d9b0-2d74-4ca6-85a8-2396bc337ddc" />
Side rails are assembled with the large m6 screws.
<img width="2554" height="1362" alt="Chassis assembly 2" src="https://github.com/user-attachments/assets/013f858b-d8a0-410f-827d-ee9627e30c7b" />
Now the rasberry pi and keyboard can be mounted. i used the screws that came with the keyboard.Then connect the USB cables from both rails and keyboard to the rasberry pi.
<img width="2554" height="1362" alt="Keyboard mounted" src="https://github.com/user-attachments/assets/1f74fe34-83da-4e1d-9185-8c82624f6144" />
The cables can then be inserted through the cable chain, before snapping it in place on the chassis mounting lugs. There should be one HDMI ribbon cable, and one USB cable for power to the screen. Plug both cables in to the rasberry pi side.
<img width="2554" height="1362" alt="Cable chain" src="https://github.com/user-attachments/assets/76e06bad-646e-4716-ae50-76d9534a559c" />

**Screen assembly**
The base of the screen must be welded together with soldering iron. Then the rod clamps are mounted using screws and nut on the backside, but not tigtened down yet.
<img width="2554" height="1362" alt="Screen frame" src="https://github.com/user-attachments/assets/9b4e4815-6c97-4e8f-a94a-aa96420fb1af" />
The assembled screen frame can then be placed over chassis. Then guiderods are installed, locking the base down.
<img width="2554" height="1362" alt="Rod insertion" src="https://github.com/user-attachments/assets/9211fc4b-1291-4da8-8395-5cde0921c649" />
The cable chain can then be screwed down to the screen frame.
<img width="2554" height="1362" alt="Aseembled screen frame" src="https://github.com/user-attachments/assets/770290a4-d234-4f8a-9a68-f7d5eb179029" />
Now the completed base with sliding mechanism lets us continue assembly to the screen frame. The assembly begins with screwing together the two halves.
