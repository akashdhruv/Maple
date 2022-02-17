Maple
=====

|Code style: black|

|BubbleBox| |FlashX| |FlowX| |Minimal|

Introduction
------------

Maple is a Python API and CLI that acts as a wrapper around
docker/singularity to implement containerization of HPC applications and
their dependencies.

Tutorial
--------

|Tutorial|

Installation
------------

::

   mkdir -p $HOME/.local/bin
   export PATH="$PATH:$HOME/.local/bin"
   ./setup develop && ./setup install

Writing a Maplefile
-------------------

``Maplefile`` is used to define environment variables required by
``maple``. Following is a list of variables:

``base``: Name of the base image

``container``: Name of the local container

``target``: Name of the target dir to mount source dir

``backend``: Backend (docker/singularity)

``maple`` passes these variables to its internal ``Dockerfile`` to build
the images and containers.

CLI use:
--------

-  Building an image

   ``maple image build <image>``: Build local image from remote image

-  Getting shell access:

   ``maple container pour --image=<image>``: Pour local image into a
   container

   ``maple container shell``: Provides shell access to the container

   ``maple container commit --image=<image>``: Save changes from local
   container to local image (only available with docker backend)

   ``maple container rinse``: This commands stops and deletes the local
   container (only available with docker backend)

   ``maple image squash --image=<image>``: Prune redundant layers from a
   local image (do this to reduce size of an image after
   ``maple container commit``, only available with docker backend)

-  Launch an ipython notebook inside the

   ``maple container notebook --image=<image> --port=<port>``: launches
   the notebook server

-  Run commands inside the container

   ``maple container run --image=<image> "echo Hello World!"``: example
   to launch specific command inside the container, use –comit to save
   changes to the image

-  Cleanup

   ``maple container rinse <container1> <container2> <container3>``:
   deletes containers

   ``maple image delete <image1> <image2> <image3>``: deletes images

-  Remote interface ``maple pull <image>`` and ``maple push <image>``

Examples
--------

See ``examples/create`` ``examples/bubblebox`` ``examples/flashsim``

.. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
.. |BubbleBox| image:: https://github.com/akashdhruv/Maple/workflows/BubbleBox/badge.svg
.. |FlashX| image:: https://github.com/akashdhruv/Maple/workflows/FlashX/badge.svg
.. |FlowX| image:: https://github.com/akashdhruv/Maple/workflows/FlowX/badge.svg
.. |Minimal| image:: https://github.com/akashdhruv/Maple/workflows/Minimal/badge.svg
.. |Tutorial| image:: http://img.youtube.com/vi/gNmVtj7-RBY/0.jpg
   :target: http://www.youtube.com/watch?v=gNmVtj7-RBY
