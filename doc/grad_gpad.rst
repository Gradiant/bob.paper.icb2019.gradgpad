.. vim: set fileencoding=utf-8 :
.. Biometrics Team  <biometrics.support@gradiant.com>

=======================
The GRAD-GPAD framework
=======================

In this paper, we present a novel evaluation framework to help the research community to address the problem of generalization in face-PAD. Our framework is publicly available as a Python package under the acronym
GRAD-GPAD (Generalization Representation over Aggregated Datasets for Generalized Presentation Attack Detection). This framework provides a common taxonomy of existing datasets and allows to evaluate face-PAD algorithms
from additional points of view, revealing new interesting properties. The GRAD-GPAD framework is extendable and scalable by design. This will help researchers to create new
protocols, to define categorizations over different datasets in order to make them compatible, and to enable the addition of new datasets.

The GRAD-GPAD framework has a top-down design and provides a very convenient level of abstraction. The following figure shows the proposed dataset evaluation pipeline, where circles with dotted lines represent the customizable and easyto-extend elements. Each of these elements in the framework follows a specific interface to work properly. Thus,
we can add, for instance, a new Dataset (e.g. using some videos recorded for an specific use case), or a new implementation of a Feature Extractor to evaluate an algorithm
or even create an ad-hoc Protocol.

.. image:: img/diagram_framework_icb2019.png
   :scale: 50 %
   :alt: proposed_evaluation_framework
   :align: center

Figure 1: Overview of GRAD-GPAD evaluation framework


GRAD-GPAD presents two main stages:

    i) feature extraction, where features are computed for each input video applying a preprocessing step and following the interface of the Feature Extractor; and
    ii) evaluation, where a filtering step is applied, using the already extracted features and the common categorization of the datasets, to train and test over the selected features.


