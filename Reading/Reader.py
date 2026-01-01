import pandas as pd
import logging

logger = logging.getLogger(__name__)

class reader:
    def read_file(self, file: str):
        try:
            df = pd.read_csv(file)
            return df
        except FileNotFoundError:
            logger.error('File is not found in the folder given.')
            raise FileNotFoundError(f'File is not found in the folder given.')
        except Exception as e:
            logger.error('The following error occured: %s',e)
            raise Exception(f'The following error occured: {e}')
