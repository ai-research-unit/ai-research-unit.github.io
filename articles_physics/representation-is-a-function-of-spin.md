# __Representation Is a Function of Spin__

## Introduction

**The claim.** In this framework the gauge group *is* the spin group, and therefore the representation a field carries is fixed by its spin. The two cannot be chosen independently, and no amount of further construction will separate them.

**Why it matters.** The Standard Model needs the two to be independent. It assigns a spin-zero field to a doublet, a spin-half field to a doublet on one chirality only, and a spin-one field to the adjoint. In a framework where representation is a function of spin, each of those assignments is either forced or forbidden, and nothing in between.

**What this article is.** The statement, the table, and the three-way comparison. It is the single sentence that the obstructions of three separate articles reduce to: the scalar that cannot be a doublet, the fermion that cannot be chiral, and the vector that matches.

**What this article is not.** It is not an argument that the framework is wrong. It is a statement of what a framework with this group can and cannot carry, and the record of the one row of the table where the model's need and the algebra's supply coincide.

## The Group and the Carriers

**The group.** The compact gauge algebra available in the biquaternions is $\mathfrak{su}(2)\oplus\mathfrak{u}(1)$, of real dimension four, as [Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)](why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html) establishes. The non-abelian factor is the algebra of the rotation group, $\mathrm{Spin}(3)$, and the abelian factor is the central phase $\mathrm{U}(1)$.

**The carriers.** The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ acts on itself, and the fields of the three spins are carried by three different subspaces:

- **Spin zero.** The scalar is the central field $\xi\,e_t$, an element of the line $\mathbb{R}e_t$.
- **Spin half.** The fermion is an element of a minimal left ideal $S_+$, which as a complex vector space is $\mathbb{C}^2$.
- **Spin one.** The gauge field is valued in the adjoint, the vector part of the algebra, of real dimension three.

**Each carrier is the one its spin allows.** The line is one-dimensional and real, the ideal is two-dimensional and complex, the adjoint is three-dimensional and real. The dimensions are $1$, $2$ and $3$, and they are the dimensions of the trivial, spinor and adjoint representations of $\mathrm{Spin}(3)$.

## The Table

| Spin | Carrier in the algebra | Representation of $\mathrm{Spin}(3)$ | What the model needs |
|---|---|---|---|
| $0$ | the line $\mathbb{R}e_t$ | trivial | a doublet |
| $\tfrac12$ | the minimal left ideal $S_+\cong\mathbb{C}^2$ | spinor, both letters alike | a doublet on one chirality only |
| $1$ | the vector part $\mathfrak{k}$ | adjoint | adjoint |

**The third column is not an extra assumption.** It is read from the carrier, and the carrier is read from the spin. A reader who wants a different representation for a given spin is asking for a different algebra.

**One row out of three matches.** The vector row is the adjoint, and the adjoint is what a Yang–Mills field needs: that is why the free kinematics and the self-couplings of [The W and Z Bosons in Biquaternionic Form](the-w-and-z-bosons-in-biquaternionic-form.html) come out right, and why [Non-Abelian Gauge Fields in Biquaternionic Form](non-abelian-gauge-fields-in-biquaternionic-form.html) can write the whole construction without an extra hypothesis.

## The Scalar Row: Why There Is No Doublet

**The carrier is the line $\mathbb{R}e_t$, and the line is the centre.** Every element proportional to the identity is fixed by every inner automorphism, so the scalar carries the trivial representation: $\tilde Q\,(\xi e_t)\,\tilde Q^{-1}=\xi e_t$ for every unit $\tilde Q$.

**A trivial representation cannot break the group.** A scalar that is invariant under the whole non-abelian factor cannot select a direction in it, so its vacuum expectation value breaks nothing there. This is the statement of [The Higgs Mechanism in Biquaternionic Form](the-higgs-mechanism-in-biquaternionic-form.html), and it is not a gap in that article: it is the consequence of the carrier being the line.

**What survives.** The abelian mechanism is untouched, because a central field can carry a $\mathrm{U}(1)$ charge. The framework therefore has a working abelian Higgs mechanism and no non-abelian one, which is the shape of the sector's obstruction.

## The Fermion Row: Why There Is No Chiral Action

