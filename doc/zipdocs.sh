#! /bin/bash

rm _build/html.zip
cd _build/html
zip -r -9 -v ../html.zip *
