from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.absolute()
ASSET_DIR = BASE_DIR.joinpath("assets")
IMAGE_DIR = ASSET_DIR.joinpath("images")

NAME = "SuperContinent"
VERSION = "2.2"

TITLE = f"{NAME} v{VERSION}"
