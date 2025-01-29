[![Maintainability](https://api.codeclimate.com/v1/badges/ed619f783e5a0091eff0/maintainability)](https://codeclimate.com/github/Mirrasol/curr-api/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ed619f783e5a0091eff0/test_coverage)](https://codeclimate.com/github/Mirrasol/curr-api/test_coverage)

Currency Converter - a simple and easy to use REST API to check the latest global currency rates. It provides registered users with an access to the list of world currencies and allows them to convert from one currency to another. The project includes JWT authentication and integration with an external API for a real-time exchange.

## 1) Features

  - register and login to check the list of all available currencies
  - quickly convert one currency to another using the most recent exchange rate data

## 2) Installation

This project is built using FastAPI as the main framework. Please refer to the pyproject.toml file for the full list of required dependencies.

`git clone git@github.com:Mirrasol/Currency-Converter.git` - download the package from GitHub

`make install` - install using uv from your console 

or set your own virtual environment using pip and other package managers.

Don't for get to create the .env file that contains your secret keys:

`SECRET_KEY = enter_your_key`
`API_KEY = exchange_api_key` (from `https://apilayer.com/marketplace/currency_data-api`)
`ALGORITHM = choose_algorithm`

and database settings (example):

`DB_HOST = localhost`
`DB_PORT = 5432`
`DB_USER = username`
`DB_PASS = my_pass`
`DB_NAME = db_name`

Run the project using Uvicorn:

`uvicorn main:app`

or check Makefile for the list of the available commands.

## 3) Swagger Demo Screens

