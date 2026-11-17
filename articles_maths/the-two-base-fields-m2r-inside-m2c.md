# __The Two Base Fields: $M_2(\mathbb{R})$ inside $M_2(\mathbb{C})$__

## Introduction

**The real matrices are the fixed set of one antilinear involution of $M_2(\mathbb{C})$, and the complex algebra is their complexification.**

The article treats the pair of base fields. It proves that $M_2(\mathbb{R})$ is the fixed algebra of the entrywise conjugation, that $\mathbb{C}\otimes_{\mathbb{R}}M_2(\mathbb{R})\cong M_2(\mathbb{C})$, that the rank survives the change of field while the dimension doubles, that the real and imaginary halves are orthogonal for the real part of the trace form only, and that the algebra has exactly two real forms, $M_2(\mathbb{R})$ and $\mathbb{H}$. It assumes *The Matrix Algebra $M_2(\mathbb{C})$* for the product, the trace and the rank. It defers the splitting of the algebra into Hermitian and anti-Hermitian parts to *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian at $n=2$*, and the spectrum over $\mathbb{C}$ to *The Spectrum of a $2\times2$ Matrix*.

The general theory of the pair $M_n(\mathbb{R})\subset M_n(\mathbb{C})$ is *The Two Base Fields: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$*; every statement below is that theory at $n=2$, with the arithmetic of two made explicit.

## The Real Matrices as a Fixed Set

**Definition.** The **entrywise conjugation** of $M_2(\mathbb{C})$ is the map $\sigma(A)=\bar A$, applied to the four entries.

**Proposition.** The map $\sigma$ is an involutive antilinear automorphism: $\sigma(A+B)=\sigma(A)+\sigma(B)$, $\sigma(\lambda A)=\bar\lambda\sigma(A)$, $\sigma(AB)=\sigma(A)\sigma(B)$, $\sigma^{2}=\mathrm{id}$.

**Proof.** Conjugation of complex numbers is additive, conjugate-linear and multiplicative, and the matrix product is built from sums and products of entries; hence $\overline{AB}=\bar A\bar B$. Applying the conjugation twice returns each entry.

**Theorem.** The fixed set of $\sigma$ is $M_2(\mathbb{R})$, a real subalgebra of real dimension $4$.

**Proof.** An entry is fixed by the conjugation exactly when it is real. The real matrices are closed under sums, products and real scalars, so they form a real subalgebra; their real dimension is the count of the four entries, that is $4$.

**The fixed set is not an ideal and not a complex subspace.** It is closed under multiplication by real scalars only: $iI$ is not real, so $M_2(\mathbb{R})$ is not stable under multiplication by $i$. It is a real form in the sense of *The Element, the Coordinates and the Conjugations*, §*The Real Form*: it meets $iM_2(\mathbb{R})$ only at $0$, and the two together fill the algebra.

## The Complexification

**Theorem.** $\mathbb{C}\otimes_{\mathbb{R}}M_2(\mathbb{R})\cong M_2(\mathbb{C})$ as $\mathbb{C}$-algebras.

**Proof.** The map $\lambda\otimes X\mapsto\lambda X$ is $\mathbb{C}$-bilinear and sends the products of the two algebras to products, since $(\lambda\otimes X)(\mu\otimes Y)=\lambda\mu\otimes XY\mapsto\lambda\mu XY$. It is surjective because $A=X+iY$ with $X=\tfrac12(A+\bar A)$ and $Y=\tfrac1{2i}(A-\bar A)$ real, and both spaces have complex dimension $4$.

**Corollary (the real and imaginary parts).** Every matrix has a unique decomposition

$$
A=X+iY,\qquad X=\tfrac12(A+\bar A)\in M_2(\mathbb{R}),\quad Y=\tfrac1{2i}(A-\bar A)\in M_2(\mathbb{R}),
$$

