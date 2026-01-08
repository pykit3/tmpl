# Build System

This directory contains shared build configuration for pykit3 packages.

## Files

- `common.mk` - Makefile targets included by the root Makefile

## Make Targets

| Target | Description |
|--------|-------------|
| `make test` | Run tests with pytest |
| `make lint` | Format and lint with ruff |
| `make doc` | Build documentation with MkDocs |
| `make readme` | Generate README.md with pk3 |
| `make release` | Bump version and create tag with pk3 |
| `make publish` | Publish to PyPI with pk3 |
| `make install` | Install package in editable mode |
| `make cov` | Run tests with coverage report |

## Dependencies

- `pk3` - pykit3 CLI tool for readme generation, tagging, and publishing
- `pytest` - Test runner
- `ruff` - Python linter and formatter
- `mkdocs` - Documentation generator
