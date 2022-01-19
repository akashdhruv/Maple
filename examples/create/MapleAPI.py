# Maple API script

import maple.api as maple

image = maple.Image()
container = maple.Container()

image.build()
container.pour(image)
container.execute("pwd")
container.rinse()
image.squash()
image.tag('new')
image.delete()
