from traffic_light import TrafficLightFSM
import time

fsm = TrafficLightFSM()
for _ in range(6):
    print(fsm)
    time.sleep(1)
    fsm.transition()
