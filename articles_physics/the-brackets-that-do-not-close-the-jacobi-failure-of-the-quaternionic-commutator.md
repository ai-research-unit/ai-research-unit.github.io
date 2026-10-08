# __The Brackets That Do Not Close: the Jacobi Failure of the Quaternionic Commutator__

## Introduction

A bracket that is to generate a group must satisfy the Jacobi identity. The antisymmetrised part of the
quaternionic product is a bracket — bilinear, alternating, vector valued, the natural candidate — and it
does **not** satisfy the identity. This article reads the failure and its physical consequence. The
operation is the **antisymmetrised quaternionic product**

$$
\tilde P\wedge_{\natural}\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P\bigr)
=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q ,
$$

the antisymmetric part of the quaternionic product $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ for
the exchange of its two arguments, and half the quaternionic bracket
$[\tilde P,\tilde Q]_{\natural}=\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P$. Its value has
zero scalar part, so it is a **pure vector**; it is **alternating**, so its diagonal vanishes; and its
**Jacobi sum** does not vanish. The witness on which the corpus reads the failure is
$(\tilde P,\tilde Q,\tilde R)=(e_0,e_1,e_2)$, where the cyclic sum is $-e_3$. The cause is exact and is
not an accident of the witness: the failure is the **associator defect** of the parent quaternionic
product, and non-associativity alone produces it. The physical consequence is the band's word,
**Obstruction**: the quaternionic commutator cannot be the Lie algebra of an internal group.

The word of the band is **Obstruction**, and the article earns it from a negative result. The companion
band, `Focus on the Symmetric Quaternionic Algebra (SQA) — Coupling`, is the other half of the same
parent: the two halves reconstruct it,

$$
\tilde P^{\natural}\tilde Q=\tilde P\bullet\tilde Q+\tilde P\wedge_{\natural}\tilde Q ,
$$

and the division of labour between them is the point of the row. The symmetric half is central valued and
carries the interval; the antisymmetric half is vector valued and carries the order, and it is the half
that fails.

The article keeps to the operation and to the failure. The operation, its image and its table are
*Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*; the cyclic sum, its closed form
and the associator criterion are *The Jacobi Failure and the Associator Defect of the Antisymmetric
Quaternionic Algebra*; the associator of the parent product is *The Associator and the Ternary Product of
the Quaternionic Product*; the general criterion relating an antisymmetrised algebra to the associator of
its parent is *The Symmetric and Antisymmetric Parts of an Algebra Product*; the invariant bilinear forms
and the operators of the bracket are the companion article *Boosts, Mixed Terms and the Missing Lie
Structure*; and the group the algebra does reach, and the group it does not, are *The Gauge Group Ceiling:
Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)*, cited and not redone.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis
$e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$, $e_1e_2=e_3$, and central scalar imaginary $i$ with $i^{2}=-1$; an
element is $\tilde Q=Q_0e_0+\mathbf Q$ with vector part $\mathbf Q=Q_1e_1+Q_2e_2+Q_3e_3$; the complex
bilinear dot and cross products of vector parts are $(\mathbf P,\mathbf Q)$ and $\mathbf P\times\mathbf Q$,
and the cross product is defined by $e_j\times e_k=e_l$ cyclically. The natural conjugation is
${}^{\natural}$, the Hermitian star is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, and the sectors are
$\mathbb{M}_\pm$. The ordinary product is $\tilde P\tilde Q$; the quaternionic product is
$\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$, with bracket
$[\tilde P,\tilde Q]_{\natural}=\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P$; and
$\tilde P\bullet\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$ is its
symmetrisation. The symmetrisation symbol $\bullet$ is **row-relative** in this chapter: the plain row
writes it for $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$, a different operation; the plain row writes
$\wedge$ for its antisymmetrisation, the cross product $\mathbf P\times\mathbf Q$. The vector subspace is
$\mathrm{Vect}(\mathbb{B})=\{\tilde Q:\mathrm{Sc}(\tilde Q)=0\}$, the image of the operation; the
general plain bilinear form is $B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)$ and the general
quaternionic bilinear form is $N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$.

## The Antisymmetrised Quaternionic Product

**Proposition (the explicit form).** For all $\tilde P=P_0e_0+\mathbf P$ and $\tilde Q=Q_0e_0+\mathbf Q$,

$$
\tilde P\wedge_{\natural}\tilde Q
=\tfrac12\bigl(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P\bigr)
=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q .
$$

