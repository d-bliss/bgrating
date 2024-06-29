# V2 to V1 Rating Conversion Web App

This web app provides a visualization of the conversion from V2 Rating to V1 Rating using Plotly graphs, deployed on PythonAnywhere using Flask. This README includes instructions on how to set up and run the project locally using Visual Studio Code (VSCode).

## Local Setup and Installation

### Prerequisites
- Python (>=3.7 is recommended for compatibility)
- Visual Studio Code installed
- Basic knowledge of using the command line

### Instructions

1. **Clone the Repository**
   Open a terminal and run the following command to clone the repository to your local machine.
   ```sh
   git clone <repository-url> bgrating
   ```

2. **Navigate to the Project Directory**
   ```sh
   cd bgrating
   ```

3. **Create a Virtual Environment**
   ```sh
   python -m venv venv
   ```

4. **Activate the Virtual Environment**
   - **On Windows:**
     ```sh
     .\venv\Scripts\activate
     ```
   - **On macOS/Linux:**
     ```sh
     source venv/bin/activate
     ```

5. **Install the Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

6. **Open the Project in VSCode**
   ```sh
   code .
   ```
   Or, manually open VSCode and use the “Open Folder” option to open the `bgrating` directory.

7. **Run the App Locally**
   With the project open in VSCode, use the integrated terminal ensuring that the virtual environment is activated, and run:
   ```sh
   flask run
   ```
   The app should now be running locally at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Development

While developing, you can make use of VSCode’s features like debugging, Git integration, extensions, etc. When modifying the Python code or templates, Flask should automatically reload the app, reflecting the changes immediately.

Remember to test your changes thoroughly locally before deploying them to PythonAnywhere or any other hosting platform.

## Data Used

| Title                        | New Rating | Old Rating | Original Rating |
|------------------------------|------------|------------|-----------------|
| Galactic Master Level 3      | 3500       | 2600       |                 |
| Galactic Master Level 2      | 3250       | 2500       |                 |
| Galactic Master Level 1      | 3000       | 2400       | 3512            |
| Grandmaster Level 3          | 2700       | 2300       |                 |
| Grandmaster Level 2          | 2500       | 2200       |                 |
| Grandmaster Level 1          | 2350       | 2100       | 2841            |
| International Master Level 3 | 2250       | 2000       |                 |
| International Master Level 2 | 2150       | 1950       |                 |
| International Master Level 1 | 2050       | 1900       | 2394            |
| Master Level 3               | 1950       | 1870       |                 |
| Master Level 2               | 1850       | 1830       |                 |
| Master Level 1               | 1750       | 1800       | 2171            |
| Advanced Level 3             | 1700       | 1750       |                 |
| Advanced Level 2             | 1650       | 1700       |                 |
| Advanced Level 1             | 1600       | 1650       | 1835            |
| Intermediate Level 6         | 1567       | 1530       |                 |
| Intermediate Level 5         | 1533       | 1515       |                 |
| Intermediate Level 4         | 1500       | 1475       |                 |
| Intermediate Level 3         | 1467       | 1450       |                 |
| Intermediate Level 2         | 1433       | 1425       |                 |
| Intermediate Level 1         | 1400       | 1400       |                 |
| Rookie Level 9               | 1367       | 1367       |                 |
| Rookie Level 8               | 1333       | 1333       |                 |
| Rookie Level 7               | 1300       | 1300       |                 |
| Rookie Level 6               | 1267       | 1267       |                 |
| Rookie Level 5               | 1233       | 1233       |                 |
| Rookie Level 4               | 1200       | 1200       |                 |
| Rookie Level 3               | 1167       | 1167       |                 |
| Rookie Level 2               | 1133       | 1133       |                 |
| Rookie Level 1               | 1100       | 1100       |                 |
| Beginner Level 6             | 1067       | 1067       |                 |
| Beginner Level 5             | 1033       | 1033       |                 |
| Beginner Level 4             | 1000       | 1000       |                 |
| Beginner Level 3             | 967        | 967        |                 |
| Beginner Level 2             | 933        | 933        |                 |
| Beginner Level 1             | 900        | 900        |                 |


## License

This project is [MIT licensed](LICENSE).
