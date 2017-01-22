'''
The relathionship between gravitational and between two bogies
'''
import matplotlib.pyplot as plt

def draw_graph(F, r):
    plt.plot(r, F, marker='*')
    plt.xlabel('Distance')
    plt.ylabel('Force')
    plt.title('Gravitational Distance')
    plt.show()
 
def calc():
    r = range(100, 1000, 50)
    g = 6.674*(10**-11)
    m1 = 0.5
    m2 = 1.5
    F = []
    for dist in r:
        force = g*m1*m2/(dist**2)
        F.append(force)
    draw_graph(F, r)

if __name__ == '__main__':
    calc()
