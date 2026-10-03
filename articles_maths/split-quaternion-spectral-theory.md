
# __Split-Quaternion Spectral Theory__

## Introduction

The split-quaternion algebra $\mathbb{H}_{\mathrm{s}} \cong M_2(\mathbb{R})$ is unital and associative but neither commutative nor a division algebra, and both failures shape its spectral theory. Because the algebra is a real form of $M_2(\mathbb{C})$ and has an **indefinite** norm, the spectrum of an element falls into two qualitatively different regimes: a real eigenvalue pair or a complex-conjugate pair, according to the sign of the split-quaternion norm of the vector part. This dichotomy is the feature that distinguishes the subject from the biquaternion spectral theory, where the corresponding vector norm is definite.

This article defines the spectrum, discusses left and right eigenvalues, states the eigenvalue dichotomy, the Cayley–Hamilton theorem and the trace and determinant functionals, the eigenspaces and their dimensions, the resolvent and the spectral radius, and the relation to the biquaternion spectral theory. It relies on *Split-Quaternion Norm and Invertibility* for the invertibility criterion and on *Split-Quaternion Zero Divisors* for the singular elements. "Spectrum" without qualification always means the set of roots of the characteristic polynomial of the element, analysed over $\mathbb{C}$. No physics is invoked.

**Conventions.** A general element is $\tilde q = q_0 + \mathbf v$ with $q_0 = \operatorname{Sc}(\tilde q)\in\mathbb{R}$ and $\mathbf v = q_1e_1+q_2e_2+q_3e_3\in V$; $N(\tilde q) = q_0^2+N(\mathbf v)$, $N(\mathbf v) = q_1^2-q_2^2-q_3^2$. The **trace** and **determinant** functionals are $T(\tilde q) = \tilde q + \tilde{q}^{\natural} = 2q_0$ and $D(\tilde q) = \tilde q\tilde{q}^{\natural} = N(\tilde q)$.

## The Spectrum of a Split Quaternion

**Definition.** The **spectrum** of $\tilde q\in\mathbb{H}_{\mathrm{s}}$ is

$$
\sigma(\tilde q) = \{\, \lambda \in \mathbb{C} : \tilde q - \lambda \text{ is not invertible in } \mathbb{H}_{\mathrm{s}}\otimes_{\mathbb{R}}\mathbb{C} \,\},
$$

equivalently the zero set of the **characteristic polynomial** of $\tilde q$

$$
p_{\tilde q}(\lambda) = \lambda^2 - 2q_0\lambda + N(\tilde q).
$$

**Theorem.** The spectrum of $\tilde q = q_0+\mathbf v$ is

$$
\sigma(\tilde q) = \{\, q_0 + \sqrt{-N(\mathbf v)},\; q_0 - \sqrt{-N(\mathbf v)} \,\},
$$

where $\sqrt{\cdot}$ denotes either complex square root, the two choices giving the two points of $\sigma(\tilde q)$. In particular $\tilde q$ is singular, i.e. a zero divisor or zero, if and only if $0 \in \sigma(\tilde q)$, if and only if $N(\tilde q) = 0$.

**Proof.** The characteristic polynomial is $\lambda^2 - 2q_0\lambda + N(\tilde q)$, with discriminant $4q_0^2-4N(\tilde q) = -4N(\mathbf v)$. Its roots are $q_0\pm\sqrt{-N(\mathbf v)}$, and $N(\tilde q) = 0$ is exactly the vanishing of the constant term, i.e. $0$ a root.

**The real spectrum.** The spectrum *over $\mathbb{R}$* is $\sigma_{\mathbb{R}}(\tilde q) = \sigma(\tilde q)\cap\mathbb{R}$. Unlike the complex case, this set may be empty: when $N(\mathbf v) > 0$ the two eigenvalues are non-real and $\sigma_{\mathbb{R}}(\tilde q) = \emptyset$ even for an invertible $\tilde q$. This is the standard behaviour of a spectrum in a real algebra, and it is the reason the spectrum is taken over $\mathbb{C}$ here.

## Left and Right Eigenvalues

Eigenvalues may be sought in the algebra itself rather than in the centre, and then the non-commutativity matters.

