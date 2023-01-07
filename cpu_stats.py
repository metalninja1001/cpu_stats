import time
import psutil
import socket
import os
import sys

def fun():
	cpu = psutil.cpu_percent(1)
	cpuA = psutil.cpu_percent(1)
	cpuB = psutil.cpu_percent(1)
	cpuC = psutil.cpu_percent(1)
	cpuD = psutil.cpu_percent(1)
	cpuE = psutil.cpu_percent(1)
	host = socket.gethostname()

	while cpu == cpu:
		print(host, cpu)
		time.sleep(1)
		os.system("cls")
		print(host, cpuA)
		time.sleep(1)
		os.system("cls")
		print(host, cpuB)
		time.sleep(1)
		os.system("cls")
		print(host, cpuC)
		time.sleep(1)
		os.system("cls")
		print(host, cpuD)
		time.sleep(1)
		os.system("cls")
		print(host, cpuE)
		time.sleep(1)
		os.system("cls")

fun()
