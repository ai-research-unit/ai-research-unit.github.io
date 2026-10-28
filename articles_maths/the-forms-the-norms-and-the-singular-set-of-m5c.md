# __The Forms, the Norms and the Singular Set__

## Introduction

The determinant is a **multiplicative form** on $M_5(\mathbb{C})$: it is a homogeneous polynomial of degree $5$,

$$
\det(\lambda A)=\lambda^5\det A,\qquad \det(AB)=\det A\det B,
$$

and it is the norm of the algebra in the sense of a multiplicative form. It is **not** a norm in the analytic sense: it is complex-valued, it is not positive, and it is not homogeneous of degree one. The analytic norms are the Frobenius norm

$$
\|A\|_F^2=\operatorname{tr}(A^*A)=\sum_{i,j}|A_{ij}|^2
$$

and the operator norm

$$
\|A\|_{\mathrm{op}}=\sup_{\|x\|=1}\|Ax\| .
$$

The article distinguishes the determinant **form** from the two **norms**, and it studies the **singular set**

$$
\Sigma=\{A:\det A=0\},
$$

the zero locus of the determinant. The singular set is a complex hypersurface of complex dimension $24$ and **real codimension $2$** in $M_5\cong\mathbb{R}^{50}$. It is the union of the determinantal varieties of rank at most $4$, with the rank stratification

$$
M_5^{(0)}\subset M_5^{(1)}\subset M_5^{(2)}\subset M_5^{(3)}\subset M_5^{(4)}=\Sigma,
$$

of complex dimensions $0,9,16,21,24$ and complex codimensions $25,16,9,4,1$. The successive differences of the codimensions are the odd numbers

$$
1,3,5,7,9,
$$

the dimensions of the adjoint summands of *The Spin Chain and the Adjoint Decomposition*.

The trace form $\operatorname{tr}(A^*B)$ is positive definite and has **no null cone**; the singular set is not a null cone of the metric. The complex bilinear pairing $\operatorname{tr}(AB)$ is indefinite, and its isotropic cone is a different set. The article assumes the matrix algebra, the trace and the involution; it uses the spectral theorem only through the definition of the operator norm, and it proves the basic inequalities directly.

## The Determinant as a Form

### Homogeneity and Multiplicativity

**Proposition.** The determinant is a homogeneous polynomial of degree $5$ on $M_5(\mathbb{C})$:

$$
\det(\lambda A)=\lambda^5\det A,\qquad \det(AB)=\det A\det B,\qquad \det I=1 .
$$

It is not additive: $\det(A+B)\ne\det A+\det B$ in general.

**Proof.** Each of the $5!$ terms in the Leibniz formula contains exactly one entry from each of the five rows and columns, so the degree is $5$; the multiplicativity is the standard theorem of determinants; the identity has determinant $1$. For the failure of additivity, take $A=B=I$: $\det(2I)=32\ne2=\det I+\det I$.

**Corollary.** The determinant is a **multiplicative form** of degree $5$: it is a polynomial that converts the algebra product into the product of scalars. The zero set is the set of non-units.

**Proof.** $\det(AB)=\det A\det B$ and $\det A\ne0$ iff $A$ is invertible; the zero set is the complement of the unit group.

### The Norm of a Matrix

**Definition.** The **determinant norm** of $A$ is $N(A)=\det A$.

**Proposition.** The determinant norm is multiplicative and homogeneous of degree $5$, but it is not a norm in the analytic sense: it takes complex values, it is not positive, and it is not subadditive.

**Proof.** The multiplicativity and homogeneity are above. The determinant of $iI$ is $i^5=i$, which is not real; the determinant of a nilpotent matrix is $0$ although the matrix is nonzero; the determinant of $I+(-I)=0$ is $0$, while $\det I+\det(-I)=1-1=0$, but $\det(I+I)=32\ne2$. The triangle inequality fails.

**Corollary.** The determinant norm is a **multiplicative form**: $N(AB)=N(A)N(B)$. It is not a quadratic form, so $M_5(\mathbb{C})$ is not a composition algebra in the classical sense (a composition algebra has a nondegenerate quadratic norm and dimension $1,2,4$ or $8$). The form is not positive definite and has nontrivial zeros; the algebra is not a division algebra.

