# Solid State Drive SSD (cpa)

RPi Zero, as test bed. Likely have to be RPi V. 

As candidate for datalogger large data sets.

## Notes

Form factor for RPi 2230, 2280, depending on HAT

As a consequence of compatibility, host, operating system, - discovery for laptop ssd replacement/upgrade
* SSD M.2 2280 NVMe drive for Ubuntu 24.04, [WS](https://discourse.ubuntu.com/t/ssd-m-2-2280-nvme-drive-for-ubuntu-24-04/68002/1), Ubuntu Community
* replace hard drive on XPS 15 9560 with installed Windows 10 Pro, [WS](https://www.dell.com/community/en/conversations/xps/replace-hard-drive-on-xps-15-9560-with-installed-windows-10-pro/68d2de3f8ca2284a249873ae?page=1), Dell Community

## Status
TODO
* <todo: consider, SSD NVMe PCIe M.2 slot to microSD to microSD cable to RPi Zero >
* <todo: consider, find M.2 slot cable like microSD cable , flex connector, ribbon cable, important! >
* <todo: consider, moving this project to rpi V >

DONE
* <done: consider, intent to commit, >

## Hardware

### Laptop

Random set of candidates. The following are not recomendations. The following are information gathering on SSD NVMe PCIe M.2 topic of conern.

SSD, NVMe, PCIe 0.4 x 4, M.2 form factor 2280, 
* Crucial P310 1TB PCIe Gen4 NVMe 2280 M.2 SSD, [WS](https://uk.crucial.com/ssd/p310/CT1000P310SSD8), TBW 220 TB, general purpose, circa £65.00 2025/09/26
* Samsung - 990 PRO 1TB Internal SSD PCle Gen 4x4 NVMe, [WS](https://www.samsung.com/uk/memory-storage/nvme-ssd/990-pro-1tb-nvme-pcie-gen-4-mz-v9p1t0bw/), TBW 600 TB, better for AI development?, circa £80.00 2025/09/26
* WD_BLACK SN850X NVMe™ SSD - 1 TB, [WS](https://shop.sandisk.com/en-gb/products/ssd/internal-ssd/wd-black-sn850x-nvme-ssd?sku=WDS100T2X0E-00BCA0), TBW 600 TB, gaming, circa £80.00+vat 2025/09/26
* WD Blue SN5000 NVMe™ SSD - 1 TB, [WS](https://shop.sandisk.com/en-gb/products/ssd/internal-ssd/wd-blue-sn5000-nvme-ssd?sku=WDS100T4B0E-00CNZ0), TBW ?, better for AI development?, circa £60.00 2025/09/26

SSD Manufacturers - in no order of preference, many other available, 
* Crucial
* Samsung 
* Western Digital
* ...

### RPi 

TBD ...
* RPi compatible SSD's, hats, etc, 

### Thermal interface materials - merchants, products, - gap pad, thermal pad, heatsink, 
* Thermal pad for M.2 SSD 2280, [WS](https://www.microconnectors.com/m-2-ssd-thermal-pad/), Micro Connectors, one yay! but depth too great? 
* Hard Drive & Solid State Drive Coolers, com [WS](https://www.scan.co.uk/shop/computer-hardware/hard-drives-internal/hard-drive-and-solid-state-drive-coolers), Scan, heatsinks only?
* Thermal Pads, com [WS](https://www.scan.co.uk/shop/computer-hardware/cooling-air/thermal-pads), Scan, some yay! many appear to be from Watercooling site, 
* Thermal Pads, com [WS](https://uk.farnell.com/c/cooling-thermal-management/thermal-interface-materials/thermal-pads), Farnell, lots, yay!, 
* Thermal Pads, com [WS](https://www.overclockers.co.uk/air-cooling/cooler-accessories/thermal-pads), Overclockers UK, lots yay! many appear to be from Watercooler site, 
* Thermal Pads, com [WS](https://www.watercoolinguk.co.uk/cat/Thermal-Pads_642.html), Watercooling UK, lots yay!

## References

Terms
* SSD
* M.2
* PCIe
* NVMe
* Form factor
* ribbon cable, PCIe NVMe compatible, 
* Total Bytes Written, TBW life expectancy, writes before failure, e.g. 600 TB, 220 TB, 

Thermal interface material  - SSD's, and motherboard component things, heat transfer, 
* Gap pad, specific type of thermal pad, bespoke use, bespoke area coverage, where precision in gap filling and depth/thickness are critical concerns, 
* Heatsink, designed for desktop systems not laptop systems, 
* Thermal conductive paste, not good? gets - leaks - on to other components
* Thermal tape, 
* Thermal pad, silicone base compounds like ceramic filled silicone, strips of soft plyable material, not hard heatsink, circa 0.5mm 1.0mm 1.5mm depth, for example for form factor M.2 2280 nvme ssd
* ...

Heat, temperature,
* Thermal throtelling, heat outside operating limits causes degradation of function and may harm device
* Thermal throtelling, self, device self throtels to reduce heat and avoid harms to hardware through heat outside safe operating limits
* W/m-K units, heat transfer effectivness of thermal transfer substrate - paste, pad, tape, other, ? 

Datasheets
* Raspberry Pi Connector for PCIe, A 16-way PCIe FFC Connector Specification, [PDF](https://datasheets.raspberrypi.com/pcie/pcie-connector-standard.pdf), Raspberry Pi, 

News Papers - RPi
* Raspberry Pi M.2 HAT+ Ribbon Cable, [WS](https://forums.raspberrypi.com/viewtopic.php?t=372574&sid=8d5e9bd306227c84372bb0f70582d533)
* Raspberry Pi SSD Kit and Class A2 microSD cards review with Raspberry Pi 5, [WS](https://www.cnx-software.com/2024/11/19/raspberry-pi-ssd-kit-and-class-a2-microsd-cards-review-with-raspberry-pi-5/), 19 November 2024, Jean-Luc Aufranc, CNXSoft
* Testing Cytron MAKERDISK M.2 NVMe SSDs on Raspberry Pi 5 with GEEKWORM X1001 and Waveshare M.2 PCIe HAT+ [WS](https://www.cnx-software.com/2024/04/07/review-cytron-makerdisk-nvme-ssd-raspberry-pi-5-geekworm-x1001-waveshare-m2-pcie-hat/), 7 April 2024, Jean-Luc Aufranc, CNXSoft,

News Papers - M.2 naming, standards,
* Differences Between M2 Cards M2 Slots Keys Sizes and Types, and types. [WS](https://www.dell.com/support/kbdoc/en-us/000144170/how-to-distinguish-the-differences-between-m-2-cards), Summary: Learn to distinguish M.2 cards, including slots, keys, sizes, Understand M.2 slot functionality, M.2 and PCIe interfaces, and the M.2 platform's versatility.

News Papers - Dell, 
* Dell laptop, M.2 2280 ssd form factor, other form factors, hard to find merchants for generic thermal pads for M.2 2280 ssd, also can't find with ease on Dell website, 
* Will a SAMSUNG 980 PRO SSD with Heatsink 2TB PCIe Gen 4 NVMe M.2 fit in my XPS 15 9560 [WS](https://www.dell.com/community/en/conversations/xps/will-a-samsung-980-pro-ssd-with-heatsink-2tb-pcie-gen-4-nvme-m2-fit-in-my-xps-15-9560/647fa1c5f4ccf8a8de7135e2), 10 January 2023

News Papers - thermal interface materials
* How to choose a Gap Filler or thermal pad, [WS](https://www.compelma.com/en/how-to-choose-a-gap-filler/), Oct 23, 2023, Clement, Thermal Management

News Papers - microSD connector
* Adapter allows users to connect an M.2 NVMe SSD to a microSD Express card slot, [WS](https://www.cnx-software.com/2025/06/10/adapter-allows-users-to-connect-an-m-2-nvme-ssd-to-a-microsd-express-card-slot/), 10 June 2025, Jean-Luc Aufranc, CNXSoft, 

News Papers - flex connector - close but no cigar
* PCI-e 4x SSD as NGFF M.2 M Key SSD Adapter with Flex Cable, [WS](https://www.microsatacables.com/pci-e-4x-ssd-as-ngff-m-2-m-key-ssd-adapter-with-flex-cable-m2-1171-4x), Micro SATA Cables, 

News Papers - flex connector - contender , ?
* NGFF M.2 PCIe M-Key Extension Card with High Speed 20 CM Cable, [WS](https://www.microsatacables.com/ngff-m-2-pcie-m-key-extension-card-with-high-speed-20-cm-cable), Micro SATA Cables, 
* M.2 NGFF Key M to PCIe 3.0 4X Extension Cable (90°Right Angle PCI-E Slot), [WS](https://www.microsatacables.com/m-2-ngff-key-m-to-pcie-3-0-4x-extension-cable-90-right-angle-pci-e-slot), Micro SATA Cables, 

News Paper - SSD's , multiple manufacturers
* WD Black SN850X Gen4 NVMe and Linux, [WS](https://delightlylinux.wordpress.com/2024/05/09/wd-black-sn850x-gen4-nvme-and-linux/), Delightly Linux, Ubuntu 24.04, 
* NVMe SSD options, [WS](https://community.frame.work/t/nvme-ssd-options/864?u=codeasm), framework, 
* ...

News Papers - Enclosures for external SSD's, USB
* AMZPILOT Rugged NVMe USB 10Gbps External Enclosure and Linux, [WS](https://delightlylinux.wordpress.com/2023/11/10/amzpilot-rugged-nvme-usb-10gbps-external-enclosure-and-linux/), Delightly Linux, Ubuntu Cinnamon 22.04, 
* ...

News Papers - External SSD's, USB
* Crucial X10 2TB Portable SSD Review Compact and Neat, [WS](https://www.servethehome.com/crucial-x10-2tb-portable-ssd-review-compact-and-neat/), Serve The Home, 

News Papers - Windows 10 Pro move to external enclosure
* HELP Can I move SSD to external USB C (3.1) enclosure and boot windows 10 from it? [WS](https://egpu.io/forums/laptop-computing/help-can-i-move-ssd-to-external-usb-c-3-1-enclosure-and-boot-windows-10-from-it/)
* If I remove SSD from laptop and put it in external enclosure, can I boot same laptop from it and access files? [WS](https://superuser.com/questions/1804449/if-i-remove-ssd-from-laptop-and-put-it-in-external-enclosure-can-i-boot-same-la)
* Can I boot and run Windows 10 from SSD connected to USB port that was internally connected before? [WS](https://learn.microsoft.com/en-us/answers/questions/4017235/can-i-boot-and-run-windows-10-from-ssd-connected-t?forum=windows-all)
* Boot from an external ssd with widows 10 already installed [WS](https://learn.microsoft.com/en-au/answers/questions/5510218/boot-from-an-external-ssd-with-widows-10-already-i), 31 July 2025, Jeffery Gross
