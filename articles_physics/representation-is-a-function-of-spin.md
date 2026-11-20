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

**Why this is an identity and not a theorem.** The claim becomes shorter once the group is named correctly. A field's spin is the label of the carrier under the **rotation group**, and the framework's gauge group *is* the rotation group, $\mathrm{SU}(2)=\mathrm{Spin}(3)$ — the same group, not a group isomorphic to it. So "the gauge representation is fixed by the spin" is not a constraint the algebra happens to satisfy; it is the sentence "the carrier is classified by the group that acts on it", read twice. A framework in which the two could be chosen independently would need a gauge group that is *not* the rotation group, and that is exactly the enlargement this algebra does not have. What is a theorem, and what the rest of the article computes, is the **table**: which carrier each spin gets, and which row of the model's needs it does or does not match.

**Each carrier is the one its spin allows.** The line is one-dimensional and real, the ideal is two-dimensional and complex, the adjoint is three-dimensional and real. The dimensions are $1$, $2$ and $3$, and they are the dimensions of the trivial, spinor and adjoint representations of $\mathrm{Spin}(3)$.

## The Rotor Conventions

**The group, and the one letter.** The compact factor is the group the standard theory calls $SU(2)$, and in the biquaternion algebra it **is** $\mathrm{SU}(2)=\{\tilde q\in\mathbb{H}:\langle\tilde q\rangle_{\natural}=1\}=S^3=\mathrm{Spin}(3)=\mathrm{Sp}(1)$ — the unit real quaternions, that is the rotors of the spatial rotations — of real dimension three. Its matrix display is $\mathsf M_2:\mathrm{SU}(2)\to SU(2)$, and the display is not the object: it marks an axis, and the mark is a choice of complex structure on $\mathbb{H}$. The corpus's statement of the distinction is [The Spin Group via 4×4 Real Matrices](../articles_maths/the-spin-group-via-4x4-real-matrices.html).

**The dagger, and why it is the tie that matters.** On $X=q+ip$ with $q$ and $p$ real quaternions the dagger is the composite of the two involutions,
$$
X^{*}=\overline{X^{\natural}}=q^{\natural}-i\,p^{\natural},
$$
conjugate-linear and **order-reversing**, $(XY)^{*}=Y^{*}X^{*}$. The unitary elements are those with $XX^{*}=e_t$, equivalently $X^{*}=X^{-1}$; they form the compact group $\mathrm{U}(\mathbb{B})$. The dagger is the only one of the algebra's involutions whose unitarity condition cuts out a compact group, and therefore the only one that can tie the two slots of a two-sided operator without leaving the unitary slice.

**The two sectors are its fixed and anti-fixed loci.** $\mathbb{B}_{\Psi}=\{X:X^{*}=X\}$ and $\mathbb{B}_{\Phi}=\{X:X^{*}=-X\}$, of real dimension four each; in the element $q+ip$ they are $q$ real with $p$ pure, and $q$ pure with $p$ real. The census is $4+4=8$. Source: [The Grading, Fermion Parity and the Two Sectors](the-grading-fermion-parity-and-the-two-sectors-in-biquaternionic-form.html).

**The operators, and the tie of each.** Four families act on the algebra, and the family is not a notation: the tie decides which subspace survives.

| Operator | Formula | Tie |
|---|---|---|
| left | $L_{\tilde Q}(X)=\tilde QX$ | none |
| right | $R_{\tilde Q}(X)=X\tilde Q$ | none |
| two-sided | $L_{\tilde Q_4}R_{\tilde Q_2}(X)=\tilde Q_4X\tilde Q_2$ | two unrelated parameters |
| **Hermitian pair** | $\mathrm{Sd}_{\tilde Q}(X)=\tilde Q\,X\,\tilde Q^{*}$ | the two slots tied by the dagger |

