# Maple API file to run a Flash-X simulation

import maple.api as maple

# Create a Maple object
flashsim = maple.Maple(container='flashsim',image='akashdhruv/flash:boiling',
                      target='/home/mount/simulation')

# Build the local image
flashsim.image.build()

# Run a command inside the container
flashsim.container.execute("export OMPI_MCA_btl_vader_single_copy_mechanism=none && mpirun -n 1 /home/run/flash4")

# Clean up not necessary always. Sometimes you want the local and remote images to stay on your system
flashsim.image.clean()
