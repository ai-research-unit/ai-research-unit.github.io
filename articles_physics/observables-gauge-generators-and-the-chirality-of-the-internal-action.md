# __Observables, Gauge Generators and the Chirality of the Internal Action__

## Introduction

The informational sector carries the observables and the material sector carries the generators of the
internal symmetry. This article states the algebra behind that division and the operator structure that
expresses it. A left multiplication by a **Hermitian** element is self-adjoint and is read as an
**observable**; a left multiplication by an **anti-Hermitian** element is skew-adjoint and is read as a
**gauge generator**, exponentating to the internal unitary group. The two-sided action
$\tilde Q\tilde P\tilde Q^{*}$ — the **sandwich** — is a different kind of operator: it can be self-adjoint
and can never be skew-adjoint, which is why the sandwich serves as an action and the one-sided
multiplication as an operator algebra. Finally the internal symmetry acts on the module through **right**
multiplication and not through left: only the right action preserves the algebra-valued canonical form, and
the one-sidedness of that form is the framework's reading of a **chirality** in the internal action.

The article keeps to the operator structure. It defers the positivity of the dagger and the positive cone
to *Mass, Rank and the Positivity of the Dagger*; the internal group and its compactness to *Particle Types, Discrete Charge and Three-Particle Couplings*; the group ceiling to *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)*; the states to *The States the Indefinite Metric Cannot Normalise* and *Decoherence as Idempotent Projection*;
and the mathematics of the adjoints and the sandwiches to the mathematics articles *The Adjoints of the
Regular Operators*, *The Two-Sided Operators on a Hermitian Algebra* and *Jordan
Algebras of Sesqualgebras*.

**Conventions.** As in the two companion articles of this block: $\mathbb{B}$ with basis
$e_0,e_1,e_2,e_3$, $e_k^{2}=-e_0$; the sesquilinear product $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$;
the Hermitian form $\langle\tilde P,\tilde R\rangle_{*}=\mathrm{Sc}(\tilde P\tilde R^{*})=\sum_\mu P_\mu\overline{R_\mu}$, positive definite, with $\mathrm{Tr}=2\,\mathrm{Sc}$; the sectors
$\mathbb{M}_\pm$; $L_{\tilde B}$ and $R_{\tilde B}$ the left and right multiplications by $\tilde B$; and
the canonical form $h(\tilde P,\tilde R)=\tilde P\tilde R^{*}$, with values in the algebra.

## The Two Kinds of One-Sided Operator

**Proposition (adjoint of a one-sided operator).** For every $\tilde B$,

$$
\bigl(L_{\tilde B}\bigr)^{\dagger}=L_{\tilde B^{*}},\qquad
\bigl(R_{\tilde B}\bigr)^{\dagger}=R_{\tilde B^{*}} .
$$

**Proof.** $\langle L_{\tilde B}\tilde T,\tilde V\rangle_{*}=\mathrm{Sc}\bigl((\tilde B\tilde T)\tilde V^{*}\bigr)=\mathrm{Sc}\bigl(\tilde T\tilde V^{*}\tilde B\bigr)=\langle\tilde T,L_{\tilde B^{*}}\tilde V\rangle_{*}$, by the cyclicity of the scalar part; the right-handed computation
is the same. $\square$

The classification follows from the sector of the parameter.

| Parameter | Sector | Operator | Kind | Physical role |
|---|---|---|---|---|
| $\tilde H$, $\tilde H^{*}=\tilde H$ | $\mathbb{M}_+$ | $L_{\tilde H}$ | self-adjoint | observable |
| $\tilde S$, $\tilde S^{*}=-\tilde S$ | $\mathbb{M}_-$ | $L_{\tilde S}$ | skew-adjoint | gauge generator |

