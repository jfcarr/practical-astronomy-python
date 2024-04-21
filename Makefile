PYEXE = python3

default:
	@echo 'Targets:'
	@echo '  all-tests'
	@echo '  test-easter'
	@echo '  test-day-number'
	@echo '  test-julian'
	@echo '  test-time'
	@echo '  test-coordinate'
	@echo '  test-sun'
	@echo '  test-planet-comet-binary'
	@echo '  test-moon'
	@echo '  test-eclipses'
	@echo '  build'
	@echo '  upload-test'
	@echo '  upload'

all-tests: test-easter test-day-number test-julian test-time test-coordinate test-sun test-planet-comet-binary test-moon test-eclipses

test-easter:
	@$(PYEXE) test_date_of_easter.py

test-day-number:
	@$(PYEXE) test_day_number.py

test-julian:
	@$(PYEXE) test_julian.py

test-time:
	@$(PYEXE) test_time.py

test-coordinate:
	@$(PYEXE) test_coordinate.py

test-sun:
	@$(PYEXE) test_sun.py

test-planet-comet-binary:
	@$(PYEXE) test_planet_comet_binary.py

test-moon:
	@$(PYEXE) test_moon.py

test-eclipses:
	@$(PYEXE) test_eclipses.py

build:
	$(PYEXE) -m build

upload-test: build
	$(PYEXE) -m twine upload --repository testpypi dist/*

upload: build
	$(PYEXE) -m twine upload dist/*
