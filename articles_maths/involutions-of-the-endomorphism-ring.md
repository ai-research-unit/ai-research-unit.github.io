
# __Involutions of the Endomorphism Ring__

## Introduction

An endomorphism ring carries an intrinsic involution as soon as the object it acts on carries a nondegenerate pairing: the **adjoint** of an endomorphism is the unique map that transfers the pairing from one side to the other, and the assignment $T \mapsto T^{*}$ is additive, anti-multiplicative and of order two, that is, an involution of the ring. The unitary elements, those with $T^{*}T = TT^{*} = \mathrm{id}$, are exactly the endomorphisms that preserve the pairing, so the involution of the endomorphism ring is the algebraic form of the preservation of a form; this article fixes the involution and the unitary group at the ring level, and the linear-space version of the same construction is *Involutions of the Endomorphism Algebra*.

This article defines the nondegenerate reflexive pairing on an additive group, constructs the adjoint involution of the endomorphism ring, proves the four laws (additivity, anti-multiplicativity, order two, compatibility with the scalars), identifies the unitary elements and records the two kinds that the symmetry of the pairing produces. It assumes *Groups* for the additive group, *Rings* for the endomorphism ring and *Involutive Rings* for the involution and the unitary elements; the vector-space and module refinements are forward references. Throughout, $(V,+)$ is an additive group, $R$ is a commutative ring with $1 \neq 0$, $B : V\times V \to R$ is a biadditive **perfect** pairing, $E = \operatorname{End}(V)$ is the endomorphism ring, and $\sigma$ is an involution of $R$ when the coefficients are twisted.

## The Pairing and the Adjoint

**Definition.** A biadditive pairing $B : V\times V \to R$ is

**(a) nondegenerate** if $B(x,y) = 0$ for all $y$ implies $x = 0$ and $B(x,y) = 0$ for all $x$ implies $y = 0$;

**(b) reflexive** if $B(x,y) = 0$ exactly when $B(y,x) = 0$;

**(c) perfect** if the map $V \to \operatorname{Hom}(V,R)$, $x \mapsto B(x,-)$, is a bijection.

A perfect pairing is nondegenerate and reflexive, and for each $y$ the functional $x \mapsto B(Tx,y)$ is additive.

**Theorem (the adjoint exists).** For every $T \in E$ and every $y \in V$ there is a unique $T^{*}y \in V$ with

$$
B(Tx,y) = B(x,T^{*}y) \quad \text{for all } x \in V .
$$

The assignment $T \mapsto T^{*}$ is well defined, and it is an **involution of the ring $E$**: it is additive, $(ST)^{*} = T^{*}S^{*}$, $\mathrm{id}^{*} = \mathrm{id}$, and $(T^{*})^{*} = T$.

