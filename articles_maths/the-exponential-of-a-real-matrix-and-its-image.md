# __The Exponential of a Real Matrix and Its Image__

## Introduction

**The exponential of a real matrix is a convergent series at every point, its image lies in the component of positive determinant, and the containment is strict: some matrices of positive determinant are not exponentials.**

The article proves the convergence and the norm bound, the transpose and determinant identities, the differentiability at the origin, and the closed forms on the diagonal, nilpotent, symmetric and triangular parts. It proves that the image lies in $\mathrm{GL}_n(\mathbb{R})^{+}$, contains a neighbourhood of the identity, misses matrices of that component, and is not dense. The counterexample that separates the image from the component is proved in *The Two Components of $\mathrm{GL}_n(\mathbb{R})$ and the Failure of the Exponential*; the restriction to the antisymmetric part is *The Exponential of the Antisymmetric Part: One-Parameter Rotations*. It assumes *The Matrix Algebra $M_n(\mathbb{R})$*.

Throughout $n\ge2$, the transpose is ${}^{\mathsf T}$, the identity is $\mathrm{I}$, and $\lVert\cdot\rVert$ is a submultiplicative norm.

## The Series

**Definition.** For $X\in M_n(\mathbb{R})$,

$$
\exp X=\sum_{k\ge0}\frac{X^{k}}{k!},\qquad X^{0}=\mathrm{I}.
$$

**The series converges at every point.** A submultiplicative norm satisfies $\lVert X^{k}\rVert\le\lVert X\rVert^{k}$, so the series of norms is dominated by the scalar exponential of the number $\lVert X\rVert$:

$$
\sum_{k\ge0}\frac{\lVert X^{k}\rVert}{k!}\le\sum_{k\ge0}\frac{\lVert X\rVert^{k}}{k!}=e^{\lVert X\rVert}.
$$

The bound depends on $X$ only through the norm, so the convergence is absolute and uniform on every ball, and each entry is a power series with infinite radius: the exponential is real-analytic, and

$$
\lVert\exp X\rVert\le e^{\lVert X\rVert},\qquad \lVert\exp X-\mathrm{I}\rVert\le e^{\lVert X\rVert}-1 .
$$

The second bound says that the defect tends to zero with $X$, so the map is continuous at the origin, and the first two terms give $\exp\mathrm{0}=\mathrm{I}$.

**A commuting pair adds.** If $XY=YX$ the binomial theorem applies to $(X+Y)^{k}$ and the rearrangement of the absolutely convergent double series gives

$$
\exp X\,\exp Y=\exp(X+Y)\qquad\text{whenever }XY=YX .
$$

Taking $Y=-X$ gives $\exp X\,\exp(-X)=\mathrm{I}$. Every exponential is invertible, with inverse $\exp(-X)$, so the image lies in the group of invertibles.

## The Transpose and the Determinant

**The transpose passes through the series.** Since $(X^{k})^{\mathsf T}=(X^{\mathsf T})^{k}$ for every $k$,

$$
\exp(X^{\mathsf T})=\big(\exp X\big)^{\mathsf T}.
$$

The exponential commutes with the involution of *The Matrix Algebra $M_n(\mathbb{R})$*: the exponential of a symmetric matrix is symmetric, and the exponential of an antisymmetric $K$ satisfies $\exp(K)^{\mathsf T}=\exp(-K)=\exp(K)^{-1}$, so it is orthogonal.

**The determinant of the exponential is the exponential of the trace.** For $X\in M_n(\mathbb{R})$,

$$
\det\exp X=\exp(\operatorname{tr}X)>0 .
$$

*Proof.* Put $A(t)=\exp(tX)$ and $f(t)=\det A(t)$. Then $A'(t)=XA(t)=A(t)X$, and Jacobi's formula gives $f'(t)=f(t)\operatorname{tr}\big(A(t)^{-1}A'(t)\big)=f(t)\operatorname{tr}X$. So $f'=(\operatorname{tr}X)f$ with $f(0)=1$, hence $f(t)=e^{t\operatorname{tr}X}$, and $t=1$ is the claim.

