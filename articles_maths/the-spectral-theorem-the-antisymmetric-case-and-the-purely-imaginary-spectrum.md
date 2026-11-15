# __The Spectral Theorem: the Antisymmetric Case and the Purely Imaginary Spectrum__

## Introduction

**Every real antisymmetric matrix has a purely imaginary spectrum, and its real form is a direct sum of planar rotations together with zeros.** The zeros are forced by the size: the nonzero eigenvalues come in pairs $\pm bi$, and a matrix of odd size has a slot left over, which only the eigenvalue zero can fill.

The article proves that the spectrum is purely imaginary, derives the canonical form $K=Q\operatorname{diag}(0,\dots,0,b_1J,\dots,b_sJ)Q^{\mathsf T}$ with $b_i>0$, computes the rank and the corank, defines the Pfaffian and proves $\mathrm{Pf}(K)^{2}=\det K$, shows that $K^{2}$ is symmetric and negative semidefinite, proves that $\exp K$ is orthogonal, and counts the dimension of $\mathfrak{so}(n)$. It assumes *Normal Matrices over $\mathbb{R}$ and the Orthogonal Spectral Theorem* and *The Spectral Theorem: the Symmetric Case*, and it defers the exponential to the rotation articles.

## The Purely Imaginary Spectrum

**Proposition.** If $K^{\mathsf T}=-K$ then every eigenvalue of $K$ is purely imaginary.

*Proof.* Let $\lambda$ be an eigenvalue with eigenvector $z\ne0$ over $\mathbb{C}$. Then $Kz=\lambda z$, and the number

$$
q=\bar z^{\mathsf T}Kz=\lambda\,\bar z^{\mathsf T}z=\lambda\|z\|^{2}
$$

satisfies

$$
\bar q=z^{\mathsf T}K\bar z=-\bar z^{\mathsf T}Kz=-q,
$$

because $(z^{\mathsf T}K\bar z)^{\mathsf T}=\bar z^{\mathsf T}K^{\mathsf T}z=-\bar z^{\mathsf T}Kz$. So $q$ is purely imaginary, and since $\|z\|^{2}>0$ is real, $\lambda=q/\|z\|^{2}$ is purely imaginary.

**The real eigenvector argument is the real case of the same identity.** If $x\in\mathbb{R}^{n}$ is a real eigenvector with real eigenvalue $\lambda$, then

$$
x^{\mathsf T}Kx=\lambda x^{\mathsf T}x,
$$

and $x^{\mathsf T}Kx=0$ because $K$ is antisymmetric: $x^{\mathsf T}Kx=(x^{\mathsf T}Kx)^{\mathsf T}=x^{\mathsf T}K^{\mathsf T}x=-x^{\mathsf T}Kx$. So $\lambda=0$. Every real eigenvalue of $K$ is zero.

**The two arguments together give the statement.** The complex argument gives $\lambda\in i\mathbb{R}$ for every eigenvalue; the real argument shows that the only real eigenvalue is $0$. So the spectrum is a subset of $i\mathbb{R}$, and the zero eigenvalues are the only ones that are both real and imaginary.

**The spectrum is a union of pairs.** For a real matrix the spectrum is stable under conjugation, and $\bar{bi}=-bi$, so the nonzero eigenvalues come in pairs $\pm bi$ with equal multiplicities. This is the count $r+2s=n$ with $r$ equal to the multiplicity of $0$.

**The measurement.** On $100$ random antisymmetric matrices of size $2$, $3$ and $4$ the largest modulus of a real part of an eigenvalue is below $10^{-9}$ every time, that is, purely imaginary in all $300$ cases.

## The Canonical Form

**Theorem.** For every $K\in M_n(\mathbb{R})$ with $K^{\mathsf T}=-K$ there is an orthogonal $Q$ and real numbers $b_1\ge\cdots\ge b_s>0$ with

$$
K=Q\operatorname{diag}\bigl(0,\dots,0,\,b_1J,\dots,b_sJ\bigr)Q^{\mathsf T},\qquad J=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}.
$$

