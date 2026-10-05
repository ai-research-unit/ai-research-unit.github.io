# __The Adjoint in an Involutive Algebra__

## Introduction

On an involutive algebra $(A,\sigma)$ the pairing of the category can be twisted by the involution, $\{x,y\}=\tau(x\sigma(y))$, and the adjoint of an operator depends on which of the two pairings is used. This article develops the **adjoint operation** of an involutive algebra: the existence and the uniqueness of the adjoint for a pairing, the elementary laws it obeys, the passage from the plain pairing to the twisted one, and the two ways in which an adjoint can be taken — the adjoint and the **left adjoint** — which coincide exactly when the pairing is reflexive. The central result is a dictionary: $T^{*_\sigma}=\sigma\,T^{*}\,\sigma$, the twisted adjoint is the conjugate of the plain one by the involution of the elements, so the involution of the elements and the adjoint of the operators are two structures that meet only after the conjugation is applied.

This article is the second of the group. It assumes the operator algebra $E=\operatorname{End}_k(A)$ and the involution $T\mapsto T^{*}$ of *Involutions of the Operator Algebra*, the trace and the pairing of *Frobenius Algebras*, the involutions of an algebra of *Involutive Bilinear Algebras*, and the one-sided multiplications of *Left and Right Multiplication*. The adjoints of the one-sided multiplications are computed in *The Adjoint of the Left Multiplication on an Algebra*; the adjoints of the signed and of the graded operators are *The Signed Adjoint Sandwich on an Algebra* and *The Graded Adjoint Action on a Module over an Algebra*; and the forms, the norms, the Hilbert-space adjoint and the positivity are Part II and *Operator Algebras*, named as the owner and not used.

Throughout, $k$ is a field of characteristic not two, $A$ is a finite-dimensional unital associative $k$-algebra, $\sigma$ is an involution of $A$, and $\tau : A \to k$ is a trace with $\tau(\sigma(x))=\tau(x)$ whose pairing $\langle x,y\rangle=\tau(xy)$ is nondegenerate. The **twisted pairing** is $\{x,y\}=\tau(x\sigma(y))$; the adjoint of $T \in E$ for the plain pairing is $T^{*}$ and for the twisted pairing is $T^{*_\sigma}$, and the **left adjoint** of $T$ is written ${}^{*}T$.

## The Twisted Pairing

**Definition.** The **twisted pairing** of the involutive algebra $(A,\sigma)$ attached to the trace $\tau$ is

$$
\{x,y\}=\tau\bigl(x\,\sigma(y)\bigr).
$$

**Proposition.** The twisted pairing is symmetric and nondegenerate, and it is obtained from the plain one by the involution of the elements,

$$
\{x,y\}=\langle x,\sigma(y)\rangle=\langle \sigma(x),y\rangle, \qquad\text{so}\qquad \{x,y\}=\{y,x\}.
$$

*Proof.* The first identity is the definition. For the second, $\langle\sigma(x),y\rangle=\tau(\sigma(x)y)=\tau(\sigma(\sigma(x)y))=\tau(\sigma(y)x)=\tau(x\sigma(y))=\{x,y\}$, using the $\sigma$-invariance and the cyclicity of $\tau$ and the anti-multiplicativity $\sigma(\sigma(x)y)=\sigma(y)x$. For symmetry, use the $\sigma$-invariance and the cyclicity of $\tau$: $\{y,x\}=\tau(y\sigma(x))=\tau(\sigma(y\sigma(x)))=\tau(x\sigma(y))=\{x,y\}$, since $\sigma(y\sigma(x))=\sigma(\sigma(x))\sigma(y)=x\sigma(y)$ by the anti-multiplicativity of $\sigma$ and $\sigma^{2}=\mathrm{id}$. For nondegeneracy, if $\{x,y\}=0$ for all $y$ then $\langle x,\sigma(y)\rangle=0$ for all $y$; as $y$ ranges over $A$ so does $\sigma(y)$, and the nondegeneracy of the plain pairing gives $x=0$.

The twisted pairing is the plain pairing composed with the involution in the second argument, and the two carry the same information as soon as $\sigma$ is known. It is the pairing adapted to the involutive structure: it is the pairing for which the one-sided multiplications have adjoints on the same side, as the dictionary below shows.

**Example (the matrix algebra and the transpose).** For $A=M_n(k)$, $\sigma$ the transpose and $\tau=\operatorname{Tr}$, the twisted pairing is $\{X,Y\}=\operatorname{Tr}(XY^{\mathsf{T}})=\sum_{i,j}X_{ij}Y_{ij}$, the pairing of the coefficient matrices of $X$ and $Y$; it is symmetric and nondegenerate, while the plain pairing $\langle X,Y\rangle=\operatorname{Tr}(XY)$ pairs $X$ with $Y$ through the matrix product.

