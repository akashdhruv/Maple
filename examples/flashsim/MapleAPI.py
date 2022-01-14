# Maple API file to run a Flash-X simulation

import pymaple

# Create a Maple object
flashsim = pymaple.Maple(container='flashsim',image='akashdhruv/flash:boiling',
                      target='/home/mount/simulation')

# Build the local image
flashsim.build()

# Run a command inside the container
flashsim.execute("export OMPI_MCA_btl_vader_single_copy_mechanism=none && mpirun -n 1 /home/run/flash4")

# Clean up not necessary always. Sometimes you want the local and remote images to stay on your system
flashsim.clean()
