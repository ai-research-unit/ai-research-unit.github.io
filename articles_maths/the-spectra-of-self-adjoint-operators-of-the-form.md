# __The Spectra of Self-Adjoint Operators of the Form__

## Introduction

A self-adjoint operator of a positive definite form on a finite-dimensional object is diagonalisable in an $h$-orthonormal basis and has a **real** spectrum; that is the finite-dimensional spectral theorem, and it is the theorem that makes the operator theory of the layer a theory of *numbers*. The **eigenvalues** of a self-adjoint operator are real, its **eigenspaces** are mutually $h$-orthogonal, the operator is the sum $\sum_{i}\lambda_{i}P_{i}$ of its eigenvalues against the $h$-orthogonal projections onto the eigenspaces, and every continuous function of the operator is obtained by applying the function to the eigenvalues in the same basis. The two consequences developed here are the **min-max (Courant–Fischer) description** of the eigenvalues, which identifies the spectrum with the extreme values of the Rayleigh quotient and makes it computable and comparable, and the **positivity criterion**, which identifies the positive self-adjoint operators with those whose spectrum lies in the positive half-line and supplies the square root used by the polar decomposition.

The spectral theorem is the bridge between the algebra and the analysis of the layer. It converts the self-adjointness of an operator, an algebraic condition, into a statement about the real line; it converts the unitary group, an algebraic group, into a group of transformations of the spectrum; and it converts the positivity of an element, an order-theoretic condition, into a condition on the spectrum. In the definite case the bridge is complete and the spectrum is real; in the indefinite case the self-adjoint operators can have genuinely non-real spectrum — the hyperbolic plane of *The Indefinite Case and the Signature* is the smallest witness — and the finite-dimensional theorem requires the definite hypothesis, which is the reason the theory is developed in the definite case and then transported by the fundamental symmetry.

The article states and proves the finite-dimensional theorem, develops the spectral decomposition and the functional calculus, the min-max principle and the norm identity, the skew-adjoint, normal and unitary spectra, the invariance under the unitary group, and the limits of the theorem in the indefinite case, and it works three cases. The self-adjoint and skew-adjoint operators are *Self-Adjoint and Skew Operators of the Form*; the norm is *The Norm Defined by a Form*; the positivity is *Positivity and the Positive Cone of a Hermitian Form*; the companion transport is *The Fundamental Symmetry of the Form*, §*The Adjoints under the Two Forms*; the square root is used by *The Polar Decomposition of an Operator of the Form*; the indefinite spectral theory is *Spectral Theory on Krein Spaces* and *Definitizable Operators and the Krein–Naĭmark Theorem*; the bilinear counterpart is *The Spectra of Self-Adjoint Operators with Hermitian Adjoint*. Throughout, $A$ is a sesquialgebra with a form in the definite case over a base $(R,\varsigma)$ of one of the two classical kinds of *The Norm Defined by a Form*, with fixed field $k = R^{\varsigma}$ and $R$ complete, $A$ is **free of finite rank over the ordered field $k$ or over $k(\mathrm{i})$**, $h$ is Hermitian, compatible, nonsingular and **positive definite**, and the operators are the $R$-linear endomorphisms of $A$.

## The Definite Case: the Spectral Theorem

### Diagonalisation

Let $h$ be positive definite. By *The Norm Defined by a Form*, §*The Norm and Its Axioms*, the diagonal $\lVert x\rVert^{2} = h(x,x)$ is a norm, and the Gram matrix $H$ of $h$ in a $k$-basis is Hermitian and positive definite. By *The Fundamental Symmetry of the Form*, §*The Gram Operators*, the modulus $|H| = (H^{2})^{1/2}$ is defined, and in the definite case the companion form of the canonical symmetry is the form itself and the symmetry is the identity, so the two Gram matrices agree.

**Theorem (the finite-dimensional spectral theorem).** Let $h$ be positive definite, let $A$ be free of finite rank over $k$ or $k(\mathrm{i})$, and let $T$ be $h$-self-adjoint. Then there is an $h$-orthonormal basis $e_{1},\dots,e_{m}$ of $A$ and real numbers $\lambda_{1},\dots,\lambda_{m}$ with $Te_{i} = \lambda_{i}e_{i}$.

*Proof.* Choose an $h$-orthonormal basis of $A$, which exists by the Gram–Schmidt process because $h$ is positive definite; in it the form has matrix the identity, so the $h$-self-adjointness of $T$ reads $T^{T} = \varsigma(T)$, the classical hermitian condition, and $T$ is a hermitian matrix over $k$ or $k(\mathrm{i})$. The classical finite-dimensional spectral theorem for a hermitian matrix supplies a unitary change of basis in which $T$ is diagonal with real entries; the change of basis is by a matrix that is unitary for the identity form, so the new basis is again $h$-orthonormal. $\square$

