#incomplete
class RecipeCalculator:
  def __init__(self, input_value):
    self.input_value = input_value

  def add_starting_conditions(self):
    self.recipes = [3,7]
    self.elf1 = 0
    self.elf2 = 1
    self.recipes_length = 2
    self.new_recipe_length = 0

  def get_input_value_out(self):
    return self.input_value

  def move_elf(self, elf):
    elf = (elf +4)%self.recipes_length
  
  def sum_elfs_recipes(self, elf1, elf2):
    self.new_recipe_length = self.recipes[self.elf1] + self.recipes[self.elf2]

  def add_new_recipes(self, new_recipe_length):
    self.recipes.extend([int(d) for d in str(new_recipe_length)])

  def proceed_one_line(self):
    self.move_elf(self.elf1)
    self.move_elf(self.elf2)
    self.sum_elfs_recipes(self.elf1, self.elf2)
    self.add_new_recipes(self.new_recipe_length)


  def print_next_ten_answer(self):
    print(self.recipes[self.input_value:(self.input_value+11)])

  def get_next_ten_answer(self):
    print(self.recipes[self.input_value:(self.input_value+11)])
    return sum(self.recipes[self.input_value:(self.input_value+11)])



x = RecipeCalculator(846021)