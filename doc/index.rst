.. vim: set fileencoding=utf-8 :
.. Gradiant's Biometrics Team <biometrics.support@gradiant.org>
.. Copyright (C) 2017 Gradiant, Vigo, Spain

===================================================================================
Generalized Presentation Attack Detection: a face anti-spoofing evaluation proposal
===================================================================================


Bob package to reproduce the work carried out in chapter "Generalized Presentation Attack Detection: a face anti-spoofing evaluation proposal" in the International Conference on Biometrics, ICB 2019.

Abstract
--------

Over the past few years, Presentation Attack Detection
(PAD) has become a fundamental part of facial recognition
systems. Although much effort has been devoted to antispoofing
research, generalization in real scenarios remains
a challenge. In this paper we present a new open-source
evaluation framework to study the generalization capacity
of face Presentation Attack Detection methods, coined here
as face-GPAD. This framework facilitates the creation of
new protocols focused on the generalization problem and
sets fair procedures of evaluation and comparison between
PAD solutions. We also introduce a large aggregated and
categorized dataset to address the problem of incompatibility
between publicly available datasets. Finally, we propose
a benchmark adding two novel evaluation protocols: one
for measuring the effect introduced by the variations in face
resolution, and the second for evaluating the influence of
adversarial operating conditions.

Acknowledgements
----------------

If you use this framework, please cite the following publication::

    @inproceedings{DBLP:conf/icb/Costa-Pazo2019,
      author    = {Costa-Pazo, Artur and
                   David Jim{\'e}nez-Cabello and
                   Vazquez-Fernandez, Esteban and
                   Alba-Castro, Jos{\'e} Luis and
                   L{\'o}pez-Sastre, Roberto J.
                   },
      title     = {Generalized Presentation Attack Detection: a face anti-spoofing evaluation proposal},
      booktitle = {2019 International Conference on Biometrics, {ICB} 2019, Crete,
                   Greece, June 4-7, 2019},
      year      = {2019}
    }

This package contains scripts to reproduce the results from the paper. The package also provides score files and features for Color-based and Quality-based PAD algorithms, the systems reported in our work.

Reproducible Research
---------------------

The easiest way to reproduce the result presented in the chapter is using docker.

.. code-block:: sh

    $ docker pull acostapazo/bob.gradiant.gradgpad:latest

Once you have downloaded the docker image, you can type:

.. code-block:: sh

    $ docker run -v $(pwd):/bob.gradiant.gradgpad acostapazo/bob.gradiant.gradgpad:latest bin/bash -c "cd bob.gradiant.gradgpad; ./ci.sh; ./rr.sh"

Then, the results will be available on the folder result/paper

.. code-block:: sh

    result/paper/
    ├── results
    │   ├── fig_5_a_iqm.png
    │   ├── fig_5_b_gradiant.png
    │   ├── fig_6_a_iqm.png
    │   ├── fig_6_b_gradiant.png
    │   ├── table_1_gradiant.html
    │   └── table_1_iqm.html
    └── summary.html



Documentation
-------------

.. toctree::
   :maxdepth: 2

   reproducible_research
   user_guide
   acknowledgements

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`





