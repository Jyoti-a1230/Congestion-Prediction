# Data

Raw data is not stored in git (about 12 GB compressed). To get it:
1. Copy the `routability_features` folder from the CircuitNet download page to your own Google Drive.
2. In Colab, copy the archives you need to local disk and run the repo's `decompress_routability.py`
   from a folder whose parent contains `routability_features` (see the script's relative paths).
3. Extracted data goes under `data/raw/`; processed arrays go under `data/processed/`.

Dataset terms: check the CircuitNet page. Cite the CircuitNet paper in any write-up.
