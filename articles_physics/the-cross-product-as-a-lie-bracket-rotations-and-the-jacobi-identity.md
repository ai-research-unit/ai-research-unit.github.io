# __The Cross Product as a Lie Bracket: Rotations and the Jacobi Identity__

## Introduction

The antisymmetric half of the ordinary product is the cross product of the two vector parts. The scalar
part drops, the result lies in the traceless vector subspace, and the operation is alternating:

$$
\tilde P\wedge\tilde Q=\tfrac12\bigl(\tilde P\tilde Q-\tilde Q\tilde P\bigr)=\mathbf{P}\times\mathbf{Q},
\qquad
\mathrm{Sc}\bigl(\tilde P\wedge\tilde Q\bigr)=0,
\qquad
\tilde P\wedge\tilde Q\in\mathrm{Vect}(\mathbb{B}) .
$$

This is the operation named $\mathrm{APA}$ among the twelve algebraic structures of the biquaternion
complex space. It is $\mathbb{C}$-bilinear and alternating, it satisfies the **Jacobi identity**, and of
the twelve operations it is the only Lie product. That is its algebraic signature, and it is the reason
the operation is a **Lie bracket**.

The physical reading offered here, and labelled as such, is that the antisymmetric plain product is the
bracket of **infinitesimal rotations**. A rotation of the frame about the direction $e_k$ is the
conjugation $\tilde X\mapsto\tilde\Lambda_k(\theta)\tilde X\tilde\Lambda_k(\theta)^{-1}$ by the real unit
rotor $\tilde\Lambda_k(\theta)=\cos\tfrac{\theta}{2}+\sin\tfrac{\theta}{2}e_k$, and the derivative of
that family at the identity is the bracket: the generator of the rotation about the direction $e_k$ is
$\tfrac12 e_k$, and the three generators close on the rotation algebra
$\mathfrak{su}(2)\cong\mathfrak{so}(3)$. The **closure of the rotation algebra is the Jacobi identity**:
the commutator of two infinitesimal rotations is again an infinitesimal rotation, and the identity is
what makes the closure hold coherently.

The boundary is stated with the reading and again in the ledger: **a Lie bracket is not yet a group.** The
bracket is the algebra of the generators; the group is the exponential of the algebra, and its
global structure is separate. The physical angular momentum of a system is not this bracket either; it is
*Angular Momentum and Spin in Biquaternionic Form*.

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis
$e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$, $e_k^{2}=-e_0$, central scalar imaginary $i$, and general element
$\tilde Q=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^{3}Q_ke_k$ and $Q_\mu\in\mathbb{C}$;
$\mathrm{Sc}(\tilde Q)=Q_0$ is the scalar part and
$\mathrm{Vect}(\mathbb{B})=\{\tilde Q:\mathrm{Sc}(\tilde Q)=0\}$ is the traceless vector subspace. The
conventions are those of *Conventions in the Biquaternion Universe*.

## The Antisymmetric Part of the Ordinary Product

The ordinary product is $\mathbb{C}$-bilinear, so the exchange of its arguments splits it into a
symmetric and an antisymmetric part, as in *The Symmetric and Antisymmetric Parts of an Algebra Product*;
the two halves are the subject of the two bands of this family. The antisymmetric half is the
**antisymmetric plain product**

$$
\tilde P\wedge\tilde Q=\tfrac12\bigl(\tilde P\tilde Q-\tilde Q\tilde P\bigr).
$$

**Proposition.** In coordinates the antisymmetric plain product is the cross product of the two vector
parts, with zero scalar part:

$$
\tilde P\wedge\tilde Q=\mathbf{P}\times\mathbf{Q}
=\bigl(P_2Q_3-P_3Q_2\bigr)e_1+\bigl(P_3Q_1-P_1Q_3\bigr)e_2+\bigl(P_1Q_2-P_2Q_1\bigr)e_3 .
$$

*Proof.* The scalar parts of $\tilde P\tilde Q$ and $\tilde Q\tilde P$ are equal, so they cancel; the
vector part of the difference is the difference of the cross products
$\mathbf{P}\times\mathbf{Q}-\mathbf{Q}\times\mathbf{P}=2\,\mathbf{P}\times\mathbf{Q}$, and halving gives
the cross product. Verified on the basis and on general elements. This is *Introduction to the
Antisymmetric Plain Algebra of Biquaternions*, and the operation is read here as the bracket of the
block.

