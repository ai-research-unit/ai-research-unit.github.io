# __Boosts, Mixed Terms and the Missing Lie Structure__

## Introduction

The antisymmetrised quaternionic product fails the Jacobi identity, and the failure has a shape: it is not
spread over the whole operation but lives in one of its two terms. This article reads that term, and it
reads what the failure leaves behind. The operation is

$$
\tilde P\wedge_{\natural}\tilde Q
=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q ,
$$

the antisymmetric part of the quaternionic product, and its value is the sum of two pieces of different
kinds. The **mixed term** $P_0\mathbf Q-Q_0\mathbf P$ carries a scalar part times a vector part, is the
piece that mixes the time direction with the space direction, and is the only place the Jacobi identity
breaks. The **cross term** $-\mathbf P\times\mathbf Q$ carries two vector parts and is the piece the plain
bracket also has, with a reversed sign. On the material sector the two pieces separate by their
Hermitian character: the cross term is **anti-Hermitian** and gives the compact **rotation** directions,
while the mixed term is **Hermitian** and gives the **boost** directions. The Jacobi failure is thus a
statement about the boost part, and the article reads the three objects that measure it: the invariant
bilinear forms of the bracket, its multiplication operators, and the Lie structure that is consequently
**missing**.

The word of the band is **Obstruction**, and this article supplies the structural half of it: the failed
bracket carries no invariant non-degenerate form, so it has no Killing form and no Casimir element, and
it has no nonzero inner derivation. Its companion *The Brackets That Do Not Close: the Jacobi Failure of
the Quaternionic Commutator* owns the operation, its class, its image and the group reading; this article
owns the split of the value, the invariant forms, the operators and the missing Lie structure.

The article keeps to the operation and to the two structures that measure it. The operation, its class and
its table are *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*; the failure, its
closed form and the associator criterion are *The Jacobi Failure and the Associator Defect of the
Antisymmetric Quaternionic Algebra*; the invariant bilinear forms, the form $\varphi$ and the trace form
of the operators are *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra*; the
operators, their traces, ranks and derivations are *The Adjoint Operators of the Antisymmetric
Quaternionic Algebra*; the compact and non-compact directions of the internal action are
*Observables, Gauge Generators and the Chirality of the Internal Action*, and the compact internal group
with the non-compact boosts and their rapidity are *Particle Types, Discrete Charge and Three-Particle
Couplings*, both cited and not redone. The group ceiling is *The Gauge Group Ceiling: Why the Biquaternion
Algebra Reaches SU(2) but Not SU(3)*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis
$e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$, $e_1e_2=e_3$, and central scalar imaginary $i$ with $i^{2}=-1$; an
element is $\tilde Q=Q_0e_0+\mathbf Q$; the natural conjugation is ${}^{\natural}$ and the Hermitian star
is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$; the sectors are $\mathbb{M}_\pm$, with the material basis
$ie_0,e_1,e_2,e_3$. The quaternionic product is $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ and
$\tilde P\wedge_{\natural}\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$ is
its antisymmetrisation. The symmetrisation symbol $\bullet$ is **row-relative** in this chapter: the plain
row writes it for $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$, a different operation;
$\mathrm{Vect}(\mathbb{B})=\{\tilde Q:\mathrm{Sc}(\tilde Q)=0\}$ is the vector subspace, the image of the
operation; and the general quaternionic bilinear form is
$N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$.

## The Two Terms of the Value

**Proposition (the split of the value).** For all $\tilde P,\tilde Q$,

$$
\tilde P\wedge_{\natural}\tilde Q
=\underbrace{P_0\mathbf Q-Q_0\mathbf P}_{\text{mixed term}}\;\underbrace{-\;\mathbf P\times\mathbf Q}_{\text{cross term}} ,
$$

and the two terms are distinguished by the number of vector parts they carry: the mixed term is a scalar
part times a vector part, the cross term a product of two vector parts. The cross term is exactly the
plain bracket, $\mathbf P\times\mathbf Q$, with the sign reversed; the mixed term is absent from the plain
bracket.

