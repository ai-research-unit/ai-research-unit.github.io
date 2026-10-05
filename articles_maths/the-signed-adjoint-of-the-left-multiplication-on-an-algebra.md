# __The Signed Adjoint of the Left Multiplication on an Algebra__

## Introduction

The signed left multiplication is the one-sided operator $\Lambda(a)(x)=a\,\alpha(x)$, the left multiplication composed with a grade involution; it is the sandwich $S_{a,1}$ and the one-sided half of the signed theory. Its **signed adjoint** with respect to the twisted pairing is again a signed left multiplication,

$$
\Lambda(a)^{*_\sigma}=S_{\delta(a),\delta(1)}=\Lambda\bigl(\delta(a)\bigr), \qquad \delta=\sigma\alpha,
$$

so the signed adjoint does **not** switch the side, in contrast with the unsigned adjoint of *The Adjoint of the Left Multiplication on an Algebra*, which sends $L_a=L(a)$ to the right multiplication $R_a$. The plain adjoint does switch the side, $\Lambda(a)^{*}=R_{\alpha(a)}\alpha=S_{1,\alpha(a)}$, and the two adjoints are related by the conjugation $c_{\sigma}(T)=\sigma T\sigma$ of *The Adjoint in an Involutive Algebra*. The signed left multiplication is unitary for the twisted pairing exactly when $\delta(a)\alpha(a)=1$, that is exactly when $\alpha(a)$ is a unitary element of the algebra, and it is an involution exactly when $a\alpha(a)=1$.

This article computes the signed adjoint of the signed left multiplication, its inverse and its composition, its self-adjointness, its unitarity and its involution conditions, and its relation to the signed sandwich and to the reflection. It assumes *The Signed Left Multiplication on an Algebra* for the operator and its elementary identities, *The Signed Sandwich on an Algebra* for the composition and the inverse of the sandwiched operators, *The Signed Adjoint Sandwich on an Algebra* for the signed adjoint and the unitarity condition, *The Adjoint of the Left Multiplication on an Algebra* for the unsigned adjoints, *The Signed Adjoint of the Reflection on an Algebra* for the two-sided case, *Involutions of the Operator Algebra* and *The Adjoint in an Involutive Algebra* for the adjoint operation and the two pairings, and *Unitary Elements of an Involutive Algebra* for the unitary elements. The module case is *The Signed Adjoint of the Left Multiplication on a Module over an Algebra* of the later category *Linear Spaces over Bilinear Algebras*; the analytic case is Part II. This article stays inside Part I: no distance, norm, form with a norm, topology or limit.

Throughout, $k$ is a field of characteristic not two, $A$ is a finite-dimensional unital associative $k$-algebra, $\tau$ is a trace whose pairing $\langle x,y\rangle=\tau(xy)$ is nondegenerate, $\sigma$ is an involution of $A$ with $\tau(\sigma(x))=\tau(x)$, and $\alpha$ is an involutive automorphism of $A$ commuting with $\sigma$ and preserving the trace. The twist is $\delta=\sigma\alpha$, the twisted pairing is $\{x,y\}=\tau(x\sigma(y))$, the unsigned left multiplication is $L(a)(x)=ax$, the signed left multiplication is $\Lambda(a)=S_{a,1}=L(a)\alpha=\alpha L(\alpha(a))$, the signed sandwich is $S_{a,b}(x)=a\alpha(x)b$, and the adjoints for the two pairings are $T^{*}$ and $T^{*_\sigma}$.

## The Signed Adjoint

**Theorem.** With respect to the twisted pairing,

$$
\Lambda(a)^{*_\sigma}=S_{\delta(a),\,\delta(1)}=\Lambda\bigl(\delta(a)\bigr),
$$

so the signed adjoint of the signed left multiplication by $a$ is the signed left multiplication by $\delta(a)$, and it stays on the **same side**; the assignment $a\mapsto\delta(a)$ on the parameter is the element involution twisted by the grade involution.

