import numpy as np



class Slopes:
    recent_timestamp = None
    cal_center = -1.0,-1.0
    input_center = -1.0,-1.0
    calibration_Xvals = np.zeros(5)
    calibration_Yvals = np.zeros(5)
    input_Xvals = np.zeros(5)
    input_Yvals = np.zeros(5)


    def update_spots(self, timestamp, X_values, Y_values):
        self.recent_timestamp = timestamp
        self.calibration_Xvals = X_values[0:4]
        self.calibration_Yvals = Y_values[0:4]
        self.input_Xvals = X_values[5:9]
        self.input_Yvals = Y_values[5:9]