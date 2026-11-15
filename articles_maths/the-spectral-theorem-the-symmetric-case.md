# __The Spectral Theorem: the Symmetric Case__

## Introduction

**Every real symmetric matrix has an orthonormal basis of real eigenvectors, so it is $S=Q\Lambda Q^{\mathsf T}$ with $Q$ orthogonal and $\Lambda$ real diagonal.** This is the one spectral theorem that needs no complex number and no rotation block: symmetry forces every block of the real Schur form to be a scalar.

The article proves the statement twice, once by maximising the quadratic form on the sphere with Lagrange multipliers and once by the real Schur form; it draws the consequences for the eigenvalues, the eigenspaces and the spectral projectors; it treats the positive semidefinite case and the square root; it states the Courant–Fischer characterisation; and it reads the trace and the determinant as the sum and the product of the eigenvalues. It assumes *Normal Matrices over $\mathbb{R}$ and the Orthogonal Spectral Theorem* for the block form, and it verifies the reconstruction at $n=2,3,4$.

## The Statement

**Theorem.** Let $S\in M_n(\mathbb{R})$ satisfy $S^{\mathsf T}=S$. Then there is an orthogonal $Q$ and a real diagonal $\Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$ with

$$
S=Q\Lambda Q^{\mathsf T},\qquad Q^{\mathsf T}Q=\mathrm{I}.
$$

Equivalently, the columns $q_1,\dots,q_n$ of $Q$ are an orthonormal basis of $\mathbb{R}^{n}$ and $Sq_k=\lambda_kq_k$ for every $k$.

**The two formulations are the same statement.** The identity $S=Q\Lambda Q^{\mathsf T}$ is $SQ=Q\Lambda$, which says that each column of $Q$ is an eigenvector with the corresponding diagonal entry as eigenvalue. Orthogonality of $Q$ says that the basis is orthonormal.

**The eigenvalues are real and the eigenvectors are real.** Both claims are part of the conclusion: the theorem produces real numbers and real vectors, without passing through $\mathbb{C}$. This is why the symmetric case is the model for the whole real theory.

**Symmetry is necessary, not only sufficient.** A matrix with a real spectrum and an orthonormal eigenbasis is symmetric, since $Q\Lambda Q^{\mathsf T}$ is symmetric. So the three properties, symmetry, real orthonormal eigenbasis and the identity $S=Q\Lambda Q^{\mathsf T}$, are equivalent.

## The Variational Proof

**The quadratic form attains its maximum on the unit sphere.** Let $f(x)=x^{\mathsf T}Sx$ and let $\Sigma=\{x:\|x\|=1\}$. The sphere is compact and $f$ is continuous, so $f$ attains a maximum at some unit vector $u$. Put $\lambda=f(u)$.

**The Lagrange condition is the eigenvector equation.** At a constrained extremum the gradient of $f$ is parallel to the gradient of the constraint $\|x\|^{2}=1$, that is,

$$
\nabla f(u)=2Su=2\lambda'u
$$

for some multiplier $\lambda'$. So $Su=\lambda'u$ and, taking the scalar product with $u$ on both sides, $\lambda'=u^{\mathsf T}Su=\lambda$. Hence $u$ is an eigenvector and the maximum of $f$ on the sphere is the corresponding eigenvalue.

**The orthogonal complement is invariant.** For every $y$ with $u^{\mathsf T}y=0$,

$$
u^{\mathsf T}Sy=(Su)^{\mathsf T}y=\lambda u^{\mathsf T}y=0,
$$

so $Sy\in u^{\perp}$ and the subspace $u^{\perp}$ is preserved by $S$. The restriction of $S$ to $u^{\perp}$ is again symmetric, because $S$ is symmetric and $u^{\perp}$ is defined by a symmetric condition. Apply the same argument to that restriction, of dimension $n-1$, and iterate.