**Proof.** The multiplicativity is the composition property; the form has degree $5$, not $2$, so it is not the quadratic norm of a composition algebra. The nilpotent matrices are nonzero with norm zero, so there are zero divisors.

**Remark.** **The word "norm" has three meanings in this category.** The determinant norm is the multiplicative form of degree $5$; the Frobenius norm is the Euclidean norm of the $25$ coordinates; the operator norm is the sup norm on the unit sphere. They agree only in special cases: for a scalar matrix $\lambda I$, $\det(\lambda I)=\lambda^5$, $\|\lambda I\|_F=\sqrt5|\lambda|$, $\|\lambda I\|_{\mathrm{op}}=|\lambda|$. The three must not be confused.

### The Determinant Form on $M_5$

**Definition.** The **polar forms** of the determinant are the multilinear forms obtained by polarizing the homogeneous polynomial $\det$. The first polar form at $A$ in the direction $H$ is the derivative

$$
D\det_A(H)=\operatorname{tr}(\operatorname{adj}(A)H).
$$

**Proposition.** The derivative of the determinant at $A$ is the linear form $H\mapsto\operatorname{tr}(\operatorname{adj}(A)H)$; at $A=I$ it is $H\mapsto\operatorname{tr}H$.

**Proof.** Expand $\det(A+tH)$ in powers of $t$; the linear term is the sum over the positions of $H$ with the cofactor of $A$, which is $\operatorname{tr}(\operatorname{adj}(A)H)$. At $A=I$, $\operatorname{adj}(I)=I$, so the derivative is the trace.

**Corollary.** The determinant is a local coordinate near $I$; its level set $\det=1$ is a hypersurface of complex dimension $24$ with tangent space $\mathfrak{sl}_5$.

**Proof.** The derivative at $I$ is the nonzero linear form $\operatorname{tr}$; its kernel is $\mathfrak{sl}_5$, of dimension $24$; the implicit function theorem gives the smooth hypersurface.

**Remark.** **The determinant is a polynomial, not a norm.** The polar forms are the algebraic linearizations; the gradient with respect to the trace pairing is the adjugate, $\langle\operatorname{adj}(A),H\rangle=\operatorname{tr}(\operatorname{adj}(A)H)$. The determinant is the **norm form** of the algebra, and its polar forms are the algebraic substitutes for the inner product that the determinant does not provide.

## The Bilinear and Hermitian Forms

### The Trace Pairing

**Definition.** The **trace pairing** is $\langle A,B\rangle_{\mathrm{tr}}=\operatorname{tr}(AB)$.

**Proposition.** The trace pairing is complex bilinear, symmetric and nondegenerate; it is **indefinite**, with isotropic vectors: a nonzero nilpotent $A$ satisfies $\operatorname{tr}(A^2)=0$.

**Proof.** The bilinearity and symmetry are the trace identities; the nondegeneracy is the matrix-unit computation $\langle E_{ij},E_{ji}\rangle=1$; a nilpotent $A\ne0$ has $A^2=0$ and trace zero.

**Corollary.** The trace pairing has an isotropic cone $\{A:\operatorname{tr}(A^2)=0\}$, a complex quadric hypersurface. The cone is not the singular set $\det=0$ and is not the null cone of the Frobenius form.

**Proof.** The equation $\operatorname{tr}(A^2)=0$ is a nonzero quadratic equation, hence a quadric hypersurface; the nilpotents give nonzero points; the determinant zero set is a different hypersurface.

### The Frobenius Form

**Definition.** The **Frobenius form** is $\langle A,B\rangle_F=\operatorname{tr}(A^*B)$.

**Theorem.** The Frobenius form is a positive definite Hermitian inner product; the only null vector is zero. It defines the Frobenius norm $\|A\|_F=\sqrt{\langle A,A\rangle_F}$.

**Proof.** $\langle A,A\rangle_F=\sum_{ij}|A_{ij}|^2$, positive for $A\ne0$; the conjugate symmetry is $\overline{\operatorname{tr}(A^*B)}=\operatorname{tr}(B^*A)$.

