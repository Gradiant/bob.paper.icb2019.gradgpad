.. vim: set fileencoding=utf-8 :
.. Biometrics Team  <biometrics.support@gradiant.com>

============
Installation
============


Installation With Docker
------------------------

The fastest way to contact the package is to use docker.

You can download the docker image from dockerhub

.. code-block:: sh

    docker pull acostapazo/bob.paper.icb2019.gradgpad:latest

or build it from Dockerfile

.. code-block:: sh

    docker build --no-cache -t acostapazo/bob.paper.icb2019.gradgpad:latest .

To check that everything is going well, use:

.. code-block:: sh

    docker run \
        -v $(pwd):/bob.paper.icb2019.gradgpad acostapazo/bob.paper.icb2019.gradgpad:latest \
        bin/bash -c "source activate bob.paper.icb2019.gradgpad; \
                     cd bob.paper.icb2019.gradgpad; \
                     ./ci.sh"

This command will execute the following steps
    * mount a the code as a volume (:code:`-v $(pwd):/bob.paper.icb2019.gradgpad`)
    * activate the conda environment (:code:`source activate bob.paper.icb2019.gradgpad`)
    * move to mounted path (:code:`cd bob.paper.icb2019.gradgpad`)
    * execute continuous integration script (:code:`ci.sh`)


Installation With Conda
-----------------------

1. Install `conda <https://conda.io/docs/user-guide/install/index.html>`_

2. Create a conda env

.. code-block:: sh

    conda env create -f envs/ubuntu_environment.yml

or if run this in macosx platform

.. code-block:: sh

    conda env create -f envs/mac_environment.yml

3. Activate the environment and add some channels

.. code-block:: sh

   source activate bob.paper.icb2019.gradgpad
