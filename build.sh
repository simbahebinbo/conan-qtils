#!/bin/bash

conan remove qtils/0.0.4 -c
conan create . --version=0.0.4 --name=qtils --build=missing --update