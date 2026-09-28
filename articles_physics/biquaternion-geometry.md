# __Biquaternion Geometry__

## Introduction

This is the slot overview of the geometry the biquaternion algebra carries. It states what decides that geometry, recalls the Cayley–Klein picture in which a geometry is its group of motions, and maps the six articles that read the geometry of $\mathbb{B}$ and the general articles of Part IV that stand behind them.

Physically the signature is the organising datum: the choice of sector selects the geometry, the material sector $\mathbb{M}_-$ giving the Minkowski geometry and the informational sector $\mathbb{M}_+$ the Euclidean one, so the physics of the framework is read as the geometry of the selected real form. The Cayley–Klein picture is the Erlangen reading — a geometry is its group of motions, and the physics is that group acting on that figure. Each article of the category states one figure and its group.

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$.

---

## The Sign of the Biquaternion Norm as the Organising Data

What geometry the algebra carries is decided by its form. The biquaternion norm $N(\tilde{Q})=\sum_\mu Q_\mu^2$ is complex-valued, so it has no signature by itself; the signature appears on a real form. The realification has the split signature $(4,4)$, and the six distinguished real subspaces carry the signatures $(1,1)$, $(3,3)$, $(4,0)$, $(0,4)$, $(1,3)$ and $(3,1)$ (*Biquaternion Norm and Invertibility*). The sign of the restricted form is therefore the organising datum:

- a **definite** form, on $\mathbb{H}_{\mathbb{B}}$ of signature $(4,0)$ or on $i\mathbb{H}_{\mathbb{B}}$ of signature $(0,4)$, gives a Euclidean geometry, whose motions are the rotations;
- an **indefinite** form, on $\mathbb{M}_+$ of signature $(1,3)$ or on $\mathbb{M}_-$ of signature $(3,1)$, gives the Lorentzian geometry, whose motions are the Lorentz transformations;
- a **neutral** form, on the realification of signature $(4,4)$, gives a split geometry, whose real quadric is ruled by real lines;
- the degenerate case, the **null** form, is the null cone and the projective quadric, the figure rather than the space.

The same algebra therefore carries several geometries at once, and the passage from one to another is a change of real form, not a change of algebra.

## The Cayley–Klein Picture

In the Cayley–Klein picture a geometry is its group of motions, and the geometry of $\mathbb{B}$ is read from the group the form defines. The unit-norm group is $\mathbb{B}^\times_1\cong Spin(1,3)$ when the form is Lorentzian, its quotient $\mathbb{B}^\times_1/\{\pm e_0\}\cong SO^+(1,3)$ is the proper orthochronous Lorentz group, $S^3=Sp(1)$ is the group of the definite form, and $(S^3\times S^3)/\{\pm e_0\}\cong SO(4)$ is the group of the two-sided action on the Euclidean form. The group is the invariant of the geometry: two forms with the same group carry the same geometry, and the isometries are the motions the group supplies. The full symmetry group of the algebra, which is wider than the isometries because the automorphisms need not preserve a form, is a separate object (*Biquaternion Automorphisms and Derivations*).

## The Six Articles

The geometry of the algebra is read in six articles, one per face of it, and each cites the general article of Part IV it depends on.

- **The figure.** *Biquaternion Null Quadric and Projective Geometry* reads the null cone as the equation of a quadric, its rulings, its Segre and Plücker descriptions, and its polarity — the geometry of the form's degenerate locus.
- **The motions.** *Biquaternion Rotations and Lorentz Transformations* reads the isometries: the rotors and the sandwich action, the double covers $SU(2)\to SO(3)$ and $Spin(1,3)\to SO^+(1,3)$, the rotations of the definite form and the boosts of the indefinite one, the two-sided action giving $SO(4)$, and the reflection $\rho_v$.
- **The discrete figures.** *Biquaternion Finite Groups and Figures* reads the finite subgroups of the unit sphere — the twofold preimages of the finite rotation groups — and the figures they determine: the regular $24$-cell with the Hurwitz units as vertices, its symmetry groups $B_4$ and $F_4$, and the McKay correspondence.
- **The full transformation group.** *Biquaternion Automorphisms and Derivations* reads the symmetries of the algebra itself, wider than the isometries: the inner and the outer automorphisms, the projective linear group, and the derivations as the infinitesimal symmetries.
- **The geometries.** *Biquaternion Lorentzian and Conformal Geometry* reads the two real slices: Minkowski space with its light cone, the Lorentz group as the conformal group of the celestial sphere, the conformal group $SU(2,2)\cong Spin(4,2)$, the conformal model of Euclidean space, and the split slice.
- **The spin geometry.** *Biquaternion Spin Geometry* reads the geometry the Clifford structure defines: the spinor module and its two chiral halves, the spinors as the minimal left ideals, the spin representation, and the Dirac operator.

