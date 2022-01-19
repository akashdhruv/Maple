# Maple API file to run a Flash-X simulation

import maple.api as maple

# Create a Maple object
flashsim = maple.Maple(container='flashsim',base='akashdhruv/flash:boiling',
                      target='/home/mount/simulation')

# Build the local image
flashsim.image.build()

# Pour a container
flashim.container.pour()

# Run a command inside the container
flashsim.container.execute("mpirun -n 1 /home/run/flash4")

# Rinse a container
flashsim.container.rinse()

# Clean up not necessary always. Sometimes you want the local and remote images to stay on your system
flashsim.image.clean()

# Remove base image
flashsim.image.remove()
