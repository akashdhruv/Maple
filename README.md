## Maple - A Python API and CLI for managing HPC projects with containers

![bubblebox-container](https://github.com/akashdhruv/Maple/workflows/bubblebox-container/badge.svg)
![create-container](https://github.com/akashdhruv/Maple/workflows/create-container/badge.svg)
![flash-container](https://github.com/akashdhruv/Maple/workflows/flash-container/badge.svg)

### Installation

```./setup develop```

### Examples

See ```examples/create```  ```examples/bubblebox```  ```examples/flashsim```
 
### Configuration variables

```maple_container```: Local container name

```maple_image```: Remote image name

```maple_source```: Source directory

```maple_target```: Mount path

### Running a docker container with FLASH executable

Build and run the local container

```
cd examples/flashxsim

$HOME/.local/bin/maple build
```

```
$HOME/.local/bin/maple run "mpirun -n 1 /home/run/flash4"
```

### Running a docker container with FLASH developer environment


Build and pour ```maple_image``` to ```maple_container```

```
$HOME/.local/bin/maple build
```

```
$HOME/.local/bin/maple pour 
```

If ```maple_image``` is not locally available it will be pulled from ```docker``` registry. Use ```./maple pull``` to pull the image without creating a local container.

Enter the ```bash``` environment of local container using

```
$HOME/.local/bin/maple bash
```

To commit changes made to the local container and save work locally type

```
$HOME/.local/bin/maple commit
```

To stop the local container run

```
$HOME/.local/bin/maple rinse
```

When you stop your local ```docker``` server, the local container will stop automatically. Any uncommited work will be lost when local container stops.

To push the save image created by ```./maple commit``` to docker registry type

```
$HOME/.local/bin/maple push <remote_image_name>
```

### Purge all local images and containers

Do this to clean up your docker data

```
$HOME/.local/bin/maple clean
```

Don't run this if you still need local images to finish work
