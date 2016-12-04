#!/bin/sh

template_zip () {
    zip -r ../django-template.zip .
}

template_create () {
    PROJECT_NAME=$1; mkdir $PROJECT_NAME && django-admin startproject $PROJECT_NAME $PROJECT_NAME --template=django-template.zip --extension=py,md,yml,ini,sh --name=Makefile,.coveragerc,.gitignore
}
