# Qorvo Double Pulse Testing on Tektronix MSO5/6 Oscilloscope Example" Software

## Overview

This is a Python script to perform a double pulse test (DPT) of a wide-bandgap transistors, like [SiC](https://www.qorvo.com/feature/sic-power-products) or Gan, by using an installed AFG module on a Tektronix MSO5 or MSO6 oscilloscope.

This command-line script takes user inputs to generate DPT pulse sequence on your PC, to send it to an MSO5 or MSO6 scope, and to configure the scope for a DPT.

See our [application note](http:somewhere.tek.com) for the detail.

## Licenses

* The source Python script code, writtne by Qorvo, is under the [license](https://github.com/MasashiNogawa/DPT-on-MSO6/LICENSE), and the compiled binary is also under the same license.

* The compiled binary is generated by the [PyInstaller](https://pyinstaller.org/) and see the PyInstaller [license](https://github.com/pyinstaller/pyinstaller/blob/develop/COPYING.txt).
* The software, both Python script code and binary, is calling the [PyVISA](https://pyvisa.readthedocs.io/) library and see the PyVISA [license](https://github.com/pyvisa/pyvisa/blob/main/LICENSE).

## Dependencies

* The PyVISA module, in the script, searches IVI library backends.  See the [detail](https://pyvisa.readthedocs.io/en/latest/introduction/configuring.html#configuring-the-ivi-backend).
We tested the code and binary with the [NI-VISA](https://www.ni.com/en-us/support/downloads/drivers/download.ni-visa.html).
* The [libusb](https://github.com/libusb/libusb) library enables a USB connection between your PC and the MSO scope.  Please place a libusb file in your "PATH".


..end of README
