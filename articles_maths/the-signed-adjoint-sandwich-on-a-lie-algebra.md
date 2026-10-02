
# __The Signed Adjoint Sandwich on a Lie Algebra__

## Introduction

The **adjoint** of an operator on a Lie algebra is taken with respect to the invariant Hermitian form of the category, and the adjoint of the signed sandwich is the operator that the form assigns to it. On a Lie algebra the two one-sided multiplications are skew for an invariant form, so the adjoint of a product is the product of the adjoints in the reverse order, and the adjoint of the signed sandwich is a signed sandwich of the transposed type together with a correction by the commutator of the carrying pair. The form under which the signed sandwich agrees with its adjoint is the **unitarity condition**, and it is the condition under which the signed sandwich defines a unitary operator.

This article treats the adjoint of the signed sandwich on a Lie algebra, the explicit form of the adjoint and the unitarity condition it defines. It is the third article of the `- * Operator Theory` group of the category; the signed sandwich is *The Signed Sandwich on a Lie Algebra* and its one-sided factors are *The Signed Left Multiplication on a Lie Algebra*, both above in the category, the invariant form and its adjoint are *Hermitian Forms on a Lie Algebra*, the star of the enveloping algebra is *The Involution on the Enveloping Algebra of a Lie Group*, and the adjoints of the remaining signed operators are *The Signed Adjoint of the Reflection on a Lie Algebra*, *The Signed Adjoint of the Left Multiplication on a Lie Algebra* and *The Graded Adjoint Action on a Module over a Lie Algebra*, below in this group.

The article assumes the Lie algebra and the bracket from *Lie Groups*, the invariant Hermitian form, its skew-adjoint adjoint operators and its positive definite case from *Hermitian Forms on a Lie Algebra*, the signed sandwich, its factorisation and its square from *The Signed Sandwich on a Lie Algebra*, the signed left multiplication and its kernel from *The Signed Left Multiplication on a Lie Algebra*, and the grade involution and the grading from *Graded Lie Algebras with an Involution*. The form is used as an instrument and not as an object of study; the metric and the geometry of the form belong to Part IV.

## The Adjoint Operation

### The Adjoints of the Factors

**Definition.** Let $H$ be a non-degenerate invariant Hermitian form on $\mathrm{G}$, so that $H([x,y],z) + H(y,[x,z]) = 0$, and suppose that the grade involution is an isometry, $H(\alpha x,\alpha y) = H(x,y)$. The **adjoint** of an endomorphism $T$ is the endomorphism $T^{*}$ with

$$
H(Tx,y) = H(x,T^{*}y) \qquad (x,y\in\mathrm{G}) ;
$$

the adjoint is conjugate-linear in the operator and reverses the order of a product, $(ST)^{*} = T^{*}S^{*}$.

**Proposition.** The one-sided multiplications and the grade involution have the adjoints

$$
L_a^{*} = -L_a, \qquad R_b^{*} = -R_b, \qquad \alpha^{*} = \alpha ,
$$

so all the multiplications are **skew-adjoint** and the grade involution is a self-adjoint isometry.

*Proof.* The invariance of $H$ is the identity $H([a,x],y) = -H(x,[a,y])$, which is $H(L_ax,y) = H(x,-L_ay) = H(x,L_{-a}y)$, hence $L_a^{*} = -L_a$; the right multiplication is the same with the antisymmetry, $R_b^{*} = -R_b$. The isometry condition is the hypothesis, and an isometry is an invertible operator with $\alpha^{*} = \alpha^{-1} = \alpha$.

**Corollary.** The adjoint of a sandwich is the composite of the adjoints in the reverse order,

$$
\Sigma^{\alpha\,*}_{a,b} = \bigl(L_aR_b\alpha\bigr)^{*} = \alpha^{*}R_b^{*}L_a^{*} = \alpha R_bL_a ,
$$

and the adjoint of the unsigned sandwich is $\Sigma_{a,b}^{*} = R_bL_a$.

*Proof.* Substitute the three adjoints in the reversal formula; the signs $(-1)^2 = 1$ cancel.

### The Explicit Form

**Theorem (the explicit adjoint).** For all $a,b\in\mathrm{G}$,

$$
\Sigma^{\alpha\,*}_{a,b} = \Sigma^{\alpha}_{\alpha(a),\alpha(b)} - \alpha R_{[a,b]} ,
$$

and since $\alpha R_{[a,b]} = R_{[\alpha(a),\alpha(b)]}\alpha$, the adjoint is a signed sandwich of the $\alpha$-transformed pair, corrected by the right multiplication of the commutator.

*Proof.* From $[L_a,R_b] = R_{[a,b]}$, proved from the Jacobi identity, one has $R_bL_a = L_aR_b - R_{[a,b]}$; multiplying by $\alpha$ on the left and using $\alpha L_a = L_{\alpha(a)}\alpha$, $\alpha R_b = R_{\alpha(b)}\alpha$ gives

