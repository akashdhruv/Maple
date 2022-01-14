# Maple API script

import pymaple

maple = pymaple.Maple()

maple.build()
maple.execute("pwd")
maple.clean()
