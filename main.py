import re
import csv
from datetime import datetime
import time
import datetime


class Patients:
    def __init__(self, id, testName, testDateAndTime, result, unit, status, resultsDate):
        self.id = id
        self.testName = testName
        self.testDateAndTime = testDateAndTime
        self.result = result
        self.unit = unit
        self.status = status
        self.resultsDate = resultsDate

    def addRecord(self):
        with open("medicalRecord.txt", "a") as f:
            if self.resultsDate:
                record_line = (f"\n{self.id}: {self.testName}, {self.testDateAndTime}, "
                               f"{self.result}, {self.unit}, {self.status}, {self.resultsDate}\n")
            else:
                record_line = (f"\n{self.id}: {self.testName}, {self.testDateAndTime}, "
                               f"{self.result}, {self.unit}, {self.status}\n")
            f.write(record_line)

    def updateRecord(self):
        lines = []
        with open("medicalRecord.txt", "r") as f:
            lines = f.readlines()

        with open("medicalRecord.txt", "w") as f:
            for line in lines:
                if line.startswith(self.id + ":"):
                    if self.resultsDate:
                        record_line = (f"{self.id}: {self.testName}, {self.testDateAndTime}, "
                                       f"{self.result}, {self.unit}, {self.status}, {self.resultsDate}\n")
                    else:
                        record_line = (f"{self.id}: {self.testName}, {self.testDateAndTime}, "
                                       f"{self.result}, {self.unit}, {self.status}\n")
                    f.write(record_line)
                else:
                    f.write(line)
####################################################################
def displayMainMenu():
    print("1. Add new medical test.")
    print("2. Add a new medical test record.")
    print("3. Update patient records including all fields.")
    print("4. Update medical tests in the medicalTest file.")
    print("5. Filter medical tests.")
    print("6. Generate textual summary reports.")
    print("7. Export medical records to a comma separated file.")
    print("8. Import medical records from a comma separated file.")
    print("9. Exit.")
####################################################################
# case1
def addMedicalTest():
    testName = input("Enter the test name you want to add:\n").strip()
    test_exists = False
    f = open("medicalTest.txt", "r")
    for line in f:

        if re.search(r"\b" + testName + r"\b", line.strip(), re.IGNORECASE):
            test_exists = True
            break
    if test_exists:
        print("The test already exists.")
        addMedicalTest()
    else:
        testRange = input("Enter the range in the following format > x or < y or both:\n")
        unit = input("Enter the unit:\n")
        turnaround = input("Enter the turnaroud time in the following format DD-hh-mm:\n")
        days, hours, min = turnaround.split('-')
        if len(days) == 2:
            if (len(hours) == 2 and int(hours) < 24):
                if (len(min) == 2 and int(min) < 60):
                    f = open("medicalTest.txt", "a")
                    f.write(f"Name: {testName}; Range: {testRange}; Unit: {unit}, {turnaround}\n")
                    f.close()
            else:
                print("Use the correct format.")
                addMedicalTest()
        else:
            addMedicalTest()
