class Person:
    def __init__(self, name, restrictions, email, address):
        self.name = name
        self.restrictions = restrictions
        self.email = email
        self.address = address

    def canGiveTo(self, recipient):
        if recipient.name in self.restrictions:
            print("BAD MATCH: %s %s" % (recipient.name, self.name))
        return not (recipient.name == self.name or recipient.name in self.restrictions)