$$
\alpha R_bL_a = \alpha L_aR_b - \alpha R_{[a,b]} = L_{\alpha(a)}R_{\alpha(b)}\alpha - R_{[\alpha(a),\alpha(b)]}\alpha = \Sigma^{\alpha}_{\alpha(a),\alpha(b)} - \alpha R_{[a,b]} ,
$$

which is the formula.

**Corollary (the commuting pair).** If the carrying pair commutes, $[a,b] = 0$, then

$$
\Sigma^{\alpha\,*}_{a,b} = \Sigma^{\alpha}_{\alpha(a),\alpha(b)} = \Sigma^{\alpha}_{a,b} ,
$$

the last equality using that the pair is brought to itself by the grading when the elements are homogeneous; hence every signed sandwich with a commuting carrying pair is self-adjoint.

*Proof.* The correction vanishes when the commutator is zero; the equality with the original pair is the case distinction on the parities, the grading changing the sign of an odd parameter and the sandwich being even quadratically in each parameter.

## The Unitarity Condition

### Self-Adjointness

**Theorem.** The signed sandwich is self-adjoint if and only if the pair satisfies the commutation condition and the invariance condition

$$
[a,b] = 0 \quad\text{and}\quad \Sigma^{\alpha}_{\alpha(a),\alpha(b)} = \Sigma^{\alpha}_{a,b} ,
$$

the second being automatic for homogeneous carrying elements; consequently the signed sandwich is self-adjoint for every pair of homogeneous commuting elements.

*Proof.* The adjoint is the formula above, so self-adjointness is the identity $\Sigma^{\alpha}_{\alpha(a),\alpha(b)} - \alpha R_{[a,b]} = \Sigma^{\alpha}_{a,b}$; separating the sandwich part from the right-multiplication part gives the two stated conditions, and the second holds for homogeneous parameters by the parity computation.

### Skew-Adjointness

**Proposition.** The signed sandwich is skew-adjoint if and only if

$$
2\Sigma^{\alpha}_{a,b} = \alpha R_{[a,b]} ,
$$

an equation which on the odd part of the algebra becomes the vanishing of the second term; in particular no nonzero sandwich with an even commuting pair is skew-adjoint.

*Proof.* Skew-adjointness is $\Sigma^{\alpha\,*}_{a,b} = -\Sigma^{\alpha}_{a,b}$; substitute the formula and rearrange.

### Unitarity

**Theorem (the unitarity condition).** The signed sandwich is **unitary** for $H$ — that is, $\Sigma^{\alpha\,*}_{a,b}\Sigma^{\alpha}_{a,b} = \mathrm{id}$ — if and only if it is self-adjoint and its square is the identity,

$$
\Sigma^{\alpha\,*}_{a,b}\Sigma^{\alpha}_{a,b} = \mathrm{id} \iff [a,b] = 0 \ \text{and}\ \bigl(\Sigma^{\alpha}_{a,b}\bigr)^{2} = \mathrm{id} ,
$$

so that the unitary signed sandwiches are exactly the involutive signed sandwiches with a commuting carrying pair; the second condition is the centrality of the correction in the sense of the square of *The Signed Sandwich on a Lie Algebra*.

*Proof.* For a self-adjoint operator the unitary condition $\Sigma^{*}\Sigma = \mathrm{id}$ is $\Sigma^2 = \mathrm{id}$; conversely the unitary condition implies $\Sigma^{*} = \Sigma^{-1}$, which combined with the explicit form separates into the two stated conditions.

**Corollary.** The signed conjugation $\rho_a = e^{\operatorname{ad}_a}\alpha$ is unitary for $H$ for every $a$, and it is self-adjoint exactly when it is an involution, that is when $a+\alpha(a)$ is central; the unitary reflections are the involutive ones.

*Proof.* The adjoint of the exponential is the exponential of the adjoint, $\rho_a^{*} = \alpha e^{-\operatorname{ad}_a} = \rho_a^{-1}$, so the reflection is unitary; and it is self-adjoint exactly when $\rho_a = \rho_a^{-1}$, that is when its square is the identity. The condition for the involution is that of *Reflections as Signed Two-Sided Operators on a Lie Algebra*.

## Relation to the Unsigned Case and the Form

### The Adjoint of the Unsigned Sandwich

**Proposition.** The adjoint of the unsigned sandwich is $\Sigma_{a,b}^{*} = R_bL_a = \Sigma_{a,b} - R_{[a,b]}$; it is self-adjoint exactly when the carrying pair commutes, and it is the case $\alpha = \mathrm{id}$ of the general formula.

*Proof.* Substitute $\alpha = \mathrm{id}$ in the explicit form.

### The Form Defined by the Operator

**Theorem.** The sesquilinear form

$$
H_{\Sigma}(x,y) = H\bigl(\Sigma^{\alpha}_{a,b}x, y\bigr) - H\bigl(x,\Sigma^{\alpha}_{a,b}y\bigr)
$$

vanishes identically if and only if the signed sandwich is self-adjoint; the antisymmetric part of the sandwich with respect to $H$ is therefore the operator $\Sigma^{\alpha}_{a,b} - \alpha R_bL_a$, and the invariance of $H$ under the sandwich is exactly the self-adjointness.

