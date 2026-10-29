# __Spectral Regularity and Degeneracy in the Split-Quaternion Algebra__

## Introduction

The split-quaternion algebra carries two quadratic conditions on one element. The first is the square of the vector part,

$$
S:=\vec v^2=-q_x^2+q_y^2+q_z^2,
$$

which involves no scalar term. The second is the split-quaternion norm $q\bar q=t^2-S$, which is multiplicative. This article studies the first condition: it defines left multiplication, proves the spectral polynomials, derives the eigenvalues $t\pm\sqrt S$, and separates the regular case $S\neq0$ from the degenerate cone $S=0$. On the cone, the scalar line is semisimple and its complement is defective with Jordan type $(2,2)$.

**Notation.** A general element is $q=t+\vec v$, with $t\in\mathbb R$ and $\vec v=q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$. The basis is $e_t=1,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_x^2=-e_t$, $\vec e_y^2=\vec e_z^2=+e_t$ and $\vec e_x\vec e_y=\vec e_z$. The conjugation is $\bar q=t-\vec v$, and the split-quaternion norm is

$$
q\bar q=t^2-S=t^2+q_x^2-q_y^2-q_z^2.
$$

The symbol $S$ denotes $\vec v^2$; the scalar subspace is $\mathbb R\cdot1$.

## Left Multiplication and the Spectral Polynomial

**Definition (left multiplication).** For $q\in\mathbb H_{\mathrm s}$, the **left multiplication** $L_q$ is the endomorphism of $\mathbb H_{\mathrm s}$ defined by $L_q(x)=qx$. It is $\mathbb R$-linear and injective, since $L_q(1)=q$.

**Proposition (the matrix).** On the basis $(1,\vec e_x,\vec e_y,\vec e_z)$, the matrix of $L_q$ is

$$
L(q)=\begin{pmatrix}
t&-q_x&q_y&q_z\\
q_x&t&q_z&-q_y\\
q_y&q_z&t&-q_x\\
q_z&-q_y&q_x&t
\end{pmatrix}.
$$

It has the block form

$$
L(q)=\begin{pmatrix}A&B\\B&A\end{pmatrix},\qquad
A=\begin{pmatrix}t&-q_x\\q_x&t\end{pmatrix},\qquad
B=\begin{pmatrix}q_y&q_z\\q_z&-q_y\end{pmatrix}.
$$

*Proof.* The columns are the products $q\cdot1$, $q\vec e_x$, $q\vec e_y$, $q\vec e_z$, read in the basis; the multiplication table gives the display. The block change $\frac1{\sqrt2}\begin{pmatrix}I&I\\I&-I\end{pmatrix}$ conjugates the matrix to $\operatorname{diag}(A+B,A-B)$.

**Theorem (the spectral polynomial).** Let $q=t+\vec v$.

1. The characteristic polynomial of $L_q$ is
$$
p_{L_q}(\lambda)=\big((\lambda-t)^2-S\big)^2.
$$
2. If $q$ is not scalar, the minimal polynomial of $L_q$ is
$$
m_q(\lambda)=(\lambda-t)^2-S.
$$
If $q=t$ is scalar, $m_q(\lambda)=\lambda-t$.
3. If $S=0$ and $\vec v\neq0$, then $L_q$ has the single eigenvalue $t$, an eigenspace of dimension $2$, minimal polynomial $(\lambda-t)^2$ and Jordan type $(2,2)$. If $q$ is scalar, $L_q=t\,\mathrm{id}$ and the Jordan type is $(1,1,1,1)$. If $S\neq0$, $L_q$ is semisimple with eigenvalues $t+\sqrt S$ and $t-\sqrt S$, each of multiplicity two.

*Proof.* Both $A+B$ and $A-B$ have trace $2t$ and determinant

$$
\det(A\pm B)=(t+q_y)(t-q_y)-(-q_x\pm q_z)(q_x\pm q_z)
=t^2+q_x^2-q_y^2-q_z^2=t^2-S.
$$

Hence each $2\times2$ block has characteristic polynomial $\lambda^2-2t\lambda+(t^2-S)=(\lambda-t)^2-S$, and the characteristic polynomial of the $4\times4$ matrix is the product of the two, that is the square in (1).

The minimal polynomial of a block diagonal matrix is the least common multiple of the minimal polynomials of its blocks. If $S\neq0$, the roots $t\pm\sqrt S$ are distinct, so each block has minimal polynomial $(\lambda-t)^2-S$, and the least common multiple is that polynomial. If $S=0$ and $\vec v\neq0$, then

