# __The Operators of the Symmetrised Plain Product: Jordan Commutativity__

## Introduction

This article is the operator article of the symmetric plain algebra, the band of *The Symmetrised Material
Composition and the Jordan Identity* and *Observables as a Jordan Algebra: the Symmetric Plain Product and the
Classical Composition*. Its product is $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$,
and the operators of the band attach an element to an argument:

$$
L^{\bullet}_{\tilde Q}(\tilde R)=\tilde Q\bullet\tilde R,\qquad
R^{\bullet}_{\tilde P}(\tilde R)=\tilde R\bullet\tilde P .
$$

Because the product is commutative the two **coincide**, $L^{\bullet}_{\tilde A}=R^{\bullet}_{\tilde A}$: the
band carries **one** family and not two, and the two-sided operator a Jordan algebra keeps from the associative
sandwich is the **quadratic representation** $U_{\tilde A}=2(L^{\bullet}_{\tilde A})^{2} -L^{\bullet}_{\tilde A\bullet\tilde A}$, acting by $\tilde X\mapsto\tilde A\tilde X\tilde A$. The element theory
of the block is *The Specificities of the Symmetric Plain Algebra*; the measurement interpretation and the classical
composition are the two sibling articles' business; this article adds the operator layer only.

The answer is one sentence. The form of the block is the **trace form**
$\tau(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\bullet\tilde Q)=P_0Q_0-(\vec P,\vec Q)$, of Gram
$\mathrm{diag}(1,-1,-1,-1)$, symmetric, non-degenerate and **invariant**; the adjoint for it is the transpose
$F^{\approx}$, and the transpose of a multiplication is the same multiplication,
$(L^{\bullet}_{\tilde A})^{\approx}=L^{\bullet}_{\tilde A}$ and
$(L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde B})^{\approx}=L^{\bullet}_{\tilde B}L^{\bullet}_{\tilde A}$.
Association therefore **keeps the parameter**, and there is no second side onto which it could move the
operator; the general plain block is the opposite case, $(L_{\tilde A})^{\approx}=R_{\tilde A}$, where the
adjoint **swaps the sides**, and that swap is impossible here because the two families are one. The conjugation
of a parameter belongs to a different adjoint, the **Hermitian dagger**
$(L^{\bullet}_{\tilde A})^{\dagger}=L^{\bullet}_{\tilde A^{*}}$ for the positive definite Hermitian form,
marked $\dagger$ and not $\approx$. The collapse of the two families is the whole difference of this row from
the general one; the comparison is the crossing reader *The Operators of the Twelve Structures: Multiplication,
Adjoint and Bracket*, not one of the twelve.

The conventions are those of *Conventions in the Biquaternion Universe*:
$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$,
$e_k^{2}=-e_0$ and central imaginary $i$; $\tilde Q=Q_0e_0+\vec Q$; sectors
$\mathbb{M}_\pm=\{\tilde Q:\tilde Q^{*}=\pm\tilde Q\}$; generic trace $T(\tilde Q)=2Q_0$ and generic norm
$N(\tilde Q)=\sum_\mu Q_\mu^{2}$. The operator theory is owned by four mathematics articles and is cited in
place: *The Multiplication Operators of the Symmetric Plain Algebra* for the one family, its composition, its
self-associateness, the Jordan identity on it, its derivations and its automorphisms; *The Trace Form and the
Invariance of the Symmetric Plain Algebra* for the form; *The Left and Right Multiplication Operators on a
Jordan Algebra* for the quadratic representation and the fundamental formula; and *The Jordan Multiplication
Operators* for the general one-sided family.

## The One Family of Multiplications and Its Composition

**Definition.** The **left** and the **right multiplication operators** of the band by an element $\tilde A$ are
$L^{\bullet}_{\tilde A}(\tilde Q)=\tilde A\bullet\tilde Q$ and
$R^{\bullet}_{\tilde A}(\tilde Q)=\tilde Q\bullet\tilde A$, both $\mathbb{C}$-linear and unital at
$\tilde A=e_0$; $L_{\tilde A}$ and $R_{\tilde A}$ denote throughout the left and right multiplication
operators of the **plain** product, $\tilde Q\mapsto\tilde A\tilde Q$ and $\tilde Q\mapsto\tilde Q\tilde A$.

**Theorem (the two families coincide; the symmetric half).** For every $\tilde A$,

$$
L^{\bullet}_{\tilde A}=R^{\bullet}_{\tilde A}
=\tfrac12\bigl(L_{\tilde A}+R_{\tilde A}\bigr),
\qquad\text{so}\qquad
L_{\tilde A}+R_{\tilde A}=2L^{\bullet}_{\tilde A},
$$

and the sum carries the factor $2$.

*Proof.* $\tilde A\bullet\tilde Q=\tilde Q\bullet\tilde A$ by commutativity, and
$\tilde A\bullet\tilde Q=\tfrac12(\tilde A\tilde Q+\tilde Q\tilde A)$. The collapse for every commutative
product is *The Left and Right Multiplication Operators on a Jordan Algebra*; the symmetric-half identity is
*The Specificities of the Symmetric Plain Algebra*, §*The Multiplication Operator*.

**Read as a physical statement.** The band's operation has no orientation: attaching a composition on the left
and attaching it on the right are the same act, so the operator of an element carries no side and there is no
opposite-algebra distinction; the contrast with the general plain block, where the two families are distinct and
the adjoint exchanges them, is the whole operator content of the job word **commutativity**. The operator is
the symmetrised half of the parent's, and the factor $\tfrac12$ is why the composite below carries four plain
terms.

**Theorem (the composition law).** For all $\tilde A,\tilde B$,

$$
L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde B}
=\tfrac14\bigl(L_{\tilde A\tilde B}+L_{\tilde A}R_{\tilde B}+R_{\tilde A}L_{\tilde B}+R_{\tilde B\tilde A}\bigr),
$$

the composite is **not** the multiplication operator of the product, and its deviation from
$L^{\bullet}_{\tilde A\bullet\tilde B}$ is the **associator** with free third slot,
$\mathrm{as}(\tilde A,\tilde B,\tilde X)=(\tilde A\bullet\tilde B)\bullet\tilde X -\tilde A\bullet(\tilde B\bullet\tilde X)$.

*Proof.* Expand $\tfrac14(L_{\tilde A}+R_{\tilde A})(L_{\tilde B}+R_{\tilde B})$ and recombine the cross
products with $L_{\tilde A}R_{\tilde B}=R_{\tilde B}L_{\tilde A}$ and
$R_{\tilde A}R_{\tilde B}=R_{\tilde B\tilde A}$; evaluating at $\tilde X$ gives the associator. This is *The
Multiplication Operators of the Symmetric Plain Algebra*, §*The Composition and the Failure of Multiplicativity*.

