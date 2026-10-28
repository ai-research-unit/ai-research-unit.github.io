# __Spectral Theory and the Spectral Projectors__

## Introduction

The spectral theorem for Hermitian matrices states that a Hermitian matrix $A=A^*$ has an orthonormal basis of eigenvectors and real eigenvalues:

$$
A=\sum_{k=1}^{5}\lambda_kP_k,\qquad \lambda_k\in\mathbb{R},
$$

where the $P_k$ are the **orthogonal spectral projectors**:

$$
P_k^2=P_k,\qquad P_kP_l=\delta_{kl}P_k,\qquad \sum_kP_k=I,\qquad P_k^*=P_k .
$$

The projectors are polynomials in $A$ (the Lagrange interpolation at the spectrum), and they give the **functional calculus** $f(A)=\sum_kf(\lambda_k)P_k$ for every continuous function $f$ on the spectrum. The **operator norm** of a Hermitian matrix is its spectral radius,

$$
\|A\|_{\mathrm{op}}=\max_k|\lambda_k|,
$$

and the **positive semidefinite order** is read on the eigenvalues: $A\ge0$ iff all $\lambda_k\ge0$. The square root $A^{1/2}=\sum_k\sqrt{\lambda_k}P_k$ and the absolute value $|A|=(A^*A)^{1/2}$ follow.

The article proves the Hermitian spectral theorem by the eigenvector induction, constructs the spectral projectors, and develops the operator norm, the positive semidefinite order and the functional calculus. It then treats the **normal** case (the $*$-unitary matrices, including the root $H=\sum_k\zeta_kE_{kk}$) and the **general** case: a matrix with simple spectrum has Lagrange projectors, but they are not orthogonal unless the matrix is normal for the standard form. The distinction is the difference between the algebraic spectral decomposition of the root and the Hilbert-space spectral theorem.

The article assumes the Hermitian form, the Frobenius form and the trace. It uses the determinant and the characteristic polynomial; the general case uses the Jordan decomposition through the Dunford calculus, while the Hermitian case uses only the spectral theorem. The polar decomposition and the singular value decomposition are the next article.

## The Spectral Theorem for Hermitian Matrices

### Eigenvalues and Eigenvectors

**Theorem.** Let $A\in M_5(\mathbb{C})$ be Hermitian, $A^*=A$. Then every eigenvalue of $A$ is real.

**Proof.** Let $Ax=\lambda x$ with $x\ne0$. Then

$$
\lambda\|x\|^2=\langle x,Ax\rangle=\langle Ax,x\rangle=\bar\lambda\|x\|^2,
$$

because $A$ is Hermitian and the form is conjugate-symmetric. Since $\|x\|^2>0$, $\lambda=\bar\lambda$, so $\lambda\in\mathbb{R}$.

**Corollary.** The characteristic polynomial of a Hermitian matrix has real coefficients and real roots. The trace and the determinant are real.

**Proof.** The eigenvalues are real; the coefficients are the elementary symmetric functions of the eigenvalues, hence real; the trace is the sum and the determinant the product.

**Theorem.** Eigenvectors of a Hermitian matrix for distinct eigenvalues are orthogonal.

**Proof.** Let $Ax=\lambda x$, $Ay=\mu y$ with $\lambda\ne\mu$. Then

$$
\lambda\langle x,y\rangle=\langle Ax,y\rangle=\langle x,Ay\rangle=\mu\langle x,y\rangle,
$$

so $(\lambda-\mu)\langle x,y\rangle=0$, and $\langle x,y\rangle=0$.

### The Eigenvector Induction

**Theorem (spectral theorem, Hermitian case).** A Hermitian matrix $A\in M_5(\mathbb{C})$ has an orthonormal basis of eigenvectors, and real eigenvalues.

**Proof.** The characteristic polynomial has a complex root $\lambda$, hence an eigenvector $x\ne0$; by the first theorem $\lambda$ is real. Normalize $x$. The orthogonal complement $x^\perp$ is invariant under $A$: if $\langle w,x\rangle=0$, then