The correspondence is linear and bijective at the level of parameters, so the two kinds of operator are in
bijection with the two sectors, and the informal rule "observables in $\mathbb{M}_+$, generators in
$\mathbb{M}_-$" has this exact content. Two further facts fix the physical reading. The skew-adjoint
operators exponentiate to the unitaries of the module, $e^{L_{\tilde S}}=L_{e^{\tilde S}}$, and the
resulting group is the internal $U(2)$; and multiplication by the central $i$ exchanges the two kinds,
$L_{i\tilde H}=iL_{\tilde H}$, so the generator of a unitary is one sector away from the observable.

## The Sandwich: Self-Adjoint, Never Skew-Adjoint

**Definition.** The **sandwich** by $\tilde Q$ is $\Theta_{\tilde Q}(\tilde P)=\tilde Q\tilde P\tilde Q^{*}$, the two-sided operator of the corpus.

Its parameter enters **twice**, so the sandwich is quadratic in $\tilde Q$ and its matrix image is
$\Phi(\tilde P)\mapsto\Phi(\tilde Q)\Phi(\tilde P)\Phi(\tilde Q)^{\dagger}$. Its adjoint is

$$
\bigl(\Theta_{\tilde Q}\bigr)^{\dagger}=\Theta_{\tilde Q^{*}} .
$$

**Proposition (which sandwiches are self-adjoint).** $\Theta_{\tilde Q}$ is self-adjoint exactly when the
parameter is **Hermitian up to a central phase**,

$$
\Theta_{\tilde Q}\ \text{self-adjoint}\iff\tilde Q^{*}=\omega\tilde Q\ \text{for some}\ \lvert\omega\rvert=1 ,
$$

equivalently when $\tilde Q=z\tilde H$ with $z\in\mathbb{C}^{\times}$ and $\tilde H$ Hermitian.

Every element of either sector satisfies the criterion, with $\omega=1$ on $\mathbb{M}_+$ and $\omega=-1$
on $\mathbb{M}_-$, so **every observable and every generator has a self-adjoint sandwich**. The
self-adjoint set is strictly larger than the two sectors: the phase multiple $e^{i\theta}(e_0+ie_3)$ is in
neither sector and still has a self-adjoint sandwich. The natural guess is wrong: **normality is not the
criterion**, and an element with $\Phi(\tilde Q)=\operatorname{diag}(1,i)$ is normal while its sandwich is
not self-adjoint.

**Proposition (no skew-adjoint sandwich).** There is no nonzero $\tilde Q$ with
$\Theta_{\tilde Q}=-\Theta_{\tilde Q^{*}}$.

**Proof.** Evaluating at $\tilde P=e_0$ and taking the trace,
$\mathrm{Tr}(\tilde Q\tilde Q^{*})=-\mathrm{Tr}(\tilde Q^{*}\tilde Q)$, that is
$2\lVert\tilde Q\rVert_E^{2}=-2\lVert\tilde Q\rVert_E^{2}$, whence $\tilde Q=0$. $\square$

The sandwich therefore occupies the self-adjoint side of the operator split and never the generator side.
That is the structural difference between the two operators, and the reason the sandwich can serve as an
action.

**Blindness.** The sandwich is insensitive to the sign and to the central phase of its parameter,
$\Theta_{-\tilde Q}=\Theta_{\tilde Q}$ and $\Theta_{e^{i\theta}\tilde Q}=\Theta_{\tilde Q}$ for every real
$\theta$, because the parameter appears once on each side. **Reading.** The central phase is not a
physical degree of freedom: no observable made of a sandwich can distinguish an element from its phase
multiple. This is the algebra's statement of global-phase invariance, and it is the same fact that makes
the unit-norm parameters $\pm\tilde\Lambda$ induce the same Lorentz transformation, the kernel of the
action being $\{\pm1\}$.

**Remark (verified).** The adjoint rule holds on $50$ random triples; the self-adjointness criterion
agrees with direct adjoint computation on $100$ of $100$ random elements, with no mismatch; the blindness
identities hold on $20$; $\mathrm{Tr}(\tilde Q\tilde Q^{*})+\mathrm{Tr}(\tilde Q^{*}\tilde Q)=4\lVert\tilde Q\rVert_E^{2}$ to $1.4\times10^{-14}$.

