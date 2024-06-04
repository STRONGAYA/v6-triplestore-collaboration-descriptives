Validation
==========

Validation of this algorithm was considered to be irrelevant for its task.
An example of the algorithm's output is provided below.

In this example the database is called `dataset` and it has data on the `biological sex` of `1000` samples.
`Mare imbrium` is the organisation name and `the near side of the moon` is the country where the organisation is located.

.. code-block:: json

  {
    "organisation": "Mare Imbrium",
    "country": "Near side of the Moon",
    "sample_size": 1000,
    "variable_info": [
      {
        "main_class": "http://data.local/rdf/ontology/dataset.biological_sex",
        "main_class_count": 1000,
        "sub_class": "http://data.local/rdf/ontology/dataset.biological_sex",
        "sub_class_count": 1000
      },
      {
        "main_class": "http://data.local/rdf/ontology/dataset.biological_sex",
        "main_class_count": 1000,
        "sub_class": "http://data.local/rdf/ontology/dataset.female",
        "sub_class_count": 500
      },
      {
        "main_class": "http://data.local/rdf/ontology/dataset.biological_sex",
        "main_class_count": 1000,
        "sub_class": "http://data.local/rdf/ontology/dataset.male",
        "sub_class_count": 499
      }
      {
        "main_class": "http://data.local/rdf/ontology/dataset.biological_sex",
        "main_class_count": 1000,
        "sub_class": "http://data.local/rdf/ontology/dataset.intersex",
        "sub_class_count": 1
      }
    }