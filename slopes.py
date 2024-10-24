import numpy as np



class Slopes:
    recent_timestamp = None
    cal_center = -1.0,-1.0
    input_center = -1.0,-1.0
    calibration_Xvals = np.zeros(5)
    calibration_Yvals = np.zeros(5)
    input_Xvals = np.zeros(5)
    input_Yvals = np.zeros(5)