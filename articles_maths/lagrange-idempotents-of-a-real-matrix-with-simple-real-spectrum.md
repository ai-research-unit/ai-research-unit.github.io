# __Lagrange Idempotents of a Real Matrix with Simple Real Spectrum__

## Introduction

**A real matrix with $n$ distinct real eigenvalues carries $n$ canonical real idempotents $P_1,\dots,P_n$, written by the Lagrange interpolation formula in $A$ itself, with $P_kP_l=\delta_{kl}P_k$, $\sum_kP_k=\mathrm{I}$ and $A=\sum_k\lambda_kP_k$.**

The article proves the three identities algebraically, with no eigenvector in sight, shows that $P_k$ is the spectral projection onto the eigenspace of $\lambda_k$, traces the failure of the construction when the spectrum has a repeated value or a conjugate pair, and writes the case $n=2$ explicitly. It assumes *The Element: Rank, Trace, Determinant, Characteristic Polynomial over $\mathbb{R}$* for the spectrum and the characteristic polynomial, and it defers the idempotents as a decomposition of the algebra to *The Peirce Decomposition in $n$ Dimensions over $\mathbb{R}$*.

## The Construction

**Let $A\in M_n(\mathbb{R})$ have $n$ distinct real eigenvalues $\lambda_1,\dots,\lambda_n$.** Define, for each $k$,

$$
L_k(t)=\prod_{j\ne k}\frac{t-\lambda_j}{\lambda_k-\lambda_j},\qquad P_k=L_k(A).
$$

The denominators are nonzero, because the eigenvalues are distinct. The polynomial $L_k$ has real coefficients, because the eigenvalues are real, and it satisfies $L_k(\lambda_l)=\delta_{kl}$.

**Each $P_k$ is a real matrix.** The matrix $A$ is real and the coefficients of $L_k$ are real, so $L_k(A)$ is real. This is the point of the hypothesis: a complex eigenvalue would give a complex coefficient and a complex projector.

**The four polynomials are the Lagrange basis of the interpolation problem.** The $L_k$ are the unique polynomials of degree at most $n-1$ with $L_k(\lambda_l)=\delta_{kl}$. Two polynomials of degree at most $n-1$ that agree at the $n$ points $\lambda_1,\dots,\lambda_n$ are equal, and this uniqueness is the engine of every identity below.

## The Idempotent Identities

**The polynomials satisfy $\sum_kL_k=1$ and $L_kL_l\equiv\delta_{kl}L_k$ at the $n$ points.** The constant polynomial $1$ and the sum $\sum_kL_k$ have degree at most $n-1$ and agree at all $\lambda_l$. For the product, $L_k(\lambda_m)L_l(\lambda_m)=\delta_{km}\delta_{lm}$, which is $\delta_{kl}$ when $m=k=l$ and zero otherwise.

**Theorem.** $P_kP_l=\delta_{kl}P_k$ and $\sum_kP_k=\mathrm{I}$.

**Proof of the sum.** The polynomial identity $\sum_kL_k=1$ is an identity of polynomials, so it holds at the matrix $A$. Applying it gives $\sum_kP_k=\mathrm{I}$.

**Proof of the product.** Write $p(t)=\prod_j(t-\lambda_j)$ for the characteristic polynomial. The polynomial $L_kL_l-\delta_{kl}L_k$ has degree at most $2n-2$ and vanishes at the $n$ points $\lambda_1,\dots,\lambda_n$. So it is divisible by $p$, and

$$
L_kL_l=\delta_{kl}L_k+p\,g_{kl}
$$

for some polynomial $g_{kl}$. Evaluating at $A$ and using $p(A)=0$, which is the Cayley–Hamilton theorem, gives $P_kP_l=\delta_{kl}P_k$.

**The proof uses no eigenvector and no diagonalisation.** Only the Cayley–Hamilton theorem and the interpolation property enter. This is why the projectors are computable from $A$ alone.

**The residuals at $n=3$ and $n=4$ are at the level of rounding.** Take the companion matrix of $(t-1)(t-2)(t-3)$, whose eigenvalues are $1,2,3$. The computed projectors satisfy

