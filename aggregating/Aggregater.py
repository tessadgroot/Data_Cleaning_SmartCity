import pandas as pd
import logging
import matplotlib.pyplot as plt


logger = logging.getLogger(__name__)

class aggregater:
    # Can be called for calculating min max of the whole dataframe
    def aggregation_minmax(self, df: pd.DataFrame):
        self.clean_data = df
        self.clean_data['timestamp'] = pd.to_datetime(self.clean_data['timestamp'])
        self.data_time = self.clean_data.set_index('timestamp')
        self.grouped_data = self.data_time.groupby(['sensor_id','location_type']).resample('5d',include_groups=False).agg(['min','max'])
        logger.info('The min and max are shown per column.')
        return self.grouped_data
    
    # Can be called for calculating mean for temp and hum
    def aggregation_mean(self, df: pd.DataFrame):
        self.group_mean = df
        self.grouped = (
            self.group_mean
            .set_index('timestamp')
            .groupby(['sensor_id','location_type'])
            .resample("5D")
            .agg({"temperature_c": "mean",'humidity_pct':'mean'})
        )
        logger.info('The average was calculated for Temp and Hum')
        return self.grouped
    
    # Can be called for plotting the temp and hum.
    def plot_raw(self):
        with pd.plotting.plot_params.use('x_compat', True):
            _ = self.clean_data['temperature_c'].plot(color='r')
            _ = self.clean_data['humidity_pct'].plot(color='b')
        logger.info('Plot was created for Temp and Hum')
        plt.show()

    def plot_mean(self):
        with pd.plotting.plot_params.use('x_compat',True):
            _ = self.grouped['temperature_c'].plot(color='g')
            _ = self.grouped['humidity_pct'].plot(color='y')
        logger.info('Plot mean data from temp and hum')
        plt.show()
        
        