### The Kernel of the Action and the State as a Ray

The blindness is a statement about a **kernel**. Two parameters that differ by a central phase give the
same operator, $\Theta_{e^{i\theta}\tilde Q}=\Theta_{\tilde Q}$, so the kernel of the map from parameters
to operators contains the **central unitaries** $e^{i\theta}e_0$: a $U(1)$. The group that acts effectively
is the quotient of the compact slice by that centre,

$$
U(2)/U(1)\cong PU(2)\cong SO(3) ,
$$

the rotation group of the state's Bloch sphere. The object the action moves is therefore a **ray** and not
a vector: multiplying a state by a central phase is an unobservable gauge act, and only the ray is physical.
This is the algebraic origin of the state space being projective, and it is the same fact the corpus reads
as global-phase invariance; the states and the Bloch ball are *The States the Indefinite Metric Cannot
Normalise* and *The Bloch Ball as the Trace-One Slice of the Future Light Cone*.

## One Formula, Three Jobs

The sandwich is the anatomy of the framework's single action form,

$$
\Gamma_{\tilde A}(\tilde Q)=\tilde A\,\tilde Q\,\tilde A^{*} .
$$

Three classes of parameter act by it, and differ by a normalisation condition rather than by a change of
action.

| Parameter class | Condition | Induced transformation |
|---|---|---|
| Lorentz rotor | $\tilde\Lambda\tilde\Lambda^{\natural}=e_0$ | Lorentz transformation on $\mathbb{M}_-$ |
| unitary | $\tilde A\tilde A^{*}=e_0$ | unitary evolution on the module |
| Hermitian idempotent | $\tilde A^{2}=\tilde A=\tilde A^{*}$ | measurement update (projection) |

That one formula carries a Lorentz transformation, a reversible evolution and a projective measurement is
the framework's central structural observation. What the adjoint computation adds is the operator type:
all three are sandwiches, **none** is skew-adjoint, and the type is not shared but read off the parameter.
An idempotent parameter is Hermitian, so the measurement update is an orthogonal projection. A general
norm-one rotor (the $SL(2,\mathbb{C})$ element, $\tilde\Lambda\tilde\Lambda^{\natural}=e_0$) preserves
the interval form on $\mathbb{M}_-$ but is neither an algebra automorphism nor generally self-adjoint: a
general Lorentz transformation is an automorphism of the interval form and not a self-adjoint operator of
the positive form. The **choice** among the three classes is the physical input; the **form** is the
algebra's.

**Reading: the sandwich is a change of frame.** A map that sends every element to $\tilde R\tilde Q\tilde R^{-1}$ is a **change of bases** of the algebra, and the sandwich is that map with $\tilde R^{*}$ in place of $\tilde R^{-1}$ — for a unitary parameter the two agree. Reading the one map as a frame rotation, a gauge transformation or a Lorentz transformation is then a reading of the **parameter class** and not a change of structure: one map, three names, according to the normalisation of $\tilde R$. The three jobs of the previous table are three readings of one change of frame.

## One Product, Two Halves

The sesquilinear product is neither symmetric nor antisymmetric, and it splits into its two halves:

$$
\tilde P\star\tilde Q=\tilde P\circ\tilde Q+\tfrac12[\tilde P,\tilde Q]_\varsigma ,\qquad
\tilde P\circ\tilde Q=\tfrac12\bigl(\tilde P\star\tilde Q+\tilde Q\star\tilde P\bigr),\qquad
[\tilde P,\tilde Q]_\varsigma=\tilde P\star\tilde Q-\tilde Q\star\tilde P .
$$

**Proposition.** The **symmetrised** product $\tilde P\circ\tilde Q$ is Hermitian-valued on every pair,
and the **sesquilinear commutator** $[\tilde P,\tilde Q]_\varsigma$ is skew-Hermitian-valued on every
pair, with no restriction on the arguments.

**Proof.** $(\tilde P\tilde Q^{*})^{*}=\tilde Q\tilde P^{*}$ because ${}^{*}$ is an anti-automorphism that
is an involution, so the symmetrisation is fixed by ${}^{*}$ and the difference is anti-fixed. $\square$