The value has zero scalar part and lies in the vector subspace $\mathrm{Vect}(\mathbb{B})$; the operation
is $\mathbb{C}$-bilinear and alternating, $\tilde Q\wedge_{\natural}\tilde P=-\tilde P\wedge_{\natural}\tilde Q$,
and its diagonal vanishes. It is half the quaternionic bracket,
$\tilde P\wedge_{\natural}\tilde Q=\tfrac12[\tilde P,\tilde Q]_{\natural}$.

*Proof.* The parent value is
$\tilde P^{\natural}\tilde Q=[P_0Q_0+(\mathbf P,\mathbf Q)]e_0+P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$
(*The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*). Exchanging the arguments reverses
the two mixed terms and the cross product and leaves the scalar part fixed, which cancels in the
difference; half the difference is the displayed value. The scalar part zero puts the value in
$\mathrm{Vect}(\mathbb{B})$; alternation is the antisymmetry of the definition and its diagonal is the
cancellation at $\tilde P=\tilde Q$.

**Remark (what the antisymmetrisation removes).** The scalar part of the parent product is exactly the
symmetric half, the operation of the companion band SQA; the antisymmetrisation is what remains after that
half is removed, and it never produces a central element. The symmetric half also carries the interval,
since $\tilde Q\bullet\tilde Q=N(\tilde Q)e_0$; the antisymmetric half carries the opposite, the part of
the product that the interval does not see. The reader must hold the two bands together to read the row.

### The Sixteen Brackets of the Basis

On the complex basis $e_0,e_1,e_2,e_3$, with the row index the left argument and the column index the
right one, the operation reads

| $\wedge_{\natural}$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $0$ | $e_1$ | $e_2$ | $e_3$ |
| $e_1$ | $-e_1$ | $0$ | $-e_3$ | $e_2$ |
| $e_2$ | $-e_2$ | $e_3$ | $0$ | $-e_1$ |
| $e_3$ | $-e_3$ | $-e_2$ | $e_1$ | $0$ |

**Proposition (the table).** The table is alternating with zero diagonal; the mixed entries are
$e_0\wedge_{\natural}e_k=e_k$ and $e_k\wedge_{\natural}e_0=-e_k$; on the pure vectors the operation is the
negative of the cross product, $e_j\wedge_{\natural}e_k=-e_j\times e_k$; and the element $e_0$ is a left
identity on the vector subspace and its negative on the right.

*Proof.* Read the explicit form on the basis; the scalar-vanishing cases give the mixed signs
$P_0\mathbf Q$ and $-Q_0\mathbf P$, and the pure-vector cases give $-\mathbf P\times\mathbf Q$. The table
is the one of *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*.

Twelve of the sixteen entries are nonzero: the operation is not the zero bracket, and on the vector
subspace it is the plain cross product up to the overall sign.

### The Image Is the Whole Vector Subspace

**Proposition (the image).** $\mathbb{B}\wedge_{\natural}\mathbb{B}=\mathrm{Vect}(\mathbb{B})$, of complex
dimension three, and it contains no nonzero central element. The operation has no unit on either side.

*Proof.* Every value has zero scalar part, so the image lies in $\mathrm{Vect}(\mathbb{B})$; conversely,
$e_0\wedge_{\natural}\tilde Q=\mathbf Q$, so every pure vector is a value. The centre is the set of
elements with zero vector part, whose intersection with $\mathrm{Vect}(\mathbb{B})$ is $0$. A unit
$\tilde E$ would satisfy $\tilde E\wedge_{\natural}\tilde X=\tilde X$ for all $\tilde X$; at
$\tilde X=e_0$ the value is $-\mathbf E$, a pure vector, which cannot equal the central $e_0$, so no left
unit exists; the same argument on the right excludes a right unit.

The image is the **whole** vector subspace (complex dimension three, real dimension six) and not a
subalgebra of the algebra; this is the object the companion article reads as the home of the rotations
and the boosts.

## The Jacobi Identity Fails

**Theorem (the identity fails).** The operation does not satisfy the Jacobi identity. At the triple
$(e_0,e_1,e_2)$ the cyclic sum — the left-nested Jacobiator of the corpus, the same nesting as in the
mathematics counterpart — is

$$
J(e_0,e_1,e_2)=(e_0\wedge_{\natural}e_1)\wedge_{\natural}e_2
+(e_1\wedge_{\natural}e_2)\wedge_{\natural}e_0
+(e_2\wedge_{\natural}e_0)\wedge_{\natural}e_1=-e_3 ,
$$

