# __Spectral Theory and the Spectral Projectors of $M_6(\mathbb{C})$__

## Introduction

The spectral theory of $A\in M_6(\mathbb{C})$ is the study of the resolvent

$$
R(z)=(zI_6-A)^{-1},
$$

its poles, and the projectors that the poles define. The spectrum $\sigma(A)$ is the set of roots of the characteristic sextic; the resolvent is analytic on the complement and has a pole of finite order at each eigenvalue. The **Dunford calculus** evaluates a holomorphic function on $A$ by a contour integral of the resolvent,

$$
f(A)=\frac{1}{2\pi\mathrm i}\oint_\gamma f(z)R(z)\,dz,
$$

and the **spectral projectors** are the residues

$$
P_i=\frac{1}{2\pi\mathrm i}\oint_{\gamma_i}R(z)\,dz .
$$

They are idempotent, orthogonal, sum to the identity, and their images are the generalized eigenspaces. At a simple spectrum they are the Lagrange projectors; at a repeated root the individual Lagrange projectors have poles, while the cluster projectors and the Dunford calculus survive.

The article assumes the characteristic polynomial and the strata of *The Sextic and the Spectral Strata of $M_6(\mathbb{C})$* and the Jordan decomposition of *The Element, the Coordinates and the Trace of $M_6(\mathbb{C})$*. It uses the holomorphic functional calculus; the contour integrals are those of *The Sextic and the Spectral Strata of $M_6(\mathbb{C})$*, but the emphasis here is the resolvent and the spectral radius. The Hermitian spectral theorem is *The Involution and the Hermitian Structure of $M_6(\mathbb{C})$*; the exponential is *The Exponential and the Lie Group of $M_6(\mathbb{C})$*.

## The Spectrum and the Resolvent

### The Spectrum

**Definition.** The **resolvent set** of $A$ is

$$
\rho(A)=\{z\in\mathbb{C}:zI_6-A\text{ is invertible}\},
$$

and the **spectrum** is its complement

$$
\sigma(A)=\mathbb{C}\setminus\rho(A).
$$

**Theorem.** $\sigma(A)$ is the set of roots of the characteristic polynomial:

$$
\sigma(A)=\{\lambda:\chi_A(\lambda)=0\},
$$

and it is a nonempty finite set of at most six points.

**Proof.** $zI_6-A$ is invertible iff $\det(zI_6-A)\neq0$, that is iff $\chi_A(z)\neq0$. The fundamental theorem of algebra gives at least one root and at most six.

**Definition.** The **algebraic multiplicity** of $\lambda\in\sigma(A)$ is its multiplicity as a root of $\chi_A$; the **geometric multiplicity** is $\dim\ker(A-\lambda I_6)$. The geometric multiplicity is at most the algebraic multiplicity, with equality for all $\lambda$ iff $A$ is diagonalizable.

**Proof.** The generalized eigenspace $\ker((A-\lambda I)^{m})$ has dimension equal to the algebraic multiplicity; the eigenspace is contained in it.

### The Resolvent

**Definition.** The **resolvent** of $A$ is

$$
R(z)=(zI_6-A)^{-1},
\qquad
z\in\rho(A).
$$

**Theorem (the resolvent identity).**

$$
R(z)-R(w)=(w-z)R(z)R(w),
\qquad
z,w\in\rho(A).
$$

**Proof.** Multiply $(zI-A)^{-1}-(wI-A)^{-1}$ by $(zI-A)(wI-A)$:

$$
(wI-A)-(zI-A)=(w-z)I=(w-z)(zI-A)(wI-A)R(z)R(w).
$$

**Corollary (the Neumann series).** For $|z|>\lVert A\rVert$,

$$
R(z)=\sum_{n=0}^{\infty}\frac{A^n}{z^{n+1}},
$$

and the series converges absolutely and uniformly on compact subsets of $|z|>r(A)$.

**Proof.** $R(z)=z^{-1}(I-A/z)^{-1}=z^{-1}\sum_n(A/z)^n$ for $|z|>\lVert A\rVert$; the series converges because $\lVert A/z\rVert<1$. The radius of convergence is the spectral radius by the Gelfand formula below.

**Theorem (the Laurent expansion at an eigenvalue).** Let $\lambda$ be an eigenvalue and let $\gamma$ be a small positively oriented circle around $\lambda$ containing no other eigenvalue. Then

