#!/usr/bin/env python
# coding=utf-8

# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/inkscape_artcards_attrs

import sys
from inkex import EffectExtension, NSS


# for debug output
def eprint(*args, **kwargs):
    # print to stderr
    print(*args, file=sys.stderr, **kwargs)


class ArtcardsAttrs(EffectExtension):

    _namespace = 'artcards'
    _available_types = ['image', 'text']

    def effect(self):
        # main method for Effect action
        # if namespace not exists in the namespace map
        if self._namespace not in NSS:
            namespace_uri = 'http://' + self._namespace + '.org/namespace'
            self.svg.add_namespace(self._namespace, namespace_uri)
            NSS[self._namespace] = namespace_uri
        # set required attributes
        if self.options.ca_type and (self.options.ca_type in self._available_types):
            # add required attributes for each selected object
            for selected_obj in self.svg.selection:
                # type
                selected_obj.set(
                    self._namespace + ':type',
                    self.options.ca_type
                )
                # lib
                selected_obj.set(
                    self._namespace + ':lib',
                    self.options.ca_lib
                )
                # id
                selected_obj.set(
                    self._namespace + ':id',
                    self.options.ca_id
                )

    def add_arguments(self, pars):
        # parse arguments from the UI
        pars.add_argument(
            '--ca_type',
            type=str,
            default='',
            help='Type'
        )
        pars.add_argument(
            '--ca_lib',
            type=str,
            default='',
            help='Lib'
        )
        pars.add_argument(
            '--ca_id',
            type=str,
            default='',
            help='Id'
        )


if __name__ == '__main__':
    ArtcardsAttrs().run()