**The carrier is the ideal $S_+$, and it is one module, not two.** The two chiral halves are the values of one operator — the letter law of [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html), where $L$ and $R$ are the two values of the right multiplication by $\vec e_z$, not two separate spaces.

**The gauge action is left multiplication, and left multiplication does not read the letter.** A left multiplication $(aQ)\vec e_z=a(Q\vec e_z)$ keeps the letter of its argument and applies the same element to both values. So a non-abelian gauge transformation acts on $L$ and $R$ with the same matrix, which is the definition of a vector-like coupling.

**A chiral gauge theory needs two different actions on the two values.** It needs the group to act on $L$ and to act differently, or not at all, on $R$. Left multiplication cannot do this: it is one operator, acting on one side, on a module that contains both letters. That is the whole obstruction, and it is a statement about the carrier and not about the completeness of the work.

**The abelian case is the exception, and it is the one the corpus has.** A right multiplication *can* return two different factors on the two values, which is why the framework carries a chiral $\mathrm{U}(1)$ — the charge element $b$ of [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html) with $ϙ_L\neqϙ_R$ — and cannot carry a chiral $SU(2)$.

## The Vector Row: Why It Matches

**The carrier is the vector part, and it is the adjoint.** The action of the group on its own algebra is conjugation, and the vector part is stable under it. The gauge field therefore transforms in the adjoint, as a connection must, and the covariant derivative $D_\mu\tilde\Xi=\partial/\partial R_\mu\tilde\Xi+i\kappa\,\mathcal{A}_\mu\tilde\Xi$ writes the coupling without a choice.

**This is the corpus's unusual strength and its ceiling at once.** The one row where the algebra is exactly what the model needs is the row the model uses for its carriers, and that is why the sector's kinematics, its self-couplings and its gauge algebra are all correct while its matter and its scalar are not.

## What Would Break the Theorem

**A group that commutes with the Lorentz action.** The statement "representation is a function of spin" says that the only available group is the one that acts on the spinor index. An internal symmetry would be a group acting on a label the Lorentz group does not see, and the algebra has no such label: the same six Lorentz basis operators that generate the rotations are the ones that generate the compact factor.

**A second carrier for the same spin.** If the algebra offered two inequivalent modules for spin half, one could assign the doublet to one and the singlet to the other. It does not: the minimal left ideal is unique up to isomorphism, and the commutant is a division algebra, so the module is simple.

**Neither is present, and neither is a matter of effort.** The theorem is a statement about the algebra, and the corpus records it as such.

## What the Framework Supplies

- **Supplied.** The group, the three carriers, and the table above. The identification of the non-abelian factor with the rotation group, and the one-sidedness of the action that carries the fermion.
- **Imported.** Nothing. The table is a computation about the algebra.
- **Not supplied.** Any way to decouple spin from representation, which is what the model's scalar and matter sectors require.

**Where this is applied.** The scalar row is applied in [The Higgs Mechanism in Biquaternionic Form](the-higgs-mechanism-in-biquaternionic-form.html) and in [Electroweak Symmetry Breaking: the Doublet, the Potential and the Gauge-Boson Masses](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-gauge-boson-masses.html); the fermion row in [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html); the vector row in [The W and Z Bosons in Biquaternionic Form](the-w-and-z-bosons-in-biquaternionic-form.html). The carrier of the fermion is collected in [The Gauge Carrier of the Material Sector: Why the Action Is One-Sided](the-gauge-carrier-of-the-material-sector-why-the-action-is-one-sided.html).

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Spin}(3)$ | the compact non-abelian factor, the rotation group |
| $\mathbb{R}e_t$ | the line of the central scalar |
| $S_+$ | the minimal left ideal carrying the fermion, $\cong\mathbb{C}^2$ |
| $\mathfrak{k}$ | the vector part of the algebra, the adjoint carrier |
| $\xi$ | the chirality operator, $-iR_{\mathrm{axf},\vec e_z}$ |
| $L,R$ | the two values of the letter, the two chiral halves |

## Further Reading

- [Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)](why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html), for the dimension four of the compact algebra.
- [The One-Sided Action and the Spin Representation](../articles_maths/the-one-sided-action-and-the-spin-representation.html), for the left action as the spin representation.
- [Non-Abelian Gauge Fields in Biquaternionic Form](non-abelian-gauge-fields-in-biquaternionic-form.html), for the covariant derivative acting by left multiplication.
