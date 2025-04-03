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
 * `PySide6-Essentials`,
 * `setuptools`,
 * `python-dotenv`.

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

---

## Installation

### Installation and Running via `pip` [Windows]

#### 1. Clone the repository
Clone the project from GitHub and navigate to the project directory:
```bash
git clone https://github.com/SkorEgor/Detector-Neural_network.git
cd Detector-Neural_network
```

#### 2. Create a virtual environment (optional but recommended)
Isolate project dependencies using a virtual environment:
```bash
python -m venv venv
```
Activate it:
```bash
venv\Scripts\activate
```
* After activation, you’ll see `(venv)` in your command prompt.
* To disable venv: `deactivate`
#### 3. Install the project
Install the project and its dependencies:
```bash
pip install .
```
The dot (`.`) refers to the current directory with `pyproject.toml`.

> **Note**: If you’re using `requirements.txt` instead, run `pip install -r requirements.txt`.

#### 4. Run the project
Launch the application:
```bash
run-detector
```
If the command isn’t recognized, ensure the virtual environment is active and the installation succeeded.

---

### Installation and Running via `pip` [Ubuntu]

#### 1. Clone the repository
Clone the project from GitHub and navigate to the project directory:
```bash
git clone https://github.com/SkorEgor/Detector-Neural_network.git
cd Detector-Neural_network
```

#### 2. Create a virtual environment (optional but recommended)
Isolate project dependencies using a virtual environment:
```bash
python3 -m venv venv
```
Activate it:
```bash
source venv/bin/activate
```
After activation, you’ll see `(venv)` in your terminal prompt.

#### 3. Install the project
Install the project and its dependencies (The dot `.` refers to the current directory with `pyproject.toml`):
```bash
pip install .
```
or if you’re using `requirements.txt` instead, run
```bash
pip install -r requirements.txt
```

#### 4. Run the project
Launch the application:
```bash
run-detector
```
or
```bash
python3 -m detector_neural_network.main
```
If you get a "command not found" error, verify that the virtual environment is activated and the installation completed successfully.

---

### Отличия и пояснения:
1. **Windows**: Используется `python` для создания виртуального окружения и `venv\Scripts\activate` для активации.
2. **Ubuntu**: Используется `python3` (в Ubuntu часто требуется явно указывать версию Python 3), а активация выполняется через `source venv/bin/activate`.
3. **Единообразие**: Оба раздела следуют одной структуре, но адаптированы под особенности ОС.
4. **Заметка про `requirements.txt`**: Добавлена в оба раздела для гибкости, если вы решите вынести зависимости.

Если нужно что-то ещё уточнить или добавить (например, зависимости вроде `libpq-dev` для Ubuntu), дайте знать!
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