**Definition.** A scalar $\lambda \in \mathbb{H}_{\mathrm{s}}$ is a **left eigenvalue** of $\tilde q$ if $\tilde q v = \lambda v$ for some nonzero $v \in \mathbb{H}_{\mathrm{s}}$, and a **right eigenvalue** if $\tilde q v = v\lambda$ for some nonzero $v$. The sets are the **left spectrum** $\sigma_L(\tilde q)$ and the **right spectrum** $\sigma_R(\tilde q)$.

**Theorem.** If the eigenvalues are required to lie in the **centre** $\mathbb{R}$ of the algebra, the left and right problems coincide and equal the real spectrum:

$$
\sigma_L(\tilde q)\cap\mathbb{R} = \sigma_R(\tilde q)\cap\mathbb{R} = \sigma_{\mathbb{R}}(\tilde q) = \{\lambda \in \mathbb{R} : p_{\tilde q}(\lambda) = 0\}.
$$

For eigenvalues taken in the full algebra, $\sigma_R(\tilde q)$ is a union of conjugacy classes: $\tilde q v = v\lambda$ implies $\tilde q(vw) = (vw)(w^{-1}\lambda w)$ for every unit $w$, so the right spectrum is closed under conjugation by units, while the left spectrum is not.

**Proof.** Central scalars commute with every element, so $(\tilde q-\lambda)v = 0$ and $v(\tilde q-\lambda) = 0$ are equivalent, and either condition is the singularity of $\tilde q-\lambda$; the conjugacy statement is the displayed computation.

**Remark.** Because $\mathbb{H}_{\mathrm{s}}$ is not a division algebra, the left spectrum in the algebra contains more than the central spectrum: any zero divisor produces an element $v$ with $\tilde q v = 0$, giving the left eigenvalue $0$ even when $\tilde q$ itself is invertible, whenever $\tilde q$ fails to be injective on the relevant left ideal. The intrinsic spectrum of the previous section, taken over $\mathbb{C}$, is the one used throughout.

## The Eigenvalue Dichotomy

**Theorem (dichotomy).** For $\tilde q = q_0+\mathbf v$, the spectrum is governed by the sign of $N(\mathbf v)$:

- if $N(\mathbf v) < 0$, then $\sigma(\tilde q)$ consists of **two distinct real numbers** $q_0 \pm \sqrt{|N(\mathbf v)|}$;
- if $N(\mathbf v) > 0$, then $\sigma(\tilde q)$ consists of a **complex-conjugate pair** $q_0 \pm i\sqrt{N(\mathbf v)}$;
- if $N(\mathbf v) = 0$, then $\sigma(\tilde q)$ is the **real double root** $\{q_0\}$.

Moreover, $\tilde q$ is singular if and only if $\lambda = 0$ is a root, i.e. $q_0 = 0$ and $N(\mathbf v) = 0$.

**Proof.** These are the three cases of the preceding formula, according to whether $-N(\mathbf v)$ is positive, negative or zero.

The dichotomy is the signature in the spectrum of the indefiniteness of $N$: the timelike directions of the vector part ($N(\mathbf v)>0$) give oscillatory, conjugate-pair behaviour, while the spacelike directions ($N(\mathbf v)<0$) give real, exponential behaviour. The null directions sit at the transition, where the two eigenvalues coalesce.

**Example.** For $\tilde q = e_1$ ($q_0=0$, $N(\mathbf v)=1>0$) the spectrum is $\{i, -i\}$, a conjugate pair; for $\tilde q = e_2$ ($q_0=0$, $N(\mathbf v)=-1<0$) the spectrum is $\{1,-1\}$, real; for $\tilde q = e_1+e_3$ ($N(\mathbf v)=0$) the spectrum is $\{0\}$ and $\tilde q$ is a zero divisor.

## Cayley–Hamilton and the Trace and Determinant Functionals

**Definition.** The **trace** and **determinant** functionals of $\mathbb{H}_{\mathrm{s}}$ are

$$
T(\tilde q) = 2q_0 = \tilde q + \tilde{q}^{\natural}, \qquad D(\tilde q) = N(\tilde q) = \tilde q\tilde{q}^{\natural} .
$$

