
# __The Signed Adjoint of the Reflection on a Bimodule over an Algebra__

## Introduction

A reflection of a graded bimodule is the signed sandwich $r_u(x)=u\,\alpha(x)\,u^{-1}$ by a unit $u$, an operator of order two when $u\alpha(u)$ is central. This article computes the adjoint of a reflection with respect to an $\alpha$-invariant pairing and asks when a reflection is self-adjoint. The adjoint of $r_u$ is the reflection $r_{\beta(u)}$ by the parameter transformed by the composite $\beta=\alpha\sigma$, so the reflections are permuted by the adjoint; a reflection is self-adjoint exactly when its parameter is fixed by $\beta$, and this criterion fails in the degenerate case where distinct parameters give the same reflection.

The article is the fifth of the `* Operator Theory` group of this category. It assumes the reflections of *Reflections as Signed Two-Sided Operators on a Bimodule over an Algebra*, the signed sandwich and its adjoint from *The Signed Sandwich on a Bimodule over an Algebra* and *The Signed Adjoint of the Sandwich on a Bimodule over an Algebra*, and the self-adjoint and unitary elements of *Module Operators with an Involution*. It is the operator-level counterpart, for the graded bimodule, of *The Adjoint of the Sandwich on a Bimodule over an Algebra*, and the one-sided partner is *The Signed Adjoint of the Left Multiplication on a Module over an Algebra*. The article stays inside Part I: no distance, norm, angle, form with a norm, topology or limit; a reflection means an operator of order two, with no geometric reading. Throughout, $R$ is a commutative ring with $1 \neq 0$ in which $2$ is invertible, $(A,\sigma)$ is an involutive $R$-algebra, $\alpha$ is a grade involution of $A$ commuting with $\sigma$, $\beta=\alpha\sigma$, ${}_A M_A$ is a graded $(A,A)$-bimodule with $\alpha$-invariant balanced $\sigma$-sesquilinear pairing, and for a unit $u \in A^{\times}$ the reflection is $r_u=S^{\alpha}_{u,u^{-1}}$, $r_u(x)=u\,\alpha(x)\,u^{-1}$.

## The Reflection and Its Adjoint

### The reflection recalled

**Definition.** For a unit $u \in A^{\times}$ the **reflection** with parameter $u$ is the signed sandwich

$$
r_u=S^{\alpha}_{u,u^{-1}}, \qquad r_u(x)=u\,\alpha(x)\,u^{-1} .
$$

**Proposition.** The square of a reflection is the inner conjugation by $u\alpha(u)$,

$$
r_u^{2}=S_{u\alpha(u),\,(u\alpha(u))^{-1}}=\operatorname{conj}_{u\alpha(u)},
$$

so $r_u$ is an operator of order two, a genuine reflection, exactly when $u\alpha(u)$ is central in $A$.

*Proof.* This is *Reflections as Signed Two-Sided Operators on a Bimodule over an Algebra*. $\square$

The two conditions in play are therefore distinct from the outset: $r_u^{2}=\mathrm{id}$ asks $u\alpha(u)$ central, while self-adjointness below asks $\beta(u)=u$ up to centrality. Neither implies the other.

### The adjoint of a reflection

**Theorem.** The adjoint of a reflection is the reflection by the parameter transformed by $\beta=\alpha\sigma$:

$$
(r_u)^{*}=r_{\beta(u)}, \qquad \beta(u)=\alpha(\sigma(u)) .
$$

*Proof.* The adjoint of a signed sandwich is $\bigl(S^{\alpha}_{a,b}\bigr)^{*}=S^{\alpha}_{\beta(a),\beta(b)}$ by *The Signed Adjoint of the Sandwich on a Bimodule over an Algebra*; for $(a,b)=(u,u^{-1})$ this is $S^{\alpha}_{\beta(u),\beta(u^{-1})}$, and $\beta(u^{-1})=\beta(u)^{-1}$, so the adjoint is $r_{\beta(u)}$. $\square$

**Corollary.** The adjoint permutes the set of reflections: $\{r_u\}^{*}=\{r_u\}$, and the permutation is the map $u \mapsto \beta(u)$ on the parameters. Since $\beta$ is an involution, the adjoint acts on the reflections as an involution on the parameters, and $(r_u)^{**}=r_{\beta^{2}(u)}=r_u$.