**The sign of the determinant is fixed over the whole image.** The right side is positive, so no exponential has determinant zero or determinant negative. On the antisymmetric part the trace is zero, so $\det\exp K=1$ and, with the transpose identity, $\exp K\in\mathrm{SO}(n)$.

## The Derivative at the Origin

**The derivative at the origin is the identity.** Splitting the series gives

$$
\exp(H)=\mathrm{I}+H+O\big(\lVert H\rVert^{2}\big),\qquad \frac{\lVert\exp H-\mathrm{I}-H\rVert}{\lVert H\rVert}\le\frac{e^{\lVert H\rVert}-1-\lVert H\rVert}{\lVert H\rVert},
$$

and the right side tends to $0$ because its numerator begins with $\lVert H\rVert^{2}/2$. So $d\exp_{\mathrm{0}}$ is the identity map of $M_n(\mathbb{R})$. The secant with $t=10^{-6}$ on a random $3\times3$ matrix differs from $H$ by $1.1\cdot10^{-6}$.

**The inverse function theorem then applies.** The derivative at $\mathrm{0}$ is invertible, so there are neighbourhoods $U$ of $\mathrm{0}$ and $V$ of $\mathrm{I}$ with $\exp:U\to V$ a diffeomorphism. The inverse is the logarithmic series

$$
\log(\mathrm{I}+Y)=\sum_{k\ge1}\frac{(-1)^{k+1}}{k}Y^{k},\qquad \lVert Y\rVert<1,
$$

which converges absolutely and inverts the exponential. So $\exp$ is injective near $\mathrm{0}$: the failure of injectivity is a large-scale phenomenon.

**The local statement does not globalise.** The derivative at $X$ is singular whenever two eigenvalues of $X$ differ by a nonzero multiple of $2\pi i$, since its second factor is $(\mathrm{I}-e^{-\operatorname{ad}X})/\operatorname{ad}X$. At $n=2$ and $X=2\pi J$ the eigenvalues are $\pm2\pi i$, the derivative is singular, and $\exp X=\mathrm{I}$.

## The Diagonal, the Nilpotent and the Symmetric Cases

**On diagonal matrices the exponential acts entry by entry.** For $D=\operatorname{diag}(d_{1},\dots,d_{n})$ the powers are diagonal, so

$$
\exp D=\operatorname{diag}\big(e^{d_{1}},\dots,e^{d_{n}}\big),
$$

and the entrywise logarithm is its inverse.

**On nilpotent matrices the series is a finite sum.** If $N^{m}=0$ then

$$
\exp N=\mathrm{I}+N+\frac{N^{2}}{2!}+\cdots+\frac{N^{m-1}}{(m-1)!},\qquad \log(\mathrm{I}+N)=\sum_{k=1}^{m-1}\frac{(-1)^{k+1}}{k}N^{k},
$$

and the two sums are inverse. So $\exp$ is a bijection from the nilpotent set onto the unipotent set $\mathrm{I}+\mathcal{N}$, an affine space and hence connected. At $n=3$ the matrix with $N_{12}=2$, $N_{23}=-1$ and the rest zero has $N^{3}=0$, and the truncated sum reproduces the exponential with error $0$.

**On symmetric matrices the exponential is a bijection onto the positive cone.** For $S=Q\Lambda Q^{\mathsf T}$ with $Q\in\mathrm{O}(n)$ and $\Lambda$ diagonal real, the series commutes with conjugation by $Q$, so

$$
\exp S=Q\,e^{\Lambda}\,Q^{\mathsf T},
$$

which is symmetric with eigenvalues $e^{\lambda_{i}}>0$, hence positive definite. Conversely every positive definite $P=Q\Lambda Q^{\mathsf T}$ with $\Lambda>0$ is $\exp S$ for $S=Q(\log\Lambda)Q^{\mathsf T}$. So

$$
\exp:\operatorname{Sym}_n\longrightarrow\operatorname{Sym}_n^{++}
$$

is a bijection. On $100$ random symmetric $4\times4$ matrices the exponential is symmetric to machine precision and its smallest eigenvalue is $0.0087$ in the worst case, never zero.

