# mercury-fixture

A throwaway repo that the integration test in [agent-runs](https://github.com/thomas-whitley/agent-runs) runs a real repo chore against. The test asks for a small change, the chore runs this repo's tests, opens a pull request on green, and the test closes that pull request and deletes its branch.

The tests use only the standard library, so the chore installs nothing. Run them with `python -m unittest -v`, which is the `test_command` listed for this repo in `mercury.yaml`.

`main` is protected, so nothing reaches it except through a pull request. Any open pull request or `agent/*` branch left behind is a test that failed before cleaning up, and is safe to close or delete.

# Contributing

If you wish to contribute, please ensure that your changes are well-tested. New features must include appropriate tests.