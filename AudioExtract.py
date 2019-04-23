#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Artsuki on 2019-04-23

"""
Please set the input_path before running
"""

import os
import subprocess


input_path = 'X:\\XXX\\Video\\'

class AudioExtract:
    def __init__(self, input_path):
        self.input_path = input_path
        self.output_path = 'audio'
        self.files = os.listdir(input_path)
        
    def output_path_renew(self):
        self.output_path = f'{self.input_path}\\self.output_path\\'
        os.mkdir(self.output_path)
        
    def mp3_convert(self):
        for filename in self.files:
            strcmd = f"ffmpeg -i {self.input_path}{filename} -vn {self.output_path}{filename[:-4]}.mp3"
            print(f'processing {filename}......')
            subprocess.call(strcmd, shell=True)
            print(f'{filename} processed')
            
def main():
    task = AudioExtract(input_path)
    task.output_path_renew()
    task.mp3_convert()


if __main__ == '__main__':
    main()