*Proof.* The form is the defect of self-adjointness, and it vanishes exactly when $H(\Sigma x,y) = H(x,\Sigma y)$, which is the definition of the adjoint.

**Corollary.** The signed sandwich is a normal operator for $H$ exactly when it commutes with its adjoint; the defect $\Sigma^{\alpha\,*}_{a,b}\Sigma^{\alpha}_{a,b} - \Sigma^{\alpha}_{a,b}\Sigma^{\alpha\,*}_{a,b}$ is the measure of the failure, and it vanishes for every commuting pair of homogeneous elements.

*Proof.* Normality is the vanishing of the commutator with the adjoint; for a commuting homogeneous pair the operator is self-adjoint by the corollary above, hence normal.

## Examples

### The Orthogonal Algebra

Let $\mathrm{G} = \mathrm{so}(3)$ with the negative definite form $H(X,Y) = -\frac12\operatorname{tr}(XY)$, which is positive definite and invariant; the algebra is compact, the left multiplications are skew-adjoint, and every signed sandwich with a commuting pair is self-adjoint. The Casimir operator is the negative of the Laplacian, and it is a positive self-adjoint combination of the sandwiches.

### The Rank-One Algebra

Let $\mathrm{G} = \mathrm{sl}_2(\mathbb{R})$ with the invariant form of signature $(2,1)$ given by the Killing form, and the Cartan involution as the grading. For an odd element $a$ and an even element $b$ with $[a,b] = 0$ the signed sandwich is self-adjoint; for a non-commuting pair the correction term is the right multiplication of the commutator, which is nonzero and destroys the self-adjointness.

### A Degenerate Case

Let $\mathrm{G}$ be the Heisenberg algebra with the central element $Z$; the invariant scalar product is degenerate, vanishing on the radical spanned by $Z$, and there is no non-degenerate invariant form. The adjoint of a signed sandwich is then defined only on the quotient by the radical, and the unitarity condition fails on the radical; this is the degenerate case in which the form does not define an adjoint for every operator, treated further in *Unitary Representations and the Orbit Method*.

## Summary

With respect to a non-degenerate invariant Hermitian form $H$ that the grade involution preserves, the one-sided multiplications are skew-adjoint, $L_a^{*} = -L_a$ and $R_b^{*} = -R_b$, and the grade involution is self-adjoint; hence the adjoint of the signed sandwich is the composite of the adjoints in the reverse order, $\Sigma^{\alpha\,*}_{a,b} = \alpha R_bL_a$, with the explicit form

$$
\Sigma^{\alpha\,*}_{a,b} = \Sigma^{\alpha}_{\alpha(a),\alpha(b)} - \alpha R_{[a,b]} ,
$$

a signed sandwich of the $\alpha$-transformed pair corrected by the right multiplication of the commutator. The signed sandwich is self-adjoint exactly when the carrying pair commutes and the sandwich is $\alpha$-invariant, which holds for homogeneous pairs; it is skew-adjoint only in the special case $2\Sigma^{\alpha}_{a,b} = \alpha R_{[a,b]}$, and it is **unitary** exactly when it is self-adjoint and its square is the identity, so the unitary signed sandwiches are the involutive ones with a commuting carrying pair. The signed conjugation is unitary for every element, being the inverse of its adjoint, and it is self-adjoint exactly when it is an involution; the unsigned case is $\alpha = \mathrm{id}$, and the form defect $H(\Sigma x,y) - H(x,\Sigma y)$ measures the failure of the self-adjointness.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H$ | a non-degenerate invariant Hermitian form |
| $T^{*}$ | the adjoint of $T$ for $H$ |
| $L_a^{*} = -L_a$, $R_b^{*} = -R_b$ | skew-adjointness of the multiplications |
| $\alpha^{*} = \alpha$ | the grade involution is a self-adjoint isometry |
| $\Sigma^{\alpha}_{a,b} = L_aR_b\alpha$ | the signed sandwich |
| $\Sigma^{\alpha\,*}_{a,b} = \alpha R_bL_a$ | the adjoint of the signed sandwich |
| $\Sigma^{\alpha\,*}_{a,b} = \Sigma^{\alpha}_{\alpha(a),\alpha(b)} - \alpha R_{[a,b]}$ | the explicit form |
| $[L_a,R_b] = R_{[a,b]}$ | the commutator identity used |
| $[a,b] = 0$ | the commuting carrying pair, self-adjointness |
| $\Sigma^{\alpha\,*}_{a,b}\Sigma^{\alpha}_{a,b} = \mathrm{id}$ | the unitarity condition |
| $\rho_a^{*} = \rho_a^{-1}$ | the reflection is unitary |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for the invariant forms, the adjoint operators and the Casimir element.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, second edition, 2002), for the invariant forms, the Cartan involution and the skew-adjoint operators.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the adjoint of a signed operator and the unitarity conditions.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, second edition, 2015), for the unitary conditions and the adjoints of the multiplication operators.
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984), for the invariant forms, the adjoints and the unitary representations.