| Product | Definition | Value | Sector |
|---|---|---|---|
| symmetrised | $\tilde P\circ\tilde Q=\tfrac12(\tilde P\tilde Q^{*}+\tilde Q\tilde P^{*})$ | Hermitian | $\mathbb{M}_+$ |
| sesquilinear commutator | $[\tilde P,\tilde Q]_\varsigma=\tilde P\tilde Q^{*}-\tilde Q\tilde P^{*}$ | skew-Hermitian | $\mathbb{M}_-$ |

Both are $\mathbb{R}$-bilinear and **not** $\mathbb{C}$-bilinear: for a complex $\lambda$ the identity
$(\lambda\tilde P)\circ\tilde Q=\lambda(\tilde P\circ\tilde Q)$ fails by exactly the imaginary part of
$\lambda$. The observable and generator structures are therefore **real** structures, over the fixed field
of the involution.

## The Observables Are the Hermitian Half, the Generators the Material Half

**Proposition (Jordan structure).** $\mathbb{M}_+$ is closed under $\circ$, and on $\mathbb{M}_+$ the
product satisfies the Jordan identity
$\tilde H\circ(\tilde K\circ\tilde H^{2})=(\tilde H\circ\tilde K)\circ\tilde H^{2}$, where
$\tilde H^{2}=\tilde H\circ\tilde H$ coincides with the ordinary square.

**Proposition (Lie structure).** $\mathbb{M}_-$ is closed under $[\cdot,\cdot]_\varsigma$, which is
antisymmetric and satisfies the Jacobi identity. On $\mathbb{M}_-$ the sesquilinear commutator is minus
the ordinary commutator, and minus a commutator is a commutator, so the Jacobi identity is inherited from
the associative product. The resulting four-dimensional real Lie algebra is that of the internal $U(2)$.

Each identity holds on its own sector and fails off it, and the failures have basis witnesses:

- the **Jordan identity fails off $\mathbb{M}_+$** at $\tilde P=\tilde Q=e_1$, where
  $e_1\circ e_1=e_1\star e_1=e_0$ and the identity's two sides differ by $-e_0$;
- the **Jacobi identity fails off $\mathbb{M}_-$** at $(e_0,e_1,e_2)$, where the cyclic sum is $4e_3$.

So the two structures are **half-algebras of one product**, not two independent algebras on the whole
space.

**Remark (verified).** The Jordan identity holds on $100$ random Hermitian pairs with maximum deviation
$2.8\times10^{-14}$; the Jacobi identity on $100$ random anti-Hermitian triples with maximum deviation
$7.1\times10^{-15}$; the two failure witnesses give $-e_0$ and $4e_3$ exactly.

**Reading.** The Hermitian sector, closed under the symmetrised product, is the algebra's **observable
half**; the material sector, closed under the commutator, is its **gauge half**. The split of one product
into a symmetric and an antisymmetric half is the exact algebraic statement of the split the framework
uses, and the Jacobi identity holding only on $\mathbb{M}_-$ is the algebraic reason the gauge structure
lives in the material sector.

**Speculation, labelled.** The antisymmetric half is a Lie algebra, and a Lie algebra is where vector
bosons are valued; it is tempting to propose that the vector bosons of the framework are carried by that
half. This is **speculation and not a result**: no propagation equation, polarisation count or coupling is
computed, and the corpus's gauge fields are built on $\mathbb{M}_-$ by the companion gauge articles,
with which the reading is consistent but which it does not derive.

## The Internal Action Is One-Sided

The algebra acts on itself, and the question is which action preserves its own canonical form.

**Proposition (right multiplication is an isometry).** Let $\tilde U$ be unitary,
$\tilde U\tilde U^{*}=e_0$. Then for all $\tilde P,\tilde R$,

$$
h(\tilde P\tilde U,\tilde R\tilde U)=\tilde P\tilde U\tilde U^{*}\tilde R^{*}=h(\tilde P,\tilde R) .
$$

