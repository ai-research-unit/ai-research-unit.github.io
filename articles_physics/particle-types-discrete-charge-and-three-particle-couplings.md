# __Particle Types, Discrete Charge and Three-Particle Couplings__

## Introduction

This article collects the particle-theoretic content of the operator structure: what kind of particle the
algebra's module carries, why the internal charge is discrete while rapidity is not, how fermion bilinears
rearrange over the four-element basis, and what the algebra says about three-particle couplings. The
answers are an application of one pattern. **Compactness gives discrete labels**: the internal symmetry
group is the compact $U(2)$, so its charges are quantised. **Non-compactness gives continuous parameters**:
the boosts form a non-compact family whose parameter is the rapidity, so there is no boost quantum. The
module is of **complex type**: the particle has a distinct antiparticle. The bilinears rearrange with the
algebra's own coefficient, $\tfrac12$ over the four-element basis and never $\tfrac14$; and the algebra's
natural three-linear object is its ternary product, which satisfies the Jordan triple identity, unlike the
ternary product of the fourth form.

The article keeps to the algebra. It defers the states to *The States the Indefinite Metric Cannot Normalise*; charge conjugation to *Charge Conjugation and the Division Ring: Charged, Neutral and Truly Neutral Particles in Biquaternionic Form*; the Majorana
and antilinear structures to *The Majorana Representation in Biquaternionic Form* and *Antilinear
Structure and the Two Kinds of Mass in Biquaternionic Form*; the Lorentz group to *The Lorentz Group in
Biquaternionic Form — Structure and Representations* and *The Two-Sheeted Cover and the Topology of Boosts
in Biquaternionic Form*; the group ceiling to *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)*; the spin ceiling to *Higher Spin
from Tensor Products: Why the Biquaternion Algebra Admits Only Spin 0 and One-Half*; and the mathematics
to the mathematics articles *Real Spinors and Reality Conditions on the Biquaternion Algebra with Hermitian Adjoint*, *The Sesquilinear
Associator and the Ternary Product* and *The Ternary Product and the Failure of the Jordan Triple
Identity*.

**Conventions.** As in the two companion articles of this block: $\mathbb{B}$ with basis
$e_0,e_1,e_2,e_3$, $e_k^{2}=-e_0$, $e_1e_2=e_3$; the sesquilinear product $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$; the sectors $\mathbb{M}_\pm$; the unitary slice
$U=\{\tilde U:\tilde U\tilde U^{*}=e_0\}$; $\Phi$ the $2\times2$ matrix model with
$\det\Phi(\tilde Q)=N(\tilde Q)$; and $\mathrm{Tr}=2\,\mathrm{Sc}$. Spinors live in $S=\mathbb{C}^{2}$
with a Clifford action $C$.

## What Kind of Particle: the Reality Condition

The particle type of a representation is decided by its **reality condition**: the existence and the square
of an antilinear map commuting with the Clifford action. Let $J(s)=X\bar s$ commute with $C$, that is
$J(C(a)s)=C(a)J(s)$ for all real generators $a$, equivalently $X\overline{c(a)}=c(a)X$.

| Type | Antilinear $J$ commuting with $C$ | Square | Particle type |
|---|---|---|---|
| real | exists | $J^{2}=+1$ | its own antiparticle (Majorana-like) |
| complex | does not exist | — | distinct antiparticle (Dirac-like) |
| quaternionic | exists | $J^{2}=-1$ | intermediate (pseudo-real) |

For a Clifford algebra $\mathrm{Cl}_{p,q}$ the type depends on the signature difference $p-q$ modulo
eight: real for $p-q\equiv0,1,2$, complex for $p-q\equiv3,7$, quaternionic for $p-q\equiv4,5,6$.

**The internal module is of complex type.** Take $\mathrm{Cl}_{3,0}$ with $c(\gamma_k)=\sigma_k$. The
volume element $\omega=\gamma_1\gamma_2\gamma_3$ has image $c(\omega)=\sigma_1\sigma_2\sigma_3=i\cdot1$,
central and of square $-1$: the complex structure of the module is **internal** to the Clifford action,
the scalar $i$ acting as the volume element. Consequently no reality structure exists. If $J(s)=X\bar s$
commuted with $C$, commuting with $\sigma_1$ would force $X$ into the span of $1,\sigma_1$, commuting with
$\sigma_3$ would force it into the span of $1,\sigma_3$, hence $X=\lambda 1$; and commuting with
$\sigma_2$ then gives $-\lambda\sigma_2=\lambda\sigma_2$, so $\lambda=0$.

