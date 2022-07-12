#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)


DOCUMENTATION = r'''
---
module: hello_world

short_description: This is hello world module

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is my longer description explaining hello world module.

options:
    hello_world:

# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - my_namespace.my_collection.my_doc_fragment_name

author:
    - Tamiltutera (@tamiltutera)
'''


from ansible.module_utils.basic import *

def main():
    module = AnsibleModule(argument_spec={})
    response = {"Hello": "world"}
    module.exit_json(changed=False,meta=response)


if __name__ == '__main__':
    main()