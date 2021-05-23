#!/bin/bash
PWD=`pwd`
python3 -m venv env
activate () {
    . $PWD/env/bin/activate
}
activate
pip install -r requirements.txt

PATH=$PATH":$PWD"

. ./llm