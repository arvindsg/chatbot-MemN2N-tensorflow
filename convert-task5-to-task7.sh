#!/bin/bash
cat $1|grep -v -E  "R\_|api" >$2
