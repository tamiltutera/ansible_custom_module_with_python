#!/usr/bin/python

from ansible.module_utils.basic import *

def display_arguments(data):
    first_name = data['first_name']
    last_name = data['last_name']
    mobile_number = data['mobile_number']
    result = {"First Name": first_name, "Last Name" : last_name, "Mobile": mobile_number}
    return False, True, result

def main():
    fields = {
        "first_name": {"required": True, "type": "str"},
        "last_name": {"required": True, "type": "str"},
        "mobile_number": {"required": True, "type": "int"}
    }

    module = AnsibleModule(argument_spec=fields)
    is_error, has_changed, result = display_arguments(module.params)
    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Some value is missing", changed=has_changed, meta=result)

if __name__ == "__main__":
    main()