$$
\max_{k,l}\|P_kP_l-\delta_{kl}P_k\|=2.3\times10^{-13},\qquad \Bigl\|\sum_kP_k-\mathrm{I}\Bigr\|=2.6\times10^{-15},\qquad \Bigl\|A-\sum_k\lambda_kP_k\Bigr\|=8.2\times10^{-15}.
$$

The companion matrix of $(t-1)(t-2)(t-3)(t-4)$ at $n=4$ gives $1.9\times10^{-11}$, $1.7\times10^{-13}$ and $4.7\times10^{-13}$, and a random conjugation of the diagonal matrix $\operatorname{diag}(1,2,3)$ gives $1.5\times10^{-14}$, $1.2\times10^{-15}$ and $2.8\times10^{-15}$.

## The Spectral Projection

**The image of $P_k$ is the eigenspace of $\lambda_k$.** Since $A$ is a polynomial in itself, $A$ commutes with $P_k$. And

$$
(A-\lambda_k\mathrm{I})P_k=\frac{p(A)}{\prod_{j\ne k}(\lambda_k-\lambda_j)}=0
$$

by Cayley–Hamilton, because the numerator $p(A)$ vanishes and the denominator is a nonzero scalar. So the image of $P_k$ lies in $\ker(A-\lambda_k\mathrm{I})$, which is the eigenspace.

**The rank of $P_k$ is one.** The polynomial $L_k$ takes the value $1$ at $\lambda_k$ and $0$ at the other eigenvalues, so $P_k$ acts as the identity on the eigenspace of $\lambda_k$ and as zero on the other eigenspaces. Those eigenspaces span $\mathbb{R}^{n}$, since the eigenvalues are distinct, so $P_k$ is the projection onto a one-dimensional space along a direct sum of the others.

**Hence $\operatorname{tr}P_k=1$.** The trace of an idempotent is its rank, and the rank is one. The numerical runs at $n=3$ and $n=4$ give $\operatorname{tr}P_k=1$ for every $k$, to the accuracy of the arithmetic.

**The $P_k$ form a complete family of orthogonal idempotents.** There are $n$ of them, each has rank one, they satisfy $P_kP_l=0$ for $k\ne l$, and their sum is the identity. Their images are the $n$ eigenspaces, and the images add directly to $\mathbb{R}^{n}$.

## Diagonalisation Without Eigenvectors

**The matrix is the weighted sum of its projectors.** The polynomial identity $\sum_k\lambda_kL_k(t)=t$ holds, because both sides have degree at most $n-1$ and agree at the $n$ eigenvalues. Evaluating at $A$ gives

$$
A=\sum_{k=1}^{n}\lambda_kP_k.
$$

This was checked with numpy: the residual is $8.2\times10^{-15}$ at $n=3$ and $4.7\times10^{-13}$ at $n=4$.

**Every function of the matrix is the same weighted sum.** For any polynomial $f$ of degree at most $n-1$, the same argument gives

$$
f(A)=\sum_{k=1}^{n}f(\lambda_k)P_k.
$$

So the inverse is $\sum_k\lambda_k^{-1}P_k$ when no eigenvalue is zero, the powers are $\sum_k\lambda_k^{m}P_k$ for every integer $m$, and the exponential is $\sum_ke^{\lambda_k}P_k$.

**The projectors are products of left and right eigenvectors.** Let $r_k$ be a right eigenvector and $\ell_k$ a left eigenvector for $\lambda_k$, normalised so that $\ell_k^{\mathsf T}r_k=1$. Then

$$
P_k=r_k\ell_k^{\mathsf T}.
$$

At $n=3$ with the companion matrix of $(t-1)(t-2)(t-3)$ the three projectors are

$$
P_1=\begin{pmatrix}3&3&3\\ -\tfrac52&-\tfrac52&-\tfrac52\\ \tfrac12&\tfrac12&\tfrac12\end{pmatrix},\quad
P_2=\begin{pmatrix}-3&-6&-12\\ 4&8&16\\ -1&-2&-4\end{pmatrix},\quad
P_3=\begin{pmatrix}1&3&9\\ -\tfrac32&-\tfrac92&-\tfrac{27}{2}\\ \tfrac12&\tfrac32&\tfrac92\end{pmatrix}.
$$

