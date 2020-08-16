default:
	@echo 'Targets:'
	@echo '  all'
	@echo '  test-easter'
	@echo '  test-day-number'
	@echo '  test-julian'
	@echo '  test-time'
	@echo '  test-coordinate'
	@echo '  test-sun'
	@echo '  test-planet-comet-binary'
	@echo '  test-moon'
	@echo '  test-eclipses'

all: test-easter test-day-number test-julian test-time test-coordinate test-sun test-planet-comet-binary test-moon test-eclipses

test-easter:
	@./test-date-of-easter.py -v

test-day-number:
	@./test-day-number.py

test-julian:
	@./test-julian.py

test-time:
	@./test-time.py

test-coordinate:
	@./test-coordinate.py

test-sun:
	@./test-sun.py

test-planet-comet-binary:
	@./test-planet-comet-binary.py

test-moon:
	@./test-moon.py

test-eclipses:
	@./test-eclipses.py