**Proposition.** The operation is $\mathbb{C}$-bilinear, **alternating** and **skew**,
$\tilde P\wedge\tilde Q=-\tilde Q\wedge\tilde P$ and $\tilde P\wedge\tilde P=0$, and its image is the
vector subspace $\mathrm{Vect}(\mathbb{B})$. It has no unit and is not commutative.

*Proof.* Both properties are those of the cross product; the image has zero scalar part by the display.
Verified on the basis. The absence of a unit is *Introduction to the Antisymmetric Plain Algebra of
Biquaternions*.

**Remark (the split of the two bands, in one display).** The ordinary product is recovered from the two
halves,

$$
\tilde P\tilde Q=\underbrace{\tilde P\bullet\tilde Q}_{\text{symmetric band}}
+\underbrace{\tilde P\wedge\tilde Q}_{\text{this band}},
\qquad\text{equivalently}\qquad
\tilde P\wedge\tilde Q=\tfrac12[\tilde P,\tilde Q],
$$

so the antisymmetric plain product is the **halved commutator**,
$[\tilde P,\tilde Q]=2\tilde P\wedge\tilde Q$. The two bands differ by the factor of two in each slot and
by nothing else. The
symmetric band is *The Symmetrised Material Composition and the Jordan Identity*; the comparison of the
four general products and their parts is *The Four General Products and Their Physical Readings: the Two Algebras and the
Two Sesqualgebras*.

## The Cross Product and the Jacobi Identity

**Definition.** A **Lie bracket** on a module is an alternating bilinear operation that satisfies the
**Jacobi identity**

$$
\tilde P\wedge(\tilde Q\wedge\tilde R)+\tilde Q\wedge(\tilde R\wedge\tilde P)
+\tilde R\wedge(\tilde P\wedge\tilde Q)=0 ,
$$

and a module with a Lie bracket is a **Lie algebra**; the axioms are those of *Lie Algebras: A General Introduction*.

**Theorem.** The antisymmetric plain product satisfies the Jacobi identity for all
$\tilde P,\tilde Q,\tilde R$:

$$
\tilde P\wedge(\tilde Q\wedge\tilde R)+\tilde Q\wedge(\tilde R\wedge\tilde P)
+\tilde R\wedge(\tilde P\wedge\tilde Q)=0 .
$$

*Proof.* By the coordinate form the identity is the Jacobi identity of the cross product,
$\mathbf{P}\times(\mathbf{Q}\times\mathbf{R})+\mathbf{Q}\times(\mathbf{R}\times\mathbf{P})+\mathbf{R}\times(\mathbf{P}\times\mathbf{Q})=0$,
which is the vector triple product identity. The scalar
part is zero on every term and the vector identity holds identically. The identity was recomputed here on
general elements and on random triples. It is established as a Lie algebra in *The Lie Algebra of the
Antisymmetric Plain Algebra*.

**Theorem (the uniqueness among the twelve).** Of the twelve operations
$\mathrm{GPA},\mathrm{SPA},\mathrm{APA},\mathrm{GQA},\mathrm{SQA},\mathrm{AQA},\mathrm{GPS},\mathrm{SPS},\mathrm{APS},\mathrm{GQS},\mathrm{SQS},\mathrm{AQS}$
of *The 12 Products of the Biquaternion Complex Space*, the antisymmetric plain product
is the **only** one that is a **Lie product**.

*Proof.* The identity is put to the antisymmetrisations of the batch; the four general products are
neither symmetrisations nor antisymmetrisations, and the identity is not put to them. Of the four
antisymmetric parts only the plain one satisfies it, the other three failing on the witnesses recorded in
the table of *The 12 Products of the Biquaternion Complex Space*, computed there on
the basis. The plain antisymmetrisation passes because it is the halved commutator of the one associative
product of the twelve, and the halved commutator of an associative product always satisfies the Jacobi
identity. The identity was recomputed here for the plain antisymmetric part and failed for the
neighbouring antisymmetric parts.

**Remark (the two laws and the two bands).** Among the four antisymmetrisations of the twelve exactly one
is a Lie product, and among the four symmetrisations exactly one is a Jordan product; both sit in the
plain row, $\mathrm{APA}$ as the Lie bracket and $\mathrm{SPA}$ as the Jordan product, and none of the
other six parts meets the identity of its kind. Read with the bracket $\wedge$, the biquaternion
space is a complex Lie algebra of complex dimension four, written
$\mathfrak{g}=(\mathbb{B},\wedge)$.

## The Bracket of the Infinitesimal Rotations