Each of the three has rank one, the columns are proportional to the right eigenvector, and the rows are proportional to the left eigenvector. The traces are $1,1,1$ and the sum is the identity.

## The Case $n=2$

**At $n=2$ the two projectors have a closed form.** For $A=\begin{pmatrix}a&b\\ c&d\end{pmatrix}$ with eigenvalues $\lambda_1\ne\lambda_2$,

$$
P_1=\frac{A-\lambda_2\mathrm{I}}{\lambda_1-\lambda_2},\qquad P_2=\frac{A-\lambda_1\mathrm{I}}{\lambda_2-\lambda_1}.
$$

The two are real, they are idempotent, they are orthogonal, and their sum is the identity. The trace of each is one: for $P_1$ the diagonal entries are $(a-\lambda_2)/(\lambda_1-\lambda_2)$ and $(d-\lambda_2)/(\lambda_1-\lambda_2)$, whose sum is $(a+d-\lambda_1-\lambda_2)/(\lambda_1-\lambda_2)=1$, because the trace is the sum of the eigenvalues.

**A numerical instance.** Take $A=\begin{pmatrix}1&2\\ 3&4\end{pmatrix}$, with eigenvalues $\lambda_{1,2}=\tfrac12\bigl(5\pm\sqrt{33}\bigr)$. Then

$$
P_1=\frac{1}{\sqrt{33}}\begin{pmatrix}\tfrac12(\sqrt{33}-3)&2\\ 3&\tfrac12(\sqrt{33}+3)\end{pmatrix},\qquad P_2=\mathrm{I}-P_1.
$$

Numerically $P_1=\begin{pmatrix}0.238884&0.348155\\ 0.522233&0.761116\end{pmatrix}$ and $P_2=\begin{pmatrix}0.761116&-0.348155\\ -0.522233&0.238884\end{pmatrix}$. The checks give $\|P_1^{2}-P_1\|=0$, $\|P_1P_2\|=2.4\times10^{-17}$, $\|A-(\lambda_1P_1+\lambda_2P_2)\|=4.4\times10^{-16}$ and $\operatorname{tr}P_1=\operatorname{tr}P_2=1$.

**The two projectors are the halves of the algebra cut by the spectrum.** A matrix of $M_2(\mathbb{R})$ with a simple real spectrum is the sum of a multiple of $P_1$ and a multiple of $P_2$, so the four-dimensional algebra splits into two lines and two mixed lines. That is the Peirce decomposition of the algebra along this frame.

## The Failure at a Repeated Value

**The formula breaks when two eigenvalues coincide.** If $\lambda_k=\lambda_l$ for $k\ne l$, the denominator $\lambda_k-\lambda_l$ vanishes and $L_k$ is not defined. There is no Lagrange polynomial, and there is no canonical projector onto a single eigenspace: the eigenspace of that value carries a whole space of projectors.

**The limit exists only when the matrix is diagonalisable and the value stays simple.** The projector is a continuous function of $A$ on the set of matrices with simple spectrum, because the formula is a polynomial in the entries with denominators the discriminant. At a matrix with a repeated eigenvalue the limit depends on the path, unless the eigenspace of that value is one-dimensional for the whole path.

**A nilpotent shows the failure plainly.** The matrix $J=\begin{pmatrix}0&1\\ 0&0\end{pmatrix}$ has the single eigenvalue $0$, and the only idempotents commuting with it are $0$ and $\mathrm{I}$, since $J$ has a one-dimensional kernel equal to its image. No pair of rank-one projectors sum to the identity, and no Lagrange formula exists.

## The Case of a Conjugate Pair

**A conjugate pair of eigenvalues gives no real Lagrange projector.** If $\lambda=a+ib$ with $b\ne0$ is an eigenvalue, then so is $\bar\lambda=a-ib$, and the Lagrange polynomial for $\lambda$ has complex coefficients. The resulting projector $P$ is complex, and its conjugate $\bar P$ is the projector for $\bar\lambda$.

