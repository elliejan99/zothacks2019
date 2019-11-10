import Algorithmia

client = Algorithmia.client('simglFzyXkye8lDWJ0rGViwralu1')
algo = client.algo('matching/DatingAlgorithm/0.1.3')
algo.set_options(timeout=300) # optional
print(algo.pipe(input).result)