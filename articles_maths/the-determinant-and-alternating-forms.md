
# __The Determinant and Alternating Forms__

## Introduction

The exterior powers of the companion article *Exterior Powers* carry, in their top degree, a one-dimensional module attached to a free module of finite rank, and an endomorphism acts on it by a scalar. That scalar is the **determinant**. The determinant is therefore not an ad hoc formula in the entries of a matrix but the unique scalar invariant of a linear transformation, obtained by transport along the top exterior power. The same construction in every intermediate degree produces the **minors**, and the multiplicativity of the determinant is a special case of the functoriality of $\Lambda^n$, while the formula relating the minors of a composite to those of its factors, known as the **Cauchy–Binet formula**, is the degreewise statement that $\Lambda^n(g \circ f) = \Lambda^n g \circ \Lambda^n f$.

The linear functionals on the exterior powers are the **alternating forms**, and the exterior algebra of the dual module is the algebraic prototype of the algebra of differential forms. A differential $k$-form on a smooth manifold is a smoothly varying alternating form on the tangent space, and the operations of the calculus — the wedge product, the pullback, and the exterior derivative — are visible already at the level of a single free module over a commutative ring, with no smooth structure required.

Throughout, $R$ denotes a commutative ring with identity $1 \neq 0$ and $M$, $N$, $P$ are $R$-modules; over a commutative ring left and right modules coincide, so no side is specified. The field is written $K$, and $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$ when only those two are meant. The determinant is defined over an arbitrary commutative ring, and the place where a field, a characteristic assumption, or the invertibility of $2$ is needed is flagged; in particular the sign-based expansions below require no division, while the Pfaffian and the identification of alternating with skew-symmetric forms require care in characteristic $2$. No physics is invoked.

The companion articlesandcontinue from here; the latter is with this one.

## Induced Maps and Minors

### The Induced Map on Exterior Powers

Let $f : M \to N$ be an $R$-linear map and let $\Lambda^n f : \Lambda^n M \to \Lambda^n N$ be the induced map of *Exterior Powers*, characterised on elementary wedges by

$$
\Lambda^n f(x_1 \wedge \cdots \wedge x_n) = f(x_1) \wedge \cdots \wedge f(x_n).
$$

Functoriality gives $\Lambda^n(\mathrm{id}_M) = \mathrm{id}_{\Lambda^n M}$ and $\Lambda^n(g \circ f) = \Lambda^n g \circ \Lambda^n f$, and these two identities are the source of the multiplicativity properties recorded below. In degree $1$ the induced map is $f$ itself, and in degree $0$ it is the identity of $R$.

### Minors and the Matrix of $\Lambda^n f$

Suppose now that $M$ and $N$ are free with bases $e_1, \ldots, e_m$ and $f_1, \ldots, f_r$, and let $A = (a_{ij})$ be the matrix of $f$ in these bases, so that $f(e_j) = \sum_i a_{ij} f_i$. The induced bases of $\Lambda^n M$ and $\Lambda^n N$ consist of the increasing wedges, and the matrix of $\Lambda^n f$ in them is described by the minors of $A$.

**Definition.** Let $I \subseteq \{1, \ldots, r\}$ and $J \subseteq \{1, \ldots, m\}$ have the same cardinality $n$, say $I = (i_1 < \cdots < i_n)$ and $J = (j_1 < \cdots < j_n)$. The **minor** of $A$ with row set $I$ and column set $J$ is

$$
A_{I,J} = \det\bigl(a_{i_p, j_q}\bigr)_{p,q=1}^{n},
$$

the determinant of the $n \times n$ submatrix formed by those rows and columns. A minor is therefore an alternating function of the rows and of the columns separately.

**Proposition.** In the induced bases, the matrix entry of $\Lambda^n f$ from the basis wedge $e_J = e_{j_1} \wedge \cdots \wedge e_{j_n}$ to the basis wedge $f_I = f_{i_1} \wedge \cdots \wedge f_{i_n}$ is the minor $A_{I,J}$:

