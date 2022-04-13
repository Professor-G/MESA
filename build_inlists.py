#!/usr/bin/env python3
import numpy as np
from pathlib import Path

here = Path(__file__).parent

dft_inlist_project = here / "inlist_project_unfilled"
dft_inlist = here / "inlist"

masses = np.geomspace(0.3, 20, 20)
masses = np.append(masses, 1.0)
print(masses)

with dft_inlist_project.open('r') as dft:
    dft_proj_txt = dft.read()
    
with dft_inlist.open('r') as dft:
    dft_inl_txt = dft.read()

names = here / "mass_list.txt"
if names.exists():
    names.unlink()
with names.open('a') as fil:
    fil.write(f"{len(masses):.0f}\n")
    
for mass in masses:
    proj_txt = dft_proj_txt.replace("FILL_HERE",
                                    f"{mass:0>5.2f}".replace('e', 'd'))
    out_path = here / f"inlist_project_{mass:0>5.2f}"
    with out_path.open('w') as out:
        out.write(proj_txt)
    out_inlist_path = here / f"inlist_{mass:0>5.2f}"
    inl_txt = dft_inl_txt.replace("inlist_project",
                                  f"inlist_project_{mass:0>5.2f}")
    with out_inlist_path.open('w') as out:
        
        out.write(inl_txt)
    
    
    with names.open('a') as fil:
        fil.write(f"{mass:0>5.2f}\n")
        
