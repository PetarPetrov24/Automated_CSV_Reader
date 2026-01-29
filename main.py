from pathlib import Path
from reader import read_csv
from main_logic import process
from saver import save_csv

def run():
    input_file = Path("input/dummy_data.csv")
    output_file = Path("output/processed_data.csv")

    data_frame = read_csv(input_file)
    data_frame = process(data_frame)
    save_csv(data_frame, output_file)

    print("Automation complete")


if __name__ == "__main__":
    run()