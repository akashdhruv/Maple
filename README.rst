.. |icon| image:: ./icon.svg
  :width: 30 
  
============  
|icon| Maple
============

|Code style: black|

|BubbleBox| |FlashX| |FlowX| |Minimal|

Maple is a productivity tool that acts a wrapper around docker, podman, and singularity containerization services to provide a seamless interface to deploy High Performance Computing (HPC) applications on cloud and supercomputing platforms. It provides a python based library and command line interface to manage developer and production environment for running complex multiphysics simulations 

Tutorial
========

The link below provides an overiew of Maple within the context of Flash-X (https://flash-x.org), a multiphysics scientific software instrument. Some of the details maybe be outdated, but we are working on updating the tutorial.

|Tutorial|

Installation
============

Stable releases of Maple are hosted on Python Package Index website (`<https://pypi.org/project/PyMaple/>`_) and can be installed by executing,

::

   pip install PyMaple
   
Note that ``pip`` should point to ``python3+`` installation package ``pip3``. 

Upgrading and uninstallation is easily managed through this interface using,

::

   pip install --upgrade PyMaple
   pip uninstall PyMaple

There maybe situations where users may want to install Jobrunner in development mode $\\textemdash$ to design new features, debug, or customize options/commands to their needs. This can be easily accomplished using the ``setup`` script located in the project root directory and executing,

::

   ./setup develop

Development mode enables testing of features/updates directly from the source code and is an effective method for debugging. Note that the ``setup`` script relies on ``click``, which can be installed using,

::

  pip install click

The ``maple`` script is installed in ``$HOME/.local/bin`` directory and therfore the environment variable, ``PATH``, should be updated to include this location for command line use.

Writing a Maplefile
===================

Usage
=====

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

.. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   
.. |BubbleBox| image:: https://github.com/akashdhruv/Maple/workflows/BubbleBox/badge.svg
.. |FlashX| image:: https://github.com/akashdhruv/Maple/workflows/FlashX/badge.svg
.. |FlowX| image:: https://github.com/akashdhruv/Maple/workflows/FlowX/badge.svg
.. |Minimal| image:: https://github.com/akashdhruv/Maple/workflows/Minimal/badge.svg

.. |Tutorial| image:: http://img.youtube.com/vi/gNmVtj7-RBY/0.jpg
   :target: http://www.youtube.com/watch?v=gNmVtj7-RBY