$$
\Lambda^n f(e_J) = \sum_{|I| = n} A_{I,J}\, f_I.
$$

**Proof.** Expand each $f(e_{j_q}) = \sum_i a_{i,j_q} f_i$ and use multilinearity of the wedge: the coefficient of $f_{i_1} \wedge \cdots \wedge f_{i_n}$ is the alternating sum $\sum_{\sigma \in S_n} \operatorname{sgn}(\sigma) \prod_q a_{i_q, j_{\sigma(q)}}$, which is the Leibniz expansion of the minor. $\square$

## The Determinant

### Definition for Endomorphisms

Let $M$ be free of rank $m$ with basis $(e_1, \ldots, e_m)$. The top exterior power $\Lambda^m M$ is free of rank $1$, with the single basis element $e_1 \wedge \cdots \wedge e_m$, so every endomorphism of it is multiplication by an element of $R$. For $f \in \operatorname{End}_R(M)$, the induced map $\Lambda^m f$ is such an endomorphism, and one names its scalar.

**Definition.** Let $M$ be a free $R$-module of rank $m$ and let $f : M \to M$ be $R$-linear. The **determinant** of $f$ is the unique scalar $\det(f) \in R$ with

$$
\Lambda^m f(e_1 \wedge \cdots \wedge e_m) = \det(f)\, e_1 \wedge \cdots \wedge e_m
$$

for a basis $(e_1, \ldots, e_m)$. By the proposition above it is independent of the choice of basis, and it is the alternating $m$-multilinear form

$$
\det(f) = \sum_{\sigma \in S_m} \operatorname{sgn}(\sigma) \prod_{q=1}^{m} a_{q, \sigma(q)},
$$

where $(a_{ij})$ is the matrix of $f$ in the basis.

### The Determinant of a Matrix

Writing $\det(A)$ for the right-hand side, the determinant of a square matrix is

$$
\det(A) = \sum_{\sigma \in S_m} \operatorname{sgn}(\sigma)\, a_{1,\sigma(1)} a_{2,\sigma(2)} \cdots a_{m,\sigma(m)}.
$$

This is the **Leibniz formula**. It is a polynomial with integer coefficients in the entries, hence defined over every commutative ring, and it is alternating in the columns and in the rows.

**Proposition (basic expansions).** For an $m \times m$ matrix $A$ over a commutative ring:

**(a)** $\det(A)$ is $R$-multilinear and alternating in the columns of $A$;

**(b)** $\det(I) = 1$ and $\det(A) = 0$ if two columns of $A$ are equal;

**(c)** $\det(A^{\mathsf{T}}) = \det(A)$.

**Proof.** (a) Each term of the Leibniz formula contains exactly one entry from each column, so the formula is linear in each column; exchanging two columns permutes the summation index $\sigma$ by a transposition and multiplies each term by $-1$. (b) is immediate from the formula. (c) The transpose relabels $\sigma$ by $\sigma^{-1}$, and $\operatorname{sgn}(\sigma^{-1}) = \operatorname{sgn}(\sigma)$. $\square$

### Multiplicativity and Invertibility

**Theorem.** Let $M$ be free of rank $m$ and let $f, g \in \operatorname{End}_R(M)$. Then

$$
\det(g \circ f) = \det(g)\, \det(f).
$$

Moreover $f$ is invertible if and only if $\det(f)$ is a unit of $R$, and then $\det(f^{-1}) = \det(f)^{-1}$.

**Proof.** Functoriality of the top exterior power gives $\Lambda^m(g \circ f) = \Lambda^m g \circ \Lambda^m f$, and on the rank-one module $\Lambda^m M$ these are multiplications by $\det(g \circ f)$, $\det(g)$, and $\det(f)$ respectively, so the scalars multiply. If $f$ is invertible, applying the first part to $g = f^{-1}$ and $g \circ f = \mathrm{id}$ gives $\det(f)\det(f^{-1}) = \det(\mathrm{id}) = 1$. Conversely, if $\det(f)$ is a unit, then the adjugate identity $f \circ \operatorname{adj}(f) = \det(f)\,\mathrm{id}_M$ exhibits an inverse: $\operatorname{adj}(f)$ is the endomorphism whose matrix entries are the $(m-1)$-minors of the matrix of $f$, with alternating signs, and it is defined over any commutative ring. $\square$

