Assignment#2

This workspace has one package called loop_task with two launch files to complete the following two tasks:
	i) Launch Turtlesim with a node and make the robot traverse a circle
	ii) Launch Turtlesim with a node and make the robot traverse a square

The structure is as follows:
	Assignment_ws->src->loop_task
				--src                     --launch
				  --scripts ---videos         --square.launch --circle.launch
					
The scripts directory has the python scripts titled square_openloop.py and circle.py.

Run roslaunch loop_task circle.launch to complete the circle task
Run roslaunch loop_task square.launch to complete the square task
