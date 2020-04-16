import math
import sys
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

gravitational_constant = 6.6743e-11

bodys = {
  "earth": {
    "radius": 6371000,
    "mass": 5.972e24,
  },
  "sun": {
    "radius": 696340000,
    "mass": 1.989e30,
  },
  "moon": {
    "radius": 1737000,
    "mass": 7.347e22
  }
}


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s %s\r' % (bar, percents, '%', status))


def set_magnitude(mag, x, y):
    try:
        new_vx = x * mag / math.sqrt(x * x + y * y)
        new_vy = y * mag / math.sqrt(x * x + y * y)
        return new_vx, new_vy
    except ZeroDivisionError:
        return 0, 0


class SimulationObject:
    def __init__(self, name, x, y, vx, vy, m):
        self.data = []
        self.name = name
        self.x = x
        self.y = y
        self.xvelo = vx
        self.yvelo = vy
        self.m = m

    def ac(self, ax, ay):
        self.xvelo += ax
        self.yvelo += ay

    def move(self, s):
        self.x += self.xvelo * s
        self.y += self.yvelo * s

    def render(self):
        self.data.append([self.x, self.y])


class GravitySimulation:
    def __init__(self):
        self.objs = []
        self.SimulationSpeed = 0

    def add(self, objs):
        self.objs.append(objs)

    def frame(self):
        for o in self.objs:
            o.move(self.SimulationSpeed)

        for o in self.objs:
            o.render()

        for o in self.objs:
            for o2 in self.objs:
                if o != o2:
                    dist = round(math.sqrt((o.x - o2.x) ** 2 + (o.y - o2.y) ** 2))

                    ga = gravitational_constant * (o2.m / (dist ** 2))

                    gx, gy = set_magnitude(ga * self.SimulationSpeed, o.x, o.y)
                    o.ac(-gx, -gy)

    def run(self, frames, simulation_speed):
        self.SimulationSpeed = simulation_speed
        s2 = round(frames / self.SimulationSpeed)
        for i in range(s2):
            progress(i, s2, status="Simulating...")
            self.frame()

    def graphic(self, size, animation_speed):
        global m

        fixed_animation_speed = round(animation_speed / self.SimulationSpeed)

        fig = plt.figure(figsize=(10, 10))
        axes = fig.add_subplot(111)
        axes.set_xlim(-size, size)
        axes.set_ylim(-size, size)
        axes.set_aspect(1)
        plt.xlabel('xlabel')
        plt.ylabel('ylabel')

        circle = plt.Circle((0, 0), radius=bodys["earth"]["radius"] / 1000)
        axes.add_artist(circle)

        points = []
        for o in self.objs:
            o.data = o.data[::fixed_animation_speed]
            n = []
            n2 = []
            for i in o.data:
                n.append(i[0] / 1000)

            for i in o.data:
                n2.append(i[1] / 1000)

            axes.plot(n, n2)
            point, = axes.plot(0, 0, 'go')
            points.append(point)

        def ani(frame):
            for o2 in self.objs:
                points[self.objs.index(o2)].set_data(o2.data[frame][0] / 1000, o2.data[frame][1] / 1000)

        m = FuncAnimation(fig, ani, frames=len(self.objs[0].data), interval=50)
        plt.show()


if __name__ == '__main__':
    # -------------------------------------------------------------------- #
    # ------------------------Edit Here----------------------------------- #


    # obj = ("[Name], [PosX], [PosY], [VelX], [VelY], [Mass]") <-- everything m, m/s

    simulation = GravitySimulation()

    earth = SimulationObject("earth", 0, 0, 0, 0, bodys["earth"]["mass"])
    simulation.add(earth)

    moon = SimulationObject("moon", bodys["earth"]["radius"] + 384400000, 0, 0, -1000, bodys["moon"]["mass"])
    simulation.add(moon)

    # iss = obj("iss", bodys["earth"]["radius"] + 408000, 0, 0, -7660, 0)
    # simulation.add(iss)

    # simulation.run(frames, simulation_speed) <--- lower speed is slower but more accurate.
    simulation.run(200000, 100)

    # simulation.graphic("size" of canvas [km], playback speed)
    simulation.graphic(500000, 1000)
