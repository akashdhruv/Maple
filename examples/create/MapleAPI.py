# Maple API script

import maple.api as maple

maple = maple.Maple()

maple.image.build()
maple.container.pour()
maple.container.execute("pwd")
maple.container.rinse()
maple.image.clean()
maple.image.remove()
