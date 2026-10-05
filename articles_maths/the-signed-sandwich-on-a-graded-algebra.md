
# __The Signed Sandwich on a Graded Algebra__

## Introduction

Let $A$ be an associative algebra with a $\mathbb{Z}/2$-grading, $A=A^0\oplus A^1$, and let $\alpha$ be its **grade involution**, the algebra automorphism acting by $(-1)^k$ on the homogeneous part $A^k$. For a pair of elements $a,b$ the **unsigned sandwich** is the operator $x\mapsto axb$, and the **signed sandwich** is the operator

$$
\Sigma^{\alpha}_{a,b}(x)=a\,\alpha(x)\,b,
$$

the two-sided multiplication with the argument twisted by $\alpha$. This article is the operator layer of the graded algebra: it defines the two sandwiches, computes their composition law, relates them through the grade involution, reads their parity and their invertibility, and examines when a signed sandwich is an involution, which is the algebraic form in which the reflections of a Clifford algebra appear. The graded algebra, the sign rule and the parity are the subject of *Superalgebras and Graded Structures* and are cited; the realisation of the reflections by the signed sandwiches, the one-sided signed operator and the graded action on a module are the companion entries *Reflections as Signed Two-Sided Operators on a Graded Algebra*, *The Signed Left Multiplication on a Graded Algebra* and *The Graded Action on a Module over a Graded Algebra*; the adjoints of these operators belong to the `- * Operator Theory` group and are deferred.

The base is a commutative ring $R$ with $1$; when invertibility is needed a field $K$ is used, and the algebra is written $A$ with homogeneous parts $A^0,A^1$. The grade involution is $\alpha$, the unsigned sandwich $\Sigma_{a,b}$, the signed sandwich $\Sigma^{\alpha}_{a,b}$, and the left multiplication by $a$ is $L_a$. The article reasons with the ring structure and the grading only.

## The Two Sandwiches

### Definitions

**Definition.** For elements $a,b\in A$ the **unsigned sandwich** is

$$
\Sigma_{a,b}:A\longrightarrow A,\qquad \Sigma_{a,b}(x)=axb,
$$

and the **signed sandwich** is

$$
\Sigma^{\alpha}_{a,b}:A\longrightarrow A,\qquad \Sigma^{\alpha}_{a,b}(x)=a\,\alpha(x)\,b .
$$

Both are $R$-linear, and $\Sigma^{\alpha}_{a,b}$ differs from $\Sigma_{a,b}$ by the twist of the argument by the grade involution.

**Proposition.** The signed sandwich factors through the unsigned one and the grade involution:

$$
\Sigma^{\alpha}_{a,b}=\Sigma_{a,b}\circ\alpha=L_a\circ\alpha\circ R_b .
$$

**Proof.** Both sides send $x$ to $a\alpha(x)b$. $\square$

**Corollary.** Since $\alpha$ is an algebra automorphism and additive, the map $\Sigma_{a,b}\mapsto\Sigma^{\alpha}_{a,b}$ is an involutive transformation of the set of unsigned sandwiches, and the signed sandwich is unsigned exactly when $\alpha(x)=x$ on the elements that matter, in particular when $\alpha=\mathrm{id}$, that is when $A^1=0$.

### Composition and Invertibility

**Theorem.** The signed sandwiches compose by

$$
\Sigma^{\alpha}_{a,b}\circ\Sigma^{\alpha}_{c,d}=\Sigma^{\alpha}_{a\,\alpha(c),\ \alpha(d)\,b},
$$

and the unsigned sandwiches compose by $\Sigma_{a,b}\circ\Sigma_{c,d}=\Sigma_{ac,db}$.

**Proof.** For the signed case, $\Sigma^{\alpha}_{a,b}(\Sigma^{\alpha}_{c,d}(x))=a\,\alpha(c\alpha(x)d)\,b=a\,\alpha(c)\,\alpha(\alpha(x))\,\alpha(d)\,b=a\alpha(c)\,x\,\alpha(d)\,b=\Sigma^{\alpha}_{a\alpha(c),\alpha(d)b}(x)$, using $\alpha^2=\mathrm{id}$ and the multiplicativity of $\alpha$. The unsigned case is associativity. $\square$

