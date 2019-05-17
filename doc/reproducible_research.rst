.. vim: set fileencoding=utf-8 :
.. Biometrics Team  <biometrics.support@gradiant.com>

=====================
Reproducible Research
=====================

The easiest way to reproduce the result presented in the paper is using the bash script :code:`rr.sh`.

.. literalinclude:: examples/rr.sh


This script downloads the extracted features and executes the experiments.

Once the :code:`rr.sh` script is finished you may find the following files:

    * Downloaded features will be stored in :code:`resources_bob_paper_icb2019_gradgpad`
    * Trained models will be stored in :code:`resources_bob_paper_icb2019_gradgpad`
    * Summary result tables will be stored in :code:`result`


In this work we have used the framework presented in the chapter :code:`Challenges of Face Presentation Attack Detection in Real Scenarios`
in the Handbook of Biometric Anti-Spoofing. Take a look of the `doc <https://gradiant.github.io/bob.chapter.hobpad2.facepadprotocols/user_guide.html>`_ to better understand the framework.
