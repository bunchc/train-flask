#!/bin/bash
#
# @script           init.sh

trainapi init && FLASK_ENV=development trainapi run --host 0.0.0.0 --debugger