$$
\langle Aw,x\rangle=\langle w,Ax\rangle=\lambda\langle w,x\rangle=0 .
$$

The restriction of $A$ to $x^\perp\cong\mathbb{C}^4$ is Hermitian, so by induction it has an orthonormal basis of eigenvectors. Together with $x$, this gives an orthonormal basis of $\mathbb{C}^5$.

**Corollary.** $A$ is unitarily diagonalizable: $A=UDU^*$ with $U$ $*$-unitary and $D=\operatorname{diag}(\lambda_1,\dots,\lambda_5)$ real.

**Proof.** The orthonormal eigenbasis is the columns of $U$; the diagonal entries are the eigenvalues.

**Corollary.** The eigenspaces of $A$ are mutually orthogonal and span $\mathbb{C}^5$; the orthogonal projection onto an eigenspace is a polynomial in $A$.

**Proof.** The eigenspaces are the spans of the orthonormal eigenvectors; the projection is the Lagrange polynomial evaluated at $A$.

### The Spectral Decomposition

**Theorem.** A Hermitian matrix $A$ has the spectral decomposition

$$
A=\sum_{k=1}^{r}\lambda_kP_k,
$$

where $\lambda_1,\dots,\lambda_r$ are the distinct eigenvalues, $P_k$ is the orthogonal projection onto the $\lambda_k$-eigenspace, and

$$
P_kP_l=\delta_{kl}P_k,\qquad \sum_kP_k=I,\qquad P_k^*=P_k,\qquad AP_k=\lambda_kP_k .
$$

**Proof.** The spectral theorem gives the orthonormal eigenbasis; group the eigenvectors by eigenvalue; $P_k$ is the sum of the rank-one projections onto the basis vectors of the $\lambda_k$-eigenspace. The identities follow from the orthonormality; $P_k^*=P_k$ is the orthogonality of the projection.

**Corollary.** The rank of $P_k$ is the multiplicity $m_k$ of $\lambda_k$; the trace of $P_k$ is $m_k$; the trace of $A$ is $\sum_km_k\lambda_k$.

**Proof.** The trace of an orthogonal projection is its rank, the dimension of the eigenspace; the trace of $A$ is the sum of the eigenvalues with multiplicity.

**Corollary.** If the spectrum is simple, the projectors are rank one and are the Lagrange projectors

$$
P_k=\prod_{l\ne k}\frac{A-\lambda_lI}{\lambda_k-\lambda_l}.
$$

**Proof.** The Lagrange polynomial is $1$ at $\lambda_k$ and $0$ at the other eigenvalues; evaluated at $A$, it is the spectral projector.

## The Spectral Projectors

### The Lagrange Projectors

**Definition.** For a matrix $A$ with simple spectrum $\lambda_1,\dots,\lambda_5$, the **Lagrange projectors** are

$$
P_k=\prod_{l\ne k}\frac{A-\lambda_lI}{\lambda_k-\lambda_l}.
$$

**Theorem.** The Lagrange projectors are idempotent, orthogonal and complete:

$$
P_k^2=P_k,\qquad P_kP_l=\delta_{kl}P_k,\qquad \sum_kP_k=I,\qquad A=\sum_k\lambda_kP_k .
$$

They are polynomial in $A$ of degree $4$, with coefficients rational in the eigenvalues.

**Proof.** The Lagrange polynomial $L_k(t)=\prod_{l\ne k}(t-\lambda_l)/(\lambda_k-\lambda_l)$ satisfies $L_k(\lambda_j)=\delta_{kj}$; the polynomial identities at the five distinct eigenvalues give the projector identities after evaluating at $A$. The degree is $4$; the coefficients are rational in the $\lambda_k$.

**Proposition.** At a simple spectrum the minimal polynomial equals the characteristic polynomial,

$$
\mu_A(t)=\chi_A(t)=\prod_{k=1}^{5}(t-\lambda_k),
$$