Both are real-valued; $T$ is linear and $D$ is multiplicative, $D(\tilde q \tilde p) = D(\tilde q)D(\tilde p)$, and $D(\tilde q) \neq 0$ is exactly invertibility.

**Theorem (Cayley–Hamilton).** Every element satisfies its characteristic equation,

$$
\tilde q^2 - T(\tilde q)\,\tilde q + D(\tilde q)\,e_0 = 0, \qquad\text{that is}\qquad \tilde q^2 - 2q_0\,\tilde q + N(\tilde q) = 0 .
$$

**Proof.** With $\mathbf v^2 = -N(\mathbf v)$, expand $\tilde q^2 = (q_0+\mathbf v)^2 = q_0^2 + 2q_0\mathbf v - N(\mathbf v)$; then $\tilde q^2 - 2q_0\tilde q + N(\tilde q) = (q_0^2+2q_0\mathbf v - N(\mathbf v)) - 2q_0(q_0+\mathbf v) + (q_0^2+N(\mathbf v)) = 0$.

**Corollary (reduction and powers).** The Cayley–Hamilton relation reduces every polynomial in $\tilde q$ to a linear expression $\alpha \tilde q + \beta e_0$ with $\alpha,\beta \in \mathbb{R}$, and gives the recurrence $\tilde q^{n+1} = 2q_0\,\tilde q^n - N(\tilde q)\,\tilde q^{n-1}$ for $n\geq1$.

**Example.** For $\tilde q = 1 + e_2$, Cayley–Hamilton reads $\tilde q^2 - 2\tilde q = 0$, so $\tilde q^2 = 2\tilde q$. For a **null vector**, $q_0 = 0$ and $N(\mathbf v)=0$, the relation reads $\tilde q^2 = 0$; the null vectors are exactly the square-zero elements, though a general zero divisor with $q_0\neq0$ is not square-zero.

## Eigenspaces and Their Dimensions

**Definition.** For $\lambda \in \sigma(\tilde q)$, the **eigenspace** is

$$
E_\lambda = \{\, v \in \mathbb{H}_{\mathrm{s}} : (\tilde q-\lambda)v = 0 \,\},
$$

a right ideal of $\mathbb{H}_{\mathrm{s}}$, stable under right multiplication because $(\tilde q-\lambda)v = 0$ gives $(\tilde q-\lambda)(vu) = 0$.

**Theorem.** The dimensions are as follows.

- If the eigenvalues are distinct — the cases $N(\mathbf v) \neq 0$ — then each eigenspace is a **line**, of complex dimension $1$ and real dimension $2$.
- If $N(\mathbf v) = 0$ and $\mathbf v \neq 0$, the single eigenvalue is $\lambda = q_0$ and the eigenspace has real dimension $2$.
- If $\mathbf v = 0$, so that $\tilde q = q_0$ is central, the single eigenvalue is $q_0$ and the eigenspace is the whole algebra, of real dimension $4$.

**Proof.** For distinct roots an eigenspace of dimension greater than one would make $\tilde q$ act as a scalar on a two-dimensional subspace, forcing a repeated root; hence the eigenspace is a line. When $N(\mathbf v)=0$ and $\mathbf v \neq 0$ the two roots coincide and $\tilde q - q_0 = \mathbf v$ is a nonzero nilpotent; the eigenspace of the regular representation is the kernel of left multiplication by $\mathbf v$, two-dimensional, a minimal right ideal of *Split-Quaternion Idempotents and Projections*. When $\mathbf v = 0$ the element is scalar and the eigenspace is everything.

**Corollary.** For a spacelike vector part the spectrum is a real pair and the eigenlines are real; for a timelike vector part the spectrum is a complex-conjugate pair and the eigenlines are complex, with no real eigenline; for a null vector part the single real eigenvalue has a two-dimensional eigenspace. The elements with a **repeated** eigenvalue are exactly those with $N(\mathbf v) = 0$; among them the zero divisors are those with $q_0 = 0$ and $\mathbf v \neq 0$, while those with $q_0 \neq 0$ are invertible with a repeated eigenvalue and a two-dimensional eigenspace.