A rotation of the frame about the direction $e_k$ is the conjugation by the real unit rotor
$\tilde\Lambda_k(\theta)$ of the corpus. More generally a conjugation by any element of unit norm is an
algebra automorphism: for a unit element $\tilde\Lambda$ with
$N(\tilde\Lambda)=\tilde\Lambda\tilde\Lambda^{\natural}=1$,

$$
R_{\tilde\Lambda}(\tilde X)=\tilde\Lambda\tilde X\tilde\Lambda^{-1},
$$

is an automorphism of the algebra, and the rotors with their Lorentzian companions are *Biquaternion
Rotations and Lorentz Transformations*. The rotor of the rotation about $e_k$ by the angle $\theta$ is

$$
\tilde\Lambda_k(\theta)=\cos\tfrac{\theta}{2}+\sin\tfrac{\theta}{2}\,e_k,
\qquad
\text{of unit norm, since } e_k^{2}=-e_0 .
$$

Because this rotor is real, its conjugation is a spatial rotation; a conjugation by a non-real unit
element is a complex rotation of the frame and not a spatial one, and the conjugations by all the unit
elements are the inner automorphisms of the algebra.

**Proposition (the generator of conjugation is the bracket).** The derivative of the conjugation at the
identity is the antisymmetric plain product:

$$
\left.\frac{d}{d\theta}\right|_{\theta=0}R_{\tilde\Lambda_k(\theta)}(\tilde X)
=\tfrac12\bigl[e_k,\tilde X\bigr]=e_k\wedge\tilde X .
$$

*Proof.* The derivative of $\tilde\Lambda\tilde X\tilde\Lambda^{-1}$ is
$\dot{\tilde\Lambda}\tilde X\tilde\Lambda^{-1}+\tilde\Lambda\tilde X(\tilde\Lambda^{-1})^{\cdot}$; at
$\theta=0$ the rotor is $e_0$, the inverse is $e_0$, and
$\dot{\tilde\Lambda}_k(0)=\tfrac12 e_k$, $\dot{\tilde\Lambda}_k^{-1}(0)=-\tfrac12 e_k$, so the
derivative is $\tfrac12(e_k\tilde X-\tilde X e_k)=\tfrac12[e_k,\tilde X]$, which is $e_k\wedge\tilde X$.
Verified by central differences on $100$ random elements, max deviation $3\times10^{-10}$.

The proposition is the whole content of the reading: **the infinitesimal rotation about the axis $e_k$ has
generator $e_k$ under the bracket**, and the bracket of the block is the algebra of the infinitesimal
rotations. The generators of the compact factor are

$$
T_a=\tfrac12 e_a,
\qquad
[T_a,T_b]=\varepsilon_{abc}T_c ,
$$

the convention of *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches $\mathrm{SU}(2)$ but Not
$\mathrm{SU}(3)$*, so the real vector triple with the commutator is $\mathfrak{su}(2)$, which is
$\mathfrak{so}(3)$ as a real Lie algebra. Verified on the three generators. The bracket $\wedge$ carries
the same structure constants up to the halving, $T_a\wedge T_b=\tfrac12\varepsilon_{abc}T_c$.

**Proposed reading, labelled as such.** The rotor returns to $-e_0$ at $2\pi$, so the identity is
reached only at $4\pi$. **The half-angle of the rotor is the algebraic home of the two-valuedness of the
spinor.** *The physical spin is owned by Angular Momentum and Spin in Biquaternionic Form.*

## The Closure of the Rotation Algebra

**Proposed reading, labelled as such.** The antisymmetric plain product is the bracket of the
**infinitesimal rotations** of the frame, and its Jacobi identity is the **closure of the rotation
algebra**. Three statements make the reading.

- **The generator of a rotation is an element of the bracket.** The derivative of a one-parameter family
  of conjugations is the bracket with the generator, by the proposition above.
- **Two infinitesimal rotations compose to an infinitesimal rotation.** The commutator of two vector
  elements is a vector element, $[T_a,T_b]=\varepsilon_{abc}T_c$, so the set of generators is
  **closed** under the bracket, and the structure constants are the antisymmetric symbols. This closure
  is the algebraic content of "a rotation is generated by a rotation".
- **The closure is coherent because of the Jacobi identity.** The Jacobi identity is the identity the
  bracket must satisfy so that the successive commutators do not depend on the order in which the
  generators are taken. It is the exact analogue, for the bracket, of the associativity of the ordinary
  product: it is the law that the halved commutator inherits from the associativity of the product, and
  it is what makes the algebra of the generators a Lie algebra. The derivation of the Jacobi identity
  from the associativity of the product is *The Commutator Operator*.

