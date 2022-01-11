# Maple API script

import pymaple

maple = pymaple.Maple()

maple.build()
maple.run("pwd")
maple.clean()
maple.remove()
