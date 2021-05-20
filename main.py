import csv
from pprint import pprint

class Node:
    def __init__(self, location=None, totalCases=None, totalICU=None, totalVacc=None, totalDeaths=None, totalHosp=None, totalTests=None):
        self.location = location
        self.totalCases = totalCases
        self.totalICU = totalICU
        self.totalVacc = totalVacc
        self.totalDeaths = totalDeaths
        self.totalHosp = totalHosp
        self.totalTests = totalTests
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    # this function prints contents of linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print("Analysis for ", printval.location)
            print("Total Cases = ", printval.totalCases)
            print("Total Vaccinations = ", printval.totalVacc)
            print("Total number of patients in ICU = ", printval.totalICU)
            print("Total number of deaths in ICU = ", printval.totalDeaths)
            print("Total number of hospital patients = ", printval.totalHosp)
            print("Total number of tests = ", printval.totalTests)
            print("------------------------------------\n")
            printval = printval.nextval

    # this function counts number of nodes in list
    def listcount(self):
        val = self.headval
        counter = 0
        while val is not None:
            counter = counter + 1
            val = val.nextval
        return counter

    #function to add new node at the end
    def append(self, location, cases, vacc, icu, deaths, hosp, tests):
        # 1. This new Node is going to be the last node
        NewNode = Node(location, cases, vacc, icu, deaths, hosp, tests)
        # 2. if the linked list is empty, then make the new node as head
        if self.headval is None:
            self.headval = NewNode
            return
        # 3. Else traverse till the last node and check if this country
        # already found in list
        # if yes, update it's data
        last = self.headval
        while(last.nextval):
            if location != '\0':
                if location != "":
                    if last.location != '\0':
                        if last.location == location:
                            tcases = last.totalCases + cases
                            last.totalCases = tcases
                            ticu = last.totalICU + icu
                            last.totalICU = ticu
                            tvacc = last.totalVacc + vacc
                            last.totalVacc = tvacc
                            tdeaths = last.totalDeaths + deaths
                            last.totalDeaths = tdeaths
                            thosp = last.totalHosp + hosp
                            last.totalHosp = thosp
                            ttests = last.totalTests + tests
                            last.totalTests = ttests
                            return
            last = last.nextval
        # 4. Once you reach last node check first if this node has same country name
        # if yes, update data
        # if no add new node
        if location != '\0':
            if location != "":
                if last.location != '\0':
                    if last.location == location:
                        tcases = last.totalCases + cases
                        last.totalCases = tcases
                        ticu = last.totalICU + icu
                        last.totalICU = ticu
                        tvacc = last.totalVacc + vacc
                        last.totalVacc = tvacc
                        tdeaths = last.totalDeaths + deaths
                        last.totalDeaths = tdeaths
                        thosp = last.totalHosp + hosp
                        last.totalHosp = thosp
                        ttests = last.totalTests + tests
                        last.totalTests = ttests
                        return
        last.nextval = NewNode

with open('owid-covid-data.csv', 'r') as file:
    reader = csv.reader(line for line in file)
    fieldsList = list(reader)
    list1 = SLinkedList()
    flag = 0
    for row in fieldsList:
        if flag == 1:
            if list1.listcount() <= 7:
                location = row[2]
                if row[5] == '':
                    row[5] = 0.0
                if row[8] == '':
                    row[8] = 0.0
                if row[17] == '':
                    row[17] = 0.0
                if row[19] == '':
                    row[19] = 0.0
                if row[26] == '':
                    row[26] = 0.0
                if row[34] == '':
                    row[34] = 0.0
                cases = int(float(row[5]))
                deaths = int(float(row[8]))
                icu = int(float(row[17]))
                hosp = int(float(row[19]))
                tests = int(float(row[26]))
                vacc = int(float(row[34]))
                list1.append(location, cases, vacc, icu, deaths, hosp, tests)
            else:
                break
        flag = 1 
    list1.listprint()