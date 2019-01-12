#incomplete
class RecipeCalculator:
  def __init__(self, input_value):
    self.input_value = input_value

  def add_starting_conditions(self):
    self.recipes = [3,7]
    self.elf1 = 0
    self.elf2 = 1
    self.recipes_length = 2
    self.new_recipe_value = 0

  def get_input_value_out(self):
    return self.input_value

  def move_elves(self):
    self.elf1 = (self.elf1 + 1 + self.recipes[self.elf1])%self.recipes_length
    self.elf2 = (self.elf2 + 1 + self.recipes[self.elf2])%self.recipes_length
    
  def sum_elfs_recipes(self, elf1, elf2):
    self.new_recipe_value = self.recipes[self.elf1] + self.recipes[self.elf2]

  def add_new_recipes(self, new_recipe_value):
    self.recipes.extend([int(d) for d in str(new_recipe_value)])
    self.recipes_length += len(str(new_recipe_value))

  def proceed_one_line(self):
    self.move_elves()
    self.sum_elfs_recipes(self.elf1, self.elf2)
    self.add_new_recipes(self.new_recipe_value)


  def _print_next_ten_answer(self):
    print(self.recipes[self.input_value:(self.input_value+10)])
    pass

  def get_next_ten_answer(self):
    #self._print_next_ten_answer()
    return ''.join(str(e) for e in self.recipes[self.input_value:(self.input_value+10)])



x = RecipeCalculator(846021)
x.add_starting_conditions()
for count in range(x.input_value+10):
  x.proceed_one_line()
print(x.get_next_ten_answer())
print(x.recipes[(x.input_value-2):(x.input_value+12)])
