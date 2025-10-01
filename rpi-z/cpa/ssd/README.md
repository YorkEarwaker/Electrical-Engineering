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

## References

Terms
* SSD
* M.2
* PCIe
* NVMe
* Form factor
* ribbon cable, PCIe NVMe compatible, 
* Total Bytes Written, TBW life expectancy, writes before failure, e.g. 600 TB, 220 TB, 
* thermal pad, soft plyable material, not hard heatsink, circa 0.5mm 1.0mm 1.5mm depth, for example for form factor M.2 2280 nvme ssd

Datasheets
* Raspberry Pi Connector for PCIe, A 16-way PCIe FFC Connector Specification, [PDF](https://datasheets.raspberrypi.com/pcie/pcie-connector-standard.pdf), Raspberry Pi, 

News Papers - RPi
* Raspberry Pi M.2 HAT+ Ribbon Cable, [WS](https://forums.raspberrypi.com/viewtopic.php?t=372574&sid=8d5e9bd306227c84372bb0f70582d533)
* Raspberry Pi SSD Kit and Class A2 microSD cards review with Raspberry Pi 5, [WS](https://www.cnx-software.com/2024/11/19/raspberry-pi-ssd-kit-and-class-a2-microsd-cards-review-with-raspberry-pi-5/), 19 November 2024, Jean-Luc Aufranc, CNXSoft
* Testing Cytron MAKERDISK M.2 NVMe SSDs on Raspberry Pi 5 with GEEKWORM X1001 and Waveshare M.2 PCIe HAT+ [WS](https://www.cnx-software.com/2024/04/07/review-cytron-makerdisk-nvme-ssd-raspberry-pi-5-geekworm-x1001-waveshare-m2-pcie-hat/), 7 April 2024, Jean-Luc Aufranc, CNXSoft,

News Papers - M.2 naming, standards,
* Differences Between M2 Cards M2 Slots Keys Sizes and Types, and types. [WS](https://www.dell.com/support/kbdoc/en-us/000144170/how-to-distinguish-the-differences-between-m-2-cards), Summary: Learn to distinguish M.2 cards, including slots, keys, sizes, Understand M.2 slot functionality, M.2 and PCIe interfaces, and the M.2 platform's versatility.

News Papers - thermal pad
* Dell, M.2 2280 ssd form factor, other form factors, 

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

