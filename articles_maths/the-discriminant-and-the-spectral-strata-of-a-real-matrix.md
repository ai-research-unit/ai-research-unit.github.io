# __The Discriminant and the Spectral Strata of a Real Matrix__

## Introduction

**The discriminant of the characteristic polynomial is one real polynomial in the entries, and its zero set is exactly the set of matrices with a repeated eigenvalue.** It is therefore the wall that separates the spectral strata, and its sign is constant on each connected region of the complement.

The article defines the discriminant as a symmetric function of the roots, proves that it is a polynomial in the coefficients of degree $2n-2$, that it vanishes exactly at a repeated root, and that it is a similarity invariant. It describes the stratification of $M_n(\mathbb{R})$ by root multiplicity, the constancy of the number of real roots on the complement, the case $n=2$ where the discriminant is a quadratic form of inertia $(2,1)$, a count on $100$ random real $3\times3$ matrices, and the boundary between the elliptic and hyperbolic regions. It assumes *The Elementary Symmetric Functions and the Real Characteristic Polynomial*, which defers this construction here.

## The Discriminant of a Polynomial

**Definition.** For a monic polynomial $p$ of degree $n$ with roots $\lambda_1,\dots,\lambda_n$ in $\mathbb{C}$, counted with multiplicity,

$$
\Delta(p)=\prod_{1\le i<j\le n}(\lambda_i-\lambda_j)^{2}.
$$

**The discriminant is symmetric in the roots.** A permutation of the roots permutes the factors of the product, so $\Delta$ is unchanged. By the fundamental theorem of symmetric polynomials, $\Delta$ is a polynomial with integer coefficients in the elementary symmetric functions $e_1,\dots,e_n$, that is, in the coefficients of $p$.

**The discriminant lives in the base field.** For $p=\chi_A$ the coefficients are real, so $\Delta(\chi_A)$ is a real number, computed from the entries without leaving $\mathbb{R}$ and without extracting a root.

**Proposition.** $\Delta(p)=0$ exactly when $p$ has a repeated root.

*Proof.* The product vanishes exactly when one factor $\lambda_i-\lambda_j$ with $i<j$ vanishes, that is, exactly when two roots coincide.

**Proposition.** $\Delta$ is homogeneous of degree $n(n-1)$ in the roots and of degree $2n-2$ in the coefficients.