## The Resolvent

**Definition.** For $\lambda \notin \sigma(\tilde q)$ the **resolvent** is

$$
R(\lambda) = (\tilde q-\lambda)^{-1} = \frac{(\tilde q-\lambda)^{\natural}}{N(\tilde q-\lambda)} = \frac{\tilde{q}^{\natural} - \lambda}{N(\tilde q) - 2q_0\lambda + \lambda^2}.
$$

**Theorem.** The resolvent is a $\mathbb{H}_{\mathrm{s}}$-valued rational function of $\lambda$ whose poles are exactly the points of $\sigma(\tilde q)$, and it satisfies

$$
R(\lambda) - R(\mu) = (\lambda - \mu)\,R(\lambda)R(\mu), \qquad \tilde q\,R(\lambda) = R(\lambda)\,\tilde q,
$$

the resolvent identity and commutativity with $\tilde q$, on the common domain of definition.

**Proof.** The inverse formula is the standard $\tilde p^{-1} = \tilde p^{\natural}/N(\tilde p)$ of *Split-Quaternion Norm and Invertibility* applied to $\tilde p = \tilde q-\lambda$, and $N(\tilde q-\lambda) = \lambda^2-2q_0\lambda+N(\tilde q) = p_{\tilde q}(\lambda)$ is the characteristic polynomial, so the denominator vanishes exactly on $\sigma(\tilde q)$. The resolvent identity is the algebraic identity for inverses of non-commuting factors that do commute here, since $\tilde q$ commutes with every polynomial in $\tilde q$.

**Remark.** $R$ is analytic in $\lambda$ off $\sigma(\tilde q)$ in the sense of $\mathbb{H}_{\mathrm{s}}$-valued functions of a **real or complex central** variable $\lambda$; because $\lambda$ is central, the calculus of one real or complex variable applies to $R$ componentwise. There is no analogue of the Cauchy integral of a non-central variable here.

## The Spectral Radius

**Definition.** The **spectral radius** of $\tilde q$ is $\rho(\tilde q) = \max\{|\lambda| : \lambda \in \sigma(\tilde q)\}$.

**Theorem.** The spectral radius is

$$
\rho(\tilde q) = |q_0| + \sqrt{|N(\mathbf v)|}\quad (N(\mathbf v) < 0), \qquad
\rho(\tilde q) = \sqrt{q_0^2 + N(\mathbf v)}\quad (N(\mathbf v) > 0), \qquad
\rho(\tilde q) = |q_0|\quad (N(\mathbf v) = 0).
$$

Equivalently, with the eigenvalues $\lambda_\pm = q_0\pm\sqrt{-N(\mathbf v)}$, $\rho(\tilde q) = \max(|\lambda_+|,|\lambda_-|)$. It satisfies $\rho(\tilde q) \le \|L_{\tilde q}\|$, where $L_{\tilde q}$ is the left-multiplication operator and $\|L_{\tilde q}\|$ its operator norm on $\mathbb{H}_{\mathrm{s}} \cong \mathbb{R}^4$ with the Euclidean norm.

**Proof.** The formulas are the three cases of the dichotomy evaluated at $\lambda_\pm$. The inequality $\rho(\tilde q)\le\|L_{\tilde q}\|$ is the general fact that every eigenvalue of an operator is bounded by its split-quaternion norm, applied to the complexification of $L_{\tilde q}$.

**Example.** For $\tilde q = 1 + e_2$ the vector part has $N(\mathbf v) = -1 < 0$, so $\rho(\tilde q) = 1 + 1 = 2$, attained at the eigenvalue $\lambda = 2$; the other eigenvalue is $0$, reflecting that $1+e_2$ is a zero divisor. For $\tilde q = e_1$ the vector part has $N(\mathbf v)=1>0$, so $\rho(\tilde q) = 1$, attained at both eigenvalues $\pm i$.

**Remark.** The inequality can be strict: for a non-diagonalisable element the operator norm exceeds the spectral radius. Here every element is diagonalisable over $\mathbb{C}$ with at most a repeated eigenvalue, so $\rho(\tilde q) = \|L_{\tilde q}\|$ fails only in the nilpotent, repeated-eigenvalue case.