*Proof.* The adjoint of $r_u$ is $r_{\beta(u)}$, and $\beta^{2}=\mathrm{id}$ because $\alpha$ and $\sigma$ commute, so the two applications return $r_u$; the bijection $u\mapsto\beta(u)$ of $A^{\times}$ has inverse itself. $\square$

The reflection adjoint formula is the module-level form of the statement that conjugating by $u$ and taking adjoints uses the involution on the parameter; it is the same identity as $(L_a)^{*}=L_{\sigma(a)}$ for the one-sided case, with the grading inserted.

## Self-Adjointness of a Reflection

### The criterion

**Definition.** A reflection $r_u$ is **self-adjoint** when $(r_u)^{*}=r_u$. Its parameter $u$ is **$\beta$-symmetric** when $\beta(u)=u$; more generally $u$ is $\beta$-symmetric modulo the centre when $\beta(u)u^{-1} \in Z(A)$.

**Theorem.** If the map $u \mapsto r_u$ is injective on $A^{\times}$, then a reflection is self-adjoint exactly when its parameter is $\beta$-symmetric:

$$
(r_u)^{*}=r_u \iff \beta(u)=u \iff \alpha\sigma(u)=u .
$$

*Proof.* By the adjoint formula, $(r_u)^{*}=r_u$ is $r_{\beta(u)}=r_u$, which by injectivity is $\beta(u)=u$. $\square$

**Corollary.** The $\beta$-symmetric units form a subgroup $A^{\times}_{\beta}=\{u \in A^{\times} : \beta(u)=u\}$ of the unit group, because $\beta$ is an involution of the algebra, and the reflection map restricts to a map $A^{\times}_{\beta}\to\{r_u : (r_u)^{*}=r_u\}$ onto the self-adjoint reflections when the parameter map is injective. The restriction is multiplicative only when $u\alpha(v)$ is central for all $u,v \in A^{\times}_{\beta}$, as it is in a commutative algebra; in general the product of two reflections is a conjugation and not a reflection.

*Proof.* $A^{\times}_{\beta}$ is a subgroup because $\beta$ is an algebra automorphism with $\beta^{2}=\mathrm{id}$; the image lies in the self-adjoint reflections by the theorem; the product $r_ur_v=S_{u\alpha(v),\,\alpha(v)^{-1}u^{-1}}$ is a reflection exactly when $u\alpha(v)$ is central, by the criterion for a diagonal sandwich to be a reflection. $\square$

The corollary stops short of a group isomorphism, because $r_ur_v$ is a reflection only under the centrality condition; the self-adjoint reflections therefore do not automatically form a group.

### Self-adjointness and the order of the reflection

**Proposition.** The two conditions

$$
\text{order two: } r_u^{2}=\mathrm{id} \iff u\alpha(u) \in Z(A), \qquad \text{self-adjoint: } (r_u)^{*}=r_u \iff \beta(u)=u,
$$

are independent: either can hold without the other.

*Proof.* Order two is $u\alpha(u)\in Z(A)$ and self-adjointness is $\alpha\sigma(u)=u$; these involve $u\alpha(u)$ and $\alpha\sigma(u)$ respectively, and neither condition forces the other, as the examples below show. $\square$

**Example.** For $\sigma=\mathrm{id}$ and $\alpha\neq\mathrm{id}$, self-adjointness is $\alpha(u)=u$ while order two is $u\alpha(u)\in Z(A)$; an element of even degree that is central is self-adjoint of order larger than two under $r$, and an odd element of order two in the grading satisfies order two without being self-adjoint.

In particular a self-adjoint reflection need not be a genuine reflection, and a genuine reflection need not be self-adjoint; the two properties are the "graded" analogue of the fact that a symmetric operator need not be an involution.

## Failure in the Degenerate Case

### Non-injective parameters

**Proposition.** For the regular bimodule $M={}_A A_A$ the parameters of a reflection are determined modulo the centre:

$$
r_u=r_v \iff v^{-1}u \in Z(A) .
$$