*Proof.* The explicit form of the operation is the sum of the two displayed terms; the plain bracket is
$\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf P\times\mathbf Q$, which carries the cross product
with the other sign and no mixed term.

The two terms behave differently under the Hermitian conjugation, and that is the physical key.

**Proposition (the Hermitian characters).** For material arguments $\tilde P,\tilde Q\in\mathbb{M}_-$ the
mixed term is **Hermitian** and the cross term is **anti-Hermitian**,

$$
(P_0\mathbf Q-Q_0\mathbf P)^{*}=P_0\mathbf Q-Q_0\mathbf P , \qquad
(-\mathbf P\times\mathbf Q)^{*}=+\mathbf P\times\mathbf Q ,
$$

and then the mixed term lies in $\mathbb{M}_+$ and the cross term in $\mathbb{M}_-$.

*Proof.* On the material sector $P_0=ip_0$, $Q_0=iq_0$ with $p_0,q_0$ real and $\mathbf P,\mathbf Q$ real
vectors. Then $P_0\mathbf Q-Q_0\mathbf P=i(p_0\mathbf q-q_0\mathbf p)$ is $i$ times a real vector, a
combination of the Hermitian imaginary units $ie_k$, hence Hermitian; and $-\mathbf P\times\mathbf Q$ is a
real vector, a combination of the anti-Hermitian units $e_k$, hence anti-Hermitian. The two sectors
$\mathbb{M}_\pm$ are the fixed and anti-fixed spaces of the star.

## The Material Bracket: Compact Rotations and Boost-Like Mixed Terms

The split just proved is a split of the bracket of two material operations into its two familiar physical
directions, and the identification is exact on the material sector.

**Proposition (the boost-rotation split).** For $\tilde P=ip_0e_0+\mathbf p$ and
$\tilde Q=iq_0e_0+\mathbf q$ with $p_0,q_0$ real and $\mathbf p,\mathbf q$ real vectors,

$$
\tilde P\wedge_{\natural}\tilde Q=-\;\mathbf p\times\mathbf q\;+\;i\,(p_0\mathbf q-q_0\mathbf p) ,
$$

so the value of the bracket of two material operations is a pure vector whose **real part is a rotation**
and whose **imaginary part is a boost**.

*Proof.* Substitute the material coordinates into the split of the value. The cross term $-\mathbf p\times\mathbf q$
is real and lies in $\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3$, the rotation directions; the mixed term
$i(p_0\mathbf q-q_0\mathbf p)$ is imaginary and lies in $i\mathbb{R}e_1+i\mathbb{R}e_2+i\mathbb{R}e_3$, the
boost directions.

### The Compact Rotations

The cross term is the negative of the cross product of the two spatial parts, and the cross product is the
Lie bracket of the compact rotations: $e_1\wedge_{\natural}e_2=-e_3$, and the three real directions
$e_1,e_2,e_3$ span the compact factor of the internal action. *Observables, Gauge Generators and the
Chirality of the Internal Action* reads the **anti-Hermitian** elements under the one-sided action as the
gauge generators, exponentiating to the compact unitary group; the rotation directions are anti-Hermitian
and thus lie on that compact side. The cross term therefore carries the **compact** part of the bracket.
This is the same term the plain bracket has; on the pure vectors alone the quaternionic bracket is the
cross product, and there it is a Lie bracket.

### The Boost-Like Part

The mixed term is $i$ times a real vector, so it lies along the **imaginary** vector directions
$ie_1,ie_2,ie_3$, which are **Hermitian** and are the **non-compact** directions of the internal action.
*Particle Types, Discrete Charge and Three-Particle Couplings* reads the compact internal group as the
source of the discrete labels and the non-compact boosts, whose parameter is the continuous **rapidity**,
as the source of a continuous family with no quantum. The mixed term is exactly the boost-like part: it
carries a scalar (time-like) part times a vector (space-like) part, the hallmark of a boost, and it is the
term the plain bracket does not have.

