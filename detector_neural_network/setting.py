import os
from dotenv import load_dotenv

load_dotenv()
MODULE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG_ALL: bool = os.getenv("DEBUG_ALL", "False").lower() == "true"
USE_DEFAULT_FILE_PATH_WITHOUT_SUBSTANCE: bool = (
    os.getenv("USE_DEFAULT_FILE_PATH_WITHOUT_SUBSTANCE", "False").lower() == "true"
)
USE_DEFAULT_FILE_PATH_WITH_SUBSTANCE: bool = (
    os.getenv("USE_DEFAULT_FILE_PATH_WITH_SUBSTANCE", "False").lower() == "true"
)
USE_DEFAULT_FILE_PATH_NEURAL_NETWORK: bool = (
    os.getenv("USE_DEFAULT_FILE_PATH_NEURAL_NETWORK", "False").lower() == "true"
)
DEFAULT_FILE_PATH_WITHOUT_SUBSTANCE: str = os.path.join(MODULE_DIR, "data", "example_spectrum", "without_substance.csv")
DEFAULT_FILE_PATH_WITH_SUBSTANCE: str = os.path.join(MODULE_DIR, "data", "example_spectrum", "with_substance.csv")
DEFAULT_FILE_PATH_NEURAL_NETWORK: str = os.path.join(MODULE_DIR, "data", "example_neural_network", "5_new.joblib")
SAVGOL_FILTER_WINDOW_LENGTH: int = int(os.getenv("SAVGOL_FILTER_WINDOW_LENGTH", 10))  # Если 0, то фильтр выключен
ORGANIZATION: str = "Institute for Physics of Microstructures RAS"
APPLICATION: str = "Detector - Neural_network"