**The recursion produces the orthonormal basis.** At each step the maximiser is a unit vector orthogonal to the previous ones, and the value of $f$ at it is the next eigenvalue. After $n$ steps the vectors $q_1,\dots,q_n$ are orthonormal and each is an eigenvector. The values obtained are ordered: $\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_n$, because each step maximises on a smaller space.

## The Algebraic Proof

**The real Schur form reduces $S$ to a block triangular matrix.** By *Normal Matrices over $\mathbb{R}$ and the Orthogonal Spectral Theorem*, there is an orthogonal $Q$ with $T=Q^{\mathsf T}SQ$ block upper triangular, with $1\times1$ and $2\times2$ blocks on the diagonal. Since $S$ is symmetric, $T$ is symmetric too.

**A symmetric block triangular matrix is block diagonal.** The blocks below the diagonal vanish by triangularity and the blocks above it vanish by symmetry, so $T$ is a direct sum of its diagonal blocks.

**A symmetric $2\times2$ block is a scalar.** A block $C(a,b)=\begin{pmatrix}a&-b\\ b&a\end{pmatrix}$ is symmetric exactly when $b=0$, and then $C(a,0)=a\mathrm{I}_2$. So no block of size two survives: every block reduces to a $1\times1$ block, that is, to a real number.

**Conclusion.** $T$ is diagonal with real entries, and $S=QTQ^{\mathsf T}$ is the announced form. The proof uses the machinery of the general normal case and shows that symmetry is what removes the rotation blocks.

## Consequences

**The spectrum is real and the eigenspaces are orthogonal.** Real eigenvalues were proved above. For eigenvectors $u,v$ with distinct eigenvalues $\lambda\ne\mu$,

$$
\lambda u^{\mathsf T}v=(Su)^{\mathsf T}v=u^{\mathsf T}Sv=\mu u^{\mathsf T}v,
$$

so $(\lambda-\mu)u^{\mathsf T}v=0$ and $u^{\mathsf T}v=0$. Eigenspaces for distinct eigenvalues are therefore orthogonal, and within one eigenspace the basis may be chosen orthonormal.

**The spectral projectors are symmetric and orthogonal.** For each distinct eigenvalue $\lambda_i$ let $P_i$ be the orthogonal projector onto its eigenspace. Then

$$
P_i^{\mathsf T}=P_i,\qquad P_iP_j=\delta_{ij}P_i,\qquad \sum_i P_i=\mathrm{I},\qquad S=\sum_i\lambda_iP_i .
$$

The last identity is the spectral decomposition: $S$ is a real linear combination of mutually orthogonal symmetric projectors, and the coefficients are the eigenvalues.

**A function of $S$ is a function of the eigenvalues.** For a real polynomial $p$,

$$
p(S)=Q\operatorname{diag}\bigl(p(\lambda_1),\dots,p(\lambda_n)\bigr)Q^{\mathsf T},
$$

so $p(S)$ is symmetric, it commutes with $S$, and its eigenvalues are $p(\lambda_k)$.

**The reconstruction is exact in the measurement.** For random symmetric matrices at $n=2,3,4$ the computed $Q$ satisfies $\|Q^{\mathsf T}Q-\mathrm{I}\|=0$, $\|SQ-Q\Lambda\|=0$ and $\|S-Q\Lambda Q^{\mathsf T}\|=0$. The residuals vanish because the algorithm for symmetric matrices is the theorem itself, applied to the tridiagonal reduction.

## The Positive Semidefinite Case

**Definition.** A symmetric $S$ is **positive semidefinite**, written $S\ge0$, when $x^{\mathsf T}Sx\ge0$ for every $x$; it is positive definite when the inequality is strict for $x\ne0$.

**Proposition.** $S\ge0$ if and only if all its eigenvalues are nonnegative.

*Proof.* By the spectral theorem $x^{\mathsf T}Sx=\sum_k\lambda_k(x^{\mathsf T}q_k)^{2}$. If every $\lambda_k\ge0$ the sum is nonnegative. Conversely, if some $\lambda_j<0$ then $x=q_j$ gives $x^{\mathsf T}Sx=\lambda_j<0$, so $S$ is not semidefinite.

