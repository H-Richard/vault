# vault

`vault` is a Python & MySQL powered password manager. The program generates a password of length 8+, containing atleast 1 numerical character, 1 special character and 1 alphabet character then stores it in a MySQL relation. Works with AWS Amazon RDS.


# Installation

## Dependencies

MySQL Server, `MySQL Connector`, and `pyperclip`

MySQL Server can be installed by visiting https://dev.mysql.com/downloads/mysql/

The rest can be installed through pip: i.e. `pip install pyperclip`

This program is written in Python3. The command line interface will soon be available as a pip package.

## Setup

You must have the following installed:

- MySQL Server (Tested for 8.0.*)

- MySQL Connector/Python (3.7) (Tested for 8.0.*)

After setting up your MySQL Server, load up config.json and change the file to match your credentials as follows:

```json
  {
    "host": "host",
    "user": "username",
    "passwd": "password"
  }
```

Then save and simply run ```python main.py```

![Setup](/img/setup.gif)

## Usage

The current program runs a CLI that will soon be available as a pip package! For now just use the input based action controller.


![Usage](/img/CRUD.gif)
