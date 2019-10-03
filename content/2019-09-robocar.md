Title: Robocar project
Author: SergeM
Date: 2019-08-24 20:32:00
Slug: robocar
Tags: robocar, donkeycar, ros, linux, robotics, raspberry, pi, robot, 


For the robocar contest in Berlin I started a project of building an autonomous toy car (scale 1:10). The goal of the contest was to show the fastest lap driving autonomously. The track had 8-shape with lane boundaries marked with white tape.

Unfortunately the competition got cancelled. But that gave me an opportunity to switch from my 1st gen car to 2nd gen version.

Here is my first version:

<iframe width="560" height="315" src="https://www.youtube.com/embed/DsQgaF0_wzY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


The second version is built upon a stock RC car Absima Abs1

![](media/2019-09-robocar/absima_abs1_unpacked.jpg)


The default choice of the software for the robot was a project called [donkeycar](https://github.com/autorope/donkeycar). Donkeycar implements a driving stack in python. The AI is based on end-to-end machine learning model.

My first car was built with that stack and I was not quite happy about it. The code quality and version compatibility was far from ideal. Knowing that stack is unlikely to be useful outside of the contest.

Therefore I decided to build the second version on top of ROS to learn that framework on the way. I found [project omicron](https://github.com/project-omicron) that became a basis for my car.

Project omicron had a goal to reimplement donkeycar functionality in ROS. 
I had patched it significantly to make it work for my hardware.


## Hardware
Donkeycar standard hardware looks like this:


I decided to introduce an intermediate layer of arduino that will (hopefully) protect my raspberry from undesired influence of high-current electornics of the car.


To be updated...


https://github.com/serge-m/omicron_robocar/
