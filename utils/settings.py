import sys
from pathlib import Path

if hasattr(sys, "_MEIPASS"):
    BASE_DIR = Path(getattr(sys, "_MEIPASS"))
else:
    BASE_DIR = Path(__file__).parent.parent.absolute()

ASSET_DIR = BASE_DIR.joinpath("assets")
IMAGE_DIR = ASSET_DIR.joinpath("images")

NAME = "SuperContinent"
VERSION = "2.2"
SERVER = "ws://127.0.0.1:7000"

TITLE = f"{NAME} v{VERSION}"
