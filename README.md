
# Full offensive and defensive simulation

## Overview
This projects simulates a brute force ssh attack on a machine, aswell as log monitoring and reporting system.

## How to use
1. download virtualBox on your computer.
2. create an Ubuntu Desktop and a Kali VM
3. configure a network adapter with the internal network setting on both VMs. Make sure both VMs use the exact same name and IPv4 address.

## Structure
**offensive/pentest/** contains offensive tools used the brute-forece ssh attack.
**defensive/defend/** contains tools used for monitoring logs and sending aerts to a slack server.

## Offensive tools
1. helper.sh: bash file used to gather network information and put it into network-infomration.txt.
2. network-information.txt: contains subnet mask, ipv4 address, and network address
3. host-information.json: contains detailed information about each port that is opened on each device.
4. rockyou.txt: a text file containing a list of common passwords for brute-forcing. Shortened for efficacy
5. recon.py: uses subnet address from network-information.txt and uses NMAP to scan for all "up" hosts, and scans ports 1-1000 on "up" hosts.
6. brute_force_ssh.py: asks the user to choose the target ip address, then uses rockyou.txt to attempt a dictionary attack on the ip address. Assumes that the username is already compromised.
7. toolkit.py, combines functionality of brute_force_ssh.py and recon.py; allows the user to enter 'q' to quit the program.
8. ssh_password.txt: contains the correct password found from SSH attempts.

## Defensive tools
1. logMonitor.py: monitors the '/var/log/auth.log' file on the ubuntu system for SSH successfull attemps and how many passwords were used.
2. alert.py: sends alert to a slack server.
3. toolkit.py: combines functionality of alert.py and logMonitr.py

## How to use it
1. On the victim machine (V) run toolkit.py foud at **./defensive/defend/toolkit.py**
2. On the Kali machine, run toolkit.py and follow instructions in terminal.

## Requirements
1. Python3
2. paramiko and nmap python libraries
3. computer that can run run two VMs simultaneously
