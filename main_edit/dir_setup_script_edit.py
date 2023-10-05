# IMPORTS
import os
from datetime import datetime


# PROCESS
def setup():

    print(f"at {str(datetime.today())}|: starting setup process")

    # initial path setup
    os.mkdir("C:\\Users\\Public\\pricempire_web_scraper")

    # daily_saves
    os.mkdir("C:\\Users\\Public\\pricempire_web_scraper\\[0]daily_saves")
    os.mkdir("C:\\Users\\Public\\pricempire_web_scraper\\[0]daily_saves\\[0-1]only_cases")
    os.mkdir("C:\\Users\\Public\\pricempire_web_scraper\\[0]daily_saves\\[0-2]normal")

    # result files
    os.mkdir("C:\\Users\\Public\\pricempire_web_scraper\\[1]result_files")

    # log files
    os.mkdir("C:\\Users\\Public\\pricempire_web_scraper\\[2]log_files")

    # any run saves
    os.mkdir("C:\\Users\\Public\\pricempire_web_scraper\\[3]any_run_saves")

    # exception saves
    os.mkdir("C:\\Users\\Public\\pricempire_web_scraper\\[4]exception_saves")

    # main run
    os.mkdir("C:\\Users\\Public\\pricempire_web_scraper\\main_run")

    # if needed setup code files as executables
    if setup_code_executables == "y":

        # create run directory
        os.mkdir("C:\\Users\\Public\\pricempire_web_scraper")

        # create the executables



