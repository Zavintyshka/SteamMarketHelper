# Steam Market Helper

Steam Market Helper allows you to quickly create a comprehensive table of all your transactions on the Steam
marketplace. The generated table is saved as a JSON file, which can be used in other applications or converted into a
different format as needed.
<img width="1280" alt="header" src="https://github.com/Zavintyshka/SteamMarketHelper/assets/116081113/31a0f07f-00f7-49a1-8993-387f6cde34d9">


[Link to PyPI](https://pypi.org/project/steammarkethelper/)

# Setup

## I. Setting Up a Virtual Environment

To get started, install the package in a virtual environment:

```bash
python3 -m venv venv
source ./venv/bin/activate
(venv) pip install steammarkethelper 
```

### Setting Up Cookies

To use the package, you need to set up a `cookie` in the root folder of your project in a `.env` file. The `cookie`
contains information about your session, which is necessary to identify your account and interact with Steam's internal
API to retrieve your market data.

#### Obtaining the Cookie

To extract the `cookie`, log into your Steam account through a browser and navigate to your transaction history. Open
the network tab in the browser's developer tools and find the request to the internal Steam API. The request URL will
look like `.../render/?query=&start=x&count=10`. Copy the `Cookie` parameter from the request header.

Now, add the `cookie` to the `.env` file:

```plaintext
# .env
cookie="your_cookie"
```

## II. Using Steam Market Helper

The application provides a user-friendly CLI tool to quickly gather and process information retrieved from Steam's
servers.

### Initializing Data
<img width="767" alt="init" src="https://github.com/Zavintyshka/SteamMarketHelper/assets/116081113/b2e0652a-43d4-4b11-a6f0-350681c9860d">

To initialize the data, use the following command:

```bash
smh init PATH 
```

The `smh init` command supports several options:

```bash
  -d, --delay   Set delay between API calls
  --test        Enable test mode
  --no-log      Disable logging
```

### Generating the Table

To present the JSON file as a table, use the `smh getlist` command. This command formats the data into a readable table,
allowing sorting and filtering of transaction types. Supported options include:

```bash
      -p, --path TEXT                 Path to item data in JSON file
      -d, --delay INTEGER             Set delay between API calls
      --no-cached                     Do not use local files
      --test                          Enable test mode (retrieve one page)
      -tt, --transaction-type [sale|purchase|listing|operation_canceled|all]
      -f, --filter [item_name|item_type|price|no_filter]
      -o, --order [desc|asc]
      -t, --title TEXT                Set custom title for table
      --stats                         Get additional statistics
```

## III. Usage Examples

```bash
smh init ./data/my_data.json # Initialize JSON file in the current directory
smh getlist -p ./data/my_data.json # Display the table in the terminal
smh getlist --no-cached --test # Retrieve a small amount of data from Steam API
smh getlist -p ./data/my_data.json -tt sale --filter price --order desc --title "My Recent Sales" --stats > my_sales.txt
# Save the table to my_sales.txt, containing all sales sorted by price.
```
<img width="671" alt="getlist_with_parameters" src="https://github.com/Zavintyshka/SteamMarketHelper/assets/116081113/1b2ad0f7-f88a-4069-8149-d80afc1b653b">
