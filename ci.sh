#!/usr/bin/env bash

function main(){
    install_package
    test_package
    doc
}

function install_package(){
    python clean.py
    python bootstrap-buildout.py
    bin/buildout
}

function test_package(){
    bin/nosetests -v
}

function doc(){
    bin/sphinx-build -b html doc doc/html
    cd doc/html
    echo "" >> .nojekyll
    cd ../..
}

main