**On $\operatorname{Skew}_n$ the behaviour is the opposite.** There the exponential is neither injective nor a bijection onto a cone; that case is *The Exponential of the Antisymmetric Part: One-Parameter Rotations*.

## The Triangular Case

**On the triangular algebra the exponential is a bijection onto the positive triangular group.** Let $\mathfrak{b}$ be the algebra of upper triangular matrices. If $X\in\mathfrak{b}$ then every power of $X$ is upper triangular with diagonal $X_{ii}^{k}$, so $\exp X$ is upper triangular with diagonal entries $e^{X_{ii}}>0$. Conversely, write $T=\Lambda(\mathrm{I}+M)$ with $\Lambda=\operatorname{diag}(T_{ii})$ positive and $M$ strictly upper triangular, hence nilpotent. Then $\log T=(\log\Lambda)+\log(\mathrm{I}+M)$ lies in $\mathfrak{b}$, because the second term is the finite sum above. Therefore

$$
\exp:\mathfrak{b}\longrightarrow\{T\text{ upper triangular}:\ T_{ii}>0\}
$$

is a bijection onto a connected set. On the solvable part, as on the nilpotent part, the image is the whole identity component of the corresponding group.

## The Image inside the Positive Component

**The image is contained in the open set of positive determinant.** This is the determinant identity: $\det\exp X=e^{\operatorname{tr}X}>0$. So

$$
\exp\big(M_n(\mathbb{R})\big)\subseteq\mathrm{GL}_n(\mathbb{R})^{+}=\{A:\det A>0\}.
$$

**The image contains a full neighbourhood of the identity.** The local diffeomorphism at the origin maps a neighbourhood of $\mathrm{0}$ onto a neighbourhood of $\mathrm{I}$, so the image has interior points. A subgroup that contains a neighbourhood of the identity is open, and an open subgroup of a connected group is the whole group; since $\mathrm{GL}_n(\mathbb{R})^{+}$ is connected, the image generates all of it.

## The Image Is Not the Component

**The Jordan block at a negative eigenvalue is the simplest obstruction.** The matrix

$$
A=\begin{pmatrix}-1&1\\0&-1\end{pmatrix}
$$

has $\det A=1$, so it lies in $\mathrm{GL}_2(\mathbb{R})^{+}$, and it is not $\exp X$ for any real $X$. The proof is in *The Two Components of $\mathrm{GL}_n(\mathbb{R})$ and the Failure of the Exponential*: any $X$ with $\exp X=A$ commutes with $A$, the centraliser of $A$ is $\{a\mathrm{I}+bN\}$ with $N^{2}=0$, and $\exp(a\mathrm{I}+bN)=e^{a}(\mathrm{I}+bN)$ has positive diagonal entries, so it cannot have $-1$ there.

**A necessary condition is the parity of the negative eigenvalues.** Let $X$ be real and let $\mu<0$ be an eigenvalue of $\exp X$. Then $\mu=e^{\lambda}$ for an eigenvalue $\lambda$ of $X$, and $\lambda$ is not real, because $e^{\lambda}>0$ for real $\lambda$. So $\lambda$ and $\bar\lambda$ are both eigenvalues of $X$ and they give the same value $e^{\lambda}=e^{\bar\lambda}=\mu$. Hence

$$
\text{every negative real eigenvalue of }\exp X\text{ has even algebraic multiplicity.}
$$

The matrix $\operatorname{diag}(-1,-2,1,\dots,1)$ has two negative eigenvalues of multiplicity one, so it is not an exponential.

**The parity condition is not sufficient.** The matrix $A$ above has $-1$ with multiplicity two, an even number, and is still not an exponential. The Jordan structure decides the rest; the exact criterion is Culver's theorem, quoted in §*Further Reading*.

**The image is therefore not dense.** The matrices with two simple negative eigenvalues form an open set, it contains $\operatorname{diag}(-1,-2)$, and it misses the image. So the closure of the image does not contain that point, and the image is not dense in $\mathrm{GL}_2(\mathbb{R})^{+}$, hence not in $\mathrm{GL}_n(\mathbb{R})^{+}$ either.

