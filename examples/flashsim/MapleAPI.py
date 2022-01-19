# Maple API file to run a Flash-X simulation

import maple.api as maple

# Create a Maple object
flashsim = maple.Maple(container='flashsim',base='akashdhruv/flash:boiling',
                      target='/home/mount/simulation')

# Build the local image
flashsim.image.build('local')

# Pour a container
flashsim.container.pour('local')

# Run a command inside the container
flashsim.container.execute("mpirun -n 1 /home/run/flash4")

# Rinse a container
flashsim.container.rinse()