**Corollary (the witness).** The block is not associative: $e_1\bullet(e_1\bullet e_2)=0\neq-e_2 =(e_1\bullet e_1)\bullet e_2$, since $e_1\bullet e_2=\tfrac12(e_3-e_3)=0$ and $e_1\bullet e_1=e_1^{2}=-e_0$.

**Read as a physical statement.** Two order-free compositions do not compose to an order-free composition, and
the defect is exactly the cross term the antisymmetric band keeps; the interpretation is that the symmetrisation
discards order when it is applied twice, so the block is a Jordan and not an associative algebra and its left
regular representation is not multiplicative.

**Theorem (the Jordan identity on the operators).** For every $\tilde X$ the operator of an element commutes
with the operator of its square,

$$
\bigl[L^{\bullet}_{\tilde X},L^{\bullet}_{\tilde X\bullet\tilde X}\bigr]=0,
$$

and in the operator algebra the surviving law is the **fundamental formula**
$U_{U_{\tilde A}\tilde B}=U_{\tilde A}U_{\tilde B}U_{\tilde A}$ with
$U_{\tilde A}^{2}=U_{\tilde A\bullet\tilde A}$.

*Proof.* The Jordan identity $(\tilde X\bullet\tilde Y)\bullet(\tilde X\bullet\tilde X) =\tilde X\bullet(\tilde Y\bullet(\tilde X\bullet\tilde X))$ written with $L^{\bullet}$ gives the commutation;
the fundamental formula is *The Jordan Multiplication Operators*, quoted in *The Left and Right Multiplication
Operators on a Jordan Algebra*.

**Read as a physical statement.** The order-free composition satisfies one law in place of associativity:
$P^{2}Q$ and $P(PQ)$ differ, but the operators of $P$ and of $P^{2}$ commute. The interpretation is that a Jordan
product keeps enough order-blindness to make the square a central object of the operator calculus, and fails
just enough to keep the operator algebra from being the algebra of the elements; the element form is *The
Symmetrised Material Composition and the Jordan Identity*.

## The Adjoint of the Trace Form Keeps the Parameter

**Definition (the trace form).** The form of the band is the scalar part of its product,

$$
\tau(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\bullet\tilde Q)=P_0Q_0-(\vec P,\vec Q),
\qquad \mathrm{Gram}=\mathrm{diag}(1,-1,-1,-1).
$$

It is $\mathbb{C}$-bilinear, symmetric, non-degenerate, of realified signature $(4,4)$, with the restrictions
$(1,1),(3,3),(1,3),(3,1),(4,0),(0,4)$ to the remarkable subspaces; it is **invariant**,
$\tau(\tilde P\bullet\tilde Q,\tilde R)=\tau(\tilde P,\tilde Q\bullet\tilde R)$, which is the associativity of
the plain product read on the symmetrised product, and not merely symmetric. Its operator traces are
$\operatorname{Tr}(L^{\bullet}_{\tilde P})=4P_0=2T(\tilde P)$ and $\operatorname{Tr}(L^{\bullet}_{\tilde P}L^{\bullet}_{\tilde Q})=4P_0Q_0-2(\vec P,\vec Q)=2\tau(\tilde P,\tilde Q)+\tfrac12T(\tilde P)T(\tilde Q)$,
the second being **not** a multiple of the form; and on the Hermitian sector the form is the positive definite
Born pairing $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})$.

*Proof.* The coordinate form and the Gram matrix are read on the basis, the invariance is the cyclic invariance
of $\mathrm{Sc}$ of a plain triple product, and the trace identity is computed on the basis: *The Trace Form and
the Invariance of the Symmetric Plain Algebra*. On the sector $P_0,Q_0$ are real and $P_k,Q_k$ purely imaginary,
so $\tau=H$ and is positive definite, as read in *Observables as a Jordan Algebra: the Symmetric Plain Product
and the Classical Composition*.

**Read as a physical statement.** The form of the band is the scalar part of its own product, and its invariance
is the associativity of the plain product read on the symmetrised one; an invariant form is one across which an
operation can be transported, and the transport is the adjoint. Its indefiniteness is the sector sign, positive
on the observables and negative on the material sector, and its identity with the Born pairing on the
observables is the algebraic content of the classical-composition interpretation.

**Theorem (association keeps the parameter).** For all $\tilde A,\tilde X,\tilde Y$,
$\tau(L^{\bullet}_{\tilde A}\tilde X,\tilde Y)=\tau(\tilde X,L^{\bullet}_{\tilde A}\tilde Y)$, that is
$(L^{\bullet}_{\tilde A})^{\approx}=L^{\bullet}_{\tilde A}$: every multiplication is its own associate, so the
adjoint for the trace form **keeps the parameter**.

*Proof.* $\tau(\tilde A\bullet\tilde X,\tilde Y)=\tau(\tilde A,\tilde X\bullet\tilde Y) =\tau(\tilde X\bullet\tilde Y,\tilde A)=\tau(\tilde X,\tilde Y\bullet\tilde A)$; the form is non-degenerate.
This is *The Multiplication Operators of the Symmetric Plain Algebra*, §*The Associate with Respect to the
Trace Form*.

**Corollary (the composite is transported backwards).** $(L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde B})^{\approx} =L^{\bullet}_{\tilde B}L^{\bullet}_{\tilde A}$, so a composite is its own associate exactly when its two factors
commute.

**Read as a physical statement.** Two interpretations, the sharp statement of the band. The adjoint for the form
**does not move the operator**: it neither swaps the sides, as the general plain adjoint does, nor conjugates
the parameter, as the Hermitian dagger does, and the interpretation is that the order-free composition is
**self-paired** — the form cannot tell a left attachment from a right one because there is only one, and it
carries no conjugation to collapse onto. The pairing transports a chain of two compositions backwards, and only
a commutative chain is invisible to the reversal. The contrast with the plain swap and with the dagger is the
crossing reader.

**Theorem (the other adjoint conjugates the parameter).** For the Hermitian form
$H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})$ the adjoint is the dagger,
$(L^{\bullet}_{\tilde A})^{\dagger}=L^{\bullet}_{\tilde A^{*}}$, which **conjugates the parameter** and is not
the adjoint for the trace form.

*Proof.* $\mathrm{Sc}(\tilde A\tilde X\tilde Q^{*})=\mathrm{Sc}(\tilde X\tilde Q^{*}\tilde A) =\mathrm{Sc}(\tilde X(\tilde A^{*}\tilde Q)^{*})$, and the same on the right; the remark of *The Multiplication
Operators of the Symmetric Plain Algebra*.

