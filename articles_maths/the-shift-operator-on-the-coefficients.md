
# __The Shift Operator on the Coefficients__

## Introduction

The coefficient sequence $(a_n)$ of a Dirichlet series carries two elementary operators: the section at a fixed integer $m$, which retains only the coefficients at the multiples of $m$, and the division by $m$, which reads the coefficient at $mn$. On the side of the series the section is multiplication by $m^{-s}$ and the division is the part of the series supported on the multiples of $m$, rescaled by $m^{s}$. The two operators are adjoint to one another for the form of the category, the section is an isometry and the division a co-isometry, and their spectrum is the closed disk of the appropriate radius. They also give the mechanism by which the analytic continuation of a Dirichlet series is organised: the continuation of the whole is equivalent to the continuation of the $m$-divisible section together with the elementary factor $m^{-s}$.

The conventions are those of the category: $\mathcal{A}$ is the algebra of arithmetic functions, $\delta_m$ the function with $\delta_m(m)=1$ and all other values $0$, $\mathcal{H}=\ell^2$ with the form $\langle f,g\rangle=\sum_nf(n)\overline{g(n)}$, and for real $\sigma$ the Banach space $\mathcal{A}(\sigma)=\{f:\|f\|_\sigma=\sum_n|f(n)|n^{-\sigma}<\infty\}$, an algebra under convolution. The multiplication operators of the same algebra are in *Multiplication Operators on an L-Function*; the shift of the argument $s\mapsto s+1$ is *Shift Operator on a Dirichlet Series*, the next article. Nothing here reads a distance as an object.

## The Two Shifts

### Definitions

**Definition.** For $m\ge1$ the **division** $S_m$ and the **section** $D_m$ act on arithmetic functions by
$$
(S_mf)(n)=f(mn),\qquad (D_mf)(n)=f(n/m)\ \text{ if } m\mid n,\ \text{ and } 0 \text{ otherwise}.
$$
The operator $D_m$ retains the multiples of $m$; the operator $S_m$ reads the coefficient at $mn$ and kills the nonmultiples of $m$.

### Elementary identities

**Theorem.** For all $m,k\ge1$,
$$
S_mS_k=S_{mk},\qquad D_mD_k=D_{mk},\qquad S_mD_m=\mathrm{id},\qquad D_mS_m=P_m,
$$
where $P_m$ is the orthogonal projection onto the subspace of functions supported on the multiples of $m$. In particular $D_m$ is injective with left inverse $S_m$, and $S_m$ has kernel the functions supported on the nonmultiples of $m$.

**Proof.** Compute on $\delta_n$: $S_m\delta_n=\delta_{n/m}$ if $m\mid n$ and $0$ otherwise, while $D_m\delta_n=\delta_{mn}$; hence $D_mD_k\delta_n=\delta_{mkn}=D_{mk}\delta_n$ and $S_mS_k\delta_n=S_{mk}\delta_n$. Further $S_mD_m\delta_n=S_m\delta_{mn}=\delta_n$, while $D_mS_m\delta_n=[m\mid n]\delta_n=P_m\delta_n$. The stated consequences are immediate.

**Proposition (relation to convolution).** $D_m=M_{\delta_m}$, the multiplication operator by the function $\delta_m$, and $S_m$ is its transpose in the sense that $\langle D_mf,g\rangle=\langle f,S_mg\rangle$ for all $f,g\in\mathcal{H}$. Hence $D_m^*=S_m$ and $S_m^*=D_m$, and the two shifts are mutual adjoints.

**Proof.** $(\delta_m*f)(n)=[m\mid n]f(n/m)=D_mf(n)$, so $D_m=M_{\delta_m}$; then $\langle D_mf,g\rangle=\sum_{n:m\mid n}f(n/m)\overline{g(n)}=\sum_kf(k)\overline{g(mk)}=\langle f,S_mg\rangle$, which is the adjoint statement.

## Norms and Spectrum

### The norms on the weighted spaces

**Theorem.** On the Banach algebra $\mathcal{A}(\sigma)$ with the norm $\|\cdot\|_\sigma$,
$$
\|D_m\|_\sigma=m^{-\sigma},\qquad \|S_m\|_\sigma=m^{\sigma}.
$$
On the Hilbert space $\mathcal{H}=\ell^2$ the section $D_m$ has operator norm $1$ and is an isometry, and $S_m$ is a co-isometry with $S_mS_m^*=\mathrm{id}$ and $S_m^*S_m=P_m$.

**Proof.** Compute $\|D_mf\|_\sigma=\sum_{n:m\mid n}|f(n/m)|n^{-\sigma}=\sum_k|f(k)|(mk)^{-\sigma}=m^{-\sigma}\|f\|_\sigma$ and $\|S_mf\|_\sigma=\sum_n|f(mn)|n^{-\sigma}=m^{\sigma}\sum_k|f(k)|k^{-\sigma}=m^{\sigma}\|f\|_\sigma$. On $\ell^2$ the first computation with $\sigma=0$ gives $\|D_mf\|_2=\|f\|_2$, so $D_m$ is an isometry; and $\|S_mf\|_2\le\|f\|_2$, the kernel of $S_m$ being the functions supported on the nonmultiples of $m$.