**Remark (the theorem is the definite case of a general isometry).** The proof is the finite-dimensional case of the reduction of the article: the $h$-self-adjoint operator is the conjugate, by the isometry of the form, of a euclidean self-adjoint operator, and the two have the same spectrum. In the indefinite case the isometry exists only after the choice of a fundamental decomposition, and the spectrum it transports is the companion spectrum, not the $h$-spectrum, which is the content of the last section.

### The Spectral Decomposition

**Theorem (the spectral decomposition).** In the situation of the theorem, let $\lambda_{1},\dots,\lambda_{r}$ be the distinct eigenvalues and let $P_{i}$ be the $h$-orthogonal projection onto the eigenspace $\{x : Tx = \lambda_{i}x\}$. Then

$$
P_{i}P_{j} = \delta_{ij}P_{i} , \qquad \textstyle\sum_{i=1}^{r} P_{i} = 1 , \qquad P_{i}^{\dagger} = P_{i} , \qquad T = \sum_{i=1}^{r}\lambda_{i}P_{i} .
$$

*Proof.* The eigenspaces of a self-adjoint operator for distinct eigenvalues are $h$-orthogonal: if $Tx = \lambda x$ and $Ty = \mu y$ with $\lambda \neq \mu$, then $\lambda h(x,y) = h(Tx,y) = h(x,Ty) = \mu h(x,y)$, and $h(x,y) = 0$ because $\lambda - \mu$ is invertible in $k$. The projections onto the eigenspaces are therefore $h$-orthogonal, which gives the first two relations, and each is self-adjoint because its image and kernel are $h$-orthogonal complements. The last relation is the diagonalisation read in the eigenbasis. $\square$

**Remark (the projection is the operator, not the vector).** The $P_{i}$ are operators of the form and not elements of the algebra; they are self-adjoint idempotents, and they are the form-layer analogue of the idempotents of the algebra. The distinction is the same as the one between the multiplication $m_{x}$ and the element $x$ in the regular representation of *Self-Adjoint and Skew Operators of the Form*.

### The Functional Calculus

**Theorem (the functional calculus).** For every function $f$ on the spectrum the operator $f(T) = \sum_{i}f(\lambda_{i})P_{i}$ is well defined, the assignment $f \mapsto f(T)$ is an algebra homomorphism, it satisfies $f(T)^{\dagger} = \overline{f}(T)$, it is continuous for the sup norm on the spectrum with the operator norm on $B(A)$, and if $f$ is real and nonnegative then $f(T)$ is self-adjoint and positive.

*Proof.* The definition is a finite sum, so the assignment is well defined and is visibly $k$-linear; the multiplicativity is $f(T)g(T) = \sum f(\lambda_{i})g(\lambda_{i})P_{i}$ by the orthogonality $P_{i}P_{j} = \delta_{ij}P_{i}$. The adjoint statement is the computation $f(T)^{\dagger} = \sum \varsigma(f(\lambda_{i}))P_{i}^{\dagger} = \sum \overline{f}(\lambda_{i})P_{i}$, using $\lambda_{i} \in k$ and the self-adjointness of each $P_{i}$. The norm bound is $\lVert f(T)\rVert \leq \sup_{i}\lvert f(\lambda_{i})\rvert$, and for $f \geq 0$, $h(f(T)x,x) = \sum f(\lambda_{i})h(P_{i}x,x) = \sum f(\lambda_{i})\lVert P_{i}x\rVert^{2} \geq 0$. $\square$

## The Rayleigh Quotient and the Extremal Characterisation

### The Min-Max Principle

Let the form be definite, so that the **Rayleigh quotient**

$$
R_{T}(x) = \frac{h(Tx,x)}{h(x,x)} , \qquad x \neq 0 ,
$$

is defined and real for a self-adjoint $T$.

**Theorem (the min-max principle).** Let $T$ be $h$-self-adjoint with eigenvalues $\lambda_{1} \geq \lambda_{2} \geq \dots \geq \lambda_{m}$, counted with multiplicity. Then for every $k$,

$$
\lambda_{k} = \max_{\dim V = k}\ \min_{0 \neq x \in V} R_{T}(x) = \min_{\dim W = m-k+1}\ \max_{0 \neq x \in W} R_{T}(x) ,
$$