**Corollary.** The Frobenius form has no null cone. Its unit sphere is the set of matrices with $\sum_{ij}|A_{ij}|^2=1$, a real sphere of dimension $49$.

**Proof.** Positive definiteness excludes nonzero null vectors; the unit sphere is the sphere in $\mathbb{R}^{50}$.

### The Operator Norm

**Definition.** The **operator norm** is

$$
\|A\|_{\mathrm{op}}=\sup_{\|x\|_2=1}\|Ax\|_2,
$$

where $\|\cdot\|_2$ is the standard Hermitian norm on $\mathbb{C}^5$.

**Proposition.** The operator norm is a norm, and

$$
\|A\|_{\mathrm{op}}\le\|A\|_F\le\sqrt5\,\|A\|_{\mathrm{op}} .
$$

**Proof.** The operator norm is the sup of the continuous function $x\mapsto\|Ax\|$ on the compact unit sphere; the triangle inequality and homogeneity are immediate. For the first inequality, $\|Ax\|_2^2=\sum_i|\sum_jA_{ij}x_j|^2\le\sum_i(\sum_j|A_{ij}|^2)(\sum_j|x_j|^2)=\|A\|_F^2\|x\|_2^2$ by Cauchy–Schwarz. For the second, $\|A\|_F^2=\sum_i\|Ae_i\|_2^2\le\sum_i\|A\|_{\mathrm{op}}^2=5\|A\|_{\mathrm{op}}^2$.

**Corollary (Hadamard).** $|\det A|\le\|A\|_{\mathrm{op}}^5$.

**Proof.** The determinant is the product of the norms of the columns times the volume of the parallelepiped, which is at most $1$; more directly, Hadamard's inequality gives $|\det A|\le\prod_i\|a_i\|_2\le\|A\|_{\mathrm{op}}^5$, because each column has norm at most the operator norm.

**Remark.** **The operator norm is not polynomial.** It is the spectral norm, equal to the square root of the largest eigenvalue of $A^*A$; the spectral theorem for $A^*A$ is *Spectral Theory and the Spectral Projectors*. The inequality with the Frobenius norm is proved here without the spectral theorem, and it is the only comparison needed in this article.

## The Singular Set

### The Determinant Hypersurface

**Definition.** The **singular set** is

$$
\Sigma=\{A\in M_5(\mathbb{C}):\det A=0\}.
$$

**Theorem.** $\Sigma$ is a complex algebraic hypersurface of complex dimension $24$ and real dimension $48$; its complement $GL_5(\mathbb{C})$ is a nonempty Zariski open set of complex dimension $25$ and real dimension $50$.

**Proof.** The determinant is a nonconstant polynomial on $M_5\cong\mathbb{C}^{25}$; its zero locus is a hypersurface of complex dimension $24$; the complement is the nonvanishing locus of a polynomial, a nonempty Zariski open set. The real dimensions are twice the complex dimensions.

**Corollary.** $\Sigma$ has **real codimension $2$**. At a point of rank $4$, the derivative of the determinant is nonzero, and the zero set is locally the zero set of one complex equation, equivalently two independent real equations.

**Proof.** At rank $4$, $\operatorname{adj}(A)\ne0$, so the derivative $H\mapsto\operatorname{tr}(\operatorname{adj}(A)H)$ is a nonzero complex-linear functional; its kernel has real codimension $2$.

### The Rank Strata

**Definition.** The **determinantal variety** of rank at most $r$ is

$$
M_5^{(r)}=\{A:\operatorname{rank}A\le r\},\qquad r=0,1,\dots,5 .
$$

**Theorem.** $M_5^{(r)}$ is an irreducible algebraic variety of complex dimension

$$
\dim M_5^{(r)}=r(10-r),
$$

and complex codimension $(5-r)^2$. The exact rank-$r$ stratum $M_5^{(r)}\setminus M_5^{(r-1)}$ has the same dimension $r(10-r)$ and is smooth.

**Proof.** A rank-$r$ matrix factors as $A=UV$ with $U\in\mathbb{C}^{5\times r}$ and $V\in\mathbb{C}^{r\times5}$; the pair $(U,V)$ has $10r$ parameters, and the ambiguity is the action of $GL_r$, of dimension $r^2$; hence the dimension is $10r-r^2=r(10-r)$. The exact rank-$r$ matrices form a homogeneous space of $GL_5\times GL_5$ and are smooth; the lower-rank loci are the singular strata. The codimension is $25-r(10-r)=(5-r)^2$.

