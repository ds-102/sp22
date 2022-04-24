test = {   'name': 'q2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> test_input = simulate_private_data(nedredv_df, N=1000, random_seed = 1)\n'
                                               '>>> test_output = alg_2_estimate(test_input, random_seed = 6)\n'
                                               '>>> true_output= np.array([ 0.61118555,  0.30388517,  0.16553917,  0.08185385,  0.01907432,\n'
                                               '...                         0.04238588,  0.07632029, -0.00456863, -0.02156009,  0.04617881,\n'
                                               '...                         0.08586842,  0.08546348,  0.00198393,  0.01626853,  0.02354852,\n'
                                               '...                         0.38347409,  0.08912664,  0.1377036 ,  0.07541032,  0.06230894,\n'
                                               '...                        -0.11471126,  0.08304802,  0.08106895,  0.04457083,  0.07825384,\n'
                                               '...                         0.0356127 , -0.04093591])\n'
                                               '>>> np.max(abs(test_output - true_output)) < 0.0001\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
