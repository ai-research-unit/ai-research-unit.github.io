
# __The Spectra of Self-Adjoint Operators with Hermitian Adjoint__

## Introduction

A self-adjoint operator on a finite-dimensional Hermitian Clifford module is diagonalisable in an orthonormal basis and has a **real** spectrum; that is the finite-dimensional spectral theorem, and on the Clifford modules it is the theorem that makes the operator theory of the module a theory of *numbers*. The **eigenvalues** of a self-adjoint operator are real, its **eigenspaces** are mutually orthogonal, the operator is the sum $\sum_i\lambda_iP_i$ of its eigenvalues against the orthogonal projections onto the eigenspaces, and every continuous function of the operator is obtained by applying the function to the eigenvalues in the same basis. The two consequences that this article develops are the **min-max (Courant–Fischer) description** of the eigenvalues, which identifies the spectrum with the extreme values of the Rayleigh quotient and makes the spectrum computable and comparable, and the **positivity criterion**, which identifies the positive self-adjoint operators with those whose spectrum lies in the positive half-line and so identifies the interior of the Hermitian cone with the strictly positive spectrum.

The spectral theorem is the bridge between the algebra and the analysis of the module. It converts the self-adjointness of an operator, an algebraic condition, into a statement about the real line; it converts the unitary group, an algebraic group, into a group of transformations of the spectrum; and it converts the positivity of an element, an order-theoretic condition, into a condition on the spectrum. In the definite case the bridge is complete and the spectrum is real; in the indefinite case the self-adjoint operators can have genuinely complex spectrum and the finite-dimensional theorem requires the definite hypothesis, which is the reason the theory is developed in the definite case and then transported.

The self-adjoint and skew-adjoint operators are *Self-Adjoint and Skew Operators with Hermitian Adjoint*; the module, its form and its positivity are *Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint*, *The Blade Form and the Hilbert Structure with Hermitian Adjoint* and *Positivity and the Hermitian Cone of a Hilbert Algebra with Hermitian Adjoint*; the unitary group and the compact real form are *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*; the two-sided operators and their eigenvalues are *Two-Sided Operators on a Clifford Algebra* and *The Hermitian Sylvester Equation with Hermitian Adjoint*; the Dirac operators and their spectra are *Dirac Operators with Hermitian Adjoint* and *Spinor Adjoints and the Dirac Adjoint with Hermitian Adjoint*; and the analytic theory of unbounded self-adjoint operators and their spectral measures is *Unbounded Operators and Spectral Measures*, quoted here in the finite-dimensional case.

## The Finite-Dimensional Spectral Theorem

### Statement and Diagonalisation

**Theorem (the spectral theorem).** Let $T$ be a self-adjoint operator on a finite-dimensional Hermitian Clifford module $(S,\langle\,,\rangle)$ over a definite form. Then the eigenvalues of $T$ are real, the eigenspaces of distinct eigenvalues are mutually orthogonal, $S$ is the orthogonal direct sum of the eigenspaces, and there is an orthonormal basis of $S$ consisting of eigenvectors of $T$. Equivalently, $T$ is **unitarily diagonalisable**: there is a form-preserving isomorphism carrying $T$ to a diagonal operator with real entries.

**Proof sketch.** Self-adjointness makes the **Rayleigh quotient** $R_T(s) = \langle Ts,s\rangle/\langle s,s\rangle$ real-valued, and on the compact unit sphere it attains a maximum; at a maximiser $s$ the variation argument gives $Ts = R_T(s)s$, so a real eigenvalue exists and its eigenvector is $s$. The orthogonal complement of an eigenspace is $T$-invariant, because $T$ is self-adjoint, so induction on the dimension completes the diagonalisation.

### The Spectral Decomposition

**Theorem (the decomposition).** A self-adjoint $T$ has the **spectral decomposition**

$$
T = \sum_{i}\lambda_i\,P_i , \qquad \lambda_i\in\mathbb{R},
$$

where the $P_i$ are the orthogonal projections onto the eigenspaces; the projections satisfy $P_i^2 = P_i = P_i^{\ast}$, $P_iP_j = \delta_{ij}P_i$ and $\sum_iP_i = \mathrm{id}$. Conversely every real linear combination of orthogonal projections is self-adjoint. The decomposition was checked on the regular module of $\mathrm{Cl}_{0,4}(\mathbb{R})$ with the eigenvectors of a self-adjoint two-sided operator: the reconstruction $T = \sum_i\lambda_iP_i$ holds, and $\mathrm{Tr}(T) = \sum_i\lambda_i$, $\det(T) = \prod_i\lambda_i$ with multiplicities.

