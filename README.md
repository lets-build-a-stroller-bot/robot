# Let's Build a Stroller Bot

StrollerBot is a collaborative learning project for robotics.  

## Getting Started

These instructions will get you started.

There are a couple of different ways to get started with strollerbot. A [docker](https://www.docker.com/) container can be run locally using the most current strollerbot docker image. Or you can SSH into the exploded robot prototype using the [Balena CLI](https://github.com/balena-io/balena-cli).

### Robot Prototype

We have a real, drivable prototype now! Woo hoo! The robot prototype is a barebones prototype that includes:

* a Raspberry Pi
* (2x) Sabertooth motor controllers
* two motors
* wooden platform
* lead acid battery

### Developing Strollerbot Software

To develop with the Strollerbot you will need:

Gazebo 9.x ( no other versions, they are not compatible with the ROS version we are using )
Docker
Balena Cli

Once those are installed you can follow these instructions to build and start the Docker container that runs the code from the software/core directory in this repo.

1. Clone this repository on to your computer
2. Change into the directory you just cloned
3. Change to the software directory
4. Run the command `docker build -t strollerbot-core .`
5. You should see a bunch of Extracting, Pull complete messages until finally a Successfully built message
6. Run the command `docker images` you should see "strollerbot-core" in the list.
7. Now start the container with the command - `docker run -d --name strollerbot-core-1 strollerbot-core`
8. Run the command `docker ps -a` you should see a container with a name of strollerbot-core-1
9. Success! Now you can "exec into" the container to see and run ROS and our python scripts in an isolated environment
10. To exec into the container `docker exec -it strollerbot-core-1 /bin/bash`
11. Clone our robot repo into the container under /home/strollerbot ( <-- Will build this into the Dockerfiel at some point )
11. Happy exploring!

So, now you have a docker container running ROS and our robot code, but it doesn't do anything ... there's no robot for it to talk to! We need to set up a simulated world for a simulated robot to live in so we can talk to it, or have the robot prototype around so we can commit our code and pull it down onto the real deal.

Let's set up Gazebo so that we can use a simulation first.

1. Follow instructions to install Gazebo on your particular OS found at: http://gazebosim.org/tutorials?tut=quick_start ( Gazebo 9.x is the only version that works with ROS Melodic, the version of ROS we have on the strollerbot so please download and install it )
2. Open gazebo using the terminal:
`gazebo`
A loading window should appear and then the gazebo main window.
3. In the new gazebo window click on the "Insert" tab on the left hand side.
4. Click the "Add Path" button.
5. Use the pop up Open Directory window to navigate to the directory in which you cloned the strollerbot repository then navigate to and select software/sim/models.
6. A new selection should appear in the left hand window with "Strollerbot" as the only possible model option.
7. Click on "Strollerbot"
8. The strollerbot model should appear in the right hand "world" window. ( Note: depending on how fast your computer is there may be some lag between clicking and the model showing)
9. Click again anywhere in the world window to place the model.
10. To see the robot move drag the right hand drawer open by clicking on the small dot and draggin to the left. Then select the robot in the world window. YOu should see a Joints tab appear. This drawer has the left and right wheel force settings moving both of these up to about 0.1 Newton-meters will make the robot move. ( Make sure the world isn't paused in the very bottom of the world window or your robot won't move.)

#### Connecting to the Robot Prototype

In order to be able to connect to the robot prototype the Raspberry Pi must have power AND connection to the internet.

To connect directly to the robot you must have the following:

* A valid Balena user
* A valid SSH public key that has been added to your Balena user profile
* [Balena CLI](https://github.com/balena-io/balena-cli) installed on your computer

To connect:

1. Login to Balena using Balena CLI:
`balena login`
2. SSH into the Host ( this is the Jetson Nano itself running Balena OS )
`balena ssh -s`
3. Select what should be the only device in the list that is presented
4. Now in the host device:
`balena ps -a`
5. Find CONTAINER ID from the list that has the COMMAND "/ros_entrypoint.sh"
`balena exec -it ${CONTAINER_ID} /bin/bash`
6. You will now be in the ROS Melodic container running on the Raspberry Pi
`rostopic` should run successfully if everything is well

## Learning ROS and Gazebo Tutorials


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
