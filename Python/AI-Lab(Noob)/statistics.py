# 1. python program to calculate mean median mode std dev, variance. (no library)
def mean(data):
    return sum(data)/len(data)

def median(data):
    data_sorted = sorted(data)  # Create a sorted copy without modifying the original
    n = len(data_sorted)
    if n % 2 == 0:
        median = (data_sorted[n//2 - 1] + data_sorted[n//2]) / 2
    else:
        median = data_sorted[n//2]
    return median

def mode(data): # most frequent element in data
    pass
    
    
def std_dev(data):
    meanval = mean(data)
    var = sum((x - meanval) ** 2 for x in data) / len(data)
    return var ** 0.5


if __name__ == "__main__":
    data = [1, 2, 2, 3, 4,5,0,4,3,1]
    print("Mean:", mean(data))
    print("Median:", median(data))
    # print("Mode:", mode(data))
    print("Standard Deviation:", std_dev(data))
    