the maximum and the minimum running over the subspaces $V, W$ of $A$ of the stated dimension. In particular $\lambda_{1} = \max_{x \neq 0} R_{T}(x)$ and $\lambda_{m} = \min_{x \neq 0} R_{T}(x)$.

*Proof.* The quotients of the subspaces reduce to the euclidean case by the $h$-orthonormal basis, where the statement is the Courant–Fischer theorem for a hermitian matrix; the Rayleigh quotient is unchanged by the change of basis because both numerator and denominator are computed in the same $h$-orthonormal coordinates. $\square$

### The Spectral Radius and the Norm

**Theorem (the norm of a self-adjoint operator).** For a self-adjoint operator $T$ of a definite form,

$$
\lVert T\rVert = \max_{i}\lvert\lambda_{i}\rvert = \rho(T) ,
$$

the spectral radius, and the maximum modulus is attained at one of the two extreme eigenvalues, $\lVert T\rVert = \max(\lvert\lambda_{1}\rvert, \lvert\lambda_{m}\rvert)$.

*Proof.* In an $h$-orthonormal basis the operator is a diagonal matrix with the eigenvalues on the diagonal, and the operator norm of the form is the norm of *The Norm Defined by a Form*, §*The Adjoint Pairs and the Operator Norm*, which in those coordinates is the euclidean operator norm; for a diagonal matrix that norm is the largest modulus of a diagonal entry. $\square$

## Skew-Adjoint, Normal and Unitary

### The Imaginary Spectrum

**Theorem (the spectrum of a skew-adjoint operator).** Let $T$ be skew-adjoint in the definite finite-dimensional case, $T^{\dagger} = -T$. Then the spectrum of $T$ is purely imaginary, and $T = \mathrm{i}S$ for a unique self-adjoint $S$.

*Proof.* The operator $\mathrm{i}T$ is self-adjoint, because $(\mathrm{i}T)^{\dagger} = \varsigma(\mathrm{i})T^{\dagger}$, and $\varsigma(\mathrm{i}) = -\mathrm{i}$ for the two classical kinds of base; hence $(\mathrm{i}T)^{\dagger} = -\mathrm{i}(-T) = \mathrm{i}T$. The spectrum of the self-adjoint operator $\mathrm{i}T$ is real, and the spectrum of $T = -\mathrm{i}(\mathrm{i}T)$ is that real set multiplied by $-\mathrm{i}$, hence purely imaginary. $\square$

### Normal Operators and Simultaneous Diagonalisation

**Theorem (the normal operators).** A normal operator in the definite finite-dimensional case is diagonalisable in an $h$-orthonormal basis, with eigenvalues in $k(\mathrm{i})$, and a commuting family of self-adjoint operators is simultaneously diagonalised in one $h$-orthonormal basis.

*Proof.* A normal operator commutes with its adjoint, so the two generate a commutative algebra with involution; the classical finite-dimensional spectral theorem for a commuting family of hermitian matrices gives one orthonormal basis diagonalising the family, which in the $h$-orthonormal coordinates is the assertion. $\square$

### The Unitary Group and the Unit Circle

**Theorem (the spectrum of a unitary operator).** Let $U$ be unitary in the definite finite-dimensional case. Then every eigenvalue of $U$ has modulus one, and $U = e^{\mathrm{i}S}$ for a self-adjoint $S$; conversely the exponential of a self-adjoint operator is unitary. The spectrum of $e^{\mathrm{i}S}$ is the image of the spectrum of $S$ under the exponential.

*Proof.* If $Ux = \lambda x$ with $x \neq 0$ then $h(x,x) = h(Ux,Ux) = \lambda\overline{\lambda}\,h(x,x)$, so $\lambda\overline{\lambda} = 1$ and $\lvert\lambda\rvert = 1$. The diagonalisation gives one $h$-orthonormal basis in which $U$ has the eigenvalues $e^{\mathrm{i}\theta_{i}}$ of modulus one on the diagonal, and choosing $\theta_{i}$ real gives a self-adjoint diagonal $S$ with $e^{\mathrm{i}S} = U$; the last clause is the functional calculus applied to the exponential. $\square$

## Invariance under the Unitary Group

**Theorem (the invariance of the spectrum).** Let $U$ be unitary and $T$ an operator in the definite finite-dimensional case. Then $T$ and $UTU^{\dagger}$ have the same spectrum and the same $h$-self-adjointness, normality and unitary properties; and if $T$ is normal, two normal operators are unitarily equivalent if and only if they have the same spectrum.

