import os
import json
from glob import glob
import shutil
import datetime

dir_path = os.path.dirname(os.path.realpath(__file__)) + '/stations'

def get_json(statation_name):
    with open(dir_path + '/' + statation_name + '.json') as f:
        return json.load(f)

def get_stations():
    file_names = glob(dir_path + '/*.json')
    stations = list()
    for file_name in file_names:
        with open(file_name) as f:
            stations.append(json.load(f))
    return stations


def backup():
    dest_dir = dir_path + '/' + 'backup' + datetime.datetime.now().isoformat()
    dest_dir = dest_dir.replace('.', '__').replace(':', '_')
    os.mkdir(dest_dir)
    file_names = glob(dir_path + '/*.json')
    for file_name in file_names:
        shutil.move(file_name, dest_dir)
        

def save_station(station_info, station_name):
    file_name = dir_path + '/' + station_name + '.json'
    with open(file_name, 'w') as f:
        json.dump(station_info, f, indent=2)