**Example (the group algebra).** For $A=k[G]$ with $G$ finite, $\sigma(g)=g^{-1}$ and $\tau$ the coefficient of the identity, the twisted pairing is $\{g,h\}=\tau(gh^{-1})=\delta_{g,h}$, the orthonormal pairing of the group basis, while the plain pairing is $\langle g,h\rangle=\tau(gh)=\delta_{g,h^{-1}}$ and pairs $g$ with $h=g^{-1}$.

## The Adjoint for the Twisted Pairing

**Theorem.** Let $T \in E$ have adjoint $T^{*}$ for the plain pairing. Then $T$ has an adjoint for the twisted pairing, written $T^{*_\sigma}$, and

$$
T^{*_\sigma}=\sigma\,T^{*}\,\sigma .
$$

The twisted adjoint is the conjugate of the plain adjoint by the involution of the elements, and the assignment $T\mapsto T^{*_\sigma}$ is an involution of $E$ of order two.

*Proof.* By the relation between the pairings, $\{Tx,y\}=\langle Tx,\sigma(y)\rangle=\langle x,T^{*}\sigma(y)\rangle$, using the definition of $T^{*}$ in the second step. On the other side, $\{x,\sigma T^{*}\sigma\,y\}=\langle x,\sigma(\sigma T^{*}\sigma\,y)\rangle=\langle x,T^{*}\sigma(y)\rangle$, because $\sigma^{2}=\mathrm{id}$. The two are equal for all $x$ and $y$, and nondegeneracy of the twisted pairing gives $T^{*_\sigma}=\sigma T^{*}\sigma$. For order two, $(\sigma T^{*}\sigma)^{*}=\sigma^{*}T^{**}\sigma^{*}=\sigma T\sigma$, because the involution of the elements is self-adjoint for the plain pairing, $\langle\sigma(x),y\rangle=\tau(\sigma(x)y)=\tau(\sigma(\sigma(x)y))=\tau(x\sigma(y))=\langle x,\sigma(y)\rangle$; hence $(T^{*_\sigma})^{*_\sigma}=\sigma(\sigma T\sigma)\sigma=T$.

**Corollary (the elementary laws for the twisted adjoint).** For $S,T \in E$,

$$
(S+T)^{*_\sigma}=S^{*_\sigma}+T^{*_\sigma}, \qquad (\lambda T)^{*_\sigma}=\lambda T^{*_\sigma}, \qquad (ST)^{*_\sigma}=T^{*_\sigma}S^{*_\sigma}, \qquad (T^{*_\sigma})^{*_\sigma}=T, \qquad \mathrm{id}^{*_\sigma}=\mathrm{id} .
$$

*Proof.* Each law is the corresponding law of *Involutions of the Operator Algebra* conjugated by $\sigma$: the conjugation $T\mapsto\sigma T\sigma$ is $k$-linear, unital and multiplicative, so it carries $+$, $\lambda$ and the composite to themselves and reverses the order of the adjoints, which are already reversed.

**Corollary (the two involutions agree where the adjoint commutes with the involution).** The plain and the twisted adjoints of $T$ coincide, $T^{*}=T^{*_\sigma}$, exactly when $T^{*}$ commutes with $\sigma$.

*Proof.* $T^{*_\sigma}=T^{*}$ is $\sigma T^{*}\sigma=T^{*}$, which is $\sigma T^{*}=T^{*}\sigma$.

**Corollary (the involution of the elements on the operators).** The map $c_{\sigma}(T)=\sigma T\sigma$ is an involutive automorphism of $E$, and the two adjoint operations are exchanged by it,

$$
c_{\sigma}(T^{*})=T^{*_\sigma}, \qquad c_{\sigma}(T^{*_\sigma})=T^{*} .
$$

*Proof.* The first identity is the theorem read as an equation of maps; the second is the case of the first with $T$ replaced by $T^{*_\sigma}$ and order two used, $c_{\sigma}(T^{*_\sigma})=(T^{*_\sigma})^{*}=T^{*}$.

## The Left and the Right Adjoint

**Definition.** Let $T \in E$ and let $\langle\cdot,\cdot\rangle$ be a pairing. A **left adjoint** of $T$ for the pairing is a map ${}^{*}T \in E$ with