**Corollary.** The signed sandwiches form a monoid under composition, with unit $\Sigma^{\alpha}_{1,1}$; the unsigned sandwiches form a monoid with unit $\Sigma_{1,1}$. The product of two signed sandwiches is a signed sandwich, not an unsigned one; the product of a signed and an unsigned sandwich is a signed sandwich, and the unsigned part is a submonoid.

**Theorem.** The signed sandwich $\Sigma^{\alpha}_{a,b}$ is invertible if and only if $a$ and $b$ are units of $A$, and then

$$
\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{-1}=\Sigma^{\alpha}_{\alpha(a^{-1}),\,\alpha(b^{-1})} .
$$

**Proof.** Compose on the right: $\Sigma^{\alpha}_{a,b}\circ\Sigma^{\alpha}_{\alpha(a^{-1}),\alpha(b^{-1})}=\Sigma^{\alpha}_{a\alpha(\alpha(a^{-1})),\ \alpha(\alpha(b^{-1}))b}=\Sigma^{\alpha}_{a a^{-1},\ b^{-1}b}=\Sigma^{\alpha}_{1,1}$, by the composition law, the multiplicativity of $\alpha$ and $\alpha^2=\mathrm{id}$; the same computation with the factors interchanged gives the left inverse. Conversely if $\Sigma^{\alpha}_{a,b}$ is invertible then left multiplication by $a$ is invertible, so $a$ is a unit, and right multiplication by $b$ is invertible, so $b$ is a unit. $\square$

## The Parity of the Sandwiches

**Definition.** The algebra $A$ is $\mathbb{Z}/2$-graded; an element is **homogeneous** of degree $|a|\in\mathbb{Z}/2$ when it lies in $A^{|a|}$. The grade involution acts on homogeneous elements by $\alpha(a)=(-1)^{|a|}a$.

**Proposition.** If $a$ and $b$ are homogeneous of degrees $|a|,|b|$, then $\Sigma_{a,b}$ and $\Sigma^{\alpha}_{a,b}$ map $A^k$ to $A^{k+|a|+|b|}$; the sign of the twist is $(-1)^k$ on $A^k$.

**Proof.** The left multiplication by $a$ shifts the degree by $|a|$, the right by $|b|$; the twist multiplies by $(-1)^k$ on $A^k$. $\square$

**Corollary.** The signed sandwich is homogeneous of degree $|a|+|b|$ as a map of graded $R$-modules, and the unsigned sandwich has the same degree; the two differ only by the sign $(-1)^k$ on each homogeneous component.

## The Signed Sandwich and the Reflections

**Definition.** An operator $S$ on $A$ is an **involution**, or a **reflection**, when $S^2=\mathrm{id}$, and a signed sandwich is a **signed reflection** when it is an involution.

**Theorem.** If $a$ is a unit with $a\,\alpha(a)=1$, then the signed sandwich

$$
\Sigma^{\alpha}_{a,\,a^{-1}}(x)=a\,\alpha(x)\,a^{-1}
$$

is an involution, a **signed reflection**; more generally $\Sigma^{\alpha}_{a,b}$ is an involution whenever $a,b$ are units with $a\alpha(a)=1$ and $b\alpha(b)=1$ and $a,b$ lie in the centre. An element $x$ is fixed by $\Sigma^{\alpha}_{a,a^{-1}}$ exactly when $\alpha(x)=a^{-1}xa$.

**Proof.** By the composition law $\Sigma^{\alpha}_{a,a^{-1}}\circ\Sigma^{\alpha}_{a,a^{-1}}=\Sigma^{\alpha}_{a\alpha(a),\,\alpha(a^{-1})a^{-1}}$; with $a\alpha(a)=1$ the first factor is $1$, and the second is $\alpha(a^{-1})a^{-1}=(a\alpha(a))^{-1}=1$. The general condition is the same computation with two pairs; the fixed-point statement is $a\alpha(x)a^{-1}=x$. $\square$