**Reading (labelled).** A particle of the internal module is **Dirac-like**: it has a distinct
antiparticle, and its spinor and conjugate spinor are inequivalent. The conjugate module $\bar S$ — the
same space with the conjugate complex structure — is inequivalent to $S$ as a complex module, exactly
because no $J$ exists, while it is isomorphic to $S$ as a **real** representation, since the two differ
only by the sign of the complex structure. The pair $S,\bar S$ is read as the **particle–antiparticle
pair**, and charge conjugation as the algebraic passage from one to the other.

**Charge conjugation.** The passage is not the coefficient conjugation $\bar{\cdot}$, which is an
automorphism of the algebra. Charge conjugation is the conjugate-linear **pseudoautomorphism**
$\bar A=\Pi A^{*}\Pi^{-1}$ of the real Clifford algebra, with $\Pi\gamma_{\hat a}\Pi^{-1}=-\gamma_{\hat a}$,
and on the spinor module it is $C[\psi]=i\gamma^{2}\psi^{*}$. Its square $C^{2}=\pm1$ is the
division-ring invariant of the signature, and for the fundamental representation it is $+1$, so the
operation is of order two. Which of the three charge states a particle carries — **charged, neutral or
truly neutral** — is the division-ring trichotomy, and the one case in which a particle is its own
antiparticle is the **Majorana** condition on the doubled module $\Delta=S\oplus\bar S$; these are
*Charge Conjugation and the Division Ring: Charged, Neutral and Truly Neutral Particles in Biquaternionic Form* and *The Neutrino and Majorana
Fermions in Biquaternionic Form*.

**The three real forms on the same $\mathbb{C}^{2}$.** The trichotomy is concrete when three actions are
placed on one space.

| Real form | Generators | Type | Antilinear $J$ | $J^{2}$ |
|---|---|---|---|---|
| $\mathrm{Cl}_{3,0}$ | $c(\gamma_k)=\sigma_k$ | complex | none | — |
| $\mathrm{Cl}_{2,1}$ | $\sigma_1,\ \sigma_3,\ \sigma_1\sigma_3$ | real | $J=\bar{\cdot}$ | $+1$ |
| $\mathrm{Cl}_{0,3}$ | $c(e_k)=-i\sigma_k$ | quaternionic | $J(s)=\sigma_2\bar s$ | $-1$ |

For $\mathrm{Cl}_{2,1}$ the three generators are real with squares $(1,1,-1)$, so the signature is
$(2,1)$ and pointwise conjugation is a real structure; the representation is of **real type** and the
particle is read as Majorana-like. For $\mathrm{Cl}_{0,3}$ the generators square to $-1$ (signature
$(0,3)$), the map $J(s)=\sigma_2\bar s$ commutes with the action, and
$J^{2}=\sigma_2\overline{\sigma_2}=-\sigma_2^{2}=-1$, so $J$ is a **quaternionic structure**; together
with the module's own $i$ it closes the quaternion algebra, and the representation is of **quaternionic
type**.

**Speculation, labelled.** The type of a particle is its reality condition and the three types cannot
mix. Which type a neutrino would carry is therefore a fair question, and the framework's answer is:
**complex, for the internal module**, since a particle built on the internal module inherits its complex
type and Dirac-like behaviour. A Majorana neutrino would require a **different** module — the real form
$\mathrm{Cl}_{2,1}$ or the quaternionic form on $\mathrm{Cl}_{0,3}$ — and the framework does not select
one. **This is not a prediction**: which real form is physical for a given particle is not fixed by the
algebra alone, and the article does not perform the selection.

**Remark (verified).** The complex type of $\mathrm{Cl}_{3,0}$ by the minimal deviation of the commuting
condition over candidate matrices (bounded away from zero, minimum $1.41$); the volume element
$\sigma_1\sigma_2\sigma_3=i\cdot1$ exactly; and the real and quaternionic structures commuting with
$J^{2}=+1$ and $J^{2}=-1$ respectively.

## The Compact Slice: Discrete Charge

**Definition.** The **unitary slice** is $U=\{\tilde U\in\mathbb{B}:\tilde U\tilde U^{*}=e_0\}$. Under
$\Phi$ it is $U(2)$, a group of real dimension $4$, and it lies in the Euclidean unit sphere $S^{7}$,
strictly: the sphere has dimension $7$ and is not a group, while the slice has dimension $4$ and is.

Its determinant-one part is $SU(2)$, the three-dimensional double cover of the rotations and the unit
sphere of the quaternions, and the whole slice is the central product
$U\cong\bigl(SU(2)\times U(1)\bigr)/\mathbb{Z}_2$, the $U(1)$ the central unitaries $e^{i\theta}e_0$ and
the identification the two elements $\pm e_0$.

