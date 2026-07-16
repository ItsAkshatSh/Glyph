<h1 align="center">
  <br>
  <img src="https://github.com/ItsAkshatSh/Glyph/blob/main/assets/Glyph.gif?raw=true" width=90%>
  <br>
  <br>
  Glyph
  <br>
</h1>
<div align="center">

![CircuitPython](https://img.shields.io/badge/Made%20with-CircuitPython-2ec4b6)
![EasyEDA](https://img.shields.io/badge/Made%20with-EasyEDA-07162A)

Glyph is a NFC PCB card but with an e-ink screen and 3 Cherry MX switches, it includes a Seeed Studio XIAO nRF52840 which runs on a 200 mAH battery! The epaper is used for cycling thorugh different screens such as an about me, interests, Projects and much more!
</div>

### Why?
This is a device that will help me standout at events such as networking, college fairs, and job fairs. Also the idea of having an e-ink display and three cherry MX switches on a NFC card sounds super cool too.

## Parts!
- Uses a ***Seeed Studio XIAO nRF52840***, using it's charging module!
- ***Seeed Studio epaper breakout board***, breakout board with a 24 pin connector for the epaper display
- ***Seeed Studio 2.13" epaper display***, neat little epaper display
- Three ***Cherry MX switches!**

## Hardware

want to work on this? head to /hardware

- Refer to the BOM [here](https://github.com/ItsAkshatSh/Glyph/blob/main/BOM.csv)
- Download the PCB Project file [here](https://github.com/ItsAkshatSh/Glyph/tree/main/Hardware/Project%20File)
- Order the PCB and parts using the Gerber Files, BOM and Pick&Place (Refer [here](https://github.com/ItsAkshatSh/Glyph/tree/main/Hardware))
- Solder all the components according to the schematic!
- Download CircuitPython for Seeed Studio XIAO nRF52840
- Hold the BOOT button and plug in the MCU
- It should appear as a CIRCUITPY drive
- Download the firmware
- Copy all the file to the CIRCUITPY drive
- and, you're done!

<div align='center'>

## Schematic
<div align="Center">
<img width="60%" height="60%" alt="image" src="https://github.com/ItsAkshatSh/Glyph/blob/main/assets/SCHEMATIC.png?raw=true" />
</div>

## PCB
<div align="Center">
<img width="60%" height="60%" alt="image" src="https://github.com/ItsAkshatSh/Glyph/blob/main/assets/PCB.png?raw=true" />
</div>
<div align="Center">
<img width="60%" height="60%" alt="image" src="https://github.com/ItsAkshatSh/Glyph/blob/main/assets/PCB3D.png?raw=true" />
</div>

View the 3D PCB on OnShape [here!](https://cad.onshape.com/documents/2ada56df9e2c89778f5abab2/w/117df8fbf0d848a4ffec5e1d/e/edb56eeac649d6d1847bad36?renderMode=0&uiState=6a58a5508228b89c97037c87)

</div>

<div align='center'>

## Firmware

</div>

```
└── /
    ├── buttons/
    │   ├── buttons.py
    ├── display/
    │   ├── display_manager.py
    ├── models/
    │   ├── project.py
    ├── ui/
    │   ├── pages.py
    │   ├── renderer.py
    │   ├── ui.py
    ├── nfc/
    │   ├── ndef.py
    │   ├── nfc_manager.py
    │   ├── st25dv.py
    ├── battery.py
    ├── code.py
    ├── config.py

```



<div align='center'>

## BOM
|   S. No | Part                       | Link                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Qty.     | Price   |
|--------:|:---------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:--------|
|       1 | E-Ink Display              | [Link](https://www.seeedstudio.com/2-13-Monochrome-ePaper-Display-with-122x250-Pixels-p-5778.html) | 1 Piece | $6.50 |
|       2 | Connecter - 24 pin         | [Link](https://www.seeedstudio.com/ePaper-Breakout-Board-p-5804.html) | 1 Pieces | $3.99 |
|       3 | NFC Chip                   | [Link](https://www.lcsc.com/product-detail/C2762854.html) | 1 Piece | $1.24 |
|       4 | 200 mAH 3.7V Lipo Battery  | [Link](https://www.amazon.ae/502030-Liter-energy-battery-Rechargeable/dp/B01IOA1HV8?crid=QKBDYL5NN70X&dib=eyJ2IjoiMSJ9.V6zbbuzD2HLvZbELSNXMKJF5TXEwtLyvTLFV990jh1GvNcslPJHm4cnwDe236voo4yQMscBQ83xZ7W_UId2qMx3WxqFC2ZqB_EqYj5_LVTpyJaBTNzKSGd13bk0PulJ31focaC9AB84E9HCuC2UiuZ3m6gvc0PNfq0_c-dAKzLqqVhhP9JbsDppYZfU0Oo0T8WkhvKS_-RJ7dJKS2nGqk0TS-FoMNIST1VpFcJQVhUzYcQONTWFBDjshJStv0JYhHzCVh1XvPuU9B4kcdAJla2dvTEVAIxk5zXOj9Sj-Grw.FR1m4rTzHwdK2MC0OBGGnZRbMBnQHCrbr2tSV9YxVaI&dib_tag=se&keywords=100-200+mAH+lipo+battery&qid=1783616967&sprefix=100-200+mah+lipo+battery,aps,229&sr=8-1&th=1 ) | 1 Piece | $18 |
|       5 | Seeed Studio Xiao nRF52840 | [Link](https://www.seeedstudio.com/Seeed-XIAO-BLE-nRF52840-p-5201.html) | 1 Piece | $9.90 |
|       6 | PCB(from JLCPCB)           | | 5 Pieces | $58.41 |
| | Total                        | |       | $98.14  |

</div>

<div align='center'>

## Zine


<img src="https://github.com/ItsAkshatSh/Glyph/blob/main/assets/Glyph.png?raw=true" width=50% height=50%>


### Thank you HackClub!
