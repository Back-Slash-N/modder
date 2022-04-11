
# GUI-launcher-for-portal-2-32PlayerMod

a GUI launcher for the portal 2: 32 players mod

This repo contains only the launcher for the mod if you want the full mod please visit [kyle's page](https://github.com/kyleraykbs/Portal2-32PlayerMod)

## Built With
- Python
- PyQt5
- and a lot of procrastination


## How to build

This project can be built theoretically on any OS that supports python 3

**-GUI launcher**
1. Clone the repo

2. Create a virtual python environment (Not needed but preferred)

	1. Create the virtual environment

		-  `python3 -m venv env`

	2. Activate the virtual environment

		- Windows: `.\env\Scripts\activate.bat`

		- Linux: `source ./env/bin/activate`

3. Download dependencies

	-  `pip install PyQt5`

	-  `pip install requests`

4. Run `src/MainWindow.py`

**-CLI launcher**

just run `src/cli.py`