import time

from rowboat import ENV
from rowboat.plugins import BasePlugin as Plugin


def to_tags(obj):
    return [u'{}:{}'.format(k, v) for k, v in obj.items()]


class StatsPlugin(Plugin):
    global_plugin = True

    def load(self, ctx):
        super(StatsPlugin, self).load(ctx)