$$
A+B=tI+\begin{pmatrix}q_y&-q_x+q_z\\q_x+q_z&-q_y\end{pmatrix},\qquad
A-B=tI+\begin{pmatrix}-q_y&-q_x-q_z\\q_x-q_z&q_y\end{pmatrix},
$$

and each square-zero matrix on the right is non-zero. A non-zero $2\times2$ nilpotent is a single Jordan block $J_2(0)$, so each block is $J_2(t)$ with minimal polynomial $(\lambda-t)^2$; the least common multiple is $(\lambda-t)^2$. If $\vec v=0$, both blocks are $tI$ and the minimal polynomial is $\lambda-t$.

For the Jordan type: at $S=0$, $\vec v\neq0$, $L_q=J_2(t)\oplus J_2(t)$ and the eigenspace has dimension $2$; at $S\neq0$ the direct sum is semisimple with each eigenvalue twice; at $\vec v=0$, $L_q=tI$.

**Corollary (Cayley–Hamilton and the inverse).** Every $q$ satisfies $q^2-2tq+(t^2-S)=0$; if $t^2-S\neq0$, then $q^{-1}=\bar q/(t^2-S)$.

*Proof.* Since $\vec v^2=S$, $q^2=t^2+2t\vec v+S=2tq-(t^2-S)$, and $q\bar q=\bar q q=t^2-S$.

**Definition and criterion (spectrum, regular and degenerate).** The **spectrum** is $\sigma(q)=\{t+\sqrt S,\ t-\sqrt S\}$. The element is **spectrally regular** when $S\neq0$ and **spectrally degenerate** when $S=0$. The regular case is equivalent to the distinctness of the two eigenvalues, to $4S\neq0$, and, for non-scalar $q$, to $p_q$ being the minimal polynomial and squarefree. For every non-scalar $q$ and every eigenvalue the eigenspace has dimension $2$ over $\mathbb C$; for the scalar, $\mathbb H_{\mathrm s}$. A non-scalar $q$ has an eigenbasis over $\mathbb C$ exactly when $S\neq0$.

*Proof.* The roots of $p_q$ are distinct exactly when $4S\neq0$. In the block decomposition each block contributes one eigenvector per eigenvalue, giving dimension $2$; at $S=0$ and $\vec v\neq0$ the geometric multiplicity $2$ is smaller than the algebraic multiplicity $4$, so no eigenbasis exists. If $S\neq0$ the minimal polynomial has distinct roots, so an eigenbasis exists.

## The Spectral Cone

**Definition (the spectral cone).** The **spectral cone** is

$$
\mathcal C=\{q\in\mathbb H_{\mathrm s}:S=0\}=\{q:-q_x^2+q_y^2+q_z^2=0\}.
$$

**Theorem (the cone is the discriminant locus).** For every $q$, $q\in\mathcal C$ exactly when the reduced polynomial $p_q=(\lambda-t)^2-S$ has a repeated root, that is, when the two eigenvalues coincide.

*Proof.* The discriminant of $p_q$ is $4S$. The characteristic polynomial is $p_q^2$, so the eigenvalues coincide exactly when $p_q$ has a repeated root, that is, when $S=0$.

**Theorem (the geometry of the cone).** Write $V=\operatorname{span}\{\vec e_x,\vec e_y,\vec e_z\}$ and

$$
N_V=\{\vec v\in V:\vec v^2=0\}=\{(q_x,q_y,q_z):q_x^2=q_y^2+q_z^2\}.
$$

Then $\mathcal C=\mathbb R\times N_V$. The cone has dimension $3$, is smooth off the scalar line and singular along it.

*Proof.* Since $S$ involves only $\vec v$, $t$ is free and $\mathcal C=\mathbb R\times N_V$. The gradient $(-2q_x,2q_y,2q_z)$ is non-zero off the origin, so $N_V$ has dimension $2$ and $\mathcal C$ has dimension $3$. The gradient of $S$ in four coordinates is $(0,-2q_x,2q_y,2q_z)$, which vanishes exactly along the scalar line.

**Proposition (what the cone is not).** The spectral cone is not a linear subspace, not the zero-divisor cone, not the set of non-units, and not the set of defective elements.

*Proof.* The elements $\vec e_x\pm\vec e_y$ lie on $\mathcal C$ while their sum $2\vec e_x$ does not, so $\mathcal C$ is not a subspace. The element $1+\vec e_y$ has norm $0$ and $S=1$; the element $1+\vec e_x+\vec e_y$ has norm $1$ and $S=0$; the scalar line lies on $\mathcal C$ and is semisimple. These witnesses separate $\mathcal C$ from the zero-divisor cone, from the non-units and from the defective set.