*Proof.* The assignment $T \mapsto UTU^{\dagger}$ is a conjugation by an invertible operator whose inverse is $U^{\dagger}$, so it preserves the spectrum and the adjoint relations, $UTU^{\dagger}$ having the adjoint $UT^{\dagger}U^{\dagger}$. For the completeness of the invariant, the diagonalisation writes each normal operator as $\sum_{i}\lambda_{i}P_{i}$ with mutually $h$-orthogonal self-adjoint projections; two operators with the same spectrum have the same list of eigenvalues and the same multiplicities, and the unitary sending one eigenbasis to the other conjugates them. $\square$

**Remark (where the invariant stops).** The spectrum is the complete invariant of unitary equivalence for normal operators and only a partial one for general operators, whose Jordan structure is an additional invariant. The comparison with the congruence of forms, whose invariant is the inertia and not the spectrum, is the subject of *Unitary Equivalence and Congruence of Operators of the Form*.

## The Indefinite Case and the Limits of the Theorem

### The Non-Real Spectrum

**Example (the theorem fails without definiteness).** On $A = \mathbb{R}^{2}$ with the indefinite form $h(x,y) = x_{1}y_{1} - x_{2}y_{2}$ and $J = \operatorname{diag}(1,-1)$, the operator $T = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$ is $h$-self-adjoint, as *Self-Adjoint and Skew Operators of the Form* records, and its characteristic polynomial is $\lambda^{2}+1$, so its spectrum is $\{\mathrm{i},-\mathrm{i}\}$: a self-adjoint operator of an indefinite form with no real eigenvalue. The example is the reason the theorem is stated for a definite form and the indefinite theory is stated separately.

### What Survives

Two statements of the definite theory survive the loss of definiteness without change. The first is the pair of identities $TT^{\dagger}$ and $T^{\dagger}T$, which are self-adjoint for every operator $T$ and always have the same spectrum away from zero, because the two products are interchanged by the adjoint and the adjoint is a bijection. The second is the **transport**: by *The Fundamental Symmetry of the Form*, §*The Adjoints under the Two Forms*, a self-adjoint operator of $h$ is a $J$-self-adjoint operator of the companion, and the indefinite spectral theory asks when such an operator is **definitizable**, that is, when some polynomial in it has real spectrum and is of bounded type; the replacement of the spectrum by the $J$-spectrum and the growth of the resolvent are the content of *Spectral Theory on Krein Spaces* and *Definitizable Operators and the Krein–Naĭmark Theorem*, which are not developed here.

## Worked Cases

### The Field

**Example (the field).** Let $A = \mathbb{C}$ with $h(z,w) = z\overline{w}$. The self-adjoint operators are the multiplications $T_{\lambda}$ with $\lambda \in \mathbb{R}$ by *Self-Adjoint and Skew Operators of the Form*, and the one-dimensional spectral theorem writes $T_{\lambda} = \lambda \cdot \mathrm{id}$; the spectrum is the single real number $\lambda$, the Rayleigh quotient is the constant $\lambda$, and the min-max principle is the statement that a constant is its own maximum and minimum. The skew-adjoint operators are the $T_{\mathrm{i}t}$ with $t$ real, of imaginary spectrum, and the unitary operators are the $T_{e^{\mathrm{i}\theta}}$ of the unit circle. The example is the smallest in which the functional calculus is the evaluation of a function at a point.

### The Matrices

**Example (the matrices).** Let $A = M_{n}(\mathbb{C})$ with the trace form $h(X,Y) = \operatorname{tr}(XY^{*})$, identifiable with $\mathbb{C}^{n^{2}}$ as a Hilbert space. The self-adjoint operators of the form include the left multiplications $m_{Z}$ with $Z$ Hermitian, whose spectrum is the spectrum of $Z$ repeated $n$ times; the eigenvalues of $m_{Z}$ are real and its eigenspaces are the matrix eigenspaces of $Z$, so the spectral theorem of the layer is the spectral theorem for the Hermitian matrix $Z$ read on the operator algebra. The unitary group of the form is $U(n^{2})$ by *Unitary and Isometric Operators of the Form*, and the conjugation $m_{Z} \mapsto m_{UZU^{*}}$ by a unitary $U$ realises the invariance of the spectrum on the Hermitian matrices. The example is the model of the article and the smallest in which the multiplicities of the spectrum are visible.

### The Hyperbolic Plane

