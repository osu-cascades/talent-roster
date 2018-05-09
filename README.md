# OSU Cascades Computer Science Talent Roster

The _Talent Roster_ is an online list of student profiles to facilitate
connections with potential employers.

## Development

This is a Django project with one application, using a Python 3 environment
managed by [venv](https://docs.python.org/3/library/venv.html) and
[pipenv](https://github.com/pypa/pipenv). After you clone this repository,
`cd` into the repo root and create the virtual environment:

`python3 -m venv .`

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

Run the migrations to establish your database schema:

`./manage.py migrate`

Create your Django superuser record:

`./manage.py createsuperuser`

Start the server:

`./manage.py runserver`

## Testing

This application uses the default Django test client and python unittest via the
[green](https://github.com/CleanCut/green) test runner for color output. Ensure
that all static assets have been "collected":

`./manage.py collectstatic`

And then run the test suite:

`./manage.py test profiles`

You shouldn't run the `collectsatic` command every time. But if you see an error
like _Missing staticfiles manifest entry for X_, then run the `collectstatic`
command.

## Deployment

TODO

(c) 2018 Ryan Kocjan and Yong Bakos. All rights reserved.
