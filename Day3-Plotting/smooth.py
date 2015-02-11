#####################
# A gift from Marty
#####################

def smooth(x,window_len=10,window='hanning'):
    if x.ndim != 1:
        raise ValueError, "smooth only accepts 1 dimension arrays."
    if x.size < window_len:
        raise ValueError, "Input vector needs to be bigger than window size."
    if window_len<3:
        return x
    if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise ValueError, "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'"
    x0 = x[window_len-1:0:-1]
    xn = x[-1:-window_len:-1]
    s  = numpy.r_[x0,x,xn]
    if window == 'flat': #moving average
        w = numpy.ones(window_len,'d')
    else:
        w = eval('numpy.'+window+'(window_len)')
    y   = numpy.convolve(w/w.sum(),s,mode='valid')
    lx0 = len(x0)
    if lx0 % 2 != 0:
        lx0=lx0+1
    ly = len(y)
    y  = y[lx0/2:ly-len(xn)/2]
    return y

# Alternate smoothing function
#def smooth(y, box_pts):
#    box      = np.ones(box_pts)/box_pts
#    y_smooth = np.convolve(y, box, mode='same')
#    return y_smooth
