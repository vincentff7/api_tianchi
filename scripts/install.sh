#!/bin/bash

rm -rf build
rm -rf dist
rm -rf hichao.egg-info
/home/quwm/.virtualenvs/webenv/bin/pip uninstall hichao  -y
/home/quwm/.virtualenvs/webenv/bin/python setup.py clean
/home/quwm/.virtualenvs/webenv/bin/python setup.py build
/home/quwm/.virtualenvs/webenv/bin/python setup.py install
