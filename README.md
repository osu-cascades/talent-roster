# OSU Cascades Computer Science Talent Roster

The _Talent Roster_ is an online list of student profiles to facilitate
connections with potential employers.

## Development

This is a Django project with one application, using a Python 3 environment
managed by [venv](https://docs.python.org/3/library/venv.html) and
[pipenv](https://github.com/pypa/pipenv). After you clone this repository,
`cd` into the repo root and create the virtual environment:

`python -m venv .`

Next, activate the environment:

`source bin/activate`

Now install [pipenv](https://github.com/pypa/pipenv):

`pip install pipenv`

From here on out, you will use `pipenv` to install all dependencies. Do it now:

`pipenv install`

This will install the dependencies listed in _Pipfile_.

### Database Configuration

We expect you to use PostgreSQL in development, since that is what we intend to
use in produciton. We suggest creating a development database named
*talent_roster_development* with appropriate ownership.

Next, configure this Django project by copying _.env.example_ to _.env_.
This is your environment-specific configuration file. Set `DATABASE_URL` to
a valid database url appropriate for your local development environment.

TODO database setup, initial migrations, starting server.

## Testing

TODO

## Deployment

TODO

(c) 2018 Ryan Kocjan and Yong Bakos. All rights reserved.