which is nonzero, so the Jacobi identity is false.

*Proof.* From the table, $e_0\wedge_{\natural}e_1=e_1$ and $e_1\wedge_{\natural}e_2=-e_3$, so the first term
is $e_1\wedge_{\natural}e_2=-e_3$; $e_k\wedge_{\natural}e_0=-e_k$, so the second term is
$(-e_3)\wedge_{\natural}e_0=+e_3$; and $e_2\wedge_{\natural}e_0=-e_2$ with
$e_2\wedge_{\natural}e_1=+e_3$, so the third term is $(-e_2)\wedge_{\natural}e_1=-e_3$. The three terms are
$-e_3,+e_3,-e_3$ and the sum is $-e_3$.

### The Closed Form and When the Sum Vanishes

**Theorem (the closed form).** For general elements the cyclic sum is

$$
J(\tilde P,\tilde Q,\tilde R)
=-P_0\,(\mathbf Q\times\mathbf R)+Q_0\,(\mathbf P\times\mathbf R)-R_0\,(\mathbf P\times\mathbf Q) ,
$$

a $\mathbb{C}$-trilinear alternating pure-vector map, $\mathbb{C}$-linear in the triple of scalar parts
$(P_0,Q_0,R_0)$ and vanishing identically in them if and only if the three vector parts are pairwise
parallel.

*Proof.* This is *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic
Algebra*; the identity of the three-cycle is proved there monomial by monomial, the double cross products
collapsing by $\mathbf U\times(\mathbf A\times\mathbf B)=\mathbf A(\mathbf U,\mathbf B)-\mathbf B(\mathbf U,\mathbf A)$.

Two consequences fix the incidence of the failure. First, the sum is decided on the basis, because it is
$\mathbb{C}$-trilinear and alternating; it is nonzero on $18$ of the $64$ ordered triples of basis
elements, the three unordered triples $\{0,1,2\}$, $\{0,1,3\}$ and $\{0,2,3\}$ with their six orderings
each, with values the negatives of the three cross products. Second, a witness needs one nonzero scalar
part and two independent vector parts: on the pure vectors alone the operation is the cross product up to
sign, and there it does satisfy the identity. The failure enters **through the mixed terms** $P_0\mathbf Q-Q_0\mathbf P$,
which carry a scalar part into the vector subspace. The three smallest witnesses are
$(e_0,e_1,e_2),(e_0,e_1,e_3),(e_0,e_2,e_3)$; the corpus's canonical witness is the first, with cyclic sum
$-e_3$.

**Remark (on the six subspaces).** The identity holds on the centre and on the vector subspace and fails
on the four four-dimensional subspaces. It holds on the vector subspace because there the operation is
the cross product, which is a Lie bracket; it fails on every subspace that mixes the scalar and vector
directions, which is exactly where the mixed terms live.

**Remark (verified).** The explicit form, the table, the witness, the closed form and the count were
recomputed on the basis and on $100$ random triples in exact complex arithmetic. The explicit form agrees
with $\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$ to $8.9\times10^{-16}$; the
reconstruction $\tilde P^{\natural}\tilde Q=\tilde P\bullet\tilde Q+\tilde P\wedge_{\natural}\tilde Q$
is **exactly** satisfied on every sample, the two halves being exact; the witness gives
$J(e_0,e_1,e_2)=-e_3$ exactly; and the closed form agrees with the cyclic sum to
$8.9\times10^{-15}$ on the random triples.

## The Cause Is the Associator of the Parent Product

The failure is not a numerical accident and not a defect of the class of the operation; it is the
**associator** of the parent quaternionic product. The general criterion is *The Symmetric and
Antisymmetric Parts of an Algebra Product*.

**Theorem (the associator criterion).** For a product over a field of characteristic not $2$, its
antisymmetrisation satisfies the Jacobi identity if and only if the associator satisfies the cyclic
identity of the criterion; equivalently the Jacobi sum of the commutator is the signed sum of the six
associators.

**Corollary (the defect of the quaternionic bracket).** For the block, half the commutator and half the
associator sum stand in the same relation,

$$
J(\tilde P,\tilde Q,\tilde R)
=\tfrac14\sum_{\sigma}\operatorname{sgn}(\sigma)\,
\bigl[\tilde P_{\sigma(1)},\tilde P_{\sigma(2)},\tilde P_{\sigma(3)}\bigr] ,
$$

