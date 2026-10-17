## Team Workflow
- Pull changes before starting work.
- Use meaningful commit messages.
- Push completed changes to GitHub.
- Review changes before merging.
AttendX Test Scripts
Project Overview

This repository contains automated UI test scripts for the AttendX student attendance application.

Test Scripts
tests/test_login.py — verifies student login and dashboard visibility.
tests/test_attendance.py — verifies the attendance-marking workflow and confirmation status.
Prerequisites
Python 3
Google Chrome
Selenium
pytest
A running AttendX test application and a valid test account
Installation

Install the required packages:

python -m pip install pytest selenium


Configure the application URL and test credentials using the ATTENDX_URL, ATTENDX_TEST_USER, and ATTENDX_TEST_PASSWORD environment variables.

Running Tests

Run the login test:

python -m pytest tests/test_login.py -v


Run the attendance test:

python -m pytest tests/test_attendance.py -v


Run all tests:

python -m pytest tests/ -v

Version Control

Git is used to track changes to scripts and documentation. GitHub hosts the remote repository so team members can share work and review changes.
