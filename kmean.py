import matplotlib.pyplot as plt
import numpy as np
import math
import time

x=0
y=1
fig = None
sub = None
def graph(data, k_points):
    sub = fig.add_subplot()

    plotx = [d[x] for d in data]
    ploty = [d[y] for d in data]

    kx = [k[x] for k in k_points]
    ky = [k[y] for k in k_points]

    sub.scatter(plotx, ploty)
#    sub.ylabel("distance")
 #   sub.xlabel("time")

    sub.plot(kx, ky, "x")
    
    #plt.show()
    #plt.draw()

    fig.canvas.draw()

    fig.canvas.flush_events()
    
    plt.clf()
    #plt.show()

def get_V(k_points, d_point):
    short_v = [d_point[x] - k_points[0][x] , d_point[y] - k_points[0][y]]
    short_d = math.sqrt(short_v[x]*short_v[x] + short_v[y]*short_v[y] )
    k = 0
    
    for kp_ind in range(0, k_points.__len__()):
        v = [d_point[x] - k_points[kp_ind][x] , d_point[y] - k_points[kp_ind][y]]
        dist = math.sqrt(v[x]*v[x] + v[y]*v[y] )
        if dist < short_d:
            short_d = dist
            short_v = v.copy()
            k = kp_ind

    return short_v, k



def k_mean(data, iterations, k_val):

    k_points = [[x,y] for x,y in zip(np.random.randint(0,50, k_val), np.random.randint(0,50, k_val))]
    
    #vector to mean point from k_point
    k_means = [[0,0] for i in range(k_val)]

    for i in range(iterations):
        for vector in data:
            t_v, k_index  = get_V(k_points, vector)
            k_means[k_index][x] = (k_means[k_index][x] + t_v[x]) / 2
            k_means[k_index][y] = (k_means[k_index][y] + t_v[y] ) / 2   #ffffffffffffffuuuuuuuuuuuuu y was x :(
        for kp in range(k_val):
             k_points[kp] = [k_means[kp][x] + k_points[kp][x], k_means[kp][y] + k_points[kp][y]]
            #k_points[kp] = k_means[kp].copy()

        
        graph(data, k_points)
        time.sleep(1)
    return k_points


if __name__ == "__main__":
    plt.ion()
    
    fig = plt.figure()
    d_bl = [[x, y] for x,y in zip(np.random.randint(0, 30, 50), np.random.randint(0, 15, 50))]
    d_tr = [[x, y] for x,y in zip(np.random.randint(40, 50, 50), np.random.randint(40, 50, 50))]

    d_tl = [[x, y] for x,y in zip(np.random.randint(0, 20, 50), np.random.randint(40, 50, 50))]
    d_br = [[x, y] for x,y in zip(np.random.randint(30, 50, 50), np.random.randint(0, 10, 50))]

    data = d_bl + d_tr + d_tl + d_br

    k_points = k_mean(data, 20, 4)

    #graph(data, k_points)