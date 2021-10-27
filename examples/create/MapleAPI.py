import pymaple

maple = pymaple.Maple()

nprocs = 20

maple.build()
maple.run(nprocs)
maple.clean()
maple.remove()
