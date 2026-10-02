
# __The Involution on the Enveloping Algebra of a Lie Group__

## Introduction

The universal enveloping algebra of a real Lie algebra carries a canonical involution, the **principal anti-automorphism**, which reverses the order of a product and sends each generator $X$ to $-X$; with it the enveloping algebra becomes an involutive algebra, and the unitary representations of the group are exactly its representations that are compatible with the involution. The grade involution of a graded Lie algebra is a second, multiplicative involution, and the two together generate the full symmetry the enveloping algebra inherits from the Lie algebra. On the level of the group the principal anti-automorphism is the infinitesimal form of the inversion, and the unitary condition is the infinitesimal form of the unitarity of the representation.

This article treats the involution on the enveloping algebra of a Lie group, the star structure and the unitary representations. It is the fifth article of the `- * Theory` group of the category; the algebra structure and the Poincaré--Birkhoff--Witt theorem are from *Universal Enveloping Algebras*, the involutions on the group and on the algebra are *Involutive Groups* and *Graded Lie Algebras with an Involution*, the unitary representations are *Unitary Representations of a Lie Group*, and the form is *Hermitian Forms on a Lie Algebra* of the `- * Operator Theory` group.

The article assumes the universal enveloping algebra and its universality from *Universal Enveloping Algebras*, the involutive algebra with its star and its Hermitian and positive elements from *Involutive Rings*, the adjoint of an operator on a Hilbert space from *Bounded Operators on a Hilbert Space*, the Lie group and the inversion from *Lie Groups*, and the grading and the grade involution from *Graded Lie Algebras with an Involution*. The unitary representations are used by name and their decomposition belongs to *Unitary Representations of a Lie Group*; the particular unitary dual is not determined here.

## The Principal Anti-Automorphism

### The Definition

**Definition.** Let $\mathrm{G}$ be a real Lie algebra and $U(\mathrm{G})$ its universal enveloping algebra. The **principal anti-automorphism** is the unique $\mathbb{R}$-linear map $\sigma : U(\mathrm{G})\to U(\mathrm{G})$ with

$$
\sigma(1) = 1, \qquad \sigma(X) = -X \quad (X\in\mathrm{G}), \qquad \sigma(uv) = \sigma(v)\sigma(u) ,
$$

and the **star** of an element is written $u^{\star} = \sigma(u)$.

**Theorem.** The principal anti-automorphism exists and is unique; it is an involutive anti-automorphism of $U(\mathrm{G})$, $\sigma^2 = \mathrm{id}$, and it is the unique anti-automorphism of $U(\mathrm{G})$ that is $-\mathrm{id}$ on $\mathrm{G}$.

*Proof.* The map $X\mapsto -X$ is a homomorphism from the Lie algebra $\mathrm{G}$ to the opposite Lie algebra $U(\mathrm{G})^{\mathrm{op}}$: it is linear, and $[-X,-Y] = [X,Y]$ equals the opposite bracket. By the universal property of $U(\mathrm{G})$ applied to $U(\mathrm{G})^{\mathrm{op}}$ it extends to an algebra homomorphism from $U(\mathrm{G})$ to $U(\mathrm{G})^{\mathrm{op}}$, that is to an anti-automorphism of $U(\mathrm{G})$; it is involutive because its square is an endomorphism of $U(\mathrm{G})$ equal to the identity on $\mathrm{G}$ and hence on the whole algebra; uniqueness is the uniqueness in the universal property.

### The Properties

**Proposition.** The star is $\mathbb{R}$-linear, $(\lambda u)^{\star} = \lambda u^{\star}$ for $\lambda\in\mathbb{R}$, and on the PBW monomials

$$
(X_{i_1}\cdots X_{i_k})^{\star} = (-1)^k\,X_{i_k}\cdots X_{i_1} .
$$

The star is an anti-automorphism of the filtered algebra and preserves the filtration degree; the centre is stable under it, $Z(U(\mathrm{G}))^{\star} = Z(U(\mathrm{G}))$.

*Proof.* The formula follows by reversing the product and negating each factor; the filtration degree is the number of factors, unchanged; the stability of the centre is because an anti-automorphism preserves centrality.

