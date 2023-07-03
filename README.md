# ASE (Automatic Speed Enforcement) System

    This is a python script to detect speed of multiple vehicles on multi-lane highways.
    It uses Haar Cascade Classifier to detect vehicles in the every nth frame.
    It removes unnecessary portion from the image to speed up processing.
    Two reference lines have been set, one for vehicle entry and one for exit.
    When any vehicle in any lane crosses the entry point, the time is recorded, and the vehicle is tracked.
    Tracking is done using centroid tracking Techniques.
    Time is recorded when the vehicles crosses the exit line.
    Based on the time difference, the vehicles speed is estimated.

Speed violations have been classified among the major causes of road accidents in Tanzania. 
Speed control on roadways is critical in reducing the number of road accidents reported on a 
day-to-day basis. It is important to specify the speed limit on different sections of the road in 
order to alert drivers of speed regulations at any time.
The Automatic Speed Enforcement system is a comprehensive solution designed to enhance 
road safety by effectively monitoring and enforcing speed limits. This project encompasses 
the development of hardware devices, software modules, and a robust database to capture 
vehicle images, measure speed, recognize number plates, store data, generate tickets, and 
provide data analysis. 
The system utilizes advanced technologies such as OpenCV for speed measurement and 
Tesseract OCR for number plate recognition. It integrates with a MySQL database for 
efficient data management and incorporates an API for seamless communication with external 
systems. The system's flowchart, hardware requirements, and implementation details are 
presented. The system demonstrates the successful implementation of key functionalities, 
including speed measurement, number plate recognition, data storage, and ticket generation.
Recommendations for future work are also provided, suggesting areas such as mobile 
application development, advanced image processing techniques, and integration with smart 
city initiatives. The Automatic Speed Enforcement system serves as a valuable tool for traffic 
authorities in promoting compliance with speed limits, enhancing road safety, and facilitating 
data-driven decision-making for effective traffic management.