*Proof.* $\Lambda(a)=S_{a,1}$ by *The Signed Left Multiplication on an Algebra*, and the signed adjoint of a sandwich is $S_{a,b}^{*_\sigma}=S_{\delta(a),\delta(b)}$ by *The Signed Adjoint Sandwich on an Algebra*; with $b=1$ and $\delta(1)=1$ this is $S_{\delta(a),1}=\Lambda(\delta(a))$. Since $\delta=\sigma\alpha$ is an anti-automorphism of order two and $\Lambda$ is injective, the assignment is involutive.

**Corollary (a `*`-map from the twisted algebra).** The signed left regular map intertwines the twisted involution $\delta$ with the adjoint,

$$
\Lambda\bigl(\delta(a)\bigr)=\Lambda(a)^{*_\sigma},
$$

so it is a `*`-map from the involutive algebra $(A,\delta)$ to the involutive algebra $(E,*_\sigma)$; it is not a homomorphism of algebras, because $\Lambda(a)\Lambda(b)=L(a\alpha(b))$ is an unsigned left multiplication.

*Proof.* The intertwining is the theorem; the failure of multiplicativity is the composition computed below, and it is the reason the signed left regular map is a `*`-map and not a `*`-homomorphism.

**Corollary (specialization).** For $\alpha=\mathrm{id}$ one has $\delta=\sigma$ and $\Lambda(a)=L(a)$, so the theorem reduces to $L(a)^{*_\sigma}=L(\sigma(a))$ of *The Adjoint of the Left Multiplication on an Algebra*; for the twisted pairing the signed adjoint of the signed left multiplication is the signed left multiplication by the $\delta$-image, and the unsigned adjoint of the unsigned one is the unsigned right multiplication.

*Proof.* Both statements are the definitions read at $\alpha=\mathrm{id}$, where $S_{a,b}=T_{a,b}$ and $\delta=\sigma$.

## The Plain Adjoint and the Two Sides

**Proposition.** With respect to the plain pairing,

$$
\Lambda(a)^{*}=S_{\alpha(1),\,\alpha(a)}=S_{1,\,\alpha(a)}=R_{\alpha(a)}\,\alpha,
$$

so the plain adjoint of the signed left multiplication is the signed sandwich $S_{1,\alpha(a)}$, the operator $x\mapsto\alpha(x)\alpha(a)$, which multiplies on the **other** side after the twist; and the two adjoints are related by the conjugation of the operator algebra,

$$
\Lambda(a)^{*_\sigma}=c_{\sigma}\bigl(\Lambda(a)^{*}\bigr)=\sigma\,R_{\alpha(a)}\,\alpha\,\sigma .
$$

*Proof.* The plain adjoint of a signed sandwich is $S_{a,b}^{*}=S_{\alpha(b),\alpha(a)}$ by *The Signed Adjoint Sandwich on an Algebra*, and with $a$ in the first place and $b=1$ this is $S_{\alpha(1),\alpha(a)}=S_{1,\alpha(a)}$; the identification $R_{\alpha(a)}\alpha(x)=\alpha(x)\alpha(a)$ is the definition. The relation is the dictionary $T^{*_\sigma}=\sigma T^{*}\sigma$ of *The Adjoint in an Involutive Algebra* applied to $T=\Lambda(a)$, with the theorem used to identify the result.

**Remark.** The distinction between the two adjoints is exactly the distinction between the sides: the plain pairing reads the signed left multiplication as a one-sided operator and sends it to the other side, while the twisted pairing reads it as a `*`-map of the twisted involutive algebra and keeps it where it is. The unsigned adjoint of $L(a)$ is $R(a)$, the plain adjoint of $\Lambda(a)$ is $S_{1,\alpha(a)}$, and the twisted adjoint of $\Lambda(a)$ is $\Lambda(\delta(a))$; the side switch is therefore the price of the untwisted pairing, and the twist $\delta$ is the correction that removes it.

## Invertibility and Composition

**Theorem.** The signed left multiplication $\Lambda(a)$ is invertible exactly when $a$ is a unit of $A$, with

$$
\Lambda(a)^{-1}=\Lambda\bigl(\alpha(a)^{-1}\bigr) ;
$$

