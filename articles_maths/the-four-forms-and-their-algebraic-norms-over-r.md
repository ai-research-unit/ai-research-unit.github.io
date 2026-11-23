# __The Four Forms and Their Algebraic Norms over $\mathbb{R}$__

## Introduction

**Four canonical objects live on $M_n(\mathbb{R})$ — the trace form, the Hilbert–Schmidt form, the Killing form and the determinant — and only the last is multiplicative, while only the first two are quadratic forms.**

The article puts the four in one table with their invariances and their inertias, explains the algebraic norm of a central simple algebra and why $\det$ is that norm here, shows that the norm form is quadratic only at $n=2$, computes the derivative of $\log\det$ at the identity, and compares the four norms at $n=3$. It assumes *The Trace Form and Its Indefinite Inertia*, *The Hilbert–Schmidt Form: Definite but Not Invariant* and *The Killing Form, Its Radical and the Centre of $\mathfrak{gl}_n(\mathbb{R})$*, and it defers the two-dimensional case to *Split-Quaternion Algebra*.

## The Four Objects

**The first form is the trace form.** It is

$$
\langle X,Y\rangle=\operatorname{tr}(XY),
$$

symmetric, nondegenerate, of inertia $\bigl(n(n+1)/2,n(n-1)/2\bigr)$, positive on $\operatorname{Sym}_n$ and negative on $\operatorname{Skew}_n$.

**The second form is the Hilbert–Schmidt form.** It is

$$
\langle X,Y\rangle_{\mathrm{HS}}=\operatorname{tr}(X^{\mathsf T}Y),
$$

an inner product, of inertia $(n^{2},0)$.

**The third form is the Killing form.** It is

$$
\operatorname{K}(X,Y)=\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y)=2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y),
$$

symmetric, invariant, with radical $\mathbb{R}\mathrm{I}$ and inertia $\bigl(n(n+1)/2-1,n(n-1)/2\bigr)$ on the quotient.

**The fourth object is the determinant.** It is a homogeneous polynomial of degree $n$ in the entries, written $\det X$. It is not a bilinear form for $n\ge3$. At $n=2$ it is a quadratic form, and it is the norm form of the split-quaternion algebra.

## The Table

**The invariances separate the four immediately.** The table records, for each object, what it is invariant under, and what its inertia is.

| Object | Invariance | Inertia |
|---|---|---|
| $\operatorname{tr}(XY)$ | conjugation by $\mathrm{GL}_n(\mathbb{R})$; all inner derivations | $\bigl(n(n+1)/2,\,n(n-1)/2\bigr)$ |
| $\operatorname{tr}(X^{\mathsf T}Y)$ | $X\mapsto QXR^{\mathsf T}$ with $Q,R\in\mathrm{O}(n)$ | $(n^{2},0)$ |
| $\operatorname{K}(X,Y)$ | all automorphisms; conjugation by $\mathrm{GL}_n(\mathbb{R})$ | $\bigl(n(n+1)/2-1,\,n(n-1)/2\bigr)$ plus a radical of dimension $1$ |
| $\det X$ | conjugation by $\mathrm{GL}_n(\mathbb{R})$; multiplicative | degree $n$; $(2,2)$ only at $n=2$ |

## The Reduced Trace and the Reduced Norm