### The Infinitesimal Inversion

**Theorem (the star is the derivative of the inversion).** Let $G$ be a Lie group with Lie algebra $\mathrm{G}$ and let $\iota : G\to G$ be the inversion. Then for every $X\in\mathrm{G}$ the differential of $\iota$ at $e$ is $-\mathrm{id}$, and on the distributions supported at the identity the transpose of $\iota$ is the principal anti-automorphism $\sigma$,

$$
\iota^{*}(u) = u^{\star} \qquad (u\in U(\mathrm{G})\cong\mathcal{D}_e(G)) .
$$

*Proof.* The inversion is a diffeomorphism with differential $-\mathrm{id}$ at the identity because its square is the identity; the transpose on distributions reverses the convolution product, because $\iota(xy) = \iota(y)\iota(x)$, and it sends the left-invariant vector field $X$ to $-X$; the two facts identify it with $\sigma$ under the isomorphism of *Operators on a Lie Group*.

## The Involutive Algebra

### The Star Structure

**Definition.** The pair $(U(\mathrm{G}),\sigma)$ is an **involutive algebra**: an associative algebra over $\mathbb{R}$ with an involutive anti-automorphism. An element is **Hermitian** when $u^{\star} = u$, and **skew** when $u^{\star} = -u$; the Hermitian elements form a real subspace, and a Hermitian element is **positive** when it is a sum of elements of the form $u^{\star}u$.

**Proposition.** Every element is the sum of a Hermitian and a skew part, $u = \tfrac12(u + u^{\star}) + \tfrac12(u - u^{\star})$; the generators $X\in\mathrm{G}$ are skew, the unit is Hermitian, and the real span of the products $u^{\star}u$ is a cone stable under the star.

*Proof.* The decomposition is the standard one for an involution, and the statements about the generators and the unit follow from $\sigma(X) = -X$ and $\sigma(1) = 1$; the cone statement is that $(u^{\star}u)^{\star} = u^{\star}u$.

### The Trace Form

**Definition.** The **trace form** of $U(\mathrm{G})$ is the symmetric bilinear form $\langle u,v\rangle = \tau(uv)$ where $\tau$ is the linear functional vanishing on the monomials of PBW degree different from the top and equal to the coefficient of the top monomial; it is invariant, $\langle uv,w\rangle = \langle u,vw\rangle$, and compatible with the star, $\langle u^{\star},v^{\star}\rangle = \langle u,v\rangle$.

**Proposition.** The trace form is non-degenerate on each finite-dimensional filtered piece, and its restriction to the Hermitian elements is definite on the semisimple case; the Casimir element is Hermitian and, for a compact form, positive.

*Proof.* The indicated functional is the standard trace like functional on the PBW basis, whose matrix is triangular with nonzero diagonal; the invariance is the associativity; the Hermitian statement for the Casimir follows from the reality of the structure constants of the compact form, and its positivity from the negative definiteness of the Killing form there.

## The Grade Involution

### The Extension of the Involution

**Definition.** Let $\mathrm{G} = \mathrm{G}^0\oplus\mathrm{G}^1$ be a graded Lie algebra, $\alpha$ the grade involution, $+1$ on the even part and $-1$ on the odd part. The **grade involution of the enveloping algebra** is the algebra automorphism $\alpha : U(\mathrm{G})\to U(\mathrm{G})$ extending the linear map that is $\pm\mathrm{id}$ on the homogeneous components.

**Proposition.** The grade involution is an algebra automorphism with $\alpha^2 = \mathrm{id}$, it commutes with the principal anti-automorphism, $\alpha\sigma = \sigma\alpha$, and in the parity grading of *Superalgebras and Graded Structures* it is the automorphism that changes the sign of the odd part. On a generator $X$ of parity $\lvert X\rvert$ the two involutions act by

$$
\sigma(X) = -X, \qquad \alpha(X) = (-1)^{\lvert X\rvert}X, \qquad (\alpha\sigma)(X) = -(-1)^{\lvert X\rvert}X .
$$

