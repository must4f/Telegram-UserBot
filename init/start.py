#!/usr/bin/env python3
import os
tf = open("./temp.txt", "w+")
tf.write("False")
tf = open("./temp.txt", "r")
isRestart = tf.read()
isFirstBoot = True
print(isRestart)
while isRestart == "True" or isFirstBoot:
  os.system("redis-server --daemonize yes")
  os.system("python3 -m userbot")
  isFirstBoot = False
  tf = open("./temp.txt", "r")
  if isRestart == "True":
    open("./temp.txt", "w").close()
    tf = open("./temp.txt", "w+")
    tf.write("False")
  isRestart = tf.read()