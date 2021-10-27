import pymaple
import os

maple = pymaple.Maple(container='flashsim_container',image='akashdhruv/flash:boiling',
                      source=os.getenv('PWD')+'/data',target='/home/user/run/IOData',
                      parfile='flash.par')

nprocs = 4

maple.build()
maple.run(nprocs)
maple.clean()
maple.remove()