**Proposition (compactness).** The slice is compact.

**Proof.** $U$ is the group of isometries of the positive definite form that the algebra's own left
multiplications supply, $U=\{\tilde U:\lVert\tilde U\tilde Q\rVert_E=\lVert\tilde Q\rVert_E\ \forall\tilde Q\}$; its defining condition is polynomial and so closed, and it lies in the unit sphere and so is
bounded. Closed and bounded in $\mathbb{R}^{8}$ is compact. Positivity of the dagger is what supplies the
boundedness. $\square$

**Reading: discrete charge.** The finite-dimensional unitary representations of a compact group are
labelled by discrete data, so the **internal charge** — the label of a representation of the internal
group — is **quantised**, with no continuous deformation available. The internal group of the algebra is
exactly $U(2)$, whose irreducible labels are discrete; that is the algebraic origin of charge
quantisation in the framework, and the group ceiling of *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)* fixes it to $U(2)$ and
no larger.

## The Non-Compact Boost: Continuous Rapidity

The units of the algebra — the invertible elements, the complement of the zero-divisor cone — form the
non-compact $GL_2(\mathbb{C})$, of real dimension $8$. Inside them sits the compact slice of Euclidean-unit
elements, and the remaining directions are the **boosts**. A boost along a unit imaginary direction
$\hat n$ is

$$
\tilde B(\varphi)=e^{\varphi\, i\hat n}=\cosh\varphi\, e_0+\sinh\varphi\, i\hat n ,
$$

Hermitian, with hyperbolic exponential because $(i\hat n)^{2}=+1$. Its **Euclidean** norm grows without
bound while its biquaternion norm stays fixed:

$$
\lVert\tilde B(\varphi)\rVert_E^{2}=\cosh^{2}\varphi+\sinh^{2}\varphi=\cosh 2\varphi,\qquad
N\bigl(\tilde B(\varphi)\bigr)=\cosh^{2}\varphi-\sinh^{2}\varphi=1 .
$$

The parameter $\varphi$ is the **rapidity** and ranges over the whole real line. The family is therefore
**non-compact**: no boost is unitary except the identity.

The two families fit together in the polar, or **Cartan**, decomposition of the units,

$$
GL_2(\mathbb{C})=U\cdot\exp(\mathbb{M}_+)=\{\tilde U\tilde B:\tilde U\in U,\ \tilde B=e^{\tilde
H},\ \tilde H\in\mathbb{M}_+\},
$$

every invertible element uniquely a unitary slice element times a positive definite Hermitian one. The
slice is a group and the boosts are not: the product of two positive definite Hermitian elements is
Hermitian exactly when they commute.

**Reading (labelled).** The compact slice is the internal symmetry group and the non-compact boosts are
the kinematic boosts. Compactness gives discrete labels — **charge quantisation**, no continuous charge
deformation. Non-compactness gives the continuous **rapidity** $\varphi\in\mathbb{R}$: there is no
smallest rapidity and no lattice of rapidities, hence **no boost quantum**, and no particle is carried by
a boost, since a boost moves states without creating quantum numbers.

**The contrast with the Lorentz group.** The same element acts on the material sector as a Lorentz
transformation, and there the isometry group is the non-compact $SO^{+}(1,3)$, not a compact group. The
difference is the form: the positive form of the informational sector gives the compact $U(2)$, the
indefinite interval form of the material sector the non-compact Lorentz group. The two sit in one algebra
and are separated by the sign of the form.

**Remark (verified).** At $\varphi=0.5,2,5$ the Euclidean square is $1.543,27.31,11013$ while
$N(\tilde B)=1$ in every case, matching $\cosh2\varphi$.

## Bilinears and Their Rearrangement

**The four-element basis.** For spinors $s,t\in S$ the outer product $M=st^{\dagger}$ is a $2\times2$
matrix, hence an element of the algebra through $\Phi^{-1}$, expanded as
$M=\sum_\mu c_\mu e_\mu$ with $c_\mu=\tfrac12\mathrm{Tr}(E_\mu^{\dagger}M)$, the factor being the inverse
of $\mathrm{Tr}(E_\mu^{\dagger}E_\nu)=2\delta_{\mu\nu}$. The four $c_\mu$ are the **bilinear components**
of the pair. In the Dirac reading the same construction with the sixteen gamma matrices gives sixteen
components; the counts, four per biquaternion pair against sixteen per Dirac pair, are the whole reason
the rearrangement coefficients differ between the two bases.