$$
R(z)=\sum_{k=1}^{m}\frac{N_k}{(z-\lambda)^k}+H(z),
$$

where $m$ is the size of the largest Jordan block of $\lambda$, $N_k$ are matrices, and $H$ is holomorphic inside $\gamma$. The coefficient $N_1$ is the spectral projector $P_\lambda$.

**Proof.** In the Jordan basis, the resolvent of a Jordan block $J_m(\lambda)$ is the finite sum

$$
(zI-J_m(\lambda))^{-1}
=\sum_{k=1}^{m}\frac{N_m^{k-1}}{(z-\lambda)^k},
$$

where $N_m$ is the nilpotent shift; summing over the blocks gives the Laurent expansion. The residue $N_1$ is the projector onto the generalized eigenspace.

### The Spectral Radius

**Definition.** The **spectral radius** of $A$ is

$$
r(A)=\max_{\lambda\in\sigma(A)}\lvert\lambda\rvert .
$$

**Theorem (the Gelfand formula).** For any matrix norm,

$$
r(A)=\lim_{n\to\infty}\lVert A^n\rVert^{1/n}.
$$

In particular the limit is independent of the norm.

**Proof.** The standard Gelfand formula; for the operator norm, $r(A)=\inf_n\lVert A^n\rVert^{1/n}$, and the limit exists and equals the infimum.

**Theorem (the inequalities).** For any induced norm,

$$
r(A)\le\lVert A\rVert,
$$

and for the operator norm,

$$
r(A)\le\lVert A\rVert_\infty\le\lVert A\rVert_2\le\lVert A\rVert_1 .
$$

**Proof.** Every eigenvalue satisfies $\lvert\lambda\rvert\le\lVert A\rVert$ for an induced norm: if $Ax=\lambda x$ with $\lVert x\rVert=1$, then $\lvert\lambda\rvert=\lVert Ax\rVert\le\lVert A\rVert$. The norm inequalities are those of *The Forms, the Norms and the Singular Set of $M_6(\mathbb{C})$*.

**Theorem (the Neumann criterion).** The following are equivalent:

- $r(A)<1$;
- $A^n\to0$ as $n\to\infty$;
- the series $\sum_{n\ge0}A^n$ converges;
- $I_6-A$ is invertible, and then $(I_6-A)^{-1}=\sum_{n\ge0}A^n$.

**Proof.** If $r(A)<1$, the Gelfand formula gives $\lVert A^n\rVert^{1/n}<1$ eventually, so $A^n\to0$ and the geometric series converges. Conversely, if the series converges, its terms tend to zero, so $r(A)<1$ (otherwise the eigenvalues of modulus at least one would prevent convergence). The inverse identity is the geometric series.

**Corollary (the resolvent at infinity).** The spectral radius is the radius of the largest disk outside which the Neumann series converges, and the poles of $R(z)$ are exactly the eigenvalues.

**Proof.** The Neumann series converges for $|z|>r(A)$ and diverges for $|z|<r(A)$; the resolvent is analytic on $\rho(A)$ and has poles at the eigenvalues.

## The Jordan Form and the Minimal Polynomial

### The Jordan Form

**Theorem (the Jordan normal form).** There is an invertible $P$ with

$$
A=PJP^{-1},
\qquad
J=\bigoplus_{i=1}^{r}\bigoplus_{j=1}^{s_i}J_{m_{ij}}(\lambda_i),
$$

where $J_m(\lambda)=\lambda I_m+N_m$ and $N_m$ is the nilpotent shift.

**Proof.** The standard Jordan normal form theorem over the algebraically closed field $\mathbb{C}$.

**Corollary (the spectral data).** The spectrum is $\{\lambda_1,\dots,\lambda_r\}$; the algebraic multiplicity of $\lambda_i$ is $\sum_jm_{ij}$; the geometric multiplicity is $s_i$; the largest block is $\max_jm_{ij}$.

**Proof.** Read the block sizes.

### The Minimal Polynomial

**Definition.** The **minimal polynomial** of $A$ is the monic polynomial $m_A$ of least degree with $m_A(A)=0$.

**Theorem.** The minimal polynomial is

$$
m_A(t)=\prod_{i=1}^{r}(t-\lambda_i)^{\ell_i},
\qquad
\ell_i=\max_jm_{ij},
$$