**Remark.** Over a general commutative ring one cannot conclude that a non-invertible endomorphism has $\det(f) = 0$: only that $\det(f)$ is a non-unit. For example, over $R = \mathbb{Z}$ the map of $\mathbb{Z}$ given by multiplication by $2$ has determinant $2$, which is neither a unit nor zero. This is the point at which the determinant over a ring differs from the determinant over a field.

### The Characteristic Polynomial

**Proposition.** Let $M$ be free of rank $m$ and let $f \in \operatorname{End}_R(M)$. Then

$$
\det(\mathrm{id}_M + t f) = \sum_{k=0}^{m} \operatorname{tr}(\Lambda^k f)\, t^k,
$$

where $\operatorname{tr}(\Lambda^k f)$ denotes the trace of the induced endomorphism of $\Lambda^k M$ and $\operatorname{tr}(\Lambda^0 f) = 1$.

**Proof.** Both sides are polynomials with integer coefficients in the matrix entries of $f$. It therefore suffices to prove the identity after base change to a field over which the matrix has a full set of eigenvalues, for instance over the algebraic closure of the fraction field of the polynomial ring in the entries. There $f$ is triangularisable, with eigenvalues $\lambda_1, \ldots, \lambda_m$; the eigenvalues of $\Lambda^k f$ are the products $\lambda_{i_1} \cdots \lambda_{i_k}$ over increasing $k$-tuples, so $\operatorname{tr}(\Lambda^k f)$ is the elementary symmetric function $e_k(\lambda)$ of the eigenvalues and $\det(\mathrm{id} + tf) = \prod_{i=1}^{m}(1 + t\lambda_i) = \sum_{k=0}^{m} e_k(\lambda) t^k$. $\square$

Setting $t = -1/s$ and clearing denominators recovers the characteristic polynomial $\det(s\,\mathrm{id} - f) = s^m \sum_k \operatorname{tr}(\Lambda^k f)(-1/s)^k$; the coefficients are the traces of the induced maps on the exterior powers.

## Alternating Forms

### Forms and the Exterior Algebra of the Dual

**Definition.** An **alternating form of degree $n$** on $M$ with values in $R$ is an alternating $n$-multilinear map $M^n \to R$. The $R$-module of such forms is

$$
\operatorname{Alt}^n(M; R) \cong (\Lambda^n M)^*,
$$

the last identification being the universal property of the exterior power. Assembling the degrees,

$$
\operatorname{Alt}^\bullet(M; R) = \bigoplus_{n \geq 0} \operatorname{Alt}^n(M; R)
$$

is the **algebra of alternating forms** on $M$.

**Proposition.** Let $M$ be free of finite rank. Then for each $n$ there is a natural isomorphism $\operatorname{Alt}^n(M; R) \cong \Lambda^n(M^*)$, and these assemble into an isomorphism of graded algebras

$$
\operatorname{Alt}^\bullet(M; R) \cong \Lambda(M^*)
$$

between the algebra of alternating forms under the wedge product and the exterior algebra of the dual module.

**Proof.** A form of degree $n$ corresponds to a linear functional on $\Lambda^n M$, hence to an element of $(\Lambda^n M)^*$; over a free module of finite rank the natural map $\Lambda^n(M^*) \to (\Lambda^n M)^*$ sending $\varphi_1 \wedge \cdots \wedge \varphi_n$ to the form $(x_1, \ldots, x_n) \mapsto \det(\varphi_p(x_q))$ is an isomorphism, by the basis theorem of *Exterior Powers* applied to the dual basis. Multiplicativity of the correspondence is the definition of the wedge product of forms. $\square$

**Definition.** The **wedge product of forms** $\alpha \wedge \beta \in \operatorname{Alt}^{p+q}(M; R)$ of forms $\alpha$ of degree $p$ and $\beta$ of degree $q$ is the form

