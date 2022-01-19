## Maple - A Python API and CLI for managing HPC projects with containers

![bubblebox-container](https://github.com/akashdhruv/Maple/workflows/bubblebox/badge.svg)
![create-container](https://github.com/akashdhruv/Maple/workflows/create/badge.svg)
![flash-container](https://github.com/akashdhruv/Maple/workflows/flash/badge.svg)

### Installation
```
mkdir -p $HOME/.local/bin
export PATH="$PATH:$HOME/.local/bin"
./setup develop && ./setup install
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

  - Building an image

    ```maple image build```: Build local image from remote image

  - Getting shell access:

    ```maple container pour```: Pour local image into a container

    ```maple container shell```: Provides shell access to the container

    ```maple container commit```: Save changes from local container to local image (only available with docker backend)

    ```maple container rinse```: This commands stops and deletes the local container (only available with docker backend)

    ```maple image squash```: Prune redundant layers from a local image (do this to reduce size of an image after ```maple container commit```, only available with docker backend)

  - Launch an ipython notebook inside the 

    ```maple container notebook```: launches the notebook server

  - Execute commands inside the container

    ```maple container execute "echo Hello World!"```: example to launch specific command inside the container

  - Cleanup

    ```maple container clean```: deletes the container environment, if you want to update remote image with local changes run ```maple image push <remote_image_name:tag>``` before ```maple container clean```

    ```maple image remove```: deletes the instance of remote image on local machine, doing this means that ```maple image build``` will have to perform the expensive task of pulling the remote image again if you decide to rebuild the local image.

### Examples

See ```examples/create```  ```examples/bubblebox```  ```examples/flashsim```