**Proposition (left multiplication is not, unless central).** For unitary $\tilde U$,

$$
h(\tilde U\tilde P,\tilde U\tilde R)=\tilde U\,h(\tilde P,\tilde R)\,\tilde U^{*} ,
$$

the **conjugation** of the form's value; since the values span the algebra, this equals
$h(\tilde P,\tilde R)$ for all arguments exactly when $\tilde U$ is central, $\tilde U=\lambda e_0$ with
$\lvert\lambda\rvert=1$.

**Witness.** For $\tilde U=e_1$, $\tilde P=e_0$, $\tilde R=e_2$: $h(\tilde P,\tilde R)=-e_2$ while $h(\tilde U\tilde P,\tilde U\tilde R)=+e_2$, a change of $2e_2$.

**The scalar part is preserved by both.** $\mathrm{Sc}(\tilde U\tilde X\tilde U^{*})=\mathrm{Sc}(\tilde X)$
by the cyclicity of the scalar part and $\tilde U^{*}\tilde U=e_0$, so
$\langle\tilde U\tilde P,\tilde U\tilde R\rangle_{*}=\langle\tilde P,\tilde R\rangle_{*}$: if only the
scalar form is in use, left and right multiplications are both isometries. The one-sidedness is a theorem
about the **algebra-valued** form and about algebra-linearity, not about the scalar positive form. What
fails for the left action is the preservation of the element $h(\tilde P,\tilde R)$ — its direction and
its non-scalar components — and it is that preservation the canonical form is for.

**Remark (verified).** Right multiplication by $50$ random unitary elements preserves $h$ to machine
precision; left multiplication is an isometry exactly for the central unitary elements in the same check;
the scalar part is preserved by the left action to $5.1\times10^{-15}$; and the witness pair gives $-e_2$
and $+e_2$.

**Reading: chirality of the internal action.** The internal symmetry acts through the right action, because
only that one preserves the canonical form. Reading $h$ as a pairing that distinguishes a left from a
right slot, the one-sidedness says that the internal gauge action couples to one slot only — which may be
read as the algebraic shadow of a **chirality** in the internal coupling.

**Cautions.** The reading is a speculation about the structure of the form and not a claim about nature.

- **No parity violation of the weak interaction is claimed.** No left-handed coupling is exhibited, no
  chirality is fixed for any fermion, and the V$-$A structure of the weak interaction is not touched. A
  left-handed coupling would require a Lagrangian and a chirality projection that this article does not
  supply; the one-sidedness of the form is at best a necessary condition.
- **The asymmetry could be a convention.** With the mirrored form $h'(\tilde P,\tilde R)=\tilde P^{*}\tilde R$ the left action would be the isometry. The theorem is that the isometry is one-sided;
  which side is physical is the reading.
- The internal group so acting is the $U(2)$ of *Particle Types, Discrete Charge and Three-Particle Couplings* and *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not
  SU(3)*; the algebra reaches $SU(2)$ and not $SU(3)$.

### The One-Sidedness as Bra–Ket Asymmetry

The right-isometry theorem has a second reading beside the chirality. A pairing that distinguishes a left
slot from a right slot, and that one side's action alone preserves, is the algebraic shape of the
**bra–ket asymmetry**: the state is written in one slot and read from the other, and the internal action
moves only one of them. What the same theorem says about the two halves of the amplitude is that the
probability is a **singlet of the internal action** and the phase is **covariant**: the action leaves the
central number it measures unchanged and rotates the vector direction it does not measure — a statement
made twice in this band, here operatorial and in *Why Probability Values Are Central: the Symmetric
Sesquilinear Product and Its Cone* algebraically.

**Caution.** The one-sidedness is a theorem about the algebra-valued form $h$; the bra–ket, singlet and
covariant readings are readings of it, and no measurement rule is derived.

## The Limits

- The operator statements are statements about the algebra acting on itself, not about a physical Hilbert
  space.
