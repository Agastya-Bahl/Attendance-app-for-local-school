import pandas as pd
from tkinter import *
import os
import numpy as np
import random
import pickle as pkl
import sys
import csv

optionPrimary = input("Enter 'A' to add attendance for today or 'I' for informtion                       on your attendance data: ")

if optionPrimary.upper() == 'A':
    dateTemp = input("Enter the date (DDMMYYYY): ")

    att = [["Name", "Roll No.", "Attendance"]]
    opt = ""
    while opt != "E" and opt != 'e':
        opt = input(
            "Enter 'A' to add a student or 'E' to exit and update the Excel sheet: "
        )
        if opt == "A" or opt == 'a':
            name = input("Enter student name: ")
            rono = input("Enter their roll no.: ")
            attend = input("Enter 'P' if they are present else enter 'A': ")
            while attend.upper() not in ['P', 'A']:
                attend = input("Please enter 'P' or 'A': ")
            att.append([name, rono, attend.upper()])

    print(att)
    date = dateTemp[:2] + "/" + dateTemp[2:4] + "/" + dateTemp[4:]

    with open('attendance.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date])
        writer.writerows(att)
        writer.writerow("")

else:
    read_att = []
    nums = ['0', '1', '2', '3']
    with open('attendance.csv', 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            if len(row) > 0:
                read_att.append(row)

    for i in range(-1, -len(read_att) - 1, -1):
        if read_att[i][0][0] in nums:
            n = i + 2 + len(read_att)
            break

    print(read_att)
    print(n)
    num_abs = 0
    total = 0
    absentees = []
    for i in range(n, len(read_att)):
        total += 1
        if read_att[i][2] == 'A':
            num_abs += 1
            absentees.append(read_att[i][0])
    print(total - num_abs, "/", total, " students were present on ",
          read_att[n - 2][0], ". Those absent were: ", absentees, ".")
