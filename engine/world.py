class World:
    def __init__(self):
        self.entities = {}
        self.next_entity_id = 1
    
    def create_entity(self):
        entity_id = self.next_entity_id
        self.entities[entity_id] = {}
        self.next_entity_id += 1
        return entity_id