# __The Signed Adjoint of the Reflection on an Algebra__

## Introduction

A reflection of an algebra with respect to a grade involution $\alpha$ is a signed conjugation $\rho_u(x)=u\,\alpha(x)\,u^{-1}$ of order two, the signed sandwich $S_{u,u^{-1}}$ of a **reflector** $u$, a unit whose product $u\alpha(u)$ is central. This article computes its adjoint: the twisted adjoint of the reflection by $u$ is the reflection by $\delta(u)=\sigma\alpha(u)$,

$$
\rho_u^{*_\sigma}=\rho_{\delta(u)}, \qquad \text{and for the plain pairing} \qquad \rho_u^{*}=\rho_{\alpha(u)},
$$

so the adjoint operation acts on the reflections by applying an anti-automorphism to the reflector. The reflection is self-adjoint for the twisted pairing exactly when $u^{-1}\delta(u)$ is central, that is when $\delta(u)$ is a central multiple of $u$, and this condition fails in interesting cases: it is automatic in the commutative algebras and when $\delta=\mathrm{id}$, and it is a genuine restriction for a matrix algebra with a non-symmetric reflector.

This article develops the adjoint of a reflection, the criterion for its self-adjointness, the cases in which the criterion is automatic, the unitary reflections beside the self-adjoint ones, and the interaction of the adjoint with the fixed subalgebra of the reflection. It assumes *Reflections as Signed Two-Sided Operators on an Algebra* for the reflectors $R^{\times}(A,\alpha)$ and the reflections $\mathrm{Ref}(A,\alpha)$, *The Signed Sandwich on an Algebra* for the signed conjugation and the relation $\rho_u^{2}=\iota_{u\alpha(u)}$, *The Signed Adjoint Sandwich on an Algebra* for the signed adjoint and the unitarity condition, *The Adjoint of the Left Multiplication on an Algebra* for the one-sided adjoints, *Involutions of the Operator Algebra* and *The Adjoint in an Involutive Algebra* for the adjoint operation and the two pairings, and *Involutive Bilinear Algebras* for the involutions. The graded reading is *The Graded Adjoint Action on a Module over an Algebra*; the geometric reflection and the metric form are Part II and *Hilbert Algebras* and *Quadratic Forms and Clifford Algebras*, named as the owner and not used. This article stays inside Part I: no distance, norm, form with a norm, topology or limit.

Throughout, $k$ is a field of characteristic not two, $A$ is a finite-dimensional unital associative $k$-algebra, $\tau$ is a trace whose pairing $\langle x,y\rangle=\tau(xy)$ is nondegenerate, $\sigma$ is an involution of $A$ with $\tau(\sigma(x))=\tau(x)$, and $\alpha$ is an involutive automorphism of $A$ commuting with $\sigma$ and preserving the trace. The twist is $\delta=\sigma\alpha$, the twisted pairing is $\{x,y\}=\tau(x\sigma(y))$, the unsigned sandwich is $T_{a,b}(x)=axb$, the signed sandwich is $S_{a,b}(x)=a\alpha(x)b$, the reflector is a unit $u$ with $u\alpha(u)\in Z(A)$, and the reflection is $\rho_u=S_{u,u^{-1}}$.

## The Adjoint of a Reflection

**Theorem.** Let $u$ be a reflector, so that $\rho_u$ is an involutive automorphism. Then $\delta(u)$ is again a reflector, and

$$
\rho_u^{*_\sigma}=S_{\delta(u),\,\delta(u)^{-1}}=\rho_{\delta(u)}, \qquad \rho_u^{*}=S_{\alpha(u)^{-1},\,\alpha(u)}=\rho_{\alpha(u)} .
$$

The twisted adjoint of the reflection by $u$ is the reflection by $\delta(u)$, and the plain adjoint is the reflection by $\alpha(u)$; both are reflections, and the adjoint operation carries the reflection set into itself.

