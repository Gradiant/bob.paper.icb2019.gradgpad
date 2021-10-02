# bob.paper.icb2019.gradgpad [![Build Status](https://travis-ci.org/Gradiant/bob.paper.icb2019.gradgpad.svg?branch=master)](https://travis-ci.org/Gradiant/bob.paper.icb2019.gradgpad) [![Doc](http://img.shields.io/badge/docs-latest-green.svg)](https://gradiant.github.io/bob.paper.icb2019.gradgpad/) 

 
 👉 👉 New version of `gradgpad` (v2) is already available in [https://github.com/acostapazo/gradgpad](https://github.com/acostapazo/gradgpad) 🗿 👈 👈
 
 
[Bob](https://www.idiap.ch/software/bob/) package to reproduce the work carried out in the paper [Generalized Presentation Attack Detection: a face anti-spoofing evaluation proposal](https://arxiv.org/abs/1904.06213) accepted in the [12th IAPR International Conference On Biometrics](http://www.icb2019.org/).

## Abstract 

_Over the past few years, Presentation Attack Detection (PAD) has become a fundamental part of facial recognition systems. Although much effort has been devoted to anti-spoofing research, generalization in real scenarios remains a challenge. In this paper we present a new opensource evaluation framework to study the generalization capacity of face PAD methods, coined here as face-GPAD. This framework facilitates the creation of new protocols focused on the generalization problem establishing fair procedures of evaluation and comparison between PAD solutions. We also introduce a large aggregated and categorized dataset to address the problem of incompatibility between publicly available datasets. Finally, we propose a benchmark adding two novel evaluation protocols: one for measuring the effect introduced by the variations in face resolution, and the second for evaluating the influence of adversarial operating conditions._

## Acknowledgements

If you use this framework, please cite the following publications:

~~~
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

@inbook{Costa-Pazo2019,
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


For more information about installation, reproducible research and how to use the GRAD-GPAD framework to evaluate your algorithms, please visit the official documentation in [![Doc](http://img.shields.io/badge/docs-latest-green.svg)](https://gradiant.github.io/bob.paper.icb2019.gradgpad/).




