import pandas as pd
import os
import glob
import argparse


def combine(file_type, data_path):

    if file_type == 'excel':
        print("Processing Excel Files.")
        file_list = glob.glob(os.path.join(data_path, '*.xlsx'))
        combined_list = []
        for file in file_list:
            data = pd.read_excel(file)
            combined_list.append(data)
        concat_data = pd.concat(combined_list, ignore_index=True)
        concat_data.to_excel(os.path.join(data_path, "combined.xlsx"),
                             index=False)
    else:
        print("Processing CSV Files.")
        file_list = glob.glob(os.path.join(data_path, '*.csv'))
        combined_list = []
        for file in file_list:
            data = pd.read_csv(file, low_memory=False, iterator=True,
                               chunksize=1000)
            data_df = pd.concat(data, ignore_index=True)
            combined_list.append(data_df)
        concat_data = pd.concat(combined_list, ignore_index=True)
        concat_data.to_csv(os.path.join(data_path, "combined.csv"), index=False)


def main():

    parser = argparse.ArgumentParser(prog="COMBIT", usage="%(prog)s [options]",
                                     description="""Description: Combine CSV or
                                     Excel  files.""",
                         formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-f", "--filetype", help="CSV or Excel.",
                        default="csv")
    parser.add_argument("-d", "--directory", help="Path to the files.",
                        default=os.getcwd())

    args = parser.parse_args()

    result = combine(args.filetype, args.directory)

    print("Results exported.")


if __name__ == "__main__":
    main()