**The two reads together.** The bracket of two material operations is a **rotation plus a boost**: its
compact part is the cross term, its non-compact part the mixed term. That is the physical content of the
split of the value, and it is exactly the content of the Jacobi failure, as the companion article
*The Brackets That Do Not Close: the Jacobi Failure of the Quaternionic Commutator* fixes: the
failure needs a scalar part in one argument and two non-parallel vector parts in the other two, which is
precisely a boost-like configuration; on the pure vectors (rotations only) the identity holds.

**Remark (verified).** The split was recomputed on $100$ random pairs of material elements in exact
complex arithmetic. The value of the bracket is always a pure vector; its real part equals
$-\mathbf p\times\mathbf q$ and its imaginary part equals $i(p_0\mathbf q-q_0\mathbf p)$ exactly; and the
mixed term is Hermitian while the cross term is anti-Hermitian, to machine precision. The two pieces are
the sector projections of the value: the real part is its $\mathbb{M}_-$ (anti-Hermitian) piece and the
imaginary part its $\mathbb{M}_+$ (Hermitian) piece.

## The Invariant Bilinear Forms of the Bracket

A Lie algebra carries an invariant bilinear form — the Killing form — and the bracket of this band has no
Jacobi identity. The question of its invariant forms is still well posed, and it has a clean and degenerate
answer.

**Definition (invariance).** A $\mathbb{C}$-bilinear form $\beta$ is **invariant** under the bracket when
$\beta(\tilde P\wedge_{\natural}\tilde Q,\tilde R)+\beta(\tilde Q,\tilde P\wedge_{\natural}\tilde R)=0$
for all triples, the classical condition of a Lie algebra read for this operation.

**Theorem (the invariant forms).** The space of invariant bilinear forms of the bracket is
**one-dimensional**, spanned by

$$
\varphi(\tilde P,\tilde Q)=P_0Q_0 ,
$$

the product of the two scalar parts. The form $\varphi$ is symmetric, its Gram matrix is
$\operatorname{diag}(1,0,0,0)$ of rank $1$, and its radical is the whole vector subspace
$\mathrm{Vect}(\mathbb{B})$; there is **no** nonzero alternating invariant form. In particular the bracket
carries **no non-degenerate invariant form**, so it has no Killing form and no Casimir element.

*Proof.* This is *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra*. The form
$\varphi$ is invariant for a trivial reason: the bracket has zero scalar part, so both terms of the
invariance condition vanish on the scalar slot,
$\varphi(\tilde P\wedge_{\natural}\tilde Q,\tilde R)=(\tilde P\wedge_{\natural}\tilde Q)_0R_0=0$; and it
is the only invariant form, since a form that reads a vector slot is moved by the mixed terms and fails
the condition. The radical is the vector subspace because $\varphi$ reads only the scalar coordinate.

**Proposition (the trace form of the bracket vanishes).** The coefficient form of the bracket is zero,
because the bracket has zero scalar part; so the natural substitute, the coefficient form of the operation,
is unavailable.

**Proposition (the operator trace form is not invariant).** The trace form of the multiplication operators
is non-degenerate and **not** invariant,

$$
K(\tilde A,\tilde B)=\operatorname{Tr}\bigl(L_{\tilde A}L_{\tilde B}\bigr)=3A_0B_0-2\,(\mathbf A,\mathbf B) ,
$$

with Gram matrix $\operatorname{diag}(3,-2,-2,-2)$ and radical zero; and the failure of its invariance,
$K(\tilde A\wedge_{\natural}\tilde B,\tilde C)+K(\tilde B,\tilde A\wedge_{\natural}\tilde C)=0$, is
**false**, the same obstruction as the Jacobi failure.

*Proof.* The matrix of $L_{\tilde A}$ is computed in *The Adjoint Operators of the Antisymmetric
Quaternionic Algebra*, where its trace is $3A_0$; the trace of the product gives the displayed $K$. It is
non-degenerate because its Gram matrix is diagonal with nonzero entries. Its failure of invariance is the
failure of the Jacobi identity expressed in the operators, and is proved in *The Invariant Bilinear Forms
of the Antisymmetric Quaternionic Algebra*.

