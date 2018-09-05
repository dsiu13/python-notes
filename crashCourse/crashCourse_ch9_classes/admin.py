from user import Admin

jeff = Admin('jeff', 'winger', 'wingman', 'hero@law.com', 'colorado')
jeff.describe_user()

jeff_privileges = [
    'teach',
    'drink',
    'give inspiring speeches'
    ]

jeff.privileges.privileges = jeff_privileges
jeff.privileges.show_privileges()