Behind them stand the general articles of Part IV — *Pseudo-Riemannian and Lorentzian Geometry*, *The Conformal Model of Euclidean Space*, *Spin Geometry* and *The Dirac Operator* — and the construction of the rotation and reflection groups in *Biquaternion Rotations and Lorentz Transformations* and *Versors, Rotors and the Sandwich Action* of Part II. Those are cited, not restated.
**Physical reading: the signature is the physics.** The real form of the norm is the choice of geometry: the definite form gives the Euclidean geometry of the informational sector $\mathbb{M}_+$, the signature $(1,3)$ gives the Minkowski geometry of the material sector $\mathbb{M}_-$, and the neutral signature gives the split geometry, so the single complex algebra carries all of them and the passage between them is a change of real form. In the Cayley–Klein picture the physics is its group of motions: $Sp(1)$ for the definite form, $Spin(1,3)$ and $SO^+(1,3)$ for the Lorentzian one, and $(S^3\times S^3)/\{\pm e_0\}\cong SO(4)$ for the two-sided action. The null case is the light cone itself, which is the figure rather than a space — the celestial sphere of *Biquaternion Null Quadric and Projective Geometry* and the causal boundary of *Biquaternion Lorentzian and Conformal Geometry*.

## Summary

The geometry of the biquaternion algebra is decided by its form. The biquaternion norm is complex-valued, and its real forms carry the signatures $(4,0)$, $(0,4)$, $(1,3)$, $(3,1)$, $(1,1)$ and $(3,3)$, with the split realification $(4,4)$; the sign therefore selects a Euclidean, a Lorentzian or a neutral geometry, and the null case gives the quadric as the figure rather than a space. The same algebra carries all of them at once, and the passage between them is a change of real form.

In the Cayley–Klein picture the geometry is its group of motions, and the group is read from the form: $Sp(1)$ for the definite form, $\mathbb{B}^\times_1\cong Spin(1,3)$ and $SO^+(1,3)$ for the Lorentzian one, and $(S^3\times S^3)/\{\pm e_0\}\cong SO(4)$ for the two-sided action. The six articles of the category read the figure, the motions, the discrete figures, the full transformation group, the two real geometries and the spin geometry, each citing the general article of Part IV it depends on and the construction of the rotation groups in Part II. Physically the signature is the organising data, the choice of sector selects the Minkowski or the Euclidean geometry, and the Cayley–Klein picture is the Erlangen reading in which the physics is its group of motions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $N(\tilde{Q})=\sum_\mu Q_\mu^2$ | Biquaternion norm; complex-valued, so the signature lives on a real form |
| $(4,0)$, $(0,4)$ | Signatures of the definite forms on $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ |
| $(1,3)$, $(3,1)$ | Signatures of the Lorentzian forms on $\mathbb{M}_+$, $\mathbb{M}_-$ |
| $(4,4)$ | Split signature of the realification |
| $Sp(1)=S^3$ | Group of the definite form |
| $\mathbb{B}^\times_1\cong Spin(1,3)$ | Group of the Lorentzian form, double cover of $SO^+(1,3)$ |
| $(S^3\times S^3)/\{\pm e_0\}\cong SO(4)$ | Group of the two-sided action on the Euclidean form |
| Null cone, $Q^2$ | The degenerate locus and its projective quadric; the figure |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed., 2001).
- P. Anglès, *Conformal Groups in Geometry and Spin Structures* (Birkhäuser, 2008).
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, 1997).
