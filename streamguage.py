import numpy as np
import matplotlib.pyplot as plt



class StreamGuage:
    '''
    class to read and plot USGS steam gauge data.
    '''
    time = []
    data = []
    units = "ft"

    def __init__(self, fid, station_id, station_name, starttime):
        self.fid = fid
        self.station_id = station_id
        self.station_name = station_name
        self.starttime = starttime


    def read_guage_file(self):
        date, time, hgt = np.loadtxt(self.fid, skiprows=28, usecols=[2,3,5], 
                                    dtype=str).T
        hgt = hgt.astype(float)
        days = [float(d[-2:]) for d in date]  # get DD from YYYY-MM-DD
        hours = [float(t.split(":")[0]) for t in time]  # get HH from HH:MM
        mins = [float(t.split(":")[1]) for t in time]  # get MM from HH:MM

        timestamps = []
        for d, h, m in zip(days, hours, mins):
            timestamp = (d * 24 * 60) + (h * 60) + m
            timestamps.append(timestamp)

        self.time = timestamps
        self.data = hgt

    def plot(self):
        plt.plot(self.time, self.data, linestyle = '-')
        plt.title(f" Stream Gauge {self.station_name} {self.station_id}" 
                  f"from {self.starttime} \n maximum height"
                  f" {max(self.data)} {self.units}")
        plt.xlabel('Time in minutes since start of September 2024')
        plt.ylabel(f"Gauge Height {self.units}")
        plt.grid()
        plt.show()

    def convert(self):
        self.data = self.data * 0.3048
        self.units = "meters"

    def demean(self):
        mean = sum(self.data)/int(len(self.data))
        self.data = self.data - mean
    
    def shift_time(self, shift):
        self.time = [item + shift for item in self.time]
    
    def main(self):
        self.read_guage_file()   
        self.convert()   
        self.demean()   
        self.shift_time(-100)
        self.plot()


class NOAAStreamGuage(StreamGuage):
    '''
    class to read and plot NOAA steam gauge data. Inherting from StreamGuage.
    '''
    
    units = "meters"

    def convert(self):       #overriding convert with nothing
        pass

    def read_guage_file(self):       #modifying read_guage_file
        super().read_guage_file()
        print("I am a NOAA stream gauge")

if __name__ == "__main__":
    fids = ["phelan_creek_stream_guage_2024-09-07_to_2024-09-14.txt",
            "phelan_creek_stream_guage_2024-10-07_to_2024-10-14.txt"
            ]  
    for fid in fids:
        NOAAStreamGuage(fid=fid, station_id="15478040 ", 
                        station_name="PHELAN CREEK",
                        starttime="2024-09-07 00:00"
                        ).main()

