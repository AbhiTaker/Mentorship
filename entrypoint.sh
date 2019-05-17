#!/usr/bin/env bash
neo4j-community-3.5.5/bin/neo4j start
sleep 30
python3 manage.py install_labels
python3 manage.py runserver 0.0.0.0:8000
