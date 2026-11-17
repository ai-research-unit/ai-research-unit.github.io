# __The Element: Rank, Trace, Determinant, Characteristic Polynomial at $n=2$__

## Introduction

**An element of $M_2(\mathbb{C})$ is four complex numbers, and its whole invariant theory is carried by the trace, the determinant and the rank.**

The article treats one element at a time: the coordinates in the two readings, the split into a scalar and a traceless part, the three possible ranks, the characteristic polynomial and its discriminant, the pair of invariants $(\operatorname{tr},\det)$ that classifies the conjugacy classes, and the Cayley–Hamilton identity with the adjugate it produces. It assumes *The Matrix Algebra $M_2(\mathbb{C})$* for the product and the matrix units. It defers the symmetric functions of the two eigenvalues to *The Elementary Symmetric Functions: $\operatorname{tr}$ and $\det$ in Dimension Two*, the two Jordan regimes to *The Minimal Polynomial and the Two Jordan Regimes of $M_2(\mathbb{C})$*, and the spectral classification itself to *The Spectrum of a $2\times2$ Matrix*.

What the dimension adds is arithmetic. At order two the scalar part is one half of the trace, the traceless part has the single relation $A_0^{2}=-\det(A_0)I$, and the discriminant is minus four times the determinant of the traceless part.

## The Coordinates

**Definition.** Write an element in the matrix units,

$$
A=\begin{pmatrix}a&b\\c&d\end{pmatrix}=aE_{11}+bE_{12}+cE_{21}+dE_{22},
\qquad a,b,c,d\in\mathbb{C}.
$$

The four numbers $a,b,c,d$ are the **complex coordinates** of $A$; the eight numbers $\operatorname{Re}a,\operatorname{Im}a,\dots,\operatorname{Im}d$ are its **real coordinates**. The element is a linear map $\mathbb{C}^{2}\to\mathbb{C}^{2}$, and it is also a bilinear form $(x,y)\mapsto x^{\mathsf T}Ay$ on $\mathbb{C}^{2}$.

**Proposition.** The three readings carry the same eight real coordinates and differ only in which structure is emphasised; the passage from the map to the form is the identity on the array, and the passage to the transpose is the exchange of the two slots of the form.

**Proof.** The map is fixed by its four entries, since $Ae_{j}$ is the $j$-th column; the form is fixed by its four values on the standard basis, which are the same entries; and $x^{\mathsf T}Ay=y^{\mathsf T}A^{\mathsf T}x$.

**Two entries decide the symmetry.** The element is symmetric exactly when $b=c$ and Hermitian exactly when $c=\bar b$ with $a,d$ real. The eight real coordinates are therefore distributed as $4$ for a Hermitian element and $4$ for the real matrices, and the two conditions are independent, which is why the Hermitian and the real readings of the algebra are different readings and not the same one.

## The Scalar and Traceless Parts

**Definition.** The **scalar part** of $A$ is $\tfrac12(\operatorname{tr}A)I$ and the **traceless part** is

$$
A_{0}=A-\tfrac12(\operatorname{tr}A)I .
$$

**Proposition.** The two parts commute, $A_{0}$ is traceless, the split $A=\tfrac12(\operatorname{tr}A)I+A_{0}$ is unique, and the space of traceless elements is three-dimensional over $\mathbb{C}$.

**Proof.** The scalar part is central, so it commutes with everything. The trace of $A_{0}$ is $\operatorname{tr}A-\tfrac12(\operatorname{tr}A)\operatorname{tr}I=\operatorname{tr}A-\operatorname{tr}A=0$. If $A=\lambda I+N$ with $N$ traceless then taking traces gives $2\lambda=\operatorname{tr}A$. The traceless elements are the kernel of the trace on a four-dimensional space.

**Theorem (the traceless square is a scalar).** Every traceless element $N$ of $M_2(\mathbb{C})$ satisfies

$$
N^{2}=-\det(N)\,I .
$$

