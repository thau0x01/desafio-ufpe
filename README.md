# Belvo security challenge

This application contains intentional security flaws which we're asking you to spot and fix.

We need your help to strengthen our fictitious secret codes' API. This API provides access to the codes we use for critical operations.

At the moment, we have 2 of them:
- safebox: we use this one to unlock our safebox containing top secret documentation.
- launch_codes: we use it to start operating a secret weapon. Only admins allowed.

At the moment we have 2 users that are allowed to retrieve those tokens. Having anyone else access these codes 
would be catastrophic for our business.

Also, we have a functionality that allows a user to read their own secrets. They cannot be viewed by anyone else, including admins. 

## What do you need to do

- Review the project, create a private repository and create one (or more) PRs for all the security issues you can find.
- Please share the private repository with the github user "belvo-hiring".

## Constraints
Focus on the entire contents of this repository - for simplicity sake, please maintain the current project structures (files/folders).

## Running
```
$ docker-compose up
```