- The observable/generator split is by the sector of the **parameter**, and the sandwich's type is read
  from the parameter as well; the two operators must not be given one type.
- The chirality reading is labelled speculation with the three cautions above, and nothing proved depends
  on it.
- The vector-boson reading of the antisymmetric half is labelled speculation.

## The Ledger

**Proved.** $(L_{\tilde B})^{\dagger}=L_{\tilde B^{*}}$ and $(R_{\tilde B})^{\dagger}=R_{\tilde B^{*}}$; self-adjoint operators from Hermitian parameters (observables), skew-adjoint from anti-Hermitian
ones (generators), with $L_{i\tilde H}=iL_{\tilde H}$. $\Theta_{\tilde Q}^{\dagger}=\Theta_{\tilde Q^{*}}$; $\Theta_{\tilde Q}$ self-adjoint iff $\tilde Q$ is Hermitian up to a central phase; no nonzero
skew-adjoint sandwich; $\Theta_{-\tilde Q}=\Theta_{e^{i\theta}\tilde Q}=\Theta_{\tilde Q}$. The product
splits into a Hermitian-valued symmetric half and a skew-Hermitian-valued commutator, both
$\mathbb{R}$-bilinear; $\mathbb{M}_+$ is a Jordan algebra under $\circ$ and $\mathbb{M}_-$ a Lie algebra
under $[\cdot,\cdot]_\varsigma$, each with its identity failing off its sector at the stated witnesses.
Right multiplication by a unitary is an isometry of $h$, left multiplication is one exactly for central
unitaries, and the scalar part is preserved by both.

**Readings.** Observables in the Hermitian half and gauge generators in the material half; the sandwich as
the one action form with three parameter classes, read as one change of frame; the state as a ray, with the
effective internal group $PU(2)\cong SO(3)$; the one-sidedness of the internal action as a chirality, and
also as a bra–ket asymmetry with the probability a singlet of the internal action and the phase covariant.

**Speculations, labelled.** Vector bosons carried by the antisymmetric half; the one-sidedness of the form
as a chirality of the internal coupling, with no parity violation claimed and with the convention caveat.

**Not claimed.** That the chirality reading is a physical result; that any weak-interaction structure is
derived; that a gauge vertex is computed.

## Physical Readings

The two one-sided operators read as the two kinds of acting element: an observable is Hermitian and an evolution is unitary, and the adjoint rule $\Theta_{\tilde Q}^{\dagger} = \Theta_{\tilde Q^{*}}$ is what makes the distinction algebraic. Read on the monoid, the reversible elements are the units and the projections are the non-invertible maps, so the chirality of the internal action is where the framework's direction of process begins (*The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*). Read on the split, the operators that preserve the sectors are the observable frame changes, which is the same statement the sandwich makes on the subspaces.

## Summary

