---
Title: Point cloud processing
Author: SergeM
Date: 2020-11-10 20:00:00
Slug: point-cloud-processing
aliases: [/point-cloud-processing.html]
Tags: [ pcl, ros, python, c++, point cloud, pcl, ply]
---



## ROS nodes

### Point Cloud IO

[https://github.com/ANYbotics/point_cloud_io](https://github.com/ANYbotics/point_cloud_io)
- two nodes for reading and writing PointCloud2 from/to `ply`, `pcd` formats

### point_cloud_assembler from laser_assembler

[http://wiki.ros.org/laser_assembler](http://wiki.ros.org/laser_assembler)

This node assembles a stream of sensor_msgs/PointCloud2 messages into larger point clouds. 
The aggregated point cloud can be accessed via a call to `assemble_scans` service.

[https://github.com/ros-perception/laser_assembler](https://github.com/ros-perception/laser_assembler)

[Tutorial](http://wiki.ros.org/laser_assembler/Tutorials/HowToAssembleLaserScans)


### Octomap

[http://octomap.github.io/](http://octomap.github.io/)

Seems like a standard solution to convert point clouds to a map in several formats



### pointcloud_to_laserscan

[http://wiki.ros.org/pointcloud_to_laserscan](http://wiki.ros.org/pointcloud_to_laserscan)


### pcl_ros

[http://wiki.ros.org/pcl_ros](http://wiki.ros.org/pcl_ros)

> This package provides interfaces and tools for bridging a running ROS system to the Point Cloud Library. These include ROS nodelets, nodes, and C++ interfaces. 

It contains for example `pointcloud_to_pcd`, `pcd_to_pointcloud`, `bag_to_pcd`.
