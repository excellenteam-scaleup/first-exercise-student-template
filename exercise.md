# Exercise 1 - Python Self Learning

**“Yam Mesika”** is a Hebrew Python tutorial that contains exercises and explanations.

[The Notebooks](https://github.com/PythonFreeCourse/Notebooks)

You need to hand in these 11 exercises from weeks 5, 6, and 7 of the notebooks. If your Python is rusty, I recommend reading weeks 3 and 4 as well.

## Exercises

### Week 5

- **5.1** - זו הדרך (*thats_the_way*), אין לי וִנִגְרֶט (*no_vinnigrete*)
- **5.2** - *cup of join* (*cup_of_join*), חתכת עוגה (*piece_of_cake*)
- **5.3** - לחששנית (*parsle_tongue*)
- **5.4** - כלים שלובים (*communicating_vessels*)

### Week 6

Watch a video about Aspect-Oriented Programming and complete these exercises:

- **6.2** - ריצת 2000 (*running_2000*)
- **6.3** - חתול ארוך הוא ארוך (*long_cat_is_long*)
- **6.4** - זכרו זכרו (*remember_remember*)
- **6.5** - *group_by* (*group_by*)

### Week 7

- **7.2** - צָב שָׁלוּחַ (*sent_turtle*)

## Bonus Exercises

Here are three bonus exercises about decorators:

1. **Decorator Factory**: Create a decorator factory that returns a decorator for functions with one argument. The factory should take one argument (a type) and return a decorator that checks if the parameter is of the correct type. If incorrect, it should raise a custom error. Use `functools.wraps`. Online solutions will not be accepted.
   - **Filename**: `type_check.py`
   - **Decorator name**: `type_check`
   
2. **Surprise Decorator**: Write a decorator that makes the function print "surprise!" instead of executing its original functionality.
   - **Filename**: `surprise.py`
   - **Decorator name**: `surprise`
   
3. **Twice Decorator**: Write a decorator that executes the function it wraps twice. Use `decorator.decorator`.
   - **Filename**: `twice.py`
   - **Decorator name**: `twice`

## How to Hand In

- Submit the assignments in the Git repository you created from the supplied link (available in Moodle).
- Open a **separate pull request** for each exercise and add **“excellenteam-scaleup”** as a reviewer.
- Paste the links in Moodle.
- Ensure that only the specific exercise appears in the **diff** section of the pull request.
  - Always return to the `main`/`master` branch before opening a new branch to avoid including previous exercises.

### Naming Conventions

- **File format**: `<week>.<part>.<exercise_name>.py`
- The **exercise name** is specified in brackets next to the Hebrew name.
  - Example: For "זו הדרך", the filename should be **`5.1.thats_the_way.py`**
- The **function inside the file** should match the exercise name:
  - `5.1.thats_the_way.py` should contain `def thats_the_way():`
  - `5.4.communicating_vessels.py` should contain two functions: `def interleaves():` and `def generator_interleaves():`
- Each exercise should be submitted as a **separate module**, unless the exercises are dependent on each other.
- Ensure `if __name__ == '__main__':` is included in every file.
- `.ipynb` file format will **not** be accepted. Only `.py` files are allowed.

## Grading

- Each exercise grants **9 points**.
- Each bonus exercise can provide **up to 3 bonus points**.
- Code **cleanliness** is also graded. Refer to **“clean code guidelines.docx”** for more details.

## Support

For any questions, contact the course staff on **Slack**.
