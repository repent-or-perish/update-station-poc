# Update Station (Proof of concept)

Update Station is a GTK-based application for managing software update settings on GhostBSD. This application allows users to configure how often the system checks for updates.

This provides a wireframe for defining a basic look and feel of the app.

## Features

- Configure automatic update check frequency (Daily, Weekly, Now)
- Revert settings to default values
- Save settings

## Installation

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Install Dependencies

To install the required dependencies, run:

```
pip install -r requirements.txt
```

### Running the Application

To launch the Update Station application, navigate to the project directory and run:

```
python update_ui.py
```

## Project Structure

```
update-station/
│
├── config/
│   └── update_settings.json  # Configuration file for storing update settings
├── update_logic.py           # Business logic for managing update settings
├── update_ui.py              # UI logic creating the GTK application and interfacing with update_logic.py
├── README.md                 # Project documentation
└── requirements.txt          # List of dependencies required to run the application
```

- `update_logic.py`: Contains the business logic for managing update settings.
- `update_ui.py`: Contains the UI logic, creating the GTK application and interfacing with `update_logic.py`.
- `config/`: Directory to store configuration files.
  - `update_settings.json`: JSON file used to persist user settings.
- `README.md`: Project documentation.
- `requirements.txt`: List of dependencies required to run the application.

## Configuration File

The `config/update_settings.json` file stores the user settings in JSON format. Here is an example of the file content:

```
{
    "auto_check": "Daily"
}
```

## Usage

1. **Install dependencies**: Ensure that all dependencies are installed by running `pip install -r requirements.txt`.
2. **Run the application**: Execute `python update_ui.py` to start the Update Station application.
3. **Configure settings**: Use the application to set how often the system checks for updates (Daily, Weekly, Now).
4. **Revert settings**: Click the "Revert" button to reset the settings to their default values.
5. **Save settings**: The settings are automatically saved when the application is closed.

## Dependencies

- PyGObject

To install PyGObject, you can include it in the `requirements.txt` file:

```
PyGObject
```

