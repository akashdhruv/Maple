# Maple API file to run a Flash-X simulation

import pymaple

maple = pymaple.Maple(container='flashx',image='akashdhruv/flash:boiling',
                      target='/home/mount/simulation')

maple.build()
maple.pour()
maple.execute("export OMPI_MCA_btl_vader_single_copy_mechanism=none && mpirun -n 1 /home/run/flash4")
maple.clean()
maple.remove()