**Proof.** For fixed $y$ the map $x \mapsto B(Tx,y)$ is additive $V \to R$, hence an element of $\operatorname{Hom}(V,R)$; since $B$ is perfect there is a unique $T^{*}y$ with $B(x,T^{*}y) = B(Tx,y)$ for all $x$, which proves existence and uniqueness. Uniqueness in $y$ makes $T^{*}$ a well-defined map $V \to V$; it is additive because $B(x,T^{*}(y+y')) = B(Tx,y+y') = B(Tx,y)+B(Tx,y') = B(x,T^{*}y+T^{*}y')$ for all $x$, and the pairing is nondegenerate, so $T^{*}(y+y') = T^{*}y+T^{*}y'$. For the anti-multiplicativity, $B(x,(ST)^{*}y) = B(STx,y) = B(S(Tx),y) = B(Tx,S^{*}y) = B(x,T^{*}S^{*}y)$ for all $x$, so $(ST)^{*}y = T^{*}S^{*}y$. The unit is fixed because $B(x,y) = B(x,\mathrm{id}^{*}y)$ for all $x$ gives $\mathrm{id}^{*} = \mathrm{id}$. Finally $B(x,(T^{*})^{*}y) = B(T^{*}x,y)$ for all $x$; by reflexivity this vanishes exactly when $B(y,T^{*}x)$ vanishes, which by the defining identity equals $B(Ty,x)$, and by reflexivity again this vanishes exactly when $B(x,Ty)$ vanishes; since the pairing is nondegenerate, $(T^{*})^{*}y = Ty$ for all $y$, that is $(T^{*})^{*} = T$.

**Remark (compatibility with the coefficients).** If $R$ carries an involution $\sigma$ and the pairing satisfies $B(\lambda x,y) = \lambda B(x,y)$, $B(x,\lambda y) = \sigma(\lambda)B(x,y)$, then the adjoint is $\sigma$-semilinear in the coefficient of a scalar endomorphism: for the endomorphism $\lambda\,\mathrm{id}$ one has $(\lambda\,\mathrm{id})^{*} = \sigma(\lambda)\,\mathrm{id}$. The coefficient involution enters only through the sesquilinearity of the pairing, and the whole construction is that of *Rings with a Semilinear Involution* when $\sigma \neq \mathrm{id}$.

## The Unitary Elements

**Definition.** The **unitary elements** of $(E,B)$ are

$$
U(V,B) = \{T \in E^\times : T^{*}T = TT^{*} = \mathrm{id}\}.
$$

**Proposition.** $U(V,B)$ is a subgroup of the unit group $E^\times$, and $T \in E^\times$ is unitary exactly when $T$ preserves $B$,

$$
T \in U(V,B) \iff B(Tx,Ty) = B(x,y) \ \text{for all } x, y \in V .
$$

**Proof.** If $T$ is unitary then $B(Tx,Ty) = B(T^{*}Tx,y) = B(x,y)$, using the defining identity for $T^{*}$ with the pair $(Tx,y)$ replaced by $(x,Ty)$; conversely, if $T$ preserves $B$ then $B(x,T^{*}Ty) = B(Tx,Ty) = B(x,y)$ for all $x$, so $T^{*}T = \mathrm{id}$ by nondegeneracy, and the same argument on the other side gives $TT^{*} = \mathrm{id}$. The product of two unitary elements is unitary because the adjoint is anti-multiplicative, $(ST)^{*}(ST) = T^{*}S^{*}ST = T^{*}T = \mathrm{id}$, and the inverse of a unitary element is unitary because $T^{*} = T^{-1}$.

**Corollary (the two kinds).** If the pairing is symmetric, $B(y,x) = B(x,y)$, then the involution of $E$ is the **orthogonal** one; if it is antisymmetric, $B(y,x) = -B(x,y)$, then it is the **symplectic** one. With $2$ invertible the endomorphism ring is the sum of the self-adjoint and the skew-adjoint endomorphisms, of dimensions $\tfrac12 n(n+1)$ and $\tfrac12 n(n-1)$ for a symmetric pairing on an object of finite rank $n$ in the matrix case, and exchanged for an antisymmetric one, as in *Matrix Rings with an Involution*.

**Proof.** The transpose type is computed in the matrix case in *Matrix Rings with an Involution*; the endomorphism ring of a finite-rank free object is the matrix ring, and the adjoint of a matrix is its transpose or its symplectic adjoint according to the symmetry, which is the statement.

## Examples

**(a) The standard pairing.** $V = R^n$ with $B(x,y) = \sum_i x_iy_i$ and $R$ a commutative ring; the adjoint of a matrix is its transpose, $X^{*} = X^{\mathrm t}$, so the involution of the matrix ring is the transpose and $U(V,B)$ is the orthogonal group.

**(b) The symplectic pairing.** $V = R^{2n}$ with the pairing $B(x,y) = \sum_i(x_iy_{i+n}-x_{i+n}y_i)$; the adjoint of $X$ is $-JX^{\mathrm t}J$ with $J$ the standard symplectic matrix, the involution is the symplectic one of *Matrix Rings with an Involution*, and $U(V,B)$ is the symplectic group.

**(c) The Hermitian pairing.** $R = \mathbb{C}$ with the conjugation, $B(x,y) = \sum_i \overline{x_i}y_i$; the adjoint is the conjugate transpose and $U(V,B)$ the unitary group. The construction is the second-kind case of the remark.

**(d) The regular pairing of a ring.** On $V = A$ the pairing $B(x,y) = \tau(xy)$, with $\tau$ the regular trace, is symmetric and nondegenerate under the hypothesis of *The Adjoint of the Left Multiplication on a Ring*; the adjoint of the left multiplication $L_a$ is the right multiplication $R_a$, and the unitary elements are the units $u$ with $u^{*} = u^{-1}$.

## Summary

A perfect pairing $B$ on an additive group $V$ defines an **adjoint involution** $T \mapsto T^{*}$ of the endomorphism ring $E = \operatorname{End}(V)$ by $B(Tx,y) = B(x,T^{*}y)$; the adjoint exists and is unique for each $T$, the assignment is additive, anti-multiplicative and of order two, and it is $\sigma$-semilinear in the coefficients when the pairing is sesquilinear with an involution $\sigma$. The unitary elements $U(V,B) = \{T : T^{*}T = TT^{*} = \mathrm{id}\}$ form a subgroup of $E^\times$ and are exactly the endomorphisms preserving the pairing; a symmetric pairing gives the **orthogonal** involution and an antisymmetric one the **symplectic** involution, with the matrix calculations and the unitary groups of *Matrix Rings with an Involution* and *Matrix Rings and the Adjoint*. The specialisation to the regular pairing $B(x,y) = \tau(xy)$ of a ring with involution gives the adjoint of the left multiplication, treated in *The Adjoint of the Left Multiplication on a Ring*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V$, $R$ | Additive group and commutative coefficient ring |
| $B : V\times V \to R$ | Perfect (nondegenerate, reflexive) biadditive pairing |
| $E = \operatorname{End}(V)$ | Endomorphism ring |
| $B(Tx,y) = B(x,T^{*}y)$ | Defining identity of the adjoint |
| $T \mapsto T^{*}$ | Adjoint involution of $E$ |
| $U(V,B)$ | Unitary group: $T^{*}T = TT^{*} = \mathrm{id}$, equivalently $B(Tx,Ty) = B(x,y)$ |
| symmetric $B$ / antisymmetric $B$ | Orthogonal / symplectic involution |
| $B = \tau(xy)$ on $A$ | Regular pairing of a ring; $L_a^{*} = R_a$ |
| $\sigma$ | Coefficient involution; adjoint is $\sigma$-semilinear when $B$ is sesquilinear |

## Further Reading

- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the adjoint involution of an endomorphism ring and the unitary elements.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for the orthogonal and symplectic involutions and their relation to the forms they preserve.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the involution of a ring, the unitary elements and the sesquilinear case.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for bilinear and sesquilinear forms, nondegeneracy and the reflexive pairings.
