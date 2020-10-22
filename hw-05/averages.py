import csv
import pandas as pd

def average(file_name):
    data_frame = pd.read_csv(file_name)
    data = open(file_name)
    lines = data.readlines();
    book = {
        'purity'    : data_frame['Purity'].tolist(),
        'records'   : data_frame['Data Records'].tolist(),
        'depth'     : data_frame[' Depth Level'].tolist(),
        'accuracy'  : data_frame[' Accuracy Rate'].tolist()
    }

    '''
    s_b = {
        p : {
            '#' : 100-accuracy
        },
    }
    '''
    store_book = {
        'purity'    : {},
        'records'   : {},
        'depth'     : {},
    }

    limit_depth_lvl = 9
    limit_data_rec = 10
    limit_purity = 8
    row = 1
    while row < len(lines):
        for i in range(9):
            tokens = lines[row].replace('\n','').split(',')
            num = float(tokens[2])
            if num in store_book['depth']:
                store_book['depth'][num] += 100 - float(tokens[3])
            else:
                store_book['depth'][num] = 100 - float(tokens[3])
            row += 1

        for i in range(10):
            tokens = lines[row].replace('\n','').split(',')
            num = float(tokens[1])
            if num in store_book['records']:
                store_book['records'][num] += 100 - float(tokens[3])
            else:
                store_book['records'][num] = 100 - float(tokens[3])
            row += 1

        for i in range(8):
            tokens = lines[row].replace('\n','').split(',')
            num = float(tokens[0])
            if num in store_book['purity']:
                store_book['purity'][num] += 100 - float(tokens[3])
            else:
                store_book['purity'][num] = 100 - float(tokens[3])
            row += 1

    for key, val in store_book['purity'].items():
        store_book['purity'][key] = val / 8

    for key, val in store_book['records'].items():
        store_book['records'][key] = val / 10

    for key, val in store_book['depth'].items():
        store_book['depth'][key] = val / 9
    
    return store_book


def write_to_csv(book):
    file = open('hw-05/average_accuracy_data.csv', 'wt')
    for key, val in book.items():
        file.write(str(key) + '\n')
        for inner_key, inner_val in book[key].items():
            file.write(str(inner_key) + ',' + str(inner_val) + '\n')
        file.write('\n')

if __name__ == "__main__":
    file_name = 'C:/Users/nikhi/OneDrive/RIT/7th Semester/Principles of Data Mining/Data-Mining/hw-05/output_results_file.csv'
    book = average(file_name)
    write_to_csv(book)