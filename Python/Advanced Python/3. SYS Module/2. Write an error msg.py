import sys
sys.stderr.write("ERROR MESSAGE\n")  # stderr mostly used to show error msgs.
sys.stderr.flush()
# stdout mostly used to show success msgs.
sys.stdout.write("STDOUT MESSAGE\n")
