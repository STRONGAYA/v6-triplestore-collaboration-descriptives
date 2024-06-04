Implementation
==============

Overview
--------

Central (``central``)
-----------------
The central part is responsible for the orchestration and aggregation of the algorithm.

``central``
~~~~~~~~~~~~~~~~
The `central` function creates a task for all organisations in the collaboration to fetch their sample size and
FAIRification information.
It waits for the results and returns them in a dictionary format.

Partials
--------
Partials are the computations that are executed on each node. The partials have access
to the data that is stored on the node. The partials are executed in parallel on each
node.

``partial``
~~~~~~~~~~~~~~~~

The `partial` function retrieves the organisation name, reads a SPARQL query from a file, posts the query to an endpoint,
and processes the results. The results are then returned in a dictionary format.

``post_sparql_query``
~~~~~~~~~~~~~~~~
The `post_sparql_query` function posts the query to an endpoint, and processes the results.
The results are then returned in a `response.text` format.

``retrieve_classes``
~~~~~~~~~~~~~~~~
The retrieve_classes query is the SPARQL query that is used to retrieve the classes from the endpoint.
The query is saved in an `.rq` file which is read by the `partial` function.
Note that the query assumes that relevant data elements have been annotated with SIO's `has-attribute` relation (
`http://semanticscience.org/resource/SIO_000008`)