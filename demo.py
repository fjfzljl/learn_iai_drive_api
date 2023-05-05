from IPython.display import clear_output
clear_output()

# import os
# os.kill(os.getpid(), 9) # Runtime needs to be restarted after updating packages

from IPython.display import display, Image, clear_output
import matplotlib.pyplot as plt
import imageio
import numpy as np
import cv2 
import invertedai as iai
from IPython.utils import io
import time

#API key:
iai.add_apikey("mZHY4zRJkJ557Aut85Q8T2pSFELU05Tn7LMrqxgu")

# We begin by setting up the simulation and previewing some of the environment. We pick a location, a four way signalized intersection.
# pick a location (4 way, signalized intgersection)
# 我们首先设置模拟并预览一些环境。 我们选择一个位置，一个四路信号交叉口。
# 选择一个位置（4 路，信号化整数部分）
location = "iai:drake_street_and_pacific_blvd"

# We can preview the map, and look at the traffic light locations to understand which of the lights control which road
# 我们可以预览地图，并查看红绿灯位置以了解哪个灯控制哪条道路
location_info = iai.location_info(location=location)
rendered_static_map = location_info.birdview_image.decode()
fig, ax = plt.subplots(constrained_layout=True, figsize=(10, 10))
ax.set_axis_off(), ax.imshow(rendered_static_map)

# show the map
plt.show()

# We initialize the client side plotting code, this class is helpful for constructing single time plots, and animated gifs:
scene_plotter = iai.utils.ScenePlotter(rendered_static_map, location_info.map_fov, (location_info.map_center.x, location_info.map_center.y), location_info.static_actors)

# These are the traffic light locations, we can infer from their coordinates which of them control what road, in the following examples we will control them manually:
for actor in location_info.static_actors:
    print(actor)

# We are now in a position to initialize the simulation, with the above traffic light information, all we need to do is set the traffic lights appropriately. There are two main directions, and a left turn light in one direction. Our initial scenario will be a red light for the main road, and a green light for both side streets. The traffic light states are passed as a dictionary.
# 我们现在可以初始化模拟了，有了上面的红绿灯信息，我们需要做的就是适当地设置红绿灯。 有两个主要方向，一个方向有一个左转灯。 我们的初始场景是主干道亮红灯，两侧街道亮绿灯。 交通灯状态作为字典传递。
main_road_light_state = 'red'
left_turn_light = 'red'
side_road_light_state = 'green'
light_states = [main_road_light_state, main_road_light_state, main_road_light_state,
                left_turn_light,
                side_road_light_state,
                main_road_light_state, main_road_light_state, main_road_light_state,
                side_road_light_state]
traffic_light = {actor.actor_id : light for actor, light in zip(location_info.static_actors, light_states)}

# Now we initialize and plot.

# Note: to make this demo consistent with its pre-rendered output, we have set the random seed to a fixed number. Removing this argument will randomize the output. We have set the random seed throughout this notebook.

# Note 2: we separate plotting code and calls to the api as much as possible, to highlight the estimated round trip time. While it is possible to plot results on the fly, this slows the simulation down significantly.
# 现在我们初始化并绘图。

# 注意：为了使这个演示与其预渲染输出一致，我们将随机种子设置为固定数字。 删除此参数将使输出随机化。 我们在本笔记本中设置了随机种子。

# 注意 2：我们尽可能将绘图代码和对 api 的调用分开，以突出估计的往返时间。 虽然可以动态绘制结果，但这会显着降低模拟速度。

t0 = time.time()
initial_conditions = iai.api.initialize(location, 
                            agent_attributes = None, 
                            states_history = None, 
                            traffic_light_state_history = [traffic_light],
                            get_birdview = False, 
                            get_infractions = False, 
                            agent_count = 12, 
                            random_seed = 0)
t0b = time.time()
print(f'Initialize time: {t0b - t0:.2f} s')

plt.figure(figsize=(10,10))
scene_plotter.plot_scene(initial_conditions.agent_states,
                         initial_conditions.agent_attributes, 
                         traffic_light_states = traffic_light,
                         numbers=True, velocity_vec=False, direction_vec=True)

# # show the map
plt.show()