The **five types** of Dirac bilinear are scalar, vector, tensor, axial and pseudoscalar, with $1,4,6,4,1$
components summing to the sixteen of the Dirac algebra. The bigeneral quaternionic bilinears sit inside that
classification.

**The module and its inner product.** The spinors $s,t$ above live in the minimal left ideal
$S=\mathbb{B}\tilde\Pi_1=\mathbb{C}\{\tilde\Pi_1,\tilde T\}$, the defining module of
$\mathbb{B}\cong M_2(\mathbb{C})$, with $\tilde\Pi_1=\tfrac12(e_0+ie_3)$ and
$\tilde T=\tfrac12(ie_1+e_2)$. Its spinor inner product is the restriction of the Born pairing of
*Mass, Rank and the Positivity of the Dagger*, and in the basis $\{\tilde\Pi_1,\tilde T\}$ its Gram
matrix is

$$
\begin{pmatrix}
\langle\tilde\Pi_1,\tilde\Pi_1\rangle_{*} & \langle\tilde T,\tilde\Pi_1\rangle_{*}\\
\langle\tilde\Pi_1,\tilde T\rangle_{*} & \langle\tilde T,\tilde T\rangle_{*}
\end{pmatrix}
=\tfrac12 I_2 .
$$

It is **positive definite**, so the module is a genuine two-dimensional Hilbert space. The basis is
**one idempotent and one nilpotent** — $\tilde\Pi_1^{2}=\tilde\Pi_1$ while $\tilde T^{2}=0$, and
$\tilde T^{*}=\tfrac12(ie_1-e_2)\neq\tilde T$ — so $\tilde T$ is not a state; a spinor is the pair
$(s_1,s_2)$ of coefficients in $\psi=s_1\tilde\Pi_1+s_2\tilde T$, and
$\langle\psi,\psi\rangle_{*}=\tfrac12(\lvert s_1\rvert^{2}+\lvert s_2\rvert^{2})$, so the two spin
states are carried by the two **coefficients** and not by the two basis elements. The positivity is
**inherited** rather than built: the scalar form of the dagger is positive definite on the whole algebra,
$\mathrm{Sc}(\tilde R^{*}\tilde R)=\sum_\mu\lvert R_\mu\rvert^{2}$, so every subspace inherits a positive
definite restriction. Two facts of the algebra then make the basis well behaved, one line each: the
idempotent is self-adjoint, $\tilde\Pi_1^{*}=\tilde\Pi_1$, and $\tilde T^{*}\tilde T=\tilde\Pi_1$. In a
general Clifford algebra the same restriction can be **totally isotropic** — the idempotent
$\pi=\tfrac12(1+e_1)$ of $\mathrm{Cl}_{1,1}(\mathbb{R})$ has $\pi^{\dagger}\pi=0$ — and the reason there
is that the ambient form is indefinite, $a^{2}-b^{2}$ on $a+be$, with both idempotents on the null line
$a=b$. That failure has no instance in $\mathbb{B}$. The module, its form and the contrast are
*Hermitian Modules over the Biquaternion Algebra with Hermitian Adjoint*.

**The completeness relation.** The identity behind every rearrangement is the completeness of the basis in
$\mathrm{End}(S)$:

$$
\sum_{\mu=0}^{3}\tfrac12\,e_\mu\,\tilde X\,e_\mu^{*}=\mathrm{Tr}\bigl(\Phi(\tilde X)\bigr)e_0
\qquad\text{for all }\tilde X ,
$$

equivalently $\sum_\mu\tfrac12 E_\mu XE_\mu^{\dagger}=\mathrm{Tr}(X)I$ in matrix form. Two corollaries
are the working form: for spinors $s,t,u,v$,

$$
(st^{\dagger})(uv^{\dagger})=(t^{\dagger}u)(sv^{\dagger}),
$$

with coefficient $1$ — the product of two bilinears collapses with no sum, the scalar $t^{\dagger}u$ being
the inner product of $t$ and $u$; and the completeness sum above, with coefficient $\tfrac12$ because the
basis is unnormalised.

**The corpus's finding.** Over the four-element quaternion basis the coefficient is $1$ or $\tfrac12$,
**never $\tfrac14$**. The textbook $\tfrac14$ belongs to the sixteen-element Dirac basis, where the
generators are normalised so that $\mathrm{Tr}(\Gamma^A\Gamma_B)=4\delta^A_B$; confusing the two bases is
the standard error this section exists to prevent.

**The six classes (Lounesto).** The sixteen Dirac bilinears are not independent. They satisfy the
**Fierz–Kofink identities**, of which the three scalar ones are

