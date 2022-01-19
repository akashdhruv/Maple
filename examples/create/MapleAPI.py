# Maple API script

import maple.api as maple

image = maple.Image()
container = maple.Container()

image.build()
container.run(image,"pwd")
image.squash()
image.tag('new')
image.delete()
