### solution: Add rentention time 

class MSPeak:
    def __init__(self,
                 mz=None,
                 intensity=None,
                 rt=None):
        self.mz = mz
        self.intensity = intensity
        self.rt = rt
             
    def show_peak(self):
        if self.mz and self.intensity and self.rt:
            print("The peak can be found at mz " + str(self.mz) + " with an intensity of " + str(self.intensity) +
                 " at the retention time of " + str(self.rt) + " seconds")
        else:
            print("Error: Either mz or intensity or retention time or all three values are missing - could not show the peak!")
            

if __name__ == "__main__": 
    x = MSPeak(250, 60000, 300)
    x.show_peak()
    
# currently still the possibilty to change the attributes without using the getter/setter methods (not encapsulated)
# this can be prevented using private attributes
