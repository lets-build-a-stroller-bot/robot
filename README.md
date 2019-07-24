# Let's Build a Stroller Bot

StrollerBot is a collaborative learning project for robotics.  

## Getting Started

These instructions will get you started.

There are a couple of different ways to get started with strollerbot. A [docker](https://www.docker.com/) container can be run locally using the most current strollerbot docker image. Or you can SSH into the exploded robot prototype using the [Balena CLI](https://github.com/balena-io/balena-cli).

### Exploded Robot Prototype

The exploded robot prototype is a barebones prototype that includes:

* a Jetson Nano Dev Kit card
* two motor controllers
* two motors

The goal of the this prototype is to start putting together the basic electronic components that will be needed by the end product / robot without having to invest in / build the hard ware to house it. This allows the stroller bot team to start developing the needed software, connect base components together, and get a better idea of the specifications and mechanical needs for the end robot.

#### Connecting to the Exploded Robot

To connect to the exploded robot you must have the following:

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
6. You will now be in the ROS Melodic container running on the Jetson Nano
`rostopic` should run successfully if everything is well

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details