**Corollary.** The dimensions and codimensions are

| $r$ | $\dim M_5^{(r)}$ | complex codimension | real codimension |
|---|---|---|---|
| $0$ | $0$ | $25$ | $50$ |
| $1$ | $9$ | $16$ | $32$ |
| $2$ | $16$ | $9$ | $18$ |
| $3$ | $21$ | $4$ | $8$ |
| $4$ | $24$ | $1$ | $2$ |
| $5$ | $25$ | $0$ | $0$ |

**Proof.** Evaluate $r(10-r)$ and $(5-r)^2$; the real codimension is twice the complex codimension.

**Corollary.** The singular set is $\Sigma=M_5^{(4)}$, of complex dimension $24$ and real codimension $2$. Its singular locus is $M_5^{(3)}$, of complex dimension $21$; the successive singular loci are the lower-rank varieties.

**Proof.** The derivative of the determinant vanishes exactly where the adjugate vanishes, i.e., at rank at most $3$; the rank-$4$ points are smooth. The singular locus of $M_5^{(3)}$ is $M_5^{(2)}$, and so on.

**Remark.** **The successive codimensions of the rank strata are the odd numbers $1,3,5,7,9$.** The codimensions are the squares $1,4,9,16,25$; their differences are $3,5,7,9$ and the first is $1$. These are the dimensions of the adjoint summands $V_0,\dots,V_4$ of *The Spin Chain and the Adjoint Decomposition*. The coincidence is a numerical pattern of the two stratifications; the rank strata and the adjoint summands are different objects.

### The Singular Locus

**Proposition.** The singular locus of $\Sigma$ is $M_5^{(3)}$, the matrices of rank at most $3$. The smooth locus of $\Sigma$ is the exact rank-$4$ stratum.

**Proof.** The gradient of the determinant is the adjugate; the adjugate vanishes exactly when the rank is at most $3$ (all $4\times4$ minors vanish). At rank $4$, at least one $4\times4$ minor is nonzero, so the gradient is nonzero and the hypersurface is smooth.

**Corollary.** The rank stratification is a Whitney stratification of $\Sigma$; the codimensions in $\Sigma$ of the strata of ranks $3,2,1,0$ are $3,8,15,24$, and the successive differences are $3,5,7,9$.

**Proof.** The codimension in $\Sigma$ of $M_5^{(r)}$ is $(5-r)^2-1$ for $r\le3$: for $r=3$, $4-1=3$; for $r=2$, $9-1=8$; for $r=1$, $16-1=15$; for $r=0$, $25-1=24$. The successive differences are $5,7,9$ after the initial $3$. The determinantal varieties are classic examples of Whitney stratifications.

## The Norm and the Singular Set

### No Null Cone

**Theorem.** The Frobenius form is positive definite, so it has no null cone; the only null vector is zero. The singular set $\Sigma$ is not a null cone of the Frobenius form.

**Proof.** $\langle A,A\rangle_F=0$ implies $A=0$; $\Sigma$ contains nonzero matrices (the nilpotents), so it is not the null set.

**Corollary.** The determinant zero set and the isotropic cone of the trace pairing are different hypersurfaces. The first is the set of non-units; the second is the set of matrices with $\operatorname{tr}(A^2)=0$.

**Proof.** The determinant vanishes on every singular matrix; $\operatorname{tr}(A^2)$ vanishes on the nilpotents and on many other matrices; the two equations are different.

### The Norm's Zero Set

**Proposition.** The zero set of the determinant norm is $\Sigma$; the norm is not positive, and its zero set is the singular set. The Frobenius norm and the operator norm have zero set $\{0\}$.

**Proof.** $\det A=0$ iff $A\in\Sigma$; the analytic norms vanish only at the zero matrix.

**Corollary.** The determinant norm is a **multiplicative form with zeros**, not a norm; the singular set is its zero locus. The two analytic norms are positive definite and have no zeros except $0$; they define the Hilbert space structure of *The Involution and the Hermitian Structure*.