with the associator $[\tilde X,\tilde Y,\tilde Z]=(\tilde X^{\natural}\tilde Y)^{\natural}\tilde Z-\tilde X^{\natural}(\tilde Y^{\natural}\tilde Z)$
taken in the parent product. The quaternionic product is not associative, so its associator does not
vanish, so the criterion is not met and the bracket is not Lie-admissible.

**Computation (the criterion at the witness).** On the triple $(e_0,e_1,e_2)$ four of the six associators
of the parent product vanish, and the two that survive are at the orderings $(e_1,e_0,e_2)$ and
$(e_2,e_0,e_1)$, with values $+2e_3$ and $-2e_3$; their signed sum is $-4e_3$, and the quarter is $-e_3$,
which is $J(e_0,e_1,e_2)$.

The reading of the mechanism is exact: **the insertion of the natural conjugation in the first slot of the
parent product is what costs the Jacobi identity.** The plain antisymmetrisation, the cross product, keeps
the identity because the plain product is associative; the quaternionic antisymmetrisation loses it because
the first slot is read through a non-automorphism, and the resulting mixed terms break the criterion. The
defect is associativity and nothing else; unlike the two sesquilinear failures of the catalogue, whose
cause is the obstruction of *Lie Algebras of Sesqualgebras*, no involution intervenes in the class of this
operation, which is $\mathbb{C}$-bilinear.

## The Contrast with the Plain Bracket

The antisymmetric part of the **plain** product is the cross product,

$$
\tfrac12\bigl(\tilde P\tilde Q-\tilde Q\tilde P\bigr)=\mathbf P\times\mathbf Q ,
$$

the operation $\mathrm{APA}$ of the catalogue. The two brackets differ in two ways, and both are what the
conjugation inserts. First, the cross term is **reversed**: the plain bracket is $+\mathbf P\times\mathbf Q$,
this one is $-\mathbf P\times\mathbf Q$, and on the pure vectors alone the two agree up to that sign.
Second, the two **mixed terms** $P_0\mathbf Q-Q_0\mathbf P$ are **added** to this bracket and are absent
from the plain one; the plain bracket vanishes whenever either argument is central, while this one does
not, since $Ae_0\wedge_{\natural}\tilde Y=A\,\mathbf Y$. The plain bracket therefore **closes** — it
satisfies the Jacobi identity, it is a Lie bracket, and it is the one Lie product of the twelve operations
— and this bracket does not. On the pure vectors this bracket is the negative of the cross product and it
satisfies the identity there; the failure is entirely the price of the two mixed terms.

**The derived bracket is a Lie bracket.** The derived subalgebra of this operation is the whole vector
subspace, $\mathbb{B}\wedge_{\natural}\mathbb{B}=\mathrm{Vect}(\mathbb{B})$, and on it the operation is
$-\mathbf P\times\mathbf Q$, a Lie bracket isomorphic to the cross product on $\mathbb{C}^3$, hence to
$\mathfrak{sl}(2,\mathbb{C})$. The failure is therefore not a failure of the **derived** bracket; it is the
failure of the extension of that bracket to the whole algebra. This is the exact bound on the negative
reading below: the operation is a Lie bracket **on the vector subspace** and not on $\mathbb{B}$. The
mathematics is *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra*
§*The Derived Bracket*.

## Why This Cannot Be the Lie Algebra of an Internal Group

**Proposed reading, labelled as such.** A bracket generates a group through the exponential of its
representation, and the exponential exists as a group only when the bracket satisfies the Jacobi identity:
the identity is exactly the condition that the bracket be the commutator of an associative algebra or the
tangent bracket of a Lie group. The quaternionic bracket fails it, so **it cannot be the Lie algebra of an
internal group**, and no group and no gauge algebra can be read off it. The two negative readings below
are the content of the band's word, Obstruction.

- **The failure is not removable by a change of sign or of scale.** The defect is the associator of the
  parent product, an intrinsic nonzero object; neither $-\tilde P\wedge_{\natural}\tilde Q$ nor
  $\lambda\,\tilde P\wedge_{\natural}\tilde Q$ changes the associator, and the derived bracket, which does
  close, is the cross product on the vector subspace alone and not a bracket on the whole algebra, so it
  cannot carry the internal action of the whole algebra.
- **The derived bracket is a bound, not a repair.** That the vector subspace is a Lie algebra under this
  operation says where the failure is not; it does not give a bracket on the algebra, and the mixed terms
  cannot be discarded without leaving the quaternionic row.