and the Jordan form is diagonal. For a general matrix, the minimal polynomial is $\prod_\lambda(t-\lambda)^{m_\lambda}$, where $m_\lambda$ is the size of the largest Jordan block of $\lambda$; the Jordan decomposition is treated in *The Element, the Coordinates and the Trace*.

**Proof.** The characteristic polynomial has the five distinct roots $\lambda_k$, so it is squarefree; a squarefree annihilating polynomial of degree $5$ is the minimal polynomial, and the matrix is diagonalizable. The general formula is the standard Jordan description.

**Corollary.** The Lagrange projectors are the spectral projectors of the algebra for any simple spectrum. They are not necessarily self-adjoint: **all** of them are self-adjoint iff $A$ is normal for the standard form. An individual Lagrange projector can be self-adjoint for a non-normal $A$.

**Proof.** The projectors are determined by the spectral decomposition. All of them are self-adjoint iff every eigenspace is orthogonal to the sum of the others, i.e., iff the eigenvectors are mutually orthogonal, which is normality. A single projector requires only its own eigenvector to be orthogonal to the other eigenspaces.

### The Orthogonal Projectors

**Proposition.** For a Hermitian $A$, the Lagrange projectors are self-adjoint and are the orthogonal projections onto the eigenspaces.

**Proof.** The eigenvectors of a Hermitian matrix are orthogonal; the Lagrange projector is the projection onto the eigenspace along the sum of the other eigenspaces, which is the orthogonal projection because the eigenspaces are orthogonal.

**Corollary.** The spectral projectors of a Hermitian matrix are the orthogonal projections of the Hilbert space; they satisfy $P_k^*=P_k$ and $\|P_k\|_{\mathrm{op}}=1$ for a nonzero eigenspace.

**Proof.** An orthogonal projection has norm $1$ unless it is zero; the eigenspaces are nonzero by definition.

### The Root Versus the Hermitian Case

**Proposition.** The standard root $H=\sum_k\zeta_kE_{kk}$ is $*$-unitary, hence normal; its spectral projectors are $E_{kk}$, and they are orthogonal for the standard Hermitian form. A general conjugate $gHg^{-1}$ has spectral projectors $gE_{kk}g^{-1}$, which are idempotent but not self-adjoint unless the columns of $g$ are mutually orthogonal.

**Proof.** $H$ is diagonal with entries of modulus $1$, so $H^*H=I$; it is normal. The spectral projectors of a diagonal matrix are the diagonal units $E_{kk}$, which are orthogonal. Conjugation sends the projectors to $gE_{kk}g^{-1}$; this is self-adjoint iff $gE_{kk}g^{-1}=g^{-*}E_{kk}g^*$ for all $k$, which holds iff $g^*g$ is diagonal, i.e., the columns of $g$ are mutually orthogonal.

**Corollary.** The root orbit has a distinguished point $H$ at which the spectral projectors are orthogonal; at a general point, the projectors are the conjugate idempotents and need not be orthogonal for the standard form. The algebraic spectral decomposition is gauge-covariant; the Hilbert-space orthogonality is not.

**Proof.** The conjugation by $g$ is the gauge; it preserves the idempotent identities but not, in general, the self-adjointness. The standard point $H$ is the diagonal representative.

**Remark.** **The Lagrange projectors and the orthogonal spectral projectors are the same only for normal matrices.** The root $H$ is $*$-unitary, so at the standard point they coincide with $E_{kk}$; a general matrix with simple spectrum has Lagrange projectors that are not orthogonal. The spectral theorem is a theorem about normal matrices; the Lagrange decomposition is a theorem about any simple spectrum. The two must not be conflated.

## The Normal Case

### $*$-Unitary Diagonalization

**Theorem.** A matrix $A$ is normal, $A^*A=AA^*$, if and only if it is unitarily diagonalizable: $A=UDU^*$ with $U$ $*$-unitary and $D$ diagonal.

