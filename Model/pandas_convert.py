import json
import pandas as pd


class DataConverter:
    def __init__(self, data_file) -> None:
        self.data = data_file

    def convert_json_to_pandas(self):
        """Read json file and convert it to a Pandas dataframe object.

        Returns:
            [Pandas dataframe]: Pandas dataframe object
        """
        with open(self.data) as obj:
            data = json.load(obj)

        df = pd.DataFrame(data.values())
        df[["Broj soba", "Broj parkirnih mjesta"]] = df[["Broj soba", "Broj parkirnih mjesta"]].apply(pd.to_numeric)
        df.Cijena = df.Cijena.map(lambda element: int(element.replace(".", "")))
        df["Stambena površina"] = df["Stambena površina"].map(
            lambda element: element.replace(".", "").replace(",", ".").split("m")[0])
        df["Površina okućnice"] = df["Površina okućnice"].map(
            lambda element: element.replace(".", "").replace(",", ".").split("m")[0])
        df[["Stambena površina", "Površina okućnice"]] = df[["Stambena površina", "Površina okućnice"]].apply(
            pd.to_numeric)
        df["Pogled na more"] = pd.to_numeric(df["Pogled na more"].replace("Da", "1"))
        df = df.drop_duplicates()
        return df

    def english_translation(self, df):
        """Creates an english translation of columns in Pandas dataframe.

        Args:
            df (Pandas dataframe): Pandas dataframe object
        Returns:
            df (Pandas dataframe): Pandas dataframe object with translated columns.
        """
        croatian = list(df.columns)
        english = ["Location", "Num_of_rooms", "Area_indoor", "Area_outdoor", "Parking", "Seaview", "Price"]
        translate = {}
        for i, column in enumerate(croatian):
            translate[str(column)] = english[i]
        df = df.rename(columns=translate)
        return df

    def give_excel(self, language):
        """Writes Pandas dataframe to an excel file.

        Args:
            language (string): Language choice passed as a string (i.e. "english")
        """
        language = language.lower()
        if language == "english":
            self.english_translation(self.convert_json_to_pandas()).to_excel("data_{}.xlsx".format(language),
                                                                             index=False)
        elif language == "croatian":
            self.convert_json_to_pandas().to_excel("data_{}.xlsx".format(language), index=False)
