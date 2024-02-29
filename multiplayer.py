#!/usr/bin/python3
from pynput import keyboard
import uuid
import pygame.mixer as mixer
import subprocess
import os
import sys
# look for #thisiswhereiam
# Fuck the above. Anyway, merge your menu with your volumes :)


# use python player instead:
# /home/chris/Apps/_cf/playertest/mixer.py

myid = uuid.uuid4()
myfilepath = "/tmp/delmeidk" + str(myid)


# Also later, I might want to add an option for a 2-dimensional input instead of just 1-dimensional.

musics = []
channels = []
# class MusicTable:
class Channel:
    def __init__(self,filepath,volume):
        self.filepath = filepath
        self.volume = volume

# for i in range(10):
    # blah = Channel("henlo" + str(i),"henlo2" + str(i))
    # musicstable.append(blah)
# print(musicstable[0].volume,musicstable[0].filepath)
# print(musicstable[1].volume,musicstable[1].filepath)
# print(musicstable[2].volume,musicstable[2].filepath)
# print(musicstable[3].volume,musicstable[3].filepath)

mixer.init()
with open(myfilepath,"w") as myfile:
    myfile.write("File Name -`-,- Volume\n")

# for line in sys.stdin:
mixer.set_num_channels(50)
tindex = 0
for line in sys.argv:
    with open(myfilepath,"a") as myfile:
        if tindex > 0:
            myfile.write(line + " -`-,- 1\n")
        tindex +=1

    
tindex = 0
with open(myfilepath,"r") as myfile:
    for eachline in myfile:
        if tindex > 0:
            parameters = eachline.split(" -`-,- ")
            channels.append(parameters)
            song = mixer.Sound(parameters[0])
            chan = mixer.Channel(tindex)
            musics.append(chan)
            musics[tindex - 1].play(song, loops = -1)

        tindex +=1


def main_menu():
    while True:
        print("# Welcome to the multiplayer # ")
        print("Here is your file:\n")
        print(myfilepath)
        print("Here are your running windows:")

        for i in range (len(channels) ): # was len() -1 but now it's not required for some reason. whatever
            print("index:",i," ",channels[i][0],'  volume = ',musics[i].get_volume())
                

        thiscmd = input()
        global cmdints
        global cmdstrs
        cmdints = [int(s) for s in thiscmd.split() if s.isdigit()]
        cmdstrs = [str(s) for s in thiscmd.split() if not s.isdigit()]


        # If "all" is in the command, add 1 to all
        for eachstr in cmdstrs:
            if eachstr == 'all':
                tindex = 0
                for songs in musics:
                    cmdints.append(tindex)
                    tindex +=1
        
        for eachint in cmdints:
            print(eachint)


        if thiscmd == 'bye':
            break
        if 'ctrl' in thiscmd:
            # Begin listening for commands
            with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
                listener.join()


def on_press(key):
    print(format(key))

    if format(key) == "'9'":
# Stop listener??? don't know what this comment is for
        for cmdint in cmdints:
            try:
                musics[cmdint].set_volume(musics[cmdint].get_volume() - .01)
                print(musics[cmdint].get_volume())
            finally:
                pass
                # hi = 1
                

    if format(key) == "'0'":
        for cmdint in cmdints:
            try:
                musics[cmdint].set_volume(musics[cmdint].get_volume() + .01)
                print(musics[cmdint].get_volume())
            finally:
                pass
                # hi = 2

    if format(key) == "'q'":
        main_menu()

#        mixer.music.set_volume(mixer.music.get_volume() + 100)

#     for cmdint in cmdints:
#         try:
#             subprocess.run('tmux send-keys -t "placeholder".' + str(cmdint) + ' "' + format(key.char) + '"',shell=True)
#             subprocess.run('echo tmux send-keys -t "placeholder".' + str(cmdint) + ' "' + format(key.char) + '"',shell=True)
#             # print(format(key.char))
#         except AttributeError:
#             noexcept = 'cool'
#             # print(format(key))
def on_release(key):
    if key == keyboard.Key.esc:  # Stop listener
        main_menu()

        # return False



main_menu()

