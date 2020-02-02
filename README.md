# RapidRelay

RapidRelay is an IOT analytics platform service that allows data aggregation from multiple sources and segregation into different containers based on the type of data and provides live visualization of the data stored.

RapidRelay collects data from multiple sources (Weather, Soil moisture and air quality monitoring systems) at 500ms using 60 bots and segregates data into different containers.

After every 5 minutes, the database is encoded and compressed with an ~83% compression ratio and is sent to the cloud infrastructure.
The data is decompressed, decoded and visualized in the cloud infrastructure.