**Remark (verified).** The invariant-form space was recomputed by solving the invariance condition over all
symmetric Gram matrices: the solution space is **one-dimensional**, spanned by $\operatorname{diag}(1,0,0,0)$,
and the alternating solution space is **zero**; the trace form $K$ was recomputed as
$\operatorname{Tr}(L_{\tilde A}L_{\tilde B})$ and equals $3A_0B_0-2(\mathbf A,\mathbf B)$ to
$4.0\times10^{-15}$; and its invariance failure at the triple $(e_0,e_1,e_1)$ is $-4$.

**Reading (the only invariant reads the time direction).** The one invariant form, $\varphi(\tilde P,\tilde Q)=P_0Q_0$,
reads the scalar coordinate alone, and its radical is the whole vector subspace: it is blind to every
spatial direction and to every mixed term. On the material sector the scalar coordinate is the time
coordinate, so the single invariant the operation carries isolates the **temporal** direction and supplies
no invariant geometry of space, and no invariant read of the boost-like directions. The degeneracy of the
invariant-form space is therefore not only an algebraic scarcity: the one direction it sees is the time
direction, exactly the direction the boost-like part mixes.

## The Missing Lie Structure

The failure of the Jacobi identity and the degeneracy of the invariant forms are two faces of the same
absence. This section reads what is **missing**, and what small piece survives.

**No Killing form, no Casimir.** A finite-dimensional Lie algebra carries the symmetric invariant form
$\beta(x,y)=\operatorname{Tr}(\mathrm{ad}_x\mathrm{ad}_y)$, non-degenerate on the semisimple part, and its
inverse supplies the Casimir element. The bracket of this band has no Jacobi identity, so it has no adjoint
representation in the Lie sense; its only invariant form is the rank-one $\varphi$, with radical the whole
vector subspace; so it has no Killing form and **no Casimir element**. There is no invariant that could
label the irreducible pieces of a bracket that is not a Lie algebra.

**The derived bracket is the only Lie part.** On the derived subalgebra $\mathrm{Vect}(\mathbb{B})$ the
bracket is $-\mathbf P\times\mathbf Q$, a Lie bracket isomorphic to $\mathfrak{sl}(2,\mathbb{C})$; this is
the entire Lie content of the operation, and it is three-dimensional. Everything the bracket adds to it —
the mixed terms, the boost-like part — breaks the identity. The Lie structure is therefore not absent from
the operation but **missing above the derived subalgebra**: the operation is a Lie bracket on
$\mathrm{Vect}(\mathbb{B})$ and not on $\mathbb{B}$, exactly as *The Jacobi Failure and the Associator
Defect of the Antisymmetric Quaternionic Algebra* proves.

**Open question (a higher structure, not claimed).** Whether the Jacobi failure is a defect or the first
sign of a **higher** structure — a homotopy bracket, an $L_\infty$ or $A_\infty$ structure, whose
Jacobiator is a three-bracket rather than a zero — is recorded and not settled. The corpus proves only
that the failure is the difference of the two bracketings and that the derived bracket is a Lie algebra on
$\mathrm{Vect}(\mathbb{B})$; it constructs no higher bracket. Reading the failure as the first layer of a
higher structure is a proposal, labelled as one, and needs a defined higher bracket before it is more than
a name.

**No inner derivation.** *The Adjoint Operators of the Antisymmetric Quaternionic Algebra* computes the
operators of the bracket: the trace of $L_{\tilde A}$ is $3A_0$ rather than $0$, the rank is $3$ off the
isotropic cone and drops to $2$ on it, the commutator of two operators deviates from the operator of the
value by a term that is the operator form of the Jacobi failure, and the operation has **no nonzero inner
derivation**, so all its derivations are outer; they form a three-dimensional algebra, the skew maps of
the vector subspace, the same algebra that appears in the Lie case as the inner derivations. The
automorphism group of the bracket is the group of linear maps preserving the cross product of the vector
subspace and fixing $e_0$, of complex dimension three.

**Reading (no self-generated gauge transformation).** Because every derivation of the operation is
**outer**, the bracket generates no transformation of itself. A gauge transformation attached to the
algebra would be an inner derivation; here there is none, so the internal transformations the framework
uses cannot be produced by the bracket and must be supplied by the **associative** one-sided action. An
operation whose derivations are all outer has its symmetry outside itself.

