import pandas as pd
import logging

logger = logging.getLogger(__name__)

class outliers:
    def remove_outliers_from_file(self, df: pd.DataFrame):
        processed_data = df.copy()

        # Calculating the boundaries for the temp outliers
        Temp_Q1 = processed_data['temperature_c'].quantile(0.25)
        Temp_Q3 = processed_data['temperature_c'].quantile(0.75)

        Temp_IQR = Temp_Q3 - Temp_Q1

        Temp_lower_bound = Temp_Q1 - 1.5 * Temp_IQR
        Temp_upper_bound = Temp_Q3 + 1.5 * Temp_IQR

        # Calculating the boundaries for the hum outliers
        Hum_Q1 = processed_data['humidity_pct'].quantile(0.25)
        Hum_Q3 = processed_data['humidity_pct'].quantile(0.75)
        Hum_IQR = Hum_Q3 - Hum_Q1

        Hum_lower_bound = Hum_Q1 - 1.5 * Hum_IQR
        Hum_upper_bound = Hum_Q3 + 1.5 * Hum_IQR

        # Creating columns for outliers
        processed_data['temp_is_outlier'] = ((processed_data['temperature_c'] > Temp_upper_bound )|(processed_data['temperature_c'] < Temp_lower_bound))
        processed_data['hum_is_outlier'] = ((processed_data['humidity_pct'] > Hum_upper_bound )|(processed_data['humidity_pct'] < Hum_lower_bound))

        # Removing outliers from clean data
        clean_data = processed_data[processed_data.temp_is_outlier == False]
        clean_data = clean_data[clean_data.hum_is_outlier == False]
        clean_data.pop('temp_is_outlier')
        clean_data.pop('hum_is_outlier')

        return clean_data