*Proof.* $r_u=r_v$ is $u\alpha(x)u^{-1}=v\alpha(x)v^{-1}$ for all $x$, that is $w\alpha(x)=\alpha(x)w$ for all $x$ with $w=v^{-1}u$. Since $\alpha$ is onto, this is $wx=xw$ for all $x$, that is $w\in Z(A)$. $\square$

**Theorem (the criterion in general).** Without injectivity of $u \mapsto r_u$ the self-adjointness criterion is the congruence

$$
(r_u)^{*}=r_u \iff \beta(u)u^{-1} \in Z(A),
$$

where $Z(A)$ is replaced by the centraliser of $M$ in $A$ when $M$ is not faithful.

*Proof.* $(r_u)^{*}=r_{\beta(u)}$ and $r_{\beta(u)}=r_u$ is $\beta(u)u^{-1}$ in the centraliser, by the same computation as in the proposition with $v=u$, $w=u^{-1}\beta(u)$. $\square$

So a reflection can be self-adjoint although its parameter is not $\beta$-symmetric, when the two parameters differ by a central element; the criterion $\beta(u)=u$ is the special case of an injective parameter map.

### The commutative case

**Proposition.** If $A$ is commutative then every reflection equals the grade involution,

$$
r_u=\alpha \quad (u \in A^{\times}),
$$

the parameter map $u \mapsto r_u$ is constant, and every reflection is self-adjoint, $(r_u)^{*}=\alpha^{*}=\alpha=r_u$.

*Proof.* In a commutative algebra $u$ commutes with $\alpha(x)$, so $u\alpha(x)u^{-1}=\alpha(x)$; the adjoint of $\alpha$ is $\alpha$ by the $\alpha$-invariance of the pairing. $\square$

The commutative case is the extreme degeneracy: the reflections collapse to a single self-adjoint operator, and the criterion $\beta(u)=u$ is vacuous. This is why the self-adjointness statement must be formulated modulo the centraliser and not as a condition on the parameter alone.

### The degenerate pairing

**Proposition.** If the pairing is not $\alpha$-invariant then $\alpha^{*}\neq\alpha$ and $(r_u)^{*}=\alpha^{*}S_{\sigma(u),\sigma(u)^{-1}}$, which need not be a reflection; in this case the adjoint of a reflection need not be a reflection at all.

*Proof.* The adjoint of a signed sandwich is $\alpha^{*}S_{\sigma(a),\sigma(b)}$ without invariance; for a reflection this is $\alpha^{*}r'$ with $r'$ the reflection by $\sigma(u)$ in the unsigned sense, and $\alpha^{*}r'$ is a reflection only when $\alpha^{*}$ is a signed sandwich, which fails when $\alpha$ is not self-adjoint. $\square$

## Unitarity and the Self-Adjoint Reflections

### Unitary reflections

**Proposition.** A reflection is unitary exactly when its parameter is a unitary element of $A$:

$$
r_u^{*}r_u=r_ur_u^{*}=\mathrm{id} \iff \sigma(u)u=u\sigma(u)=1 .
$$

*Proof.* This is the unitarity criterion of *The Signed Adjoint of the Sandwich on a Bimodule over an Algebra* with $(a,b)=(u,u^{-1})$. $\square$

### Self-adjoint unitary reflections

**Proposition.** A reflection is simultaneously self-adjoint and unitary exactly when its parameter is unitary and $\beta$-symmetric:

$$
(r_u)^{*}=r_u \text{ and } r_u^{*}r_u=r_ur_u^{*}=\mathrm{id} \iff \sigma(u)u=u\sigma(u)=1 \text{ and } \beta(u)=u .
$$

A simultaneously self-adjoint and unitary reflection is automatically of order two, and its parameter is a $\beta$-symmetric unitary element; the unitaries of $A$ that are $\beta$-symmetric form a subgroup of the unitary group of $A$ on which the reflection map is defined, and the unitary group generated by the simultaneously self-adjoint and unitary reflections consists of their products, an even number at a time.

*Proof.* Combine the unitarity criterion with the self-adjointness criterion. If $r_u^{*}=r_u$ and $r_u^{*}r_u=\mathrm{id}$ then $r_u^{2}=\mathrm{id}$, so the operator is of order two. The $\beta$-symmetric unitaries are closed under multiplication because $\beta$ is an algebra automorphism and the unitary elements of $A$ form a group. $\square$