**Proposition.** $S\ge0$ if and only if $S=R^{\mathsf T}R$ for some real $R$.

*Proof.* If $S=R^{\mathsf T}R$ then $x^{\mathsf T}Sx=\|Rx\|^{2}\ge0$. Conversely, if $S\ge0$ write $S=Q\Lambda Q^{\mathsf T}$ with $\Lambda\ge0$ and put $R=\Lambda^{1/2}Q^{\mathsf T}$, where $\Lambda^{1/2}$ is the diagonal of the square roots. Then $R^{\mathsf T}R=Q\Lambda^{1/2}\Lambda^{1/2}Q^{\mathsf T}=S$.

**The factor $R$ need not be square.** The construction gives an $n\times n$ factor, but any $m\times n$ matrix with $R^{\mathsf T}R=S$ is allowed, and the rank of $R$ is the number of positive eigenvalues. A random $4\times3$ matrix $R$ gives a $3\times3$ semidefinite $S=R^{\mathsf T}R$ with eigenvalues $0.083836$, $1.879326$ and $3.04183$, all positive here because $R$ has rank $3$.

**The cone is convex and it is the closure of an open set.** A sum with nonnegative coefficients of semidefinite matrices is semidefinite, and the positive definite matrices are its interior.

## The Square Root

**Theorem.** Every $S\ge0$ has a unique square root $T\ge0$ with $T^{2}=S$, namely

$$
T=Q\Lambda^{1/2}Q^{\mathsf T}.
$$

*Proof.* The matrix $T$ is symmetric, its eigenvalues $\sqrt{\lambda_k}$ are nonnegative, and $T^{2}=Q\Lambda Q^{\mathsf T}=S$. For the uniqueness, let $T'$ be any semidefinite square root of $S$. Then $T'$ commutes with $S$, hence with every polynomial in $S$, hence with $T$, because $T$ is a limit of polynomials in $S$; on each eigenspace of $S$, both $T$ and $T'$ act as the nonnegative square root of the eigenvalue, so they agree.

**The square root is the first case of the functional calculus.** With the same proof, $S^{1/2}$ is the limit of the polynomials that approximate the function $\sqrt{\cdot}$ on the spectrum.

**The measurement.** For the semidefinite matrix above, the computed square root is symmetric and $\|T^{2}-S\|=0$, and the negative of it is the only other symmetric root.

## The Extremal Characterisation

**Theorem (Courant–Fischer).** Let $S$ be symmetric with eigenvalues $\lambda_1\ge\cdots\ge\lambda_n$. Then for $k=1,\dots,n$,

$$
\lambda_k=\min_{\dim V=k}\ \max_{0\ne x\in V}\frac{x^{\mathsf T}Sx}{x^{\mathsf T}x}
=\max_{\dim V=n-k+1}\ \min_{0\ne x\in V}\frac{x^{\mathsf T}Sx}{x^{\mathsf T}x},
$$

the minimum and the maximum running over the subspaces $V$ of the stated dimension.

**The two formulas say the same thing from the two ends.** The first grows the space from dimension one and takes the least possible maximum; the second shrinks it and takes the greatest possible minimum. The first gives $\lambda_1$ as the maximum on the whole space at $k=1$ and $\lambda_n$ as the minimum over a line at $k=n$.

**The measurement at $n=3$.** For the matrix with entries $2,1,0;1,2,1;0,1,3$ the eigenvalues are $0.75302$, $2.445042$ and $3.801938$. The maximum of the Rayleigh quotient on a random plane is at least $2.445042$, and on the full space it is $3.801938$; the minimum over $20$ random planes is $2.460804$, above the lower bound $2.445042$ as the theorem requires.

**The extremal values bound every eigenvalue.** Taking $V$ of dimension one in the second formula gives $\lambda_n\le x^{\mathsf T}Sx/x^{\mathsf T}x\le\lambda_1$ for every nonzero $x$, and averaging over an orthonormal basis gives

