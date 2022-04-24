test = {   'name': 'q1a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> test_input = simulate_private_data(nedredv_df, N=100, random_seed = 0)\n'
                                               '>>> test_output = alg_1_estimate(test_input)\n'
                                               '>>> true_output= np.array([0.54, 0.26, 0.1 , 0.17, 0.09, 0.04, 0.09, 0.  , 0.  , 0.04, 0.09,\n'
                                               '...                        0.05, 0.  , 0.  , 0.  , 0.14, 0.04, 0.11, 0.  , 0.  , 0.  , 0.05,\n'
                                               '...                        0.04, 0.  , 0.05, 0.04, 0.04])\n'
                                               '>>> np.max(abs(test_output - true_output)) < 0.00001\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
