# CRUD Operations with MySQL using Streamlit

This is a simple Python code that demonstrates the four CRUD (Create, Read, Update, and Delete) operations using MySQL database and Streamlit web framework.

## Requirements

* Python 3.6 or above
* Streamlit
* MySQL Connector

## Installation

You can install Streamlit and MySQL Connector using pip:

```bash
pip install streamlit mysql-connector-python
```

## Usage

* Create a MySQL database and table by running `database.sql` script provided in this repository.
* Replace the MySQL database credentials in `main()` function with your own database credentials.
* Run the script `app.py` using the following command:

```bash
streamlit run app.py
```

* Select an operation (Create, Read, Update, or Delete) from the dropdown list.
* Enter the required fields and click the respective button to perform the operation.

## License

This code is licensed under the [MIT License](https://github.com/your/your-repo/blob/main/LICENSE).