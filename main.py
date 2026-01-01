from reading.Reader import reader
from cleaning.Cleaner import cleaner
from cleaning.Outliers import outliers
from aggregating.Aggregater import aggregater
from writing.Writer import writer
from pathlib import Path
import logging

logging.basicConfig(
filename="Data_Cleaning_SmartCity.log",
level=logging.DEBUG,
format="%(asctime)s - %(levelname)s - %(message)s"
)

BASE_DIR = Path(__file__).resolve().parent

# Reader is called
raw_data = reader()
raw_data = raw_data.read_file(BASE_DIR)

# Cleaner is called
clean_data = cleaner()
clean_data = clean_data.clean_data(raw_data)

# Outliers is called
processed_data = outliers()
processed_data = processed_data.remove_outliers_from_file(clean_data)

# Aggregater is called
agg = aggregater()

data_minmax = agg.aggregation_minmax(processed_data)
data_mean = agg.aggregation_mean(processed_data)

write_data = writer()
write_data.write_file(processed_data,'C:/Users/Tessa/Data_Cleaning_SmartCity/data/processed_data/processed_data.xlsx')
write_data.write_file(data_minmax,'C:/Users/Tessa/Data_Cleaning_SmartCity/data/processed_data/MinMax_data.xlsx')
write_data.write_file(data_mean,'C:/Users/Tessa/Data_Cleaning_SmartCity/data/processed_data/mean_data.xlsx')

#agg.plot_raw()
agg.plot_mean()