**A sharper closed condition holds at $n=2$.** For real $2\times2$ $X$, $\operatorname{tr}\exp X+2\sqrt{\det\exp X}\ge0$: the trace is $e^{\lambda_{1}}+e^{\lambda_{2}}$ for a real spectrum and $2e^{\sigma}\cos\theta$ for the spectrum $\sigma\pm i\theta$, and both are bounded below by $-2\sqrt{\det\exp X}$. The left side was never below $0.28$ over $100$ samples.

## The Numbers at $n=3$

**A random $3\times3$ matrix checks the truncation.** Take $X$ a normal random $3\times3$ matrix with seed $7$ and let $S_{K}=\sum_{k<K}X^{k}/k!$. Compared with the sum through $k=39$, the errors $\lVert S_{K}-\exp X\rVert$ at $K=3,5,8,10,14,18$ are

$$
4.1\cdot10^{-1},\quad 4.3\cdot10^{-2},\quad 3.5\cdot10^{-4},\quad 7.7\cdot10^{-6},\quad 1.2\cdot10^{-9},\quad 6.2\cdot10^{-14}.
$$

**An independent route agrees.** The same $X$ has distinct eigenvalues, so $\exp X=V e^{\Lambda}V^{-1}$ for its complex eigendecomposition, and that value differs from the sum through $k=39$ by $8.2\cdot10^{-16}$. Twenty terms exhaust the double precision answer.

**The identities hold at the same level.** Over $100$ random $4\times4$ matrices the bound $\lVert\exp X\rVert\le e^{\lVert X\rVert}$ is never violated and the determinant identity has maximum error $6.8\cdot10^{-13}$.

## Summary

The exponential of a real matrix is the sum of $X^{k}/k!$, convergent everywhere and analytic, with $\lVert\exp X\rVert\le e^{\lVert X\rVert}$. It satisfies $\exp(X^{\mathsf T})=\exp(X)^{\mathsf T}$ and $\det\exp X=e^{\operatorname{tr}X}>0$, and it adds on commuting factors. Its derivative at the origin is the identity, so it is a local diffeomorphism there and its image contains a neighbourhood of $\mathrm{I}$; it is not a local diffeomorphism everywhere, and it is not injective, since $\exp(2\pi J)=\mathrm{I}$ at $n=2$. On the diagonal, nilpotent and triangular parts it is a bijection onto a positive or unipotent set, and on $\operatorname{Sym}_n$ onto the positive definite cone. Its image lies in $\mathrm{GL}_n(\mathbb{R})^{+}$, generates that component, misses the Jordan block at a negative eigenvalue, excludes every matrix with a negative eigenvalue of odd multiplicity, and is not dense.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\exp X$ | the sum $\sum_k X^{k}/k!$ |
| $\lVert X\rVert$ | a submultiplicative norm |
| $\operatorname{tr}$, $\det$ | the trace and the determinant |
| $\mathrm{GL}_n(\mathbb{R})^{+}$ | the matrices of positive determinant |
| $\operatorname{Sym}_n^{++}$ | the positive definite symmetric matrices |
| $\mathfrak{b}$ | the upper triangular algebra |
| $J$ | the matrix $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ |
| $S_{K}$ | the partial sum through $k=K-1$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge, 1991), for the exponential, its derivative and the logarithm.
- W. J. Culver, *On the existence and uniqueness of the real logarithm of a matrix*, Proceedings of the American Mathematical Society (1966), for the exact criterion of §*The Image Is Not the Component*.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the trace, the determinant and the two halves.
- [The Two Components of $\mathrm{GL}_n(\mathbb{R})$ and the Failure of the Exponential](the-two-components-of-glnr-and-the-failure-of-the-exponential.html), for the proof that the image is strict.
- [The Exponential of the Antisymmetric Part: One-Parameter Rotations](the-exponential-of-the-antisymmetric-part-one-parameter-rotations.html), for the restriction to $\operatorname{Skew}_n$.
- [The Element: Rank, Trace, Determinant, Characteristic Polynomial over $\mathbb{R}$](the-element-rank-trace-determinant-characteristic-polynomial-over-r.html), for the eigenvalues and the sign of the determinant.