**Proof.** Write $N=\begin{pmatrix}p&q\\ r&-p\end{pmatrix}$, which is the general traceless array. Then $N^{2}=(p^{2}+qr)I$ and $\det N=-p^{2}-qr$, so $N^{2}=-\det(N)I$. Both sides are polynomials in the entries, and every traceless element is of that form.

**Corollary (the discriminant).** For any $A$,

$$
A_{0}^{2}=\tfrac14\bigl((\operatorname{tr}A)^{2}-4\det A\bigr)I ,
$$

so the discriminant of the characteristic polynomial is $-4\det(A_{0})$.

**Proof.** By Cayley–Hamilton for $A$, $\det A=\tfrac14\bigl((\operatorname{tr}A)^{2}-\operatorname{tr}(A^{2})\bigr)$; substituting $A=\tfrac12(\operatorname{tr}A)I+A_{0}$ and using $A_{0}^{2}=-\det(A_{0})I$ gives the identity.

**Example.** For $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ the scalar part is $\tfrac52I$ and $A_{0}=\begin{pmatrix}-\tfrac32&2\\ 3&\tfrac32\end{pmatrix}$, with $\det A_{0}=-\tfrac{33}{4}$ and $A_{0}^{2}=\tfrac{33}{4}I$. The discriminant of $\chi_A=\lambda^{2}-5\lambda-2$ is $25+8=33$, which is $-4\det A_{0}$.

## The Rank

**The rank is the dimension of the image, and at order two it takes three values.** By rank–nullity,

$$
\mathrm{rank}\,A=2-\dim\ker A ,
$$

so the rank is $2$ for an invertible element, $1$ for an element whose kernel is a line, and $0$ only for $A=0$.

**Proposition.** The rank is $2$ exactly when $\det A\neq0$. The rank is $1$ exactly when $\det A=0$ and $A\neq0$.

**Proof.** The determinant is nonzero exactly when the two columns are independent, that is exactly when the image is the whole plane. If the determinant vanishes and $A\neq0$, at least one column is nonzero, so the image is the line it spans.

**Proposition (the rank-one form).** Every rank-one element is $uv^{\mathsf T}$ with $u,v\in\mathbb{C}^{2}$ nonzero, its image is the line $\mathbb{C}u$, its kernel is the line $\{v\}^{\perp}=\{x:v^{\mathsf T}x=0\}$, and its trace is $v^{\mathsf T}u$.

**Proof.** The image of $x\mapsto uv^{\mathsf T}x=u(v^{\mathsf T}x)$ is contained in $\mathbb{C}u$ and equals it because $v^{\mathsf T}x\neq0$ for some $x$; the kernel is the orthogonal complement of $v$ for the standard bilinear form, a line because $v\neq0$. The trace of $uv^{\mathsf T}$ is $\sum_{i}u_{i}v_{i}=v^{\mathsf T}u$.

**Corollary (rank one is a square-zero condition away from the trace).** A rank-one element is nilpotent exactly when $v^{\mathsf T}u=0$, that is exactly when its trace vanishes. The nilpotent rank-one elements are therefore the nonzero traceless elements of rank one, and they form the cone $\{A\neq0,\operatorname{tr}A=0,\det A=0\}$.

## The Characteristic Polynomial

**Definition.** The characteristic polynomial is $\chi_A(\lambda)=\lambda^{2}-(\operatorname{tr}A)\lambda+\det A$. Its **discriminant** is $\Delta=(\operatorname{tr}A)^{2}-4\det A$, and its roots are

$$
\lambda_{\pm}=\tfrac12\Bigl(\operatorname{tr}A\pm\sqrt{\Delta}\Bigr).
$$

**Proposition.** The roots of $\chi_A$ are the eigenvalues of $A$, the sum of the roots is $\operatorname{tr}A$ and their product is $\det A$; the roots coincide exactly when $\Delta=0$.

**Proof.** An eigenvalue is a root of $\chi_A$ by definition of the determinant of $\lambda I-A$; the two statements about the roots are the Vieta formulas for a monic quadratic. A double root is exactly a vanishing discriminant.

