OK_FORMAT = True

test = {   'name': 'q7.2',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> np.testing.assert_allclose(f1_train_svm_best_config_fbow >= 0., 1)\n'
                                               '>>> np.testing.assert_allclose(f1_train_svm_best_config_fbow <= 1., 1)\n'
                                               '>>> np.testing.assert_allclose(f1_val_svm_best_config_fbow >= 0., 1)\n'
                                               '>>> np.testing.assert_allclose(f1_val_svm_best_config_fbow <= 1., 1)\n'
                                               '>>> np.testing.assert_allclose(f1_test_svm_best_config_fbow >= 0., 1)\n'
                                               '>>> np.testing.assert_allclose(f1_test_svm_best_config_fbow <= 1., 1)\n'
                                               '>>> np.testing.assert_allclose(best_C > 0, 1)\n'
                                               '>>> np.testing.assert_allclose(best_max_iter > 0, 1)\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
