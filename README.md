# Detector: Neural Network

Find spectral lines in recorded data with the help of a neural network.

## Content
- [Requirements](#requirements)
- [Instructions for developers](#instructions-for-developers)
- [Installation](#installation)

## Requirements:
 * Python >= 3.10,
 * `joblib`,
 * `numpy`,
 * `pandas`,
 * `pyqtgraph`,
 * `scipy`,
 * `scikit-learn`,
 * `PySide6-Essentials`.

## Instructions for developers

* Edit the interface in Qt Designer using `gui.ui`.
* After changes in `gui.ui`, convert it to `gui.py` with:  
    ```bash
    pyside6-uic gui.ui -o gui.py
    ```  
* To update resources, convert `res.qrc` to `res_rc.py` using:  
    ```bash
    pyside6-rcc.exe resources.qrc -o resources_rc.py
    ```
* Before submitting code, run the linter
  ```bash
  ruff check .
  ```
  and
    ```bash
  ruff format
  ```

## Installation
### Installation and Running via `pip`

#### 1. Clone the repository
```bash
git clone https://github.com/SkorEgor/Detector-Neural_network.git
cd Detector-Neural_network    
```

#### 2. Create a virtual environment (optional)
```bash
python -m venv venv
```
Activate it (if it doesn’t activate automatically):
- On Windows:
```bash
venv\Scripts\activate
```
- On Linux/Mac:
```bash
source venv/bin/activate
```

#### 3. Install the project
```bash
pip install .
```
The dot (`.`) refers to the current directory where `pyproject.toml` is located.

#### 4. Run the project
```bash
run-detector
```

### Installation and Running via `Git URL`

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

2. **Activate it:**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

3. **Install the project from GitHub:**
   ```bash
   python -m pip install git+https://github.com/SkorEgor/Detector-Neural_network.git
   ```

4. **Run the project:**
   ```bash
   run-detector
   ```
