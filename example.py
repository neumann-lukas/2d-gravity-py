from GravityPy import *

simulation = GravitySimulation()

earth = SimulationObject("earth", 0, 0, 0, 0, bodys["earth"]["mass"])
simulation.add(earth)

moon = SimulationObject("moon", bodys["earth"]["radius"] + 384400000, 0, 0, -1000, bodys["moon"]["mass"])
simulation.add(moon)

# simulation.run(frames, simulation_speed) <--- lower speed is slower but more accurate.
simulation.run(2419200, 10)

# simulation.graphic("size" of canvas [km], playback speed)
simulation.graphic(500000, 1000)