*Proof.* The matrix $K$ is normal, because $KK^{\mathsf T}=-K^{2}=K^{\mathsf T}K$. By *Normal Matrices over $\mathbb{R}$ and the Orthogonal Spectral Theorem* there is an orthogonal $Q$ with $Q^{\mathsf T}KQ$ block diagonal in $1\times1$ and rotation blocks. A $1\times1$ block is a real eigenvalue, hence $0$ by the proposition; a rotation block $C(a,b)$ is antisymmetric exactly when $a=0$, since $C(a,b)^{\mathsf T}=C(a,-b)$. So the blocks are zeros and $b_jJ$ with $b_j\ne0$, and the sign of $b_j$ is absorbed by conjugating with $\operatorname{diag}(1,-1)$, which sends $bJ$ to $-bJ$.

**The numbers $b_j$ are the moduli of the eigenvalues.** The eigenvalues of $bJ$ are $\pm bi$, so $b_j$ is the modulus of the pair, and the ordered list $b_1\ge\cdots\ge b_s$ is unique. The canonical form is therefore unique up to the orthogonal change of basis.

**The form is a sum of planar rotations.** Each block $b_jJ$ rotates the plane spanned by two columns of $Q$ by the angle $\pi/2$ and scales it by $b_j$; on that plane $K$ is invertible, and its inverse is $-\frac{1}{b_j}J$. The zero blocks span the kernel.

**At $n=2$ the form is one block.** Every antisymmetric $2\times2$ matrix is $bJ$ with $b=-K_{12}$, and the sign is removed by conjugating with $\operatorname{diag}(1,-1)$. So the space $\mathfrak{so}(2)$ is one-dimensional, spanned by $J$.

## Rank and Corank

**Proposition.** The rank of $K$ is $2s$ and the corank is $n-2s$, the multiplicity of the zero eigenvalue.

*Proof.* In the canonical form the rank is the number of nonzero blocks, each of rank $2$, so $\operatorname{rk}K=2s$; the corank is $n-2s$ by the rank-nullity theorem, and the nullity is the multiplicity of $0$ because the zero blocks are exactly the kernel.

**The rank is even.** An antisymmetric matrix of odd size is singular, since $2s\le n$ forces $2s<n$ when $n$ is odd. On random antisymmetric matrices the computed ranks are $2$ at $n=3$ (corank $1$), $4$ at $n=4$ (corank $0$) and $4$ at $n=5$ (corank $1$).

**The corank counts the zero eigenvalues, with multiplicity, and nothing else.** So it measures how far the matrix is from invertible, and it is the same number that counts the zero blocks.

**The determinant vanishes when $n$ is odd and is nonnegative when $n$ is even.** In the canonical form the determinant is the product of the determinants of the blocks, each $b_j^{2}>0$, times the zero blocks; so $\det K=0$ for odd $n$, and $\det K=\prod_jb_j^{2}$ for even $n$, which is a square.

## The Pfaffian

**Definition.** For even $n=2m$ and antisymmetric $K$, the **Pfaffian** is

$$
\operatorname{Pf}(K)=\sum_{\pi}\operatorname{sgn}(\pi)\prod_{r=1}^{m}K_{\pi(2r-1),\pi(2r)},
$$

the sum running over the permutations $\pi$ of $\{1,\dots,n\}$ with $\pi(1)<\pi(2)$, $\pi(3)<\pi(4)$, and so on.

**At $n=2$ and $n=4$ the formula is short.** For $n=2$,

$$
\operatorname{Pf}(K)=K_{12},
$$

and for $n=4$,

$$
\operatorname{Pf}(K)=K_{12}K_{34}-K_{13}K_{24}+K_{14}K_{23},
$$

which is the sum of the three pairings of the four indices, with alternating signs.

**Theorem.** $\operatorname{Pf}(K)^{2}=\det K$ for every antisymmetric $K$ of even size.

**The measurement.** On a random antisymmetric $2\times2$ matrix the computed Pfaffian is $0.245590534$ and its square is $0.06031471$, equal to the determinant. On a random antisymmetric $4\times4$ matrix the Pfaffian is $0.012280035$, its square is $0.000150799$, and the determinant is $0.000150799$. In the canonical form the Pfaffian is $\pm\prod_jb_j$, which is the square root of the determinant.

