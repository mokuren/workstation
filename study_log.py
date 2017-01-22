import matplotlib.pyplot as plt

def create_graph(Times, labels):
    numbars = len(Times)
    positions = range(1, numbars+1)
    plt.barh(positions, Times, align= 'center')
    plt.show()


if __name__ == '__main__':
    Times = []
    i    = 0
    labels = ['Sun', 'Mon', 'Tue', 'Web', 'Thu','Fri', 'Sat']
    for day in labels:
        Time = int(input('Enter Play game time!:'))
        Times.append(Time)
        print('Day:{0} Recorde:{1}'.format(day, Time))
        i += 1

    create_graph(Times, labels)
