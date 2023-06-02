from imports_and_setup import *
from molecular_operations import *

def conformer_generator(input, output, numconf, add_ref):
    mol = Chem.MolFromSmiles(input)
    mol = Chem.AddHs(mol)

    # Generate conformers
    cids = AllChem.EmbedMultipleConfs(mol, numConfs=numconf, randomSeed=1)

    # If a reference molecule should be added, load it and add it to the output
    if add_ref:
        ref_mol = Chem.MolFromSmiles(add_ref)
        ref_mol = Chem.AddHs(ref_mol)
        AllChem.EmbedMolecule(ref_mol, randomSeed=1)
        cids.append(ref_mol.GetConformer().GetId())

    writer = Chem.SDWriter(output)
    for cid in cids:
        writer.write(mol, confId=cid)
    writer.close()

def draw(ms, p=None, confIds=None):
    # Draw the molecules with provided properties and conformers
    img = Draw.MolsToGridImage(ms, molsPerRow=4, subImgSize=(200,200), legends=[x.GetProp("_Name") for x in ms])

    if p is not None:
        for m in ms:
            m.SetProp(p, str(m.GetProp(p)))

    if confIds is not None:
        for m in ms:
            m.RemoveAllConformers()
            for cid in confIds:
                m.AddConformer(m.GetConformer(cid), assignId=True)

    return img