**The bearing on the gauge ceiling.** The group the algebra does reach is read elsewhere, and this is what
makes the failure informative. *Observables, Gauge Generators and the Chirality of the Internal Action*
reads the gauge generators as the **anti-Hermitian** elements under the **associative** one-sided action,
where the bracket is the plain commutator and closes; *The Gauge Group Ceiling: Why the Biquaternion
Algebra Reaches SU(2) but Not SU(3)* owns the resulting group, the algebra's intrinsic $U(2)$, locally
$SU(2)\times U(1)$, and the ceiling above it. So the internal group is reached by the associative
product and the one-sided action, and **not** by the quaternionic bracket of this article. The failure of
this bracket is therefore not an obstacle to the framework's gauge group; it isolates where the gauge
structure does not come from. A reader who tries to build the internal algebra out of the antisymmetrised
quaternionic product will fail, and the failure is the associator of the quaternionic product.

**Caution.** An obstruction is a **negative result**: it says which operation cannot be the Lie algebra
and supplies no group in its place. This article does not construct an internal group, does not repair the
bracket, and does not claim that the framework lacks gauge structure. It says that the quaternionic
commutator is not a Lie algebra, and it names the reason. The positive statements about the group belong
to the two articles cited above. The failure is a negative result of the same kind as the entries of the
catalogue *What the Biquaternion Algebra Cannot Do: a Catalogue of Algebraic Obstructions*, and it is
written in that catalogue's manner: a **Statement** (the antisymmetrised quaternionic product is not
Lie-admissible), a **Consequence** (no internal group can be read off it), and a **Remedy** (read the
internal group off the associative one-sided action, not off this bracket).

## The Ledger

**Proved.** The explicit form
$\tilde P\wedge_{\natural}\tilde Q=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$, its zero scalar
part, its pure-vector value, its alternation and its vanishing diagonal; its identity with half the
quaternionic bracket; its image $\mathrm{Vect}(\mathbb{B})$; the absence of a unit on either side; the
sixteen brackets of the basis; the failure of the Jacobi identity at the witness $(e_0,e_1,e_2)$ with
cyclic sum $-e_3$; the closed form
$J=-P_0(\mathbf Q\times\mathbf R)+Q_0(\mathbf P\times\mathbf R)-R_0(\mathbf P\times\mathbf Q)$ and its
$18$ nonzero ordered basis triples; the associator criterion and the defect as non-associativity alone;
the contrast with the plain bracket, which closes; the derived bracket on the vector subspace as a Lie
bracket isomorphic to $\mathfrak{sl}(2,\mathbb{C})$.

**Readings.** That the quaternionic commutator cannot be the Lie algebra of an internal group; that the
insertion of the conjugation in the first slot is what costs the Jacobi identity; that the failure enters
through the mixed terms and is invisible on the pure vectors; that the internal group is reached by the
associative one-sided action and not by this bracket.

**Not claimed.** That a physical operation is a biquaternion, or that the bracket is a physical
commutator. That the failure can be repaired, or that a group was expected from this operation. That the
framework lacks a gauge group; the group is read elsewhere. That the obstruction overthrows any physical
result.

## Summary

