from conscripts import Conscripts
from data_processor import DataProcessor


def main():
    conscripts = Conscripts().get_conscripts()
    DataProcessor(conscripts).process_data()

if __name__ == "__main__":
    main()
