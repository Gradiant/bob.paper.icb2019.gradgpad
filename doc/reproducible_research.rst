.. vim: set fileencoding=utf-8 :
.. Biometrics Team  <biometrics.support@gradiant.com>

=====================
Reproducible Research (TODO)
=====================

Note: Under construction!

* System scores generated with evaluated PAD methods are available.
* Software for reproduce the results are available.
* Python bob-based framework is now available for running your face-PAD over GRAD-GPAD databases.


The easy way to reproduce the results
-------------------------------------

There is available a python script which perform all the operations to get the figures and tables reported in the paper.

We assume you have already install the package (See Installation section in github page)

.. code-block:: sh

    $ #You should be inside the package directory (bob.paper.icb2019.gradgpad)
    $ bin/reproducible_research.py --verbose

This script will do:
    1. Download the scripts (wget)
    2. From the scores, it evaluates the performance for all the protocols presented in the paper.
    3. Retrieve the tables and figures and summarize into a html webpage (result/chapter/summary.html)


Step by step
------------
If you prefer reproduce the results step by step, you can follow the instructions below.

Downloading score files
~~~~~~~~~~~~~~~~~~~~~~~

We are providing the score files obtained for all the systems presented in the chapter. These score files can be used to compute error rates (ACER, APCER, BPCER, HTER) over all of the presented protocols.
To download the scores, please execute the following script:

.. code-block:: sh

    $ #You should be inside the package directory (bob.paper.icb2019.gradgpad)
    $ bin/download_scores.py


Downloading the database
------------------------

The proposed frameworks has been created for be used with whatever database. From now, it has been tested with OULU-NPU, MSU-MFSD, REPLAY-MOBILE and REPLAY-ATTACK. In the chapter we share the results considering OULU-NPU data. 

Follow the steps given in `https://sites.google.com/site/oulunpudatabase/welcome <https://sites.google.com/site/oulunpudatabase/welcome>`_., you can download OULU-NPU database.

You must export environment variable for running the experiments:

.. code-block:: sh
    
    $ export OULU_NPU_PATH="<path/to/database>"


Reproducing results of the chapter
----------------------------------

We assume that the score files of the PAD systems can be found in folder `scores`.


Algorithmic Evaluation Unconstrained
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Getting Table 1** (Algorithmic Evaluation Unconstrained) ...

To compute error rates presented in the Table 1 of the chapter, you can use the following script:

.. code-block:: sh

    $ #For IQM system
    $ bin/algorithmic_unconstrained_evaluation.py -r experiments/configuration_iqm_from_scores.py
    $ #For Gradiant system
    $ bin/algorithmic_unconstrained_evaluation.py -r experiments/configuration_gradiant_from_scores.py

The script will create a folder for each configuration of PAD system and dataset. The folders contain DET curves for each given configuration (subset of these plots are shown in Figure 4 of the chapter), histograms of score distributions, and error rates. The script also creates a text file 'latex_table_overall_stats_eer.txt' which contains a LaTeX formatted table with the results from Table 4 of the paper.


**Getting Figure 5** (Algorithmic Evaluation Constrained) ...

To compute error rates for different types of attack as presented in Figure 5, please execute following scripts:

.. code-block:: sh

    $ #For IQM system
    $ bin/algorithmic_constrained_evaluation.py -r experiments/configuration_iqm_from_scores.py
    $ #For Gradiant system
    $ bin/algorithmic_constrained_evaluation.py -r experiments/configuration_gradiant_from_scores.py


**Getting Figure 6** (Algorithmic Evaluation Constrained with pretrained face-PAD) ...

To compute error rates for different types of attack as presented in Figure 6, please execute following scripts:

.. code-block:: sh

    $ #For IQM system
    $ bin/algorithmic_constrained_evaluation.py -r experiments/configuration_iqm_from_scores_pretrained.py
    $ #For Gradiant system
    $ bin/algorithmic_constrained_evaluation.py -r experiments/configuration_gradiant_from_scores_pretrained.py


**Getting Table 2** (End-to-end Evaluation) ...

To compute error rates for different types of attack as presented in Table 2, please execute the following script:

.. code-block:: sh

    $ #For IQM system
    $ bin/end_to_end_evaluation.py -r experiments/end_to_end_iqm.py

Please, consider these measurements are not reproducibles due to depends on the execution processor. Reported table was calculated with a Intel (R) XeonRCPU X5675 @3.07GHz


Retrieve the results
~~~~~~~~~~~~~~~~~~~~

To make easier obtaining the results, there is a script which will put together reported tables into a html page.

.. code-block:: sh

    $ bin/retrieve_results.py

Results will be stored in result/chapter/summary.html