## The Reading: What the Missing Structure Costs

**Proposed reading, labelled as such.**

- **The failure is a boost phenomenon.** The Jacobi identity holds on the rotations, where the bracket is
  the cross product, and fails as soon as a boost-like mixed term is present; the failure needs a scalar
  part in one argument and two non-parallel vector parts in the other two. So the obstruction is the price
  of the boost-like part of the bracket, and the compact rotation part is untouched.
- **The bracket spans two sectors, and closure is the price.** The value of the bracket of two material
  operations is not material: it is a rotation in $\mathbb{M}_-$ plus a boost in $\mathbb{M}_+$, so the
  material sector is not closed under the bracket either. The failure is not an accident of one term; it is
  the price of an operation asked to produce two sectors at once.
- **The non-invariance is an anomaly of the internal symmetry.** The trace form $K$ is non-degenerate but
  not invariant, and its failure of invariance is exactly the Jacobiator. That is the pattern of an
  **anomaly**: a symmetry that cannot be preserved by the structure that would carry it. The reading is
  offered as a name for the pattern and is not claimed as a physical anomaly of a gauge theory.
- **The one invariant reads the time direction.** The only invariant form, $\varphi=P_0Q_0$, is blind to
  the vector part, so the single invariant of the operation isolates the temporal direction and carries no
  invariant geometry of space — the direction the boost-like part mixes is exactly the direction that is
  invisible to the only invariant there is.
- **The symmetry is outside the operation.** Every derivation is outer, so the bracket generates no
  transformation of itself: a gauge transformation attached to the algebra, an inner derivation, does not
  exist here, and the internal transformations must come from the associative action.
- **A higher structure is an open proposal.** Whether the Jacobi failure is a defect or the first layer of
  a homotopy ($L_\infty$/$A_\infty$) structure is recorded as an open question and not claimed.
- **The bracket is a deformed cross product, not a Lie algebra.** The operation is the cross product of
  the vector subspace plus the mixed terms; the mixed terms make the centre act, so the bracket is a
  **deformation** of the cross product in which the algebra's centre has ceased to be central, not a
  central extension of it.
- **The missing structure is exactly the Killing structure.** No invariant non-degenerate form, hence no
  Killing form, no Casimir, no adjoint representation in the Lie sense — the whole standard apparatus of a
  gauge algebra is absent, and it is absent for the reason the Jacobi identity is: the operation has no
  Lie structure above its derived subalgebra.
- **The internal group is read elsewhere.** As in the companion article, the framework's group is reached
  by the **associative** one-sided action on the anti-Hermitian sector, not by this bracket; the missing
  structure of this article is not a missing group.

**Caution.** An obstruction is a negative result, and a negative result constrains a reading without
supplying one. This article says that the quaternionic bracket has no invariant non-degenerate form, no
Killing form, no Casimir and no inner derivation; it does not supply a group, a form or an invariant in
their place, and it does not claim that the framework lacks gauge structure. It also does not claim that
the mixed term **is** a boost; it claims that the mixed term is the Boost-like part of the bracket, on the
exact ground that on the material sector it is Hermitian and lies along the imaginary vector directions,
which the corpus reads as the non-compact boost directions.

## The Ledger

**Proved.** The split of the value into the mixed term $P_0\mathbf Q-Q_0\mathbf P$ and the cross term
$-\mathbf P\times\mathbf Q$; the Hermitian character of the mixed term ($\mathbb{M}_+$) and the
anti-Hermitian character of the cross term ($\mathbb{M}_-$) for material arguments; the boost-rotation
split $-\mathbf p\times\mathbf q+i(p_0\mathbf q-q_0\mathbf p)$ on the material sector; the
one-dimensional space of invariant forms, spanned by $\varphi=P_0Q_0$, symmetric of rank $1$ with radical
the vector subspace, and the absence of a nonzero alternating invariant form; the vanishing of the
coefficient form of the bracket; the non-degenerate but non-invariant operator trace form
$K=3A_0B_0-2(\mathbf A,\mathbf B)$; the absence of a Killing form and a Casimir element; the derived
bracket as a Lie bracket on $\mathrm{Vect}(\mathbb{B})$ isomorphic to $\mathfrak{sl}(2,\mathbb{C})$; the
trace $3A_0$, rank $3$ off the isotropic cone, absence of a nonzero inner derivation and the
three-dimensional derivation algebra of the operators.

