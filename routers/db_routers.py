from uservers.models import *
from productvers.models import *


class UserRouter:
    route_app_labels = {'uservers', 'auth', 'contenttypes', 'sessions', 'admin'}

    # permission to read database
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'user'
        return None

    # permission to write database
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'user'
        return None

    # permission to relations in database
    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    # permission to migrate database
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'user'
        return None


class ProductsRouter:
    route_app_labels = {'productvers', 'auth',
                        'contenttypes', 'sessions', 'admin'}

    # permission to read database
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'product'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'product'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    # permission to migrate database

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'product'
        return None