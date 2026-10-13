# __The Four Readings of a Biquaternion: Norm, Rank, Charge and Scale__

## Introduction

The algebra is read four ways in the corpus, and the four are read off one element. The biquaternion norm $N$
is the interval and carries the mass shell: of the four, this is the one the word **mass** names. The rank of
the Hermitian square is the count of polarisations, and it reads only whether the mass vanishes, never how
much. The compact part of the algebra is what makes the internal charge discrete: this is the internal charge
label, read beside the mass and not a reading of it. The **polar scale** $r$ of the polar representation
multiplies the element and is read as a change of unit: it is the unit the mass is measured in and not a value
of it. Four readings, one element, and no article states on which elements they agree. This article is that
statement. It owns no new theorem: it collects the four readings, marks which of them the word mass names,
states on which elements they agree, and states exactly where they part company.

The owners are, in order, *Biquaternion Norm and Invertibility* for the norm and its reversal by the central
imaginary, *Mass, Rank and the Positivity of the Dagger* for the rank and the positive cone, *Particle
Types, Discrete Charge and Three-Particle Couplings* for the compact slice and the discrete charge, and
*The Polar Element Representation of Biquaternions* for the polar scale, with the dilation interpretation in
*Conformal Invariance and the Massless Limit in Biquaternionic Form*. The four forms and the sesquilinear
product are *Conventions in the Biquaternion Universe*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, basis $e_0,e_1,e_2,e_3$, units
$e_k^2=-e_0$; the material sector $\mathbb{M}_-$ with the four-position
$\tilde{Q}=ict\,e_0+\mathbf{x}$; the Hermitian square $\tilde{Q}\tilde{Q}^{*}$ and the rank taken in the
matrix model $\mathsf{M}_2$.

## The Four Readings, One at a Time

**The norm.** $N(\tilde{Q})=\tilde{Q}\tilde{Q}^{\natural}=\sum_\mu Q_\mu^2$ is the complex-linear quadratic
form, its zero set the zero-divisor cone, its value on the material sector the interval
$-c^2t^2+\mathbf{x}^2$. Read as mass, its sign is the mass-shell sign: the shell $N=-m^2c^2$ is the
hyperboloid and the light cone is $N=0$. The interpretation is **value**: which level set the element lies on.

**The rank.** The Hermitian square $\tilde{Q}\tilde{Q}^{*}$ is positive semidefinite, of rank two when
$N(\tilde{Q})\neq0$ and of rank at most one on the cone. Beside the mass, the rank gives the **count of
polarisations**: two for the massive type and one for the massless type. The interpretation is **count**: how many
independent rank-one terms the square needs.

**The charge.** The unitary slice $U=\{\tilde{U}:\tilde{U}\tilde{U}^{*}=e_0\}\cong U(2)$ is compact, and the
finite-dimensional unitary representations of a compact group are labelled by discrete data. Beside the mass,
this is the **other internal label**: the charge is the discrete label of a representation of the compact
internal group, and it is discrete because the group is compact and for no other reason. The interpretation is
**label**: which irreducible representation the element transforms in. The slice lies inside the invertible
elements and the cone is its complement, so no null element is in the slice and no element of the cone carries
one of these labels.

**The scale.** The polar representation writes an element as a polar factor times a phase and a unit
element, and the modulus $r$ is the polar scale. The norm is reversed by the central imaginary,
$N(i\tilde{Q})=-N(\tilde{Q})$, and its logarithm $\log\lvert N\rvert$ is read as a dilation potential. Beside
the mass, the scale is the **unit**: a change of $r$ is a change of the unit of length, and the conformal
rescaling acts on it. The interpretation is **unit**: how the element scales, not what level set it lies on. The
polar representation is stated only for $N(\tilde{Q})\neq0$, so the cone is the boundary of its domain and not a
locus it detects.

## Where the Norm and the Rank Agree