**Proof.** If $A=UDU^*$, then $A^*A=UD^*DU^*=UDD^*U^*=AA^*$. Conversely, if $A$ is normal, write $A=B+iC$ with $B=(A+A^*)/2$ and $C=(A-A^*)/(2i)$ Hermitian. The normality is equivalent to $[B,C]=0$; commuting Hermitian matrices are simultaneously diagonalizable by a $*$-unitary matrix (apply the Hermitian spectral theorem on each eigenspace of $B$, where $C$ acts Hermitian). Then $A$ is diagonal in the common eigenbasis.

**Corollary.** The eigenvalues of a normal matrix are complex; the eigenvectors are orthogonal; the spectral projectors are orthogonal.

**Proof.** The $*$-unitary diagonalization gives an orthonormal eigenbasis; the eigenspaces are orthogonal; the projections are self-adjoint.

**Corollary.** The root $H$ is normal ($*$-unitary), and the spectral theorem applies to it at the standard point. The general element of the root orbit is diagonalizable but need not be normal for the standard form.

**Proof.** $H$ is $*$-unitary; a general conjugate $gHg^{-1}$ is diagonalizable. It is normal for the standard form when the eigenbasis is orthonormal, i.e., when the columns of $g$ are mutually orthogonal; this fails for a general $g$.

### The Spectral Measure

**Definition.** For a normal $A$, the **spectral measure** is the projection-valued measure on the finite spectrum,

$$
E(\Omega)=\sum_{\lambda_k\in\Omega}P_k,
$$

for a subset $\Omega$ of the spectrum.

**Proposition.** $E$ is multiplicative, $E(\Omega\cap\Omega')=E(\Omega)E(\Omega')$, and $A=\sum_k\lambda_kE(\{\lambda_k\})$. The functional calculus is

$$
f(A)=\sum_kf(\lambda_k)P_k=\int f(\lambda)\,dE(\lambda).
$$

**Proof.** The projectors are orthogonal; the sum over the eigenvalues in $\Omega$ is the projection onto the sum of the corresponding eigenspaces; the identities are the finite-dimensional spectral integral.

**Corollary.** The spectral measure gives the spectral decomposition of every normal matrix and the functional calculus for continuous functions.

**Proof.** The finite sum is the spectral integral; the multiplicativity is the orthogonality of the projectors.

## The Operator Norm

### The Spectral Radius

**Definition.** The **spectral radius** of $A$ is $\rho(A)=\max_k|\lambda_k|$, the maximum of the moduli of the eigenvalues.

**Theorem.** For a Hermitian matrix $A$, the operator norm equals the spectral radius:

$$
\|A\|_{\mathrm{op}}=\rho(A)=\max_k|\lambda_k| .
$$

**Proof.** By the spectral decomposition, $\|Ax\|^2=\sum_k|\lambda_k|^2\|P_kx\|^2\le\rho(A)^2\|x\|^2$, so $\|A\|_{\mathrm{op}}\le\rho(A)$. For an eigenvector of the eigenvalue of maximum modulus, equality holds.

**Corollary.** For a normal matrix, the same formula holds. For a general matrix, the operator norm is the square root of the spectral radius of $A^*A$:

$$
\|A\|_{\mathrm{op}}^2=\|A^*A\|_{\mathrm{op}}=\rho(A^*A).
$$

**Proof.** $\|Ax\|^2=\langle A^*Ax,x\rangle$; the supremum over unit $x$ is the largest eigenvalue of the Hermitian matrix $A^*A$, which is $\rho(A^*A)$.

### The Norm Formula

**Proposition.** The operator norm is a norm, and for Hermitian $A$ it is the maximum modulus of the eigenvalues. The Frobenius norm is $\|A\|_F=\sqrt{\sum_k\lambda_k^2}$ for Hermitian $A$.

**Proof.** The operator norm is the sup norm on the unit sphere; the Hermitian spectral decomposition gives the maximum eigenvalue modulus; the Frobenius norm is the square root of the trace of $A^2$, which is the sum of the squares of the eigenvalues.

**Corollary.** For Hermitian $A$, $\|A\|_{\mathrm{op}}\le\|A\|_F\le\sqrt5\|A\|_{\mathrm{op}}$, with equality in the second inequality iff all eigenvalues have the same modulus.

