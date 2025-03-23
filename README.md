# Detector: Neural Network

Find spectral lines in recorded data with the help of a neural network.

## Requirements:
 * Python >= 3.10,
 * `joblib`,
 * `numpy`,
 * `pandas`,
 * `pyqtgraph`,
 * `scipy`,
 * `scikit-learn`,
 * `PySide6-Essentials`.

### Instructions for developers

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
  
### Install from repository and run
* install: `pip install git+https://github.com/SkorEgor/Detector-Neural_network.git`
* run: `detect`
