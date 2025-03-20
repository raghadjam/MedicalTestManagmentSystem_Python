

# Python Medical Record Management System

## Overview
This is a Python-based medical record management system. It allows you to add, update, and filter medical test records, and supports importing/exporting data to/from CSV files. The system is designed to store patient medical records and provides a simple command-line interface for interacting with the records.

## Key Features:
- ID Validation: Ensures that each medical record has a valid, unique patient ID, formatted as a 6-digit number.
- Date Validation: Validates the test date to ensure it follows the proper YYYY-MM format.
- Unit Validation: Verifies that the test result unit is one of the accepted values, such as mg/dL, mm Hg, or g/dL.
- Test Status Validation: Ensures that the test status is one of the predefined valid statuses, such as pending, completed, or other user-defined values.
- Medical Test Data Integrity: Validates the overall structure of the test records, ensuring that all required fields (ID, test name, date, value, unit, and status) are present and correctly formatted.

## Functions

- addMedicalTest(): Adds a new medical test to the system, preventing duplicate entries.
- addMedicalRecord(): Adds a new medical record for a patient, including test details, result values, and status.
- updateRecord(): Updates an existing medical record, modifying test details like result values, status, and unit.
- updateMedicalTest(): Updates the details of a specific medical test (e.g., result ranges, unit).
- filterMedicalTests(): Filters and displays medical tests based on selected criteria, such as test name or status.
- exportRecordsToCSV(): Exports all patient records to a CSV file for further analysis.
- importRecordsFromCSV(): Imports patient records from a CSV file into the system.


## Project Files
- medicalRecord.txt: Stores patient medical records in text format.
- medicalTest.txt: Contains details of medical tests available in the system.
- main.py: The main Python script that runs the program.
- PythonReport: Conatains test cases for validating functionality and performance.

## Conclusion:
This Medical Test Record Management System offers an efficient way to store, manage, and retrieve medical test records. The system ensures proper data validation and integrity, maintaining accurate medical records for patients.
