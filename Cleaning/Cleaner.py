import pandas as pd
import logging

logger = logging.getLogger(__name__)

class cleaner:
    def clean_data(self, df: pd.DataFrame):
        self.raw_data = df

        if not isinstance(self.raw_data, pd.DataFrame):
            logger.error('The file is not a DataFrame')

        # Preparing columns for data manipulation   
        self.raw_data.columns = (
            self.raw_data.columns
            .str.lower()
            .str.strip()
            .str.replace(' ','_')
        )
        # Preparing dataframe for data manipulation
        unprocessed_data = self.raw_data.dropna(how='all')

        unprocessed_data = unprocessed_data.copy()

        # column names
        Numeric_columns = ['temperature_c','humidity_pct','wind_speed_kmh','precipitation_mm','traffic_density_score','co2_ppm','no2_ppb','pm2.5','pm10']

        # Cleaning the data
        unprocessed_data['timestamp']=pd.to_datetime(unprocessed_data['timestamp'],errors='coerce')
        for col in Numeric_columns:
            unprocessed_data[col] = pd.to_numeric(unprocessed_data[col], errors='coerce')

        processed_data = unprocessed_data.dropna()
        removed_data = len(unprocessed_data['temperature_c']) - len(processed_data['temperature_c'])
        logger.info('The amount of rows that are removed: %s',removed_data)
        return processed_data