**The discriminant is a quadratic form in the entries, and it is not the determinant.** For $A=\begin{pmatrix}a&b\\ c&d\end{pmatrix}$,

$$
\Delta=(a-d)^{2}+4bc ,
$$

which is indefinite over the reals and vanishes on a cone of real dimension $3$. The vanishing of $\Delta$ is the condition that the two eigenvalues merge; the vanishing of $\det A$ is the condition that one of them vanishes. The two conditions meet only at the nilpotent cone.

**The spectrum is read from the pair $(\operatorname{tr},\det)$.** The map $A\mapsto(\operatorname{tr}A,\det A)$ is polynomial, of degree one and two, and it is invariant under conjugation. It is not injective: its fibres are three-dimensional, and the fibre over a generic pair is a single conjugacy class. The classification is completed in *The Spectrum of a $2\times2$ Matrix*.

## The Trace and the Determinant as Invariants

**Theorem (the classification).** Two elements of $M_2(\mathbb{C})$ with the same trace, the same determinant and the same discriminant are conjugate, except for the scalar multiples of the identity and the nonzero nilpotents, which are separated by the rank.

**Proof.** If $\Delta\neq0$ the two eigenvalues are distinct, both elements are diagonalisable with the same two eigenvalues, and a change of basis matches the two eigenlines. If $\Delta=0$ and the element is not scalar, the single eigenvalue is $\tfrac12\operatorname{tr}A$ and the element is $\lambda I+N$ with $N\neq0$ nilpotent; two such elements are conjugate by a change of basis sending one nonzero nilpotent to the other, since every nonzero nilpotent of order two has rank one and the same Jordan form.

**Corollary (the two scalar invariants and the two exceptional strata).** The conjugation orbits of $M_2(\mathbb{C})$ are: the single point $0$; the family $\{\lambda I\}$ of scalars, one orbit for each $\lambda$; the cone $\{N\neq0,\ N^{2}=0\}$ of nonzero nilpotents, which is one orbit; and the generic stratum $\{\Delta\neq0\}$, on which $(\operatorname{tr},\det)$ is a complete invariant.

**The trace is additive and the determinant is multiplicative.** For $A,C$ arbitrary, $\operatorname{tr}(A+C)=\operatorname{tr}A+\operatorname{tr}C$ and $\det(AC)=\det A\det C$; the determinant is not additive, and the trace is not multiplicative. The pair is the pair of elementary symmetric functions of the eigenvalues, and the identities that relate the two are *The Elementary Symmetric Functions: $\operatorname{tr}$ and $\det$ in Dimension Two*.

## Cayley–Hamilton and the Adjugate

**Theorem.** Every $A$ satisfies $A^{2}-(\operatorname{tr}A)A+(\det A)I=0$.

**Proof.** On the general array, the identity has entries $a^{2}+bc-(a+d)a+ad=0$, $ab+bd-(a+d)b=0$, $ca+dc-(a+d)c=0$ and $cb+d^{2}-(a+d)d+ad=0$; all four vanish identically.

**Corollary (the adjugate).** The adjugate of $A$ is $\operatorname{adj}A=(\operatorname{tr}A)I-A$, and $A\operatorname{adj}A=(\det A)I$. For $\det A\neq0$,

$$
A^{-1}=\frac{1}{\det A}\bigl((\operatorname{tr}A)I-A\bigr).
$$

**Proof.** The Cayley–Hamilton identity rearranges to $A\bigl((\operatorname{tr}A)I-A\bigr)=(\det A)I$; the adjugate is characterised by $A\operatorname{adj}A=(\det A)I$, and it is unique when $\det A\neq0$.

**The adjugate at rank one.** If $\mathrm{rank}\,A=1$ then $\det A=0$, so $\operatorname{adj}A=(\operatorname{tr}A)I-A$, of rank at most one, and $A\operatorname{adj}A=0$; the adjugate spans the same line as $A$ exactly when $\operatorname{tr}A\neq0$. At rank zero the adjugate vanishes.