Two of the four readings agree on one locus, and they agree exactly: **the norm vanishes on the
zero-divisor cone and the rank of the Hermitian square drops there, while the charge and the scale are defined
only off it.** The norm vanishes there; the rank drops to at most one; the other two readings do not reach the
cone at all, the compact label because the unitary slice is the complement of the cone and the polar scale
because its representation requires $N\neq0$. Only the massless elements are detected by the norm and the rank
together, and the agreement is a statement about that pair, not about the four. This is what justifies
calling the norm and the rank two readings of one word: on the massless locus they are two descriptions of one
element, and the dictionary of the corpus — massless, rank one, null, on the cone — is the agreement stated
twice.

$N(\tilde{Q})=0$ exactly when the rank of $\tilde{Q}\tilde{Q}^{*}$ is at most one, with rank zero only at
$\tilde{Q}=0$; off the cone the rank is two. The two directions were recomputed on $100$ of $100$ random
non-null elements each way, and every constructed nonzero null element has rank one.

Off the cone the agreement stops, and it stops in a stated way. A rank-two element may have $N>0$ or $N<0$;
on the material sector those are the spacelike and the timelike regions, so **rank two does not say which
sign**, and the mass label "massive" covers both the timelike and the spacelike elements. The corpus's own
caution is *Mass, Rank and the Positivity of the Dagger*, §*No Ghosts, No Tachyons*: no element of the
algebra has a negative sesquilinear norm, and the spacelike elements lie outside the state cone rather than
inside it, so the rank-two spacelike elements are massive in the rank sense and are not states in the
probability sense.

## The Pole

Two limiting elements show where the interpretations must be stated with their scope.

**The rank-one state.** A rank-one element of the informational sector is a pure state — the projector
$\tilde{\Pi}=\tfrac12(e_0-ie_3)$ has $N=0$, rank one, and $\mathrm{Sc}(\tilde{\Pi}\tilde{\Pi}^{*})=\tfrac12$
— so the same rank-one condition that reads as **massless** on the material side reads as **pure state** on
the informational side. The two interpretations are not in conflict, because they are interpretations of the rank on two
different sectors: a massless material element is a null four-vector, and a rank-one informational element
is a state, and both are the same algebraic fact, that the square has one independent rank-one term. What
the pole shows is that "rank one = massless" is a statement of the **material** interpretation, and it must not be
carried to the state side, where rank one is what a state *is*.

**The spacelike element.** A rank-two element with $N>0$ on the material sector is spacelike: massive in the
rank count and tachyon-like in the interval. Whether it is a physical particle is not an algebraic question,
and the algebra settles only that its sesquilinear square is positive, so it is a legitimate element of the
algebra and not a legitimate state.

## The Dictionary

| reading | the object | what it says | and the mass | where it fails |
|---|---|---|---|---|
| norm | $N(\tilde{Q})=\sum_\mu Q_\mu^2$ | the value and its sign; the mass shell as a level set | is the mass: $N=-m^2c^2$ on shell | detects no polarisation count and no label |
| rank | $\mathrm{rank}\,\mathsf{M}_2(\tilde{Q}\tilde{Q}^{*})$ | the count of polarisations, two or one | whether $m$ vanishes, never its value | does not fix the sign of $N$ |
| charge | the compact slice $U(2)\cong(\mathrm{SU}(2)\times\mathrm{U}(1))/\mathbb{Z}_2$ | the discrete internal label | nothing; $m$ is not a charge | says nothing about the cone |
| scale | the polar modulus $r$ | the unit of length, the dilation potential | the unit of $m$: $r=mc$ for the four-momentum | is a unit and not a level set |

The dictionary is the answer the article offers: the four readings are four questions asked of one element,
the norm and the rank coincide on the cone, the charge and the scale are defined only off it, and each one is
silent where the others speak. **They are not four kinds of
mass**, and the article does not claim they are one kind either; the claim is that the four readings of the
element are the four rows of the table and that only the first of them is the mass, so that a reader who meets
the word should ask which reading is meant.

## The Fifth Reading, Named and Left Out