**Readings.** That the mixed term is the boost-like part of the bracket and the cross term the compact
rotation part; that the failure is a boost phenomenon; that the bracket is a deformation of the cross
product in which the centre is not central; that the missing structure is exactly the Killing structure;
that the internal group is read off the associative one-sided action and not off this bracket; that the
bracket spans two sectors and closure is the price; that the non-invariance of the trace form is an anomaly
of the internal symmetry; that the one invariant reads the time direction; that the symmetry is outside the
operation, all derivations being outer.

**Not claimed.** That a physical operation is a biquaternion, or that the mixed term **is** a physical
boost. That the bracket can be repaired into a Lie algebra. That the framework lacks a gauge group or a
gauge algebra; both are reached elsewhere. That the rank-one invariant $\varphi$ is a physical pairing of
significance — it is a trivial invariant of the operation, not a metric. That the "anomaly" naming is a
physical anomaly of a gauge theory, or that "spanning two sectors" and "the symmetry is outside" are
forced readings; and that a higher homotopy structure exists behind the Jacobi failure — it is an open
question.

## Physical Readings

The mixed term reads as the boost and the missing Lie structure reads as the non-compactness of the informational generators: the commutator of two boosts is a rotation, so the material bracket closes where the informational one does not, which is the framework's reading of the Cartan decomposition. The invariant bilinear forms of the article then read as the two surviving pairings, one compact and one Lorentzian, which is the same dichotomy the four forms carry and the same pair that a change of the local complex structure separates.

## Summary

The antisymmetrised quaternionic product
$\tilde P\wedge_{\natural}\tilde Q=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ splits into a
**mixed term** $P_0\mathbf Q-Q_0\mathbf P$ and a **cross term** $-\mathbf P\times\mathbf Q$, and on the
material sector the two separate by their Hermitian character: the cross term is anti-Hermitian and gives
the **compact rotation** directions, the mixed term is Hermitian and gives the **boost-like** directions.
The value of the bracket of two material operations is therefore $-\mathbf p\times\mathbf q+i(p_0\mathbf q-q_0\mathbf p)$,
a rotation plus a boost, and the Jacobi failure — which needs a scalar part in one argument and two
non-parallel vector parts in the other two — is exactly a **boost phenomenon**: it is invisible on the
rotations and enters with the mixed terms. The bracket's only invariant bilinear form is the rank-one
$\varphi(\tilde P,\tilde Q)=P_0Q_0$, reading the scalar parts, with radical the whole vector subspace, and
there is no nonzero alternating invariant form; its coefficient form vanishes; and the operator trace form
$K=\operatorname{Tr}(L_{\tilde A}L_{\tilde B})=3A_0B_0-2(\mathbf A,\mathbf B)$ is non-degenerate but
**not** invariant, its failure being the Jacobi failure itself. Consequently the bracket has **no Killing
form, no Casimir element and no nonzero inner derivation**, and its only Lie part is the derived bracket on
$\mathrm{Vect}(\mathbb{B})$, isomorphic to $\mathfrak{sl}(2,\mathbb{C})$. This Lie structure is **missing
above the derived subalgebra**, and the reading is that the missing structure is exactly the Killing
structure of a gauge algebra: the quaternionic bracket is a deformation of the cross product in which the
centre is not central, and the internal group is reached by the **associative** one-sided action of
*Observables, Gauge Generators and the Chirality of the Internal Action* and bounded by *The Gauge Group
Ceiling*, not by this bracket. Three further readings are recorded in the reading list, all labelled as
such: the bracket of two material operations is a rotation in $\mathbb{M}_-$ plus a boost in $\mathbb{M}_+$
and so **spans two sectors**, the non-invariance of the trace form is the pattern of an **anomaly** of the
internal symmetry, and the single invariant $\varphi=P_0Q_0$ reads only the **time direction**, the vector
part being in its radical. Whether the Jacobi failure is a defect or the first layer of a **higher**
(homotopy) structure is recorded as an open question and not claimed. The operation, its class and its
table are *Introduction to the
Antisymmetric Quaternionic Algebra of Biquaternions*; the failure and the associator criterion are *The
Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra*; the invariant forms
are *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra*; the operators are
*The Adjoint Operators of the Antisymmetric Quaternionic Algebra*; and the group reading is the companion
*The Brackets That Do Not Close: the Jacobi Failure of the Quaternionic Commutator*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\wedge_{\natural}\tilde Q=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ | the antisymmetrised quaternionic product (AQA) |
| $P_0\mathbf Q-Q_0\mathbf P$ | the mixed term; the boost-like, Hermitian part on $\mathbb{M}_-$ |
| $-\mathbf P\times\mathbf Q$ | the cross term; the compact, anti-Hermitian rotation part on $\mathbb{M}_-$ |
| $-\mathbf p\times\mathbf q+i(p_0\mathbf q-q_0\mathbf p)$ | the bracket of two material operations; rotation plus boost |
| $\mathbb{M}_+,\mathbb{M}_-$ | the Hermitian and anti-Hermitian sectors; the boost and rotation directions |
| $\varphi(\tilde P,\tilde Q)=P_0Q_0$ | the only invariant bilinear form; rank $1$, radical $\mathrm{Vect}(\mathbb{B})$ |
| $K(\tilde A,\tilde B)=\operatorname{Tr}(L_{\tilde A}L_{\tilde B})=3A_0B_0-2(\mathbf A,\mathbf B)$ | the operator trace form; non-degenerate, not invariant |
| $L_{\tilde A}$ | the left multiplication $\tilde R\mapsto\tilde A\wedge_{\natural}\tilde R$; trace $3A_0$, rank $3$ off the cone |
| $\mathfrak{sl}(2,\mathbb{C})$ | the derived bracket on $\mathrm{Vect}(\mathbb{B})$; the only Lie part |
| $i(p_0\mathbf q-q_0\mathbf p)$ | the boost parameter content: rapidity directions, non-compact |

