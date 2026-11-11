"""
Code to generate pandas df for the length of each audio file
and how to select them
"""

import pandas as pd

from language_detection.data.csv_tools.directory import (
    open_files, person_to_group,
    make_into_list, form_dataframe
)

from language_detection.data.audio import df_values
from language_detection.utils.io import check_path
from language_detection import config 

def main(lang):
    """
    Runs through main code
    """

    files = person_to_group(open_files(lang))

    location = f"{config.AUDIO_LOCATION}/{lang}/custom"

    name, person_data = files.popitem()

    df = form_dataframe(
        name,
        df_values(person_data, lang)
    )

    # start=1: row 0 already holds the popped speaker
    for i, (name, urls) in enumerate(files.items(), start=1):
        df.loc[i] = make_into_list(
            name,
            df_values(urls, lang)
        )

    check_path(location)
    df.to_csv(location + '/length.csv')

    print('Done')

if __name__ == '__main__':

    import sys

    # Pass languages on the command line, or default to all seven synthesized ones
    languages = sys.argv[1:] or ["de", "en", "es", "it", "ja", "nl", "ta"]

    for lang in languages:
        main(lang)

