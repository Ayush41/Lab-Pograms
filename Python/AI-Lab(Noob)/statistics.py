# 1. python program to calculate mean median mode std dev, variance. (no library)
def mean(self,data):
    return sum(data)/len(data)

def med(self,data):
     data.sort() #sort data first

def mode(self,data):

def stddev(self,data):


if __name__ == "__main__":
    data = [1, 2, 2, 3, 4]
    print("Mean:", mean(data))
    print("Median:", med(data))
    print("Mode:", mode(data))
    print("Standard Deviation:", stddev(data))
    