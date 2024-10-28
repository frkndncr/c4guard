# C4Guard - File Search Application

C4Guard is a web application that allows users to search for files in a specified directory and monitor system resource status. The project enables users to quickly and effectively find the files they need while also displaying the status of system resources (CPU, memory, and disk usage). Additionally, it includes VirusTotal integration to determine the threat status of found files.

## Features

- **File Search**: Allows users to search for files in specified directories.
- **Results List**: Detailed information about found files, including names, sizes, statuses, and threat levels.
- **System Status Monitoring**: Displays real-time CPU, memory, and disk usage.
- **VirusTotal Integration**: Checks the security status of found files.
- **User-Friendly Interface**: A modern and responsive design for an intuitive user experience.

## Requirements

The application works with the following software and libraries:

- **Python**: Version 3.6 or higher
- **Required Libraries**:
  - Flask: For web application development
  - aiohttp: Asynchronous HTTP client
  - beautifulsoup4: For parsing HTML and XML files
  - numpy: For numerical calculations
  - aiohappyeyeballs: For asynchronous DNS resolution

## How to Get Your VirusTotal API Key
  1. Go to the VirusTotal website.
  2. Create a free account or log in if you already have one.
  3. Navigate to your profile, where you will find your API key in the settings or account section.
  4. Copy the API key and paste it into the appropriate lines in the app.py and file_search_module.py files.

## Usage
  1. When the application opens, enter the directory you want to search in the "Root Directory" field (e.g., C:\Users\DELL\Desktop\).
  2. Enter the name of the file you are looking for in the "File Name" field (e.g., file.pdf).
  3. Click the "Search" button to start the search.
  4. The application will scan the specified directory and list the results in the "Results" section.
  5. The "System Status" section will display real-time information about system resource usage.

## Results Table
 1. The search results will be displayed in a table format, including file name, size (KB), status, threat level, and a link to VirusTotal.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/frkndncr/c4guard.git
   cd c4guard

2. **Install Required Libraries**:
   ```bash
   pip install -r requirements.txt

3. **Run the Application**:
   ```bash
   python app.py

4. **Uninstall Packages (Optional)**:
   ```bash
    python uninstall.py
