# 2d-gravity-py
A small 2d program to simulate realistic gravity.

# Usage
## First step
First import the module:
```python
  import GravityPy
```
Then create a Simulation:
```python
  simulation = GravitySimulation()
```

## Second step
Create all objects that should be simulated.
The units are **m, m/s and kg**
You can create a SimulationObject like this:
```python
  simulation_object = SimulationObject([Name], [PosX], [PosY], [VelX], [VelY], [Mass])
```
Then add the object to the simulation
```python
  simulation.add(simulation_object)
```

## Third step
Run the simulation.
You can run the simulation like this:
```python
  simulation.run(frames, simulation_speed)
```
`frames` represents the 'duration' of the simulation in **seconds**.

`simulation_speed` controlls the speed at which the simulation is runned. A smaller speed is slower but more accurate.

## Fourth step
Display the results.
You can display the results as following:
```python
  simulation.display(canvas_size, playback_speed)
```
`canvas_size` is the size of the kanvas in **km**.

`playback_speed` is the playback speed.

The result is `20*playbackspeed` faster then reality.

