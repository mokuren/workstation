from collections import Counter

def freq_table(numbers):
    table = Counter(numbers)
    print('Number\tFrequentry')
    for number in table.most_common():
        print('{0}\t{1}'.format(number[0],number[1]))

if __name__=='__main__':
    scores = [7,7,4,3,6,7,2,2,1,8,7,9,7,1,9,9,9,2,3,5,5]
    freq_table(scores)
    
