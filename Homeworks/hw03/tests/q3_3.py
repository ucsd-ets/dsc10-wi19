test = {
  'name': 'Question 3_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(complaints_per_person, Table)
          True
          >>> 'Complaints Per Person' not in complaints_per_person.labels # "Per" should not be capitalized!
          True
          >>> set(complaints_per_person.labels) == {'State', 'Complaints per Person'}
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
