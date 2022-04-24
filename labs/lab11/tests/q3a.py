test = {   'name': 'q3a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> test_input = simulate_private_data(nedredv_df, N=10000, random_seed = 8)\n'
                                               '>>> test_output = alg_3_estimate(test_input, random_seed = 2)\n'
                                               '>>> true_output= np.array([-0.40967514,  0.07351822, -0.4317238 ,  1.00062335, -0.5200155 ,\n'
                                               '...                        -0.89679615, -0.65737125, -0.29722826,  0.84077436,  0.40867117,\n'
                                               '...                        -1.00796038, -0.43696672,  0.01821487, -1.80613563, -0.90836173,\n'
                                               '...                        -0.17835337,  0.72904829, -0.72107227,  0.15482221, -0.55084658,\n'
                                               '...                        -0.31396992, -0.3488769 ,  0.77788347,  0.45583122,  0.05131975,\n'
                                               '...                         0.77705583,  0.56286043])\n'
                                               '>>> np.max(abs(test_output - true_output)) < 0.0001\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
