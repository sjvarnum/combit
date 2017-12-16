import pandas as pd
from pandas import DataFrame
import os
import glob
import argparse


def combine(file_type, data_path=os.getcwd()):
        
    if file_type == 'excel':
        file_list = glob.glob(os.path.join(data_path, '*.xlsx'))
        combined_list = []
        for file in file_list:
            data = pd.read_excel(file)
            combined_list.append(data)
        concat_data = pd.concat(combined_list, ignore_index=True)        
        concat_data.to_excel(os.path.join(data_path, "combined.xlsx"), index=False)
        print("Processing Excel Files.")    
    else:
        file_list = glob.glob(os.path.join(data_path, '*.csv'))
        combined_list = []
        for file in file_list:
            data = pd.read_csv(file, low_memory=False, iterator=True, chunksize=1000)
            data_df = pd.concat(data, ignore_index=True)
            combined_list.append(data_df)
        concat_data = pd.concat(combined_list, ignore_index=True)
        concat_data.to_csv(os.path.join(data_path, "combined.csv"), index=False)
        print("Processing CSV Files.")
        

def Main():
    
    parser = argparse.ArgumentParser("""This program will combine CSV or Excel files. You have the option of selecting 
    one or the other by including csv or excel as an argument. This is required.""")
    parser.add_argument("filetype", help="CSV or Excel (xlsx) files supported. Enter csv or excel.")
    parser.add_argument("-d", "--directory", help="""Path to the folder where the files you want to combine are located. 
    Defaults to the current working directory.""")   
      
    args = parser.parse_args()
    
    if args.directory:
        result = combine(args.filetype, args.directory)
    else:
        result = combine(args.filetype)      
    
        
    print("Results exported.")
    
    
if __name__ == "__main__":    
    Main()
