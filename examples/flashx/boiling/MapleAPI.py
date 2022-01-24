# Maple API file to run a Flash-X simulation

import maple.api as maple

# Create a Maple object
image_docker      = maple.Image(name='local',base='akashdhruv/flashx:boiling',backend='docker')
image_singularity = maple.Image(name='local',base='docker://akashdhruv/flashx:boiling',backend='singularity')

container = maple.Container(name='flashx',target='/home/mount/simulation')

# Build images
image_docker.build()
image_singularity.build()

# Run containers
container.run(image_docker,"mpirun -n 1 /home/run/flash4")
container.run(image_singularity,"mpirun -n 1 /home/run/flash4")

# Delete images
image_docker.delete()
image_singularity.delete()