**Read as a physical statement.** The framework carries two adjoints of one family and they must not be
exchanged: the trace-form adjoint keeps the parameter and is a transpose statement about an indefinite form,
while the Hermitian dagger conjugates the parameter and carries the physical dictionary of observables and
generators. That dictionary and its positivity are *Observables, Gauge Generators and the Chirality of the
Internal Action* and *Mass, Rank and the Positivity of the Dagger*; the reading here is only that the
conjugation belongs to the dagger and the trace-form adjoint has none to apply.

## The Types of the Operators

**Theorem (the types for the trace form).** Every $L^{\bullet}_{\tilde A}$ is **self-adjoint** for $\tau$, and
the only **skew-adjoint** multiplication is the zero operator, so the one-sided family contains **no generator**.
The generators of the operator calculus are instead the **commutators** of the family, which are its **inner
derivations**,

$$
\bigl[L^{\bullet}_{\tilde A},L^{\bullet}_{\tilde B}\bigr]
=\tfrac14\operatorname{ad}_{[\tilde A,\tilde B]},\qquad
\operatorname{ad}_{\tilde C}=L_{\tilde C}-R_{\tilde C},
$$

of complex dimension three, each skew for $\tau$.

*Proof.* Self-adjointness is the associate theorem in the mark of the form; skew-adjointness gives
$\tilde A\bullet\tilde X=0$ for every $\tilde X$, hence $\tilde A=0$ at $e_0$. The commutator identity and the
dimension are *The Multiplication Operators of the Symmetric Plain Algebra*, §*The Inner Derivations*, and each
derivation is skew because it is a derivation of the plain product and $\tau$ is invariant.

**Read as a physical statement.** The one-parameter family is a family of symmetric operators and contains no
generator: the band supplies no infinitesimal operation of its own family. The generators are the
**commutators** of two multiplications, the inner derivations, of dimension three, and the interpretation is that what
is infinitesimal in the block is the failure of two compositions to commute. The derivation algebra is
$\mathfrak{sl}(2,\mathbb{C})$, read as *Angular Momentum and the Lie Algebra of the Material Sector* and, with
the observables dictionary, in *Observables, Gauge Generators and the Chirality of the Internal Action*.

**Theorem (the types for the Hermitian dagger).** $(L^{\bullet}_{\tilde A})^{\dagger}=L^{\bullet}_{\tilde A}$
iff $\tilde A\in\mathbb{M}_+$, and $(L^{\bullet}_{\tilde A})^{\dagger}=-L^{\bullet}_{\tilde A}$ iff
$\tilde A\in\mathbb{M}_-$: a multiplication by an observable is self-adjoint for the physical form, one by a
generator is skew-adjoint, and a mixed parameter gives neither.

*Proof.* By $(L^{\bullet}_{\tilde A})^{\dagger}=L^{\bullet}_{\tilde A^{*}}$ and injectivity of
$\tilde A\mapsto L^{\bullet}_{\tilde A}$, the condition is $\tilde A^{*}=\pm\tilde A$.

**Read as a physical statement.** The two sectors separate the two physical classes: a Hermitian parameter is the
self-adjoint multiplication of an observable, an anti-Hermitian one the skew-adjoint multiplication of a
generator. On the observables the trace form is the Born pairing, so the two adjoints coincide there and the two
dictionaries agree, while off that sector they separate, and the separation is the indefiniteness of the trace
form.

**Corollary (the types of the sandwich).** $U_{\tilde A}$ is self-adjoint for $\tau$ for **every** parameter;
for the dagger $U_{\tilde A}^{\dagger}=U_{\tilde A^{*}}$, so $U_{\tilde A}$ is dagger-self-adjoint iff
$\tilde A\in\mathbb{M}_+\cup\mathbb{M}_-$ and is **never** dagger-skew.

*Proof.* $U_{\tilde A}=2(L^{\bullet}_{\tilde A})^{2}-L^{\bullet}_{\tilde A\bullet\tilde A}$ is a polynomial in
self-adjoint operators with the same parameter, hence self-adjoint for $\tau$; dually
$U_{\tilde A}^{\dagger}=U_{\tilde A^{*}}$. Since $U_{-\tilde A}=U_{\tilde A}$, both sectors qualify, while a
mixed parameter fails, checked on the polarization
$U_{\tilde A,\tilde B}\tilde X=\tfrac12(\tilde A\tilde X\tilde B+\tilde B\tilde X\tilde A)$. *The Left and
Right Multiplication Operators on a Jordan Algebra*, §*The Trace Form*.

**Read as a physical statement.** The sandwich is symmetric for the trace form whatever its parameter, so the
trace form never distinguishes one sandwich from another; the physical form does, and it is self-adjoint exactly
on the two sectors. The interpretation is the framework's own: a measurement update and a conjugation are both
symmetric, a sector-mixing parameter is not. The difference from the general plain block is the form for which
the criterion holds.

## The Symmetries of the Form and of the Product

**Theorem (the form-preserving multiplications).** $L^{\bullet}_{\tilde A}$ preserves $\tau$,
$\tau(L^{\bullet}_{\tilde A}\tilde X,L^{\bullet}_{\tilde A}\tilde Y)=\tau(\tilde X,\tilde Y)$ for all
$\tilde X,\tilde Y$, iff $\tilde A=\pm e_0$, that is $L^{\bullet}_{\tilde A}=\pm\mathrm{id}$; inside the family
the symmetries of the form are only the two scalar signs.

*Proof.* With self-adjointness, preservation is $(L^{\bullet}_{\tilde A})^{2}=\mathrm{id}$; at $e_0$ this gives
$\tilde A\bullet\tilde A=e_0$, and reading the operator identity at a general $\tilde X$ gives
$\tilde A\bullet(\tilde A\bullet\tilde X)=\tilde X$; together they force $\tilde A\tilde X\tilde A=\tilde X$ for
all $\tilde X$, so $\tilde A$ is central of square $e_0$, that is $\pm e_0$.

**Corollary (the form-preserving two-sided operators).** A two-sided operator $L_{\tilde A}R_{\tilde B}$
preserves $\tau$ iff $\tilde B\tilde A=\pm e_0$, so the form-preserving two-sided operators are the
$\pm\mathrm{Ad}_{\tilde A}$; in particular the quadratic representation $U_{\tilde A}=L_{\tilde A}R_{\tilde A}$
preserves $\tau$ iff $\tilde A\bullet\tilde A=\tilde A^{2}=\pm e_0$.

