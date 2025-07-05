# Integration grt (jva)

Integration with periferal and controller end points. For use by extract transform and load of time series data for use by, amoungst other things, numerical climate/weather prediction systems. 


## Goals & Objectives
Ponder more on exact function of this capability

* level zero raw data ? time series data logs? file transfer? likely yes. 
* Should this be only a server side interaction layer or integration layer used by etl, likely just integration layer, interaction /act or integration /grt ?
* Keep focus on this project as only integration with periferals and controllers IOT IIOT .
* Keep focus on microcontroller integration in the first instance
* Will project actually requrie any electrical enginnering? 

## Status

TODO
* <todo: consider, extract, pull get/retrieve sime series data from RPi Pico, likely Java over ftp?http?, >
* <todo: consider, extract, push recieve time series data from RPi Pico, likely Java listener >
* <todo: consider, enterprise integration patterns, canonical data model cdm, and so on, >
* <todo: consider, breaking URI schemes into seperate project, this project to use URIS project to access resources to extract, or is that what this project is focused on>
* <todo: consider, COTS or open source equivalent capability don't reinvent the wheel, >
* <todo: consider, use case for feed into kafka ? part of etl level one data? not this project? >
* <todo: consider, use case for feed into RDF ? part of etl level one data? not this project? >
* <todo: consider, deployment to local host laptop first instance PoC, >
* <todo: consider, deployment to local host single board computer second isntance, MVP, Raspberry Pi Five V >
* <todo: consider, would python be a better choice if SBC Raspberry Pi V will be a primary depoloyment environment? >


DONE
* <done: intent to commit>

## Reference

Terms
* Extract transform & load, not likely this. to be used by this in layered architecture asysncronous call stack.
* Interaction, not likely this. to be used by this in layered architecture asysncronous call stack.
* Integration, think this is the focus!
* URI schemes,
* URIS, FTP [WP](https://en.wikipedia.org/wiki/File_Transfer_Protocol)