and it divides the characteristic polynomial

$$
\chi_A(t)=\prod_{i=1}^{r}(t-\lambda_i)^{m_i},
\qquad
m_i=\sum_jm_{ij}.
$$

**Proof.** The minimal polynomial vanishes on each Jordan block iff it is divisible by $(t-\lambda_i)^{\ell_i}$; the product is the least common multiple of the elementary divisors. The characteristic polynomial is the product of the diagonal entries.

**Corollary (the cyclic case).** $A$ is cyclic iff $m_A=\chi_A$; equivalently, iff the centralizer of $A$ is $\mathbb{C}[A]$, of dimension six.

**Proof.** The equality of degrees means a single Jordan block for each eigenvalue, which is the cyclic condition.

### The Spectral Decomposition

**Theorem (the Dunford decomposition).** Let $P_i$ be the spectral projector of $\lambda_i$. Then

$$
A=\sum_{i=1}^{r}(\lambda_iP_i+N_i),
\qquad
N_i=(A-\lambda_iI_6)P_i,
$$

with

$$
P_iP_j=\delta_{ij}P_i,\qquad
\sum_iP_i=I_6,\qquad
P_iA=AP_i,
$$

and $N_i$ nilpotent of order $\ell_i$, with $N_iN_j=0$ for $i\neq j$.

**Proof.** The images of the $P_i$ are the generalized eigenspaces; on the $i$-th, $A=\lambda_iI+N_i$; the projectors are the coordinate projections. The nilpotence order is the largest block; the products $N_iN_j$ vanish because the projectors are orthogonal.

**Corollary (the semisimple and nilpotent parts).**

$$
S=\sum_i\lambda_iP_i,
\qquad
N=\sum_iN_i,
\qquad
A=S+N,
$$

and $S$ is semisimple, $N$ is nilpotent, $SN=NS$.

**Proof.** $S$ is diagonal in the Jordan basis; $N$ is the sum of the nilpotent shifts; they commute because the $P_i$ commute with $A$.

## The Dunford Calculus

### The Functional Calculus

**Theorem (the Dunford calculus).** Let $f$ be holomorphic on an open set containing $\sigma(A)$, and let $\gamma$ be a finite union of positively oriented Jordan curves in the domain of $f$, enclosing $\sigma(A)$ and no point of the complement of the domain. Then

$$
f(A)=\frac{1}{2\pi\mathrm i}\oint_\gamma f(z)R(z)\,dz
$$

defines a homomorphism

$$
f\longmapsto f(A),
\qquad
(fg)(A)=f(A)g(A),
\qquad
1\longmapsto I_6,
$$

which agrees with the polynomial calculus.

**Proof.** The integral converges because $R(z)$ is analytic on $\gamma$; the homomorphism property follows from the resolvent identity and the Cauchy theorem; for $f(z)=z^n$, the integral reproduces $A^n$ by the Neumann expansion at infinity.

**Corollary (the spectral mapping theorem).**

$$
\sigma(f(A))=f(\sigma(A)).
$$

**Proof.** The standard spectral mapping theorem for the holomorphic functional calculus; in the Jordan basis, $f(A)$ has the eigenvalues $f(\lambda_i)$ with the same block structure.

**Corollary (the spectral projectors).** For a contour $\gamma_i$ around $\lambda_i$ alone,

$$
P_i=\frac{1}{2\pi\mathrm i}\oint_{\gamma_i}R(z)\,dz,
$$

and $P_i$ is the spectral projector of $\lambda_i$.

**Proof.** The residue of the resolvent at $\lambda_i$ is the projector onto the generalized eigenspace, by the Laurent expansion.

### The Properties of the Projectors

**Theorem.** The spectral projectors satisfy

$$
P_i^2=P_i,\qquad
P_iP_j=\delta_{ij}P_i,\qquad
\sum_iP_i=I_6,\qquad
P_iA=AP_i,
$$

and

$$
\operatorname{rank}P_i=\operatorname{tr}P_i=m_i,
$$

the algebraic multiplicity. Moreover

$$
\operatorname{im}P_i=\ker((A-\lambda_iI_6)^{m_i}),
\qquad
\ker P_i=\bigoplus_{j\neq i}\operatorname{im}P_j .
$$

