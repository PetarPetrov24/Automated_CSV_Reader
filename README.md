# AUTOMATED CSV READER

This project can read CSV files, process them, and finally save the result.  
It doesn't overwrite the original files; instead, it creates a copy with the new results.
<br>
<br>
Sources, that you can get CSV data from: Excel, Databases, Google Sheets, LibreOffice, Web/API's or Text files.

# Main idea of the project
Input file  -->  Read  -->  Process  -->  Save

## Project Structure

The CSV Reader contains four Python files:

- **reader.py** – reads CSV files
- **main_logic.py** – processes the data
- **saver.py** – saves the processed data
- **main.py** – connects all logic into one script

## Library Used

This project uses **Pandas**, a fast, powerful, and open-source library for:

- data manipulation: Fix mistakes, remove duplicates, handle missing values
- data cleaning: Change, add, remove, or reshape data
- data analysis: Explore data to find patterns, insights, summaries

Pandas efficiently handles structured data using two primary data structures:

- **Series** – 1D data  
- **DataFrame** – 2D tables  

It allows users to import, manipulate, filter, and merge data easily.

## Run the project
- Simply write in the terminal this command: python main.py

## Tech Stack

- **Language:** Python  
- **Library:** Pandas

