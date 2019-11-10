import Algorithmia
import json
from Algorithmia.acl import ReadAcl, AclType

apiKey = "simglFzyXkye8lDWJ0rGViwralu1"
# Create the Algorithmia client
client = Algorithmia.client("simglFzyXkye8lDWJ0rGViwralu1")

# Set your Data URI
nlp_directory = client.dir("data://eijan/nlp_directory")
# Create your data collection if it does not exist
if nlp_directory.exists() is False:
    nlp_directory.create()

# Create the acl object and check if it's the .my_algos default setting
acl = nlp_directory.get_permissions()  # Acl object
acl.read_acl == AclType.my_algos  # True

# Update permissions to private
nlp_directory.update_permissions(ReadAcl.private)
nlp_directory.get_permissions().read_acl == AclType.private # True

text_file = "data://eijan/nlp_directory/data1.txt"

# Upload local file
if client.file(text_file).exists() is False:
    client.file(text_file).putFile("/Users/eijan/Documents/zothacks2019/data1.txt")

# Download contents of file as a string
if client.file(text_file).exists() is True:
    #input_string = client.file(text_file).getString()
    with open('data1.txt') as json_file:
        input = json.load(json_file)
    
# Create the algorithm object using the Summarizer algorithm
algo = client.algo('matching/DatingAlgorithm/0.1.3')
#algo_dict = json.loads(algo.pipe(input).result)
# Pass in input required by algorithm
try:
    # Get the summary result of your file's contents
    print(algo.pipe(input).result)
except Exception as error:
    # Algorithm error if, for example, the input is not correctly formatted
    print(error)