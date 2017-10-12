#!/usr/bin/env python3

# Copyright (c) 2016 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Tell Cozmo to find a cube, and then drive up to it
This is a test / example usage of the robot.go_to_object call which creates a
GoToObject action, that can be used to drive within a given distance of an
object (e.g. a LightCube).
'''

import asyncio

import cozmo
from cozmo.util import degrees, distance_mm, Pose
from fysom import *


def go_to_ar_cube(robot: cozmo.robot.Robot):
    '''The core of the go to object test program'''

    # look around and try to find a cube
    look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)

    cube = None

    try:
        cube = robot.world.wait_for_observed_light_cube(timeout=30)
        print("Found cube: %s" % cube)
    except asyncio.TimeoutError:
        print("Didn't find a cube")
    finally:
        look_around.stop()

    if cube:
        # Drive to 70mm away from the cube (much closer and Cozmo
        # will likely hit the cube) and then stop.
        # print(cube.pose)
        # fsm.found_cube()
        # robot.say_text("Found cube, going to cube!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        print("robot vals : x-val: %d, y-val: %d", robot.pose.position.x, robot.pose.position.y)
        print("cube vals : x-val: %d, y-val: %d", cube.pose.position.x, cube.pose.position.y)
        robot.go_to_pose(Pose(cube.pose.position.x - robot.pose.position.x, cube.pose.position.y - robot.pose.position.y, 0,
                              angle_z=cube.pose.rotation.angle_z), relative_to_robot=True).wait_for_completed()
        # print("Completed action: result = %s" % action)
        # fsm.at_cube()
        # robot.say_text("Now at cube, moving to search for colored cube!")
        print("Done.")


cozmo.run_program(go_to_ar_cube)