*Proof.* The twisted adjoint of a signed sandwich is $S_{a,b}^{*_\sigma}=S_{\delta(a),\delta(b)}$ by *The Signed Adjoint Sandwich on an Algebra*; with $a=u$ and $b=u^{-1}$ this is $S_{\delta(u),\delta(u^{-1})}$, and $\delta(u^{-1})=\delta(u)^{-1}$ because $\delta$ is an anti-automorphism of order two. The result is the signed conjugation by $\delta(u)$, that is $\rho_{\delta(u)}$. For the plain pairing the adjoint of a signed sandwich is $S_{\alpha(b),\alpha(a)}$, which with $a=u$ and $b=u^{-1}$ is $S_{\alpha(u)^{-1},\alpha(u)}=\rho_{\alpha(u)}$. That $\delta(u)$ is a reflector: $\delta(u)\alpha(\delta(u))=\sigma(\alpha(u))\alpha(\sigma(\alpha(u)))=\sigma(\alpha(u))\sigma(u)=\sigma(u\alpha(u))$, which is central exactly when $u\alpha(u)$ is central, the involution $\sigma$ preserving centrality and being onto; so $\rho_{\delta(u)}$ is an involutive automorphism. That $\alpha(u)$ is a reflector is the same computation with $\delta$ replaced by $\alpha$: $\alpha(u)\alpha(\alpha(u))=\alpha(u)u=u\alpha(u)$, central.

**Corollary.** The adjoint operation acts on the set of reflections by the anti-automorphism $\delta$ for the twisted pairing and by the automorphism $\alpha$ for the plain one, and

$$
(\rho_u^{*_\sigma})^{*_\sigma}=\rho_u, \qquad (\rho_u^{*})^{*}=\rho_u,
$$

so the action is an involution of the reflection set; the reflection by $1$ is $\alpha$, and it is fixed by both adjoints.

*Proof.* Order two is the order two of the adjoint operation and of $\delta$, respectively $\alpha$; the case $u=1$ gives $\rho_1=\alpha$, and $\alpha$ is self-adjoint for both pairings by *The Signed Adjoint Sandwich on an Algebra*.

## Self-Adjointness

**Theorem.** A reflection $\rho_u$ is self-adjoint for the twisted pairing exactly when

$$
u^{-1}\delta(u) \in Z(A),
$$

and self-adjoint for the plain pairing exactly when $u^{-1}\alpha(u) \in Z(A)$. Equivalently, $\rho_u^{*_\sigma}=\rho_u$ exactly when $\delta(u)=\lambda u$ for some central $\lambda \in Z(A)$.

*Proof.* Two signed conjugations by units $u$ and $v$ agree as operators exactly when $u^{-1}v$ is central: $\rho_v=\rho_u$ is $v\alpha(x)v^{-1}=u\alpha(x)u^{-1}$ for all $x$, that is $u^{-1}v\alpha(x)=\alpha(x)u^{-1}v$ for all $x$, and since $\alpha$ is onto this is the centrality of $u^{-1}v$. Applying this to the theorem gives the criterion with $v=\delta(u)$, respectively $v=\alpha(u)$; the last form is $\delta(u)=u\lambda$ with $\lambda=u^{-1}\delta(u)$ central.

**Corollary.** If the reflector $u$ is central then $\rho_u$ is self-adjoint for both pairings, since $\delta(u)$ and $\alpha(u)$ are then central as well and the quotients are central. If $u$ is fixed by $\delta$, respectively by $\alpha$, then the reflection is self-adjoint for the corresponding pairing.

*Proof.* A central $u$ has $u^{-1}\delta(u)$ central as the product of central elements, and a fixed $u$ has the quotient $1$, which is central.

**Corollary (the reflection and the twisted involution).** The reflection is self-adjoint for the twisted pairing if and only if the difference $\delta(u)-u$ is a central multiple of $u$, and the self-adjoint reflections by reflectors of the form $u=\lambda v$ with $\lambda$ central are exactly the reflections of the $v$ with $\delta(v)=v$; in particular the self-adjointness depends only on the reflector class modulo the central units.

