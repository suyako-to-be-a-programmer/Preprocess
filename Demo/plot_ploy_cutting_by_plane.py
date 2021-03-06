from Lib.GeometryLib import *

if __name__ == '__main__':
    plt.figure(figsize=(20, 15))
    plt.ion()
    # points = np.random.random((5, 3))
    points = np.array([[0.38498958, 0.13116157, 0.8070374],
                       [0.37564539, 0.78600008, 0.38217829],
                       [0.91703835, 0.04443514, 0.07185674],
                       [0.93409103, 0.88993785, 0.73242011],
                       [0.72458681, 0.1604321, 0.33335469]])
    poly = Polyhedron(points)
    normal_vector = np.array([0, 0, 1])
    constant = np.linspace(-poly.z_range.end, -poly.z_range.start, 50)
    ax1 = plt.subplot2grid((2, 3), (0, 0), rowspan=2, colspan=2, projection='3d')
    ax1.axis('off')
    ax2 = plt.subplot2grid((2, 3), (0, 2), projection='3d')
    ax2.axis('off')
    ax3 = plt.subplot2grid((2, 3), (1, 2), projection='3d')
    ax3.axis('off')
    poly.plot(ax1)
    for e in constant:
        plane = Plane(normal_vector=normal_vector, z_=e)
        figplane = plane.plot(ax1)
        _, intersect, _ = poly.intersect(plane)
        # figintersect = ax1.scatter(intersect[:, 0], intersect[:, 1], intersect[:, 2], marker='x')
        above, down = poly.cutting(plane)
        above.plot(ax2)
        down.plot(ax3)
        plt.pause(0.01)
        ax1.patches.remove(figplane)
        # ax1.collections.remove(figintersect)
        while len(ax2.patches):
            ax2.patches.pop()
        while len(ax3.patches):
            ax3.patches.pop()
    # print(points)
