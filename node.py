from flask import Flask, jsonify, request, render_template, redirect, url_for
from uuid import uuid4
import requests
from blockchain import Blockchain

app = Flask(__name__)
node_id = str(uuid4()).replace('-', '')
blockchain = Blockchain()

@app.route('/')
def index():
    return render_template('index.html',
                           node_id=node_id,
                           chain=blockchain.chain,
                           peers=list(blockchain.nodes),
                           transactions=blockchain.current_transactions)

@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    proof = blockchain.proof_of_work(last_block['proof'])
    blockchain.add_transaction(sender="0", recipient=node_id, amount=1)
    block = blockchain.create_block(proof, blockchain.hash(last_block))
    return redirect(url_for('index'))

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    sender = request.form['sender']
    recipient = request.form['recipient']
    amount = int(request.form['amount'])
    blockchain.add_transaction(sender, recipient, amount)
    return redirect(url_for('index'))

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    node = request.form['node']
    blockchain.register_node(node)
    return redirect(url_for('index'))

@app.route('/nodes/resolve', methods=['GET'])
def resolve():
    def get_chain(node):
        try:
            return requests.get(f'http://{node}/chain')
        except:
            class FailResponse:
                status_code = 404
            return FailResponse()
    blockchain.resolve_conflicts(get_chain)
    return redirect(url_for('index'))

@app.route('/chain', methods=['GET'])
def full_chain():
    return jsonify({'chain': blockchain.chain, 'length': len(blockchain.chain)})

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int)
    args = parser.parse_args()
    port = args.port
    app.run(host='0.0.0.0', port=port)