and the algebra is the direct sum $M_2(\mathbb{R})\oplus iM_2(\mathbb{R})$ of two real four-dimensional subspaces.

**The product in the two parts.** For $A=X+iY$ and $C=U+iV$,

$$
AC=(XU-YV)+i(XV+YU),
$$

so the complex multiplication is the pair of the two real products, with the sign of the second term given by $i^{2}=-1$. The formula is the definition of the complexification read on entries, and it shows that no new product is introduced: the algebra over $\mathbb{C}$ is the algebra over $\mathbb{R}$ with the scalars enlarged.

## Dimension and Rank across the Two Fields

**The dimension doubles and the dimension of the singular set does not follow it.** The real dimension of $M_2(\mathbb{C})$ is $8$ and that of $M_2(\mathbb{R})$ is $4$; the complex dimension of the first is $4$, and the second has no complex dimension because it is not a complex vector space.

**Proposition (the rank is the same).** For $X\in M_2(\mathbb{R})$, the rank of $X$ computed over $\mathbb{R}$ equals its rank computed over $\mathbb{C}$.

**Proof.** The rank is the largest order of a nonvanishing minor, and a minor is a polynomial with integer coefficients in the entries. Its vanishing is therefore a condition on the entries alone, and it does not depend on the field in which the entries are read. At order two the minors are the four entries and the single determinant $ad-bc$, so the statement is the statement that $ad-bc=0$ over $\mathbb{R}$ exactly when it holds over $\mathbb{C}$.

**Corollary.** The three rank strata meet $M_2(\mathbb{R})$ in real dimension $0$, $3$ and $4$: the origin, the rank-one real matrices, and the open set of real matrices of nonzero real determinant.

**The singular set of the real algebra is a genuine cone of a form.** The determinant restricted to $M_2(\mathbb{R})$ is the quadratic form $ad-bc$, whose matrix has two positive and two negative eigenvalues; its zero set is a cone, and it separates the real matrices of positive determinant from those of negative determinant. Over $\mathbb{C}$ the same determinant has no such separation, because the complex numbers are not ordered.

## Real and Imaginary Parts

**The two parts are orthogonal for the real part of the trace form, and not for the form itself.**

**Proposition.** For $A=X+iY$ and $C=U+iV$ with $X,Y,U,V$ real,

$$
\operatorname{Re}\operatorname{tr}(AC)=\operatorname{tr}(XU)-\operatorname{tr}(YV),\qquad
\operatorname{Im}\operatorname{tr}(AC)=\operatorname{tr}(XV)+\operatorname{tr}(YU).
$$

**Proof.** Multiply out, using $\operatorname{tr}(XU)$, $\operatorname{tr}(YV)$, $\operatorname{tr}(XV)$ and $\operatorname{tr}(YU)$ real: the product is $\operatorname{tr}(XU)-\operatorname{tr}(YV)+i\bigl(\operatorname{tr}(XV)+\operatorname{tr}(YU)\bigr)$.

**Corollary (the orthogonality).** The two direct summands $M_2(\mathbb{R})$ and $iM_2(\mathbb{R})$ are orthogonal for the real bilinear form $(A,C)\mapsto\operatorname{Re}\operatorname{tr}(AC)$.

**Proof.** For real $X,U$ the trace $\operatorname{tr}(X\,iU)=i\operatorname{tr}(XU)$ is purely imaginary, since $\operatorname{tr}(XU)$ is real; its real part is zero. The two summands span the algebra, so the form is block diagonal in that decomposition.

**The complex form is isotropic on the two parts.** The matrix $E_{12}+iE_{12}=(1+i)E_{12}$ is nonzero and its square is $(1+i)^{2}E_{12}^{2}=0$, so $\operatorname{tr}\bigl((1+i)^{2}E_{12}^{2}\bigr)=0$. The trace form is indefinite on the complex algebra, and its inertia on the real matrices is computed in *The Trace Form and Its Inertia on the Two Halves of $M_2(\mathbb{R})$*.

