# Maple API file to run a Flash-X simulation

import maple.api as maple

# Create a Maple object
image_docker      = maple.Image(name='local',base='akashdhruv/flash:boiling',backend='docker')
image_singularity = maple.Image(name='local',base='docker://akashdhruv/flash:boiling',backend='singularity')

container = maple.Container(name='flashsim',target='/home/mount/simulation')

# Build the local image
image_docker.build()
image_singularity.build()

# Run docker container
container.pour(image_docker)
container.execute("mpirun -n 1 /home/run/flash4")
container.rinse()

# Run singularity container
container.pour(image_singularity)
container.execute("mpirun -n 1 /home/run/flash4")
container.rinse()
