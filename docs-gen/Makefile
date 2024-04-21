default:
	@echo 'Targets:'
	@echo ' view            View documentation in Firefox.'
	@echo ' build-python    Build documentation from Python sources.'

view: build-python
	@firefox ../docs/index.html &

build-python:
	@-rm -rf ../docs
	@mkdir ../docs
	@doxygen

