import csv

def n_cross_divide(n, data):
    csv_data_list = [[] for _ in range(n)] 
    csv_data = csv.reader(open(data, 'r'))
    next(csv_data)
    n_index = 0
    for row in csv_data:
        if n_index == n:
            n_index = 0
        csv_data_list[n_index].append(row)
        n_index += 1
    return csv_data_list



if __name__ == "__main__":
    fileName = 'C:/Users/nikhi/OneDrive/RIT/7th Semester/Principles of Data Mining/Data-Mining/hw-05/Abominable_Data_HW05_v725.csv'
    li = n_cross_divide(10, fileName)
    print(li)
    pass