### The Functional Calculus

**Theorem (the calculus).** For a continuous function $f$ on the spectrum, define $f(T) = \sum_if(\lambda_i)P_i$. Then $T\mapsto f(T)$ is a $\ast$-homomorphism from the continuous functions on $\sigma(T)$ into the operators, it takes the constant $1$ to the identity, it is isometric for the supremum norm, and for a polynomial $f$ it agrees with the polynomial in $T$. In particular $\sqrt{T}$, $|T| = \sqrt{T^{\ast}T}$, $\exp(T)$ and the resolvent $(T-\lambda)^{-1} = \sum_i(\lambda_i-\lambda)^{-1}P_i$ for $\lambda\notin\sigma(T)$ are defined, and $\exp(T)$ is self-adjoint positive. These are the finite-dimensional cases of *Unbounded Operators and Spectral Measures*.

## The Spectrum as an Extremal Problem

**Theorem (min-max, Courant–Fischer).** Let $T$ be self-adjoint with eigenvalues ordered $\lambda_1\leq\lambda_2\leq\cdots\leq\lambda_N$ and let $\mathcal{S}_k$ range over the $k$-dimensional subspaces of $S$. Then

$$
\lambda_k = \min_{\dim\mathcal{S}_k = k}\ \max_{0\neq s\in\mathcal{S}_k}\ \frac{\langle Ts,s\rangle}{\langle s,s\rangle} = \max_{\dim\mathcal{S}_{N-k+1}=N-k+1}\ \min_{0\neq s\in\mathcal{S}}\ \frac{\langle Ts,s\rangle}{\langle s,s\rangle} ,
$$

so the spectrum is read off from the extremes of the Rayleigh quotient; in particular $\lambda_{\min} = \min_sR_T(s)$ and $\lambda_{\max} = \max_sR_T(s)$. This was checked on the regular module: for every random vector the Rayleigh quotient lay between the extreme eigenvalues.

**Corollary (positivity).** A self-adjoint operator is **positive**, $\langle Ts,s\rangle\geq0$ for all $s$, exactly when $\lambda_i\geq0$ for all $i$, and **strictly positive** exactly when $\lambda_i>0$ for all $i$. So in the definite case the positive self-adjoint operators are those with spectrum in $[0,\infty)$, the strictly positive ones are the interior of the **Hermitian cone** of *Positivity and the Hermitian Cone of a Hilbert Algebra with Hermitian Adjoint*, and the Cauchy–Schwarz inequality $\langle Ts,t\rangle^2\leq\langle Ts,s\rangle\langle Tt,t\rangle$ for $T$ positive is the Cauchy–Schwarz inequality of the form polarised by $T$. This was checked: spectrum strictly positive implies the quadratic form is strictly positive.

## Skew-Adjoint, Normal and Unitary

### Imaginary Spectrum

**Theorem (skew-adjoint operators).** If $K$ is skew-adjoint then $iK$ is self-adjoint, so the eigenvalues of $K$ are **purely imaginary** and the eigenspaces of $K$ are orthogonal; $K$ generates a one-parameter unitary group $\exp(tK)$ whose eigenvalues are $e^{it\lambda}$ on the unit circle. This was checked: on the definite regular module the skew-adjoint operators are the skew-symmetric matrices, so their eigenvalues are the purely imaginary numbers $\pm i\theta$ and the eigenvalues of $iK$ are real.

### Normal Operators and Simultaneous Diagonalisation

**Theorem (normal operators).** The following are equivalent for a finite-dimensional operator: $T$ is normal ($TT^{\ast} = T^{\ast}T$); $T$ is unitarily diagonalisable; the spectral decomposition holds with complex eigenvalues. In particular the self-adjoint, the skew-adjoint and the unitary operators are normal, and a **commuting family of normal operators** is simultaneously unitarily diagonalisable. This is what makes the spectrum of the two-sided operators computable below.

**Proof.** For normal $T$ the operator $H = \tfrac12(T+T^{\ast})$ and $K = \tfrac12(T-T^{\ast})$ commute and are self-adjoint and skew-adjoint, so they can be diagonalised simultaneously by the induction of the spectral theorem applied to $H$ and then to $K$ on each eigenspace; the converse is immediate from the diagonal form.

### Invariance under the Unitary Group

