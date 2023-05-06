import sys
import argparse
import subprocess
import os


def run_tests_with_scenarios(scenarios, testmarker, htmlOutput, basetestpath):
    if "win32" in sys.platform:
        pytest_command = "python -m pytest --log-level=INFO"
    else:
        # used in 'darwin'
        pytest_command = "python3 -m pytest --log-level=INFO"

    if testmarker:
        if htmlOutput == "YES":
            command = (
                pytest_command
                + " --capture=sys --html="
                + basetestpath
                + os.path.sep
                + "pytest_report.html --self-contained-html --junitxml="
                + basetestpath
                + os.path.sep
                + "pytest_report.xml "
                + basetestpath
                + os.path.sep
                + scenarios
                + ' -v -k "'
                + testmarker
                + '"'
            )
        else:
            command = (
                pytest_command
                + " -s --junitxml="
                + basetestpath
                + os.path.sep
                + "pytest_report.xml "
                + basetestpath
                + os.path.sep
                + scenarios
                + ' -v -k "'
                + testmarker
                + '"'
            )
    else:
        if htmlOutput == "YES":
            command = (
                pytest_command
                + " --capture=sys --html="
                + basetestpath
                + os.path.sep
                + "pytest_report.html --self-contained-html --junitxml="
                + basetestpath
                + os.path.sep
                + "pytest_report.xml "
                + basetestpath
                + os.path.sep
                + scenarios
                + " -v"
            )
        else:
            command = (
                pytest_command
                + " -s --junitxml="
                + basetestpath
                + os.path.sep
                + "pytest_report.xml "
                + basetestpath
                + os.path.sep
                + scenarios
                + " -v"
            )
    print(command)
    res = subprocess.call(command, shell=True)
    return res


def main():
    testmarker = ""
    htmlOutput = "YES"

    parser = argparse.ArgumentParser()
    requiredNamed = parser.add_argument_group("required named arguments")
    parser.add_argument(
        "--testmarker",
        "-t",
        default=None,
        help="Pass marker to run specific group of tests",
    )
    parser.add_argument(
        "--htmlOutput",
        default="YES",
        help="NO for debugging - output will go to stdout and summary will be unavailable",
    )

    args = parser.parse_args()

    testmarker = args.testmarker
    htmlOutput = args.htmlOutput

    basetestpath = os.getcwd()

    scenarios = "test_drive.py"

    run_tests_with_scenarios(scenarios, testmarker, htmlOutput, basetestpath)


if __name__ == "__main__":
    main()