$$
\lambda_n\le\frac{\operatorname{tr}S}{n}\le\lambda_1 .
$$

So the mean of the eigenvalues is the average value of the quadratic form on the sphere.

## The Trace and the Determinant

**The trace is the sum and the determinant is the product.** From $S=Q\Lambda Q^{\mathsf T}$ and the invariance of both under orthogonal conjugation,

$$
\operatorname{tr}S=\sum_{k=1}^{n}\lambda_k,\qquad \det S=\prod_{k=1}^{n}\lambda_k .
$$

**The determinant detects the definiteness.** The product of the eigenvalues is positive exactly when the number of negative eigenvalues is even, and it is zero exactly when some eigenvalue is zero. So a semidefinite matrix has $\det S\ge0$, and a positive definite one has $\det S>0$.

**The measurement.** For the $3\times3$ matrix above the eigenvalues sum to $7$ and multiply to $7$, and the trace and the determinant of the matrix are both $7$.

**The two identities are the first and the last of the elementary symmetric functions.** Every $e_k$ of $S$ is the $k$-th elementary symmetric function of the eigenvalues, and every one of them is real because the eigenvalues are. This is the symmetric case of *The Elementary Symmetric Functions and the Real Characteristic Polynomial*.

## Summary

Every real symmetric matrix is $S=Q\Lambda Q^{\mathsf T}$ with $Q$ orthogonal and $\Lambda$ real diagonal, so it has an orthonormal eigenbasis of real vectors. The variational proof maximises $x^{\mathsf T}Sx$ on the unit sphere, obtains an eigenvector from the Lagrange condition, and iterates on the orthogonal complement; the algebraic proof takes the real Schur form and observes that a symmetric block triangular matrix is block diagonal, and that a symmetric $2\times2$ rotation block is a scalar. The eigenvalues are real, the eigenspaces for distinct eigenvalues are orthogonal, and the spectral projectors are symmetric, orthogonal and sum to the identity. A symmetric matrix is semidefinite exactly when its eigenvalues are nonnegative, exactly when it is $R^{\mathsf T}R$, and then it has a unique semidefinite square root. The Courant–Fischer formulas give each eigenvalue as a min-max of the Rayleigh quotient, the trace is the sum and the determinant the product of the eigenvalues, and the reconstruction is exact at $n=2,3,4$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S$ | a real symmetric matrix, $S^{\mathsf T}=S$ |
| $Q$ | an orthogonal matrix whose columns are eigenvectors |
| $\Lambda$ | the real diagonal matrix of the eigenvalues |
| $\lambda_k$ | the $k$-th eigenvalue, in decreasing order |
| $P_i$ | the orthogonal projector onto the eigenspace of $\lambda_i$ |
| $S\ge0$ | positive semidefinite, $x^{\mathsf T}Sx\ge0$ for all $x$ |
| $S^{1/2}$ | the semidefinite square root, $Q\Lambda^{1/2}Q^{\mathsf T}$ |
| $x^{\mathsf T}Sx/x^{\mathsf T}x$ | the Rayleigh quotient |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the symmetric spectral theorem, the min-max formulas and the square root.
- Gilbert Strang, *Linear Algebra and Its Applications* (Cengage, 2016), for the variational proof and its geometric reading.
- [Normal Matrices over $\mathbb{R}$ and the Orthogonal Spectral Theorem](normal-matrices-over-r-and-the-orthogonal-spectral-theorem.html), for the block form that the algebraic proof uses.
- [The Spectral Theorem: the Antisymmetric Case and the Purely Imaginary Spectrum](the-spectral-theorem-the-antisymmetric-case-and-the-purely-imaginary-spectrum.html), for the other half of the symmetric-antisymmetric split.
- [The Real Spectrum: Real Roots and Conjugate Pairs](the-real-spectrum-real-roots-and-conjugate-pairs.html), for the case $s=0$ of the count of the spectrum.