## Hermitian and Normal Elements

The definite spectral theorem has no direct analogue, and the reason is the indefinite form.

**Definition.** An element is **symmetric** (Hermitian for the conjugation ${}^{\natural}$) if $\tilde{q}^{\natural} = \tilde q$, and **normal** if $\tilde q\tilde{q}^{\natural} = \tilde{q}^{\natural} \tilde q$.

**Theorem.** The symmetric elements are exactly the scalars, $\tilde q = q_0$, because $\tilde{q}^{\natural} = q_0 - \mathbf v$ equals $\tilde q = q_0+\mathbf v$ only for $\mathbf v = 0$. Every element is normal, since $\tilde q\tilde{q}^{\natural} = \tilde{q}^{\natural} \tilde q = N(\tilde q)e_0$ holds identically. Thus the symmetric elements are the scalar line, and the "unitarily diagonalisable" class is the whole algebra only in the trivial sense that all elements are diagonalisable over $\mathbb{C}$ by similarity.

**Proof.** The symmetric statement is immediate; normality follows from $\tilde q\tilde{q}^{\natural} = N(\tilde q)$ being central.

**Remark.** The involutions $\alpha$ and $\rho$ of *Split-Quaternion Subspaces and the Involutions* have larger fixed spaces, $\operatorname{span}\{1,e_2,e_3\}$ and $\operatorname{span}\{1,e_1,e_2\}$, and the indefinite form makes neither of them a positive-definite Hermitian structure; a genuine spectral theorem in the sense of Hilbert space theory requires a definite form, which $\mathbb{H}_{\mathrm{s}}$ does not carry. What replaces it is the direct-sum (Peirce) decomposition of *Split-Quaternion Ideals and Peirce Decomposition*, which is a decomposition tailored to an idempotent rather than to a Hermitian element.

## Relation to the Biquaternion Spectral Theory

The biquaternion article *Biquaternion Spectral Theory* takes the spectrum of $\tilde Q = \sum_\mu Q_\mu e_\mu \in \mathbb{B} = M_2(\mathbb{C})$ over $\mathbb{C}$, with trace $2Q_0$ and determinant $N(\tilde Q) = \sum_\mu Q_\mu^2$, and eigenvalues

$$
\tilde\lambda_\pm = Q_0 \pm iB, \qquad B = \sqrt{Q_1^2+Q_2^2+Q_3^2},
$$

the **definite** complex norm of the vector part. There, the eigenvalues are always of the same type — a complex-conjugate pair the moment $B \neq 0$ — because the vector norm is complex and definite on the quaternion directions.

The split-quaternion case, by contrast, has real eigenvalues $q_0\pm\sqrt{-N(\mathbf v)}$ whose type is decided by the **sign** of the indefinite norm $N(\mathbf v)$: a real pair for spacelike $\mathbf v$, a conjugate pair for timelike $\mathbf v$, and a double root for null $\mathbf v$. The Cayley–Hamilton relation and the trace and determinant functionals have the same shape in both cases, $\tilde q^2 - T \tilde q + D = 0$, with $D = N$ the determinant and $T$ twice the scalar part; the zero-divisor set is $\{N = 0\}$ in both, and for the split algebra it is exactly the set of elements with $0$ in the spectrum. Since $\mathbb{H}_{\mathrm{s}}\otimes_{\mathbb{R}}\mathbb{C} = M_2(\mathbb{C}) \cong \mathbb{B}$, the complexified theories are the same; the split-quaternion theory is the real form in which the spectrum displays the indefiniteness of the form. Nothing biquaternion-specific — the central imaginary unit $i$, the definite vector norm, the Hermitian spectral theorem — is imported.

## Summary

