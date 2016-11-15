#!/bin/sh

template_zip () {
    zip -r ../django-template.zip .
}

template_create () {
    mkdir $1
    django-admin startproject $1 $1 --template=django-template.zip --extension=py,md,yml --name=Makefile,.coveragerc,.gitignore
}