### The spectrum

**Theorem.** On $\mathcal{H}=\ell^2(\mathbb{N})$, the spectrum of $D_m$ is the closed unit disk $\{|\zeta|\le1\}$, and the spectrum of $S_m$ is the same disk. On $\mathcal{A}(\sigma)$ the spectrum of $D_m$ is the closed disk of radius $m^{-\sigma}$ and the spectrum of $S_m$ is the closed disk of radius $m^{\sigma}$.

**Proof.** Decompose $\mathbb{N}$ into the chains $k,km,km^2,\ldots$ for the integers $k$ not divisible by $m$. Each chain is a copy of the additive monoid $\mathbb{N}_0$, and on it $D_m$ is the unilateral up-shift and $S_m$ the unilateral down-shift. Hence $D_m$ is the countable direct sum of copies of the up-shift on $\ell^2(\mathbb{N}_0)$, and $S_m$ the direct sum of copies of the down-shift. The up-shift on $\ell^2(\mathbb{N}_0)$ is an isometry whose spectrum is the closed unit disk, and a countable direct sum of copies has the same spectrum because it contains one copy as a direct summand and its norm is $1$. The rescaling to $\mathcal{A}(\sigma)$ multiplies the operators by $m^{-\sigma}$ and $m^{\sigma}$ after the substitution $f\mapsto(f(n)n^{-\sigma})$, which is an isometric identification of $\mathcal{A}(\sigma)$ with $\ell^1$ and preserves the spectral radius. The spectrum of a shift on $\ell^p(\mathbb{N}_0)$, $1\le p\le\infty$, is the closed unit disk; the standard computation is in *Spectral Theory*.

**Corollary.** The spectral radius of $D_m$ on $\mathcal{H}$ is $1$ although $D_m$ is not invertible: $D_m$ is an isometry with image the functions supported on the multiples of $m$, its inverse on that image is $S_m$, and its cokernel is the space of functions supported on the nonmultiples of $m$. The value $0$ belongs to the spectrum as a limit of the finite-dimensional approximations, not as an eigenvalue.

## The Shift Equation and the Analytic Continuation

### The $L$-function identity

**Theorem.** For every $f$ and every $m$,
$$
L(D_mf,s)=m^{-s}L(f,s),\qquad L(S_mf,s)=m^{s}\sum_{\substack{n\ge1\\ m\mid n}}f(n)n^{-s}.
$$
The first identity is an identity of Dirichlet series in their common half-plane; the second exhibits $L(S_mf,\cdot)$ as $m^{s}$ times the $m$-divisible section of $L(f,\cdot)$.

**Proof.** For the first, $\sum_n(D_mf)(n)n^{-s}=\sum_{n:m\mid n}f(n/m)n^{-s}=\sum_kf(k)(mk)^{-s}=m^{-s}L(f,s)$. For the second, $\sum_nf(mn)n^{-s}=\sum_{n:m\mid n}f(n)(n/m)^{-s}=m^{s}\sum_{n:m\mid n}f(n)n^{-s}$.

### Continuation

**Definition.** The **$m$-divisible section** of $L(f,\cdot)$ is $L^{(m)}(f,s)=\sum_{n:m\mid n}f(n)n^{-s}$, so that $L(f,s)=L^{(m)}(f,s)+L^{(1-m)}(f,s)$ with the second term the sum over $n$ not divisible by $m$.

**Theorem (continuation by the shift).** $L^{(m)}(f,s)=m^{-s}L(S_mf,s)$ and $L(f,s)=m^{-s}L(D_mf,s)$. Consequently the meromorphic continuation of $L(f,\cdot)$ is equivalent to that of $L(D_mf,\cdot)$ for any single $m$, and the continuation of $L^{(m)}(f,\cdot)$ is equivalent to that of $L(S_mf,\cdot)$; the incompletely multiplicative factor $m^{-s}$ has no zeros or poles and neither helps nor obstructs the continuation.

**Proof.** The identities are the theorem above. The equivalence of the continuations is the invariance of meromorphic continuation under multiplication by the entire function $m^{-s}$; the statement about sections is the splitting $L=L^{(m)}+L^{(1-m)}$ together with the identity for $L^{(m)}$.

**Remark (the Bohr spectrum).** In Bohr's terminology the **spectrum** of the Dirichlet series $\sum_nf(n)n^{-s}$ is the set of frequencies $\{\log n:f(n)\ne0\}$, and the shift $D_m$ acts on that set by the translation $\log n\mapsto\log n+\log m$ of the frequencies under the identification $n\mapsto mn$. The down-shift is thus the operator form of the elementary translation of the frequency set by $\log m$, and it is the reason the continuation of a Dirichlet series is studied frequency by frequency; the theory is in *Zeta Functions* and *Harmonic Analysis*.

## Worked Examples

