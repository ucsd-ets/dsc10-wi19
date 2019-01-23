test = {
  'name': 'Question 1_9',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # your answer should be a string
          >>> isinstance(most_per_capita_state, str)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # your answer should be a number
          >>> import numbers
          >>> isinstance(most_per_capita_pct, numbers.Real)
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
