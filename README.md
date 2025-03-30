<table>
<tr style="border: none">
<td style="border: none">

# THE Python Template Repository

</td>
<td align="right" style="border: none">
<img src="./img/scaleup.png" alt="Scaleup" height="100">
</td>
</tr>
</table>

This is a template repository for the Tel Hai Excellenteam (THE) Python course.

All exercises and submissions should follow the format of this repository. For your convenience, you can start each assignment by cloning this template.

## Environment Setup and Pycharm Installation
During the course we will utilize Linux based operating system (OS), to run and execute programs.

### Windows Installation
1. Install [WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install
) , with Ubuntu distribution.
2. Make sure you have a GUI system installed for WSL:
     - a. WSLg is built into WSL2 on Windows 11 (Good for you!)
     - b. Or install an X server on Windows like VcXsrv or Xming
3. Launch WSL and install required dependencies:
```bash
   sudo apt update
   sudo apt install openjdk-17-jdk curl unzip -y
```
4. Download [PyCharm](https://download.jetbrains.com/python/pycharm-community-2023.3.3.tar.gz)
5. Install Pycharm
```bash
curl -L -o pycharm.tar.gz 
tar -xzf pycharm.tar.gz
cd pycharm-*/bin
./pycharm.sh
``` 
   PyCharm will launch (if GUI is set up properly).
5. Install Git in WSL 
   If it’s not installed yet:
```bash
sudo apt update 
sudo apt install git -y
```
6. Then verify git installation using following command
```bash
git --version
```

### Linux/Mac Installation
Congragulations, you made the right decision.
1. [Install Pycharm](https://www.jetbrains.com/help/pycharm/installation-guide.html)

## Grading and Conventions
Your assignment will be graded according to the following criteria. Please make sure your assignment follows the standards and conventions outlined below:

### Python Conventions and Best Practices
In this course you will be required to follow industry standard conventions [Python PEP8 Conventions](https://peps.python.org/pep-0008/). Make sure that once in a while you take a look at the conventions. We have installed a [GitHub Action](https://docs.github.com/en/actions/writing-workflows/quickstart) (extra curriculum) workflow to help you ensure and validate that you follow the conventions as expected, each time a new pull request is created or updated. Additionally you are highly encouraged to use your IDE's ([Pycharm](https://www.jetbrains.com/pycharm/)) built-in linter ;)

For best practices please use examples presented in [PRACTICES.md](PRACTICES.md), if still there is an uncertainty or missing use cases, you are highly encouraged to contact the staff for further clarifications.

### Branching
Use the [WORK-INSTRUCTIONS.md](WORK-INSTRUCTIONS) file as your guideline for proper use of Git. For more information, you are encouraged to search online for "[GitHub Workflow Methodology](https://www.youtube.com/watch?v=U_IFGpJDbeU&ab_channel=DevOpsToolkit)."

### Python Environment
1. Use Python 3.10 as the interpreter.
2. At submission, ensure that the `requirements.txt` file is updated and contains all required packages for the application to run.

### Repository Structure
Please follow the guidelines in this section strictly.

<table>
<tr style="border: none">
<td style="border: none"><img src="./img/snakey_python.png" alt="Python Logo" width="70" height="70"></td>
<td style="border: none"><h4>Python Environment Structure</h4></td>
</tr>
</table>

* The repository should include a `requirements.txt` file at the root directory.
  * Make sure that `requirements.txt` is up to date — it should contain **only** the dependencies that are actually used in the project. Missing or extra packages will negatively affect your grade.
* The repository **MUST NOT** include the `venv` directory.

#### GitHub Configuration
* The repository should include a `README.md` file at the root directory.
* You must have a `.gitignore` file, and there shouldn’t be any unnecessary files in the repository.
* 🚨 **CRITICAL:** Do not touch `.github/workflows` directory :(
* You must have an `img` directory at the root directory.

#### Project's Files
* The repository should include a `main.py` file (this should be the entry point of the repository) at the root.
* The repository should include a `src` directory at the root.
  * All source files should be placed in the `src` directory.
* The repository should include a `test` directory at the root.
  * All tests should be placed in the `test` directory.

#### Project Tree
Project tree should match the following structure:

```bash
.
├── WORK-INSTRUCTIONS.md
├── .git
│   ├── ...
├── .github
│   └── workflows
│       └── pylint.yml
├── .gitignore
├── img
│   ├── excellenteam.png
│   ├── scaleup.png
│   └── snakey_python.png
├── main.py
├── README.md
├── requirements.txt
├── src
│   ├── example.py
│   ├── ...
│   ├── ...
│   └── __pycache__
├── tests
│   ├── __pycache__
│   ├── ...
│   ├── ...
│   └── test_example.py
└── venv
    ├── bin
    ├── .gitignore
    ├── lib
    └── pyvenv.cfg
```
* `venv` directory should exist only on your local machine but not in the remote directory
* `...` notation stands for several files (might change from project to project, example files are just placeholders for examples)

## How to Submit an Exercise
You are required to submit each exercise using "GitHub Classroom". To do this, you must upload a link to your "GitHub Classroom" repository via Moodle.

### Pre-submission Checkup
1. Make sure you've answered all the questions.
2. Review and refactor your code for better readability (ideally, review your code one or two days later — sometimes it's better to review with fresh eyes).
3. Ensure that all intended files are uploaded to Git and follow the structure convention outlined in the [Repository Structure](#repository-structure) section.
4. Ensure that your code is running.
5. Once you open a PR, review the changes **carefully**. You can leverage GitHub's built-in diff viewer.
6. Wait and confirm that the linter test completed successfully. If the linter test fails, assess the errors and refactor accordingly — otherwise, each error will negatively impact your grade.
7. Upload the repository link to Moodle.
8. Good luck :)

<!-- Center Excellenteam image -->
<p align="center">
  <img src="./img/excellenteam.png" alt="Excellenteam">
</p>
