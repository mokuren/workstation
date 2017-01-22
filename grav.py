import matplotlib.pyplot as plt


def draw_graph(x, y):
    plt.plot(x, y, marker = 'o')
    plt.xlabel('Distance in meters')
    plt.ylabel('Gravitational force in newton')
    plt.title('Gravitational force and distance')
    plt.show()

def generate_F_r(distance, mrange, erange, body1, body2):
    G = 6.674*(10**-11)
    r = range(distance, mrange, erange)
    F = []
    for dist in r:
        force = G*(body1*body2)/(dist**2)
        F.append(force)
    draw_graph(r, F)

if __name__ == '__main__':
    distance = int(input('Distance between two things:'))
    max_range= int(input('Pls set Max range:'))
    engrave  = int(input('Engrave Distance:'))
    body1    = int(input('Object 1:'))
    body2    = int(input('Object 2:'))    
    generate_F_r(distance, max_range, engrave, body1, body2)
