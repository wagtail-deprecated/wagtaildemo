from fabric.api import *


env.roledefs = {
    'demo': ['dokku@demo.torchboxapps.com'],
}


def dokku(command, **kwargs):
    kwargs.setdefault('shell', False)
    return run(command, **kwargs)


class DemoEnvironment(object):

    def __init__(self, app, branch):
        self.app = app
        self.branch = branch
        self.name = app + '-' + branch.replace('/', '-')

    def set_config(self, config):
        config_string = ' '.join([
            name + '=' + value
            for name, value in config.items()
        ])
        dokku('config:set %s %s' % (self.name, config_string), warn_only=True)

    def run(self, command, interactive=False):
        dokku('run %s %s' % (self.name, command))

    def django_admin(self, command, interactive=False):
        self.run('django-admin %s' % command, interactive=interactive)

    def push(self):
        local('git push %s:%s %s:master' % (env['host_string'], self.name, self.branch))

    def push_postgres_data(self, localdb):
        local('pg_dump -c --no-acl --no-owner %s | ssh %s "postgres:connect %s"' % (localdb, env['host_string'], self.name))
        self.django_admin('migrate')
        self.django_admin('update_index')

    def exists(self):
        return dokku('config %s' % self.name, quiet=True).succeeded

    def create(self):
        # Create app
        dokku('apps:create %s' % self.name)

        # Create database
        dokku('postgres:create %s' % self.name)
        dokku('postgres:link %s %s' % (self.name, self.name))

        # Create redis instance
        dokku('redis:create %s' % self.name)
        dokku('redis:link %s %s' % (self.name, self.name))

        # Link to central Elasticsearch instance
        dokku('elasticsearch:link elasticsearch %s' % self.name)

        # Mount media folder
        dokku('docker-options:add %s deploy "-v /var/lib/app-media/%s/:/app/media/"' % (self.name, self.name))
        dokku('docker-options:add %s run "-v /var/lib/app-media/%s/:/app/media/"' % (self.name, self.name))

        # Extra configuration
        self.set_config({
            'APP_NAME': self.name,
            'DJANGO_SETTINGS_MODULE': 'wagtaildemo.settings.heroku',
            'SECRET_KEY': 'demo',
            'ALLOWED_HOSTS': self.name + '.demo.torchboxapps.com',
            'MEDIA_URL': 'http://media.demo.torchboxapps.com/%s/' % self.name,
        })

    def update(self):
        self.push()
        self.django_admin('migrate')
        self.django_admin('update_index')


@roles('demo')
def demo(subcommand='deploy'):
    branch = local('git branch | grep "^*" | cut -d" " -f2', capture=True)

    env = DemoEnvironment('wagtail', branch)

    if subcommand == 'deploy':
        # Create the environment
        if not env.exists():
            print("Creating demo environment for %s..." % branch)
            env.create()

        # Update it
        print("Updating demo environment...")
        env.update()
    elif subcommand == 'pushdb':
        # Check the environment exists
        if not env.exists():
            raise Exception("Demo environment doesn't exist yet. Please run 'fab demo' first.")

        # Push data
        env.push_postgres_data(localdb='wagtaildemo')
    else:
        raise Exception("Unrecognised command: " + subcommand)