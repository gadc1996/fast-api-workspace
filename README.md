# Django Workspace
The main objetive of this repository is to serve as a fullstack django workspace, with integration with Google Cloud services, and powered by dev containers for development

## Development setup
- Create a `.env.dev` file using example
```
cp .env.example .env.dev
```

- Open dev container:

  - For the first time se1tup, you need to rebuild and reopen in a container:
    1. Press `F1` to open the command palette.
    2. Type `Remote-Containers: Rebuild and Reopen in Container` and select it from the dropdown list.

  - For subsequent times, you just need to reopen in a container:
    1. Press `F1` to open the command palette.
    2. Type `Remote-Containers: Reopen in Container` and select it from the dropdown list.

## Interacting with AWS
The workspace has comes with [eb-cli](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html), preinstalled, add credentials as env variables in [.env.dev](.env.dev)

Also, some convenience scripts are placed in aws directory

### Managing remote env variables
To define variables in cloud instance, create a file named .env.aws, this will be loaded to the
enviroment when running
```
python aws/setup.py
```

or update the active enviroment using
```
python aws/setenv.py
```