*Proof.* $\delta(\lambda v)=\delta(v)\sigma(\lambda)$ for a central $\lambda$; for the twisted pairing and a central reflector the centrality bookkeeping is the statement that $\rho_{\lambda v}=\rho_{v}$ up to the central factor, and the criterion $u^{-1}\delta(u)$ central is unchanged when $u$ is multiplied by a central unit.

## The Degenerate Cases

**Theorem (the grade involution is the identity).** If $\alpha=\mathrm{id}$ then the reflections are the inner involutions $\rho_u(x)=uxu^{-1}$ with $u^{2}$ central, $\rho_u^{*_\sigma}=\rho_{\sigma(u)}$ and $\rho_u^{*}=\rho_u$; every reflection is self-adjoint for the plain pairing, and it is self-adjoint for the twisted pairing exactly when $u^{-1}\sigma(u)$ is central.

*Proof.* With $\alpha=\mathrm{id}$ the signed sandwich is the unsigned one and the signed conjugation is the inner automorphism; the reflector condition $u\alpha(u)=u^{2}\in Z(A)$ is the classical one, and the two adjoint formulas specialize to $\rho_{\sigma(u)}$ and $\rho_{\alpha(u)}=\rho_u$. The last statement is the self-adjointness criterion with $\alpha=\mathrm{id}$.

**Theorem (the anti-automorphism is the grade involution).** If $\delta=\mathrm{id}$, equivalently $\sigma=\alpha$, then every signed sandwich is self-adjoint for the twisted pairing, $S_{a,b}^{*_\sigma}=S_{a,b}$, and in particular every reflection is self-adjoint. The case occurs exactly when $\sigma=\alpha$ and the algebra is commutative.

*Proof.* The twisted adjoint of a signed sandwich is $S_{\delta(a),\delta(b)}$, which is $S_{a,b}$ when $\delta=\mathrm{id}$; the equation $\sigma=\alpha$ between an anti-automorphism and an automorphism gives $\alpha(x)\alpha(y)=\alpha(y)\alpha(x)$ for all $x,y$, so the image of $\alpha$, which is $A$, is commutative, and conversely in a commutative algebra the identity is both an automorphism and an anti-automorphism.

**Theorem (the commutative algebra).** If $A$ is commutative then every unit is a reflector, every reflection is the grade involution $\alpha$, and every reflection is self-adjoint for both pairings.

*Proof.* In a commutative algebra $u\alpha(u)$ is central for every unit $u$, and $\rho_u(x)=u\alpha(x)u^{-1}=\alpha(x)$ because $u$ commutes with everything; the reflections are therefore all equal to $\alpha$, which is self-adjoint, and the general criterion is automatic because every element is central.

The two theorems describe the failure of the self-adjointness criterion as a degeneracy: it holds trivially when the algebra is commutative or when the twist $\delta$ is the identity, and it is a genuine condition only for a noncommutative algebra with $\delta\neq\mathrm{id}$. In that non-degenerate case the reflectors split into those whose reflection is self-adjoint and those whose reflection is not, and the split is by the criterion $u^{-1}\delta(u)\in Z(A)$.

## The Unitary Reflections

**Theorem.** A reflection is unitary for the twisted pairing exactly when $\sigma(u)u$ is central and fixed by $\alpha$; a reflection that is both self-adjoint and unitary satisfies $\rho_u^{2}=\mathrm{id}$ as an operator and $\rho_u^{*_\sigma}=\rho_u=\rho_u^{-1}$.

*Proof.* The unitarity criterion is the corollary of *The Signed Adjoint Sandwich on an Algebra* for $b=\alpha(a)^{-1}$, that is $\sigma(u)u\in Z(A)$ and $\alpha(\sigma(u)u)=\sigma(u)u$. A self-adjoint unitary operator has $T^{*}=T$ and $T^{*}=T^{-1}$, so $T=T^{-1}$; for the reflection, $T^{2}=\mathrm{id}$ holds by the reflector condition.

**Corollary.** For a reflection that is self-adjoint, the unitarity is the condition that $\sigma(u)u$ be a central element of the even part; the orthogonal reflections of a matrix algebra with the transpose are the case in which $\sigma(u)u$ is a scalar.