*Proof.* Preservation is $\tau(\tilde A\tilde X\tilde B,\tilde A\tilde Y\tilde B)=\tau(\tilde X,\tilde Y)$;
since $\tau(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)$, cyclicity shifts it to
$\mathrm{Sc}(\tilde X\tilde B\tilde A\tilde Y\tilde B\tilde A)=\mathrm{Sc}(\tilde X\tilde Y)$, that is
$\tau(\tilde X,(\tilde B\tilde A)\tilde Y(\tilde B\tilde A))=\tau(\tilde X,\tilde Y)$ for all $\tilde X$, and
non-degeneracy gives $(\tilde B\tilde A)\tilde Y(\tilde B\tilde A)=\tilde Y$ for all $\tilde Y$ — the middle
word is the product $\tilde B\tilde A$ on both sides, never $\tilde B\tilde Y\tilde A$. At $\tilde Y=e_0$ this
gives $(\tilde B\tilde A)^{2}=e_0$, and multiplying the identity by $\tilde B\tilde A$ on the left gives
centrality; setting $\tilde A=\tilde B$ gives the quadratic criterion.

**Read as a physical statement.** Inside the one family only the two scalar signs preserve the form; the richer
statement is that an element of square $\pm e_0$ acts as an isometry through its **sandwich**, not through its
multiplication, which need not be invertible. The two-sided criterion is the same one the general plain block
records for the same pairing, so the two-sided symmetries do not change from block to block; what changes is
the form.

**Theorem (the product-preserving operators).** The invertible operators preserving the symmetrised product are
the **automorphisms**, and no non-trivial multiplication is one: the inner automorphisms
$\mathrm{Ad}_{\tilde A}=\tilde A(\cdot)\tilde A^{-1}$ over the units, of complex dimension three and isomorphic
to the projective general linear group, together with their coset through the **natural conjugation**
${\natural}$, which is outer. Every automorphism fixes $e_0$, preserves $T$ and $N$, and preserves $\tau$.

*Proof.* Conjugation by a unit preserves the plain product and hence the symmetrisation, with kernel the central
scalars; the natural conjugation is outer because it negates the antisymmetric part, which an inner automorphism
preserves; an automorphism fixes the unit and preserves $T,N$, hence $\tau=\tfrac12T\circ\bullet$. This is *The
Multiplication Operators of the Symmetric Plain Algebra*, §*The Automorphisms and the Structure Group*.

**Corollary (the multiplicative operators).** A multiplication is multiplicative,
$L^{\bullet}_{\tilde A}(\tilde X\bullet\tilde Y) =(L^{\bullet}_{\tilde A}\tilde X)\bullet(L^{\bullet}_{\tilde A}\tilde Y)$ for all $\tilde X,\tilde Y$, iff it
is the identity or the zero operator: $\tilde A=e_0$ or $0$.

*Proof.* Multiplicativity at $\tilde X=e_0$ gives $L^{\bullet}_{\tilde A}=(L^{\bullet}_{\tilde A})^{2}$, a
projector, and at $e_0$ gives $\tilde A=\tilde A\bullet\tilde A$, an idempotent; by *The Specificities of the
Symmetric Plain Algebra*, §*The Multiplication Operator*, a non-trivial idempotent gives no projector, so the
only projectors are $L^{\bullet}_{e_0}=\mathrm{id}$ and $L^{\bullet}_{0}=0$, and both are multiplicative.

**Read as a physical statement.** The symmetry of the form and the symmetry of the product fall on different
operators: the form is preserved by the quadratic representations at the elements of square $\pm e_0$, the
product by the two-sided inner automorphisms and the outer natural conjugation. The interpretation is that the band's
family carries **no** non-trivial automorphism — a multiplication moves an element but cannot relabel the
algebra — and the relabelling is the two-sided conjugation of the parent, the outer one being the coset the
inner automorphisms cannot reach.

## The Operators Acting on the State Space

**Proposition (the observable sector).** The sector $\mathbb{M}_+$ is closed under $\bullet$ and preserved by a
multiplication with a Hermitian parameter, $L^{\bullet}_{\tilde A}\mathbb{M}_+\subseteq\mathbb{M}_+$ for
$\tilde A\in\mathbb{M}_+$; on it $\tau$ is the positive definite Born pairing $H$, the two adjoints coincide,
and every multiplication of the sector is self-adjoint for that positive form. For an idempotent
$\tilde\Pi\bullet\tilde\Pi=\tilde\Pi$ the multiplication satisfies the **cubic Peirce identity**
$L^{\bullet}_{\tilde\Pi}(2L^{\bullet}_{\tilde\Pi}-\mathrm{id})(L^{\bullet}_{\tilde\Pi}-\mathrm{id})=0$, so
its eigenvalues lie in $\{0,\tfrac12,1\}$, the Peirce dimensions at a non-trivial idempotent are $1,2,1$, and
the operator is not a projector.

*Proof.* The product of two Hermitian elements is Hermitian, and on the sector $\tau=H$ is positive definite:
*Observables as a Jordan Algebra: the Symmetric Plain Product and the Classical Composition* and *The Trace
Form and the Invariance of the Symmetric Plain Algebra*. The cubic identity, the dimensions and the failure of
being a projector are *The Specificities of the Symmetric Plain Algebra*, §*The Idempotents and the Cubic Peirce
Theory*.

**Read as a physical statement.** On the observables the multiplications are the symmetric operators of a
classical system, and the interpretation is that the symmetrised composition, restricted to them, is the classical
composition and the operator of an observable is the operator of a measurable quantity. At a sharp question the
operator has the three Peirce values; the interpretation is that the answer is **graded** and that the classical
two-valued projection is absent, because a non-trivial idempotent gives no projector. The measurement and the
classical composition are the siblings' business, and this article supplies only the operator behind them.

**Proposition (the spinor space).** On the minimal left ideal
$S=\mathbb{B}\tilde\Pi_+=\mathbb{C}\{\tilde\Pi_+,\tilde\Upsilon_2\}$ with $\tilde\Pi_+=\tfrac12(e_0+ie_3)$, the
operator is half the matrix action of the module and half a module endomorphism of the complement,
$L^{\bullet}_{\tilde A}s=\tfrac12(\tilde A s+s\tilde A)$ for $s\in S$; a **central** parameter has equal halves
and acts as a scalar, $L^{\bullet}_{\lambda e_0}=\lambda\,\mathrm{id}$. Here $ie_3$ is a root of $+1$, $(ie_3)^2=e_0$, and $\tilde\Pi_+$ and $\tilde\Pi_-$ are its two associated idempotents.

*Proof.* The display is the symmetric-half theorem; the left half is the left regular representation of the
module, and a right multiplication commutes with every left one and is therefore a module map, carrying the
simple ideal into itself or its complement. *The Spinor Space as a Module and as a Hilbert Space* and *The
Complementary Space of the Spinor Space and Its Physical Meaning*.

