"""Upload waypoints to a mav device
Usage:
  main.py <plane-uri> --wp_path=<wp_path_file>
  main.py -h | --help
Options:
  --wp_path=<wp_path_file>  path to csv that contains waypoints of format (lat, lon, alt)
  -h --help                 show this
"""
from docopt import docopt
import numpy as np
from pymavlink import mavutil, mavwp


def upload_waypoints(**config):
    """Upload waypoints to mav device"""
    master = mavutil.mavlink_connection(config["<plane-uri>"])
    master.wait_heartbeat(blocking=True)
    wp = mavwp.MAVWPLoader()
    frame = mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT
    radius = 10
    coords = np.genfromtxt(config["--wp_path"], delimiter=",")

    master.waypoint_clear_all_send()
    master.waypoint_count_send(len(coords))

    for seq, (lat, lon, alt) in enumerate(coords):
        # add waypoint to uploader
        wp.add(mavutil.mavlink.MAVLink_mission_item_message(
            master.target_system,
            master.target_component,
            seq + 1,
            frame,
            mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,
            0, 0, 0, radius, 0, 0,
            lat, lon, alt))

        # Send waypoint
        wp_msg = wp.wp(seq)
        master.mav.send(wp_msg)
        print(f"Sending waypoint {seq}: ({wp_msg.x}, {wp_msg.y}, {wp_msg.z})")


if __name__ == '__main__':
    arguments = docopt(__doc__)
    upload_waypoints(**arguments)
