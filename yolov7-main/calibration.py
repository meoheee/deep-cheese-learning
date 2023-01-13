import pickle

def load_calibration(calib_file):
    with open(calib_file, 'rb') as file:
        # print('load calibration data')
        data= pickle.load(file)
        mtx = data['mtx']       # calibration matrix
        dist = data['dist']     # distortion coefficients

    return mtx, dist


mtx, dist = load_calibration('./XT2_calibration_pickle.p')

print(mtx)
print(dist)