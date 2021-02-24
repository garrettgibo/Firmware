import numpy as np
import glob
import os
import fnmatch
import sys

#look for file using input date and time
date = sys.argv[1]
time = sys.argv[2]

for path,dirs,files in os.walk('.'):
    for f in fnmatch.filter(files, time +'.ulg'):
        fullname = os.path.abspath(os.path.join(path,f))

for time in fullname:
    path = fullname

#convert ulg to csv
dir = date + "-" + time
os.system("mkdir " + dir)
os.system("cp " + path + " " + dir)
os.system("ulog2csv " + dir + " " + time + ".ulg")
os.system("cd " + dir)


#TODO still have to find a better way to import csvs without having to cd into dir made
attitude_sp = np.genfromtxt(glob.glob('*attitude_setpoint*')[0], delimiter=',')
attitude_sp_roll = attitude_sp[:,1]
attitude_sp_pitch = attitude_sp[:,2]
attitude_sp_yaw = attitude_sp[:,3]

#these are quaternions
attitude_gt = np.genfromtxt(glob.glob('*attitude_groundtruth*')[0], delimiter=',')
attitude = np.genfromtxt(glob.glob('*attitude_setpoint_0*')[0], delimiter=',')

global_pos = np.genfromtxt(glob.glob('*global_position_0*')[0], delimiter=',')
global_pos_lat = global_pos[:,2]
global_pos_lon = global_pos[:,3]
global_pos_alt = global_pos[:,4]

global_pos_gt = np.genfromtxt(glob.glob('*global_position_groundtruth*')[0], delimiter=',')
global_pos_gt_lat = global_pos_gt[:,2]
global_pos_gt_lon = global_pos_gt[:,3]
global_pos_gt_alt = global_pos_gt[:,4]

local_pos = np.genfromtxt(glob.glob('*local_position_0*')[0], delimiter=',')
local_pos_lat = local_pos[:,3]
local_pos_lon = local_pos[:,4]
local_pos_alt = local_pos[:,21]
local_pos_x = local_pos[:,5]
local_pos_y = local_pos[:,6]
local_pos_z = local_pos[:,7]

local_pos_gt = np.genfromtxt(glob.glob('*local_position_groundtruth*')[0], delimiter=',')
local_pos_gt_lat = local_pos_gt[:,3]
local_pos_gt_lon = local_pos_gt[:,4]
local_pos_gt_alt = local_pos_gt[:,21]
local_pos_gt_x = local_pos_gt[:,5]
local_pos_gt_y = local_pos_gt[:,6]
local_pos_gt_z = local_pos_gt[:,7]

local_pos_sp = np.genfromtxt(glob.glob('*local_position_setpoint*')[0], delimiter=',')
local_pos_sp_x = local_pos_sp[:,1]
local_pos_sp_y = local_pos_sp[:,2]
local_pos_sp_z = local_pos_sp[:,3]

actuator_output = np.genfromtxt(glob.glob('*actuator_output*')[0], delimitr=',')
