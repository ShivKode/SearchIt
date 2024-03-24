# file_searcher.py
import os
import time
import pandas as pd

class FileSearcher:
    def __init__(self):
        self.target_name = ""
        self.search_type = ""
        self.found_items = []

    def get_search_params(self):
        while True:
            self.target_name = input("Enter the name you want to search for: ")
            self.search_type = input("Do you want to search for a file or a folder? Enter 'file' or 'folder': ").lower()

            if self.search_type in ['file', 'folder']:
                break
            else:
                print("Invalid search type. Please enter 'file' or 'folder'.")

    def get_found_items(self):
        return self.found_items

    def search_items(self, start_path='C:\\'):
            total_items = 0
            for root, dirs, files in os.walk(start_path):
                total_items += len(files) if self.search_type == 'file' else len(dirs)

            bars_to_add = 0
            print("Searching... [", end="", flush=True)

            try:
                start_time = time.time()
                for root, dirs, files in os.walk(start_path):
                    if self.search_type == 'file':
                        items = files
                    elif self.search_type == 'folder':
                        items = dirs
                    else:
                        print("Invalid search type. Please enter 'file' or 'folder'.")
                        return

                    for item in items:
                        elapsed_time = time.time() - start_time
                        if elapsed_time > 5 * bars_to_add:
                            print("=", end="", flush=True)
                            bars_to_add += 1
                        if self.target_name.lower() in item.lower():
                            item_path = os.path.join(root, item)
                            self.found_items.append(item_path)

            except PermissionError as e:
                print(f"Permission error: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")

            print("] Done")
            end_time = time.time()
            search_duration = end_time - start_time
            print("\n----------Results----------")
            print(f"Search ended in {search_duration:.2f} seconds.")