**For a central simple algebra of degree $n$, the reduced trace is the trace and the reduced norm is the determinant.** Let $A$ be a central simple algebra of dimension $n^{2}$ over a field $F$, and let $F'$ be a splitting field, so that $A\otimes_FF'\cong M_n(F')$. For $a\in A$ the element $a\otimes1$ is a matrix over $F'$, and

$$
\operatorname{Tred}(a)=\operatorname{tr}(a\otimes1),\qquad \operatorname{Nred}(a)=\det(a\otimes1).
$$

The trace and the determinant of that matrix lie in $F$ and do not depend on the splitting field. So both functions are defined on $A$ itself.

**For $M_n(\mathbb{R})$ the two functions are the trace and the determinant.** The algebra is already split, so $F'=F=\mathbb{R}$ and the matrix is the element itself. Hence

$$
\operatorname{Tred}=\operatorname{tr},\qquad \operatorname{Nred}=\det.
$$

**The reduced norm is multiplicative and the reduced trace is additive.** For all $X,Y$,

$$
\det(XY)=\det X\det Y,\qquad \operatorname{tr}(X+Y)=\operatorname{tr}X+\operatorname{tr}Y.
$$

The first identity is the reason the determinant is called the norm of the algebra: it is a multiplicative function of degree $n$, and it vanishes exactly on the non-invertibles.

**The norm form of the algebra is the determinant.** In the language of quadratic forms, the norm form of a central simple algebra of degree $n$ is the reduced norm, a homogeneous polynomial of degree $n$. For $n=2$ it is a quadratic form; for $n\ge3$ it is a form of higher degree. The degree is the invariant that decides everything below.

## The Norm Form Is Quadratic Only at $n=2$

**At $n=2$ the determinant is a quadratic form of inertia $(2,2)$.** In the matrix-unit basis of $M_2(\mathbb{R})$,

$$
\det\begin{pmatrix}a&b\\ c&d\end{pmatrix}=ad-bc.
$$

The polar form is $B(X,Y)=\tfrac14\bigl(\det(X+Y)-\det(X-Y)\bigr)$. Its matrix in the basis $E_{11},E_{12},E_{21},E_{22}$ has eigenvalues $\tfrac12,\tfrac12,-\tfrac12,-\tfrac12$, computed with numpy, so the inertia is $(2,2)$. The form is split: a two-dimensional positive part and a two-dimensional negative part.

**That form is the norm of the split-quaternion algebra.** The algebra $M_2(\mathbb{R})$ is the split quaternions, and $\det$ is the norm. The norm form of a quaternion algebra is a quadratic form of dimension four; for the split algebra it is the form of inertia $(2,2)$, and for the division algebra $\mathbb{H}$ it is the positive definite form of inertia $(4,0)$. So the two real quaternion algebras are distinguished by the inertia of the same norm form.

**At $n\ge3$ the determinant is not a quadratic form.** Its degree is $n$, and a quadratic form has degree two. A homogeneous polynomial of degree $n$ is a quadratic form only when $n=2$.

**The determinant is not a power of a quadratic form either.** Suppose $\det=q^{n/2}$ with $q$ a quadratic form.

**The two cases.** For odd $n\ge3$ the exponent $n/2$ is not an integer, and a power of a quadratic form has even degree. For even $n\ge4$ the exponent is at least two, so $\det$ would be a product of two polynomials of positive degree, and the determinant is irreducible as a polynomial in the entries. Neither case allows such a $q$, and only at $n=2$, where the exponent is one, is $\det$ itself quadratic.

## The Derivative of the Logarithm at the Identity

**The derivative of $\log\det$ at the identity is the trace.** For $H\in M_n(\mathbb{R})$,

$$
\det(\mathrm{I}+tH)=1+t\operatorname{tr}(H)+O(t^{2}),
$$

so

$$
\frac{d}{dt}\Big|_{t=0}\log\det(\mathrm{I}+tH)=\operatorname{tr}(H).
$$

The linear functional that appears is the trace, and it is the only one.

**The identity is the reason $\det(\exp H)=\exp(\operatorname{tr}H)$.** The exponential of a matrix has determinant the exponential of its trace, and the display above is the infinitesimal form of that identity. The function $\log\det$ is a primitive of the trace along every line through the identity.

## The Four Norms

**Four norms are attached to a matrix.** They are

$$
\|X\|_{\mathrm{op}}=\sigma_{\max}(X),\qquad \|X\|_{\mathrm{F}}=\Bigl(\sum_{i,j}X_{ij}^{2}\Bigr)^{1/2},\qquad \|X\|_{\mathrm{tr}}=\bigl|\operatorname{tr}(X^{2})\bigr|^{1/2},\qquad \rho(X)=\max_i|\lambda_i(X)|.
$$

The first is the operator norm, the largest singular value. The second is the Frobenius norm, the norm of the Hilbert–Schmidt form. The third is the norm of the trace form, taken with the absolute value because the form is indefinite. The fourth is the spectral radius, the largest modulus of an eigenvalue.

**Only two of the four are norms on the whole algebra.** The operator norm and the Frobenius norm are norms on $M_n(\mathbb{R})$. The trace-form quantity is a norm on $\operatorname{Sym}_n$, where it equals the Frobenius norm, and it is not a norm on the algebra, because it vanishes on the nonzero null vectors of the trace form: at $n=2$ the matrix $E_{11}-E_{22}+E_{12}-E_{21}$ has $\operatorname{tr}(X^{2})=0$. The spectral radius is a norm on $\operatorname{Sym}_n$ and fails to be one in general, because a nonzero nilpotent has spectral radius zero.

**On the symmetric part all four coincide in pairs.** For symmetric $X$,

$$
\|X\|_{\mathrm{tr}}^{2}=\operatorname{tr}(X^{2})=\|X\|_{\mathrm{F}}^{2},\qquad \rho(X)=\|X\|_{\mathrm{op}}.
$$

The first identity was checked at $n=3$ on a symmetric matrix $Y$: both sides equal $26$. The second is the spectral theorem for symmetric matrices.

**On the antisymmetric part the trace-form quantity is the Frobenius norm.** For antisymmetric $K$, $\operatorname{tr}(K^{2})=-\|K\|_{\mathrm{F}}^{2}$, so the absolute value restores the equality. At $n=3$ an antisymmetric matrix $K$ gave $\operatorname{tr}(K^{2})=-28$ and $\|K\|_{\mathrm{F}}^{2}=28$.

## The Inequalities at $n=3$

**The norms are ordered by one chain and two separate bounds.** For every $X$,

$$
\rho(X)\le\|X\|_{\mathrm{op}}\le\|X\|_{\mathrm{F}}\le\sqrt{n}\,\|X\|_{\mathrm{op}},\qquad \bigl|\operatorname{tr}(X^{2})\bigr|^{1/2}\le\|X\|_{\mathrm{F}},\qquad |\operatorname{tr}X|\le\sqrt{n}\,\|X\|_{\mathrm{F}}.
$$

The first chain compares the spectral radius with the operator norm, the operator norm with the Frobenius norm, and the Frobenius norm with its dimension bound. The fourth inequality is the Cauchy–Schwarz inequality for the Hilbert–Schmidt form applied to $X^{\mathsf T}$ and $X$. The fifth applies the same inequality to $\mathrm{I}$ and $X$, since $\|\mathrm{I}\|_{\mathrm{F}}=\sqrt{n}$.

**The numbers at $n=3$ confirm each inequality with room to spare.** Take

$$
X=\begin{pmatrix}1&2&0\\ 0&1&3\\ 4&0&1\end{pmatrix}.
$$

The singular values are $4.4133$, $2.9882$ and $1.8957$, so $\|X\|_{\mathrm{op}}=4.413270$ and $\|X\|_{\mathrm{F}}=5.656854$. The eigenvalues have modulus at most $3.884499$, so $\rho(X)=3.884499$. Then

| Quantity | Value | Bound |
|---|---|---|
| $\rho(X)$ | $3.884499$ | $\le\|X\|_{\mathrm{op}}=4.413270$ |
| $\|X\|_{\mathrm{F}}$ | $5.656854$ | $\le\sqrt{3}\,\|X\|_{\mathrm{op}}=7.644008$ |
| $\bigl|\operatorname{tr}(X^{2})\bigr|^{1/2}$ | $1.732051$ | $\le\|X\|_{\mathrm{F}}=5.656854$ |
| $|\operatorname{tr}X|$ | $3$ | $\le\sqrt{3}\,\|X\|_{\mathrm{F}}=9.797959$ |
| $|\det X|$ | $25$ | $\le\|X\|_{\mathrm{op}}^{3}=85.957059$ |
| $|\det X|$ | $25$ | $\le\bigl(\|X\|_{\mathrm{F}}/\sqrt{3}\bigr)^{3}=34.837187$ |

**The last two rows are the determinant bounds.** The determinant is bounded by the product of the singular values, which is at most $\|X\|_{\mathrm{op}}^{n}$, and by the geometric mean bound $\bigl(\|X\|_{\mathrm{F}}/\sqrt{n}\bigr)^{n}$. The two bounds coincide for a scalar multiple of an orthogonal matrix. Also $\rho(X)^{3}=58.614503$ bounds $|\det X|=25$ from above, because the determinant is the product of the eigenvalues.

## Summary

Four objects live on $M_n(\mathbb{R})$. The trace form $\operatorname{tr}(XY)$ is invariant under conjugation by $\mathrm{GL}_n(\mathbb{R})$ and under the inner derivations, of inertia $\bigl(n(n+1)/2,n(n-1)/2\bigr)$. The Hilbert–Schmidt form $\operatorname{tr}(X^{\mathsf T}Y)$ is invariant only under $X\mapsto QXR^{\mathsf T}$ with $Q,R\in\mathrm{O}(n)$, and it is positive definite. The Killing form $\operatorname{K}(X,Y)=2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y)$ is invariant under all automorphisms, with a radical of dimension one and the inertia of the trace form on the quotient. The determinant is multiplicative and invariant under conjugation, of degree $n$. The algebraic norm of the central simple algebra $M_n(\mathbb{R})$ is $\det$ and its algebraic trace is $\operatorname{tr}$, so the norm form of the algebra is the determinant. That norm form is a quadratic form only at $n=2$, where it has inertia $(2,2)$ and is the norm of the split-quaternion algebra; at $n\ge3$ it has degree $n$ and is not a power of a quadratic form, by the irreducibility of the determinant and by degree. The derivative of $\log\det$ at the identity is the trace, which is the infinitesimal form of $\det(\exp H)=\exp(\operatorname{tr}H)$. The operator, Frobenius, trace-form and spectral quantities coincide on the symmetric part, coincide in absolute value on the antisymmetric part, and satisfy the chain $\rho\le\|\cdot\|_{\mathrm{op}}\le\|\cdot\|_{\mathrm{F}}\le\sqrt{n}\|\cdot\|_{\mathrm{op}}$ together with the two Cauchy–Schwarz bounds, all checked at $n=3$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{tr}(XY)$ | the trace form, of inertia $\bigl(n(n+1)/2,n(n-1)/2\bigr)$ |
| $\operatorname{tr}(X^{\mathsf T}Y)$ | the Hilbert–Schmidt form, positive definite |
| $\operatorname{K}(X,Y)$ | the Killing form, with radical $\mathbb{R}\mathrm{I}$ |
| $\det X$ | the determinant, the reduced norm of the algebra |
| $\operatorname{Tred}$, $\operatorname{Nred}$ | the reduced trace and the reduced norm |
| $\|X\|_{\mathrm{op}}$ | the operator norm, the largest singular value |
| $\|X\|_{\mathrm{F}}$ | the Frobenius norm, the norm of the Hilbert–Schmidt form |
| $\|X\|_{\mathrm{tr}}$ | $\bigl|\operatorname{tr}(X^{2})\bigr|^{1/2}$, the trace-form quantity |
| $\rho(X)$ | the spectral radius, the largest modulus of an eigenvalue |
| $B(X,Y)$ | the polar form $\tfrac14\bigl(\det(X+Y)-\det(X-Y)\bigr)$ at $n=2$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the reduced trace, the reduced norm and the norm form of a central simple algebra.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for norm forms, quaternion algebras and inertias.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the operator norm, the Frobenius norm, the spectral radius and their inequalities.
- [The Trace Form and Its Indefinite Inertia](the-trace-form-and-its-indefinite-inertia.html), for the first row of the table.
- [The Hilbert–Schmidt Form: Definite but Not Invariant](the-hilbert-schmidt-form-definite-but-not-invariant.html), for the second row.
- [The Killing Form, Its Radical and the Centre of $\mathfrak{gl}_n(\mathbb{R})$](the-killing-form-its-radical-and-the-centre-of-gl-n-r.html), for the third row.
- [Split-Quaternion Algebra](split-quaternion-algebra.html), for the case $n=2$ and the norm form of inertia $(2,2)$.