$$
J^{2}=\sigma^{2}+\omega^{2},\qquad J^{2}=-K^{2},\qquad J\cdot K=0 ,
$$

and these identities constrain the covariants so tightly that a nonzero spinor with $J\neq0$ has only
**six** possible configurations: three **regular**, with $\sigma$ or $\omega$ nonzero, and three
**singular**, with $\sigma=\omega=0$, separated by the vanishing or non-vanishing of the axial vector $K$
and of the tensor $S$.

| class | condition | name |
|---|---|---|
| $1$ | $\sigma\neq0$, $\omega\neq0$ | Dirac |
| $2$ | $\sigma\neq0$, $\omega=0$ | regular, purely scalar |
| $3$ | $\sigma=0$, $\omega\neq0$ | regular, purely pseudoscalar |
| $4$ | $K\neq0$, $S\neq0$ | flag-dipole |
| $5$ | $K=0$, $S\neq0$ | flagpole |
| $6$ | $K\neq0$, $S=0$ | dipole |

The names *flagpole* and *dipole* are exchanged in some of the literature, so the conditions are the safe
identifier; the vector $J$ is null in the three singular classes, by $J^{2}=\sigma^{2}+\omega^{2}$. The
**flag-dipole** is the type that the usual list of Dirac, real and chiral spinors does not exhaust. Two
limits belong with the table: a general element of $\mathbb{B}$ is class $1$, and the corpus's
two-component spinors are **not** in the six classes as written, because the classification applies to
the four-component recombination. The identities, the proof that all six classes are non-empty, and the
Fierz aggregate $Z=\sigma+J+iS+K\gamma_5-i\omega\gamma_5$ with $Z^{2}=4\sigma Z$ from which the spinor is
recovered — the aggregate and the inversion **quoted from the literature**, not recomputed in the corpus —
are *The Fierz–Kofink Identities and the Classification of Spinors*.

**The physical reading (labelled).** In a scattering amplitude a bilinear at one vertex and a bilinear at
another can be contracted with the spinors adjacent — an $s$-channel pairing — or crossed — a
$t$-channel pairing. The rearrangement identity says the two pairings describe the **same exchange**, the
coefficient being fixed by the algebra rather than chosen. A biquaternion-model exchange is rearranged
with coefficient $1$ or $\tfrac12$; a Dirac-model computation must use the sixteen-element basis and
$\tfrac14$.

**Remark (verified).** The completeness sum with coefficient $\tfrac12$ reproduces
$\mathrm{Tr}(\Phi(\tilde X))e_0$ exactly over $100$ random elements, while replacing $\tfrac12$ by
$\tfrac14$ leaves a deviation of order unity; the bilinear-product identity holds on $100$ random
quadruples; and $e_1\star e_2=-e_3$, $e_2\star e_1=+e_3$, $e_1\star e_1=e_0$.

## Three-Particle Couplings: the Ternary Product

**Non-associativity is forced.** The sesquilinear product is not associative:
$(e_0\star e_1)\star e_1=-e_0$ while $e_0\star(e_1\star e_1)=e_0$, so the associator on the triple
$(e_0,e_1,e_1)$ is $-2e_0\neq0$. The failure is not an accident of the example: the collapse theorem of
the mathematics article *Sesqualgebras* shows that an associative or commutative such operation would
force the involution to be trivial. The product is also non-commutative, with $e_1\star e_2=-e_3$ against
$e_2\star e_1=+e_3$.

**The associator.** The **sesquilinear associator** is $[\tilde P,\tilde Q,\tilde R]_\varsigma=(\tilde P\star\tilde Q)\star\tilde R-\tilde P\star(\tilde Q\star\tilde R)$. It is additive
in each argument, of **mixed parity** in the third slot (the two groupings differ there in their
semilinearity), and it measures the algebra's own non-associativity: its nonzero values are the
obstruction to freely re-bracketing a triple.

**The ternary product.** A three-slot product cannot be read as an iterated two-slot product, so one is
named:

$$
\{\tilde P,\tilde Q,\tilde R\}=(\tilde P\star\tilde Q)\star\tilde R^{*}=\tilde P\tilde Q^{*}\tilde R .
$$

It is additive in each slot, $\mathbb{C}$-linear in the outer two and semilinear in the middle — the
triple product of an algebraic $J^{*}$-algebra — and it contains the binary product and the involution as
its shadows, $\{\tilde P,\tilde R,e_0\}=\tilde P\tilde R^{*}$ and
$\{e_0,\tilde Q,e_0\}=\tilde Q^{*}$.

