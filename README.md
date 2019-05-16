# bob.paper.icb2019.gradgpad 

<!---
[![Build Status](https://travis-ci.org/Gradiant/bob.paper.icb2019.gradgpad.svg?branch=master)](https://travis-ci.org/Gradiant/bob.paper.icb2019.gradgpad) [![Doc](http://img.shields.io/badge/docs-latest-orange.svg)](https://gradiant.github.io/bob.paper.icb2019.gradgpad/)
-->
 
[Bob](https://www.idiap.ch/software/bob/) package to reproduce the work carried out in the paper [Generalized Presentation Attack Detection: a face anti-spoofing evaluation proposal](https://arxiv.org/abs/1904.06213) accepted in the [12th IAPR International Conference On Biometrics](http://www.icb2019.org/).

:construction:
~~~
The code will be available at the beginning of May.

Ongoing tasks:
	- Migrating to python 3
	- Preparing the environment (with conda)
	- Preparing docker image
~~~

## Abstract 

_Over the past few years, Presentation Attack Detection (PAD) has become a fundamental part of facial recognition systems. Although much effort has been devoted to anti-spoofing research, generalization in real scenarios remains a challenge. In this paper we present a new opensource evaluation framework to study the generalization capacity of face PAD methods, coined here as face-GPAD. This framework facilitates the creation of new protocols focused on the generalization problem establishing fair procedures of evaluation and comparison between PAD solutions. We also introduce a large aggregated and categorized dataset to address the problem of incompatibility between publicly available datasets. Finally, we propose a benchmark adding two novel evaluation protocols: one for measuring the effect introduced by the variations in face resolution, and the second for evaluating the influence of adversarial operating conditions._

## Acknowledgements

If you use this framework, please cite the following publication:

~~~
@INPROCEEDINGS{Costa-Pazo-ICB-2019,
	title = {Generalized Presentation Attack Detection: a face anti-spoofing evaluation proposal},
	author={Costa-Pazo, Artur and David Jim\'enez-Cabello and V\'azquez-Fern\'andez, Esteban and Alba-Castro, Jos\'e Luis and L\'opez-Sastre, Roberto J.},
	year = {2019},
	booktitle={The 12th IAPR International Conference On Biometrics (ICB)}
}
~~~

## Disclaimer 

Third party publicly available datasets are not managed by Gradiant. 
To access them, please contact each of the institutions responsible for 
each dataset. The license for the use of these datasets must be consulted
with each institution.

Hope the following table will help you download publicly available datasets.

| Dataset | Link | 
| --- | --- | 
| CASIA-FASD | [http://www.cbsr.ia.ac.cn/english/FASDB_Agreement/Agreement.pdf](http://www.cbsr.ia.ac.cn/english/FASDB_Agreement/Agreement.pdf) |
| REPLAY-ATTACK | [https://www.idiap.ch/dataset/replayattack](https://www.idiap.ch/dataset/replayattack) | 
| 3DMAD | [https://www.idiap.ch/dataset/3dmad](https://www.idiap.ch/dataset/3dmad) | 
| MSU-MFSD | [http://biometrics.cse.msu.edu/Publications/Databases/MSUMobileFaceSpoofing/index.htm](http://biometrics.cse.msu.edu/Publications/Databases/MSUMobileFaceSpoofing/index.htm) | 
| UVAD | [https://recodbr.wordpress.com/code-n-data/#UVAD](https://recodbr.wordpress.com/code-n-data/#UVAD) | 
| REPLAY-MOBILE | [https://www.idiap.ch/dataset/replay-mobile](https://www.idiap.ch/dataset/replay-mobile) | 
| HKBU (v1) | [http://rds.comp.hkbu.edu.hk/mars/](http://rds.comp.hkbu.edu.hk/mars/) |
| OULU-NPU  | [https://sites.google.com/site/oulunpudatabase/](https://sites.google.com/site/oulunpudatabase/) | 
| ROSE-YOUTU | [http://rose1.ntu.edu.sg/Datasets/faceLivenessDetection.asp](http://rose1.ntu.edu.sg/Datasets/faceLivenessDetection.asp) | 
| SIW | [http://cvlab.cse.msu.edu/spoof-in-the-wild-siw-face-anti-spoofing-database.html](http://cvlab.cse.msu.edu/spoof-in-the-wild-siw-face-anti-spoofing-database.html) | 
| CS-MAD | [https://www.idiap.ch/dataset/csmad](https://www.idiap.ch/dataset/csmad) | 


## Installation 

#### Installation With Docker 

The fastest way to contact the package is to use docker. 

You can download the docker image from dockerhub

~~~
docker pull acostapazo/bob.paper.icb2019.gradgpad:latest 
~~~

or build it from Dockerfile

~~~
docker build --no-cache -t acostapazo/bob.paper.icb2019.gradgpad:latest  .
~~~

To check if everything is alright you can run the ci.sh script with:

~~~
docker run -v $(pwd):/bob.paper.icb2019.gradgpad acostapazo/bob.gradiant.face.databases:latest bin/bash -c "source activate bob.gradiant.face.databases; cd bob.gradiant.pad.evaluator; ./ci.sh"
~~~

#### Installation With Conda


1. Install conda -> https://conda.io/docs/user-guide/install/index.html

2. Create the conda env

~~~
    conda env create -f envs/ubuntu_environment.yml
~~~

or if run this in macosx platform

~~~
    conda env create -f envs/mac_environment.yml
~~~

3. Activate the environment and add some channels

~~~
   source activate bob.paper.icb2019.gradgpad
~~~


## Test

~~~
  bin/nosetests -v
~~~

## Clean

~~~
  python clean.py
~~~

## Coverage

~~~  
  bin/coverage run -m unittest discover
  bin/coverage html -i
  bin/coverage xml -i
~~~

Coverage result will be store on htmlcov/.

## Doc

~~~
bin/sphinx-build -b html doc/ doc/html/
~~~


## Reproducible Research

1. Build the package 
    
~~~
    python clean.py
    python bootstrap-buildout.py
    bin/buildout
~~~

2. Download the resources

~~~
bin/download_resources.py -v
~~~
 
3. Execute the experiments

~~~
 bin/algorithmic_constrained_evaluation.py -r experiments/quality_based/configuration_msu_iqm_face_cropped.py 
 bin/algorithmic_constrained_evaluation.py -r experiments/color_based/configuration_boulkafanet_face_cropped.py 
~~~


