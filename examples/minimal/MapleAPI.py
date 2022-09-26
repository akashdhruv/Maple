# Maple API script

import maple.api as maple

# Image object
image = maple.Image(backend="docker")

# Container object
container = maple.Container()

# Check basic functionality
image.build()
container.run(image, "pwd")
image.squash()
image.delete()