*Proof.* The grade involution is multiplicative because the bracket preserves parity, so it is an algebra automorphism by the universal property; its square is the identity on the generators and hence everywhere; it commutes with $\sigma$ because it is an automorphism on the generators and $\sigma$ is determined on the generators.

### The Two Involutions

**Theorem.** The group generated by $\sigma$ and $\alpha$ inside the algebra of linear maps of $U(\mathrm{G})$ is the Klein four-group, and its three non-trivial elements are $\sigma$, $\alpha$ and the composite $\alpha\sigma$, with

$$
\sigma^2 = \alpha^2 = (\alpha\sigma)^2 = \mathrm{id} .
$$

The composite $\alpha\sigma$ is the **graded transposition**, the anti-automorphism reversing the product and changing the sign of the odd part.

*Proof.* The relations are immediate; the composite is an anti-automorphism as a product of an automorphism and an anti-automorphism, its square is the identity, and the action on a monomial is the reversal with the sign $(-1)^{k}$ times the parity sign of each factor.

## The Star Structure and the Unitary Representations

### The Star-Representations

**Definition.** A **star-representation** of $(U(\mathrm{G}),\sigma)$ on a Hilbert space $\mathcal{H}$ is an algebra homomorphism $\pi$ such that

$$
\pi(u^{\star}) = \pi(u)^{*}
$$

where the adjoint on the right is the Hilbert-space adjoint. A **unitary representation** of $G$ is a strongly continuous homomorphism into the unitary group; its derived representation is a star-representation on the smooth vectors.

**Theorem.** Let $\pi$ be a unitary representation of $G$ and $\pi_*$ its derived representation on the smooth vectors. Then

$$
\pi_*(X)^{*} = -\pi_*(X) \qquad (X\in\mathrm{G}),
$$

so $\pi_*$ is a star-representation of $U(\mathrm{G})$: the generators are skew-adjoint and the star is the adjoint operation. Conversely a star-representation of $U(\mathrm{G})$ whose operators integrate to a group representation gives a unitary representation.

*Proof.* The skew-adjointness of $\pi_*(X)$ is the derivative of the unitarity at the identity; since the generators are skew and generate $U(\mathrm{G})$, the identity $\pi_*(u^{\star}) = \pi_*(u)^{*}$ holds on the whole algebra by multiplicativity and the adjoint of a product; the converse is the integration of the skew operators to a unitary group, which is Stone's theorem of *Unitary Representations of a Lie Group*.

### The Form and the Star

**Theorem.** Let $H$ be an invariant Hermitian form on $\mathrm{G}$ whose associated operator is the star, in the sense that $H([X,Y],Z) + H(Y,[X,Z]) = 0$ for all $X,Y,Z$. Then the adjoint of the operator of left multiplication $\pi_*(X)$ with respect to $H$ is $-\pi_*(X)$, and the star of $U(\mathrm{G})$ is the adjoint operation for the extended form on the enveloping algebra; the invariance of $H$ on $\mathrm{G}$ is equivalent to the star identity on $U(\mathrm{G})$.

*Proof.* The invariance of $H$ under the adjoint action says that $\operatorname{ad}_X$ is skew for $H$, so the adjoint of $\operatorname{ad}_X$ is $-\operatorname{ad}_X = \operatorname{ad}_{X^{\star}}$; the extension to the enveloping algebra is by multiplicativity of the adjoint and of the star. The equivalence is the statement that both properties are generated on the first order.

**Corollary (the Casimir is positive).** For a compact real form the Casimir element is a positive Hermitian element and the operator $\pi_*(\Omega)$ is a negative semidefinite self-adjoint operator on each unitary representation, with a negative eigenvalue on each irreducible summand.

*Proof.* The Casimir is a sum of products $X_iX^i$ which is a sum of the elements $X_i^{\star}X_i$ up to signs for a compact form, hence positive; its image is self-adjoint because the star is the adjoint, and its spectrum is negative on a compact group because it is minus the Laplacian, whose eigenvalues are non-negative; the value on an irreducible summand is the scalar of *The Casimir Operator of a Lie Group*.

## Examples

