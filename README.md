# RapidRelay

RapidRelay is an IOT analytics platform service that allows data aggregation from multiple sources and segregation into different containers based on the type of data and provides live visualization of the data stored.

RapidRelay collects data from multiple sources (Weather, Soil moisture and air quality monitoring systems) at 500ms using 60 bots and segregates data into different containers.

After every 5 minutes, the database is encoded and compressed with an ~83% compression ratio and is sent to the cloud infrastructure.
The data is decompressed, decoded and visualized in the cloud infrastructure.

### Demo
TODO

### Installation steps:

 1. Clone this repo
 `https://github.com/harshpatel23/RapidRelay.git`
 
 2. Change directory
 `cd RapidRelay/`

 3. Create a virtual environment with Python 3.6: 
 `python3 -m virtualenv venv`
 
 4. Activate the environment:
 	- **Linux:** `source venv/bin/activate`
	- **Windows:** `.\venv\Scripts\activate.bat`
		 
 5. Install the required packages from `requirements.txt` inside this virtual environment:
	 `pip install -r requirements.txt`

 6. Install mosquitto broker (refer the following link)
http://www.steves-internet-guide.com/install-mosquitto-linux/

 7. Second install paho-mqtt (refer the following link)
http://www.steves-internet-guide.com/into-mqtt-python-client/
 
    
### Usage Instructions:
 1. Activate the environment:
 	- **Linux:** `source venv/bin/activate`
	- **Windows:** `.\venv\Scripts\activate.bat`
	
    TODO

### Future Work

1. Graphical representation and analysis of the data received on cloud.
2. Adding load balancer to enhance the scalability of the product by handling huge load of requests and data.

### Contributers

1. Murtaza Patrawala -- [@murtaza98](https://github.com/murtaza98)
2. Harsh Patel -- [@harshpatel23](https://github.com/harshpatel23)
3. Tanay Raul -- [@padfoot18](https://github.com/padfoot18)
4. Ojas Kapre -- [@ojasskapre](http://github.com/ojasskapre)

### Recognition
    - Part of KJSCE HACKIT 2.0 (Feb 2020).

### Development

Want to contribute? Great!
Please read [CONTRIBUTING.md](https://github.com/murtaza98/VirtualProctor/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

### Todos

 - 

### License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/murtaza98/VirtualProctor/LICENSE) file for details

### Note 
This project was done under 24 hours with minimal pre-preparation.

