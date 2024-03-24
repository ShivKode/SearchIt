# search_logger.py
import pandas as pd
import os

def save_to_excel(search_results):

    file_exists = os.path.isfile("search_log.xlsx")

    if file_exists:
        existing_df = pd.read_excel("search_log.xlsx")
        last_empty_row = existing_df.index[-1] + 2 if not existing_df.empty else 1

        for i, result in enumerate(search_results, start=last_empty_row):
            existing_df = existing_df._append(result, ignore_index=True)

        existing_df.to_excel("search_log.xlsx", index=False)
        print("Search results appended to existing file.")

        search_results.clear()

    else:
        
        df = pd.DataFrame(search_results, columns=["Timestamp", "Search Type", "Search Name", "Result"])
        df.to_excel("search_log.xlsx", index=False)
        print("New search log file created.")

        search_results.clear()