**Example ($m=p$, $f=\mathbf{1}$).** $D_p\mathbf{1}=\delta_p$-convolution: $(D_p\mathbf{1})(n)=1$ if $p\mid n$, $0$ otherwise, and $L(D_p\mathbf{1},s)=p^{-s}\zeta(s)$; this is the classical identity $\zeta(s)=p^{-s}\zeta(s)+\sum_{p\nmid n}n^{-s}$ written with the shift.

**Example (the Möbius function).** $D_2\mu$ vanishes on the odd integers and equals $\mu(n/2)$ on the even ones; $L(D_2\mu,s)=2^{-s}L(\mu,s)=2^{-s}/\zeta(s)$.

**Example (a normalised eigenform).** For $f$ with coefficients $a_n$, $(D_pf)(n)=a_{n/p}[p\mid n]$ and $L(D_pf,s)=p^{-s}L(f,s)$; the extraction $S_p$ recovers $a_{pn}$ and the local recursion of *The Hecke Operator* is the composition $S_pD_p=\mathrm{id}$ together with $D_pS_p=P_p$.

## Failure of the Degenerate Cases

The identities of this article fail in three degenerate configurations. First, if $m=1$ then $S_1=D_1=\mathrm{id}$ and the whole content collapses; the operators are interesting only for $m>1$. Second, the isometry $D_m$ is not surjective and the co-isometry $S_m$ is not injective; the spectral statements on $\mathcal{A}(\sigma)$ use the weight $n^{-\sigma}$, and at $\sigma=0$ the Banach algebra $\mathcal{A}(0)$ contains the unbounded-support functions for which $D_m$ has norm $1$ but is not surjective, so the "inverse" $S_m$ does not invert $D_m$. Third, the continuation statement is vacuous when $L(f,\cdot)$ has no continuation at all; the shift cannot create one, and the equivalence is an equivalence between two failures. These are the degenerate cases; they are the boundary of the half-plane of absolute convergence, where the shift equation still holds as an identity of series but the two sides have different domains of validity.

## Summary

For $m\ge1$ the division $S_mf(n)=f(mn)$ and the section $D_mf(n)=f(n/m)$ for $m\mid n$, $0$ otherwise, satisfy $S_mS_k=S_{mk}$, $D_mD_k=D_{mk}$, $S_mD_m=\mathrm{id}$ and $D_mS_m=P_m$, the projection onto the multiples of $m$; $D_m$ is the multiplication operator $M_{\delta_m}$, and $D_m^*=S_m$, $S_m^*=D_m$ for the form of the category. On the weighted space $\mathcal{A}(\sigma)$ the norms are $\|D_m\|_\sigma=m^{-\sigma}$ and $\|S_m\|_\sigma=m^{\sigma}$; on $\mathcal{H}$ the section $D_m$ is an isometry of norm $1$ and the division $S_m$ is a co-isometry, the spectrum of both being the closed unit disk, and on $\mathcal{A}(\sigma)$ the disks of radius $m^{-\sigma}$ and $m^{\sigma}$. The $L$-function identities are $L(D_mf,s)=m^{-s}L(f,s)$ and $L(S_mf,s)=m^{s}L^{(m)}(f,s)$, so the continuation of $L(f,\cdot)$ is the continuation of $L(D_mf,\cdot)$ and the elementary factor $m^{-s}$, and Bohr's frequency spectrum is translated by $\log m$ under the shift.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S_m$, $(S_mf)(n)=f(mn)$ | Division; kills the nonmultiples of $m$ |
| $D_m$, $(D_mf)(n)=f(n/m)$ for $m\mid n$ | Section; isometry of $\mathcal{H}$ |
| $D_m=M_{\delta_m}$ | Section is convolution with $\delta_m$ |
| $S_mD_m=\mathrm{id}$, $D_mS_m=P_m$ | The fundamental identities |
| $D_m^*=S_m$, $S_m^*=D_m$ | Mutual adjointness |
| $\|D_m\|_\sigma=m^{-\sigma}$, $\|S_m\|_\sigma=m^{\sigma}$ | Norms on $\mathcal{A}(\sigma)$ |
| $\operatorname{spec}D_m=\{|\zeta|\le1\}$ | Spectrum on $\mathcal{H}$ |
| $L(D_mf,s)=m^{-s}L(f,s)$ | The shift equation |
| $L^{(m)}(f,s)=\sum_{m\mid n}f(n)n^{-s}$ | The $m$-divisible section |
| $\{\log n:f(n)\ne0\}$ | Bohr spectrum |

## Further Reading

- Hugh Montgomery and Robert Vaughan, *Multiplicative Number Theory I: Classical Theory* (Cambridge University Press, 2007), for the arithmetic functions and the dirichlet convolution.
- Harald Bohr, *Almost Periodic Functions* (Chelsea, 1947), for the frequency spectrum of a Dirichlet series.
- Einar Hille and Ralph Phillips, *Functional Analysis and Semi-Groups* (American Mathematical Society, 1957), for the unilateral shift and its spectrum.
- Paul Halmos, *A Hilbert Space Problem Book* (Springer, 1982), for the shift operators and the partial isometries.
- Nelson Dunford and Jacob Schwartz, *Linear Operators, Part II: Spectral Theory* (Interscience, 1963), for the spectrum of the weighted shifts.