## The Two Real Forms

**Definition.** A **real form** of $M_2(\mathbb{C})$ is a real subalgebra $A_0$ of real dimension $4$ with $A_0\oplus iA_0=M_2(\mathbb{C})$.

**Theorem.** Up to conjugation by a complex unit, $M_2(\mathbb{C})$ has exactly two real forms: $M_2(\mathbb{R})$ and the quaternion algebra $\mathbb{H}$.

**Proof.** A real form is the fixed algebra of an antilinear involutive automorphism $\sigma$, and every antilinear automorphism of $M_2(\mathbb{C})$ has the form $\sigma(A)=S\bar AS^{-1}$ for an invertible $S$. The condition $\sigma^{2}=\mathrm{id}$ becomes $S\bar S\in\mathbb{C}^{\times}I$. Rescaling $S$ shows that the two cases are $S\bar S=I$ and $S\bar S=-I$: in the first the fixed algebra is $M_2(\mathbb{R})$, in the second it is the set of matrices $A$ with $A=S\bar AS^{-1}$, which is a copy of $\mathbb{H}$ acting on $\mathbb{C}^{2}$ as the quaternions act on $\mathbb{C}\oplus\mathbb{C}$ by $j\mapsto S\,\bar{\cdot}$. The classification in general is *The Two Base Fields: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$*, §*The Two Real Structures*.

**The quaternionic form.** Take $S=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, so that $S\bar S=-I$. The fixed algebra consists of the matrices

$$
A=\begin{pmatrix}\alpha&\beta\\-\bar\beta&\bar\alpha\end{pmatrix},
$$

which is the regular representation of $\mathbb{H}$ on $\mathbb{C}^{2}$: the four real parameters are those of $a+bi+cj+dk$, with $\alpha=a+bi$ and $\beta=c+di$. The determinant of such a matrix is $\lvert\alpha\rvert^{2}+\lvert\beta\rvert^{2}=a^{2}+b^{2}+c^{2}+d^{2}$, the Euclidean norm on $\mathbb{R}^{4}$, and it is the quaternionic norm.

**The two forms are not isomorphic as real algebras.** $M_2(\mathbb{R})$ has zero divisors, since $E_{12}^{2}=0$, while $\mathbb{H}$ is a division algebra, every nonzero quaternion being invertible. That single contrast separates the two forms without any further computation.

## The Determinant and the Spectrum

**The determinant of a real matrix is real, and the spectrum of a real matrix is stable under conjugation.**

**Proposition.** If $X\in M_2(\mathbb{R})$ then $\det X\in\mathbb{R}$ and $\chi_X$ has real coefficients; hence the eigenvalues of $X$ are either two real numbers or a conjugate pair.

**Proof.** The determinant is a polynomial with integer coefficients in the entries, so a real matrix has a real determinant. The same holds for every coefficient of $\chi_X$, so a nonreal root $\lambda$ is accompanied by $\bar\lambda$, which is also a root; the polynomial has degree two, so those are the two roots.