**Proof.** The projector is the residue of a simple pole of the resolvent; the rank is the dimension of the generalized eigenspace, which is the algebraic multiplicity; the trace of a rank-$m$ idempotent is $m$.

**Corollary (the restrictions).** On the image of $P_i$,

$$
A|_{P_i}= \lambda_iI+N_i,
$$

and $N_i$ is nilpotent; on the kernel of $P_i$, $A$ is the sum of the other blocks.

**Proof.** The generalized eigenspace is invariant; the restriction is $\lambda_iI$ plus the nilpotent part.

### The Resolvent and the Calculus

**Theorem.** The Dunford calculus is the residue calculus of the resolvent:

$$
f(A)=\sum_{i=1}^{r}\sum_{k=1}^{\ell_i}\frac{f^{(k-1)}(\lambda_i)}{(k-1)!}N_i^{k-1},
$$

where $N_i=(A-\lambda_iI)P_i$.

**Proof.** Expand $f$ in a Taylor series around $\lambda_i$ inside the contour and use the Laurent expansion of the resolvent; the residues give the derivatives of $f$ at the eigenvalues.

**Corollary (the polynomial case).** For a polynomial $p$,

$$
p(A)=\sum_i\left(p(\lambda_i)P_i+\sum_{k=1}^{\ell_i}\frac{p^{(k-1)}(\lambda_i)}{(k-1)!}N_i^{k-1}\right).
$$

**Proof.** The polynomial is holomorphic; the formula is the Taylor expansion.

## The Lagrange Projectors

### The Simple Spectrum

**Theorem.** If $A$ has six distinct eigenvalues, the spectral projectors are the Lagrange projectors

$$
P_i=\prod_{j\neq i}\frac{A-\lambda_jI_6}{\lambda_i-\lambda_j},
\qquad
i=1,\dots,6,
$$

and they coincide with the Dunford projectors.

**Proof.** The Lagrange polynomial $L_i$ satisfies $L_i(\lambda_j)=\delta_{ij}$; by the spectral mapping theorem, $L_i(A)$ is the projector onto the $i$-th eigenspace. The Dunford projector of a simple eigenvalue is the same residue.

**Corollary (the interpolation).** For every polynomial $p$ of degree at most five,

$$
p(A)=\sum_{i=1}^{6}p(\lambda_i)P_i .
$$

**Proof.** Both sides are polynomials in $A$ of degree at most five that agree on the six eigenvalues; the Lagrange interpolation is unique.

### The Repeated Root

**Theorem (the degeneration).** Let $A(\varepsilon)$ be a holomorphic family, and suppose that at $\varepsilon=0$ two eigenvalues coalesce. Then the individual Lagrange projectors may have poles of order one, the cluster projector (the sum over the coalescing eigenvalues) has a holomorphic limit, and the weighted sum $\sum_i\lambda_i(\varepsilon)P_i(\varepsilon)=A(\varepsilon)$ has the limit $A(0)$.

**Proof.** The Lagrange denominators are the eigenvalue differences; the cluster sum is the contour integral around the cluster, which is holomorphic as long as the cluster is separated from the other eigenvalues. The spectral identity is an identity for every $\varepsilon$.

**Example (the Jordan block).** For

$$
A(\varepsilon)=\begin{pmatrix}\lambda+\varepsilon&1\\0&\lambda\end{pmatrix},
$$

the eigenvalues are $\lambda+\varepsilon$ and $\lambda$; the projectors are

$$
P_+(\varepsilon)=\begin{pmatrix}1&1/\varepsilon\\0&0\end{pmatrix},
\qquad
P_-(\varepsilon)=\begin{pmatrix}0&-1/\varepsilon\\0&1\end{pmatrix}.
$$

Both have a pole at $\varepsilon=0$; their sum is $I_2$; the weighted sum is $A(\varepsilon)$, which tends to $\lambda I_2+E_{12}$. The cluster projector is $I_2$, the spectral projector of $A(0)$ onto its generalized eigenspace; the nilpotent part $E_{12}$ is the limit of $\varepsilon P_+(\varepsilon)$.

**Corollary (the Dunford limit).** The Dunford projector of the cluster is the limit of the sum of the Lagrange projectors; the individual Lagrange projectors may diverge; when they have a limit, it need not be the spectral projector of the limit matrix. The Dunford calculus of the limit is the calculus of the Jordan block.

