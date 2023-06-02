from imports_and_setup import *

def load_molecules(pdb_file_path, sdf_file_path):
    molecule = Chem.MolFromPDBFile(pdb_file_path)
    molecule_smile = Chem.MolToSmiles(molecule)
    
    pattern = next(Chem.SDMolSupplier(sdf_file_path))
    pattern_smile = Chem.MolToSmiles(pattern)

    return molecule, molecule_smile, pattern, pattern_smile

def find_substruct_matches(pattern):
    matches = pattern.GetSubstructMatches(pattern)
    return matches
