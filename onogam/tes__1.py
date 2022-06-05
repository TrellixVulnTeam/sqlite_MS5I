import tempfile

with tempfile.NamedTemporaryFile(delete=False) as tf:
    print(tf.name)