**Read as a physical statement.** A state is acted on from the left by the observable and from the right by the
same observable, and the interpretation is that the classical composition sees a state from both sides at once. A
central parameter acts as a scalar and is the one operation the state space cannot see: the interpretation is the
invariance under a central phase and the statement that the state space carries no phase of its own.

## The Sandwich and the Inner Automorphism

**Proposition.** For an invertible $\tilde A$, $U_{\tilde A}(\tilde X)=\tilde A\tilde X\tilde A$ and
$\mathrm{Ad}_{\tilde A}(\tilde X)=\tilde A\tilde X\tilde A^{-1}$, so the sandwich attaches the parameter
without conjugation and the inner automorphism its inverse. They agree exactly at the **symmetries**
$\tilde A\bullet\tilde A=\tilde A^{2}=e_0$, and at an anti-symmetry $\tilde A^{2}=-e_0$ they differ by the sign,
$U_{\tilde A}=-\mathrm{Ad}_{\tilde A}$.

*Proof.* $U_{\tilde A}$ acts by $\tilde A\tilde X\tilde A$ (*The Left and Right Multiplication Operators on a
Jordan Algebra*, §*The Special Case*); the inner automorphism is the conjugation by the inverse; they coincide
when $\tilde A=\tilde A^{-1}$. An invertible element of square $-e_0$ has $\tilde A^{-1}=-\tilde A$, so
$\mathrm{Ad}_{\tilde A}=-U_{\tilde A}$.

**Theorem.** On a **symmetry** the quadratic representation is an automorphism of order two and is the inner
automorphism, $U_{\tilde A}^{2}=\mathrm{id}$ and $U_{\tilde A}=\mathrm{Ad}_{\tilde A}$, so it is an isometry of
the trace form and an automorphism of the product at once; for a general parameter it is self-adjoint for
$\tau$ but not multiplicative.

*Proof.* $U_{\tilde A}^{2}=U_{\tilde A\bullet\tilde A}=U_{e_0}=\mathrm{id}$ by the fundamental formula, and the
symmetry makes $U_{\tilde A}=\mathrm{Ad}_{\tilde A}$; self-adjointness for $\tau$ is the types corollary.
*The Left and Right Multiplication Operators on a Jordan Algebra*, §*Symmetries and Operators of Order Two*.

**Read as a physical statement.** The band has one two-sided operator, the sandwich, interpolating between two
roles: at an element of square $e_0$ it is the inner automorphism, isometry and automorphism at once, while at
an idempotent it is the symmetric quadratic representation, a projection ($U_{\tilde\Pi}^{2}=U_{\tilde\Pi}$)
and not a conjugation, and at a general element it is symmetric and not multiplicative. The interpretation is that the
**symmetry** of a Jordan algebra is the exact parameter for which the order-blind composition and the two-sided
conjugation agree, and they agree nowhere else.

## A Worked Case

Take the Hermitian symmetry $\tilde A=ie_1\in\mathbb{M}_+$, with $\tilde A^{*}=\tilde A$,
$\tilde A\bullet\tilde A=-e_1^{2}=e_0$, $\tau(\tilde A,\tilde A)=1$ and $N(\tilde A)=i^{2}=-1$. Its
multiplication operator on the basis $(e_0,e_1,e_2,e_3)$ is

$$
L^{\bullet}_{ie_1}=
\begin{pmatrix}0&-i&0&0\\ i&0&0&0\\ 0&0&0&0\\ 0&0&0&0\end{pmatrix},
\qquad
\det L^{\bullet}_{ie_1}=0,\qquad
\operatorname{rank}L^{\bullet}_{ie_1}=2,\qquad
\operatorname{Tr}L^{\bullet}_{ie_1}=4A_0=0 .
$$

It is self-adjoint for the trace form and for the Hermitian dagger, in agreement with the sector theorem, and it
is **not** an isometry of the trace form — it has rank two, so it cannot be. The element is a symmetry, and the
isometry it carries is its **sandwich**,

$$
U_{ie_1}(\tilde X)=ie_1\tilde X ie_1=\mathrm{diag}(1,1,-1,-1)\tilde X,
\qquad
U_{ie_1}^{2}=\mathrm{id},\qquad
U_{ie_1}=\mathrm{Ad}_{ie_1},
$$

the reflection that fixes the span of $e_0,e_1$ and negates the span of $e_2,e_3$; the multiplication by the
symmetry and the sandwich of the symmetry are different operators, and only the second preserves the form.

Take next the anti-Hermitian material parameter $\tilde B=e_1\in\mathbb{M}_-$, with $\tilde B^{*}=-e_1$,
$\tilde B\bullet\tilde B=e_1^{2}=-e_0$, $\tau(\tilde B,\tilde B)=-1$ and $N(\tilde B)=1$. Its operator is the
negative imaginary multiple of the previous one, $L^{\bullet}_{e_1}=-i\,L^{\bullet}_{ie_1}$, so
$(L^{\bullet}_{e_1})^{\dagger}=L^{\bullet}_{-e_1}=-L^{\bullet}_{e_1}$: the multiplication by a generator is
skew-adjoint for the Hermitian dagger and self-adjoint for the trace form, the two adjoints separating exactly
as the sectors do. Its sandwich is minus the inner automorphism, $U_{e_1}=-\mathrm{Ad}_{e_1}$, because
$e_1^{2}=-e_0$.

Take finally the Hermitian idempotent $\tilde\Pi=\tfrac12(e_0+ie_1)$, with
$\tilde\Pi\bullet\tilde\Pi=\tilde\Pi=\tilde\Pi^{*}$, $\tau(\tilde\Pi,\tilde\Pi)=\tfrac12$ and $N(\tilde\Pi)=0$.
Its operator has the cubic Peirce eigenvalues $0,\tfrac12,1$, is not a projector, satisfies
$L^{\bullet}_{\tilde\Pi}\tilde\Pi=\tilde\Pi$ and $L^{\bullet}_{\tilde\Pi}(e_0-\tilde\Pi)=0$ — the fixed line
$\mathbb{C}\tilde\Pi$ of eigenvalue $1$ and the kernel $\mathbb{C}(e_0-\tilde\Pi)$ of eigenvalue $0$ — while the
eigenvalue $\tfrac12$ has the two-dimensional eigenspace $\mathbb{C}\{e_2,e_3\}$. The three parameters — a
Hermitian symmetry, an anti-Hermitian generator and a Hermitian idempotent — give the two adjoint verdicts and
the one Peirce spectrum, and the case displays the whole type theory of the band on three elements.

