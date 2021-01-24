## MAPLE - command line utility for running docker containers with FLASH

### Configuration variables

The configuration files are located in the ```configs``` directory

```maple_container``` : Local container name

```maple_image``` : Base image name

```maple_parfile``` : Simulation specific ```flash.par``` located in ```parfiles``` directory

### Running a docker container with FLASH executable

Set environment variable ```maple_config``` using example configuration from ```configs/config.lidcav```

```
export maple_config=configs/config.lidcav
```

Build and run the local container

```
./maple build
```

```
./maple run
```
Results for the simulation are written in the  ```IOData``` directory

### Running a docker container with FLASH developer environment

Set environment variable ```maple_config``` using example configuration from ```configs/config.hdf5_async```

```
export maple_config=configs/config.hdf5_async
```

Pour ```maple_image``` to ```maple_container```

```
./maple pour
```

If ```maple_image``` is not locally available it will be pulled from ```docker``` registry. Use ```./maple pull``` to pull the image without creating a local container.

Enter the ```bash``` environment of local container using

```
./maple bash
```

To commit changes made to the local container and save work locally type

```
./maple commit
```

To stop the local container run

```
./maple stop
```

When you stop your local ```docker``` server, the local container will stop automatically. Any uncommited work will be lost when local container stops.

To create a new container and resume work from previously saved image created by ```./maple commit``` type

```
./maple repour
```

To push the save image created by ```./maple commit``` to docker registry type

```
./maple push <remote_image_name>
```


### Purge all local images and containers

Do this to clean up your docker data

```
./maple clean
```

Don't run this if you still need local images to finish work