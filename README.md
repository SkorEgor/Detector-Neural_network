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
 * `PyQt5`, `PyQt6`, or `PySide6-Essentials`.

If you have several Qt bindings installed,
one of them will be used automatically.
If you'd like to have a specific flavor to use,
provide its name in the `PYQTGRAPH_QT_LIB` environment variable (case-sensitive!).

### Instructions for developers

* Edit the interface in Qt Designer using `gui.ui`.
* After changes in `gui.ui`, convert it to `gui.py` with:  
    ```bash
    pyuic6 gui.ui -o gui.py
    ```  
* To update resources, convert `res.qrc` to `res_rc.py` using:  
    ```bash
    pyside6-rcc res.qrc -o res_rc.py
    ```
* Before submitting code, run the linter
  ```bash
  ruff check .
  ```
  and
    ```bash
  ruff format
  ```