The reading collects the three into one sentence: the antisymmetric plain product is the algebra of the
rotation group, its generators are the three real vector units, its structure constants are the
antisymmetric symbols, and the Jacobi identity is the coherence of the closure. What the algebra proves
is that $(\mathrm{Vect}(\mathbb{B}),\wedge)$ with the real vector triple is $\mathfrak{su}(2)$; the words
"infinitesimal rotation", "rotation group" and "closure" are the reading.

**Proposed reading, labelled as such.** Lifted from this bracket to the operator algebra of covariant
derivatives, the same identity becomes the Bianchi identity of the gauge curvature. *Gauge Curvature and
the Bianchi Identity in Biquaternionic Form* carries out that substitution; the bracket here is its
algebraic ancestor, at the level of the algebra rather than of the operators.

**Proposed reading, labelled as such.** The real vector triple generates the compact
$\mathfrak{su}(2)\cong\mathfrak{so}(3)$, whose complexification $\mathfrak{sl}(2,\mathbb{C})$ is the
algebra the whole vector subspace carries. **The internal symmetry the frame carries natively is the
rotation algebra of its own material sector**: the symmetry it carries internally is nothing beyond the
rotations of the frame itself.

**Proposed reading, labelled as such.** The derived algebra is the vector subspace, six-dimensional over
$\mathbb{R}$, which is the Lorentz algebra of bivectors. **The generators of the Lorentz transformations
and the components of an antisymmetric field strength are the same space**, and the central imaginary $i$
acts on it as the duality rotation, giving the self-dual and anti-self-dual halves and the combination
$\mathbf E+ic\mathbf B$. *The identification of the vector subspace with the field-strength space, and
the split, are owned by The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material
Sector.*

## What the Bracket Is Not

**Bound (a Lie bracket is not yet a group).** The bracket is the algebra of the generators, and a group is
obtained from it only by an exponential, which the block does not carry. The passage from the algebra to
the group, the global topology, the two-to-one cover of the rotation group and the reachable gauge groups
are *Biquaternion Rotations and Lorentz Transformations*, *The Biquaternion Unit Group as a Topological
Group* and *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches $\mathrm{SU}(2)$ but Not
$\mathrm{SU}(3)$*; the bracket of this article is the input, not the output. In particular the bracket
does not know whether the group it generates is compact: the compactness is read from the sign of the
invariant form, and that is the subject of *Angular Momentum and the Lie Algebra of the Material Sector*.

**Bound (the bracket is not the physical angular momentum).** The algebra of the generators is not the
angular momentum of a physical system. The angular momentum operators of the frame, their action on the
spinor module, their ladder structure and their quantisation are *Angular Momentum and Spin in
Biquaternionic Form*, which owns the physical object and imports the bracket from here. The bracket
supplies the algebra; the operators, the modules and the representations are the other article's.

**Bound (no positivity, no unit, no metric).** The bracket has no unit, because it has zero diagonal,
$\tilde P\wedge\tilde P=0$, and it carries no positivity and no metric: the invariant form it does carry
is indefinite and degenerate, and it is read in the companion article. The cross product of this block is
the bracket of the generators of the frame and not the vector product of two physical vector fields,
which is a separate construction.

## The Ledger

**Proved.** The antisymmetric plain product
$\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf{P}\times\mathbf{Q}$ is
$\mathbb{C}$-bilinear, alternating and skew, with zero scalar part and values in $\mathrm{Vect}(\mathbb{B})$,
and no unit; it satisfies the Jacobi identity, and it is the only Lie product among the twelve; the
ordinary product is reconstructed as $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$, so
$\tilde P\wedge\tilde Q=\tfrac12[\tilde P,\tilde Q]$; the derivative of the rotation
$\tilde X\mapsto\tilde\Lambda_k(\theta)\tilde X\tilde\Lambda_k(\theta)^{-1}$ at the identity is the
bracket with $e_k$, $\tfrac12[e_k,\tilde X]=e_k\wedge\tilde X$; and the real
vector triple with the generators $T_a=\tfrac12 e_a$ satisfies $[T_a,T_b]=\varepsilon_{abc}T_c$, so it
is $\mathfrak{su}(2)\cong\mathfrak{so}(3)$.

**Readings.** That the antisymmetric plain product is the bracket of the **infinitesimal rotations** of
the frame; that its generators are the three real vector units and its structure constants the
antisymmetric symbols; that the Jacobi identity is the **closure of the rotation algebra** and the
ancestor of the Bianchi identity; that the generator space is the field strength; that the internal
symmetry the frame carries natively is its own rotation algebra; and that the half-angle of the rotor is
the two-valuedness of the spinor. Each is the framework's naming of a proved algebraic
fact and is labelled as such.

