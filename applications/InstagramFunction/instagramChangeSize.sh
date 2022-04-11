#!/bin/bash
wmctrl -r 'Istekram' -b remove,maximized_horz,maximized_vert
wmctrl -r 'Istekram' -e 0,1200,100,500,800
wmctrl -r 'Istekram' -b add,above