The algebra's operator structure expresses the split of its sectors. Left multiplication by a Hermitian
element is self-adjoint and read as an **observable**; left multiplication by an anti-Hermitian element is
skew-adjoint and read as a **gauge generator**, exponentating to the internal unitary group. The two-sided
sandwich $\Theta_{\tilde Q}(\tilde P)=\tilde Q\tilde P\tilde Q^{*}$ is a different kind of operator: it is
self-adjoint exactly when the parameter is Hermitian up to a central phase — which every observable and
every generator satisfies, and which normality does **not** give — and it can never be skew-adjoint, so
the sandwich belongs to the observable kind and serves as the framework's single action form, carrying a
Lorentz transformation, a unitary evolution and a projective measurement according to the normalisation
of its parameter; it is blind to the sign and to the central phase of that parameter, so the central
unitaries act trivially, the effective internal group is $PU(2)\cong SO(3)$, and the state the action moves
is a **ray**. One product then
carries two half-algebras: its symmetrised half is Hermitian-valued, closed on the Hermitian sector and a
Jordan algebra there, while its antisymmetric half is skew-Hermitian-valued, closed on the material sector
and a Lie algebra there, so the observables live in $\mathbb{M}_+$ and the gauge generators in
$\mathbb{M}_-$; each identity fails off its own sector at a basis witness. Finally the internal symmetry
acts through **right** multiplication, since only the right action preserves the algebra-valued canonical
form $h(\tilde P,\tilde R)=\tilde P\tilde R^{*}$ — left multiplication conjugates the form's value and is
an isometry only for central unitaries, though both actions preserve the scalar part — and the
one-sidedness of the form is read, as a labelled speculation with explicit cautions, as a **chirality** of
the internal action, and beside it as a **bra–ket asymmetry** in which the probability is a singlet of the
internal action and the phase covariant. The positivity of the dagger is owned by *Mass, Rank and the Positivity of the
Dagger*; the compactness of the internal group by *Particle Types, Discrete Charge and Three-Particle Couplings*; the
adjoints and sandwiches by the mathematics articles *The Adjoints of the Regular Operators* and
*The Two-Sided Operators on a Hermitian Algebra*; and the Jordan and Lie
structures by *Jordan Algebras of Sesqualgebras*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\tilde B}$, $R_{\tilde B}$ | left and right multiplication by $\tilde B$ |
| $(L_{\tilde B})^{\dagger}=L_{\tilde B^{*}}$ | the adjoint rule; self-adjoint iff $\tilde B\in\mathbb{M}_+$ |
| $\Theta_{\tilde Q}(\tilde P)=\tilde Q\tilde P\tilde Q^{*}$ | the two-sided sandwich |
| $\Theta_{\tilde Q}^{\dagger}=\Theta_{\tilde Q^{*}}$ | the sandwich adjoint |
| $\tilde Q^{*}=\omega\tilde Q$ | the self-adjointness criterion, $\lvert\omega\rvert=1$ |
| $e^{i\theta}e_0$ in the kernel; $U(2)/U(1)\cong PU(2)\cong SO(3)$ | central-phase blindness; the state as a ray |
| $\Gamma_{\tilde A}(\tilde Q)=\tilde A\tilde Q\tilde A^{*}$ | the one action form |
| $\tilde P\circ\tilde Q$ | the symmetrised product; Hermitian-valued; Jordan on $\mathbb{M}_+$ |
| $[\tilde P,\tilde Q]_\varsigma$ | the sesquilinear commutator; skew-valued; Lie on $\mathbb{M}_-$ |
| $h(\tilde P,\tilde R)=\tilde P\tilde R^{*}$ | the algebra-valued canonical form |
| $\langle\tilde P,\tilde R\rangle_{*}=\mathrm{Sc}\,h$ | its scalar part, positive definite |
| $\mathbb{M}_\pm$ | the observable and the gauge halves |

## Further Reading

- *The Mathematical Study of Biquaternions*, the physics entry point to the mathematical study under
  which this block sits.
- Companion article *Mass, Rank and the Positivity of the Dagger*, for the positive form, the cone and the
  positivity.
- Companion article *Particle Types, Discrete Charge and Three-Particle Couplings*, for the internal $U(2)$, its compactness and the boosts.
- Companion article *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not
  SU(3)*, for why the internal group is $U(2)$ and not larger.
- Mathematics article *The Adjoints of the Regular Operators*
  (`articles_maths/the-adjoints-of-the-regular-operators.md`), for the one-sided adjoint rule.
- Mathematics article *The Two-Sided Operators on a Hermitian Algebra*
  (`articles_maths/the-two-sided-operators-on-a-hermitian-algebra.md`), for the
  sandwich, its Hermitian-up-to-phase criterion and the absence of a skew-adjoint sandwich.
- Mathematics article *Jordan Algebras of Sesqualgebras*
  (`articles_maths/jordan-algebras-of-sesqualgebras.md`), for the Jordan structure on the Hermitian
  sector and its failure off it.
- Mathematics article *Sesqualgebras* (`articles_maths/sesqualgebras.md`), for the general theory of the
  product and its involution.
- Companion article *Decoherence as Idempotent Projection*, for the idempotent parameter as a measurement.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for adjoints and Hermitian forms in
  a quaternion algebra.