**A numerical check.** For random elements of the block the identities
$L^{\bullet}_{\tilde A}=R^{\bullet}_{\tilde A}$, $L^{\bullet}_{\tilde A} =\tfrac12(L_{\tilde A}+R_{\tilde A})$, the four-term composition law, the associator deviation and the Jordan
identity $[L^{\bullet}_{\tilde X},L^{\bullet}_{\tilde X\bullet\tilde X}]=0$ hold to machine precision; the trace
form was checked to satisfy $\tau(\tilde P,\tilde Q)=P_0Q_0-(\vec P,\vec Q)$ with Gram
$\mathrm{diag}(1,-1,-1,-1)$ and the invariance, and the operator traces to satisfy
$\operatorname{Tr}(L^{\bullet}_{\tilde P})=4P_0$ and
$\operatorname{Tr}(L^{\bullet}_{\tilde P}L^{\bullet}_{\tilde Q})=4P_0Q_0-2(\vec P,\vec Q)$; every
multiplication was verified self-associate with the only
skew-adjoint one zero, and the inner derivations $\tfrac14\operatorname{ad}_{[\tilde A,\tilde B]}$ were verified
skew and three-dimensional; the form-preserving criterion was checked to hold exactly at $\pm e_0$ in the family
and at $\tilde B\tilde A=\pm e_0$ for two-sided operators, and the multiplicativity criterion only at the
identity and the zero operator; the quadratic representation was checked to act by $\tilde A\tilde X\tilde A$,
to be self-adjoint for $\tau$ for every parameter and for $\dagger$ exactly on the two sectors; and the three
worked parameters were recomputed element by element.

## The Bound

The article states one cell of the grid of the twelve operator rows, and the boundary of the cell is what it must
declare.

- **The element theory is not re-proved here.** The idempotents, the square, the Jordan inverse, the generic
  trace and norm, the Peirce decomposition and the zero divisors are *The Specificities of the Symmetric Plain
  Algebra* and the specific-theory articles; this article reads the operators they produce.
- **The operator theory is cited, not re-derived.** The one family, the composition law, the self-associateness,
  the Jordan identity, the derivations, the automorphism group and the structure group are *The Multiplication
  Operators of the Symmetric Plain Algebra*; the quadratic representation, the fundamental formula and the
  symmetries are *The Left and Right Multiplication Operators on a Jordan Algebra*; the trace form, its
  invariance and its restrictions are *The Trace Form and the Invariance of the Symmetric Plain Algebra*; and the
  general one-sided family is *The Jordan Multiplication Operators*.
- **Measurement, the classical composition and the Jordan algebra of observables are not this article's
  business.** They are *The Symmetrised Material Composition and the Jordan Identity* and *Observables as a
  Jordan Algebra: the Symmetric Plain Product and the Classical Composition*, whose claims are not repeated.
- **The physical adjoint is not the trace-form adjoint.** Self-adjointness for $\tau$ is a transpose statement
  about an indefinite form; the observables and the generators are the self-adjoint and the skew-adjoint
  operators for the Hermitian form, in *Observables, Gauge Generators and the Chirality of the Internal Action*,
  with the positivity in *Mass, Rank and the Positivity of the Dagger*.
- **The twelve adjoints are not compared here.** The comparison is the crossing reader *The Operators of the
  Twelve Structures: Multiplication, Adjoint and Bracket*, not one of the twelve; this article declares only the
  symmetrised plain column and its one point of contrast, the swap of the sides that this row cannot make.
- **The state space is cited.** The spinor module, its matrix units and its complement are *The Spinor Space as
  a Module and as a Hilbert Space* and *The Complementary Space of the Spinor Space and Its Physical Meaning*.

**What the framework does not claim.** The interpretation does not derive the classical composition or the measurement
update from the operator calculus; it names the operator behind two objects the band already uses. It does not
identify the trace-form adjoint with hermiticity — the two adjoints are different and coincide only on the
observables — and it does not claim a generator algebra inside the family: the family is symmetric and the
generators are its commutators.

## The Ledger

**Proved.** The product is commutative, so $L^{\bullet}_{\tilde A}=R^{\bullet}_{\tilde A} =\tfrac12(L_{\tilde A}+R_{\tilde A})$ and the band has one family; the composition is
$L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde B} =\tfrac14(L_{\tilde A\tilde B}+L_{\tilde A}R_{\tilde B}+R_{\tilde A}L_{\tilde B}+R_{\tilde B\tilde A})$, not
multiplicative, with associator deviation and witness $e_1,e_1,e_2$, and the Jordan identity on the operators is
$[L^{\bullet}_{\tilde X},L^{\bullet}_{\tilde X\bullet\tilde X}]=0$ with the fundamental formula; the trace form
$\tau=P_0Q_0-(\vec P,\vec Q)$ is symmetric, non-degenerate, invariant, of Gram $\mathrm{diag}(1,-1,-1,-1)$
and realified signature $(4,4)$, its associate **keeps the parameter**, $(L^{\bullet}_{\tilde A})^{\approx}=L^{\bullet}_{\tilde A}$,
and reverses a composite; every multiplication is self-adjoint for $\tau$, the only skew-adjoint one is zero, and
the commutators of the family are the inner derivations $\tfrac14\operatorname{ad}_{[\tilde A,\tilde B]}$, of
dimension three, each skew; the Hermitian dagger **conjugates the
parameter**, $(L^{\bullet}_{\tilde A})^{\dagger}=L^{\bullet}_{\tilde A^{*}}$, is self-adjoint exactly on
$\mathbb{M}_+$ and skew-adjoint exactly on $\mathbb{M}_-$; the sandwich is self-adjoint for $\tau$ for every
parameter, for the dagger exactly on the two sectors, and never skew; the form-preserving multiplications are
$\pm\mathrm{id}$, the form-preserving two-sided operators are the $\pm\mathrm{Ad}_{\tilde A}$ with
$\tilde B\tilde A=\pm e_0$, and $U_{\tilde A}$ is a form-isometry exactly at the elements of square $\pm e_0$;
the product-preserving operators are the inner automorphisms and the outer natural conjugation, and no
multiplication is a non-trivial automorphism; the observable sector is closed with self-adjoint multiplications
for the Born pairing and the cubic Peirce spectrum $\{0,\tfrac12,1\}$ at an idempotent; and the sandwich equals
the inner automorphism exactly on the symmetries and is minus it on the anti-symmetries.