The spectrum of $\tilde q = q_0+\mathbf v$ is the zero set of the characteristic polynomial $p_{\tilde q}(\lambda) = \lambda^2-2q_0\lambda+N(\tilde q)$, namely $\sigma(\tilde q) = \{q_0\pm\sqrt{-N(\mathbf v)}\}$, with $\tilde q$ singular exactly when $0\in\sigma(\tilde q)$, i.e. $N(\tilde q)=0$. The **eigenvalue dichotomy** is decided by the sign of $N(\mathbf v)$: a distinct real pair for spacelike $\mathbf v$, a complex-conjugate pair for timelike $\mathbf v$, and a real double root for null $\mathbf v$; the spectrum over $\mathbb{R}$ may be empty. Left and right eigenvalues with central scalars coincide with the real spectrum, while the right spectrum in the full algebra is a union of conjugacy classes. The trace and determinant functionals are $T(\tilde q)=2q_0$ and $D(\tilde q)=N(\tilde q)$, and Cayley–Hamilton reads $\tilde q^2-2q_0\tilde q+N(\tilde q)=0$, reducing all powers to a linear expression and making every null element square-zero. Eigenspaces are lines for distinct eigenvalues, two-dimensional for the null elements, and the whole algebra for scalars. The resolvent $R(\lambda) = (\tilde{q}^{\natural}-\lambda)/(\lambda^2-2q_0\lambda+N(\tilde q))$ has poles exactly on the spectrum and satisfies the resolvent identity, and the spectral radius is $|q_0|+\sqrt{|N(\mathbf v)|}$, $\sqrt{q_0^2+N(\mathbf v)}$ or $|q_0|$ according to the sign of $N(\mathbf v)$. Symmetric elements are the scalars and every element is normal, so there is no definite spectral theorem; the Peirce decomposition replaces it. Compared with the biquaternion theory, the spectra have the same polynomial shape but the split vector norm makes the eigenvalue type depend on the sign of the indefinite form.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$, $\tilde q=q_0+\mathbf v$ | the split-quaternion algebra and a general element | *Split-Quaternion Algebra* |
| $T(\tilde q) = 2q_0 = \tilde q+\tilde{q}^{\natural}$ | the trace functional | this article |
| $D(\tilde q) = N(\tilde q) = \tilde q\tilde{q}^{\natural}$ | the determinant / norm functional | *Split-Quaternion Norm and Invertibility* |
| $\sigma(\tilde q) = \{q_0\pm\sqrt{-N(\mathbf v)}\}$ | the spectrum over $\mathbb{C}$ | this article |
| $\sigma_{\mathbb{R}}(\tilde q)$, $\sigma_L(\tilde q)$, $\sigma_R(\tilde q)$ | real, left and right spectra | this article |
| $p_{\tilde q}(\lambda) = \lambda^2-2q_0\lambda+N(\tilde q)$ | the characteristic polynomial | this article |
| $\tilde q^2-2q_0\tilde q+N(\tilde q)=0$ | Cayley–Hamilton | this article |
| $E_\lambda$ | the eigenspace, a left ideal | this article |
| $R(\lambda) = (\tilde{q}^{\natural}-\lambda)/(\lambda^2-2q_0\lambda+N(\tilde q))$ | the resolvent | this article |
| $\rho(\tilde q)$ | the spectral radius, by cases on $\operatorname{sgn}N(\mathbf v)$ | this article |
| $N(\mathbf v) = q_1^2-q_2^2-q_3^2$ | the restricted norm, signature $(2,1)$ | *Split-Quaternion Scalar and Vector Subspaces* |
| zero divisors $=\{N=0\}$ | the singular elements, spectrum containing $0$ | *Split-Quaternion Zero Divisors* |

## Further Reading

- F. R. Gantmacher, *The Theory of Matrices*, Vol. 1 (Chelsea, 1959), for the characteristic polynomial, Cayley–Hamilton, the resolvent identity and the spectral radius of a finite matrix.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed. (Cambridge University Press, 2013), for the spectral radius, the operator-norm bound and diagonalisability.
- John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288 (Springer, 2021), for spectra of elements of a four-dimensional real algebra and the left/right eigenvalue distinction.
- Graziano Gentili, Caterina Stoppato and Daniele C. Struppa, *Regular Functions of a Quaternionic Variable* (Springer, 2013), for the non-commutative spectral theory and the Peirce decomposition of a quaternion algebra.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Matrix Polynomials* (Academic Press, 1982), for the resolvent, the companion form and the reduction of powers in a non-commutative algebra.