**Theorem (the spectrum is a unitary invariant).** If $U$ is form-preserving and $T$ is self-adjoint then $UTU^{-1}$ is self-adjoint with the same spectrum, and the map $T\mapsto UTU^{-1}$ is the conjugation action of the unitary group on the self-adjoint operators. The orbits are the **isospectral sets**, classified in the definite case by the multiset of eigenvalues alone. This was checked on the regular module: conjugation of a self-adjoint two-sided operator by a slice element leaves the spectrum unchanged.

## The Two-Sided Operators

**Theorem (the spectrum of $L_a+R_b$).** The left and the right multiplications commute, $L_aR_b = R_bL_a$, so for self-adjoint $a,b$ the operator $L_a+R_b$ is self-adjoint, the pair $L_a,R_b$ is a commuting family of self-adjoint operators, and it is simultaneously diagonalisable. The eigenvalues of $L_a+R_b$ are the sums $\lambda_i+\mu_j$ of an eigenvalue $\lambda_i$ of $L_a$ and an eigenvalue $\mu_j$ of $R_b$ taken along the common eigenbasis, hence lie in the set of all sums $\sigma(L_a)+\sigma(R_b)$; this was checked on the regular module of $\mathrm{Cl}_{0,4}(\mathbb{R})$, where every eigenvalue of $L_a+R_b$ was a sum of a left and a right eigenvalue. In particular

$$
L_a+R_b \ \text{invertible} \iff \lambda_i+\mu_j\neq0 \ \text{for every pair} ,
$$

the Clifford form of the solvability condition of the Hermitian Sylvester equation, checked against the determinant: $\det(L_a+R_b) = 0$ exactly when some $\lambda_i+\mu_j$ vanished.

**Corollary (the $L_a$ spectrum).** The eigenvalues of the left multiplication $L_a$ are the values of $a$ in the left regular representation, that is the spectrum of the matrix of $A\mapsto aA$; for a self-adjoint $a$ in a definite algebra they are real, and the $L_a$ for all $a$ generate a commutative algebra only when the algebra is commutative. For the spinor modules the corresponding eigenvalues are the **Clifford weights** of the finite-dimensional representation, which are the subject of *Spin Representations of the Orthogonal Lie Algebra with Inner Conjugation*; the finite $\mathbb{Z}/2$-grading of the module is the **chirality**, and the operators that respect it are the even ones.

## The Indefinite Case and the Limits of the Theorem

**Remark (why the form is assumed definite).** The spectral theorem requires the positivity of the form. In an indefinite signature the operator adjoint is $T^{\ast} = G^{-1}T^{H}G$ with $G$ a non-definite Gram matrix, and a $T$ that is self-adjoint for such a form need not have real spectrum. On the regular module of $\mathrm{Cl}_{1,3}(\mathbb{R})$ the self-adjoint operators are the $G$-symmetric matrices, and the self-adjoint two-sided operators of the indefinite example were **not** symmetric in the ordinary sense, so the finite-dimensional spectral theorem is not available for them. The correct statement in the indefinite case is the **Krein-space** statement: the spectrum is symmetric with respect to the real axis, the eigenvalues are real or occur in complex-conjugate pairs, and the eigenvectors may be **isotropic** and do not span the space. So the definite case is the case of the full spectral theorem, and the indefinite case is a structural theory of a different kind, treated through the signature and the Pontryagin spaces.

## Worked Cases

### The Definite Case $\mathrm{Cl}_{0,4}(\mathbb{R})$

Here the form is positive definite and the Gram matrix is the identity, so the self-adjoint operators of the regular module are the symmetric matrices of the blade basis; the Hermitian part of the algebra is $\mathrm{span}\{e_A : |A|\equiv0,3\pmod4\}$ of degrees $0,3,4$, so there are non-central self-adjoint elements and the self-adjoint operators have spectra that are not concentrated at a single value; a sampled operator had four distinct eigenvalues, each of multiplicity four, so the multiplicities are inherited from the module and are not all one. The example $\mathrm{Tr}(L_a+R_b) = \sum\lambda_i$ and $\det(L_a+R_b) = \prod\lambda_i$ hold, the spectral decomposition reconstructs the operator, the min-max principle bounds the Rayleigh quotient, the positive operators are those with spectrum in $[0,\infty)$, and conjugation by a slice element permutes the eigenvalues. This is the model case of the whole article.

### The Definite Case $\mathrm{Cl}_{0,3}(\mathbb{R})$

