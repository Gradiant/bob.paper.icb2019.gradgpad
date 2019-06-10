.. vim: set fileencoding=utf-8 :
.. Biometrics Team  <biometrics.support@gradiant.com>

===============
Getting started
===============

Once you have finished the installation stage. Please, activate the conda environment :code:`bob.paper.icb2019.gradgpad`.

.. code-block:: sh

    source activate bob.paper.icb2019.gradgpad

Buildout
--------

.. code-block:: sh

    python bootstrap-buildout.py
    bin/buildout

Test
----

.. code-block:: sh

    bin/nosetests -v

Clean
-----

.. code-block:: sh

    python clean.py


Coverage
--------

.. code-block:: sh

    bin/coverage run -m unittest discover
    bin/coverage html -i
    bin/coverage xml -i


Coverage result will be store on htmlcov/.

Doc
---

.. code-block:: sh

    bin/sphinx-build -b html doc/ doc/html/

Continuous Integration
----------------------

In the following script (:code:`ci.sh`) you can check the different stages that are evaluated over the continuous integration pipeline:

.. literalinclude:: examples/ci.sh
