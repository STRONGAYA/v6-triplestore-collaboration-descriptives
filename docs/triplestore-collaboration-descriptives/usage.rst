How to use
==========
Note that this algorithm was built to be used with a GraphDB triplestore.
The algorithm is likely to not work with other types of triplestores unless adapted.

Input arguments
---------------

The algorithm requires no input arguments.

Python client example
---------------------

To understand the information below, you should be familiar with the vantage6
framework. If you are not, please read the `documentation <https://docs.vantage6.ai>`_
first, especially the part about the
`Python client <https://docs.vantage6.ai/en/main/user/pyclient.html>`_.

The following code snippet is a basic example of how you can use this algorithm
with the demo network available through `v6 dev create-demo-network`.
Note that after creation of the demo-network, you should ensure that the CSV file has a
column named `endpoint` with a value that represents the URL to the GraphDB location.

.. code-block:: python

  from vantage6.client import Client

  server = 'http://localhost'
  port = 5000
  api_path = '/api'
  private_key = None
  username = 'org_1-admin'
  password = 'password'

  # Create connection with the vantage6 server
  client = Client(server, port, api_path)
  client.setup_encryption(private_key)
  client.authenticate(username, password)

  input_ = {
    'master': True,
    'method': 'central',
    'args': [],
    'kwargs': {
    },
    'output_format': 'json'
  }

  my_task = client.task.create(
      collaboration=1,
      organizations=[1],
      name='triplestore-collaboration-descriptives',
      description='Vantage6 algorithm that retrieves the descriptive information of triplestores in a collaboration',
      image='medicaldataworks.azurecr.io/projects/strongaya/triple-collab-descr',
      input=input_,
      data_format='json'
  )

  task_id = my_task.get('id')
  results = client.wait_for_results(task_id)