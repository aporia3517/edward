import tensorflow as tf

def log_gamma(x):
    # use an approximation avoiding special functions, because
    # TensorFlow doesn't currently support them
    # http://www.machinedlearnings.com/2011/06/faster-lda.html
    logterm = tf.log(x * (1.0 + x) * (2.0 + x))
    xp3 = 3.0 + x
    return -2.081061466 - x + 0.0833333 / xp3 - logterm + (2.5 + x) * tf.log (xp3)

def log_beta(x, y):
    # use an approximation avoiding special functions, because
    # TensorFlow doesn't currently support them
    return log_gamma(x) + log_gamma(y) - log_gamma(x+y)