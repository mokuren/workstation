def calculate_mean(numbers):
    N = len(numbers)
    numbers.sort()
    
    if N%2 == 0:
        m1 = N/2
        m2 = N/2 + 1
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        mean = (numbers[m1] + numbers[m2])/2
        

    else:
        m1 = N/2
        m1 = int(m1) - 1
        mean = nubers[m1]

    return mean

if __name__ == '__main__':
    donation = [100, 60,70,900,100,200,500,500,503,600,1000,1200]
    x  = calculate_mean(donation)
    n  = len(donation) 
    print('{0} {1}'.format(x, n))
