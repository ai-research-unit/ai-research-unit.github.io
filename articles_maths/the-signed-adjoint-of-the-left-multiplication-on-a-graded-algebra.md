
# __The Signed Adjoint of the Left Multiplication on a Graded Algebra__

## Introduction

The **signed left multiplication** of *The Signed Left Multiplication on a Graded Algebra* is the one-sided operator $\ell_a(x)=a\,\alpha(x)=L_a\circ\alpha$, the left multiplication with the argument twisted by the grade involution. When the graded algebra carries a balanced α-compatible form, the adjoint of $\ell_a$ has a closed expression,

$$
(\ell_a)^{\dagger}=\varrho_{\alpha(a)},\qquad \varrho_b(x)=\alpha(x)\,b,
$$

the **signed right multiplication** by $\alpha(a)$; the adjoint of the signed left multiplication is therefore a signed right multiplication, and the adjoint of the two-sided signed sandwich is assembled from the two. This article, the seventh of the `- * Operator Theory` group of the category, computes the adjoint of $\ell_a$, identifies it with a signed right multiplication, derives the self-adjointness and the isometry conditions for $\ell_a$, and reads the adjoint of the signed sandwich as the composite of the two one-sided adjoints. The signed left multiplication is *The Signed Left Multiplication on a Graded Algebra*; the form and the adjoint are *The Signed Adjoint Sandwich on a Graded Algebra*; the analytic theory of unitary operators belongs to a later Part and is named only.

The base is a field $K$ of characteristic not two, $A$ a finite-dimensional graded algebra with grade involution $\alpha$ and a balanced α-compatible nondegenerate form $\beta$ with $\alpha^{\dagger}=\alpha$. The operators are $L_a,R_b$ (unsigned), $\ell_a=L_a\alpha$ (signed left) and $\varrho_b=R_b\alpha$ (signed right), and ${}^{\dagger}$ is the adjoint. The article uses the form algebraically and forms no length from it.

## The Signed Right Multiplication

**Definition.** The **signed right multiplication** by $b$ is

$$
\varrho_b=\varrho^{\alpha}_b=R_b\circ\alpha,\qquad \varrho_b(x)=\alpha(x)\,b .
$$

**Proposition.** The signed right multiplications satisfy $\varrho_a\varrho_b=\varrho_{a\alpha(b)}$ and $R_b\alpha=\alpha R_{\alpha(b)}$; they form the coset $R(A)\alpha$ of the unsigned right multiplications, and the map $b\mapsto\alpha(b)$ conjugates the multiplication in that coset, so a product of two signed right multiplications is unsigned, as for the signed left multiplications.

**Proof.** Using $\alpha R_b=R_{\alpha(b)}\alpha$,
$$
\varrho_a\varrho_b=R_a\alpha R_b\alpha=R_aR_{\alpha(b)}\alpha\alpha=R_{a\alpha(b)}\alpha=\varrho_{a\alpha(b)},
$$
and $R_b\alpha=\alpha R_{\alpha(b)}$ is the same relation read the other way; the family is the coset $R(A)\alpha$. $\square$

**Corollary.** The signed right multiplications are the mirror image of the signed left multiplications: a product of two signed right multiplications is unsigned, as for the left, and the two families are exchanged by the involution $T\mapsto T^{\dagger}$ of the adjoint below.

## The Adjoint of the Signed Left Multiplication

**Theorem.** For a balanced α-compatible form,

$$
(\ell_a)^{\dagger}=\varrho_{\alpha(a)},\qquad\text{that is}\qquad (\ell_a)^{\dagger}(x)=\alpha(x)\,\alpha(a).
$$

**Proof.** By *The Signed Adjoint Sandwich on a Graded Algebra*, $(\ell_a)^{\dagger}=\Sigma^{\alpha}_{1,\alpha(a)}$ (the case $b=1$ of the sandwich adjoint), and $\Sigma^{\alpha}_{1,\alpha(a)}(x)=1\cdot\alpha(x)\cdot\alpha(a)=\alpha(x)\alpha(a)=\varrho_{\alpha(a)}(x)$. $\square$