$$
\langle y,Tx\rangle=\langle {}^{*}T\,y,x\rangle \qquad \text{for all } x,y \in A .
$$

The adjoint $T^{*}$ of the preceding sections is the adjoint taken on the other side, $\langle Tx,y\rangle=\langle x,T^{*}y\rangle$; the left adjoint is the adjoint taken with the two arguments of the pairing in the reverse order.

**Theorem.** For a reflexive pairing the left adjoint exists, is unique, and equals the adjoint, ${}^{*}T=T^{*}$; the pairings of this category are symmetric and hence reflexive, so for them the two adjoints are one and the same operator. Without reflexivity a left adjoint may fail to exist, and when it exists it is the adjoint for the opposite pairing $\langle y,x\rangle$.

*Proof.* For a symmetric pairing, $\langle y,Tx\rangle=\langle Tx,y\rangle=\langle x,T^{*}y\rangle=\langle T^{*}y,x\rangle$, so $T^{*}$ satisfies the defining identity of ${}^{*}T$, and uniqueness is the nondegeneracy argument of *Involutions of the Operator Algebra*. For a reflexive pairing with sign $\varepsilon$, $\langle y,Tx\rangle=\varepsilon\langle Tx,y\rangle=\varepsilon\langle x,T^{*}y\rangle=\langle T^{*}y,x\rangle$ and the same conclusion holds; without reflexivity nothing relates $\langle y,Tx\rangle$ to $\langle Tx,y\rangle$, and the left adjoint, when it exists, is by definition the adjoint for the pairing with the arguments interchanged.

**Remark.** The distinction is therefore not a second adjoint of the same pairing but a second pairing: the left adjoint of the plain pairing is the adjoint for the pairing $\langle y,x\rangle$, which for the symmetric pairings of this category is the plain pairing itself. The distinction becomes real for a pairing that is not reflexive and for a sesquilinear pairing, where the involution of the coefficients governs the passage; the module case is *The Adjoint of a Module Homomorphism* of the later category *Linear Spaces over Bilinear Algebras*.

## The Adjoints of the One-Sided Multiplications

**Theorem.** For $a,b \in A$ the one-sided multiplications have adjoints

$$
L_a^{*}=R_a, \qquad R_b^{*}=L_b \qquad \text{(plain pairing)}, \qquad
L_a^{*_\sigma}=L_{\sigma(a)}, \qquad R_b^{*_\sigma}=R_{\sigma(b)} \qquad \text{(twisted pairing)} .
$$

The adjoint operation therefore **exchanges** the two sides for the plain pairing and **preserves** each side for the twisted one; and the twisting map is the one that turns the exchange into a preservation, in the sense $c_{\sigma}(L_a^{*})=c_{\sigma}(R_a)=L_{\sigma(a)}=L_a^{*_\sigma}$.

*Proof.* The plain case is the compatibility of the pairing, $\langle L_ax,y\rangle=\langle ax,y\rangle=\langle x,ya\rangle=\langle x,R_ay\rangle$, and the second identity is the same computation with the sides exchanged; the full treatment is *The Adjoint of the Left Multiplication on an Algebra*. For the twisted case, apply the theorem $T^{*_\sigma}=c_{\sigma}(T^{*})$ to $T=L_a$: $L_a^{*_\sigma}=\sigma R_a\sigma$, and $\sigma R_a\sigma(x)=\sigma(\sigma(x)a)=\sigma(a)x=L_{\sigma(a)}x$. The right-multiplication case is the same computation.

**Corollary.** The left regular representation is a `*`-representation for the twisted pairing,

$$
L_{\sigma(a)}=L_a^{*_\sigma}, \qquad \text{that is} \qquad L\bigl(\sigma(a)\bigr)=\bigl(L(a)\bigr)^{*_\sigma},
$$

whereas for the plain pairing it is not, since $L_a^{*}=R_a$ and not $L_{\sigma(a)}$ in general. The agreement of the element involution and the operator involution is thus the choice of the twisted pairing, and it is proved here and not assumed.

*Proof.* The first identity is the theorem; the failure for the plain pairing is the same identity read with the wrong side, and $R_a=L_{\sigma(a)}$ would force $ax=xa$ for all $x$.

**Example (the matrix algebra).** For $A=M_n(k)$ with the transpose and the trace, $L_X^{*}=R_X$ and $L_X^{*_\sigma}=L_{X^{\mathsf{T}}}$; the twisted adjoint of the left multiplication by $X$ is the left multiplication by the transpose of $X$.

