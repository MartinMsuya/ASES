# ASE (Automatic Speed Enforcement) System

    This is a python script to detect speed of multiple vehicles on multi-lane highways.
    It uses Haar Cascade Classifier to detect vehicles in the every nth frame.
    It removes unnecessary portion from the image to speed up processing.
    Two reference lines have been set, one for vehicle entry and one for exit.
    When any vehicle in any lane crosses the entry point, the time is recorded, and the vehicle is tracked.
    Tracking is done using centroid tracking Techniques.
    Time is recorded when the vehicles crosses the exit line.
    Based on the time difference, the vehicles speed is estimated.