The antisymmetrised quaternionic product
$\tilde P\wedge_{\natural}\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$
is the antisymmetric part of the quaternionic product for the exchange of its two arguments, pure vector,
alternating, and half the quaternionic bracket; its image is the whole vector subspace
$\mathrm{Vect}(\mathbb{B})$, it has no unit, and on the basis the mixed entries are $e_0\wedge_{\natural}e_k=e_k$,
$e_k\wedge_{\natural}e_0=-e_k$ and the pure-vector entries are the negatives of the cross products. It
**fails the Jacobi identity**, with the witness $(e_0,e_1,e_2)$ whose cyclic sum is $-e_3$; the sum is the
closed form $J=-P_0(\mathbf Q\times\mathbf R)+Q_0(\mathbf P\times\mathbf R)-R_0(\mathbf P\times\mathbf Q)$,
nonzero on $18$ of the $64$ ordered basis triples and decided by the mixed scalar-vector terms. The cause
is the **associator defect** of the parent quaternionic product: the associator criterion reads the failure
off the non-associativity of the parent, and the two surviving associators at the witness, $\pm2e_3$,
give the quarter $-e_3$. The **plain** bracket, the cross product of the plain row, is the contrast and
**closes**; it is the one Lie product of the twelve. On the derived subalgebra $\mathrm{Vect}(\mathbb{B})$
this operation is the negative of the cross product and is a Lie bracket isomorphic to
$\mathfrak{sl}(2,\mathbb{C})$, so the failure is the failure of the extension of that bracket to the whole
algebra. The reading is the band's word **Obstruction**: the quaternionic commutator cannot be the Lie
algebra of an internal group, and no group can be read off it. The internal group the algebra does reach
is the algebra's intrinsic $U(2)$, locally $SU(2)\times U(1)$, read off the **associative** one-sided
action by *Observables, Gauge Generators and
the Chirality of the Internal Action* and bounded by *The Gauge Group Ceiling: Why the Biquaternion
Algebra Reaches SU(2) but Not SU(3)*; the failure of this bracket therefore isolates where the gauge
structure does not come from, and the caution stands that a negative result constrains a reading without
supplying one. The operation, its image and its table are *Introduction to the Antisymmetric Quaternionic
Algebra of Biquaternions*; the cyclic sum and the associator criterion are *The Jacobi Failure and the
Associator Defect of the Antisymmetric Quaternionic Algebra*; the invariant forms and the operators of the
bracket are the companion *Boosts, Mixed Terms and the Missing Lie Structure*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\wedge_{\natural}\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$ | the antisymmetrised quaternionic product (AQA, this band) |
| $[\tilde P,\tilde Q]_{\natural}=\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P$ | the quaternionic bracket; twice the operation |
| $P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ | the explicit form; zero scalar part, pure vector |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, the image of the operation |
| $J(\tilde P,\tilde Q,\tilde R)=(\tilde P\wedge_{\natural}\tilde Q)\wedge_{\natural}\tilde R+(\tilde Q\wedge_{\natural}\tilde R)\wedge_{\natural}\tilde P+(\tilde R\wedge_{\natural}\tilde P)\wedge_{\natural}\tilde Q$ | the Jacobi cyclic sum, left-nested; fails |
| $(e_0,e_1,e_2)$ | the canonical witness; $J=-e_3$ |
| $[\tilde X,\tilde Y,\tilde Z]$ | the associator of the parent product; the defect |
| $\mathbf P\times\mathbf Q$ | the cross product; the plain bracket that closes |
| $\mathfrak{sl}(2,\mathbb{C})$ | the derived bracket on the vector subspace |
| $\tilde P\bullet\tilde Q$ | the symmetric half (SQA); the two halves reconstruct the parent |

## Further Reading

- *The Mathematical Study of Biquaternions*, the physics entry point to the mathematical study under
  which this block sits.
- Mathematics article *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*
  (`articles_maths/the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the twelve
  operations, the method of the decomposition and the laws of each.
- Mathematics article *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*
  (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-biquaternions.md`), for the
  operation, its class, its image and the sixteen brackets.
- Mathematics article *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic
  Algebra*
  (`articles_maths/the-jacobi-failure-and-the-associator-defect-of-the-antisymmetric-quaternionic-algebra.md`),
  for the cyclic sum, its closed form, the associator criterion and the derived bracket.
- Mathematics article *The Associator and the Ternary Product of the Quaternionic Product*
  (`articles_maths/the-associator-and-the-ternary-product-of-the-quaternionic-product.md`), for the
  associator of the parent product.
- Mathematics article *The Symmetric and Antisymmetric Parts of an Algebra Product*
  (`articles_maths/the-symmetric-and-antisymmetric-parts-of-an-algebra-product.md`), for the general
  associator criterion.
- Companion article *The Quaternion Form as a Product: the Scalar Coupling of Two Material Operations* and
  *Why a Central Product Cannot Compose: the Radical and the Isotropic Elements*, for the symmetric half
  of the same parent.
- Companion article *Boosts, Mixed Terms and the Missing Lie Structure*, for the mixed term, the invariant
  forms and the operators of this bracket.
- Companion article *Observables, Gauge Generators and the Chirality of the Internal Action*, for the
  compact and non-compact directions and the one-sided action that does carry the group.
- Companion article *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)*,
  for the group the algebra reaches.
- Companion article *The Cross Product as a Lie Bracket: Rotations and the Jacobi Identity*, for the plain
  bracket $\mathrm{APA}$ that does satisfy the identity and is the one Lie product of the twelve.
- Companion article *A Bracket Invisible on the Real Forms: the Complex Witness of the Jacobi Failure*, for
  one of the two sesquilinear Jacobi failures contrasted here, whose witness needs a complex element.
- Companion article *What the Biquaternion Algebra Cannot Do: a Catalogue of Algebraic Obstructions*, for
  the catalogue of negative results this failure belongs to.