**Corollary.** The adjoint of the signed left multiplication is a signed right multiplication; the adjoint of the signed right multiplication is a signed left multiplication, $(\varrho_b)^{\dagger}=\ell_{\alpha(b)}$; and the adjoint operation exchanges the two families $L(A)\alpha$ and $R(A)\alpha$.

**Proposition (the sandwich from the two adjoints).** The signed sandwich factors as $\Sigma^{\alpha}_{a,b}=\ell_a\circ R_{\alpha(b)}$, and its adjoint is the composite of the two one-sided adjoints,

$$
(\Sigma^{\alpha}_{a,b})^{\dagger}=R_{\alpha(b)}^{\,\dagger}\circ(\ell_a)^{\dagger}=L_{\alpha(b)}\circ\varrho_{\alpha(a)}=\Sigma^{\alpha}_{\alpha(b),\alpha(a)},
$$

in agreement with the two-sided computation.

**Proof.** The factorization is $\ell_aR_{\alpha(b)}(x)=a\alpha(x\alpha(b))=a\alpha(x)b$; the adjoint of a composite reverses the order, and $R_{\alpha(b)}^{\dagger}=L_{\alpha(b)}$ by the balanced property; the last equality is the displayed evaluation. $\square$

## Self-Adjointness and Isometry

**Theorem (self-adjointness).** The signed left multiplication is self-adjoint, $(\ell_a)^{\dagger}=\ell_a$, if and only if $a$ is central and even; in that case $\alpha(a)=a$ and $\ell_a=L_a\alpha$ equals its own adjoint $\varrho_a$.

**Proof.** $(\ell_a)^{\dagger}=\varrho_{\alpha(a)}=R_{\alpha(a)}\alpha$ and $\ell_a=L_a\alpha$; since $\alpha$ is invertible, equality is $R_{\alpha(a)}=L_a$, which for all $x$ means $x\alpha(a)=ax$, that is $\alpha(a)$ central and equal to $a$; so $a$ is central and $\alpha(a)=a$, i.e., $a$ is even. $\square$

**Corollary.** The grade involution $\ell_1=\alpha$ is self-adjoint; a central even element gives a self-adjoint signed left multiplication; a non-central or odd element gives a signed left multiplication whose adjoint is a different signed right multiplication.

**Theorem (isometry).** The signed left multiplication $\ell_a$ is an isometry of $\beta$ if and only if $a$ is central and $a^{2}=1$.

**Proof.** Compute the two products. Since $\alpha L_a\alpha=L_{\alpha(a)}$ and $\alpha R_b\alpha=R_{\alpha(b)}$,
$$
(\ell_a)^{\dagger}\ell_a=\varrho_{\alpha(a)}\ell_a=R_{\alpha(a)}\alpha L_a\alpha=R_{\alpha(a)}L_{\alpha(a)},\qquad x\mapsto\alpha(a)\,x\,\alpha(a),
$$
$$
\ell_a(\ell_a)^{\dagger}=\ell_a\varrho_{\alpha(a)}=L_a\alpha R_{\alpha(a)}\alpha=L_aR_a,\qquad x\mapsto a\,x\,a .
$$
Both are the identity exactly when the square of the element is $1$ and the element is central; the first gives $\alpha(a)$ central with $\alpha(a)^{2}=1$, the second $a$ central with $a^{2}=1$, and either central condition implies the other, since $\alpha(a)$ is central when $a$ is. $\square$

**Corollary.** The isometric signed left multiplications are $\ell_a$ with $a$ central and $a^{2}=1$, of either parity; the element $a=1$ gives the grade involution $\alpha$, which is an isometry; and the isometry condition is the one-sided counterpart of the two-sided condition $b=a^{-1}$ of *The Signed Adjoint Sandwich on a Graded Algebra*.

