test = {
  'name': 'Question 1_8',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from datascience import *
          >>> type(state_stats) == Table
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # make sure your table has columns 'STATE', 'POP', and 'PER_CAPITA'
          >>> len(set(state_stats.labels).intersection(set(['STATE', 'POP', 'PER_CAPITA']))) == 3
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
