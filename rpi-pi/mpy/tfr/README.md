# Transfer tfr (mpy)

Transfer of things like files to and from Raspberry Pi Pico .

How much of this should actually sit in electrical engineering? move some/all to applications, integration, .

## Goals & Objectives

Goals
* Primary goal to support /amn and other global warming and climate model projects
* Toward precursor to time series data etl/elt/tel , get level zero tsd server side for processing, 

Objectives
* use case; transfer time series data log file, file sharing, 
* use case; near real time transfer of time series data, event driven, stp, asnychronous, 
* use case; recover and replace sd card, remote site no network, manual or rotobits, drone or other unmanned vehicle and so on, possibly automated retreval and no human in the loop, also as maintenance use case, 
* ...

## Status

TODO
* <todo: consider, ftp, ftp server on Pico, ftp file client on laptop like FileZilla, other? >
* <todo: consider, secure copy protocol scp, wifi connection then from terminal scp pi@:/path/to/file /path/to/destination >
* <todo: consider, secure copy protocol scp, Putty, >
* <todo: consider, Samba, confirm that samaba is noted as a primary attack vector, so prefernce for NFS, WebDAV, SSHFS, >
* <todo: consider, rsync and script? >
* <todo: consider, connect via USB from laptop - or other compute device - to RPi Pico and transfer file, >

DONE
* <done: intent to commit>
* <done: consider, manually remove sd card from RPi Pico dev env SD Card Reader and put into laptop, manually copy file, files copied to /dat/dig/l-0/raw , >

## Libs

File sharing and network protocols - to evaluate
* SMB/CIFS, Server Message Block, Samba, org [WS](https://www.samba.org/), implementation of SMB and Active Directory AD protocols, ldap, kerberos, cluster filesystem access,  
* NFS, Network File System, linux use case
* WebDAV, Web Distributed Authoring and Versioning, 
* SSHFS, SSH File System, secure file sharing over SSH, linux use case

Tools - to evaluate
* Syncthing,
* OnionShare,
* Croc, 
* ...

## References

Terms
* File sharing, 