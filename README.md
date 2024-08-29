# Storm CLI

Storm CLI is a command-line interface tool designed to streamline the development of server-side applications using the Storm framework. Inspired by the NestJS CLI, Storm CLI provides a powerful suite of commands to scaffold projects, generate boilerplate code, run development servers, and manage your application's lifecycle.

## Table of Contents
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Commands](#commands)
  - [new](#new)
  - [generate (g)](#generate-g)
  - [serve](#serve)
  - [build](#build)
  - [test](#test)
  - [lint](#lint)
  - [migrate](#migrate)
  - [console](#console)
  - [config](#config)
  - [deploy](#deploy)
  - [env](#env)
  - [cache](#cache)
  - [update](#update)
  - [plugin](#plugin)
  - [doctor](#doctor)
  - [logs](#logs)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

You can install Storm CLI using pip:

```bash
pip install storm-cli
```

## Getting Started

To create a new Storm project, use the `new` command:

```bash
storm new my-storm-app
```

This command will scaffold a new Storm project in a directory named `my-storm-app` with a basic structure and initial setup.

## Commands

### `new`

Scaffolds a new Storm project.

```bash
storm new <project-name> [options]
```

**Options:**
- `--skip-install`: Skip installing dependencies.
- `--template <template-name>`: Use a specific project template.

### `generate` (or `g`)

Generates a new resource within the project.

```bash
storm generate <type> <name> [options]
```

**Types:**
- `module`
- `controller`
- `service`
- `guard`
- `middleware`
- `interceptor`
- `filter`
- `entity`
- `resource`

**Options:**
- `--dry-run`: Show what files would be created without actually creating them.
- `--flat`: Generate files without a nested folder.

### `serve`

Starts the application server for development.

```bash
storm serve [options]
```

**Options:**
- `--port <port>`: Specify the port to serve on (default: 3000).
- `--watch`: Restart the server on file changes.
- `--debug`: Run in debug mode for additional logging and debugging.

### `build`

Builds the Storm application for production deployment.

```bash
storm build [options]
```

**Options:**
- `--prod`: Build in production mode.
- `--output <directory>`: Specify the output directory for the build files.

### `test`

Runs the tests for the Storm application.

```bash
storm test [options]
```

**Options:**
- `--watch`: Run tests in watch mode.
- `--coverage`: Generate a code coverage report.
- `--filter <pattern>`: Run tests that match a specific pattern.

### `lint`

Lints the project’s code to enforce coding standards.

```bash
storm lint [options]
```

**Options:**
- `--fix`: Automatically fix linting errors where possible.
- `--rules <rule-set>`: Use a specific set of linting rules.

### `migrate`

Manages database migrations.

```bash
storm migrate <subcommand> [options]
```

**Subcommands:**
- `run`: Applies pending migrations.
- `revert`: Reverts the last applied migration.
- `create <name>`: Creates a new migration file.
- `status`: Shows the current status of migrations.

### `console`

Opens an interactive REPL session within the context of the application.

```bash
storm console
```

### `config`

Manages configuration settings for the Storm CLI.

```bash
storm config <subcommand>
```

**Subcommands:**
- `get <key>`: Retrieves a configuration value.
- `set <key> <value>`: Sets a configuration value.
- `list`: Lists all configuration settings.

### `deploy`

Deploys the application to a specified environment.

```bash
storm deploy [options]
```

**Options:**
- `--env <environment>`: Specify the environment for deployment (e.g., production, staging).
- `--dry-run`: Simulate the deployment without actually performing it.

### `env`

Manages environment variables for the application.

```bash
storm env <subcommand> [options]
```

**Subcommands:**
- `add <key> <value>`: Adds a new environment variable.
- `remove <key>`: Removes an environment variable.
- `list`: Lists all environment variables.

### `cache`

Manages caching mechanisms used by the application.

```bash
storm cache <subcommand>
```

**Subcommands:**
- `clear`: Clears the application cache.
- `status`: Displays the status of the cache.

### `update`

Updates the Storm CLI to the latest version.

```bash
storm update [options]
```

**Options:**
- `--force`: Force update even if the current version is up-to-date.

### `plugin`

Manages plugins for the Storm framework.

```bash
storm plugin <subcommand> [options]
```

**Subcommands:**
- `install <plugin-name>`: Installs a plugin.
- `uninstall <plugin-name>`: Uninstalls a plugin.
- `list`: Lists all installed plugins.

### `doctor`

Runs diagnostics on the project to identify common problems or misconfigurations.

```bash
storm doctor [options]
```

**Options:**
- `--fix`: Automatically attempt to fix detected issues.

### `logs`

Displays logs for the application.

```bash
storm logs [options]
```

**Options:**
- `--tail`: Continuously stream logs.
- `--filter <pattern>`: Filter logs based on a specific pattern.

## Configuration

Configuration for the CLI can be managed using the `storm config` command. This allows you to set and retrieve configuration options specific to your development environment and needs.

## Contributing

Contributions are welcome! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to get started.

## License

Storm CLI is open-source software licensed under the [MIT license](LICENSE).
