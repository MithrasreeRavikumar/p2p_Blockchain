import os
import sys

if len(sys.argv) != 2:
    print("Usage: python run_node.py <port>")
else:
    port = sys.argv[1]
    os.system(f"python node.py -p {port}")