**The ternary product is the state pairing at three entries.** The binary product the ternary object
extends is the sesquilinear product $\tilde P\tilde Q^{*}$ of the probability pairing, so the three-slot
product is the same pairing read on three amplitudes: the two-field coupling and the three-field coupling
are **one operation at two arities**, and no new product is introduced for the triple.

**The Jordan triple identity.** The identity that qualifies such a product is

$$
\{\tilde P,\tilde Q,\{\tilde U,\tilde V,\tilde R\}\}
-\{\{\tilde P,\tilde Q,\tilde U\},\tilde V,\tilde R\}
+\{\tilde U,\{\tilde Q,\tilde P,\tilde V\},\tilde R\}
-\{\tilde U,\tilde V,\{\tilde P,\tilde Q,\tilde R\}\}=0 ,
$$

and the general plain sesquilinear ternary product **satisfies it**.

**The fourth form fails.** The **general quaternionic sesquilinear product**
$\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q^{*}$ has a ternary product of the same formal shape,
and it **fails**: on the five-tuple $(e_0,e_1,e_0,e_2,e_0)$ the two sides of the identity are
$e_3$ and $-3e_3$. The failure is not a small-set accident — $480$ of the $1024$ five-tuples of the four real quaternion units are
witnesses. For the physics this is a caution: which ternary product an algebra carries is decided by the
involution that defines the product, and a change of involution can turn a coherent triple into an
incoherent one.

**The reading: three-particle couplings (speculation, labelled).** A coupling of three particles is a
three-linear object, and the algebra's natural three-linear object is its ternary product. It is then
tempting to propose that the **associator is the obstruction to a naive three-particle coupling** — a
naive coupling written as an iterated binary product is not well defined where the associator is nonzero —
that the **ternary product is the repair**, giving the coupling as a single three-linear object, and that
the **Jordan triple identity is the coherence condition** the repair must meet, so that the identity
selects which three-particle vertices an algebra admits. Bilinear couplings are assembled without
ambiguity; ternary ones require the ternary product, and that shift is the content of the algebra's
non-associativity. In this reading the **associator is the order dependence of a three-field coupling**:
its value on a triple is the amount by which the outcome changes when the triple is re-bracketed, so a
nonzero associator is exactly the statement that a three-field coupling is order-dependent and cannot be
written as an iteration of two-field ones.

**Caution.** No gauge-theory vertex is claimed. In particular the **three-gluon vertex is not derived**
here or elsewhere: a gauge-theory vertex requires a Lagrangian, a representation and a computation of
structure constants, and none is performed. What is offered is a structural analogy, labelled
speculation.

**Open questions.** Which ternary couplings, if any, the framework's other articles require, and whether
they use this ternary product; whether the associator's values can be read as something other than an
obstruction; whether the quaternionic product's failure excludes any physical triple, and if so which;
and whether any gauge vertex can be obtained from the ternary structure without additional input.

**Remark (verified).** The associator on $(e_0,e_1,e_1)$ is $-2e_0$; $\{e_1,e_2,e_3\}=e_0$ and
$\{e_1,e_2,e_1\}=-e_2$; the Jordan triple identity holds for the sesquilinear ternary product on $100$
random five-tuples with maximum deviation $2.7\times10^{-13}$, and no basis five-tuple violates it; the
general quaternionic sesquilinear ternary product violates it on $480$ of the $1024$ five-tuples of the four
real quaternion units, the
witness $(e_0,e_1,e_0,e_2,e_0)$ giving $e_3$ and $-3e_3$.

## The Limits

- The particle vocabulary — Dirac-like, Majorana-like, neutrino — is the framework's reading, labelled;
  the algebra supplies the trichotomy, not the assignment.
- The charge quantisation is a statement about the representations of the compact internal group; it is
  not a derivation of the observed charge spectrum.
- The Fierz discussion is about rearrangement coefficients over a chosen basis, not about the size of any
  amplitude.
- The three-particle coupling section is speculation from beginning to end, with the three-gluon vertex
  explicitly excluded.

## The Ledger