*Proof.* The centrality and the $\alpha$-fixedness are the two clauses of the criterion, and an element fixed by the grade involution is even; for the matrix algebra with the transpose, a scalar $\sigma(u)u$ is central and fixed.

## The Fixed Subalgebra of a Reflection

**Theorem.** Let $u$ be a reflector. The fixed set of the reflection,

$$
\mathrm{Fix}(\rho_u)=\{x\in A : u\,\alpha(x)=x\,u\},
$$

is a unital subalgebra of $A$, on which $\rho_u$ acts as the identity, and it contains the central elements fixed by the grade involution. The reflection preserves the trace and the plain pairing of the category,

$$
\tau(\rho_u(x))=\tau(x), \qquad \langle \rho_u(x),\rho_u(y)\rangle=\langle x,y\rangle ,
$$

so a reflection is an automorphism of the algebra that is also an automorphism of its pairing.

*Proof.* The reflection is a signed conjugation by the unit $u$, hence an automorphism, so its fixed set is a subalgebra; the unit is fixed because $\rho_u(1)=u\alpha(1)u^{-1}=uu^{-1}=1$, and a central $z$ with $\alpha(z)=z$ satisfies $u\alpha(z)=uz=zu$. For the trace, $\tau(u\alpha(x)u^{-1})=\tau(\alpha(x)u^{-1}u)=\tau(\alpha(x))=\tau(x)$ by the cyclic property and the invariance of $\tau$ under $\alpha$; then $\langle\rho_u(x),\rho_u(y)\rangle=\tau(u\alpha(x)u^{-1}u\alpha(y)u^{-1})=\tau(u\alpha(xy)u^{-1})=\tau(\alpha(xy))=\tau(xy)$, using the multiplicativity of $\alpha$ and the trace computation again.

**Corollary.** The fixed subalgebra of the twisted adjoint is the fixed subalgebra of the reflected reflector, $\mathrm{Fix}(\rho_u^{*_\sigma})=\mathrm{Fix}(\rho_{\delta(u)})$, and that of the plain adjoint is $\mathrm{Fix}(\rho_u^{*})=\mathrm{Fix}(\rho_{\alpha(u)})$; hence self-adjointness is sufficient for the equality of the fixed subalgebras, $\rho_u^{*_\sigma}=\rho_u$ implying $\mathrm{Fix}(\rho_u)=\mathrm{Fix}(\rho_{\delta(u)})$, and the criterion $u^{-1}\delta(u)\in Z(A)$ of the earlier section gives the exact condition.

*Proof.* The adjoints are the reflections $\rho_{\delta(u)}$ and $\rho_{\alpha(u)}$ by the theorem of the first section, and their fixed sets are computed as above; two equal operators have equal fixed sets, which is the implication.

## Examples

**(a) The matrix algebra with the transpose.** $A=M_n(k)$, $\sigma$ the transpose, $\alpha$ the grade involution of a $\mathbb{Z}/2$-grading; a reflector $u$ has $\rho_u^{*_\sigma}=\rho_{\delta(u)}$ and $\rho_u$ is self-adjoint exactly when $\delta(u)$ is a scalar multiple of $u$. For $\alpha=\mathrm{id}$ this is the condition $u^{\mathsf{T}}=\lambda u$ with $\lambda$ scalar, the symmetry of $u$ up to a scalar; a generic reflector fails it.

**(b) The group algebra with a parity.** $A=k[G]$ with a parity homomorphism $\chi$ and $\sigma(g)=g^{-1}$; a reflector is a group element $g$ with $g\alpha(g) = \chi(g)\,g^{2}$ central, and $\rho_g^{*_\sigma}=\rho_{\delta(g)}$ with $\delta(g)=\chi(g)g^{-1}$. The reflection is self-adjoint exactly when $g^{-1}\delta(g)=\chi(g)g^{-2}$ is central, that is when $g^{2}\in Z(k[G])$, since $\chi(g)$ is the scalar $\pm1$.