### The Universal Enveloping Algebra of $\mathrm{sl}_2(\mathbb{R})$

The algebra $\mathrm{sl}_2(\mathbb{R})$ has the basis $E,F,H$ with $[H,E] = 2E$, $[H,F] = -2F$, $[E,F] = H$; the star is $E^{\star} = -E$, $F^{\star} = -F$, $H^{\star} = -H$, and the Casimir $\Omega = EF + FE + \frac12H^2$ is Hermitian. Its image in a unitary representation is the negative of the standard Laplacian, and the eigenvalues are computed in *The Casimir Operator of a Lie Group*.

### The Heisenberg Algebra

For the Heisenberg algebra with $[P,Q] = Z$ central, the star sends each generator to its negative, and the symmetric elements include $PQ + QP$ and $Z$; a unitary representation sends $P$ and $Q$ to skew-adjoint operators and $Z$ to a central skew-adjoint scalar, so the imaginary parts are the self-adjoint position and momentum operators of the Schrödinger representation, named here only as the analytic model, with no physical interpretation.

### A Graded Case

For a Lie superalgebra with a non-trivial odd part the grade involution is not the identity, and the two involutions $\sigma$ and $\alpha$ act by the four sign patterns; the star representation of the enveloping algebra of a Lie superalgebra is the super-analogue of the unitary representation, and the compatible structures are the ones of *Graded Lie Algebras and Lie Superalgebras*.

## Summary

The universal enveloping algebra of a real Lie algebra carries the **principal anti-automorphism** $\sigma$, the unique anti-automorphism equal to $-\mathrm{id}$ on the generators; it is involutive, it reverses the order of a product, it preserves the filtration and the centre, and it is the infinitesimal form of the inversion of the group, acting on the distributions supported at the identity as the transpose of the inversion. Its square is the identity and its fixed elements are the Hermitian ones, the generators being skew; the trace form is invariant and compatible with it, and the Casimir element of a compact form is positive. A graded Lie algebra carries in addition the **grade involution** $\alpha$, an involutive automorphism changing the sign of the odd part; $\sigma$ and $\alpha$ commute and generate the Klein four-group, whose third element is the graded transposition. A star-representation of $U(\mathrm{G})$ on a Hilbert space is one with $\pi(u^{\star}) = \pi(u)^{*}$, and the derived representation of a unitary representation is a star-representation with skew-adjoint generators, the star playing the role of the Hilbert-space adjoint; the invariance of a Hermitian form on the Lie algebra is equivalent to the star identity on the enveloping algebra, so the unitary representations are the star-representations and the adjoint operation is the star.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$, $u^{\star} = \sigma(u)$ | the principal anti-automorphism and the star |
| $\sigma(X) = -X$ | the action on the generators |
| $\sigma(uv) = \sigma(v)\sigma(u)$, $\sigma^2 = \mathrm{id}$ | anti-multiplicativity and involution |
| $\alpha$ | the grade involution, $\alpha(X) = (-1)^{\lvert X\rvert}X$ |
| $\alpha\sigma$ | the graded transposition |
| Hermitian, skew, positive | the elements with $u^{\star} = u$, $u^{\star} = -u$, and sums $u^{\star}u$ |
| $\langle u,v\rangle = \tau(uv)$ | the trace form |
| $\pi(u^{\star}) = \pi(u)^{*}$ | the star-representation, the unitary condition |
| $\pi_*(X)^{*} = -\pi_*(X)$ | skew-adjointness of the generators |
| $\Omega$ | the Casimir, Hermitian and positive for a compact form |

## Further Reading

- Jacques Dixmier, *Enveloping Algebras* (North-Holland, 1977), for the principal anti-automorphism, the filtration and the centre of the enveloping algebra.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, second edition, 2015), for the star-representations and the unitary representations of a Lie group.
- Anthony W. Knapp, *Representation Theory of Semisimple Groups* (Princeton University Press, 1986), for the infinitesimal unitarity condition and the Casimir element.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the general theory of involutions on an algebra and their Hermitian elements.
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984), for the enveloping algebra of a real form and the inversion of the group.
