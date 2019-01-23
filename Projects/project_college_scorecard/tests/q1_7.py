test = {
  'name': 'Question 1_7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # state_with_third_most_colleges should be a str with two letters.
          >>> isinstance(state_with_fourth_most_students, str) and len(state_with_fourth_most_students) == 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # your answer should be a number
          >>> import numbers
          >>> isinstance(number_of_students_in_state, numbers.Real)
          True
          """,
          'hidden': False,
          'locked': False
        }

      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