**Corollary.** In a Clifford algebra the signed sandwich $x\mapsto u\alpha(x)u^{-1}$ with $u\alpha(u)=1$ is the reflection in the direction of $u$ on the space of vectors, since $\alpha(v)=-v$ there; this is the algebraic mechanism by which a signed sandwich realises a reflection, and it is developed in *Reflections as Signed Two-Sided Operators on a Graded Algebra*. The Clifford algebra itself, its quadratic form and its orthogonal group belong to the symmetric algebras and are named here only as the model; nothing of them is used.

## Worked Case: The Exterior Algebra

Let $A=\Lambda^\bullet V$ be the exterior algebra of a finite-dimensional $K$-vector space $V$, graded by the degree modulo two, with the grade involution $\alpha$ acting by $(-1)^k$ on $\Lambda^kV$. For homogeneous $a,b$ the signed sandwich is $\Sigma^{\alpha}_{a,b}(\omega)=a\wedge\alpha(\omega)\wedge b$, and the composition law reads $\Sigma^{\alpha}_{a,b}\circ\Sigma^{\alpha}_{c,d}=\Sigma^{\alpha}_{a\wedge\alpha(c),\alpha(d)\wedge b}$. For $a$ of even degree and $b=a^{-1}$ when $a$ is a unit in the even part, the sandwich is an unsigned conjugation; for $a$ of odd degree, for example $a=v$ a vector, one has $\alpha(v)=-v$ and $\Sigma^{\alpha}_{v,v}(\omega)=v\wedge\alpha(\omega)\wedge v=v\wedge(-1)^{|\omega|}\omega\wedge v$, which is $0$ on the whole algebra because $v\wedge v=0$. The degenerate case shows that the involution condition is not automatic and is the reason the next entry separates the nondegenerate from the degenerate correspondences.

**Verified.** The composition law and the parity of $\Sigma^{\alpha}_{a,b}$ were checked on the exterior algebra of a two-dimensional space on homogeneous basis elements, and the vanishing of the odd vector sandwich was checked on the four basis elements $1,e_1,e_2,e_1e_2$.

## Summary

On a $\mathbb{Z}/2$-graded algebra $A$ with grade involution $\alpha$, the **unsigned sandwich** is $\Sigma_{a,b}(x)=axb$ and the **signed sandwich** is $\Sigma^{\alpha}_{a,b}(x)=a\alpha(x)b=\Sigma_{a,b}\alpha$. The signed sandwiches compose by $\Sigma^{\alpha}_{a,b}\circ\Sigma^{\alpha}_{c,d}=\Sigma^{\alpha}_{a\alpha(c),\alpha(d)b}$, so they form a monoid with unit $\Sigma^{\alpha}_{1,1}$, and the product of two signed sandwiches is again signed; a signed sandwich is invertible exactly when its two elements are units. Homogeneous elements give homogeneous sandwiches of degree $|a|+|b|$, the twist contributing the sign $(-1)^k$ on $A^k$. A signed sandwich is an involution, a **signed reflection**, exactly under the stated centrality conditions, and the special case $\Sigma^{\alpha}_{a,a^{-1}}$ with $a\alpha(a)=1$ gives the algebraic reflection of a Clifford algebra, model only, while in the exterior algebra an odd element with $a\wedge a=0$ gives the degenerate vanishing. The reflections, the one-sided signed operators and the graded actions are the companion entries, and the adjoints belong to the `- * Operator Theory` group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | the commutative base ring, $K$ a field when units are needed |
| $A=A^0\oplus A^1$ | a $\mathbb{Z}/2$-graded associative algebra |
| $\alpha$ | the grade involution, $\alpha(x)=(-1)^k x$ on $A^k$ |
| $\Sigma_{a,b}(x)=axb$ | the unsigned sandwich |
| $\Sigma^{\alpha}_{a,b}(x)=a\alpha(x)b$ | the signed sandwich |
| $L_a$ | left multiplication by $a$ |
| $\vert a\vert$ | the parity of a homogeneous element |
| $\varepsilon$ | a central unit in the involution conditions |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1989), for graded algebras and the exterior algebra as the model case.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the signed inner conjugation and the generation of reflections.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the signed conjugation action on a Clifford algebra.
- Charles A. Weibel, *An Introduction to Homological Algebra*, Cambridge Studies in Advanced Mathematics 38 (Cambridge University Press, 1994), for the graded-structure conventions.