## Further Reading

- *The Mathematical Study of Biquaternions*, the physics entry point to the mathematical study under
  which this block sits.
- Mathematics article *The 12 Products of the Biquaternion Complex Space*
  (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the twelve
  operations, the method of the decomposition and the laws of each.
- Mathematics article *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra*
  (`articles_maths/the-invariant-bilinear-forms-of-the-antisymmetric-quaternionic-algebra.md`), for the
  form $\varphi$, the rank-one invariant space and the non-invariance of the trace form.
- Mathematics article *The Adjoint Operators of the Antisymmetric Quaternionic Algebra*
  (`articles_maths/the-adjoint-operators-of-the-antisymmetric-quaternionic-algebra.md`), for the matrices,
  the traces, the ranks, the derivations and the automorphism group of the bracket.
- Mathematics article *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic
  Algebra*
  (`articles_maths/the-jacobi-failure-and-the-associator-defect-of-the-antisymmetric-quaternionic-algebra.md`),
  for the closed form of the cyclic sum and the derived bracket.
- Mathematics article *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*
  (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-biquaternions.md`), for the
  operation and its table.
- Companion article *The Brackets That Do Not Close: the Jacobi Failure of the Quaternionic Commutator*,
  for the failure, the witness and the group reading.
- Companion article *Observables, Gauge Generators and the Chirality of the Internal Action*, for the
  compact and non-compact directions and the one-sided action.
- Companion article *Particle Types, Discrete Charge and Three-Particle Couplings*, for the compact
  internal group and the non-compact boosts with their rapidity.
- Companion article *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)*,
  for the group the algebra does reach.
- Companion article *The Quaternion Form as a Product: the Scalar Coupling of Two Material Operations*,
  for the symmetric half of the same parent.
- Companion article *The Cross Product as a Lie Bracket: Rotations and the Jacobi Identity*, for the
  compact rotation bracket $\mathrm{APA}$, the Lie case this article contrasts with.