$$
(\alpha \wedge \beta)(x_1, \ldots, x_{p+q}) = \sum_{\sigma} \operatorname{sgn}(\sigma)\, \alpha(x_{\sigma(1)}, \ldots, x_{\sigma(p)})\, \beta(x_{\sigma(p+1)}, \ldots, x_{\sigma(p+q)}),
$$

the sum over the $(p, q)$-shuffles of $\{1, \ldots, p+q\}$. It is graded-commutative, $\alpha \wedge \beta = (-1)^{pq}\beta \wedge \alpha$, and associative.

### Pullback

**Definition.** Let $f : M \to N$ be $R$-linear. The **pullback** along $f$ is the algebra homomorphism

$$
f^* : \operatorname{Alt}^\bullet(N; R) \to \operatorname{Alt}^\bullet(M; R), \qquad (f^*\omega)(x_1, \ldots, x_n) = \omega(f(x_1), \ldots, f(x_n)).
$$

**Proposition.** The pullback is contravariantly functorial: $\mathrm{id}^* = \mathrm{id}$ and $(g \circ f)^* = f^* \circ g^*$.

**Proof.** Both are immediate from the definition; the reversal of order is the usual contravariance of a hom functor. $\square$

### The Prototype of Differential Forms

The algebraic data above are the pointwise model of the differential calculus. On a smooth manifold $M$ one forms the cotangent bundle $T^*M$ , for each $k$, the bundle $\Lambda^k T^*M$; a **differential $k$-form** is a smooth section of that bundle, and the space of sections $\Omega^k(M) = \Gamma(\Lambda^k T^*M)$ is the module of $k$-forms. The wedge product of forms and the pullback of forms along a smooth map are obtained by applying the constructions of this section fibrewise. The exterior derivative, a degree-one derivation $d: \Omega^k(M) \to \Omega^{k+1}(M)$ with $d^2 = 0$, is the further structure that the smooth setting supplies; it is the subject of with this one. The determinant reappears there as the change-of-variables factor in the integration of a top-degree form.

## The Cauchy–Binet Formula

The multiplicativity of the determinant in the square case is the $n = m$ case of a formula valid in every degree.

**Theorem (Cauchy–Binet).** Let $A$ be an $r \times m$ matrix and $B$ an $m \times s$ matrix over a commutative ring $R$. For increasing index sets $I \subseteq \{1, \ldots, r\}$ and $J \subseteq \{1, \ldots, s\}$ of size $n$,

$$
\det\bigl((AB)_{I,J}\bigr) = \sum_{K} \det(A_{I,K})\, \det(B_{K,J}),
$$

the sum over the increasing $n$-element subsets $K \subseteq \{1, \ldots, m\}$.

**Proof.** Let $f : R^s \to R^m$ and $g : R^m \to R^r$ be the linear maps with matrices $B$ and $A$, so that $AB$ is the matrix of $g \circ f$. By the minor proposition, the matrix entries of $\Lambda^n(g \circ f)$ are the minors of $AB$, and by functoriality $\Lambda^n(g \circ f) = \Lambda^n g \circ \Lambda^n f$, whose matrix entries are sums of products of the minors of $A$ and of $B$ indexed by the intermediate basis wedges. Equating the two expressions gives the formula. $\square$

**Corollary.** If $m = r = s = n$, Cauchy–Binet reduces to $\det(AB) = \det(A)\det(B)$.

