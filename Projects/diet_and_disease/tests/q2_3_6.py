test = {
  'name': 'Question 2.3.6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numbers
          >>> len(totchol_ci_by_diabp)
          10
          >>> all([x[0] < x[1] for x in totchol_ci_by_diabp])
          True
          >>> len(totchol_mean_by_diabp)
          10
          >>> all([isinstance(x, numbers.Real) for x in totchol_mean_by_diabp])
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
