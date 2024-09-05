#!/bin/bash

conan remove qtils/0.0.4 -c
conan create . --build=missing --update