# __The Signed Adjoint of the Reflection on a Jordan Algebra__

## Introduction

A **reflection** in the algebraic sense is an operator of order two; on a Jordan algebra the signed two-sided operators of order two are the **signed conjugations** $r_u(x) = u\,\alpha(x)\,u^{-1}$ of *Reflections as Signed Two-Sided Operators on a Jordan Algebra*, built from the **grade involution** $\alpha$ and the inner conjugation by a unit $u$. Such an operator is an automorphism of the Jordan algebra whenever it is defined, and it is an involution exactly when the **twisted square** $u\alpha(u)$ is central; this is the reflection correspondence of that article. The present article computes the **adjoint** of the reflection with respect to the **natural pairing** of the category, the trace form $T(x,y) = \operatorname{tr}(L_{x\circ y})$ of *The Adjoint of the Left Multiplication on a Jordan Algebra*, and decides when a reflection is **self-adjoint**.

Because the trace form is associative and the grade involution is an isometry, every operator of the multiplication algebra is self-adjoint and the involution satisfies $\alpha^{\dagger} = \alpha$; the reflection that lives in the Jordan operator algebra is the symmetrisation $U_u\circ\alpha$ of the signed conjugation at a **symmetry** $u$, and its adjoint is the reflection at the image of the parameter,

$$
\bigl(U_u\circ\alpha\bigr)^{\dagger} = U_{\alpha(u)}\circ\alpha .
$$

A reflection is therefore **self-adjoint exactly when it is fixed by the grade involution**, $\alpha(u) = u$, and the self-adjointness fails precisely in the **degenerate case** in which the twisted square $u\alpha(u)$ is not central, where the operator $r_u$ is not an involution at all but an automorphism of infinite order, and its adjoint is a different signed conjugation. The article also records the reflection for its own grade involution, where the operator collapses to the identity, and it states the unitarity of the reflections that are symmetries.

The article assumes *Reflections as Signed Two-Sided Operators on a Jordan Algebra* for the signed conjugation, the twisted square and the reflection criterion; *The Signed Sandwich on a Jordan Algebra* for the symmetrisation $\Sigma^{\alpha}_{a,b} = U_{a,b}\circ\alpha$; *The Signed Adjoint Sandwich on a Jordan Algebra* for the adjoint computation and the unitarity condition; *The Adjoint of the Left Multiplication on a Jordan Algebra* for the trace form, its associativity and the self-adjointness of the quadratic representations; and *The Left and Right Multiplication Operators on a Jordan Algebra* for the symmetries and the inner structure group. Throughout, $J = A^+$ is a special unital Jordan algebra over a commutative ring $R$ in which $2$ is invertible, $\alpha$ is a grade involution of $A$, $u$ is a unit of $A$, $r_u(x) = u\alpha(x)u^{-1}$ is the signed conjugation, $T$ is the trace form and ${}^{\dagger}$ its adjoint; no norm, form, distance or geometric reflection occurs, and the symmetric-space reading of "reflection" is deferred to Part IV.

## The Reflection and Its Adjoint

### The Signed Conjugation

**Definition.** The **signed conjugation** by the unit $u$ is $r_u(x) = u\,\alpha(x)\,u^{-1}$; it is an automorphism of $J$, and it is a **reflection** when $r_u^2 = \mathrm{id}$, which holds exactly when the **twisted square** $u\alpha(u)$ is central.

**Proposition (the symmetrised form).** The reflection by a **symmetry** $u = u^{-1}$ coincides with the symmetrised signed sandwich $U_u\circ\alpha$, and the diagonal signed sandwich $S^{\alpha}_{u,u^{-1}}$ has this symmetrisation.

*Proof.* The symmetrisation of the sandwich $S^{\alpha}_{u,u^{-1}}(x) = u\alpha(x)u^{-1}$ over the outer parameter is the twisted quadratic representation $U_u\circ\alpha$; for a symmetry the conjugation and the sandwich agree, as in *The Signed Sandwich on a Jordan Algebra*. $\square$

### The Adjoint

**Theorem.** The adjoint of the reflection $U_u\circ\alpha$ with respect to the trace form is the reflection at the image of the parameter:

$$
\bigl(U_u\circ\alpha\bigr)^{\dagger} = U_{\alpha(u)}\circ\alpha .
$$

*Proof.* By *The Signed Adjoint Sandwich on a Jordan Algebra*, $(U_{a,b}\circ\alpha)^{\dagger} = U_{\alpha(a),\alpha(b)}\circ\alpha$; with $a = b = u$ and $U_{u,u} = U_u$ this is the displayed formula. $\square$

**Theorem (self-adjointness).** A reflection is self-adjoint exactly when its parameter is fixed by the grade involution:

$$
\bigl(U_u\circ\alpha\bigr)^{\dagger} = U_u\circ\alpha \iff \alpha(u) = u .
$$

*Proof.* The adjoint is $U_{\alpha(u)}\circ\alpha$; it is equal to $U_u\circ\alpha$ exactly when $U_{\alpha(u)} = U_u$, which for a non-degenerate trace form holds exactly when $\alpha(u) = u$. $\square$

