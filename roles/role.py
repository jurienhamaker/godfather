class Role:
    def __init__(self, name=None, role_id=None, description=''):
        self.name = name
        self.role_id = role_id
        self.description = description

    # str representation of role
    def __str__(self):
        return self.name

    # called when a player is lynched. takes the game object, and the player lynched
    async def on_lynch(self, game, player):
        pass

    def night_instructions(self, ctx):
        return None