## Worked Case: Endomorphisms of a Graded Two-Dimensional Space

Let $A=\mathrm{End}_K(V)$, $J=\operatorname{diag}(1,-1)$, $\alpha(X)=JXJ^{-1}$, and $\beta(X,Y)=\operatorname{tr}(XY)$.

For the central element $a=I$ one has $\alpha(a)=a$ and $\ell_I=\alpha$, the grade involution; its adjoint is $\varrho_I=\alpha$, so $\ell_I$ is self-adjoint, and since $I^{2}=1$ it is an isometry, as the criterion requires.

For the non-central element $a=J$ one has $\alpha(J)=J$, and $\ell_J(X)=J\alpha(X)=J(JXJ)=XJ$, the unsigned right multiplication $R_J$; its adjoint is $\varrho_J=L_J$, which differs from $R_J$ because $J$ is not central, so $\ell_J$ is neither self-adjoint nor an isometry, in agreement with the criteria, which require centrality.

For the non-central element $a=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ one has $\alpha(a)=\begin{pmatrix}1&-1\\0&1\end{pmatrix}\neq a$, and at $X=I$ one has $\ell_a(I)=a$ while $(\ell_a)^{\dagger}(I)=\varrho_{\alpha(a)}(I)=\alpha(a)$, so $\ell_a$ is not self-adjoint; and $a^{2}\neq1$, so it is not an isometry either.

**Verified.** The adjoint formula $(\ell_a)^{\dagger}=\varrho_{\alpha(a)}$ was checked on the four basis elements of $M_2(K)$ for the trace form and $\alpha(X)=JXJ^{-1}$; the self-adjointness criterion (central and even) and the isometry criterion (central, $a^{2}=1$) were checked against the three examples above, in which $\ell_I$ is self-adjoint and isometric, and $\ell_J$, $\ell_a$ with $a=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ are neither.

## Summary

The **signed left multiplication** $\ell_a=L_a\alpha$ has adjoint, with respect to a balanced α-compatible form,

$$
(\ell_a)^{\dagger}=\varrho_{\alpha(a)},\qquad \varrho_b(x)=\alpha(x)\,b,
$$

the **signed right multiplication** by $\alpha(a)$; the adjoint operation exchanges the two families $L(A)\alpha$ and $R(A)\alpha$. The signed sandwich factors as $\Sigma^{\alpha}_{a,b}=\ell_aR_{\alpha(b)}$, and its two-sided adjoint is assembled from the one-sided ones, $(\Sigma^{\alpha}_{a,b})^{\dagger}=L_{\alpha(b)}\varrho_{\alpha(a)}=\Sigma^{\alpha}_{\alpha(b),\alpha(a)}$, in agreement with the direct computation. The signed left multiplication is **self-adjoint** exactly when $a$ is central and even, and it is an **isometry** exactly when $a$ is central with $a^{2}=1$; the grade involution $\ell_1=\alpha$ satisfies both. The endomorphisms of a graded two-dimensional space are the worked case, where the formulas are explicit. The analytic theory of unitary operators belongs to a later Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | the base field, of characteristic not two |
| $A=A^0\oplus A^1$ | a graded algebra with a balanced α-compatible form |
| $\alpha$ | the grade involution |
| $L_a,R_b$ | unsigned left and right multiplication |
| $\ell_a=L_a\alpha$ | the signed left multiplication |
| $\varrho_b=R_b\alpha$ | the signed right multiplication |
| $\Sigma^{\alpha}_{a,b}(x)=a\alpha(x)b$ | the signed sandwich |
| ${}^{\dagger}$ | the adjoint with respect to $\beta$ |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for signed one-sided operators and their adjoints.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1989), for adjoint operators and bilinear forms.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for one-sided operators in algebras with involution.
- Larry C. Grove, *Classical Groups and Geometric Algebra*, Graduate Studies in Mathematics 39 (American Mathematical Society, 2002), for isometries and their one-sided descriptions.