The physics conventions name the last one $\mathrm{Sd}_{\tilde Q}$, "the two-sided operator, the congruence by the element"; the mathematics call it the Hermitian pair. This article uses $\mathrm{Sd}$.

**Which operator can act on a sector.** One line each, and they are the only three facts a gauge-theory article needs.

- $L_{\tilde A}$ maps a sector into itself only when $\tilde A$ is a real scalar. The check is one line: for $X$ anti-fixed, $(AX)^{*}=X^{*}A^{*}=-XA^{*}$, so $AX$ is anti-fixed only if $A$ commutes with every element of the sector, which forces $A$ real. Verified at random: $0$ of $200$ parameters preserve, and a real scalar does.
- $\mathrm{Sd}_{\tilde Q}$ maps **each sector into itself for every** $\tilde Q$, because the dagger appears once in each slot: $(\tilde QX\tilde Q^{*})^{*}=\tilde QX^{*}\tilde Q^{*}=\mathrm{Sd}_{\tilde Q}(X^{*})$. Verified: $0$ of $200$ failures in either sector.
- $\mathrm{Sd}_{\tilde Q}$ is multiplicative, $\mathrm{Sd}_a\mathrm{Sd}_b=\mathrm{Sd}_{ab}$, and it is an **algebra** automorphism exactly when $\tilde Q\tilde Q^{*}=e_t$ — the exact defect is $\mathrm{Sd}_{\tilde Q}(XY)-\mathrm{Sd}_{\tilde Q}(X)\mathrm{Sd}_{\tilde Q}(Y)=\tilde QX(e_t-\tilde Q^{*}\tilde Q)Y\tilde Q^{*}$, which vanishes on the unitary slice and only there. On that slice $\tilde Q^{*}=\tilde Q^{-1}$ and $\mathrm{Sd}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{-1}}=\operatorname{Ad}_{\tilde Q}$, the change of frame. Off it the two are different operators, and only the first is a frame change.

**Two carriers, one angle.** For a unit rotor $\tilde u=\cos\tfrac{\varphi}{2}+\sin\tfrac{\varphi}{2}\vec u$ the same parameter acts differently on the two spin carriers, and the difference is a factor two:

- on the **vector part** $\mathfrak{k}$, $\mathrm{Sd}_{\tilde u}(\vec v)=\tilde u\vec v\tilde u^{*}$ is the rotation of $\vec v$ about $\vec u$ by the **full** angle $\varphi$;
- on the **left ideal** $S_+$, left multiplication is multiplication by a complex phase in the Peirce basis, $L_{\tilde u}|_{S_+}=\operatorname{diag}(e^{-i\varphi/2},e^{+i\varphi/2})$, the **half** angle, of determinant one.

Left multiplication does not rotate the vector part: $L_{\tilde u}$ does not map $\mathfrak{k}$ into itself unless $\tilde u$ is real. The two statements are both true of different maps, and an article that names one and writes the other has written a wrong factor.

**The ideal is a family, and no result depends on the member.** $S_\pm(\vec u_{\mathrm r})=\mathbb{B}\tilde\Pi_\pm(\vec u_{\mathrm r})$ with $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec u_{\mathrm r})$ depends on the axis $\vec u_{\mathrm r}$, and the algebra contains one such ideal for every point of $S^2$. All minimal left ideals of $\mathbb{B}\cong M_2(\mathbb{C})$ are isomorphic as left modules, so a result proved for one holds for all, and every display that writes a Peirce basis declares the axis it used.

**The generators.** $T_a=\tfrac12\vec e_a$ with $[\vec e_a,\vec e_b]=2\varepsilon_{abc}\vec e_c$, so $[T_a,T_b]=\varepsilon_{abc}T_c$ and $f_{abc}=2\varepsilon_{abc}$ in the $\vec e_a$ basis. The normalisation is not cosmetic: the factor two is the half-angle of the paragraph above, and it is the constant that appears in the three-boson vertex.

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
