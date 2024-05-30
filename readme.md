# Inventory Management System

This is a simple inventory management system written in Python using Flask.

## Requirements

- Python 3.x
- Flask

## Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Create a virtual environment and activate it:

   ```sh
   pip install virtualenv
   virtualenv venv
   ```

   - **Windows**:

     ```sh
     venv\Scripts\activate
     ```

     For Windows, if this is your first time running the script, you might get an error like below:

     ```sh
     venv\Scripts\activate : File C:\flask_project\venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
     At line:1 char:1
     + venv\Scripts\activate
        + FullyQualifiedErrorId : UnauthorizedAccess
     ```

     This means that you don’t have access to execute the scripts.

     To solve this error, run PowerShell as admin. When you right-click on the PowerShell icon, choose the option ‘Run as administrator’. Now, PowerShell will open in admin mode.

     Type the following command in Shell:

     ```sh
     set-executionpolicy remotesigned
     ```

   - **Linux**:

     ```sh
     source ./venv/bin/activate
     ```

4. Install the requirements:

   ```sh
   pip install flask
   pip install db-sqlite3
   ```

5. Run the application:

   ```sh
   flask --app main run
   ```

## Endpoints

- **Add Item**: `POST /items`
- **View Items**: `GET /items`
- **Update Item**: `PUT /items/<id>`
- **Delete Item**: `DELETE /items/<id>`

## Data Format

### Add/Update Item

```json
{
  "name": "Item Name",
  "quantity": 10,
  "price": 19.99
}
```