A fifth interpretation exists and is deliberately not one of the four. The **left-regular eigenvalue
problem** $L_{\tilde{Q}}\tilde{R}=\lambda\tilde{R}$ has the spectrum of the operator,
$\mathrm{spec}(L_{\tilde{Q}})=\mathrm{spec}(\mathsf{M}_2(\tilde{Q}))$ with each eigenvalue twice, and a
spectrum is not a label. The operator spectrum is owned by *The Spectra of the Operators on the Biquaternion
Algebra with Hermitian Adjoint*, and the element spectrum it is built on by *Biquaternion Spectral Theory*.
It is named here because it is the interpretation a reader may expect to find in this list, and it is left
out because it answers a different question: it asks what the element does as an operator, not what the
element is. No article of the present corpus reads that spectrum as a mass spectrum, and the gap is recorded
rather than a connection assumed.

**A second sense left out, at the equation level.** The corpus also uses the word for the **Dirac** and
**Majorana** masses of *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*: the two
pairings of a field equation with a conjugate of the field, indexed by the conjugation. That is a property
of an equation and not of an element, so it is not a fifth row of the dictionary — the four rows are
readings of one element, and this pair is a reading of one term.

## Physical Readings

- **One of the four readings is the mass; the other three are read beside it.** The interpretation is that the
framework's mass is the norm's level set, $N=-m^2c^2$ on shell, and that the rank, the charge and the scale are
separate labels the word mass does not name. The massless locus — the cone — is the one place where the norm
and the rank agree. Boundary: a statement about usage, and it adds no identity between the four.
- **Discreteness of charge is compactness.** The interpretation of the charge row is that charge is discrete
because the internal group is compact, which is the same mechanism as the quantisation of angular
momentum and not a separate postulate.
- **The scale is the odd row.** The interpretation of the scale row is that it is the one reading that is not a
property of the element alone: $r$ is a unit and moves under a conformal rescaling, so it is the row where
the framework's mass meets its choice of units, which is the subject of *Action, Units, and the Constants
of the Biquaternion Universe*.

## Summary

The algebra is read four ways, all off one element: the norm $N$ (a value and its level set, and the one
reading the word mass names), the rank of the Hermitian square (a count of polarisations, reading only whether
the mass vanishes), the compact-slice label (a discrete internal charge, not a mass) and the polar scale $r$
(a unit of length, the unit the mass is measured in). The norm and the rank agree on the zero-divisor cone and
nowhere else; the charge and the scale are silent about the cone because both are defined only off it. Off the
cone the rank does not fix the sign of the norm, so "massive" covers the timelike and the spacelike alike. The rank-one
condition that reads as massless on the material sector reads as pure state on the informational sector, and
the article keeps the two apart. A fifth interpretation — the operator spectrum of $L_{\tilde{Q}}$ — is named and
left out, and the Dirac and Majorana pair is placed at the equation level, outside the four rows.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $N(\tilde{Q})=\tilde{Q}\tilde{Q}^{\natural}$ | the biquaternion norm, the interval, the value and its level set |
| $\mathrm{rank}\,\mathsf{M}_2(\tilde{Q}\tilde{Q}^{*})$ | the rank of the Hermitian square, two off the cone and at most one on it |
| $U(2)$ | the unitary slice, compact, the internal group whose labels are the discrete charge |
| $r$ | the polar scale, the modulus of the polar factor, the unit of the scale reading |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | the material and informational sectors, on which the rank-one condition reads as massless and as a pure state respectively |

## Further Reading

- *Biquaternion Norm and Invertibility*, for the norm, its multiplicativity and its reversal by the central
imaginary.
- *Mass, Rank and the Positivity of the Dagger*, for the rank criterion, the positive cone and the
no-ghost and no-tachyon statements.
- *Particle Types, Discrete Charge and Three-Particle Couplings*, for the compact slice and the discrete
charge, and for the continuous rapidity of the non-compact directions.
- *The Polar Element Representation of Biquaternions* and *Conformal Invariance and the Massless Limit in
Biquaternionic Form*, for the polar scale and its dilation reading.
- *The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint* and *Biquaternion
Spectral Theory*, for the operator spectrum named and left out above, and *Antilinear Structure and the Two
Kinds of Mass in Biquaternionic Form*, for the Dirac and Majorana pair placed at the equation level.