**Corollary (Jacobi's complementary minor identity).** Let $A$ be an invertible $m \times m$ matrix over a commutative ring, with inverse $A^{-1}$. For increasing index sets $I, J \subseteq \{1, \ldots, m\}$ of size $n$, written $I^c$ and $J^c$ for their complements,

$$
\det\bigl((A^{-1})_{I,J}\bigr) = (-1)^{\textstyle\sum I + \sum J}\, \det(A_{J^c, I^c}) \cdot \det(A)^{-1},
$$

where $\sum I$ denotes the sum of the entries of $I$. Thus the $n \times n$ minors of the inverse are the complementary $(m-n) \times (m-n)$ minors of $A$, up to a sign and the scalar $\det(A)^{-1}$.

This is the classical complementary-minor theorem of Jacobi; it is the statement that the compound matrix of $A^{-1}$ is the inverse of the compound matrix of $A$, combined with the description of the inverse of a compound matrix through complementary minors. When $n = m$ it reduces to $\det(A^{-1}) = \det(A)^{-1}$.

## The Top Power, Volume and the Pfaffian

**Definition.** Let $V$ be a free $K$-module of finite rank $m$. A **volume form** on $V$ is a nonzero element of the one-dimensional space $\Lambda^m V$; a choice of volume form is a choice of basis of the determinant line $\Lambda^m V$, of which it records the direction but not the scale, and the determinant of an automorphism is the factor by which it scales the volume form.

**Proposition (the determinant as the volume form).** Let $\omega$ be a nonzero alternating $m$-form on $V$ and let $(e_1, \ldots, e_m)$ be a basis with $\omega(e_1, \ldots, e_m) = 1$. Then for every endomorphism $f$ of $V$,

$$
\omega(f(e_1), \ldots, f(e_m)) = \det(f).
$$

**Proof.** The form $\omega$ is a basis of the one-dimensional space of alternating $m$-forms; the pullback $f^*\omega = \det(f)\omega$ by definition of the determinant, and evaluating at the basis gives the claim. $\square$

**Example (alternating forms of degree $2$).** An alternating $2$-form on a free module with basis $(e_1, \ldots, e_m)$ is determined by its values $\omega_{ij} = \omega(e_i, e_j)$ on pairs, and these satisfy $\omega_{ij} = -\omega_{ji}$ and $\omega_{ii} = 0$. In matrix form $\Omega = (\omega_{ij})$ is **alternating**, $\Omega^{\mathsf{T}} = -\Omega$, and the form is

$$
\omega(x, y) = x^{\mathsf{T}} \Omega\, y.
$$

Such a form is the matrix object studied. When $m = 2n$ is even and $\Omega$ is alternating and invertible, its determinant is a square, $\det(\Omega) = \operatorname{Pf}(\Omega)^2$, where the **Pfaffian** $\operatorname{Pf}(\Omega)$ is the polynomial

$$
\operatorname{Pf}(\Omega) = \frac{1}{2^n n!} \sum_{\sigma \in S_{2n}} \operatorname{sgn}(\sigma) \prod_{i=1}^{n} \Omega_{\sigma(2i-1), \sigma(2i)}.
$$

The Pfaffian and its relation to the symplectic form are treated. Over a ring in which $2^n n!$ is invertible, for instance a $\mathbb{Q}$-algebra or a field of characteristic zero, the displayed formula is directly available; the summand is in fact divisible by $2^n n!$ in $\mathbb{Z}[\Omega_{ij}]$, so the Pfaffian is an integral polynomial and is defined over every commutative ring. The identity $\det(\Omega) = \operatorname{Pf}(\Omega)^2$ holds over every commutative ring because both sides are integral polynomials and the identity holds over $\mathbb{Q}$.

## Summary

The determinant of an endomorphism of a free module of rank $m$ is the scalar by which it acts on the top exterior power $\Lambda^m M$; in a basis it is the Leibniz sum $\sum_\sigma \operatorname{sgn}(\sigma)\prod_q a_{q,\sigma(q)}$. It is multiplicative, $\det(g \circ f) = \det(g)\det(f)$, it satisfies $\det(f^{\mathsf{T}}) = \det(f)$, and an endomorphism is invertible exactly when its determinant is a unit of the base ring. The characteristic polynomial is governed by the traces of the induced maps on the exterior powers, $\det(\mathrm{id} + tf) = \sum_k \operatorname{tr}(\Lambda^k f)t^k$.

In every degree the induced map $\Lambda^n f$ has matrix the $n \times n$ minors of the matrix of $f$, and the identity $\Lambda^n(g \circ f) = \Lambda^n g \circ \Lambda^n f$ reads, in entries, as the Cauchy–Binet formula

$$
\det\bigl((AB)_{I,J}\bigr) = \sum_K \det(A_{I,K})\det(B_{K,J}).
$$

The alternating forms of degree $n$ are the linear functionals on $\Lambda^n M$, equivalently, for free $M$ of finite rank, the elements of $\Lambda^n(M^*)$; they form the graded-commutative algebra $\Lambda(M^*)$, with wedge product and contravariant pullback. This algebra, with the extra structure of a smooth manifold supplying the exterior derivative, is the algebra of differential forms, and the determinant is the factor by which a linear map scales a volume form. For an alternating matrix of even size the determinant is the square of the Pfaffian.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity $1 \neq 0$; the default base |
| $K$ | Field |
| $M$, $N$, $P$ | $R$-modules, free of finite rank where a determinant is taken |
| $\Lambda^n M$ | $n$-th exterior power |
| $\Lambda^n f$ | Induced map on exterior powers |
| $e_1, \ldots, e_m$; $f_1, \ldots, f_r$ | Bases of $M$ and of $N$ in which matrices and minors are written |
| $A_{I,J}$ | Minor of a matrix on row set $I$ and column set $J$ |
| $\det(f)$, $\det(A)$ | Determinant: scalar action on $\Lambda^m M$, Leibniz sum in a basis |
| $\operatorname{End}_R(M)$ | $R$-linear endomorphisms of $M$; the home of $\det$, $\operatorname{tr}$ and $\operatorname{adj}$ |
| $\operatorname{tr}$ | Trace; $\operatorname{tr}(\Lambda^k f)$ is the trace on $\Lambda^k M$ |
| $\operatorname{adj}(f)$ | Adjugate; $f \circ \operatorname{adj}(f) = \det(f)\,\mathrm{id}_M$ |
| $\det(\mathrm{id} + tf) = \sum_k \operatorname{tr}(\Lambda^k f)t^k$ | Characteristic-polynomial identity |
| $\operatorname{Alt}^n(M; R) \cong (\Lambda^n M)^*$ | Alternating $n$-forms on $M$ |
| $\operatorname{Alt}^\bullet(M; R) \cong \Lambda(M^*)$ | Algebra of alternating forms, for free $M$ of finite rank |
| $\alpha \wedge \beta$ | Wedge product of forms; graded-commutative |
| $f^*$ | Pullback of forms, contravariant: $(g \circ f)^* = f^* \circ g^*$ |
| $\Omega = (\omega_{ij})$ | Matrix of an alternating $2$-form, $\Omega^{\mathsf{T}} = -\Omega$ |
| $\operatorname{Pf}(\Omega)$ | Pfaffian of an alternating matrix of even size; $\det(\Omega) = \operatorname{Pf}(\Omega)^2$ |
| $\Omega^k(M) = \Gamma(\Lambda^k T^*M)$ | Module of differential $k$-forms on a smooth manifold |



## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the determinant as the action on the top exterior power and the Cauchy–Binet formula.
- Werner Greub, *Multilinear Algebra* (Springer, 2nd ed. 1978), for minors, alternating forms, and the determinant defined by multilinear algebra.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for the determinant over a commutative ring and the adjugate identity.
- Gilbert Strang, *Linear Algebra and Its Applications* (Cengage, 4th ed. 2005), for the Leibniz formula, the classical expansions, and the volume interpretation.
- Israel M. Gelfand and Mikhail M. Kapranov and Andrei V. Zelevinsky, *Discriminants, Resultants, and Multidimensional Determinants* (Birkhäuser, 1994), for determinants, minors, and their geometric role.
- Frank W. Warner, *Foundations of Differentiable Manifolds and Lie Groups* (Springer, 1983), for alternating forms on the tangent space and the prototype of differential forms.
- D. G. Northcott, *Multilinear Algebra* (Cambridge University Press, 1984), for the exterior algebra of the dual and the algebra of alternating forms.