**Interpretations.** That the adjoint **keeps the parameter** and that the swap of sides is impossible, one family
replacing two, which is the operator content of commutativity; that the order-free composition is
**self-paired**, the trace form being unable to distinguish a left attachment from a right one; that the
infinitesimal structure is not in the symmetric family but in its commutators, the inner derivations; that the
conjugation of a parameter is the dagger's property, not the trace-form adjoint's, and the two coincide on the
observables; that inside the family the form is preserved only at the two scalar signs, while an element of unit
square acts as an isometry through its sandwich; that the product-preserving relabellings are two-sided and
outside the family, the outer one being the natural conjugation; that a sharp question's operator is graded and
not a projector; and that on the state space the operator is the mean of the module action and the complementary
module map, the centre acting as a scalar. Each is the framework's naming of a proved algebraic fact and is
labelled as such.

## Physical Readings

The operators of the symmetrised plain product read as one family rather than two, and the interpretation of their
collapse is the band's job word. Where the general plain block has two distinct families and an adjoint that
exchanges them, here the commutativity of the composition makes them one, and the **physical interpretation** is that an
order-free composition has no orientation: nothing distinguishes an attachment on the left from one on the
right, and no transport can distinguish them either. The trace form is the scalar part of the product itself,
invariant and indefinite, and its adjoint is the identity on the family; the interpretation of the invariance is that
the pairing of two order-free compositions is itself order-free, which is the operator form of the classical
composition read in *Observables as a Jordan Algebra: the Symmetric Plain Product and the Classical Composition*.

Read on the types, every multiplication is symmetric for the trace form and none is a generator, so the band
supplies no infinitesimal operation of its own family; the generators are the order defects
$[L^{\bullet}_{\tilde A},L^{\bullet}_{\tilde B}]$, of dimension three, and the interpretation is that what is
infinitesimal in the block is the failure of two compositions to commute. The conjugation of a parameter belongs
to the Hermitian dagger, the adjoint of the physical form, and the interpretation is the sector dictionary: a Hermitian
parameter gives the observable, an anti-Hermitian one the generator, and on the observable sector the trace form
is the Born pairing, so the two adjoints agree exactly there. Read on the symmetries, the form is preserved by a
multiplication only at the two scalar signs, while an element of unit square acts as an isometry through its
sandwich; the interpretation is that the isometry of the band is the two-sided quadratic representation and not the
one-sided multiplication, and that the sandwich and the inner automorphism coincide exactly at the symmetries.
Read on the state space, the operator is the mean of the module action and a complementary module map and the
centre acts as a scalar; the interpretation is the invariance under a central phase and the statement that the state
space carries no phase of its own. Read on a sharp question, its operator has the three Peirce values and is not
a projector; the interpretation is that the answer is graded and that the classical two-valued projection is absent.
The distinctions are labelled throughout: what is proved is the algebra, what is proposed is the naming.

## Summary

The operators of the symmetrised plain product are one family, because the product is commutative: the left and
the right multiplication by an element coincide, $L^{\bullet}_{\tilde A}=R^{\bullet}_{\tilde A} =\tfrac12(L_{\tilde A}+R_{\tilde A})$, and the two-sided operator of the band is the quadratic representation
$U_{\tilde A}=2(L^{\bullet}_{\tilde A})^{2}-L^{\bullet}_{\tilde A\bullet\tilde A}$, acting by
$\tilde X\mapsto\tilde A\tilde X\tilde A$. The composition of two multiplications is the four-term mean of the
plain operators and is not a multiplication, the deviation being the associator with witness $e_1,e_1,e_2$; the
operator form of the Jordan identity is the commutation of the operator of an element with the operator of its
square, with the fundamental formula for the quadratic representations. The bilinear form of the block is the
trace form $\tau(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\bullet\tilde Q)=P_0Q_0-(\vec P,\vec Q)$,
symmetric, non-degenerate, invariant, of Gram $\mathrm{diag}(1,-1,-1,-1)$ and realified signature $(4,4)$; its adjoint **keeps the
parameter**, $(L^{\bullet}_{\tilde A})^{\approx}=L^{\bullet}_{\tilde A}$, and reverses a composite, so the band
has **no swap of sides**, the swap being impossible with one family. The conjugation of a parameter belongs to
the Hermitian dagger, $(L^{\bullet}_{\tilde A})^{\dagger}=L^{\bullet}_{\tilde A^{*}}$; every multiplication is
self-adjoint for the trace form and none is skew-adjoint, the commutators of the family being the inner
derivations $\tfrac14\operatorname{ad}_{[\tilde A,\tilde B]}$, of dimension three, each skew; the
dagger is self-adjoint exactly on the Hermitian sector and skew-adjoint exactly on the anti-Hermitian one; and
the sandwich is self-adjoint for the trace form for every parameter and for the dagger exactly on the two
sectors. The form-preserving multiplications are $\pm\mathrm{id}$, the form-preserving two-sided operators are
the $\pm\mathrm{Ad}_{\tilde A}$ with $\tilde B\tilde A=\pm e_0$, the product-preserving operators are the inner
automorphisms and the outer natural conjugation, and no multiplication is a non-trivial automorphism. On the
observable sector the multiplications are self-adjoint for the positive Born pairing, and at an idempotent the
operator has the cubic Peirce spectrum $\{0,\tfrac12,1\}$; on the state space it is the mean of the module
action and a complementary module map, the centre acting as a scalar; and the sandwich coincides with the inner
automorphism exactly on the symmetries, being minus it on the anti-symmetries. The adjoint keeps the parameter,
the swap is impossible, and the conjugation is the Hermitian dagger's: that one sentence is the band's operator
answer.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | The biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^{2}=-e_0$, $e_1e_2=e_3$ |
| $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ | The symmetrised plain product |
| $L^{\bullet}_{\tilde A}(\tilde Q)=\tilde A\bullet\tilde Q$ | The multiplication operator; $R^{\bullet}_{\tilde A}=L^{\bullet}_{\tilde A}$ |
| $L^{\bullet}_{\tilde A}=\tfrac12(L_{\tilde A}+R_{\tilde A})$ | The operator is the symmetric half of the plain ones |
| $L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde B}=\tfrac14(L_{\tilde A\tilde B}+L_{\tilde A}R_{\tilde B}+R_{\tilde A}L_{\tilde B}+R_{\tilde B\tilde A})$ | The composition law |
| $\mathrm{as}(\tilde A,\tilde B,\tilde X)=(\tilde A\bullet\tilde B)\bullet\tilde X-\tilde A\bullet(\tilde B\bullet\tilde X)$ | The associator; the deviation from multiplicativity |
| $[L^{\bullet}_{\tilde X},L^{\bullet}_{\tilde X\bullet\tilde X}]=0$ | The Jordan identity on the operators |
| $U_{\tilde A}=2(L^{\bullet}_{\tilde A})^{2}-L^{\bullet}_{\tilde A\bullet\tilde A}$ | The quadratic representation; $U_{\tilde A}\tilde X=\tilde A\tilde X\tilde A$ |
| $U_{U_{\tilde A}\tilde B}=U_{\tilde A}U_{\tilde B}U_{\tilde A}$, $U_{\tilde A}^{2}=U_{\tilde A\bullet\tilde A}$ | The fundamental formula and the square |
| $\tau(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\bullet\tilde Q)=P_0Q_0-(\vec P,\vec Q)$ | The trace form; Gram $\mathrm{diag}(1,-1,-1,-1)$ |
| $(L^{\bullet}_{\tilde A})^{\approx}=L^{\bullet}_{\tilde A}$ | The associate **keeps the parameter** |
| $(L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde B})^{\approx}=L^{\bullet}_{\tilde B}L^{\bullet}_{\tilde A}$ | Association reverses a composite |
| $(L^{\bullet}_{\tilde A})^{\dagger}=L^{\bullet}_{\tilde A^{*}}$ | The Hermitian dagger **conjugates the parameter** |
| self-adjoint for $\tau$: all $\tilde A$; skew for $\tau$: $\tilde A=0$ | The types for the trace form |
| $\dagger$-self-adjoint $\iff\tilde A\in\mathbb{M}_+$, $\dagger$-skew $\iff\tilde A\in\mathbb{M}_-$ | The types for the Hermitian dagger |
| $U_{\tilde A}$ $\dagger$-self-adjoint $\iff\tilde A\in\mathbb{M}_+\cup\mathbb{M}_-$ | The types of the sandwich |
| $[L^{\bullet}_{\tilde A},L^{\bullet}_{\tilde B}]=\tfrac14\operatorname{ad}_{[\tilde A,\tilde B]}$ | The inner derivations, of dimension three |
| $L^{\bullet}_{\tilde A}$ preserves $\tau\iff\tilde A=\pm e_0$ | The form-preserving multiplications |
| $\tilde B\tilde A=\pm e_0\iff L_{\tilde A}R_{\tilde B}=\pm\mathrm{Ad}_{\tilde A}$ | The form-preserving two-sided operators |
| $U_{\tilde A}$ preserves $\tau\iff\tilde A\bullet\tilde A=\pm e_0$ | The form-preserving quadratic representations |
| $L^{\bullet}_{\tilde A}$ multiplicative $\iff L^{\bullet}_{\tilde A}\in\{\mathrm{id},0\}$ | The multiplicative multiplications |
| $\mathrm{Ad}_{\tilde A}$ (inner), ${\natural}$ (outer) | The product-preserving operators |
| $U_{\tilde A}=\mathrm{Ad}_{\tilde A}\iff\tilde A\bullet\tilde A=e_0$ | The sandwich and the inner automorphism agree on the symmetries |
| $\mathbb{M}_+$ closed; $\tau|_{\mathbb{M}_+}=H$ positive definite | The observable sector and its Born pairing |
| $L^{\bullet}_{\tilde\Pi}(2L^{\bullet}_{\tilde\Pi}-\mathrm{id})(L^{\bullet}_{\tilde\Pi}-\mathrm{id})=0$ | The cubic Peirce identity; eigenvalues $\{0,\tfrac12,1\}$ |
| $S=\mathbb{B}\tilde\Pi_+$ | The spinor space; $L^{\bullet}_{\lambda e_0}=\lambda\,\mathrm{id}$ |

