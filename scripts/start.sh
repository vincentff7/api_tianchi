#!/bin/bash

uwsgi_start_comment="/home/quwm/workspace/web_hichao/bin/uwsgi --ini-paste "

if [ $# -eq 0  ]; then
        INI="develop.ini"
    else
            INI=$1
        fi

        $uwsgi_start_comment $INI
