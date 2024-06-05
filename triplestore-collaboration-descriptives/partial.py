"""
This module contains the decentralised part of the algorithm for the collaboration descriptives.

The `partial` function retrieves the organisation name, reads a SPARQL query from a file, posts the query to an endpoint,
and processes the results. The results are then returned in a dictionary format.

Functions:
    partial(client: AlgorithmClient, df1: pd.DataFrame) -> Any: Executes the decentralised part of the algorithm.
"""
import os
import sys

import numpy as np
import pandas as pd

from .post_query import post_sparql_query
from typing import Any
from vantage6.algorithm.tools.util import info, error
from vantage6.algorithm.tools.decorators import algorithm_client, data
from vantage6.algorithm.client import AlgorithmClient


@data(1)
@algorithm_client
def partial(client: AlgorithmClient, df1: pd.DataFrame) -> Any:
    """
    Executes the decentralised part of the algorithm for the collaboration descriptives.

    This function retrieves the organisation name ad country,
    reads a SPARQL query from a file,  posts the query to an endpoint, and processes the results.
    The results are then returned in a dictionary format.

    Args:
        client (AlgorithmClient): The client instance for the algorithm.
        df1 (pd.DataFrame): The input data frame.

    Returns:
        dict: A dictionary containing the organisation name, country, sample size, and variable info.
    """
    # Get the name of the organisation
    organisation_name = client.organization.get(client.organization_id).get("name")
    organisation_country = client.organization.get(client.organization_id).get("country")

    try:
        # The 'r' argument means the file will be opened in read mode
        query = open(f'{os.path.sep}app{os.path.sep}triplestore-collaboration-descriptives{os.path.sep}'
                     f'retrieve_classes.rq', 'r').read()
    except Exception as e:
        # If there's an error reading the file, log an error
        error(f"Unexpected error occurred whilst reading the SPARQL query file, error: {e}")
        sys.exit(1)

    try:
        # Post the SPARQL query to the endpoint specified in df1
        info(f"Posting SPARQL query to {df1['endpoint'].iloc[0]}.")
        result = post_sparql_query(endpoint=df1['endpoint'].iloc[0], query=query)
    except Exception as e:
        error(f"Unexpected error occurred whilst posting SPARQL query, error: {e}")
        sys.exit(1)

    # If the result is empty (i.e. the query returned no results) it is likely the data is not available
    if not result:
        return {"organisation": organisation_name, "country": organisation_country,
                "sample_size": np.nan, "variable_info": []}

    try:
        # Convert main_class_count to int for all items in the list
        for item in result:
            item['main_class_count'] = int(item['main_class_count'])
            item['sub_class_count'] = int(item['sub_class_count'])

        # Find the item with the maximum main_class_count
        max_main_class_count_item = max(result, key=lambda x: x['main_class_count'])

        # Get the maximum main_class_count
        sample_size = max_main_class_count_item['main_class_count']
    except Exception as e:
        error(f"Unexpected error processing results, error: {e}")
        sys.exit(1)

    # Return a dictionary with the organisation name, country, sample size, and variable info
    return {"organisation": organisation_name, "country": organisation_country,
            "sample_size": sample_size, "variable_info": result}