**Example (the hyperbolic plane).** On $\mathbb{R}^{2}$ with $h(x,y) = x_{1}y_{1} - x_{2}y_{2}$, the operator $T = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$ is $h$-self-adjoint of spectrum $\{\mathrm{i},-\mathrm{i}\}$, and its Rayleigh quotient is $R_{T}(x) = -2x_{1}x_{2}/(x_{1}^{2}-x_{2}^{2})$, which is undefined on the null vectors $x_{1} = \pm x_{2}$ and is unbounded above and below on the rest: the denominator has both signs while the numerator does not control it. The min-max principle therefore has no meaning for this operator, since it needs the quotient to be bounded and to attain its extreme values, and both fail. The example is the smallest in which the two ingredients of the definite theorem — the reality of the spectrum and the good behaviour of the quotient — both fail, and it is the reason the indefinite theory replaces the spectrum by the $J$-spectrum of the companion operator.

## Summary

A self-adjoint operator of a **definite** form on a finite-dimensional object is diagonalisable in an **$h$-orthonormal** basis with **real** eigenvalues, and it is the sum $\sum_{i}\lambda_{i}P_{i}$ of its eigenvalues against the mutually $h$-orthogonal self-adjoint projections onto its eigenspaces; the spectral theorem is the reduction of the $h$-self-adjoint operator to a hermitian matrix by the isometry of the form. The **functional calculus** $f \mapsto f(T) = \sum f(\lambda_{i})P_{i}$ is a homomorphism, and a real nonnegative $f$ gives a self-adjoint positive operator, which is the **positivity criterion** and the source of the square root. The **min-max principle** identifies the eigenvalues with the extreme values of the **Rayleigh quotient** $R_{T}(x) = h(Tx,x)/h(x,x)$, and for a self-adjoint operator $\lVert T\rVert = \rho(T)$ is the largest modulus of an eigenvalue. A **skew-adjoint** operator has **purely imaginary** spectrum, a **normal** operator is diagonalisable with eigenvalues in $k(\mathrm{i})$, and a **unitary** operator has its spectrum on the **unit circle**, with $U = e^{\mathrm{i}S}$ for a self-adjoint $S$. The spectrum is invariant under the unitary group and is the complete invariant of unitary equivalence for normal operators. In the **indefinite** case the theorem fails — the hyperbolic plane gives a self-adjoint operator with spectrum $\{\mathrm{i},-\mathrm{i}\}$ — and the indefinite theory replaces the spectrum by the $J$-spectrum of the companion operator $JT$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $Te_{i} = \lambda_{i}e_{i}$ | the diagonalisation in an $h$-orthonormal basis |
| $T = \sum_{i}\lambda_{i}P_{i}$ | the spectral decomposition, $P_{i}$ the $h$-orthogonal projections |
| $f(T) = \sum_{i}f(\lambda_{i})P_{i}$ | the functional calculus |
| $R_{T}(x) = h(Tx,x)/h(x,x)$ | the Rayleigh quotient |
| $\lambda_{k}$ | the min-max extreme of the Rayleigh quotient over $k$-dimensional subspaces |
| $\lVert T\rVert = \rho(T) = \max_{i}\lvert\lambda_{i}\rvert$ | the norm of a self-adjoint operator |
| $T^{\dagger} = -T \Rightarrow \sigma(T) \subseteq \mathrm{i}\mathbb{R}$ | the imaginary spectrum of a skew-adjoint operator |
| $U^{\dagger}U = 1 \Rightarrow \lvert\lambda\rvert = 1$ | the unit circle of the spectrum of a unitary operator |
| $U = e^{\mathrm{i}S}$, $S^{\dagger} = S$ | the unitary operators are the exponentials of the self-adjoint ones |
| $\sigma(UTU^{\dagger}) = \sigma(T)$ | the invariance of the spectrum under the unitary group |
| $JT$, the $J$-spectrum | the companion operator and its spectrum in the indefinite case |

## Further Reading

- John B. Conway, *A Course in Functional Analysis* (2nd ed., Springer, 1990), for the finite-dimensional spectral theorem, the functional calculus and the Rayleigh quotient.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for self-adjoint, normal and unitary operators and their spectra.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed. (Cambridge University Press, 2013), for the Courant–Fischer theorem, the spectral radius and the hermitian and unitary matrices.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the $J$-self-adjoint operators and the failure of the real spectrum in the indefinite case.
- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for the spectrum of a self-adjoint operator of an indefinite inner product and the definitizable operators.
- Paul R. Halmos, *A Hilbert Space Problem Book* (2nd ed., Springer, 1982), for the smallest counterexamples of the spectral theory and the role of normality.
