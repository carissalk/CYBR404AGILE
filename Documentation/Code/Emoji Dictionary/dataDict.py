

"""Data containing all current emoji
   Extracted from https://unicode.org/Public/emoji/latest/emoji-test.txt
   and https://www.unicode.org/Public/UCD/latest/ucd/emoji/emoji-variation-sequences.txt
   See utils/get_codes_from_unicode_emoji_data_files.py

   +----------------+-------------+------------------+-------------------+
   | Emoji Version  |    Date     | Unicode Version  | Data File Comment |
   +----------------+-------------+------------------+-------------------+
   | N/A            | 2010-10-11  | Unicode 6.0      | E0.6              |
   | N/A            | 2014-06-16  | Unicode 7.0      | E0.7              |
   | Emoji 1.0      | 2015-06-09  | Unicode 8.0      | E1.0              |
   | Emoji 2.0      | 2015-11-12  | Unicode 8.0      | E2.0              |
   | Emoji 3.0      | 2016-06-03  | Unicode 9.0      | E3.0              |
   | Emoji 4.0      | 2016-11-22  | Unicode 9.0      | E4.0              |
   | Emoji 5.0      | 2017-06-20  | Unicode 10.0     | E5.0              |
   | Emoji 11.0     | 2018-05-21  | Unicode 11.0     | E11.0             |
   | Emoji 12.0     | 2019-03-05  | Unicode 12.0     | E12.0             |
   | Emoji 12.1     | 2019-10-21  | Unicode 12.1     | E12.1             |
   | Emoji 13.0     | 2020-03-10  | Unicode 13.0     | E13.0             |
   | Emoji 13.1     | 2020-09-15  | Unicode 13.0     | E13.1             |
   | Emoji 14.0     | 2021-09-14  | Unicode 14.0     | E14.0             |
   | Emoji 15.0     | 2022-09-13  | Unicode 15.0     | E15.0             |
   | Emoji 15.1     | 2023-09-12  | Unicode 15.1     | E15.1             |

                  http://www.unicode.org/reports/tr51/#Versioning

"""

__all__ = [
    'EMOJI_DATA', 'STATUS', 'LANGUAGES'
]

component = 1
fully_qualified = 2
minimally_qualified = 3
unqualified = 4

STATUS = {
    "component": component,
    "fully_qualified": fully_qualified,
    "minimally_qualified": minimally_qualified,
    "unqualified": unqualified
}

LANGUAGES = ['en', 'es', 'ja', 'ko', 'pt', 'it', 'fr', 'de', 'fa', 'id', 'zh', 'ru', 'tr', 'ar']






import pandas as pd
import os

#-------------------------------------------------------
# THE BELOW CODE WILL CONVERT THE UNICODE TO EMOJI IN THE CSV
#-------------------------------------------------------
# Create a new dictionary that contains the Unicode and the 'en' value for each emoji (may convert to emoji in csv)

en_data = {}
for unicode, emoji_dict in EMOJI_DATA.items():
    if 'en' in emoji_dict:
        en_data[unicode] = emoji_dict['en']

# Convert the new dictionary into a DataFrame
en_df = pd.DataFrame(list(en_data.items()), columns=['Unicode', 'English Name'])

# Lowercase every English name and remove colons
en_df['English Name'] = en_df['English Name'].str.lower().str.replace(':', '') #.str.replace('_', ' ')

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the full path of the CSV file
csv_path = os.path.join(script_dir, 'updatedDict.csv')

# Write the DataFrame to a CSV file
en_df.to_csv(csv_path, index=False)