from pokemon_dict_151 import pokemon_list_151, pokemon_types_151


class Pokemon:
    def __init__(self, pokemon_list, pokemon_types):
        self.pokemon_list = pokemon_list
        self.pokemon_types = pokemon_types

    def add_pokemon(self, id, name, type):
        if int(id) in self.pokemon_list:
            raise ValueError(f"Pokemon with id {id} already exists as {name}")
        self.pokemon_list[int(id)-1] = (name, type)
        with open("pokemon.txt", "a", encoding='utf-8') as f:
            f.write(f"Name and type for number {id} is {name}, {type}\n")

    def delete_pokemon(self, id):
        del self.pokemon_list[int(id)-1]
        with open("pokemon.txt", "r", encoding='utf-8') as f:
            lines = f.readlines()
        with open("pokemon.txt", "w", encoding='utf-8') as f:
            for line in lines:
                if str(id) not in line:
                    f.write(line)

    def search_by_id(self, pokemon_id):
        if int(pokemon_id) in self.pokemon_list:
            return (pokemon_id, self.pokemon_list[int(pokemon_id)-1][0], self.pokemon_list[int(pokemon_id)-1][1])
        return None

    def search_by_type(self, pokemon_type):
        ids = [id for id, p_type in self.pokemon_types.items(
        ) if p_type.lower() == pokemon_type.lower()]
        indexes = [idx for idx, (name, p_type) in self.pokemon_list.items(
        ) if p_type.lower() == pokemon_type.lower()]
        results = []
        for id in ids:
            index = indexes[ids.index(id)]
            results.append(
                (id, self.pokemon_list[index][0], self.pokemon_list[index][1]))
        return results

    def search_by_name(self, name):
        results = []
        for id, (pokemon_name, _) in self.pokemon_list.items():
            if name.lower() in pokemon_name.lower():
                results.append(
                    (id, pokemon_name, self.pokemon_list[int(id)-1][1]))
        return results

    def update_pokemon(self, id, name=None, type=None):
        if id not in self.pokemon_list:
            raise ValueError(f"Pokemon with id {id} not found")
        if name:
            self.pokemon_list[int(id)-1] = name
        if type:
            self.type = type

        # Find the line that we want to modify
        with open("pokemon.txt", "r", encoding='utf-8') as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            if str(id) in line:
                break
        else:
            raise ValueError(f"Pokemon with id {id} not found in file")

        # Modify the line
        if name and type:
            lines[i] = f"{id}: {name} is a {type} pokemon\n"
        elif name:
            lines[i] = f"{id}: {name} is a {self.type} pokemon\n"
        elif type:
            lines[i] = f"{id}: {self.pokemon_list[int(id)-1]} is a {type} pokemon\n"

        # Write the modified lines back to the file
        with open("pokemon.txt", "w", encoding='utf-8') as f:
            f.writelines(lines)


p = Pokemon(pokemon_list_151, pokemon_types_151)

print(p.search_by_id(37))
