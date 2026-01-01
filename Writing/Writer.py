import pandas as pd
import logging

logger = logging.getLogger(__name__)

class writer:
    def write_file(self, df: pd.DataFrame,file_path):
        try:
            cleaned_file = df
            cleaned_file.to_excel(file_path)
            logger.info('File is written')
        except PermissionError:
            logger.error('Excel file is still open. Please close it before writing to it.')
            raise PermissionError('Please close the excel file.')
        