####################################################################
# case2
def addMedicalRecord():
    while True:
        id = input("Enter the ID you want to add:").strip()
        if id.isdigit() and len(id) == 7:
            break
        else:
            print("Invalid ID.Please try again.")
    while True:
        testName = input("Enter the test name you want to add:").strip()
        test_exists = False
        f = open("medicalTest.txt", "r")
        for line in f:
            if re.search(r"\b" + testName + r"\b", line.strip(), re.IGNORECASE):
                test_exists = True
                break
        if test_exists:
            break
        else:
            print("Test does not exist. Please enter a valid test name.")
    while True:
        dateTime = input("Enter Test date and time (format like YYYY-MM-DD hh:mm):")
        testDate, testTime = dateTime.split(" ")
        year, month, day = testDate.split("-")
        hour, min = testTime.split(":")
        if int(year) <= 2024:
            if int(month) >= 1 and int(month) <= 12:
                if int(day) >= 1 and int(day) <= 31:
                    if int(hour) >= 0 and int(hour) <= 23:
                        if int(min) >= 1 and int(min) <= 59:
                            break
                        else:
                            print("Enter a valid date and time")
                    else:
                        print("Enter a valid date and time")
                else:
                    print("Enter a valid date and time")
            else:
                print("Enter a valid date and time")
        else:
            print("Enter a valid date and time")
    result = input("Enter the result:")
    while result.isalpha():
        result = input("Enter the result:")
    unit = input("Enter the test unit:")
    status = input("Enter the status:").lower()
    if status == "completed":
        dateTime1 = input("Enter the test turnaround (format like YYYY-MM-DD hh:mm)")
        while True:
            testDate1, testTime1 = dateTime1.split(" ")
            year1, month1, day1 = testDate1.split("-")
            hour1, min1 = testTime1.split(":")
            if int(year1) <= 2024:
                if int(month1) >= 1 and int(month1) <= 12:
                    if int(day1) >= 1 and int(day1) <= 31:
                        if int(hour1) >= 0 and int(hour1) <= 23:
                            if int(min1) >= 1 and int(min1) <= 59:
                                break
                            else:
                                print("Enter a valid date and time")
                                dateTime1 = input("Enter the test turnaround (format like YYYY-MM-DD hh:mm)")
                        else:
                            print("Enter a valid date and time")
                            dateTime1 = input("Enter the test turnaround (format like YYYY-MM-DD hh:mm)")
                    else:
                        print("Enter a valid date and time")
                        dateTime1 = input("Enter the test turnaround (format like YYYY-MM-DD hh:mm)")
                else:
                    print("Enter a valid date and time")
                    dateTime1 = input("Enter the test turnaround (format like YYYY-MM-DD hh:mm)")
            else:
                print("Enter a valid date and time")
                dateTime1 = input("Enter the test turnaround (format like YYYY-MM-DD hh:mm)")
        patientObj = Patients(id, testTime, dateTime, result, unit, status, dateTime1)
        patientObj.addRecord()
        return

    patientObj = Patients(id, testTime, dateTime, result, unit, status, 0)
    patientObj.addRecord()
####################################################################
# case3
def updateAllFields():
    while True:
        id = input("Enter the ID you want to update: ").strip()
        if id.isdigit() and len(id) == 7:
            id_exists = False
            with open("medicalRecord.txt", "r") as f:
                for line in f:
                    if line.startswith(id + ":"):
                        id_exists = True
                        while True:
                            testName = input("Enter the test name you want to add:").strip()
                            test_exists = False
                            with open("medicalRecord.txt", "r") as f_test:
                                for line in f_test:
                                    if re.search(r"\b" + re.escape(testName) + r"\b", line.strip(), re.IGNORECASE):
                                        test_exists = True
                                        break
                            if test_exists:
                                break
                            else:
                                print("Test does not exist. Please enter a valid test name.")

                        testDateAndTime = input(
                            "Enter the new value of test date and time (format like YYYY-MM-DD hh:mm): ").strip()
                        result = input("Enter the new value of the result: ").strip()
                        unit = input("Enter the new value of the unit: ").strip()
                        status = input("Enter the new value of the status: ").strip()
                        if status == "completed":
                            resultsDate = input("Enter the new test turnaround (format like YYYY-MM-DD hh:mm)")
                        else:

                            resultsDate = 0

                        patient = Patients(id, testName, testDateAndTime, result, unit, status, resultsDate)
                        patient.updateRecord()

                        break
            if id_exists:
                break
            else:
                print("ID does not exist. Please enter a valid ID.")
        else:
            print("Invalid ID. The ID must be a 7-digit number. Please try again.")