## The Defective Stratum

**Definition (the defective stratum).** The **defective stratum** of the spectral cone is

$$
\mathcal D=\mathcal C\setminus\{q:\vec v=0\}=\{q:S=0,\ \vec v\neq0\}.
$$

**Theorem (the normal form on the defect).** Let $q=t+\vec v$ with $S=0$ and $\vec v\neq0$. Then $\vec v^2=0$ and $\vec v\neq0$, and $L_q$ has minimal polynomial $(\lambda-t)^2$, characteristic polynomial $(\lambda-t)^4$, eigenspace $\ker L_{\vec v}$ of dimension $2$, and Jordan type $(2,2)$. No eigenbasis exists.

*Proof.* The spectral polynomial theorem gives the polynomials and Jordan type; the eigenspace is $\ker(L_q-t\,\mathrm{id})=\ker L_{\vec v}$, of dimension $2$. Since $2<4$, no eigenbasis exists.

**Corollary (the cone is the scalar line plus the defect).** The spectral cone is the disjoint union of the scalar line $\{\vec v=0\}$ and $\mathcal D$. On the scalar line $L_q=t\,\mathrm{id}$ is semisimple with minimal polynomial $\lambda-t$; on $\mathcal D$ the element is defective. Spectral degeneracy is therefore not defect: the scalar line is degenerate and semisimple.

## The Matrix Model and the Singular Locus

**Theorem (the matrix model).** The assignment

$$
\varphi(q)=\begin{pmatrix}t+q_y&q_x-q_z\\-(q_x+q_z)&t-q_y\end{pmatrix}
$$

is an isomorphism of $\mathbb H_{\mathrm s}$ onto $M_2(\mathbb R)$. It satisfies

$$
\det\varphi(q)=t^2+q_x^2-q_y^2-q_z^2=t^2-S,\qquad
\operatorname{tr}\varphi(q)=2t,
$$

and the characteristic polynomial of $\varphi(q)$ is $(\lambda-t)^2-S$.

*Proof.* On the generators,

$$
\varphi(\vec e_x)=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
\varphi(\vec e_y)=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
\varphi(\vec e_z)=\begin{pmatrix}0&-1\\-1&0\end{pmatrix},
$$

and these satisfy the defining relations. The four images are linearly independent, so $\varphi$ is injective between four-dimensional algebras, hence an isomorphism. The determinant, trace and characteristic polynomial are direct computations.

**Theorem (two different loci).** In the matrix model the singular (non-invertible) locus $\{\det=0\}$ is the zero-divisor cone $\mathcal Z=\{t^2=S\}$. The discriminant locus, where the two eigenvalues coincide, is the spectral cone $\mathcal C=\{S=0\}$. The two loci are different, and their intersection is the set $\{t=0,S=0\}$.

*Proof.* The determinant $t^2-S$ vanishes exactly on $\mathcal Z$. The reduced characteristic polynomial $(\lambda-t)^2-S$ has discriminant $4S$, so its roots coincide exactly when $S=0$. Both conditions give $t^2=S=0$, hence $t=0$.

## Contrast with the Quaternion and Biquaternion Cases

In each of the three algebras the reduced characteristic polynomial has the form

$$
(\lambda-t)^2-\vec v^2,
$$

the eigenvalues are $t\pm\sqrt{\vec v^2}$, and the spectral condition is $\vec v^2=0$. What changes is the signature of the form $\vec v^2$ on the vector subspace.

| algebra | $\vec v^2$ | spectral condition | eigenvalues | defective stratum | norm | norm cone |
|---|---|---|---|---|---|---|
| $\mathbb H$ | $-\lvert\vec v\rvert^2$, negative definite | $\vec v=0$ | $t\pm i\lvert\vec v\rvert$ | none | $t^2+\lvert\vec v\rvert^2$ | $\{0\}$ |
| $\mathbb B$ | $-B^2$, complex nondegenerate | $B^2=0$ | $t\pm iB$ | $B^2=0,\ \vec v\neq0$ | $t^2+B^2$ | $t^2+B^2=0$ |
| $\mathbb H_{\mathrm s}$ | $S$, real of signature $(2,1)$ | $S=0$ | $t\pm\sqrt S$ | $S=0,\ \vec v\neq0$ | $t^2-S$ | $t^2=S$ |

