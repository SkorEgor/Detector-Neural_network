# Detector: Neural Network

Find spectral lines in recorded data with the help of a neural network.

## Table of Contents
- [Requirements](#requirements)
- [Configuration Settings](#configuration-settings)
- [Instructions for Developers](#instructions-for-developers)
- [Installation](#installation)
  - [Installation and Running via `pip` (Windows)](#installation-and-running-via-pip-windows)
  - [Installation and Running via `pip` (Ubuntu)](#installation-and-running-via-pip-ubuntu)
  - [Installation and Running via Git URL (Windows)](#installation-and-running-via-git-url-windows)
  - [Installation and Running via Git URL (Ubuntu)](#installation-and-running-via-git-url-ubuntu)

## Requirements
- Python >= 3.10
- `joblib`
- `numpy`
- `pandas`
- `pyqtgraph`
- `scipy`
- `scikit-learn`
- `PySide6-Essentials`
- `setuptools`
- `python-dotenv`

## Configuration Settings

The application includes configurable settings defined in `settings.py`. These settings allow you to customize behavior, such as enabling debug mode, specifying default file paths, or adjusting parameters like the Savitzky-Golay filter window length. Variables are loaded with default values but can be overridden for flexibility.

### How to Set Variables
You can override default settings in two ways:
1. **Using a `.env` file**: Create a `.env` file in the project root and define variables (e.g., `DEBUG_ALL=True`). The application automatically loads these values.
2. **Environment Variables**: Set variables directly in your operating system's environment (e.g., `export DEBUG_ALL=True` on Ubuntu or `set DEBUG_ALL=True` on Windows) before running the application.

### List of Configurable Variables
Here’s an overview of some available settings:
- `DEBUG_ALL`: Enable/disable debug mode (default: `False`).
- `USE_DEFAULT_FILE_PATH_WITHOUT_SUBSTANCE`: Use default path for data without substance (default: `False`).
- `DEFAULT_FILE_PATH_WITH_SUBSTANCE`: Path to the default file with substance data.
- `SAVGOL_FILTER_WINDOW_LENGTH`: Window length for the Savitzky-Golay filter (default: `10`; set to `0` to disable).
- `ORGANIZATION`: Name of the organization (default: `"Institute for Physics of Microstructures RAS"`).
- And more...

For the full and up-to-date list of variables, refer to `settings.py` in the project root.

## Instructions for Developers
- **Edit the interface**: Use Qt Designer to modify `gui.ui`.
- **Convert UI to Python**: After editing `gui.ui`, generate `gui.py` with:
  ```bash
  pyside6-uic gui.ui -o gui.py
  ```
- **Update resources**: Convert `res.qrc` to `res_rc.py` using:
  ```bash
  pyside6-rcc.exe resources.qrc -o resources_rc.py
  ```
- **Linting**: Before submitting code, run the linter:
  ```bash
  ruff check .
  ```
  and format the code:
  ```bash
  ruff format
  ```

## Installation

### Installation and Running via `pip` (Windows)

#### 1. Clone the Repository
Clone the project from GitHub and navigate to the directory:
```bash
git clone https://github.com/SkorEgor/Detector-Neural_network.git
cd Detector-Neural_network
```

#### 2. Create a Virtual Environment (Optional but Recommended)
Set up a virtual environment:
```bash
python -m venv venv
```
Activate it:
```bash
venv\Scripts\activate
```
- After activation, `(venv)` will appear in your command prompt.
- To deactivate: `deactivate`

#### 3. Install the Project
Install the project and its dependencies (`.` refers to the current directory with `pyproject.toml`):
```bash
pip install .
```
Or, if using `requirements.txt`:
```bash
pip install -r requirements.txt
```

#### 4. Run the Project
Launch the application:
```bash
run-detector
```
Or:
```bash
python3 -m detector_neural_network.main
```
If the command isn’t recognized, ensure the virtual environment is active and the installation succeeded.

### Installation and Running via `pip` (Ubuntu)

#### 1. Clone the Repository
Clone the project from GitHub and navigate to the directory:
```bash
git clone https://github.com/SkorEgor/Detector-Neural_network.git
cd Detector-Neural_network
```

#### 2. Create a Virtual Environment (Optional but Recommended)
Set up a virtual environment:
```bash
python3 -m venv venv
```
Activate it:
```bash
source venv/bin/activate
```
- After activation, `(venv)` will appear in your terminal prompt.

#### 3. Install the Project
Install the project and its dependencies (`.` refers to the current directory with `pyproject.toml`):
```bash
pip install .
```
Or, if using `requirements.txt`:
```bash
pip install -r requirements.txt
```

#### 4. Run the Project
Launch the application:
```bash
run-detector
```
Or:
```bash
python3 -m detector_neural_network.main
```
If you get a "command not found" error, verify the virtual environment is activated and the installation completed successfully.

---

### Installation and Running via Git URL (Windows)

#### 1. Create a Virtual Environment
Optionally, you can create a directory. Set up a virtual environment:
```bash
python -m venv venv
```

#### 2. Activate It
Activate the virtual environment:
```bash
venv\Scripts\activate
```
- After activation, `(venv)` will appear in your command prompt.
- To deactivate: `deactivate`

#### 3. Install the Project from GitHub
Install the project directly from the GitHub URL:
```bash
python -m pip install git+https://github.com/SkorEgor/Detector-Neural_network.git
```

#### 4. Run the Project
Launch the application:
```bash
run-detector
```
If the command isn’t recognized, ensure the virtual environment is active and the installation succeeded.

---

### Installation and Running via Git URL (Ubuntu)

#### 1. Create a Virtual Environment
Optionally, you can create a directory
```bash
mkdir detector_neural_network
cd detector_neural_network
```
Set up a virtual environment:
```bash
python3 -m venv venv
```

#### 2. Activate It
Activate the virtual environment:
```bash
source venv/bin/activate
```
- After activation, `(venv)` will appear in your terminal prompt.

#### 3. Install the Project from GitHub
Install the project directly from the GitHub URL:
```bash
python3 -m pip install git+https://github.com/SkorEgor/Detector-Neural_network.git
```

#### 4. Run the Project
Launch the application:
```bash
run-detector
```
If you get a "command not found" error, verify the virtual environment is activated and the installation completed successfully.
