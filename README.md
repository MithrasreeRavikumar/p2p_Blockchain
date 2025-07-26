=>Understand the project structure and functionality:
1.Core features: transactions, mining (PoW), peer registration, consensus.

2.Dashboard UI: interact with the blockchain via a web interface.

3.Endpoints: like /mine, /transactions/new, /nodes/register, /nodes/resolve.

=>Run the project:
Install dependencies:
    pip install -r requirements.txt
Start multiple nodes (on different ports):
    python run_node.py 5000
    python run_node.py 5001
Access from your browser:
    http://localhost:5000/

    http://localhost:5001/