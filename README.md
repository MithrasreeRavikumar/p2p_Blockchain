
# P2P Blockchain Network Simulation

## Objective
Simulate a peer-to-peer (P2P) blockchain network where each node maintains its own blockchain copy and synchronizes with peers using Flask and HTTP.

## Features
- Custom blockchain structure with transaction, block, and chain classes
- Proof-of-Work (PoW) mining
- Peer-to-peer node discovery and communication
- Consensus algorithm (longest chain wins)
- Blockchain sync between nodes
- Frontend using Flask + HTML templates

## Getting Started

### Prerequisites
- Python 3.x
- `pip install flask requests`

### How to Run:
1. Start a node on a port:
   ```bash
   python run_node.py 5000
   python run_node.py 5001
   python run_node.py 5002