**Proof.** The first inequality is the general comparison; the second is the comparison of the max and the Euclidean norm of the five eigenvalues.

## The Positive Semidefinite Order

### The Order

**Definition.** A Hermitian matrix $A$ is **positive semidefinite**, $A\ge0$, if $\langle x,Ax\rangle\ge0$ for all $x\in\mathbb{C}^5$; it is **positive definite** if the inequality is strict for $x\ne0$. The **Loewner order** is $A\ge B$ iff $A-B\ge0$.

**Theorem.** A Hermitian matrix is positive semidefinite iff all its eigenvalues are nonnegative; it is positive definite iff all its eigenvalues are positive.

**Proof.** By the spectral decomposition, $\langle x,Ax\rangle=\sum_k\lambda_k\|P_kx\|^2$. If all $\lambda_k\ge0$, the sum is nonnegative; if some $\lambda_k<0$, an eigenvector of $\lambda_k$ gives a negative value. The strict case is the same with $x\ne0$.

**Corollary.** The positive semidefinite matrices form a convex cone, closed under addition and under conjugation by invertible matrices; the positive definite matrices are its interior.

**Proof.** The conditions on the eigenvalues are convex and conjugation-invariant; the strict inequalities define the interior.

### The Square Root

**Theorem.** Every positive semidefinite $A$ has a unique positive semidefinite square root

$$
A^{1/2}=\sum_k\sqrt{\lambda_k}P_k .
$$

**Proof.** The spectral decomposition defines $A^{1/2}$; its square is $A$; it is positive semidefinite because the square roots are nonnegative. For uniqueness, if $B^2=A$ with $B\ge0$, then $B$ commutes with $A$ and preserves its eigenspaces; on the $\lambda_k$-eigenspace, $B$ has square $\lambda_k$ and is nonnegative, so $B=\sqrt{\lambda_k}$ there.

**Corollary.** The square root is continuous in the entries and is the unique positive semidefinite solution of $X^2=A$.

**Proof.** The eigenvalues and projectors depend continuously on $A$ (for a Hermitian matrix); the square root is the spectral function.

### The Absolute Value

**Definition.** The **absolute value** of $A$ is $|A|=(A^*A)^{1/2}$.

**Theorem.** $|A|$ is positive semidefinite, and $A=U|A|$ for a partial isometry $U$; this is the polar decomposition.

**Proof.** $A^*A$ is positive semidefinite; its square root $|A|$ is positive semidefinite. Define $U$ on the range of $|A|$ by $U(|A|x)=Ax$; this is well defined and isometric because $\||A|x\|=\|Ax\|$; extend by zero on the orthogonal complement. Then $A=U|A|$ and $U$ is a partial isometry.

**Corollary.** The polar decomposition is the matrix analogue of the polar form of a complex number; the positive part is $|A|$ and the $*$-unitary part is $U$.

**Proof.** The construction is the polar decomposition; the details are in the next article.

## The Functional Calculus

### Polynomials

**Proposition.** For a polynomial $f(t)=\sum_{m=0}^{d}c_mt^m$ and a matrix $A$, $f(A)=\sum_{m=0}^{d}c_mA^m$. For a Hermitian $A$ with spectral decomposition, $f(A)=\sum_kf(\lambda_k)P_k$.

**Proof.** The polynomial evaluation is the algebra homomorphism; the spectral decomposition gives $A^m=\sum_k\lambda_k^mP_k$, and the sum over $m$ gives the formula.

**Corollary.** The map $f\mapsto f(A)$ is an algebra homomorphism from the polynomials to the matrices commuting with $A$.

**Proof.** $(fg)(A)=f(A)g(A)$ because the powers of $A$ commute.

### Continuous Functions

**Theorem.** For a Hermitian $A$ and a continuous function $f$ on the spectrum, the formula

$$
f(A)=\sum_kf(\lambda_k)P_k
$$

