<p align="center">
    <img src="LLM_CLI.png" alt="Logo" width="160" height="160">
</p>

# LLM CLI

This project is made for a **Lalamove challenge** . It is a command-line interface that emulates Lalamove. 

## Technology choices
### Programming language: Python 3
### Database: MongoDB (NoSQL)
### Other: Shell script

## Structure
1. `my_llm/llm_cli.py`
    - File with `Order` class and functions to create/list/take orders connected to MongoDB. 
2. `my_llm/config.py`
    - File with MongoDB details.
3. `my_llm/llm_handler.py`
    - Handles command-line arguments.
4. `llm_test.py`
    - Test file for `llm_cli.py` for `create_order(from, to)`, `take_order(id)`, `list_orders` functions.
5. `llm`
    - Shell script to execute python program as a command-line command .`llm`.
6. `requirements.txt`
    - Specifies what Python packages required to run the project.
7. `setup.sh` 
    - Shell script for setting up project.
    - Creates and activates virutal environment, downloads requirements,and enables `llm` to be run from terminal.
## Setting up
```bash
source setup
```

## Commands
### `create_order [to] [from]`
CLI command to create order using [to] and [from] arguments.

```bash
create_order "Hong Kong Island" "Tai Po Market"
```

### `list_order`
CLI command to list all orders in database.
```bash
list_orders
```

### `take_order [id]`
CLI command to take an order from existing orders.
```bash
take_order  60a8d2b3e5a13d5fae066a12
```

## Example:
```
$ llm create_order "Polyu" "Sheck O Beach" 
60aa5cade4a8b928b3c4e1be is placed
$ lm list_orders
60a90d20f1533901c27fc9b2, HK, Shatin
60a910c3bb33166840b17dfa, Hong Kong Island, Mong Kok
$ llm take_order 60a90d20f1533901c27fc9b2
"60a90d20f1533901c27fc9b2" is successfully taken
$ llm take_order 60a90d20f1533901c27fc9b2
order "60a90d20f1533901c27fc9b2" already taken
$ llm take_order 60a90d20f1533901c27fc933
order "60a90d20f1533901c27fc933" does not exist
```

## Testing
Run the `llm_test` to test the file and run 4 test cases:
```bash
python llm_test.py
```
