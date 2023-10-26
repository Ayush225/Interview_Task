# Interview_Task
## Problem Statement
Writing a python function which takes the date as an input and prints the settlement details table. So if a users provides a date as 20th Oct 2023 in the input, the script would print the contents of the table in the format(Month, Open, Close, …, Settle etc) for all the contracts (Oct 23, Nov 23, etc). The settlement details can vary from day to day for these contracts.

## Project Description
I had developrd a Python script that allows users to input a specific date, and the script will retrieve and display the settlement details for various futures contracts for that date. The settlement details typically include information such as the open price, close price, and settle price for different contracts, and these details can vary from day to day. For example, if a user provides a date like "20th Oct 2023" as input, the script will fetch and print the settlement data for contracts with delivery months like "Oct 23", "Nov 23", and so on.


## Screenshots
 Below screenshot shows the output of the script after manually providing date.
<p align="center">
<img src="https://github.com/Ayush225/Interview_Task/assets/66459226/401cbe80-3618-4240-b667-0363c803ac15" alt="this is the image description" >
</p>

## Built with

* I've used python Requests for sending HTTP GET Requests and BeautifulSoup to fetch and arrange json data.