defines a continuous functional calculus: it is an algebra homomorphism, it satisfies $\|f(A)\|_{\mathrm{op}}\le\sup_k|f(\lambda_k)|$, and it extends the polynomial calculus.

**Proof.** The formula is linear and multiplicative on the finite spectrum; the norm inequality is the spectral norm formula; a continuous function on the finite spectrum is the limit of polynomials (Weierstrass interpolation), and the map is continuous in the operator norm.

**Corollary.** The functional calculus gives the exponential $e^{tA}=\sum_ke^{t\lambda_k}P_k$, the resolvent $(A-zI)^{-1}=\sum_k(\lambda_k-z)^{-1}P_k$ for $z$ not in the spectrum, and the absolute value.

**Proof.** The functions $e^{tz}$, $(z-\lambda)^{-1}$ and $\sqrt{\lambda}$ are continuous on the spectrum; apply the calculus.

### The Spectral Mapping

**Theorem.** For a Hermitian $A$ and a continuous $f$ on the spectrum,

$$
\sigma(f(A))=f(\sigma(A)),
$$

where $\sigma$ denotes the spectrum.

**Proof.** $f(A)$ is diagonal in the eigenbasis of $A$ with diagonal entries $f(\lambda_k)$; its eigenvalues are exactly the values $f(\lambda_k)$.

**Corollary.** The spectrum of a Hermitian matrix is the set of its eigenvalues; the spectral radius is the maximum modulus; the operator norm is the maximum modulus.

**Proof.** The spectral mapping with $f(t)=t$; the norm formula.

### The Resolvent and the Dunford Projectors

**Definition.** For $A\in M_5(\mathbb{C})$, the **resolvent** is $R(z)=(zI-A)^{-1}$, holomorphic on $\mathbb{C}\setminus\sigma(A)$. For an isolated eigenvalue $\lambda$, the **Dunford projector** is

$$
P_\lambda=\frac{1}{2\pi i}\oint_\Gamma(zI-A)^{-1}\,dz,
$$

where $\Gamma$ is a small positively oriented circle around $\lambda$ enclosing no other eigenvalue.

**Theorem.** $P_\lambda$ is the spectral projector of the generalized eigenspace of $\lambda$: it is idempotent, $P_\lambda P_\mu=\delta_{\lambda\mu}P_\lambda$, $\sum_\lambda P_\lambda=I$, and $A=\sum_\lambda(\lambda P_\lambda+N_\lambda)$ with $N_\lambda=P_\lambda(A-\lambda I)P_\lambda$ nilpotent and commuting with $P_\lambda$. At a simple eigenvalue, $P_\lambda$ is the Lagrange projector.

**Proof.** The contour integral of the resolvent is the standard Dunford calculus; the residue at $\lambda$ is the projection onto the generalized eigenspace along the sum of the other generalized eigenspaces (Kato, *Perturbation Theory*, or Pierce, *Associative Algebras*). The nilpotency of $N_\lambda$ is the definition of the generalized eigenspace. At a simple eigenvalue, the residue is $\prod_{\mu\ne\lambda}(A-\mu I)/(\lambda-\mu)$, which is the Lagrange projector.

**Proposition (degeneration at a repeated eigenvalue).** Let $A_t$ be a holomorphic family with simple spectrum for $t\ne0$ and limit $A_0$ with a repeated eigenvalue $\lambda$ of multiplicity $m$. The individual Lagrange projectors of the $m$ branches need not have limits as $t\to0$; their sum tends to the Dunford projector $P_\lambda$. When the family is normal for the standard form, the limit is the orthogonal projection onto the generalized eigenspace; in general it need not be self-adjoint.

**Proof.** The sum of the Lagrange projectors of the $m$ branches is the contour integral of the resolvent over a contour enclosing those branches and no other eigenvalue; as $t\to0$ the contour tends to one around $\lambda$, and the integral tends to $P_\lambda$ by continuity of the resolvent. The individual projectors carry factors $(\lambda_i(t)-\lambda_j(t))^{-1}$ and may fail to converge when the branches collide. For a normal family the eigenspaces are orthogonal, so the Dunford projector is the orthogonal projection; for a non-normal family it is not self-adjoint.