## Further Reading

- Mathematics article *The Multiplication Operators of the Symmetric Plain Algebra*
(`articles_maths/the-multiplication-operators-of-the-symmetric-plain-algebra.md`), for the one family, the
composition law, the self-associateness, the Jordan identity on the operators, the inner derivations, the
automorphisms and the structure group.
- Mathematics article *The Trace Form and the Invariance of the Symmetric Plain Algebra*
(`articles_maths/the-trace-form-and-the-invariance-of-the-symmetric-plain-algebra.md`), for the trace form, its
Gram matrix, its invariance, its realified signature and its restrictions.
- Mathematics article *The Left and Right Multiplication Operators on a Jordan Algebra*
(`articles_maths/the-left-and-right-multiplication-operators-on-a-jordan-algebra.md`), for the collapse of the
two families, the quadratic representation, the fundamental formula, the symmetries and the self-adjointness of
the quadratic representations.
- Mathematics article *The Jordan Multiplication Operators*
(`articles_maths/the-jordan-multiplication-operators.md`), for the one-sided family of a general Jordan algebra,
the multiplication algebra and the fundamental formula.
- Mathematics article *The Specificities of the Symmetric Plain Algebra*
(`articles_maths/the-specificities-of-the-symmetric-plain-algebra.md`), for the symmetric-half identity, the
cubic Peirce identity, the eigenvalues $\{0,\tfrac12,1\}$ and the absence of a projector from a non-trivial
idempotent.
- Mathematics article *Introduction to the Symmetric Plain Algebra of Biquaternions*
(`articles_maths/introduction-to-the-symmetric-plain-algebra-of-biquaternions.md`), for the product and its
place among the twelve structures.
- Physics article *The Symmetrised Material Composition and the Jordan Identity*
(`articles_physics/the-symmetrised-material-composition-and-the-jordan-identity.md`), the framing article of the
band, for the split of the general plain bilinear product, the operation and the Jordan identity.
- Physics article *Observables as a Jordan Algebra: the Symmetric Plain Product and the Classical Composition*
(`articles_physics/observables-as-a-jordan-algebra-the-symmetric-plain-product-and-the-classical-composition.md`),
for the closure of the Hermitian sector, the observables and the classical composition, which are the band's own
physics and not this article's.
- Physics article *Observables, Gauge Generators and the Chirality of the Internal Action*
(`articles_physics/observables-gauge-generators-and-the-chirality-of-the-internal-action.md`), for the physical
adjoint, the observables and the generators, which are the self-adjoint and the skew-adjoint operators for the
Hermitian form and not for the trace form.
- Physics article *Mass, Rank and the Positivity of the Dagger*
(`articles_physics/mass-rank-and-the-positivity-of-the-dagger.md`), for the positivity of the Hermitian form
that makes the sector a state structure.
- Physics article *The Spinor Space as a Module and as a Hilbert Space*
(`articles_physics/the-spinor-space-as-a-module-and-as-a-hilbert-space.md`), for the ideal, the matrix units of
the left action and the state space.
- Physics article *The Complementary Space of the Spinor Space and Its Physical Meaning*
(`articles_physics/the-complementary-space-of-the-spinor-space-and-its-physical-meaning.md`), for the right
multiplication as a module map and the complement.
- Physics article *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*
(`articles_physics/the-operators-of-the-twelve-structures-multiplication-adjoint-and-bracket.md`), the crossing
reader of the twelve operator rows, for the comparison of the twelve adjoints and the contrast with the general
plain column.
