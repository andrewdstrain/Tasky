#!/bin/sh

source .env

ibmcloud cf set-env TaskyApp2 SECRET_KEY $SECRET_KEY && ibmcloud cf set-env TaskyApp2 DATABASE_URL "$DATABASE_URL" && ibmcloud cf restage TaskyApp2
