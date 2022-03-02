.PHONY: help freeze mitm up test_time normal_tests remote_tests selenium_wire_tests

VENV = deactivate >/dev/null 2>&1 ; sh .venv/bin/activate
MITMPROXY_PORT = 9137

# this is meant to silence `ResourceWarning: unclosed`

# The — shm-size option increases the size of the /dev/shm directory, which is a temporary file storage system.
# This is because the default shared memory on the container is too small for Chrome to run.

help:
	@echo "help: ---->"
	@echo
	@echo "freeze:                  freeze Python libraries"
	@echo "mitm:                    runs mitmproxy"
	@echo "up:                      runs brings up the standalone selenium chrome"
	@echo "test_time:               runs test_time for the current time in JS"
	@echo "normal_tests:            runs normal_tests with Selenium"
	@echo "remote_tests:            runs remote_tests using standlone chrome in docker"
	@echo "selenium_wire_tests:     runs selenium_wire_tests using selenium_wire"

freeze:
	@$(VENV) && pip freeze | egrep -i \
	"requests|cryptography|selenium|seleniumwire|mitmproxy|undetected-chromedriver|python-dotenv|pillow" \
	> requirements.txt

mitm:
	@$(VENV) && mitmproxy --listen-host 0.0.0.0 --listen-port $(MITMPROXY_PORT) --save-stream-file logs/bots.mitm

up:
	@docker-compose --project-name bots up --remove-orphan -d

test_time:
	@$(VENV) && python -m unittest normal_tests.test_browsers.TestHeadlessBrowsers.test_time

normal_tests:
	@$(VENV) && python -m unittest discover normal_tests

remote_tests:
	@$(VENV) && python -m unittest discover remote_tests

selenium_wire_tests:
	@$(VENV) && python -m unittest discover selenium_wire_tests

specific_git_config:
	@git config user.name "Chukwudi Nwachukwu"
	@git config user.email "theichux@gmail.com"
	@git config credential.username "ichux"
	
	@git config --get user.name
	@git config --get user.email
	@git config --get credential.username