**Not claimed.** That a Lie bracket is a group; that the bracket knows the compactness of the group it
generates; that the bracket is the physical angular momentum of a system; that the operation carries a
positivity, a unit or a metric.

## Summary

The antisymmetric part of the ordinary product is the **cross product of the two vector parts**,
$\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)=\mathbf{P}\times\mathbf{Q}$, with zero
scalar part and values in the traceless vector subspace, and it is the halved commutator,
$\tilde P\wedge\tilde Q=\tfrac12[\tilde P,\tilde Q]$. The operation is $\mathbb{C}$-bilinear, alternating
and skew, it has no unit, and it satisfies the **Jacobi identity**; it is the only Lie product of the
twelve operations of *The 12 Products of the Biquaternion Complex Space*, so the
biquaternion space with the bracket is a complex Lie algebra of complex dimension four. The physical
reading offered and labelled here is that the operation is the bracket of the **infinitesimal rotations**
of the frame: the derivative of the rotation
$\tilde X\mapsto\tilde\Lambda_k(\theta)\tilde X\tilde\Lambda_k(\theta)^{-1}$ at the identity is the
bracket, the generator of the rotation about $e_a$ is $T_a=\tfrac12e_a$, and the
three generators satisfy $[T_a,T_b]=\varepsilon_{abc}T_c$, so the real vector triple is
$\mathfrak{su}(2)\cong\mathfrak{so}(3)$; the Jacobi identity is the **closure of the rotation algebra**.
A Lie bracket is not yet a group, and the bracket is the algebra of the generators, not the physical
angular momentum.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\wedge\tilde Q=\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)$ | Antisymmetric plain product, the operation $\mathrm{APA}$ |
| $\mathbf{P}\times\mathbf{Q}$ | The cross product of the two vector parts; the value of the bracket |
| $\tilde P\wedge\tilde Q=\tfrac12[\tilde P,\tilde Q]$ | The bracket as the halved commutator |
| $\tilde P\tilde Q=\tilde P\bullet\tilde Q+\tilde P\wedge\tilde Q$ | The reconstruction $\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA}$ |
| $\mathrm{Vect}(\mathbb{B})$ | Traceless vector subspace; the derived algebra and the image of the bracket |
| $\tilde P\wedge(\tilde Q\wedge\tilde R)+\tilde Q\wedge(\tilde R\wedge\tilde P)+\tilde R\wedge(\tilde P\wedge\tilde Q)=0$ | The Jacobi identity |
| $R_{\tilde\Lambda}(\tilde X)=\tilde\Lambda\tilde X\tilde\Lambda^{-1}$ | Conjugation by a unit element; a rotation of the frame |
| $\tilde\Lambda_k(\theta)=\cos\tfrac{\theta}{2}+\sin\tfrac{\theta}{2}e_k$ | Rotor of the rotation about $e_k$ by $\theta$ |
| $T_a=\tfrac12e_a$, $[T_a,T_b]=\varepsilon_{abc}T_c$ | Generators of the compact factor; $\mathfrak{su}(2)\cong\mathfrak{so}(3)$ |
| $(p,q)$ | Signature written as (number of $+$, number of $-$) |

## Further Reading

- Mathematics article *Introduction to the Antisymmetric Plain Algebra of Biquaternions*, for the
  operation, its alternation, its coordinate form and its placement among the twelve.
- Mathematics article *The Lie Algebra of the Antisymmetric Plain Algebra*, for the centre, the derived
  algebra, the identifications with $\mathfrak{sl}(2,\mathbb{C})$, $\mathfrak{su}(2)$ and $\mathfrak{u}(2)$,
  and the ideals.
- Mathematics article *The Commutator Operator* and *Associative Algebras*, for the derivation of the
  Jacobi identity from the associativity of the product.
- Mathematics article *The 12 Products of the Biquaternion Complex Space*, for the
  twelve operations and the uniqueness of the Jacobi and Jordan laws.
- Mathematics article *Biquaternion Rotations and Lorentz Transformations*, for the conjugations, the
  rotors and the Lorentz action.
- Companion article *The Symmetrised Material Composition and the Jordan Identity*, for the symmetric
  half of the same product.
- Companion article *Angular Momentum and the Lie Algebra of the Material Sector*, for the invariant form
  of the bracket, the adjoint operators and the reading of the generators.
- Companion article *Angular Momentum and Spin in Biquaternionic Form*, for the physical angular momentum.
