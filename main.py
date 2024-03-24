# main.py
import os
import time
from file_searcher import FileSearcher
from search_logger import save_to_excel

if __name__ == "__main__":
    search_results = []

    while True:
        print('''
                        ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗    ██╗████████╗██╗██╗
                        ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║    ██║╚══██╔══╝██║██║
                        ███████╗█████╗  ███████║██████╔╝██║     ███████║    ██║   ██║   ██║██║
                        ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║    ██║   ██║   ╚═╝╚═╝
                        ███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║    ██║   ██║   ██╗██╗
                        ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝   ╚═╝   ╚═╝╚═╝
        ''')

        file_searcher = FileSearcher()
        file_searcher.get_search_params()
        file_searcher.search_items()
        found_items = file_searcher.get_found_items()

        if found_items:
            item_type = file_searcher.search_type

            if len(found_items) == 1:
                print(f"\nFound 1 {item_type}:")
            else:
                print(f"\nFound {len(found_items)} {item_type}s:")

            for item_path in found_items:
                print(item_path)

            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            search_results.append({
                "Timestamp": timestamp,
                "Search Type": file_searcher.search_type,
                "Search Name": file_searcher.target_name,
                "Result": found_items
            })

            save_to_excel(search_results)

        else:
            print(f"\nNo {file_searcher.search_type}s found.")

        repeat = input("Do you want to perform another search? (y/n): ").lower()
        if repeat == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')

        if repeat == 'n':
            break