**Example (the group algebra).** For $A=k[G]$ with $\sigma(g)=g^{-1}$, the twisted adjoint of $L_g$ is $L_{g^{-1}}$; the plain adjoint is $R_g$. The left regular representation with the twisted pairing is a `*`-representation of the group algebra with the inversion.

## Examples

**(a) The commutative case.** If $A$ is commutative then $L_a=R_a$ and the plain adjoint of $L_a$ is $L_a$ itself; the twisted adjoint is $L_{\sigma(a)}$, and the two agree exactly on the symmetric elements. The symmetric and the twisted adjoints of the one-sided multiplications are the two faces of the same operator in a commutative algebra.

**(b) The scalar extension.** If $A=B\times B$ is a product of two copies of an algebra $B$ with the exchange involution $\sigma(x,y)=(y,x)$, the twisted pairing pairs the first factor with the first and the second with the second, while the plain pairing pairs the two factors across; the twisted adjoint of $L_{(a,b)}$ is $L_{(b,a)}=L_{\sigma(a,b)}$.

**(c) The trivial involution.** For $\sigma=\mathrm{id}$ the twisted pairing is the plain one and $T^{*_\sigma}=T^{*}$; the two involutions of $E$ coincide, and every statement of the article reduces to the corresponding statement of *Involutions of the Operator Algebra*.

## Summary

An involutive algebra $(A,\sigma)$ with a $\sigma$-invariant trace carries two pairings — the plain $\langle x,y\rangle=\tau(xy)$ and the twisted $\{x,y\}=\tau(x\sigma(y))=\langle x,\sigma(y)\rangle$ — both symmetric and nondegenerate, and two adjoint operations on the operator algebra $E=\operatorname{End}_k(A)$: the plain adjoint $T^{*}$ and the twisted adjoint $T^{*_\sigma}$, related by

$$
T^{*_\sigma}=\sigma\,T^{*}\,\sigma,
$$

so that the twisted adjoint is the plain adjoint conjugated by the involution of the elements. Each is an involution of $E$ with the elementary laws $(ST)^{*}=S^{*}T^{*}$ and $(ST)^{*_\sigma}=T^{*_\sigma}S^{*_\sigma}$; the two agree on $T$ exactly when $T^{*}$ commutes with $\sigma$, and the conjugation $c_{\sigma}(T)=\sigma T\sigma$ is the involutive automorphism of $E$ that exchanges them. The adjoint and the left adjoint of a map coincide for a reflexive pairing, and the pairings of this category are symmetric, so for them the two coincide; the distinction is real only for a pairing without reflexivity, where the left adjoint is the adjoint for the opposite pairing. Applied to the one-sided multiplications the dictionary reads $L_a^{*}=R_a$, $R_b^{*}=L_b$ for the plain pairing and $L_a^{*_\sigma}=L_{\sigma(a)}$, $R_b^{*_\sigma}=R_{\sigma(b)}$ for the twisted one: the adjoint exchanges the sides in the first case and preserves them in the second, and the left regular representation is a `*`-representation for the twisted pairing.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$, $A$ | the field, and a finite-dimensional unital associative $k$-algebra |
| $\sigma$, $\sigma(x)$ | the involution of the elements and its image |
| $\tau$, $\langle x,y\rangle=\tau(xy)$ | the $\sigma$-invariant trace and the plain pairing |
| $\{x,y\}=\tau(x\sigma(y))$ | the twisted pairing |
| $\{x,y\}=\langle x,\sigma(y)\rangle$ | the twisted pairing read from the plain one |
| $T^{*}$, $T^{*_\sigma}$ | the plain adjoint and the twisted adjoint |
| $T^{*_\sigma}=\sigma T^{*}\sigma$ | the dictionary between the two adjoints |
| ${}^{*}T$ | the left adjoint, equal to $T^{*}$ for a reflexive pairing |
| $(ST)^{*_\sigma}=T^{*_\sigma}S^{*_\sigma}$ | anti-multiplicativity of the twisted adjoint |
| $c_{\sigma}(T)=\sigma T\sigma$ | the involutive automorphism exchanging the two adjoints |
| $L_a^{*}=R_a$, $L_a^{*_\sigma}=L_{\sigma(a)}$ | the adjoints of the one-sided multiplications |
| $L(\sigma(a))=L(a)^{*_\sigma}$ | the regular representation as a `*`-representation |

## Further Reading

- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the twisted pairing of an involutive algebra and the adjoint of the one-sided multiplications.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the trace form, the adjoint involution and the regular representation.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for the duality of a module, the adjoint under a pairing and the transpose.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for the adjoint involution, the unitary group and the sesquilinear conventions of an algebra with involution.