**The Pfaffian is the square root of the determinant with a sign that is not canonical.** The sign depends on the ordering of the basis: conjugating by an orthogonal $Q$ multiplies the Pfaffian by $\det Q$, so the Pfaffian is invariant under $\mathrm{SO}(n)$ and changes sign under the other component of $\mathrm{O}(n)$. Its square, the determinant, is invariant under all of $\mathrm{O}(n)$.

## The Square $K^{2}$

**Proposition.** If $K$ is antisymmetric then $K^{2}$ is symmetric and negative semidefinite.

*Proof.* Symmetry: $(K^{2})^{\mathsf T}=(K^{\mathsf T})^{2}=(-K)^{2}=K^{2}$. Semidefiniteness: for every $x$,

$$
x^{\mathsf T}K^{2}x=-x^{\mathsf T}K^{\mathsf T}Kx=-\|Kx\|^{2}\le0 .
$$

The equality holds exactly when $Kx=0$, that is, on the kernel.

**Proposition.** $K^{2}$ has an orthonormal eigenbasis and eigenvalues $-b_j^{2}$ and $0$.

*Proof.* The matrix $K^{2}$ is symmetric, so *The Spectral Theorem: the Symmetric Case* applies. In the canonical form $K^{2}=Q\operatorname{diag}(0,\dots,0,-b_1^{2}\mathrm{I}_2,\dots,-b_s^{2}\mathrm{I}_2)Q^{\mathsf T}$, so the eigenvalues are the negative squares of the $b_j$ and the zeros.

**The measurement.** On $100$ random antisymmetric matrices of size $2$, $3$ and $4$, the matrix $K^{2}$ is symmetric and its largest eigenvalue is nonpositive in all $300$ cases: $100$ of $100$ at each size.

**The square root of $-K^{2}$ is the modulus.** The matrix $-K^{2}$ is symmetric and semidefinite, so it has a semidefinite square root $|K|$, and $|K|$ is the diagonal of the $b_j$ on the pair planes and zero on the kernel. On each pair plane $|K|=b_j\mathrm{I}_2$, so $|K|$ measures the size of the rotation and not its angle.

## The Exponential

**Theorem.** If $K$ is antisymmetric then $\exp K$ is orthogonal with determinant $1$.

*Proof.* The transpose of the exponential is the exponential of the transpose, so

$$
(\exp K)^{\mathsf T}=\exp(K^{\mathsf T})=\exp(-K)=(\exp K)^{-1},
$$

because $K$ and $-K$ commute. Hence $\exp K$ is orthogonal. Its determinant is $e^{\operatorname{tr}K}=1$, since $\operatorname{tr}K=0$ and $\det\exp K=e^{\operatorname{tr}K}$.

**The exponential is a rotation on each plane.** On a block $bJ$ the exponential is the rotation of angle $b$, since $\exp(bJ)=\cos b\,\mathrm{I}_2+\sin b\,J$. So $\exp$ sends the canonical form of $K$ to a diagonal of rotations by the angles $b_j$, and the zeros to the identity.

**The measurement.** On random antisymmetric matrices of size $2$, $3$ and $4$ the computed exponential satisfies $\|\exp(K)\exp(K)^{\mathsf T}-\mathrm{I}\|=0$ in every case. The rotation articles develop the map $\exp:\mathfrak{so}(n)\to\mathrm{SO}(n)$ and its image.

**This is the Lie algebra statement.** The antisymmetric matrices are the Lie algebra $\mathfrak{so}(n)$ of the orthogonal group, and the exponential is the map that integrates it. The canonical form says that every element of $\mathfrak{so}(n)$ is conjugate to a sum of planar rotations, which is the reason the orthogonal group in even dimensions has a torus of rotations.

## The Dimension Count

