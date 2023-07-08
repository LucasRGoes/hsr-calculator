.PHONY: unit-tests integration-tests tests run

unit-tests:
	python3 -m unittest -vvv tests.unit.test_light_cones

integration-tests:

tests: unit-tests integration-tests

run:
