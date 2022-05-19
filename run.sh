#!/bin/bash

PATTERNS_STR='
iterator
adapter
template_method
factory_method
singleton
prototype
builder
abstract_factory
bridge
strategy
composite
decorator
visitor
chain_of_responsibility
facade
mediator
observer
memento
state
flyweight
proxy
command
interpreter
'
PATTERNS_ARRAY=(`echo $PATTERNS_STR`)

if [ $# -ne 1 ]; then
  echo "specify pattern"
  exit 1
fi

if printf '%s\n' "${PATTERNS_ARRAY[@]}" | grep -qx "$1"; then
  poetry run pytest --no-cov tests/test_200_func/$1
else
  echo "not found: $1"
  exit 1
fi
