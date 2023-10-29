class User:
    def role():
        return "user"

    def can_process_admin(self):
        return False

    def set_name(self, name):
        self.name = name
