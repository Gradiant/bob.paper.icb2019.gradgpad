.. vim: set fileencoding=utf-8 :
.. Gradiant's Biometrics Team <biometrics.support@gradiant.org>
.. Copyright (C) 2017 Gradiant, Vigo, Spain

===================================================================================
Generalized Presentation Attack Detection: a face anti-spoofing evaluation proposal
===================================================================================


Bob package to reproduce the work carried out in chapter `Generalized Presentation Attack Detection: a face anti-spoofing evaluation proposal <https://arxiv.org/abs/1904.06213>`_ in the International Conference on Biometrics, ICB 2019.
This package contains scripts to reproduce the results from the paper. The GRAD-GPAD is designed on the top of the frameworks presented in the chapter `Challenges of Face Presentation Attack Detection in Real Scenarios <https://link.springer.com/chapter/10.1007/978-3-319-92627-8_12>`_
in the Handbook of Biometric Anti-Spoofing, where from different protocols some of the gaps between research and real scenario deployments, including generalisation, usability, and performance were analysed.




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

If you use this framework, please cite the following publications::

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

    @Inbook{Costa-Pazo2019,
        author="Costa-Pazo, Artur and Vazquez-Fernandez, Esteban and Alba-Castro, Jos{\'e} Luis and Gonz{\'a}lez-Jim{\'e}nez, Daniel",
        editor="Marcel, S{\'e}bastien and Nixon, Mark S. and Fierrez, Julian and Evans, Nicholas",
        title="Challenges of Face Presentation Attack Detection in Real Scenarios",
        bookTitle="Handbook of Biometric Anti-Spoofing: Presentation Attack Detection",
        year="2019",
        publisher="Springer International Publishing",
        address="Cham",
        pages="247--266",
        isbn="978-3-319-92627-8",
        doi="10.1007/978-3-319-92627-8_12",
        url="https://doi.org/10.1007/978-3-319-92627-8_12"
    }


Disclaimer
----------

Third party publicly available datasets are not managed by Gradiant.
To access them, please contact each of the institutions responsible for
each dataset. The license for the use of these datasets must be consulted
with each institution.

Hope the following table will help you download publicly available datasets.

+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Dataset       | Link                                                                                                                                                                           |
+===============+================================================================================================================================================================================+
| REPLAY-ATTACK | `https://www.idiap.ch/dataset/replayattack <https://www.idiap.ch/dataset/replayattack>`_                                                                                       |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 3DMAD         | `https://www.idiap.ch/dataset/3dmad <https://www.idiap.ch/dataset/3dmad>`_                                                                                                     |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MSU-MFSD      | `http://biometrics.cse.msu.edu/Publications/Databases/MSUMobileFaceSpoofing/index.htm <http://biometrics.cse.msu.edu/Publications/Databases/MSUMobileFaceSpoofing/index.htm>`_ |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| UVAD          | `https://recodbr.wordpress.com/code-n-data/#UVAD <https://recodbr.wordpress.com/code-n-data/#UVAD>`_                                                                           |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| REPLAY-MOBILE | `https://www.idiap.ch/dataset/replay-mobile <https://www.idiap.ch/dataset/replay-mobile>`_                                                                                     |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HKBU (v1)     | `http://rds.comp.hkbu.edu.hk/mars/ <http://rds.comp.hkbu.edu.hk/mars/>`_                                                                                                       |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OULU-NPU      | `https://sites.google.com/site/oulunpudatabase/ <https://sites.google.com/site/oulunpudatabase/>`_                                                                             |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ROSE-YOUTU    | `http://rose1.ntu.edu.sg/Datasets/faceLivenessDetection.asp <http://rose1.ntu.edu.sg/Datasets/faceLivenessDetection.asp>`_                                                     |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SIW           | `http://cvlab.cse.msu.edu/spoof-in-the-wild-siw-face-anti-spoofing-database.html <http://cvlab.cse.msu.edu/spoof-in-the-wild-siw-face-anti-spoofing-database.html>`_           |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CS-MAD        | `https://www.idiap.ch/dataset/csmad <https://www.idiap.ch/dataset/csmad>`_                                                                                                     |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Documentation
-------------

.. toctree::
   :maxdepth: 2

   installation
   reproducible_research
   grad_gpad
   acknowledgements

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`





