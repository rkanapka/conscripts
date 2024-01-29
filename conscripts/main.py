from conscripts.conscripts import Conscripts
from conscripts.data_processor import DataProcessor


def main() -> None:
    conscripts = Conscripts().get_conscripts()
    DataProcessor(conscripts).process_data()


if __name__ == "__main__":
    main()
