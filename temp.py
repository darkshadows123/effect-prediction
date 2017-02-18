import json

import requests
from argparse import ArgumentParser
from requests.auth import HTTPBasicAuth
from urllib import urlopen
import re
from APIDownloader import APIDownloader
from dateUtil import DateUtil

if __name__ == "__main__":
    def byteify(input):
        if isinstance(input, dict):
            return {byteify(key): byteify(value)
                    for key, value in input.iteritems()}
        elif isinstance(input, list):
            return [byteify(element) for element in input]
        elif isinstance(input, unicode):
            return input.encode('utf-8')
        else:
            return input
    def download_api(url, username=None, password=None, headers=None):
        auth = None
        if username is not None:
            auth = HTTPBasicAuth(username, password)
        response = requests.get(url, verify=False,	auth=auth, headers=headers)
        # print response.text
        return byteify(json.loads(response.text))	
    # Two Properties : platform and target software ..... class computerHardware
    def write_as_json_lines(array, file_handler):
        i = 0
        print len(array)
        for line in array:
            i = i + 1
            print "i = ",i
            if (i == 100):
                break;
            line = json.dumps(line, ensure_ascii=False)
            file_handler.write(line + "\n")
    # date = "2017-02-14T12:00:00+00:00"
    # date = DateUtil.unix_timestamp(date, "%Y-%m-%dT%H:%M:%S%Z")
    # print date
    # timestamp = DateUtil.unix_timestamp(date, "%Y-%m-%dT%H:%M:%S%Z")
    url = "https://apigargoyle.com/GargoyleApi/getHackingPosts?from=" + "1970-01-01&limit=20"
    headers = {"userId" :"usc","apiKey": "0d91afcb-a286-4967-a880-ea0cf9697f1f", "Connection" : "close"}

    data = download_api(url, None, None, headers)
    # json_data = open('sample.json.txt').read()
    # data = byteify(json.loads(json_data))
    if data is not None:
    	out_file = open("hackingpost" + ".jl", "w")
        write_as_json_lines(data['results'], out_file)