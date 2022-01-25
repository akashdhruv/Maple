# Maple API script

import maple.api as maple

# Image object
image = maple.Image()

# Container object
container = maple.Container()

# Check basic functionality
image.build()
container.run(image,"pwd")
image.squash()
image.delete()
