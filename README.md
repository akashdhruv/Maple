## Maple - A Python API and CLI for managing HPC projects with containers

![bubblebox-container](https://github.com/akashdhruv/Maple/workflows/bubblebox-container/badge.svg)
![create-container](https://github.com/akashdhruv/Maple/workflows/create-container/badge.svg)
![flash-container](https://github.com/akashdhruv/Maple/workflows/flash-container/badge.svg)

### Installation
```
mkdir -p $HOME/.local/bin
export PATH="$PATH:$HOME/.local/bin"

./setup develop
./setup clean
```
### Writing a Maplefile

  ```Maplefile``` is used to define environment variables required by ```maple```. Following is a list of variables:
  
  ```maple_image```: Name of the image in remote registry   	 
  
  ```maple_container```: Name of the local container  	
  
  ```maple_target```: Name of the target dir to mount src dir 
  
  ```maple_port```: Port ID for jupyter notebooks 
  
  ```maple_backend```: Backend (docker/singularity)
  
  ```maple``` passes these variables to its internal ```Dockerfile``` to build the images and containers.

### CLI use:

uitilty  - Build maple image from local image using ```maple build```

  - Getting shell access:

    ```maple pour```: Pour local image into a container

    ```maple shell```: Provides shell access to the container

    ```maple commit```: Save changes from local container to local image (only available with docker backend)

    ```maple squash```: Prune redundant layers from a local container and save it to local image (do this to reduce size of an image, only available with docker backend)

    ```maple rinse```: This commands stops and deletes the local container (only available with docker backend)

  - Launch an ipython notebook inside the 

    ```maple notebook```: launches the notebook server

  - Execute commands inside the container

    ```maple execute "echo Hello World!"```: example to launch specific command inside the container

  - Cleanup

    ```maple clean```: deletes the local image, if you want to update remote image with changes to local image run ```maple push <remote_image_name:tag>``` before ```maple clean```

    ```maple remove```: deletes the instance of remote image on local machine, doing this means that ```maple build``` will have to perform the expensive task of pulling the remote image again if you decide to rebuild the local image.

### Examples

See ```examples/create```  ```examples/bubblebox```  ```examples/flashsim```