The self-adjoint unitary reflections are the "graded orthogonal" operators of the bimodule: they preserve the pairing and are fixed by the involution, and their parameters are the unitary elements fixed by $\beta$.

## Examples

**(a) The trivial grading.** For $\alpha=\mathrm{id}$ the reflection is the inner conjugation $r_u(x)=uxu^{-1}$, $\beta=\sigma$, $(r_u)^{*}=r_{\sigma(u)}$, and $r_u$ is self-adjoint exactly when $\sigma(u)=u$: the conjugation by a symmetric unit.

**(b) The trivial involution.** For $\sigma=\mathrm{id}$ and a nontrivial grading, $(r_u)^{*}=r_{\alpha(u)}$, so a reflection is self-adjoint exactly when its parameter is even, $\alpha(u)=u$, and the self-adjoint reflections are the conjugations by even units.

**(c) The commutative algebra.** For $A$ commutative every reflection is $\alpha$; the parameter map is constant and the self-adjointness is automatic.

**(d) The Clifford algebra.** For a Clifford algebra with its canonical involution $\sigma$ and grade involution $\alpha$, the reflection $r_v$ by a unit versor $v$ has adjoint $r_{\alpha\sigma(v)}$, and it is self-adjoint exactly when $\alpha\sigma(v)=v$; the standard examples of self-adjoint reflections are the conjugations by vectors, which have $v\alpha(v)=\pm1$ central and are of order two.

**(e) A matrix algebra.** For $A=M_n(k)$ with the transpose involution $\sigma$ and a diagonal grading $\alpha$, $(r_u)^{*}=r_{\beta(u)}$ with $\beta(X)=\alpha(X^{\mathsf{T}})$; the self-adjoint reflections are those with $\alpha(u)=u^{\mathsf{T}}$, the graded-symmetric units.

## Summary

For a graded bimodule with an $\alpha$-invariant balanced $\sigma$-sesquilinear pairing, the adjoint of the reflection $r_u(x)=u\alpha(x)u^{-1}$ is the reflection $r_{\beta(u)}$ by the composite $\beta=\alpha\sigma$, so the adjoint permutes the reflections and acts on the parameters as the involution $\beta$. When the parameter map $u \mapsto r_u$ is injective, a reflection is self-adjoint exactly when $\beta(u)=u$; in general the criterion is $\beta(u)u^{-1}\in Z(A)$ — that is, $\beta(u)$ and $u$ differ by a central element — and in the commutative case all reflections collapse to the grade involution and all are self-adjoint. Self-adjointness and being an operator of order two are independent conditions, the first involving $\beta(u)=u$ and the second $u\alpha(u)$ central. A reflection is unitary exactly when its parameter is unitary, and it is simultaneously self-adjoint and unitary exactly when the parameter is unitary and $\beta$-symmetric; these are the graded isometries among the reflections. If the pairing is not $\alpha$-invariant the adjoint of a reflection need not be a reflection, the failure being governed by the adjoint of the grade involution.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $(A,\sigma)$ | base ring, involutive $R$-algebra |
| $\alpha$ | grade involution, commuting with $\sigma$ |
| $\beta=\alpha\sigma$ | the composite involution |
| $r_u=S^{\alpha}_{u,u^{-1}}$ | the reflection, $r_u(x)=u\alpha(x)u^{-1}$ |
| $r_u^{2}=S_{u\alpha(u),(u\alpha(u))^{-1}}$ | the square is a conjugation |
| $(r_u)^{*}=r_{\beta(u)}$ | the adjoint of the reflection |
| $\beta(u)=u$ | the $\beta$-symmetry of the parameter |
| $\beta(u)u^{-1}\in Z(A)$ | the self-adjointness criterion in general |
| $\sigma(u)u=u\sigma(u)=1$ | unitarity of the parameter |
| $A^{\times}_{\beta}$ | the $\beta$-symmetric units |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for graded algebras, involutions and reflections.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for graded involutions and their symmetric elements.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the reflections and the versor conjugation of a Clifford algebra.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for conjugations, centralisers and the degenerate behaviour of reflection parameters.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, second edition, 2001), for the unitarity conditions and the centraliser computations over rings.