**Proved.** The reality-condition trichotomy and the modulo-eight signature rule; the complex type of
$\mathrm{Cl}_{3,0}$ by the volume-element argument, with $\sigma_1\sigma_2\sigma_3=i\cdot1$; the real and
quaternionic types of $\mathrm{Cl}_{2,1}$ and $\mathrm{Cl}_{0,3}$ with $J^{2}=+1$ and $J^{2}=-1$; the
inequivalence of $S$ and $\bar S$ as complex modules. The unitary slice is $U(2)$, of dimension $4$,
inside $S^{7}$, with $SU(2)$ as its determinant-one part and the central-product decomposition; it is
compact by positivity of the dagger. The boosts have $N=1$ and $\lVert\tilde B(\varphi)\rVert_E^{2}=\cosh 2\varphi$, and the units decompose as $U\cdot\exp(\mathbb{M}_+)$. The completeness relation with
coefficient $\tfrac12$ and the bilinear-product identity with coefficient $1$; the coefficient is never
$\tfrac14$ over the four-element basis. Non-associativity with the witness $-2e_0$; the ternary product
$\{\tilde P,\tilde Q,\tilde R\}=\tilde P\tilde Q^{*}\tilde R$ and its shadows; the Jordan triple identity
for it, and its failure for the general quaternionic sesquilinear product on $480$ of $1024$ five-tuples of the four real quaternion units.

**Readings.** Dirac-like particles with distinct antiparticles; charge quantisation from compactness and
continuous rapidity from non-compactness; the $s$-channel/$t$-channel exchange; the ternary product as a
three-particle coupling, and as the state pairing at three entries; the associator as the order dependence
of a three-field coupling.

**Speculations, labelled.** The neutrino's type; the three-particle coupling dictionary, with the
three-gluon vertex explicitly not derived.

**Not claimed.** That a reality type is assigned to any observed particle; that a mass or charge spectrum
is derived; that any gauge vertex is computed.

## Physical Readings

The reality-condition trichotomy reads as a particle taxonomy: a spinor whose reality condition holds for no coefficient, for the central one only and for the whole real part are three physical species, and the algebra rather than an external label fixes the types. The ternary couplings read as the gauge side: a three-particle vertex is a ternary product of the gauge structure, which is why the couplings of the framework are not the structure constants of a Lie algebra but the values of a product. Read on the states, the trichotomy is also the boundary of the state space, since only the elements that meet the reality condition of the whole real part carry states.

## Summary

The particle content of the operator structure follows one pattern. The algebra's module carries a
**reality condition**, and the internal module is of **complex type** — the volume element of
$\mathrm{Cl}_{3,0}$ is $i\cdot1$ and no commuting antilinear map exists — so its particle is Dirac-like
with a distinct antiparticle, housed in the conjugate module $S\mapsto\bar S$, with charge conjugation
the conjugate-linear pseudoautomorphism $C[\psi]=i\gamma^{2}\psi^{*}$ of order two; the real and
quaternionic types exist on the same $\mathbb{C}^{2}$ for other real forms, and which type a given
particle carries is a labelled speculation. The spinors are elements of the minimal left ideal
$S=\mathbb{B}\tilde\Pi_1=\mathbb{C}\{\tilde\Pi_1,\tilde T\}$, whose inner product is positive definite
with Gram matrix $\tfrac12 I_2$. The internal symmetry is the **compact** slice
$U\cong(SU(2)\times U(1))/\mathbb{Z}_2$,
compact because the dagger is positive, and compactness is read as **discrete charge**; the **boosts** are
non-compact, with $N=1$, $\lVert\tilde B\rVert_E^{2}=\cosh2\varphi$ and rapidity $\varphi\in\mathbb{R}$,
and non-compactness is read as **continuous rapidity with no boost quantum**, the units decomposing as
$U\cdot\exp(\mathbb{M}_+)$. Fermion bilinears over the four-element basis rearrange with coefficient $1$
or $\tfrac12$ — the completeness relation gives $\mathrm{Tr}(\Phi(\tilde X))e_0$, and the textbook
$\tfrac14$ belongs to the sixteen-element Dirac basis — which is read as the identity of the
$s$-channel and $t$-channel exchanges. The four bilinears of the module sit inside the sixteen Dirac
covariants, whose **Fierz–Kofink identities** force exactly **six classes**, three regular and three
singular, the flag-dipole being the type the usual list of Dirac, real and chiral spinors does not
exhaust. Finally the algebra's non-associativity, with witness $-2e_0$,
forces a **ternary product** $\{\tilde P,\tilde Q,\tilde R\}=\tilde P\tilde Q^{*}\tilde R$, which
satisfies the Jordan triple identity while the fourth form's ternary product fails it on $480$ of $1024$
five-tuples of the four real quaternion units; the ternary product is read, as a labelled speculation that excludes the three-gluon
vertex, as the algebra's natural **three-particle coupling** — the state pairing read at three entries,
with the associator as the order dependence of a three-field coupling. The states are owned by *The States the
Indefinite Metric Cannot Normalise*; the charge-state trichotomy and the Majorana condition by *Charge Conjugation and the Division Ring: Charged, Neutral and Truly Neutral Particles in Biquaternionic Form*
and *The Neutrino and Majorana Fermions in Biquaternionic Form*; the Lorentz group by
*The Lorentz Group in Biquaternionic Form — Structure and Representations* and *The Two-Sheeted Cover and the Topology of Boosts in Biquaternionic Form*; the
group ceiling by *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)*; the spin ceiling by *Higher Spin from Tensor Products: Why the Biquaternion Algebra Admits Only Spin 0 and One-Half*; and
the operator structure on which all of this rests by the companion articles *Mass, Rank and the
Positivity of the Dagger* and *Observables, Gauge Generators and the Chirality of the Internal Action*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $U=\{\tilde U:\tilde U\tilde U^{*}=e_0\}\cong U(2)$ | the unitary slice; compact; inside $S^{7}$ |
| $SU$ | its determinant-one part, $SU(2)$ |
| $\tilde B(\varphi)=e^{\varphi i\hat n}$ | a boost; Hermitian, $N=1$, $\lVert\tilde B\rVert_E^{2}=\cosh2\varphi$ |
| $\varphi$ | the rapidity; $\varphi\in\mathbb{R}$, no quantum |
| $GL_2(\mathbb{C})=U\cdot\exp(\mathbb{M}_+)$ | the Cartan decomposition of the units |
| $J(s)=X\bar s$ | the antilinear reality structure, $J^{2}=\pm1$ |
| $\bar S$ | the conjugate module; the antiparticle space |
| $\sum_\mu\tfrac12 e_\mu\tilde X e_\mu^{*}=\mathrm{Tr}(\Phi(\tilde X))e_0$ | the Fierz–Kofink completeness relation |
| $S=\mathbb{B}\tilde\Pi_1=\mathbb{C}\{\tilde\Pi_1,\tilde T\}$, $G=\tfrac12 I_2$ | the spinor module and its positive definite inner product |
| $\sigma,\omega,J,K,S$; six classes | the Dirac covariants and Lounesto's six classes |
| $\{\tilde P,\tilde Q,\tilde R\}=\tilde P\tilde Q^{*}\tilde R$ | the ternary product |
| $[\tilde P,\tilde Q,\tilde R]_\varsigma$ | the sesquilinear associator |
| $\mathbb{M}_\pm$ | the informational and material sectors |