### The Degenerate Case

**Proposition.** If the twisted square $u\alpha(u)$ is not central, then $r_u$ is not an involution, the reflection correspondence fails, and $r_u$ is an automorphism of infinite order; its adjoint $r_{\alpha(u)}$ is a different signed conjugation, and the operator is neither self-adjoint nor unitary in general.

*Proof.* The square of the signed conjugation is the inner conjugation by $u\alpha(u)$, which is trivial exactly when that element is central; when it is not central, $r_u^2\ne\mathrm{id}$ and $r_u$ has infinite order. The adjoint is computed as the signed conjugation at $\alpha(u)$, which differs from $r_u$ whenever $\alpha(u)\ne u$. $\square$

## Reflection for Its Own Grade Involution

**Theorem.** For the grade involution $\alpha_r$ defined by a reflection, the signed conjugation by $r$ is the identity,

$$
r_r(x) = r\,\alpha_r(x)\,r^{-1} = x ,
$$

which is self-adjoint and unitary; the reflection at the parameter equal to its own involution degenerates to the identity of the algebra.

*Proof.* $\alpha_r(x) = rxr$ and $r^{-1} = r$, so $r_r(x) = r(rxr)r^{-1} = x$; the identity is self-adjoint for every pairing and unitary. $\square$

## Unitarity

**Proposition.** A reflection that is a symmetry is unitary with respect to the adjoint exactly when the quadratic representation is an involution, $U_u^2 = \mathrm{id}$, which holds for the symmetries; in that case $(U_u\circ\alpha)^{\dagger}(U_u\circ\alpha) = \mathrm{id}$.

*Proof.* By *The Signed Adjoint Sandwich on a Jordan Algebra* the unitarity of the signed sandwich is $U_{u,u}^2 = \mathrm{id}$, that is $U_u^2 = \mathrm{id}$; the symmetries satisfy it. $\square$

## Examples

**Example (the identity reflection).** For $u = 1$ the signed conjugation is $\alpha$ itself, a reflection of order two; it is self-adjoint because $\alpha(1) = 1$, and unitary because $U_1 = \mathrm{id}$.

**Example (the matrix algebra).** Let $J = A^+$ for $A = M_n(F)$ with the transpose grade involution; a symmetry $u = u^{-1}$ gives the reflection $U_u\circ\alpha$, $x\mapsto u x^{\mathsf{T}} u$, whose adjoint is $U_{u^{\mathsf{T}}}\circ\alpha = U_u\circ\alpha$ because $u$ is symmetric; the reflection is self-adjoint, and it degenerates to the identity when $u$ is the involution defining $\alpha$.

**Example (the degenerate conjugation).** Let $A$ be the polynomial algebra $F[x,y]$ with the swap grade involution and $u = x$; the twisted square $u\alpha(u) = xy$ is not central, so $r_u$ is not a reflection but an automorphism of infinite order, and its adjoint $r_{\alpha(u)} = r_y$ is a different conjugation.

## Summary

A **reflection** on a Jordan algebra is a signed conjugation $r_u(x) = u\alpha(x)u^{-1}$ of order two, which exists exactly when the twisted square $u\alpha(u)$ is central; at a symmetry it coincides with the symmetrised signed sandwich $U_u\circ\alpha$. With respect to the **trace form**, the associativity of the form and the isometry property of the grade involution give the adjoint

$$
\bigl(U_u\circ\alpha\bigr)^{\dagger} = U_{\alpha(u)}\circ\alpha ,
$$

so a reflection is **self-adjoint exactly when $\alpha(u) = u$**; when the twisted square is not central the operator is an automorphism of infinite order, the reflection correspondence fails, and the adjoint is a different signed conjugation. The reflection for its own grade involution is the identity, and the reflections that are symmetries are unitary when $U_u^2 = \mathrm{id}$. No norm, form, distance or geometric reflection occurs.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $r_u(x) = u\alpha(x)u^{-1}$ | Signed conjugation (reflection when of order two) |
| $u\alpha(u)$ central | Reflection criterion |
| $u = u^{-1}$ | Symmetry, where the reflection is $U_u\circ\alpha$ |
| $(U_u\circ\alpha)^{\dagger} = U_{\alpha(u)}\circ\alpha$ | Adjoint of the reflection |
| $\alpha(u) = u$ | Self-adjointness condition |
| $u\alpha(u)$ not central | Degenerate case, infinite order |
| $r_r = \mathrm{id}$ | Reflection for its own grade involution |
| $U_u^2 = \mathrm{id}$ | Unitarity condition |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the reflections, the symmetries and their adjoints.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the quadratic representations, the symmetries and the structure group.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the signed conjugations, the reflections and the adjoints.
- Hel Braun and Max Koecher, *The Jordan Algebra Approach to Bounded Symmetric Domains* (Springer, 1966), for the reflections, the structure group and the trace form.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the multiplication algebra, the involutions and the conjugations.
