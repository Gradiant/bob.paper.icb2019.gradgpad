#!/usr/bin/env bash

function main(){
    install_package
    download_resources
    run_experiment_quality_based
    run_experiment_color_based
    retrieve_summary_results
}

function install_package(){
    python clean.py
    python bootstrap-buildout.py
    bin/buildout
}

function download_resources(){
    bin/download_resources.py -v
}

function run_experiment_quality_based(){
    bin/algorithmic_constrained_evaluation.py -r experiments/quality_based/configuration_msu_iqm_face_cropped.py
}

function run_experiment_color_based(){
    bin/algorithmic_constrained_evaluation.py -r experiments/color_based/configuration_boulkenafet_face_cropped.py
}

function retrieve_summary_results(){
    bin/create_summary_table.py -bp resources_bob_paper_icb2019_gradgpad/msuiqm_face_cropped/ -rp result/quality_based
    bin/create_summary_table.py -bp resources_bob_paper_icb2019_gradgpad/boulkenafet_face_cropped/ -rp result/color_based
}

main