# And then we can run drive, conditioned on the traffic light state. For this example, we keep the traffic light fixed over time:
# 然后我们可以运行 drive，以交通灯状态为条件。 对于这个例子，我们保持交通灯随时间固定：
agent_attributes = initial_conditions.agent_attributes
scene_plotter.initialize_recording(initial_conditions.agent_states, agent_attributes=agent_attributes, traffic_light_states=traffic_light)
updated_state = initial_conditions;
times = []
for i in range(100):
    t0 = time.time()
    updated_state = iai.drive(
        agent_attributes=agent_attributes,
        agent_states=updated_state.agent_states,
        recurrent_states=updated_state.recurrent_states,
        traffic_lights_states=traffic_light,
        get_birdview=False,
        location=location,
        get_infractions=False,
    )
    t0b = time.time()
    times.append(t0b - t0)
    scene_plotter.record_step(updated_state.agent_states, traffic_light_states=traffic_light);
    print(f'Iteration {i}, api call time: {(times[-1]):.2f} s')
    clear_output(wait=True)
print(f'Average time per call: {sum(times)/len(times):.2f} over {len(times)} calls')
# Average time per call: 0.22 over 100 calls

# Then we assemble a gif:
# 然后我们组装一个gif：
# %%capture
gif_name = 'iai-drive-side-road-green.gif'
fig, ax = plt.subplots(constrained_layout=True, figsize=(10, 10))
scene_plotter.animate_scene(output_name=gif_name, ax=ax,
                      numbers=False, direction_vec=True, velocity_vec=False,
                      plot_frame_number=True)

plt.show()
Image(gif_name)


# Note how both initialize and ITRA correctly obey the set traffic lights: agents stop for red light, and go on green. This is also reflected in the initialized velocities, and positions.
# 请注意初始化和 ITRA 如何正确遵守设置的交通信号灯：代理在红灯时停止，然后在绿灯时继续行驶。 这也反映在初始化的速度和位置上。

# Alternate traffic light
# To demonstrate how the model reacts to different traffic light states, we now show what happens when we initialize with an alternate traffic light state: the main road now has the green light while the side roads are red.

# 备用交通灯
# 为了演示模型如何对不同的交通灯状态做出反应，我们现在展示当我们使用备用交通灯状态进行初始化时会发生什么：主干道现在是绿灯，而辅路是红灯。

main_road_light_state = 'green'
left_turn_light = 'green'
side_road_light_state = 'red'
light_states = [main_road_light_state, main_road_light_state, main_road_light_state, 
                left_turn_light,
                side_road_light_state,
                main_road_light_state, main_road_light_state, main_road_light_state,
                side_road_light_state]
traffic_light = {actor.actor_id : light for actor, light in zip(location_info.static_actors, light_states)}

# We again initialize
t0 = time.time()
initial_conditions = iai.api.initialize(location, 
                            agent_attributes = None, 
                            states_history = None, 
                            traffic_light_state_history = [traffic_light],
                            get_birdview = False, 
                            get_infractions = False, 
                            agent_count = 12, 
                            random_seed = 0)
t0b = time.time()
print(f'Initialize time: {t0b - t0:.2f} s')
# Initialize time: 0.76 s

plt.figure(figsize=(10,10))
scene_plotter.plot_scene(initial_conditions.agent_states,
                         initial_conditions.agent_attributes, 
                         traffic_light_states = traffic_light,
                         numbers=True, velocity_vec=False, direction_vec=True)

plt.show()

# And simulate using DRIVE:
# 并使用 DRIVE 进行模拟：

agent_attributes = initial_conditions.agent_attributes
scene_plotter.initialize_recording(initial_conditions.agent_states, agent_attributes=agent_attributes, traffic_light_states=traffic_light)
updated_state = initial_conditions;
times = []
for i in range(100):
    t0 = time.time()
    updated_state = iai.drive(
        agent_attributes=agent_attributes,
        agent_states=updated_state.agent_states,
        recurrent_states=updated_state.recurrent_states,
        traffic_lights_states=traffic_light,
        get_birdview=False,
        location=location,
        get_infractions=False,
    )
    t0b = time.time()
    times.append(t0b - t0)
    scene_plotter.record_step(updated_state.agent_states, traffic_light_states=traffic_light);
    print(f'Iteration {i}, api call time: {(times[-1]):.2f} s')
    clear_output(wait=True)
print(f'Average time per call: {sum(times)/len(times):.2f} over {len(times)} calls')

# Average time per call: 0.16 over 100 calls


# %%capture
gif_name = 'iai-drive-side-road-green.gif'
fig, ax = plt.subplots(constrained_layout=True, figsize=(10, 10))
scene_plotter.animate_scene(output_name=gif_name, ax=ax,
                      numbers=False, direction_vec=True, velocity_vec=False,
                      plot_frame_number=True)

plt.show()
Image(gif_name)

