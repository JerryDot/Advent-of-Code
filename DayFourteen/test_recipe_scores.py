from recipe_scores import RecipeCalculator


def test_class_exists():
  x = RecipeCalculator
  assert x is not False

def test_class_can_return_input_value():
  x = RecipeCalculator(10)
  assert x.get_input_value_out() == 10

def test_start_up_variables():
  x = RecipeCalculator(1)
  x.add_starting_conditions()
  assert x.elf1 == 0

def test_after_one_line():
  x = RecipeCalculator(1)
  x.add_starting_conditions()
  x.proceed_one_line()
  assert x.recipes == [3, 7, 1, 0]

def test_result_after_five_recipes():
  x = RecipeCalculator(5)
  x.add_starting_conditions()
  for count in range(10):
    x.proceed_one_line()
  x.print_next_ten_answer()
  assert x.get_next_ten_answer() == 36