## Summary

A Hermitian matrix $A$ has an orthonormal eigenbasis, real eigenvalues and the spectral decomposition

$$
A=\sum_k\lambda_kP_k,\qquad P_k^*=P_k,\quad P_kP_l=\delta_{kl}P_k,\quad \sum_kP_k=I .
$$

$$
\boxed{\ \|A\|_{\mathrm{op}}=\max_k|\lambda_k|;\quad A\ge0\iff\lambda_k\ge0;\quad f(A)=\sum_kf(\lambda_k)P_k.\ }
$$

The spectral projectors are the orthogonal projections onto the eigenspaces; at a simple spectrum they are the Lagrange projectors. The operator norm of a Hermitian matrix is its spectral radius; for a general matrix it is the square root of the spectral radius of $A^*A$. The positive semidefinite order is the eigenvalue order; the square root, the absolute value and the polar decomposition follow from the functional calculus.

The normal matrices are exactly the unitarily diagonalizable matrices; the root $H$ is $*$-unitary and normal at the standard point, and its projectors are orthogonal there. A general conjugate $gHg^{-1}$ has idempotent projectors $gE_{kk}g^{-1}$ that are not self-adjoint unless $g$ is $*$-unitary. The algebraic Lagrange decomposition holds for every simple spectrum; the Hilbert-space orthogonality holds only for normal matrices. For a general matrix with a repeated eigenvalue, the Dunford projector is the contour integral of the resolvent over the eigenvalue; the Lagrange projectors of a splitting tend to it in sum, but not individually, and it is orthogonal when the matrix is normal; in general it need not be.

| Object | Value |
|---|---|
| Hermitian eigenvalues | Real |
| Spectral projectors | Orthogonal, $P_k^*=P_k$ |
| Dunford projector | $\frac{1}{2\pi i}\oint_\Gamma(zI-A)^{-1}dz$ |
| Operator norm (Hermitian) | $\max_k|\lambda_k|$ |
| Operator norm (general) | $\sqrt{\rho(A^*A)}$ |
| Positive semidefinite | All eigenvalues $\ge0$ |
| Square root | $A^{1/2}=\sum_k\sqrt{\lambda_k}P_k$ |
| Functional calculus | $f(A)=\sum_kf(\lambda_k)P_k$ |
| Normal matrices | Unitarily diagonalizable |
| Root $H$ | $*$-Unitary, normal, projectors $E_{kk}$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A^*$ | The conjugate transpose |
| $P_k$ | The spectral projector of the eigenvalue $\lambda_k$ |
| $\rho(A)$ | The spectral radius |
| $\|A\|_{\mathrm{op}}$ | The operator norm |
| $A\ge0$ | Positive semidefinite |
| $A^{1/2}$ | The positive semidefinite square root |
| $|A|=(A^*A)^{1/2}$ | The absolute value |
| $\sigma(A)$ | The spectrum |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2013), for the spectral theorem, the spectral projectors, the operator norm and the positive semidefinite order.
- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the functional calculus, the Loewner order and the matrix square root.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, second edition, 2015), for the spectral theorem for Hermitian and normal matrices and the $*$-unitary diagonalization.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 1995), for the resolvent, the Dunford projectors and the degeneration at a repeated eigenvalue.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the algebraic spectral decomposition and the Dunford calculus.
- [The Involution and the Hermitian Structure](the-involution-and-the-hermitian-structure-of-m5c.html), for the Hermitian form and the $*$-unitary group.
- [The Polar Decomposition](the-polar-decomposition-of-m5c.html), for the absolute value and the polar decomposition.
- [The Exponential and the Lie Group](the-exponential-and-the-lie-group-of-m5c.html), for the exponential and the functional calculus.
- [The Quintic and the Spectral Strata](the-quintic-and-the-spectral-strata-of-m5c.html), for the characteristic polynomial and the spectral strata.
