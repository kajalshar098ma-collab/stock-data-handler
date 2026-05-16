# stock_company_selector_full.py

# Install first:
# pip install yfinance pandas matplotlib

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


class StockSelector:

    def __init__(self):
        self.company_list = {
            "1": ("Apple", "AAPL"),
            "2": ("Microsoft", "MSFT"),
            "3": ("Tesla", "TSLA"),
            "4": ("Google", "GOOGL"),
            "5": ("Amazon", "AMZN"),
            "6": ("Meta", "META"),
            "7": ("Netflix", "NFLX"),
            "8": ("Nvidia", "NVDA"),
            "9": ("Intel", "INTC"),
            "10": ("AMD", "AMD")
        }

    # ===================================
    # Show Company List
    # ===================================
    def show_menu(self):
        print("\n========== STOCK MENU ==========")

        for key, value in self.company_list.items():
            print(f"{key}. {value[0]} ({value[1]})")

        print("0. Exit")

    # ===================================
    # Get User Choice
    # ===================================
    def choose_company(self):
        while True:
            self.show_menu()
            choice = input("\nEnter company number: ")

            if choice == "0":
                print("Thank You")
                break

            elif choice in self.company_list:
                company_name, ticker = self.company_list[choice]
                self.show_stock_data(company_name, ticker)

            else:
                print("Invalid Choice. Try Again.")

    # ===================================
    # Show Stock Data
    # ===================================
    def show_stock_data(self, company_name, ticker):
        print(f"\nLoading {company_name} Data...\n")

        stock = yf.Ticker(ticker)
        info = stock.info

        print("========== LIVE DATA ==========")
        print("Company Name   :", company_name)
        print("Ticker Symbol  :", ticker)
        print("Current Price  :", info.get("currentPrice"))
        print("Open Price     :", info.get("open"))
        print("High Price     :", info.get("dayHigh"))
        print("Low Price      :", info.get("dayLow"))
        print("Previous Close :", info.get("previousClose"))
        print("Volume         :", info.get("volume"))
        print("Market Cap     :", info.get("marketCap"))
        print("52W High       :", info.get("fiftyTwoWeekHigh"))
        print("52W Low        :", info.get("fiftyTwoWeekLow"))

        self.show_historical_data(stock)
        self.save_csv_option(stock, ticker)
        self.plot_graph(stock, company_name)

    # ===================================
    # Historical Data
    # ===================================
    def show_historical_data(self, stock):
        print("\n========== LAST 7 DAYS DATA ==========")

        hist = stock.history(period="7d")
        print(hist)

    # ===================================
    # Save CSV
    # ===================================
    def save_csv_option(self, stock, ticker):
        ans = input("\nSave data to CSV? (y/n): ")

        if ans.lower() == "y":
            df = stock.history(period="1mo")

            filename = f"{ticker}_stock_data.csv"
            df.to_csv(filename)

            print("Saved as:", filename)

    # ===================================
    # Plot Graph
    # ===================================
    def plot_graph(self, stock, company_name):
        ans = input("Show graph? (y/n): ")

        if ans.lower() == "y":
            df = stock.history(period="1mo")

            plt.figure(figsize=(10, 5))
            plt.plot(df.index, df["Close"], marker='o')
            plt.title(f"{company_name} Stock Price (1 Month)")
            plt.xlabel("Date")
            plt.ylabel("Closing Price")
            plt.grid(True)
            plt.show()


# ===================================
# MAIN PROGRAM
# ===================================
if __name__ == "__main__":
    app = StockSelector()
    app.choose_company()