its products obey

$$
\Lambda(a)\Lambda(b)=L\bigl(a\alpha(b)\bigr), \qquad \Lambda(a)L(b)=\Lambda\bigl(a\alpha(b)\bigr), \qquad L(a)\Lambda(b)=\Lambda(ab),
$$

and a product of three is again signed, $\Lambda(a)\Lambda(b)\Lambda(c)=\Lambda(a\alpha(b)c)$. The signed left multiplications therefore generate the union of the unsigned and the signed left multiplications, and they form a semigroup, closed under inverses on the units.

*Proof.* $\Lambda(a)$ is the composite $L(a)\alpha$ of the invertible operator $\alpha$ with $L(a)$, so it is invertible exactly when $L(a)$ is, that is when $a$ is a unit; then $\Lambda(\alpha(a)^{-1})\Lambda(a)(x)=\alpha(a)^{-1}\alpha(a\alpha(x))=\alpha(a)^{-1}\alpha(a)x=x$. The first product rule is the direct computation $\Lambda(a)(b\alpha(x))=a\alpha(b\alpha(x))=a\alpha(b)x$; the latter two are the identities (d) of *The Signed Left Multiplication on an Algebra*; the threefold product follows by applying the third to $\Lambda(a)\Lambda(b)=L(a\alpha(b))$ and $\Lambda(c)$. Stability under inversion is the inverse formula, and the products of three being signed is the last identity.

**Corollary.** The multiplicative closure of the left multiplications and the signed left multiplications is their union $L(A)\cup\Lambda(A)$, with $\Lambda(A)=L(A)\alpha$ the coset of the left multiplications; the product of two signed left multiplications is always an unsigned left multiplication, and the product of three is signed again.

*Proof.* $\Lambda(a)\Lambda(b)=L(a\alpha(b))$ lies in $L(A)$, and $\Lambda(a)\Lambda(b)\Lambda(c)=\Lambda(a\alpha(b)c)$ lies in $\Lambda(A)$; the two cosets $L(A)$ and $L(A)\alpha$ are therefore closed under products in the pattern of the parity, and they exhaust the closure.

## Self-Adjointness, Unitarity and Involution

**Theorem.** For the twisted pairing,

$$
\Lambda(a) \text{ is self-adjoint} \iff \delta(a)=a, \qquad
\Lambda(a) \text{ is unitary} \iff \delta(a)\alpha(a)=1, \qquad
\Lambda(a) \text{ is an involution} \iff a\alpha(a)=1 .
$$

The unitary signed left multiplications are exactly the operators $\Lambda(a)$ with $\alpha(a)$ a unitary element of the algebra, and they form a subgroup of the unit group of $E$ isomorphic to a subgroup of the units of $A$.

*Proof.* Injectivity of $\Lambda$ makes $\Lambda(\delta(a))=\Lambda(a)$ equivalent to $\delta(a)=a$; for unitarity, $\Lambda(a)^{*_\sigma}\Lambda(a)=\Lambda(\delta(a))\Lambda(a)=L(\delta(a)\alpha(a))$ by the product rule, and a left multiplication is the identity exactly when its parameter is $1$, so $\delta(a)\alpha(a)=1$; with $\delta=\sigma\alpha$ and $v=\alpha(a)$ this is $\sigma(v)v=1$, the unitarity of $v$ in $(A,\sigma)$. For the involution, $\Lambda(a)^{2}=L(a\alpha(a))$, which is the identity exactly when $a\alpha(a)=1$. The group statement is *Unitary Operators of an Involutive Algebra* applied to the image.

**Corollary.** A signed left multiplication that is both self-adjoint and unitary is its own inverse adjoint, $\Lambda(a)^{*_\sigma}=\Lambda(a)=\Lambda(a)^{-1}$, and this happens exactly when $\delta(a)=a=\alpha(a)^{-1}$, that is when $a=\alpha(a)^{-1}$ and $a$ is fixed by $\delta$. In particular the self-adjoint unitary signed left multiplications are the operators with $a\alpha(a)=1$ and $\delta(a)=a$, and the grade involution $a=1$ is one of them.