**Proof.** The multiplicativity and the zeros are the determinant properties; the positivity of the analytic norms is the sum of squares.

**Remark.** **The singular set is $\det=0$, of real codimension $2$, and it is not a null cone.** The determinant norm is a multiplicative form of degree $5$; its zero set is the singular set. The positive definite forms have no null cone; the indefinite trace pairing has an isotropic cone, but that cone is a different object. The three notions — zeros of the determinant, isotropic vectors of the trace pairing, null vectors of the Frobenius form — must be kept apart.

## Summary

The determinant is a multiplicative form of degree $5$; it is the norm of the algebra, but it is not a norm in the analytic sense. The analytic norms are the Frobenius norm and the operator norm, related by $\|A\|_{\mathrm{op}}\le\|A\|_F\le\sqrt5\|A\|_{\mathrm{op}}$. The determinant is bounded by the operator norm, $|\det A|\le\|A\|_{\mathrm{op}}^5$ (Hadamard).

$$
\boxed{\ \det\text{ is a multiplicative form of degree }5;\quad \Sigma=\{\det=0\}\text{ has real codimension }2;\quad \text{no null cone.}\ }
$$

The singular set is the determinantal hypersurface of rank at most $4$, of complex dimension $24$ and real codimension $2$. The rank strata have complex dimensions $0,9,16,21,24$ and complex codimensions $25,16,9,4,1$; their successive codimensional differences are the odd numbers $1,3,5,7,9$. The singular locus of $\Sigma$ is the rank-at-most-$3$ variety. The Frobenius form is positive definite and has no null cone; the trace pairing is indefinite and has an isotropic cone; the determinant zero set is neither.

| Object | Value |
|---|---|
| Determinant | Multiplicative form of degree $5$ |
| Frobenius norm | $\sqrt{\sum_{ij}|A_{ij}|^2}$ |
| Operator norm | $\sup_{\|x\|=1}\|Ax\|$ |
| Norm comparison | $\|A\|_{\mathrm{op}}\le\|A\|_F\le\sqrt5\|A\|_{\mathrm{op}}$ |
| Hadamard | $|\det A|\le\|A\|_{\mathrm{op}}^5$ |
| Singular set | $\det=0$, complex dimension $24$ |
| Real codimension | $2$ |
| Rank strata | dimensions $0,9,16,21,24$ |
| Codimensions | $25,16,9,4,1$ |
| Null cone | none for the Frobenius form |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $N(A)=\det A$ | The determinant norm |
| $\|A\|_F$ | The Frobenius norm |
| $\|A\|_{\mathrm{op}}$ | The operator norm |
| $\langle A,B\rangle_{\mathrm{tr}}=\operatorname{tr}(AB)$ | The trace pairing, indefinite |
| $\langle A,B\rangle_F=\operatorname{tr}(A^*B)$ | The Frobenius form, positive definite |
| $\Sigma=\{\det=0\}$ | The singular set |
| $M_5^{(r)}$ | The matrices of rank at most $r$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2013), for the determinant, the operator norm, Hadamard's inequality and the singular values.
- Israel M. Gelfand, Mikhail M. Kapranov and Andrei V. Zelevinsky, *Discriminants, Resultants, and Multidimensional Determinants* (Birkhäuser, 1994), for the determinant as a form, the discriminants and the determinantal varieties.
- Joe Harris, *Algebraic Geometry: A First Course* (Springer, 1992), for the determinantal varieties, their dimensions and their singular loci.
- [The Involution and the Hermitian Structure](the-involution-and-the-hermitian-structure-of-m5c.html), for the positive definite Frobenius form and the real codimension $2$.
- [The Element, the Coordinates and the Trace](the-element-the-coordinates-and-the-trace-of-m5c.html), for the trace pairing and the determinant.
- [The Quintic and the Spectral Strata](the-quintic-and-the-spectral-strata-of-m5c.html), for the determinant, the discriminant and the spectral strata.
- [Spectral Theory and the Spectral Projectors](spectral-theory-and-the-spectral-projectors-of-m5c.html), for the spectral theorem and the operator norm as the largest singular value.
