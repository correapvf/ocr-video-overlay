# folder with img files (frames) to train the model
# choose frames so you have at least 10 occurrences for each digit
train_folder = r'C:\Users\paulo\Documents\overlay'
ext_train = '*.jpg'

# folder with video files to recognize
ocr_folder = r'C:\Users\paulo\Documents'
ext_train = '*.mp4'

# time interval to ocr from video
time_interval = 1 # in seconds

"""
specify the position of each digit to be recognized
████████████████████  
██     │          ██  D = digit
██    Y│          ██  X e Y = position of the digit
██  X  │          ██  H e W = height and width of the digit
██─────╔═══╗      ██  
██    H║ D ║      ██  
██     ╚═══╝      ██  
██       W        ██  
██                ██  
████████████████████
"""

# height and width of the digits
h = 12
w = 9

# for each number, put the Xs and the Y position of the digits
# pos X (or j) must be a list, pos Y (or i) must be a single int
# you can add or remove items as you like

# time
timej = [94,104,124,134,154,164] # X position for each digit
timei = 2 # Y position of time

# northing
northingj = [84,94,104,114,124,134,144,164,174]
northingi = 22

# easting
eastingj = [96,106,116,126,136,146,166,176]
eastingi = 42

# depth
depthj = [396,406,416,436,446]
depthi = 22

# define funcions to format the strings for each number
def timef(time):
    # 1234567 --> 12:34:56
    return '' #'{}{}:{}{}:{}{}'.format(*time)

def decimalf(string):
    # 12345 --> 123.45 (last two digits are decimals)
    return string[:-2] + '.' + string[-2:]

# edit these list as you add or remove numbers
ifor = [timei, northingi, eastingi, depthi]
jfor = [timej, northingj, eastingj, depthj]
ffor = [timef, decimalf, decimalf, decimalf]
names = ['time','northing', 'easting', 'depth']

# use blank positions (without position) to train the model
# use when a number has a variable number of digits (eg. depth from 1200 to 800)
blank = True
# i/Y e j/X positions for blank areas
blankj = [184,456]
blanki = [22,22]

# distance threshold between the recognized digit and the trained model
# lower values, more chance for a false negative in the flags (recognizes right, but flags says it is wrong)
# higher values, more chance for a false positive (recognizes wrong, but flags says it is right)
dist_thr = 200000

# set channel to use (0=blue, 1=green, 2=red)
# you shoulf pick one 
channel = 2