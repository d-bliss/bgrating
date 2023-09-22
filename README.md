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

## License

This project is [MIT licensed](LICENSE).
