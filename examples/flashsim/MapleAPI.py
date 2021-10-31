import pymaple
import os

maple = pymaple.Maple(container='flashsim',image='akashdhruv/flash:boiling',
                      source=os.getenv('PWD')+'/data',target='/home/user/run/IOData',
                      parfile='flash.par')


maple.build()
maple.run(nprocs=1)
maple.clean()
maple.remove()
