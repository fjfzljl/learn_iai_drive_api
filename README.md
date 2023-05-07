# pytest_iai_drive_api
Test invertedai.api.drive()

## This test can run in macOS. Install requirement
```shell
make install
```

OR

```shell
pip install -r requirements.txt
```


## How to run the tests in macOS
```shell
make test
```

OR

```shell
python3 start_tests.py
```

OR run only selected test cases

```shell
python3 start_tests.py -t TEST00001
```

## How to view the report
The test report should save in pytest_report.html


## File Structure
- pytest.ini : explain the test cases mark
- conftest.py : includes test setup, teardown, and test report setting
- starts_tests.py : main function to start the test
- test_drive.py : all test cases

## Documents
- documents/test_plan.xlsx : test plan

