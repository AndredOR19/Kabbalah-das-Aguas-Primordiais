import pandas as pd
import json
import os
import glob
import re
from tqdm import tqdm
import numpy as np
import ast
from merge_utility import merge_database_by_id_group


if __name__ == "__main__":
    # Base dirs
    symmap_dir = '../data/symmap'
    merge_result_dir = '../merge_result'
    symmap_data_dir = symmap_dir  # keep name used later

    # Load syndromes from SymMap
    syndrome = pd.read_excel(os.path.join(symmap_dir, 'symmap_syndrome.xlsx'))
    syndrome['Syndrome_id'] = syndrome.Syndrome_id.apply(lambda x: 'SMSY{:05d}'.format(x))
    syndrome.rename(columns={'Syndrome_id': 'SymMap_id'}, inplace=True)
    # Drop known duplicated/noisy row (kept from original script)
    syndrome.drop(54, inplace=True)
    # Cleanup unused cols
    syndrome.drop(["Version", "Type", "Suppress"], inplace=True, axis=1)

    # Merge two syndromes with the same syndrome description
    syndrome = merge_database_by_id_group(syndrome, 'Syndrome_definition')

    # Assign TMDB ids and save
    syndrome['TMDB_id'] = [
        'TMSY{:05d}'.format(index) for index in range(1, syndrome.shape[0] + 1)
    ]

    # Map SymMap_id -> TMDB_id for later joins
    symmap_syndrome_map = dict(zip(syndrome['SymMap_id'], syndrome['TMDB_id']))

    # Ensure target folders exist and write entities
    os.makedirs(os.path.join(merge_result_dir, 'entity'), exist_ok=True)
    syndrome.to_csv(os.path.join(merge_result_dir, 'entity/syndrome.csv'), index=False)

    # herb2syndrome
    herb_df = pd.read_csv(os.path.join(merge_result_dir, "entity/medicinal_material.csv"))

    # Build map from SymMap herb id -> TMDB herb id
    symmap_herb_map = {}
    for _, row in herb_df.iterrows():
        symmap_val = row.get("SymMap_id")
        if isinstance(symmap_val, str):
            for SymMap_id in symmap_val.split(";"):
                try:
                    key = "SMHB{:05d}".format(int(SymMap_id))
                except ValueError:
                    key = SymMap_id.strip()
                symmap_herb_map[key] = row["TMDB_id"]

    herb2syndrome = []
    symmap_syndrome_data = os.path.join(symmap_data_dir, "syndrome")
    for syndrome_herb_path in glob.glob(os.path.join(symmap_syndrome_data, "*/herb.json")):
        symmap_syndrome_id = os.path.basename(os.path.dirname(syndrome_herb_path))
        # Normalize numeric folder names to SMSYxxxxx
        if symmap_syndrome_id.isdigit():
            symmap_syndrome_id = "SMSY{:05d}".format(int(symmap_syndrome_id))

        TMDB_syndrome_id = symmap_syndrome_map.get(symmap_syndrome_id)
        if not TMDB_syndrome_id:
            # Unknown syndrome id in mapping; skip
            continue

        with open(syndrome_herb_path, 'r', encoding='utf-8') as f:
            herb_json = json.load(f)

        for herb_item in herb_json.get("data", []):
            herb_id = herb_item.get("Herb_id")
            # Normalize herb id to SMHBxxxxx
            if isinstance(herb_id, str) and herb_id.isdigit():
                herb_id = "SMHB{:05d}".format(int(herb_id))
            elif isinstance(herb_id, (int, float)):
                try:
                    herb_id = "SMHB{:05d}".format(int(herb_id))
                except Exception:
                    herb_id = str(herb_id)

            TMDB_herb_id = symmap_herb_map.get(herb_id)
            if TMDB_herb_id:
                herb2syndrome.append((TMDB_herb_id, TMDB_syndrome_id))

    herb2syndrome_df = pd.DataFrame(sorted(set(herb2syndrome)), columns=["source_id", "target_id"])
    herb2syndrome_df["Relation_type"] = [
        "herb_treat_syndrome"
    ] * herb2syndrome_df.shape[0]

    os.makedirs(os.path.join(merge_result_dir, "relation"), exist_ok=True)
    herb2syndrome_df.to_csv(
        os.path.join(merge_result_dir, "relation/herb2syndrome.csv"), index=False
    )