Here the Hermitian part of the algebra is $\mathrm{span}\{1,\omega\}$, **central**, so the self-adjoint two-sided operators of the regular module descend from central elements and the spectrum is highly degenerate; the example shows that the spectral theory is a statement about the module and the form, not about the dimension of the Hermitian part of the algebra. The non-degeneracy of the spectrum requires the Hermitian part of the algebra to be non-central, which happens from $\mathrm{Cl}_{0,4}$ on.

### The Skew-Adjoint and the Unitary Group

The skew-adjoint operators of the definite module are the skew-symmetric matrices; their eigenvalues are purely imaginary, the eigenvalues of $\exp(K)$ lie on the unit circle, and the exponential of the skew-adjoint part of a two-sided operator is a slice element of *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*. So the spectrum of the skew-adjoint operators is the infinitesimal form of the spectrum of the unitary group, and the spectral theorem for the two is the same statement in the definite case.

## Summary

A self-adjoint operator on a finite-dimensional Hermitian Clifford module with a definite form has a **real spectrum**, orthogonal eigenspaces spanning the module, and a **spectral decomposition** $T = \sum_i\lambda_iP_i$ into orthogonal projections; it is unitarily diagonalisable, the reconstruction and the identities $\mathrm{Tr}(T) = \sum\lambda_i$, $\det(T) = \prod\lambda_i$ hold, and the **functional calculus** $f(T) = \sum_if(\lambda_i)P_i$ is a $\ast$-homomorphism, isometric for the supremum norm. The eigenvalues are the extreme values of the **Rayleigh quotient** by the **min-max (Courant–Fischer) principle**, the **positive** self-adjoint operators are exactly those with spectrum in $[0,\infty)$ (the cone in the definite case), and the **skew-adjoint** operators have purely imaginary spectrum generating the one-parameter unitary groups. **Normal** operators are the unitarily diagonalisable ones, a commuting family is simultaneously diagonalisable, and the spectrum is invariant under conjugation by the **unitary group**, whose orbits are the isospectral sets.

The regular representation realises the theory on the algebra: $L_aR_b = R_bL_a$, so for self-adjoint $a,b$ the operator $L_a+R_b$ is self-adjoint and its eigenvalues are the sums $\lambda_i+\mu_j$ of a left and a right eigenvalue, and $L_a+R_b$ is invertible exactly when no such sum vanishes, the spectral form of the solvability condition of the Hermitian Sylvester equation. The theorem requires a **definite** form: in indefinite signature the self-adjoint operators need not have real spectrum, the eigenvalues are real or occur in conjugate pairs, and the eigenvectors may be isotropic; the definite case is the case of the full spectral theorem, and the indefinite case is treated by the signature.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T = \sum_i\lambda_iP_i$, $\lambda_i\in\mathbb{R}$ | Spectral decomposition of a self-adjoint operator |
| $P_i^2=P_i=P_i^{\ast}$, $P_iP_j=\delta_{ij}P_i$, $\sum P_i=\mathrm{id}$ | The spectral projections |
| $f(T)=\sum_if(\lambda_i)P_i$ | Functional calculus |
| $R_T(s)=\langle Ts,s\rangle/\langle s,s\rangle$ | Rayleigh quotient |
| $\lambda_k=\min_{\dim\mathcal S_k=k}\max_{s\in\mathcal S_k}R_T(s)$ | Min-max principle |
| $\lambda_i\geq0$ / $>0$ | Positive / strictly positive self-adjoint operators |
| $K^{\ast}=-K\Rightarrow\mathrm{spec}(K)\subset i\mathbb{R}$ | Skew-adjoint spectrum |
| $TT^{\ast}=T^{\ast}T$ | Normal operators (unitarily diagonalisable) |
| $\mathrm{spec}(UTU^{-1})=\mathrm{spec}(T)$ | Unitary invariance |
| $\mathrm{spec}(L_a+R_b)\subseteq\mathrm{spec}(L_a)+\mathrm{spec}(R_b)$ | Two-sided spectrum |

## Further Reading

- Rajendra Bhatia, *Matrix Analysis*, Graduate Texts in Mathematics 169 (Springer, 1997), for the finite-dimensional spectral theorem, the minimax principle and the Rayleigh quotient.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2nd ed. 2013), for the spectral theorem for normal operators, the spectral projections and the invariance of the spectrum under unitary conjugation.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the self-adjoint operators in an indefinite inner product and the structure of their spectra, the Krein spaces and the isotropic eigenvectors.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic Press, 1980), for the unbounded spectral theorem, the projection-valued measures and the functional calculus quoted in the finite-dimensional case.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Vol. I (Academic Press, 1983), for the positive elements, the order structure and the continuous functional calculus.
