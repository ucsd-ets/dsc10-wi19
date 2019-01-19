test = {
  'name': 'Question 1_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # your answer should be a table made of the previos arrays
          >>> from datascience import *
          >>> type(basic_stats) == Table
          True
          """,
          'hidden': False,
          'locked': False
        },        
        {
          'code': r"""
          >>> # Be sure the name of your columns are exactly as expected.
          >>> basic_stats.labels == ("School Type", "Number of Students", "Percentage of Colleges", "Minimum Size")
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