**(c) The Clifford algebra.** For a Clifford algebra with its grading and an odd element $v$ of square a scalar, the reflection $\rho_v$ is the reflection in the vector $v$; it is self-adjoint for the twisted pairing when $\sigma(v)v$ is central, and the classical statement that a vector reflection is self-adjoint for the bilinear form is the case in which that product is a scalar. The metric reading of the form is Part II.

**(d) The commutative case.** For a commutative algebra every reflection is the grade involution and is self-adjoint for both pairings, so the criterion of this article is vacuous; this is the extreme degenerate case, and it shows that the self-adjointness is a condition on the noncommutativity of the algebra as much as on the reflection.

## Summary

The reflection $\rho_u=S_{u,u^{-1}}$ by a reflector $u$ has twisted adjoint $\rho_u^{*_\sigma}=\rho_{\delta(u)}$ and plain adjoint $\rho_u^{*}=\rho_{\alpha(u)}$, and both are again reflections, so the adjoint operation acts on the reflection set by the two order-two maps $\delta$ and $\alpha$; the reflection by $1$ is the grade involution $\alpha$, self-adjoint for both pairings. The reflection is self-adjoint for the twisted pairing exactly when $u^{-1}\delta(u)$ is central, equivalently when $\delta(u)$ is a central multiple of $u$, and for the plain pairing exactly when $u^{-1}\alpha(u)$ is central; central reflectors and reflectors fixed by the twist always give self-adjoint reflections. The criterion is automatic in the degenerate cases — $\alpha=\mathrm{id}$, where the reflections are the inner involutions; $\delta=\mathrm{id}$, where every signed sandwich is self-adjoint; and the commutative algebras, where every reflection is the grade involution — and it is a genuine condition only for a noncommutative algebra with $\delta\neq\mathrm{id}$. A reflection is unitary for the twisted pairing exactly when $\sigma(u)u$ is central and even, and a reflection that is both self-adjoint and unitary is its own inverse adjoint. The fixed set of a reflection is a unital subalgebra, it contains the central elements fixed by the grade involution, and the reflection preserves the trace and the plain pairing of the category; self-adjointness forces the fixed subalgebra of the twisted adjoint to coincide with that of the reflection. The geometric reflection and the metric form are Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S_{a,b}(x)=a\alpha(x)b$ | the signed sandwich |
| $\rho_u=S_{u,u^{-1}}$, $\rho_u(x)=u\alpha(x)u^{-1}$ | the reflection by the reflector $u$ |
| $R^{\times}(A,\alpha)$, $\mathrm{Ref}(A,\alpha)$ | the reflectors and the reflections |
| $\alpha$, $\sigma$, $\delta=\sigma\alpha$ | the grade involution, the involution, and their twist |
| $\rho_u^{*_\sigma}=\rho_{\delta(u)}$ | the twisted adjoint of a reflection |
| $\rho_u^{*}=\rho_{\alpha(u)}$ | the plain adjoint of a reflection |
| $u^{-1}\delta(u)\in Z(A)$ | self-adjointness for the twisted pairing |
| $u^{-1}\alpha(u)\in Z(A)$ | self-adjointness for the plain pairing |
| $\mathrm{Fix}(\rho_u)=\{x:u\alpha(x)=xu\}$ | the fixed subalgebra of a reflection |
| $\tau(\rho_u(x))=\tau(x)$, $\langle\rho_ux,\rho_uy\rangle=\langle x,y\rangle$ | a reflection preserves the trace and the pairing |
| $\alpha=\mathrm{id}$ | the reflections are the inner involutions |
| $\delta=\mathrm{id}$ | every signed sandwich is self-adjoint |
| $\sigma(u)u\in Z(A)$, $\alpha$-fixed | the unitary reflections |

## Further Reading

- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the conjugations, the reflections and the two-sided operators of the regular representation.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the adjoint of a conjugation and the unitary elements.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for the unitary groups and the involutions of an algebra with involution.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras* (Springer, 1997), for the reflections realised by signed conjugations and their adjoint properties.