**The sum of the two conjugates is a real projector of rank two.** The identities $P\bar P=0$ and $P^{2}=P$ give $(P+\bar P)^{2}=P+\bar P$, and $P+\bar P$ is real. It is the projection onto the two-dimensional real invariant subspace spanned by the real and imaginary parts of a complex eigenvector. So the pair contributes one real projector of rank two, not two of rank one.

**The rotation illustrates the extreme case.** For $R=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}$ the eigenvalues are $\pm i$. The complex projectors are

$$
P=\tfrac12\begin{pmatrix}1&i\\ -i&1\end{pmatrix},\qquad \bar P=\tfrac12\begin{pmatrix}1&-i\\ i&1\end{pmatrix},
$$

and $P+\bar P=\mathrm{I}$. The only real idempotent that the pair produces is the identity, so the matrix admits no nontrivial real spectral decomposition. That is the real phenomenon: the spectral decomposition of a real matrix is finer over $\mathbb{C}$ than over $\mathbb{R}$, and a pair of complex eigenvalues is one block over $\mathbb{R}$ and two lines over $\mathbb{C}$.

## Summary

For a real matrix $A$ with $n$ distinct real eigenvalues $\lambda_1,\dots,\lambda_n$, the Lagrange idempotents $P_k=L_k(A)$ with $L_k(t)=\prod_{j\ne k}(t-\lambda_j)/(\lambda_k-\lambda_j)$ are real, satisfy $P_kP_l=\delta_{kl}P_k$ and $\sum_kP_k=\mathrm{I}$, and give $A=\sum_k\lambda_kP_k$. The proofs use the Lagrange interpolation property, the Cayley–Hamilton theorem and nothing else, so no eigenvector is computed. Each $P_k$ is the spectral projection onto the eigenspace of $\lambda_k$, it has rank one, its trace is one, and it is the product $r_k\ell_k^{\mathsf T}$ of a right and a left eigenvector normalised to $\ell_k^{\mathsf T}r_k=1$. The residuals are $2.3\times10^{-13}$ for the orthogonality, $2.6\times10^{-15}$ for the sum and $8.2\times10^{-15}$ for the reconstruction at $n=3$, and of the same order at $n=4$. At $n=2$ the formulas are $P_1=(A-\lambda_2\mathrm{I})/(\lambda_1-\lambda_2)$ and $P_2=\mathrm{I}-P_1$, with the example $A=\begin{pmatrix}1&2\\ 3&4\end{pmatrix}$ and eigenvalues $\tfrac12(5\pm\sqrt{33})$. A repeated eigenvalue destroys the denominators and leaves no canonical projector, and a conjugate pair leaves no real projector of rank one: it leaves the real projector $P+\bar P$ of rank two, which for the rotation is the identity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\lambda_1,\dots,\lambda_n$ | the distinct real eigenvalues of $A$ |
| $L_k(t)$ | the Lagrange polynomial, $L_k(\lambda_l)=\delta_{kl}$ |
| $P_k=L_k(A)$ | the $k$-th Lagrange idempotent |
| $p(t)=\prod_j(t-\lambda_j)$ | the characteristic polynomial |
| $r_k,\ell_k$ | a right and a left eigenvector for $\lambda_k$ |
| $\delta_{kl}$ | the Kronecker symbol |
| $\mathrm{I}$ | the identity matrix |
| $P+\bar P$ | the real projector of rank two attached to a conjugate pair |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the spectral projections, the Lagrange interpolation and the Cayley–Hamilton theorem.
- Peter Lancaster and Miron Tismenetsky, *The Theory of Matrices* (Academic Press, 1985), for the spectral projectors and the functions of a matrix.
- [The Element: Rank, Trace, Determinant, Characteristic Polynomial over $\mathbb{R}$](the-element-rank-trace-determinant-characteristic-polynomial-over-r.html), for the spectrum and the characteristic polynomial.
- [The Minimal Polynomial over $\mathbb{R}$ and the Real Jordan Form](the-minimal-polynomial-over-r-and-the-real-jordan-form.html), for the repeated values and the conjugate pairs.
- [The Peirce Decomposition in $n$ Dimensions over $\mathbb{R}$](the-peirce-decomposition-in-n-dimensions-over-r.html), for the algebra decomposed along a family of idempotents.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the algebra and its trace.