*Proof.* Self-adjointness is $\delta(a)=a$ and unitarity is $\delta(a)=\alpha(a)^{-1}$, and the two together are $a=\alpha(a)^{-1}$; the case $a=1$ gives $\Lambda(1)=\alpha$, which is self-adjoint and of order two.

**Corollary (the parameter duality).** The map $a\mapsto\alpha(a)^{-1}$ on the units produces the inverse of a signed left multiplication, and the unitary condition $\delta(a)\alpha(a)=1$ reads $\sigma(v)v=1$ for the element $v=\alpha(a)$, so the unitary signed left multiplications are exactly the operators $\Lambda(a)$ whose parameter has $\alpha(a)$ unitary in $(A,\sigma)$.

*Proof.* The inverse formula is the theorem, and with $\delta=\sigma\alpha$ the condition $\delta(a)\alpha(a)=1$ is $\sigma(\alpha(a))\alpha(a)=1$, which is the definition of the unitarity of $\alpha(a)$.

## Relation to the Sandwich and the Reflection

**Theorem.** The signed sandwich is the product of a signed left multiplication and a right multiplication,

$$
S_{a,b}=\Lambda(a)\,R_{\alpha(b)}=\alpha\,T_{\alpha(a),\alpha(b)},
$$

and the signed conjugation is the special case

$$
\rho_u=S_{u,u^{-1}}=\Lambda(u)\,R_{\alpha(u)^{-1}} .
$$

The one-sided signed operators therefore generate the two-sided ones, and the unsigned sandwich is recovered as $T_{a,b}=L(a)R(b)=S_{a,b}\alpha$.

*Proof.* $\Lambda(a)R_{\alpha(b)}(x)=\Lambda(a)(x\alpha(b))=a\alpha(x\alpha(b))=a\alpha(x)\alpha(\alpha(b))=a\alpha(x)b$; the second form is the reading $S_{a,b}=\alpha T_{\alpha(a),\alpha(b)}$ of *The Signed Sandwich on an Algebra*, since $\alpha(\alpha(a)x\alpha(b))=a\alpha(x)b$. The reflection is the case $b=u^{-1}$, and the last identity is $S_{a,b}\alpha=\alpha T_{\alpha(a),\alpha(b)}\alpha=T_{a,b}$.

**Corollary (the one-sided reading of the reflections).** Every reflection is a signed left multiplication followed by the inverse right multiplication of the $\alpha$-image, and its adjoint is the signed left multiplication by $\delta(u)$ followed by the inverse right multiplication of $\alpha\delta(u)$; the side switch of the plain pairing is confined to the second factor, and the signed pairing keeps both factors on their sides.

*Proof.* The first identity is the theorem at $b=u^{-1}$; the adjoint statement is the same identity applied to $\delta(u)$, since $\rho_u^{*_\sigma}=\rho_{\delta(u)}$ by *The Signed Adjoint of the Reflection on an Algebra*.

## Examples

**(a) The trivial grading.** For $\alpha=\mathrm{id}$ the signed left multiplication is the left multiplication, $\Lambda(a)=L(a)$, the signed adjoint is $L(\sigma(a))$, the plain adjoint is $R(a)$, and the unitarity condition is $\sigma(a)a=1$; the whole article reduces to *The Adjoint of the Left Multiplication on an Algebra*.

**(b) The group algebra with a parity.** $A=k[G]$ with a parity homomorphism $\chi$, $\sigma(g)=g^{-1}$ and $\alpha(g)=\chi(g)g$; then $\Lambda(g)(h)=\chi(h)gh$ and $\Lambda(g)^{*_\sigma}=\Lambda(\delta(g))$ with $\delta(g)=\chi(g)g^{-1}$. The signed left multiplication is unitary exactly when $\delta(g)\alpha(g)=1$, that is $g^{-2}=1$, which for a group of exponent two is every element.

