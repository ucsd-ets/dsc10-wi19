test = {
  'name': 'Question 1_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> callable(how_close)
          True
          >>> how_close('0-3', 'nan') == "not close"
          True
          >>> how_close('1-1', 'nan') == "tied"
          True
          >>> how_close('0-0', 'y') == "very close"
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
