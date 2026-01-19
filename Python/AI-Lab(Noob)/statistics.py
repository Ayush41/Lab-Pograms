# 1. python program to calculate mean median mode std dev, variance. (no library)
# Modular way of programming
import matplotlib.pyplot as plt

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
    f ={} 
    count = 0
    for i in data:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1 
    mode_val = None
    for key in f:
        if f[key] > count:
            count = f[key]
            mode_val = key
    return mode_val 

def std_dev(data):
    meanval = mean(data)
    var = sum((x - meanval) ** 2 for x in data) / len(data)
    return var ** 0.5

def vizualization(data):
    plt.hist(data, bins=10, edgecolor='black')
    plt.title('Data Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == "__main__":
    data = [1,2, 2, 2, 3, 4,5,0,4,2,3,1,10,10,10,10,10,10]
    print("Mean:", mean(data))
    print("Median:", median(data))
    print("Mode:", mode(data))
    print("Standard Deviation:", std_dev(data))
    vizualization(data)