## Further Reading

- *The Mathematical Study of Biquaternions*, the physics entry point to the mathematical study under
  which this block sits.
- Companion articles *Mass, Rank and the Positivity of the Dagger* and *Observables, Gauge Generators and
  the Chirality of the Internal Action*, the other two articles of this block.
- Companion article *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)*,
  for the internal group.
- Companion article *Higher Spin from Tensor Products: Why the Biquaternion Algebra Admits Only Spin 0 and
  One-Half*, for the spin ceiling.
- Companion articles *Charge Conjugation and the Division Ring: Charged, Neutral and Truly Neutral Particles in Biquaternionic Form*, *The Majorana Representation in
  Biquaternionic Form* and *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*, for
  the particle and antiparticle structures.
- Companion articles *The Lorentz Group in Biquaternionic Form — Structure and Representations* and *The
  Two-Sheeted Cover and the Topology of Boosts in Biquaternionic Form*, for the Lorentz side.
- Mathematics article *Real Spinors and Reality Conditions on the Biquaternion Algebra with Hermitian
  Adjoint*
  (`articles_maths/real-spinors-and-reality-conditions-on-the-biquaternion-algebra-with-hermitian-adjoint.md`)
  and *Hermitian Modules over the Biquaternion Algebra with Hermitian Adjoint*
  (`articles_maths/hermitian-modules-over-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the
  trichotomy and for the internal module $S\cong\mathbb{C}^{2}$.
- Mathematics article *The Sesquilinear Associator and the Ternary Product*
  (`articles_maths/the-sesquilinear-associator-and-the-ternary-product.md`) and *The Ternary Product and
  the Failure of the Jordan Triple Identity*
  (`articles_maths/the-ternary-product-and-the-failure-of-the-jordan-triple-identity.md`), for the
  ternary structures.
- Mathematics article *Sesqualgebras* (`articles_maths/sesqualgebras.md`), for the collapse theorem
  that forces non-associativity.
- Mathematics article *The Fierz–Kofink Identities and the Classification of Spinors*
  (`articles_maths/the-fierz-kofink-identities-and-the-classification-of-spinors.md`), for the
  four-dimensional FPK identities and the six classes.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for Clifford modules and their real
  forms.