## The Real Element and the Biquaternion Coordinates

**A real element is an element fixed by the entrywise conjugation, and a biquaternion is four complex coordinates.** The matrix $A$ is real exactly when $b,c$ are real together with $a,d$; in the Pauli model of *$M_2(\mathbb{C})$ Pauli Representation* the same element is

$$
A=Q_tI-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3),
$$

with $Q_t=\tfrac12\operatorname{tr}A$ and the three other coordinates read off the traceless part.

**Proposition.** In these coordinates $\det A=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ and the scalar-free part satisfies $A_{0}^{2}=-(Q_x^{2}+Q_y^{2}+Q_z^{2})I$.

**Proof.** The determinant is the algebraic norm $N$ of the biquaternion, and the traceless part is $-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$, whose square is $-(Q_x^{2}+Q_y^{2}+Q_z^{2})I$ because the three Pauli matrices anticommute and each squares to $I$.

**Corollary.** The element is singular exactly when $Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}=0$, which over the complex coordinates is a cone and over the real coordinates is the single point $Q=0$.

## Summary

An element of $M_2(\mathbb{C})$ has four complex coordinates and eight real ones, and reads as a map, as a bilinear form and as a biquaternion. It splits uniquely as $\tfrac12(\operatorname{tr}A)I+A_{0}$ with $A_{0}$ traceless, and at order two the traceless part obeys the single relation $A_{0}^{2}=-\det(A_{0})I$, so that $A_{0}^{2}=\tfrac14\Delta I$ with $\Delta=(\operatorname{tr}A)^{2}-4\det A$ the discriminant. The rank takes the values $0,1,2$, the rank-one elements are $uv^{\mathsf T}$ with trace $v^{\mathsf T}u$, and the nilpotent ones among them are exactly those of trace zero.

The characteristic polynomial is $\lambda^{2}-(\operatorname{tr}A)\lambda+\det A$ with roots $\tfrac12(\operatorname{tr}\pm\sqrt{\Delta})$. Cayley–Hamilton gives $A^{2}-(\operatorname{tr}A)A+(\det A)I=0$ and the adjugate $\operatorname{adj}A=(\operatorname{tr}A)I-A$. The pair $(\operatorname{tr},\det)$ classifies the conjugacy classes on the generic stratum; the scalars and the nonzero nilpotents are the two exceptional families.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $a,b,c,d$ | the four complex coordinates of $A$ |
| $\operatorname{tr}A=a+d$ | the trace |
| $\det A=ad-bc$ | the determinant of the image |
| $\chi_A$ | the characteristic polynomial |
| $\Delta$ | the discriminant $(\operatorname{tr}A)^{2}-4\det A$ |
| $\lambda_{\pm}$ | the two roots of $\chi_A$ |
| $A_{0}$ | the traceless part $A-\tfrac12(\operatorname{tr}A)I$ |
| $\mathrm{rank}\,A$ | the dimension of the image, $2-\dim\ker A$ |
| $\operatorname{adj}A$ | the adjugate, equal to $(\operatorname{tr}A)I-A$ |
| $Q_t,Q_x,Q_y,Q_z$ | the biquaternion coordinates, $Q_t=\tfrac12\operatorname{tr}A$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the characteristic polynomial, the adjugate and the rank at order two.
- F. R. Gantmacher, *The Theory of Matrices* (Chelsea, 1959), for the Jordan form and the classification of conjugacy classes.
- [The Matrix Algebra $M_2(\mathbb{C})$](the-matrix-algebra-m2c.html), for the product, the trace and the determinant of the algebra.
- [The Two Base Fields: $M_2(\mathbb{R})$ inside $M_2(\mathbb{C})$](the-two-base-fields-m2r-inside-m2c.html), for the real elements and the reality of the spectrum.
- [$M_2(\mathbb{C})$ Pauli Representation](m2c-pauli-representation.html), for the biquaternion coordinates of an element.
