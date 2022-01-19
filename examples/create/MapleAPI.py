# Maple API script

import maple.api as maple

maple_obj = maple.Maple()

maple_obj.image.build('local')
maple_obj.container.pour('local')
maple_obj.container.execute("pwd")
maple_obj.container.rinse()