The quaternion form is negative definite, so its spectral cone is the centre, every element is semisimple and there is no defective stratum; its norm is positive definite. The biquaternion form is complex nondegenerate, so its spectral cone is a complex cone containing the centre, with a defective part off the centre; its norm is a second complex cone. The split form is real of signature $(2,1)$, so its spectral cone is a real cone containing the scalar line, with a defective part off it; its norm is a second real cone. The split case is the only one in which both cones are real hypersurfaces and neither is the centre.

## Summary

The split-quaternion algebra carries the condition $S=\vec v^2=-q_x^2+q_y^2+q_z^2$. Left multiplication by $q=t+\vec v$ has characteristic polynomial $((\lambda-t)^2-S)^2$ and, for non-scalar $q$, minimal polynomial $(\lambda-t)^2-S$; the eigenvalues are $t\pm\sqrt S$, real for $S>0$, conjugate for $S<0$, and coincident at $t$ for $S=0$. The spectral criterion is $S\neq0$: the eigenvalues are distinct, $L_q$ is semisimple and an eigenbasis exists. The degenerate case is the spectral cone $\{S=0\}=\mathbb R\times\{q_x^2=q_y^2+q_z^2\}$, of dimension $3$, smooth off the scalar line and singular along it. The scalar line is semisimple; off it the element is defective with minimal polynomial $(\lambda-t)^2$, eigenspace of dimension $2$ and Jordan type $(2,2)$.

The matrix model $\mathbb H_{\mathrm s}\cong M_2(\mathbb R)$ has determinant $t^2-S$ and trace $2t$; its singular (non-invertible) locus is the zero-divisor cone $t^2=S$, while its discriminant locus is the spectral cone $S=0$. The two loci differ: a unit can have a repeated eigenvalue and a zero divisor can have distinct eigenvalues. The comparison is *Relations between the Split-Quaternion Norm and Spectral Regularity and Degeneracy*; the four combinations are *The Four Sectors of the Split-Quaternion Algebra*. The quaternion, biquaternion and split cases differ by the signature of $\vec v^2$: negative definite, complex nondegenerate, and real of signature $(2,1)$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb H_{\mathrm s}$ | the split-quaternion algebra |
| $q=t+\vec v$ | a general element |
| $\vec v=q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ | the vector part |
| $S=\vec v^2=-q_x^2+q_y^2+q_z^2$ | the square of the vector part, the spectral discriminant up to $4$ |
| $\bar q=t-\vec v$ | the conjugation |
| $q\bar q=t^2-S$ | the split-quaternion norm |
| $L_q(x)=qx$ | left multiplication |
| $p_q(\lambda)=(\lambda-t)^2-S$ | the reduced characteristic polynomial |
| $\sigma(q)=\{t\pm\sqrt S\}$ | the spectrum |
| $\mathcal C=\{S=0\}$ | the spectral cone |
| $\mathcal D=\mathcal C\setminus\{\vec v=0\}$ | the defective stratum |
| $\mathcal Z=\{t^2=S\}$ | the zero-divisor cone |
| $N_V=\{q_x^2=q_y^2+q_z^2\}$ | the vector null cone, with $\mathcal C=\mathbb R\times N_V$ |
| $\varphi(q)$ | the isomorphism $\mathbb H_{\mathrm s}\to M_2(\mathbb R)$ |

## Further Reading

- [Split-Quaternion Algebra](split-quaternion-algebra.html), for the algebra, its multiplication table, its conjugations and its idempotents.
- [Split-Quaternion Norm and Invertibility](split-quaternion-norm-and-invertibility.html), for the norm $q\bar q=t^2-S$, its isotropy and the invertibility criterion.
- [Split-Quaternion Zero Divisors](split-quaternion-zero-divisors.html), for the zero-divisor cone, its two families of minimal ideals and the non-zero nilpotents.
- [Split-Quaternion Spectral Theory](split-quaternion-spectral-theory.html), for the spectrum, the left and right eigenvalue problems and the resolvent.
- [Relations between the Split-Quaternion Norm and Spectral Regularity and Degeneracy](relations-between-the-split-quaternion-norm-and-spectral-regularity-and-degeneracy.html), for the comparison of the two cones and the chain of invariants.
- [The Four Sectors of the Split-Quaternion Algebra](the-four-sectors-of-the-split-quaternion-algebra.html), for the partition, the descriptions and the table of dimensions.
- [The Spectrum](the-spectrum.html), for the complex analogue.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (2nd edition, Cambridge University Press, 2013), for the characteristic polynomial, diagonalisability and the Jordan form.