**Example.** The rotation $\begin{pmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{pmatrix}$ has trace $2\cos\theta$ and determinant $1$, and its eigenvalues are $e^{\pm i\theta}$, a conjugate pair on the unit circle. A real matrix of order two has a nonreal pair exactly when its discriminant $(\operatorname{tr}X)^{2}-4\det X$ is negative.

**The determinant is a quadratic form of inertia $(2,2)$ on the real algebra.** In the basis $(E_{11},E_{12},E_{21},E_{22})$ the determinant $ad-bc$ has the symmetric matrix of eigenvalues $\tfrac12,\tfrac12,-\tfrac12,-\tfrac12$. Its zero set is therefore a cone over a torus, and not the single point that a definite form would give.

## The Split Quaternions at Order Two

**The real algebra $M_2(\mathbb{R})$ is the split quaternion algebra.** Put

$$
e_1=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
e_2=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
e_3=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$

Then $e_1^{2}=e_2^{2}=I$, $e_3^{2}=-I$, $e_1e_2=e_3$, $e_2e_3=-e_1$, $e_3e_1=-e_2$, and the four elements $I,e_1,e_2,e_3$ are a real basis. The table is the quaternion table with two of the three squares equal to $+I$; that sign pattern is the definition of the split quaternions.

**Proposition.** Under this basis a matrix $X=aI+xe_1+ye_2+ze_3$ has $\operatorname{tr}X=2a$ and $\det X=a^{2}-x^{2}-y^{2}+z^{2}$.

**Proof.** Each generator is traceless, so $\operatorname{tr}X=2a$. On the entries, $X=\begin{pmatrix}a+x&y+z\\ y-z&a-x\end{pmatrix}$, and $(a+x)(a-x)-(y+z)(y-z)=a^{2}-x^{2}-y^{2}+z^{2}$.

**The correspondence with the biquaternion algebra.** The split quaternion algebra is the real algebra $\mathbb{B}^{\mathrm{spl}}$ whose norm is of inertia $(2,2)$; the biquaternion algebra $\mathbb{B}$ carries the algebraic norm $N$, the sum $Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ of four squares, read over $\mathbb{R}^{8}$ through the real and imaginary parts of the four coordinates. The two algebras are related by the change of the scalar field and not by an isomorphism over $\mathbb{R}$, and their tables differ in signs. The split algebra and its null quadric are *Split Quaternion Null Quadric and Projective Geometry*.

## Summary

$M_2(\mathbb{R})$ is the fixed algebra of the entrywise conjugation of $M_2(\mathbb{C})$, of real dimension $4$ against the real dimension $8$ of the complex algebra, and $\mathbb{C}\otimes_{\mathbb{R}}M_2(\mathbb{R})\cong M_2(\mathbb{C})$. Every matrix is $X+iY$ with $X,Y$ real and unique, and the product reads $AC=(XU-YV)+i(XV+YU)$. The rank is a condition on minors and survives the change of field, while the dimension doubles; the determinant restricted to the real matrices is a quadratic form of inertia $(2,2)$ with a cone as zero set.

The algebra has exactly two real forms, $M_2(\mathbb{R})$ and $\mathbb{H}$, distinguished by the sign $S\bar S=\pm I$ and by the presence of zero divisors. The real algebra is the split quaternion algebra, with generators of squares $I,I,-I$ and the norm $a^{2}-x^{2}-y^{2}+z^{2}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma(A)=\bar A$ | the entrywise conjugation |
| $M_2(\mathbb{R})$ | the fixed set of $\sigma$, the real matrices |
| $X,Y$ | the real and imaginary parts of $A=X+iY$ |
| $\operatorname{Re}\operatorname{tr}(AC)$ | the real part of the trace form, a real bilinear form |
| $S$ | a matrix with $\sigma(A)=S\bar AS^{-1}$ |
| $\mathbb{H}$ | the quaternion algebra, the second real form |
| $e_1,e_2,e_3$ | the split quaternion generators of $M_2(\mathbb{R})$ |
| $\chi_X$ | the characteristic polynomial of a real matrix |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the real and complex readings of one matrix and the reality of the spectrum.
- Tsit-Yuen Lam, *Introduction to Quadratic Forms over Fields* (AMS, 2005), for the quaternion algebra, its split twin and the norms.
- [The Matrix Algebra $M_2(\mathbb{C})$](the-matrix-algebra-m2c.html), for the product, the trace, the determinant and the rank of the complex algebra.
- [The Two Base Fields: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$](the-two-base-fields-mnr-inside-mnc.html), for the general order and the classification of the real structures.
- [Split Quaternion Null Quadric and Projective Geometry](split-quaternion-null-quadric-and-projective-geometry.html), for the null cone of the split algebra.
