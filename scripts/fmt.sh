#!/usr/bin/env bash

set -eoux pipefail

(
  cd scripts
  chmod +x ./*.sh
  shfmt -i 2 -ci -sr -bn -s -w ./*.sh
)

(
  prettier --write README.md
  prettier --write docker-compose.yaml
)

(
  cd airflow
  chmod +x ./*.sh
  shfmt -i 2 -ci -sr -bn -s -w ./*.sh
  prettier --write docker-compose.yaml
  black ./**/*.py
)

(
  cd dag_stack
  find . -type f -name "*.md" | xargs -L 1 prettier --write
  find . -type f -name "*.yml" | xargs -L 1 prettier --write
  find . -type f -name "*.json" | xargs -L 1 prettier --write
  black ./**/*.py
)

(
  cd dbt_demo
  find . -type f -name "*.md" | xargs -L 1 prettier --write
  find . -type f -name "*.yml" | xargs -L 1 prettier --write
)

(
  cd ge_demo
  find . -type f -name "*.yml" | xargs -L 1 prettier --write
  find . -type f -name "*.json" | xargs -L 1 prettier --write
  black ./**/*.py
)