**(c) The matrix algebra with the transpose.** $A=M_n(k)$ with $\sigma$ the matrix transpose and $\alpha$ the grade involution of a $\mathbb{Z}/2$-grading; the twist is $\delta(X)=\alpha(X)^{\mathsf{T}}$, the signed adjoint is $\Lambda(X)^{*_\sigma}=\Lambda(\delta(X))$, and the operator is unitary exactly when $\alpha(X)^{\mathsf{T}}X=1$.

**(d) The exterior algebra.** For $A=\Lambda(V)$ with the parity grading and $\sigma$ the reversal of a word up to sign, the signed left multiplication by an odd element is the operator that interchanges the parity parts, and its twisted adjoint is the signed left multiplication by the $\delta$-image; the graded case is *The Graded Adjoint Action on a Module over an Algebra*.

## Summary

The signed left multiplication $\Lambda(a)=S_{a,1}=L(a)\alpha=\alpha L(\alpha(a))$ has twisted adjoint $\Lambda(a)^{*_\sigma}=\Lambda(\delta(a))$ with $\delta=\sigma\alpha$: the signed adjoint does not switch the side, and the signed left regular map is a `*`-map from $(A,\delta)$ to $(E,*_\sigma)$, though not a homomorphism, since $\Lambda(a)\Lambda(b)=L(a\alpha(b))$. The plain adjoint does switch the side, $\Lambda(a)^{*}=S_{1,\alpha(a)}=R_{\alpha(a)}\alpha$, and the two adjoints differ by the conjugation $c_{\sigma}(T)=\sigma T\sigma$. The operator is invertible exactly when $a$ is a unit, with $\Lambda(a)^{-1}=\Lambda(\alpha(a)^{-1})$; it is self-adjoint for the twisted pairing exactly when $\delta(a)=a$, unitary exactly when $\delta(a)\alpha(a)=1$, equivalently when $\alpha(a)$ is a unitary element, and an involution exactly when $a\alpha(a)=1$. The signed sandwich is the product $\Lambda(a)R_{\alpha(b)}$ and the reflection is $\Lambda(u)R_{\alpha(u)^{-1}}$, so the side switch of the plain pairing is confined to the second factor while the signed pairing keeps both factors on their sides. The unsigned case is the specialization $\alpha=\mathrm{id}$, and the module case is the next category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L(a)$, $R(a)$ | the left and the right multiplication by $a$ |
| $\alpha$, $\sigma$, $\delta=\sigma\alpha$ | the grade involution, the involution, and their twist |
| $\Lambda(a)=S_{a,1}=L(a)\alpha=\alpha L(\alpha(a))$ | the signed left multiplication |
| $\Lambda(a)^{*_\sigma}=\Lambda(\delta(a))$ | the signed adjoint; no side switch |
| $\Lambda(a)^{*}=S_{1,\alpha(a)}=R_{\alpha(a)}\alpha$ | the plain adjoint; side switch |
| $\Lambda(a)^{*_\sigma}=c_{\sigma}(\Lambda(a)^{*})$ | the two adjoints related by the conjugation |
| $\Lambda(a)^{-1}=\Lambda(\alpha(a)^{-1})$ | the inverse, for a unit $a$ |
| $\Lambda(a)\Lambda(b)=L(a\alpha(b))$ | the composition |
| $\Lambda(a)$ self-adjoint $\iff \delta(a)=a$ | self-adjointness for the twisted pairing |
| $\delta(a)\alpha(a)=1$ | the unitarity condition |
| $a\alpha(a)=1$ | the involution condition |
| $S_{a,b}=\Lambda(a)R_{\alpha(b)}$ | the sandwich from the one-sided operators |
| $\rho_u=\Lambda(u)R_{\alpha(u)^{-1}}$ | the reflection from the one-sided operators |

## Further Reading

- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the regular representation, its signed deformations and the trace form.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the adjoint of a one-sided operator under an involution and the unitary elements.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for the regular representation, the opposite algebra and the adjoint under a pairing.
- Matej Brešar, *Introduction to Noncommutative Algebra* (Springer, 2014), for the one-sided multiplications, their compositions and their adjoint properties.
