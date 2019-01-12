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

def test_result_after_recipes_one(rec_number=5):
  x = RecipeCalculator(rec_number)
  x.add_starting_conditions()
  for count in range(rec_number+10):
    x.proceed_one_line()
  assert x.get_next_ten_answer() == "0124515891"

#https://docs.pytest.org/en/latest/example/parametrize.html is worth looking into

def test_result_after_recipes_two(rec_number=18):
  x = RecipeCalculator(rec_number)
  x.add_starting_conditions()
  for count in range(rec_number+10):
    x.proceed_one_line()
  assert x.get_next_ten_answer() == "9251071085"

def test_result_after_recipes_three(rec_number=2018):
  x = RecipeCalculator(rec_number)
  x.add_starting_conditions()
  for count in range(rec_number+10):
    x.proceed_one_line()
  assert x.get_next_ten_answer() == "5941429882"