*Proof.* There are $\binom{n}{2}$ factors, each of degree $2$ in the roots, so the degree in the roots is $2\binom{n}{2}=n(n-1)$. For the coefficients, the resultant $\operatorname{Res}(p,p')$ is the determinant of the Sylvester matrix of order $2n-1$, and every term of that determinant is a product of one entry from each row, hence a monomial of degree $2n-1$ in the coefficients of $p$ and $p'$. So the resultant is homogeneous of degree $2n-1$, and $\Delta=\pm\operatorname{Res}(p,p')/a_n$ is homogeneous of degree $2n-2$. The degrees read $2$ at $n=2$, $4$ at $n=3$ and $6$ at $n=4$.

**The discriminant is, up to a sign, the resultant of $p$ and $p'$.** Since $p'(\lambda_i)=\prod_{j\ne i}(\lambda_i-\lambda_j)$,

$$
\prod_{i=1}^{n}p'(\lambda_i)=\prod_{i\ne j}(\lambda_i-\lambda_j)=(-1)^{\binom{n}{2}}\Delta(p).
$$

The product on the left is the resultant of $p$ and $p'$ up to the leading coefficient, so $\Delta$ vanishes exactly when $p$ and $p'$ have a common root. On the eigenvalues of a random real matrix of size $2,3,4$ the two sides agree to rounding.

## The Two Smallest Cases

**At $n=2$ the discriminant is the discriminant of the quadratic.** For $\chi_A(t)=t^{2}-t\operatorname{tr}A+\det A$ with roots $\lambda_1,\lambda_2$,

$$
\Delta=(\lambda_1-\lambda_2)^{2}=(\lambda_1+\lambda_2)^{2}-4\lambda_1\lambda_2=(\operatorname{tr}A)^{2}-4\det A .
$$

**At $n=3$ the discriminant is the discriminant of the cubic.** With $t=\operatorname{tr}A$, $s=\tfrac12(t^{2}-\operatorname{tr}A^{2})$ and $d=\det A$,

$$
\chi_A(\lambda)=\lambda^{3}-t\lambda^{2}+s\lambda-d,\qquad
\Delta=t^{2}s^{2}-4s^{3}-4t^{3}d-27d^{2}+18tsd .
$$

The formula is homogeneous of degree $4$ in $t,s,d$. On random real $3\times3$ matrices the two sides, the product of the squared differences and the polynomial in $t,s,d$, agree to six decimals.

**The two formulas are the first of a family.** For every $n$ the discriminant is a polynomial in the $n$ coefficients, but its expansion grows fast: the number of terms of the general discriminant is large from $n=4$ on. The structural statements above do not depend on the expansion.

## The Spectral Strata

**The regular stratum is open and dense.** The set

$$
U=\{A:\text{the }n\text{ eigenvalues of }A\text{ are distinct}\}=\{A:\Delta(\chi_A)\ne0\}
$$

is the complement of the zero set of a nonzero polynomial, so it is open and dense, and its complement has empty interior. A matrix of $U$ has $n$ distinct eigenvalues, hence $n$ distinct eigenspaces, and its conjugacy class is the set of all matrices with the same spectrum.

**The discriminant is a hypersurface of codimension one.** The set $\{\Delta=0\}$ is a real algebraic hypersurface of $M_n(\mathbb{R})\cong\mathbb{R}^{n^{2}}$, of dimension $n^{2}-1$ whenever $\Delta$ is not identically zero, and $\Delta$ is not identically zero because a diagonal matrix with distinct entries has $\Delta\ne0$.

**A root of multiplicity $m$ costs $m-1$ conditions.** The condition that $\lambda$ be a root of multiplicity at least $m$ is

$$
p(\lambda)=p'(\lambda)=\cdots=p^{(m-1)}(\lambda)=0,
$$

which is $m$ equations in the $n+1$ unknowns given by the coefficients and $\lambda$; eliminating $\lambda$ leaves $m-1$ conditions on the coefficients. So a double root has codimension $1$, a triple root codimension $2$, and the stratum of matrices with a root of multiplicity exactly $m$ and all other roots simple has dimension $n^{2}-(m-1)$.

**The strata are unions of conjugacy orbits.** Conjugation preserves the characteristic polynomial, hence the discriminant and the multiplicity pattern. Each stratum is therefore a union of orbits, and the orbit of a matrix is determined by its Jordan form, not by its spectrum alone; the stratum of a repeated eigenvalue contains several orbits, distinguished by the sizes of the blocks.

## The Real Stratification

**On each connected component of the complement the number of real roots is constant.** Suppose that a continuous path in the complement joins two matrices with different numbers of real eigenvalues. The eigenvalues are continuous functions of the matrix, and a real eigenvalue can become nonreal only by colliding with another real eigenvalue, at a matrix where the discriminant vanishes. So the number $r$ is constant on each component.

**The sign of the discriminant is also constant on each component.** The function $\Delta\circ\chi$ is continuous and never zero there, so it has a constant sign. The two invariants, the sign and the number of real eigenvalues, are not independent: at $n=2$ the sign is positive exactly when both roots are real.

**The complement splits into an elliptic part and a hyperbolic part.** A component on which all eigenvalues are real is a **hyperbolic** region, and one on which some pair is conjugate is an **elliptic** region. At $n=2$ the hyperbolic part is $\{\Delta>0\}$ and the elliptic part is $\{\Delta<0\}$, and the discriminant is their common boundary. At higher $n$ the same vocabulary applies component by component.

**The stratification is real, not complex.** Over $\mathbb{C}$ the discriminant detects the collision of two eigenvalues but not their reality, because every root is real in the only sense available, namely that it lies in $\mathbb{C}$. Over $\mathbb{R}$ the same hypersurface carries the extra information of the number of real roots on each side.

## The Case $n=2$: A Quadratic Cone of Inertia $(2,1)$

**For a $2\times2$ matrix the discriminant is a quadratic form in the four entries.** Write

$$
A=\begin{pmatrix}a&b\\ c&d\end{pmatrix},\qquad \operatorname{tr}A=a+d,\qquad \det A=ad-bc .
$$

Then

$$
\Delta=(a+d)^{2}-4(ad-bc)=(a-d)^{2}+4bc .
$$

**The form does not see the trace.** The right-hand side depends on $a-d$, $b$ and $c$, but not on $a+d$. So $\Delta$ is invariant under the translation $A\mapsto A+\tau\mathrm{I}$, which shifts both roots by $\tau$ and preserves their difference. In the decomposition

$$
M_2(\mathbb{R})=\mathfrak{sl}_2(\mathbb{R})\oplus\mathbb{R}\mathrm{I}
$$

the discriminant is pulled back from the traceless part, and it is constant along the centre.

**On the traceless part it has inertia $(2,1)$.** Write a traceless matrix as

$$
A=\begin{pmatrix}x&y\\ z&-x\end{pmatrix},
$$

so that the discriminant is $4x^{2}+4yz$. The symmetric matrix of this form in the coordinates $(x,y,z)$ is

$$
\begin{pmatrix}4&0&0\\ 0&0&2\\ 0&2&0\end{pmatrix},
$$

whose eigenvalues are $4$, $2$ and $-2$: the inertia is $(2,1)$. Adding the degenerate trace direction gives a form on $\mathbb{R}^{3}\times\mathbb{R}$ of rank $3$ and inertia $(2,1)$, with a one-dimensional radical.

**The zero set is a cone.** The equation $x^{2}+yz=0$ is the cone over a circle in the traceless part, and it is the null cone of the Killing form of $\mathfrak{sl}_2(\mathbb{R})$, which is $4\operatorname{tr}(A^{2})=8(x^{2}+yz)$. So the discriminant cone and the null cone of the Killing form are the same cone, up to the factor.

## A Count on Random Matrices

**A random real $3\times3$ matrix has either three real eigenvalues or one.** A cubic with real coefficients has an odd number of real roots counted with multiplicity, so the possibilities are three and one; the value zero is a codimension-one event and does not occur on a random matrix.

**The measurement.** On $100$ random real $3\times3$ matrices with independent standard normal entries, $36$ have three real eigenvalues and $64$ have one real eigenvalue and one conjugate pair. The split is not even, and the majority side is the elliptic one. The count is a property of the sample, not a theorem: what is a theorem is that both strata have positive measure and that the discriminant is the boundary between them.

**The two counts are read from the discriminant.** The sign of $\Delta$ separates the two cases at $n=3$ as well, by the general rule that the number of real roots is constant on each component of the complement.

## Invariance and the Boundary

**The discriminant is a similarity invariant.** For $S\in\mathrm{GL}_n(\mathbb{R})$ the matrices $A$ and $SAS^{-1}$ have the same characteristic polynomial, hence the same discriminant. So $\Delta$ is a conjugation-invariant polynomial on $M_n(\mathbb{R})$, of degree $2n-2$ in the coefficients, and it descends to a function on the set of conjugacy classes. On a random real $3\times3$ matrix and a random real conjugate the two values agree, here $-442.294218$ for both.

**It vanishes on the boundary between the elliptic and the hyperbolic regions.** At $n=2$ the hyperbolic region $\{\Delta>0\}$ and the elliptic region $\{\Delta<0\}$ are separated by $\{\Delta=0\}$, the parabolic set, where the two roots coincide. The three names are the classical ones for the three cases: two real roots, a double root, a conjugate pair.

**The discriminant is not a complete invariant.** Matrices with the same discriminant need not be conjugate, and even the whole characteristic polynomial does not determine the conjugacy class when roots repeat. The discriminant answers one question, namely whether the spectrum has a collision, and it answers it exactly.

## Summary

The discriminant of the characteristic polynomial is the product of the squared differences of the roots. It is a symmetric function of the roots, hence a polynomial in the coefficients of degree $2n-2$, and it is homogeneous of degree $n(n-1)$ in the roots. It vanishes exactly when two eigenvalues coincide, so its zero set is the hypersurface that separates the open dense stratum of matrices with distinct eigenvalues from the strata with a repeated root; a root of multiplicity $m$ costs $m-1$ conditions. The sign of the discriminant and the number of real roots are constant on each connected component of the complement, which is why the discriminant is the boundary between the elliptic and the hyperbolic regions. At $n=2$ it is $(\operatorname{tr}A)^{2}-4\det A$, a quadratic form of inertia $(2,1)$ on the traceless part, degenerate along the centre. On $100$ random real $3\times3$ matrices, $36$ have three real eigenvalues and $64$ have one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Delta(p)$ | the discriminant, $\prod_{i<j}(\lambda_i-\lambda_j)^{2}$ |
| $\chi_A$ | the characteristic polynomial of $A$ |
| $e_k$ | the $k$-th elementary symmetric function, a coefficient of $\chi_A$ |
| $t,s,d$ | the trace, the second coefficient and the determinant at $n=3$ |
| $U$ | the open dense set of matrices with distinct eigenvalues |
| $r$ | the number of real eigenvalues, counted with multiplicity |
| $\mathfrak{sl}_2(\mathbb{R})$ | the traceless $2\times2$ matrices, of dimension $3$ |
| $\{\Delta=0\}$ | the discriminant hypersurface, of codimension one |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the discriminant of the characteristic polynomial and its invariance.
- B. L. van der Waerden, *Algebra* (Springer, 1991), for the discriminant, the resultant and the symmetric functions.
- [The Elementary Symmetric Functions and the Real Characteristic Polynomial](the-elementary-symmetric-functions-and-the-real-characteristic-polynomial.html), for the coefficients that the discriminant is a polynomial in.
- [The Real Spectrum: Real Roots and Conjugate Pairs](the-real-spectrum-real-roots-and-conjugate-pairs.html), for the count of real roots and pairs.
- [The Minimal Polynomial over $\mathbb{R}$ and the Real Jordan Form](the-minimal-polynomial-over-r-and-the-real-jordan-form.html), for the orbits inside a stratum.