**Proof.** The cluster contour encloses both eigenvalues for small $\varepsilon$ and deforms to the contour of the repeated eigenvalue; the individual contours shrink to a point and the resolvent poles collide.

**Remark (the Lagrange and the Dunford).** The Lagrange formula is the interpolation formula of the simple spectrum; the Dunford formula is the residue formula of the general spectrum. **At a simple spectrum they agree; at a repeated root the Lagrange individual projectors degenerate, and the Dunford cluster projectors are the correct limit.**

## Summary

The spectrum of $A$ is the set of roots of the characteristic sextic, and the resolvent

$$
R(z)=(zI_6-A)^{-1}
$$

is analytic off the spectrum with poles at the eigenvalues. The spectral radius is

$$
r(A)=\max_i\lvert\lambda_i\rvert=\lim_{n\to\infty}\lVert A^n\rVert^{1/n},
$$

and $r(A)\le\lVert A\rVert$ for every induced norm. The Neumann series converges for $\lVert A\rVert<1$, and $r(A)<1$ iff $A^n\to0$.

$$
\boxed{\ \sigma(A)=\{\chi_A=0\},\qquad r(A)=\lim\lVert A^n\rVert^{1/n},\qquad P_i=\frac{1}{2\pi\mathrm i}\oint_{\gamma_i}R(z)\,dz .\ }
$$

The Dunford calculus is

$$
f(A)=\frac{1}{2\pi\mathrm i}\oint_\gamma f(z)R(z)\,dz,
\qquad
\sigma(f(A))=f(\sigma(A)),
$$

and the spectral projectors are idempotent, orthogonal, sum to $I_6$, commute with $A$, and have rank equal to the algebraic multiplicity.

At a simple spectrum the projectors are the Lagrange projectors $P_i=\prod_{j\neq i}(A-\lambda_j)/(\lambda_i-\lambda_j)$; at a repeated root the individual Lagrange projectors have poles, the cluster projectors extend, and the nilpotent part is the residue.

| Object | Data |
|---|---|
| Spectrum | roots of $\chi_A$, at most $6$ points |
| Resolvent | $(zI_6-A)^{-1}$, poles at $\sigma(A)$ |
| Spectral radius | $\max\lvert\lambda_i\rvert=\lim\lVert A^n\rVert^{1/n}$ |
| Dunford calculus | $f(A)=\frac{1}{2\pi\mathrm i}\oint fR$ |
| Spectral projectors | residues, rank $m_i$ |
| Simple spectrum | Lagrange projectors |
| Repeated root | cluster projectors, nilpotent residue |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma(A)$ | the spectrum |
| $\rho(A)$ | the resolvent set |
| $r(A)$ | the spectral radius |
| $R(z)$ | the resolvent $(zI_6-A)^{-1}$ |
| $P_i$ | the spectral projector of $\lambda_i$ |
| $N_i$ | the nilpotent part $(A-\lambda_iI)P_i$ |
| $m_A$ | the minimal polynomial |
| $\ell_i$ | the size of the largest Jordan block of $\lambda_i$ |

## Further Reading

- [The Sextic and the Spectral Strata of $M_6(\mathbb{C})$](the-sextic-and-the-spectral-strata-of-m6c.html), for the characteristic polynomial, the strata and the degeneration.
- [The Element, the Coordinates and the Trace of $M_6(\mathbb{C})$](the-element-the-coordinates-and-the-trace-of-m6c.html), for the Jordan decomposition.
- [The Involution and the Hermitian Structure of $M_6(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m6c.html), for the Hermitian spectral theorem.
- [The Exponential and the Lie Group of $M_6(\mathbb{C})$](the-exponential-and-the-lie-group-of-m6c.html), for the exponential as a Dunford calculus.
- [The Polar Decomposition of $M_6(\mathbb{C})$](the-polar-decomposition-of-m6c.html), for the spectral theory of $A^*A$.
- [The Matrix Algebra $M_6(\mathbb{C})$](the-matrix-algebra-m6c.html), for the characteristic polynomial and Cayley–Hamilton.
- [Holomorphic Functional Calculus](holomorphic-functional-calculus.html), for the Dunford calculus in a Banach algebra.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 1995), for the resolvent and the spectral projectors at a coalescence.
