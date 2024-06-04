Privacy
=======

Guards
------

The algorithm does not use actual data of the triplestore, rather it takes the counts of every data element with a http://semanticscience.org/resource/SIO_000008 relation.
For this no privacy guards were put in place.
Note however that this algorithm can expose what columns have a low number of occurrences.

Data sharing
------------

The counts of the variables are shared with the aggregating organisation.


Vulnerabilities to known attacks
--------------------------------


.. list-table::
    :widths: 25 10 65
    :header-rows: 1

    * - Attack
      - Risk eliminated?
      - Risk analysis
    * - **Identification of privacy-sensitive columns and values**
      - t.b.d.
      - The algorithm will expose what column/value combinations have a low number of counts, but it is not yet decided whether this is a feature or a 'bug'.
    * - Reconstruction
      - not relevant
      - The algorithm does not use actual data of the triplestore, rather it takes the counts of every element.
    * - Differencing
      - not relevant
      - The algorithm does not use actual data of the triplestore, rather it takes the counts of every element.
    * - Deep Leakage from Gradients (DLG)
      - not relevant
      - The algorithm does not use actual data of the triplestore, rather it takes the counts of every element.
    * - Generative Adversarial Networks (GAN)
      - not relevant
      - The algorithm does not use actual data of the triplestore, rather it takes the counts of every element.
    * - Model Inversion
      - not relevant
      - The algorithm does not use actual data of the triplestore, rather it takes the counts of every element.
    * - Watermark Attack
      - not relevant
      - The algorithm does not use actual data of the triplestore, rather it takes the counts of every element.