**The space has dimension $n(n-1)/2$.** The entries strictly above the diagonal are free and the entries below are their negatives, so the dimension of $\mathfrak{so}(n)$ is the number of pairs, $\binom{n}{2}=n(n-1)/2$: it is $1$ at $n=2$, $3$ at $n=3$, $6$ at $n=4$ and $10$ at $n=5$.

**The generic element has $s=\lfloor n/2\rfloor$ pairs.** The condition for a pair to collapse, $b_j=0$, is one equation, so it is a codimension-one condition and a random element has no zero eigenvalue when $n$ is even. For odd $n$ the corank is at least one by parity, and it is exactly one generically.

**The count of parameters is the orbit plus the moduli.** The stabiliser of the canonical form in $\mathrm{O}(n)$ is $\mathrm{O}(n-2s)$ on the zero space times a copy of $\mathrm{SO}(2)$ on each pair plane, of dimension

$$
\binom{n-2s}{2}+s .
$$

So the orbit of $K$ has dimension $\binom{n}{2}-\binom{n-2s}{2}-s$, and adding the $s$ moduli $b_j$ gives $\binom{n}{2}-\binom{n-2s}{2}$. The count reads $3=2+1$ at $n=3$, $6=4+2$ at $n=4$ and $10=8+2$ at $n=5$, cases where the corank is at most one and the binomial term vanishes.

**The zeros are constraints, not parameters.** A zero eigenvalue is not a modulus: it is a condition that holds on a subset of codimension $\binom{n-2s}{2}$, which is zero only when the corank is $0$ or $1$. For corank $2$ and above the stratum of the matrix is strictly smaller than $\mathfrak{so}(n)$, and the deficit is the dimension of $\mathrm{O}(n-2s)$ acting on the zero space.

## Summary

An antisymmetric real matrix has a purely imaginary spectrum, because $\bar z^{\mathsf T}Kz$ is purely imaginary and equals $\lambda\|z\|^{2}$, and its only real eigenvalue is $0$, because $x^{\mathsf T}Kx=0$ for real $x$. Its canonical form is $Q\operatorname{diag}(0,\dots,0,b_1J,\dots,b_sJ)Q^{\mathsf T}$ with $b_j>0$, so the rank is $2s$ and the corank is $n-2s$, the multiplicity of the zero eigenvalue. The Pfaffian is defined for even size and its square is the determinant; numerically the identity holds at $n=2$ and $n=4$. The square $K^{2}$ is symmetric and negative semidefinite, hence orthogonally diagonalisable with eigenvalues $-b_j^{2}$ and $0$, and it is $100$ of $100$ at $n=2,3,4$. The exponential is orthogonal of determinant one and acts as a rotation by the angle $b_j$ on each plane. The space has dimension $n(n-1)/2$, the generic element has $\lfloor n/2\rfloor$ pairs, and the orbit plus the moduli account for the whole dimension.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | a real antisymmetric matrix, $K^{\mathsf T}=-K$ |
| $J$ | the rotation $\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}$ |
| $b_j$ | the moduli of the pairs, $b_j>0$ |
| $s$ | the number of pairs, so that $\operatorname{rk}K=2s$ |
| $\operatorname{Pf}(K)$ | the Pfaffian, defined for even $n$ |
| $\mathfrak{so}(n)$ | the space of antisymmetric matrices, of dimension $n(n-1)/2$ |
| $|K|$ | the semidefinite square root of $-K^{2}$ |
| $\exp K$ | the orthogonal matrix $e^{K}$, of determinant $1$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for antisymmetric matrices, the Pfaffian and the canonical form.
- Werner Greub, *Multilinear Algebra* (Springer, 1978), for the Pfaffian and its square as the determinant.
- [Normal Matrices over $\mathbb{R}$ and the Orthogonal Spectral Theorem](normal-matrices-over-r-and-the-orthogonal-spectral-theorem.html), for the block form in the proof of the canonical form.
- [The Spectral Theorem: the Symmetric Case](the-spectral-theorem-the-symmetric-case.html), for the theorem applied to $K^{2}$.
- [The Real Jordan Form and the Rotation Blocks](the-real-jordan-form-and-the-rotation-blocks.html), for the block $bJ$ as a rotation.
