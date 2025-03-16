# paper-assortment
The `paper-assortment` project is designed to help manage and assign research papers to different members of a group using Google Sheets. This project uses the `gspread` library to interact with Google Sheets and automate the process of paper assignment.

## Features
- List all PDF papers in a specified directory.
- Assign papers to specific individuals in a Google Sheet.
- Automatically update the Google Sheet with the assigned papers.

## Setup

### Prerequisites
- Python 3.x
- Google Cloud Service Account with access to Google Sheets API

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/Armin-Hajibeygi/paper-assortment.git
    cd paper-assortment
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv env
    source env/bin/activate 
    ```

3. Install the required packages from `requirements.txt`:
    ```sh
    pip install -r requirements.txt
    ```

4. Place your `client_secret.json` file in the root directory of the project.

5. Ensure `client_secret.json` is added to `.gitignore` to prevent it from being committed to the repository.

## Usage

1. Set up your Google Sheet:
    - Create a Google Sheet named "LLM Group Paper Assignment".
    - Add worksheets for each person you want to assign papers to.

2. Modify the script parameters:
    - Update the `sheet_name` and `path` variables in `assign_cluster.py` to match your Google Sheet name and the directory containing your PDF papers.

3. Run the script:
    ```sh
    python assign_cluster.py
    ```