####################################################################
# case4
def updatemedicalTest():
    testName = input("Enter the test name you want to update:\n").strip()
    test_exists = False
    with open("medicalTest.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        if re.search(r"\b" + testName + r"\b", line.strip(), re.IGNORECASE):
            test_exists = True
            break
    if not test_exists:
        print("The test does not exist. Please add the test before updating.")
        return
    range_value = ""
    unit_value = ""
    turnaround_value = ""
    str1 = input("Do you want to change the range (Yes or No): ").strip().lower()
    if str1 == "yes":
        range_value = input("Enter the new value of the range (like this format > X or < Y or both and make sure to include the comma): ").strip()
    str2 = input("Do you want to change the unit (Yes or No): ").strip().lower()
    if str2 == "yes":
        unit_value = input("Enter the new value of the unit:").strip()
    str3 = input("Do you want to change the turnaround date (Yes or No): ").strip().lower()
    if str3 == "yes":
        turnaround_value = input("Enter the new value of the turnaround date (like this format DD-hh-mm): ").strip()
    with open("medicalTest.txt", "w") as f:
        for line in lines:
            if re.search(r"\b" + testName + r"\b", line.strip(), re.IGNORECASE):
                name, range, unit = line.split(";")
                rangeName,originalRange=range.split(":")
                originalRange=originalRange.replace(","," ").strip()
                u,t= unit.split(",")
                unitName, originalUnit = u.split(":")
                originalUnit = originalUnit.strip()
                t=t.strip()
                if range_value =="":
                    range_value=originalRange
                if unit_value =="":
                    unit_value=originalUnit
                if turnaround_value == "":
                    turnaround_value = t
                updated_line = (
                    f"Name: {str(testName)}; Range: {str(range_value)}; Unit: {str(unit_value)}, {turnaround_value}\n")
                f.write(updated_line)
            else:
                f.write(line)
####################################################################
# case5
def filterMedicalTests():
    print("Enter Yes for the criteria you want to filter and No for other:")
    idFilter = ""
    testNameFilter = ""
    resultFilter = ""
    startDateFilter = ""
    endDateFilter = ""
    turnaroundFilter = ""
    statusFilter = ""
    idOption = input("do you want to retrieve the id: ").lower().strip()
    if idOption == "yes":
        idFilter = input("Enter the id:")
    testNameOption = input("do you want to retrieve the test Name: ").lower().strip()
    if testNameOption == "yes":
        testNameFilter = input("Enter the test name:")
    resultOption = input("do you want to retrieve the Abnormal tests: ").lower().strip()
    if resultOption == "yes":
        resultFilter = "value"
    periodOption = input("do you want to retrieve test within a specific period: ").lower().strip()
    if periodOption == "yes":
        startDateFilter = input("Enter the start date like this format %d-%m-%Y:").strip()
        endDateFilter = input("Enter the end date like this format %d-%m-%Y:").strip()
    statusOption = input("do you want to retrieve the status:").lower().strip()
    if statusOption == "yes":
        statusFilter = input("Enter the status:")
    turnaroundOption = input("do you want to retrieve the turnaround:").lower().strip()
    if turnaroundOption == "yes":
        turnaroundFilter = "value"
    filtered_tests = []
    filteredTurn_tests = []
    turnaround_dict = {}
    with open("medicalRecord.txt", "r") as file:
        lines = len(file.readlines())
    file.close()
    with open("medicalRecord.txt", "r") as file:
        lineNum = 1
        for line in file:
            lineNum += 1
            fields = line.split(', ')
            if len(fields) == 6:
                test, date_time, result, unit, status, turnaround = line.strip().split(', ')
                id, testName = test.strip().split(":")
                date, time = date_time.split(" ")
                hours, min2 = time.split(":")
                hours = int(hours)
                min2 = int(min2)
                date1, time1 = turnaround.split(" ")
                hours1, min1 = time1.split(":")
                hours1 = int(hours1)
                min1 = int(min1)
            else:
                test, date_time, result, unit, status = line.strip().split(', ')
                id, testName = test.strip().split(":")
                date, time = date_time.split(" ")
                hours, min2 = time.split(":")
                turnaround = 0
            if turnaround:
                a = datetime.datetime(1, 1, 1, hours1, min1, 1)
                b = datetime.datetime(1, 1, 1, hours, min2, 1)
                c = a - b  # turnaround Difference
                seconds = c.seconds
                turnaroundDiff = seconds
            if idFilter and id != idFilter:
                continue
            if testNameFilter and testName.strip() != testNameFilter:
                continue
            if resultFilter:
                with open("medicalTest.txt", "r") as f:
                    for l in f:
                        fTest, fRange, fUnit = l.split("; ")
                        if "," in fRange:
                            string = fRange.split(" ")
                            lower = string[2].replace(",", "")
                            upper = string[4]
                            if (lower < result < upper):
                                continue
                        else:
                            string = fRange.split(" ")
                            upper = string[2]
                            if result < upper:
                                continue
            if startDateFilter.strip() and endDateFilter.strip():
                dateBetween = datetime.datetime.strptime(date, "%d-%m-%Y")
                start = datetime.datetime.strptime(startDateFilter, "%d-%m-%Y")
                end = datetime.datetime.strptime(endDateFilter, "%d-%m-%Y")
                if not (start <= dateBetween <= end):
                    continue
            if statusFilter and status.strip() != statusFilter:
                continue

            if turnaroundFilter and turnaround:
                turnaround_dict[turnaroundDiff] = line.strip()

            if turnaround_dict and lineNum == lines + 1 and turnaroundDiff:
                max_key = max(turnaround_dict.keys())
                filtered_tests = []
                filtered_tests.append(turnaround_dict[max_key])
                min_key = min(turnaround_dict.keys())
                filtered_tests.append(turnaround_dict[min_key])
            else:
                filtered_tests.append(line.strip())

        for item in filtered_tests:
            print(item)
    return filtered_tests
####################################################################
# case6
def generaTetextualSummary(filtered):
    testDist = {}
    values = {}
    turnaraounds = {}
    turnDist = {}
    for i in filtered:
        fields = i.split(', ')
        if len(fields) == 6:
            test, date_time, result, unit, status, turnaround = i.strip().split(', ')
            id, testName = test.strip().split(":")
            if testName not in testDist:
                testDist[testName] = []
            testDist[testName].append(result)
            values[result] = i.strip()
            date, time = date_time.split(" ")
            hours, min2 = time.split(":")
            hours = int(hours)
            min2 = int(min2)
            date1, time1 = turnaround.split(" ")
            hours1, min1 = time1.split(":")
            hours1 = int(hours1)
            min1 = int(min1)
        else:
            test, date_time, result, unit, status = i.strip().split(', ')
            id, testName = test.strip().split(":")
            if testName not in testDist:
                testDist[testName] = []
            testDist[testName].append(result)
            values[result] = i
            date, time = date_time.split(" ")
            hours, min2 = time.split(":")
            turnaround = 0
        if turnaround:
            a = datetime.datetime(1, 1, 1, hours1, min1, 1)
            b = datetime.datetime(1, 1, 1, hours, min2, 1)
            c = a - b
            seconds = c.seconds
            turnaroundDiff = seconds
            turnaraounds[turnaroundDiff] = i.strip()
            if testName not in turnDist:
                turnDist[testName] = []
            turnDist[testName].append(turnaroundDiff)

    String1 = []

    for key in values.keys():
        String1.append(key)
    int_numbers = [float(num) for num in String1]
    max_key = max(int_numbers)
    min_key = min(int_numbers)

    print(f"Max value for the filtered tests is: {max_key}")
    print(f"Min value for the filtered tests is: {min_key}")

    for k in testDist:
        test = [float(value) for value in testDist[k]]
        avg = sum(test) / len(test)
        print(f"The average for test{k} is {avg}")

    String2 = []

    for key1 in turnaraounds.keys():
        String2.append(key1)
    int_numbers1 = [float(num1) for num1 in String2]
    max_key1 = max(int_numbers1)
    min_key1 = min(int_numbers1)
    hoursmax = int(max_key1//3600)
    minmax = int(max_key1 % 3600 // 60)
    hoursmin = int(min_key1 // 3600)
    minmin = int(min_key1 % 3600 // 60)
    print(f"Max turnarounds for the filtered tests is: {hoursmax}:{minmax}")
    print(f"Min turnarounds for the filtered tests is: {hoursmin}:{minmin}")
    for k in turnDist:
        test1 = [float(value1) for value1 in turnDist[k]]
        avg = sum(test1) / len(test1)
        print(f"The average for turnaround test{k} is {avg} seconds")
####################################################################
# case7
def exportMedicalRecords():
    with open("medicalRecord.txt", "r") as f:
        lines = f.readlines()
    with open("medicalRecords.csv", "w", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["ID", "Test Name", "Test Date and Time", "Result", "Unit", "Status", "Results Date"])
        for line in lines:
            line = line.strip()
            parts = line.split(", ")
            id_and_test = parts[0].split(": ")
            id = id_and_test[0]
            test_name = id_and_test[1]
            csvwriter.writerow([id, test_name] + parts[1:])
####################################################################
# case8
def importMedicalRecords():
    with open("medicalRecords.csv", "r", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        with open("medicalRecord.txt", "w") as txtfile:
            for row in csvreader:
                test_datetime = row["Test Date and Time"]
                results_date = row["Results Date"]
                if not test_datetime:
                    test_datetime = ""
                if not results_date:
                    results_date = ""
                line = f"{row['ID']}, {row['Test Name']}, {test_datetime}, {row['Result']}, {row['Unit']}, {row['Status']}, {results_date}\n"
                txtfile.write(line)
######################################################################
displayMainMenu()
x = int(input("Select your option:"))
option = 0
while x != 9:
    if x == 1:
        addMedicalTest()
    elif x == 2:
        addMedicalRecord()
    elif x == 3:
        updateAllFields()
    elif x == 4:
        updatemedicalTest()
    elif x == 5:
        filtered = filterMedicalTests()
        option = 1
    elif x == 6:
        if option:
            generaTetextualSummary(filtered)
        else:
            print("Filter the tests first")
    elif x == 7:
        exportMedicalRecords()
    elif x == 8:
        importMedicalRecords()
    else:
        print("Invalid option, please try again.")

    displayMainMenu()
    x = int(input("Select your option:"))
