# Automated User Provisioning and Deprovisioning Tool

## Project Description

This project implements a basic automated user provisioning and deprovisioning system. It simulates the process of creating and removing user accounts across different platforms (in this case, a simple text file simulator). This tool can be used as a foundation to integrate with more complex systems and services.

The project is designed to be a flexible and configurable way to automate user account lifecycle management.

## Features

*   **User Provisioning:** Reads user data from a CSV file and simulates creating new user accounts by adding them to a designated text file.
*   **User Deprovisioning:** Reads a list of users to remove from a CSV file and simulates removing user accounts by removing them from the designated text file.
*   **Command-Line Interface (CLI):**  Provides a simple and easy-to-use CLI for performing provisioning and deprovisioning actions.
*   **Logging:**  Provides informative log output to the terminal to track the process.
*   **Configurable Output:**  The target output file is configurable via CLI argument.
*   **Error Handling:**  Basic error handling (e.g., file not found) is implemented to ensure graceful exits.

## How to Run

### Prerequisites

*   Python 3.6 or higher
*   Basic knowledge of how to use a command line interface

### Setup

1.  Clone the repository to your local machine:
    ```bash
    git clone https://github.com/linuxtj/user-provisioning.git
    cd user-provisioning
    ```
2. (Optional) Create a virtual environment and install the required libraries (In this case there is not external libraries):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt #No requirements needed at the moment
    ```

### Usage

1.  **Prepare a CSV User File:** Create a CSV file named `users.csv` (or any name you prefer) with the following structure:

    ```csv
    username,email,role
    john.doe,john.doe@example.com,user
    jane.smith,jane.smith@example.com,admin
    ```
2.  **Provision Users:** Run the script with the `provision` action and the path to your CSV file:

    ```bash
    python user_provisioning.py provision --user-file users.csv
    ```

    This will add users to the `users.txt` file (by default) or to the specified output file using the `--output-file` parameter.
3.  **Deprovision Users:** Run the script with the `deprovision` action and the path to your CSV file:

    ```bash
    python user_provisioning.py deprovision --user-file users.csv
    ```
    This will remove users from the `users.txt` file (by default) or from the specified output file using the `--output-file` parameter.
4.  **Custom Output File:** Use the `--output-file` parameter to specify a different output file:

    ```bash
    python user_provisioning.py provision --user-file users.csv --output-file my_users.txt
    python user_provisioning.py deprovision --user-file users.csv --output-file my_users.txt
    ```

## Technologies Used

*   **Programming Language:** Python 3
*   **Standard Libraries:** `csv`, `argparse`, `logging`

## Author

[Oscar Tejada/linuxtj]

[MIT License]
