import datetime
from collections.abc import KeysView
from types import MappingProxyType

import pandas as pd


class DataProcessor:
    column_renames: MappingProxyType = MappingProxyType(
        {
            "pos": "Eil. numeris",
            "number": "Karo prievolininko kodas",
            "name": "Vardas",
            "lastname": "Pavardė",
            "bdate": "Gimimo metai",
            "department": "Departamentas",
            "info": "Šaukimo eiga ir nurodymai",
        }
    )
    start_row_values: tuple = (0, 0, 0, 13, 13, 13, 26)
    start_col_values: tuple = (0, 4, 8, 0, 4, 8, 0)
    file_name: str = "conscripts.xlsx"
    sheet_1_name: str = "Pagal miestus"
    sheet_2_name: str = "Šauktinių sąrašas"

    def __init__(self, data: dict) -> None:
        self.data = data
        self.cities: KeysView = data.keys()
        self.conscripts: list = [
            resp for responses_vals in data.values() for resp in responses_vals
        ]

    def process_data(self) -> None:
        with pd.ExcelWriter(self.file_name, engine="xlsxwriter") as writer:
            self.process_conscripts_in_each_city_by_age(writer)
            self.process_all_conscripts_by_age(writer)
            self.process_list_of_conscripts(writer)

    def process_conscripts_in_each_city_by_age(self, writer) -> None:
        for city, start_row, start_col in zip(
            self.cities, self.start_row_values, self.start_col_values
        ):
            conscripts_in_city_by_age_df = self.group_by_age(city=city)
            conscripts_in_city_by_age_df.to_excel(
                writer,
                sheet_name=self.sheet_1_name,
                startrow=start_row,
                startcol=start_col,
            )

    def process_all_conscripts_by_age(self, writer: pd.ExcelWriter) -> None:
        total_conscripts_by_age_df = self.group_by_age(use_conscripts_data=True)
        total_conscripts_by_age_df.to_excel(
            writer,
            sheet_name=self.sheet_1_name,
            startrow=self.start_row_values[-1],
            startcol=self.start_col_values[-1],
        )

    def process_list_of_conscripts(self, writer: pd.ExcelWriter) -> None:
        conscripts_df = pd.DataFrame(self.conscripts).rename(
            columns=self.column_renames
        )
        conscripts_df.to_excel(
            writer, sheet_name=self.sheet_2_name, startrow=0, startcol=0
        )

    def group_by_age(
        self, city: str | None = None, use_conscripts_data: bool = False
    ) -> pd.DataFrame:
        format_percent = "{:.02f}%".format
        current_year = datetime.datetime.now().year

        if city is None and not use_conscripts_data:
            raise ValueError(
                "You must pass city or use_conscripts_data boolean flag to method."
            )

        if use_conscripts_data:
            df = pd.DataFrame(self.conscripts).rename(columns=self.column_renames)
            city = "Viso"
        else:
            df = pd.DataFrame(self.data[city]).rename(columns=self.column_renames)

        df_grouped_by_age = df.groupby(
            df["Gimimo metai"].map(lambda x: f"{x} ({current_year-int(x)} m.)")
        )
        df_count_by_age = df_grouped_by_age[["Eil. numeris"]].count()
        df_by_age_renamed = df_count_by_age.rename(
            columns={"Eil. numeris": "Šauktinių sk."}
        )
        df_by_age_renamed["%"] = (
            df_by_age_renamed["Šauktinių sk."] / df.shape[0] * 100
        ).map(format_percent)
        df_by_age_renamed.loc["Viso", "Šauktinių sk."] = df_by_age_renamed[
            "Šauktinių sk."
        ].sum()
        df_by_age_renamed.columns = pd.MultiIndex.from_product(
            [[city], df_by_age_renamed.columns]
        )
        return df_by_age_renamed
