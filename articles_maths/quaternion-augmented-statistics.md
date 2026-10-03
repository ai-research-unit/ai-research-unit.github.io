# __Quaternion Augmented Statistics__

## Introduction

A quaternion-valued random variable has four real components, and its second-order theory can be written in four ways at once: once for the identity and once for each of the three involutions about the coordinate axes of the quaternion algebra. Written that way the second-order forms are quaternion valued, and the four of them together carry exactly the information of the sixteen real second-order forms of the components; the passage between the two descriptions is an invertible sign transform of Hadamard type. The description is called **augmented** here, and the estimators that are linear in the augmented variables are called **widely linear**, since linearity in the augmented variable is linearity in a wider sense than linearity in the variable itself. This article develops the involutions, the augmented vector, the second-order forms, the duality with the real forms, and the widely linear estimator.

Four boundaries are held.

- The algebra, the basis, the conjugate and the scalar–vector split are those of *Quaternion Algebra*; the norm, the modulus and the inner product are those of *Quaternion Norm and Invertibility*; the inner automorphism $\iota_u$ and the theorem that every automorphism of $\mathbb{H}$ is inner are those of *Quaternion Automorphisms and Derivations*; the reflection $\rho_v = -\iota_v$ and the half-turn reading of $\iota_{e_k}$ are those of *Quaternion Rotations and Reflections*. None of them is restated here.
- The probability is that of Part III. A quaternion-valued random variable, its expectation and its covariance are the notions of *Measure-Theoretic Probability*; the conditional expectation and its description as the $L^2$ projection are those of *Independence and Conditional Expectation*; the sample averages by which the forms below are estimated are those of *Ergodic Theory* and *Laws of Large Numbers and the Central Limit Theorem*.
- The differentiation of the second-order forms, and the least-mean-square optimisation of a widely linear estimator by a gradient, are not done here. They are the subject of the companion article *The Generalised Hamilton–Rodrigues Calculus*, which is the calculus this statistics was built for.
- The Fourier transform of a quaternion-valued function or sequence is *Quaternion Harmonic Analysis*, where the transform theory lives; the spectral theory of a second-order stationary process in the commutative case is *Harmonic Analysis on Groups*. Neither is used here.

No physics is invoked.

Throughout, $\mathbb{H}$ is the quaternion algebra over $\mathbb{R}$ with basis $e_0 = 1, e_1, e_2, e_3$ and $e_1^2 = e_2^2 = e_3^2 = e_1e_2e_3 = -e_0$; a quaternion is $\tilde q = \sum_{\mu=0}^{3}q_\mu e_\mu$ with $\mathrm{Sc}(\tilde q) = q_0$, conjugate $\tilde{q}^{\natural}$, quaternion norm $N(\tilde q) = \tilde q\tilde{q}^{\natural} = \sum_\mu q_\mu^2$, modulus $|\tilde q|$, and inner product $\langle\tilde p,\tilde q\rangle = \mathrm{Sc}(\tilde p\tilde{q}^{\natural}) = \sum_\mu p_\mu q_\mu$. The $e_\mu$-component of $\tilde q$ is written $q_\mu$, so that $\tilde q = \sum_\mu q_\mu e_\mu$. A quaternion-valued random variable is written in lower case with a tilde, $\tilde p,\tilde q$, so that the glyph identifies the ambient algebra, and its expectation $\mathbb{E}[\tilde q] = \sum_\mu\mathbb{E}[q_\mu]e_\mu$ is componentwise. For matrices, ${}^{\mathsf T}$ is the transpose and ${}^{\mathsf H}$ the conjugate transpose, $\bar A^{\mathsf T}$.

## The Involutions about the Axes

### The Three Maps

The inner automorphism determined by a unit $u$, $\iota_u(\tilde q) = u\tilde q u^{-1}$, is an involution exactly when $\iota_{u^2} = \mathrm{id}$, that is when $u^2$ is real: for $u = u_0+\mathbf{u}$ one has $u^2 = u_0^2-N(\mathbf{u})+2u_0\mathbf{u}$, real precisely when $u$ is real or pure imaginary. On the three basis imaginary units this gives three non-trivial involutions, and one writes $\iota_0 = \mathrm{id}$ for the identity.

**Definition.** For $k = 1,2,3$ the **involution about the axis $e_k$** is

$$
\iota_k(\tilde q) = e_k\,\tilde q\,e_k^{-1} = e_k\tilde q e_k , \qquad e_k^{-1} = -e_k ,
$$

and $\iota_0$ is the identity. A map $\iota$ with $\iota^2 = \mathrm{id}$ is an **involution**.

**Proposition.** Each $\iota_k$ is an $\mathbb{R}$-algebra automorphism of $\mathbb{H}$ with $\iota_k^2 = \mathrm{id}$; it fixes the scalar part and the $e_k$-axis, and it negates the two remaining axes. Its fixed subspace is $\{q_0e_0+q_ke_k\}$, of dimension $2$, and its anti-fixed subspace is $\{q_le_l+q_me_m\}$ for $(k,l,m)$ cyclic, also of dimension $2$.

*Proof.* The map $\iota_k$ is an inner automorphism, hence an algebra automorphism, by *Quaternion Automorphisms and Derivations*; its square is the inner automorphism of $e_k^2 = -e_0$, which is the identity, so it is an involution. On the basis, $e_ke_0e_k^{-1} = e_0$, $e_ke_ke_k^{-1} = e_k$, and for $l\neq k$ one has $e_ke_le_k^{-1} = -e_ke_le_k = -e_l$, using $e_ke_l = \varepsilon_{klm}e_m$ and $e_me_k = e_l$ for $(k,l,m)$ cyclic. The fixed and anti-fixed subspaces are read from the four signs.

### The Sign Matrix

**Definition.** The **sign matrix** of the family is the $4\times4$ matrix $\sigma$ with $\iota_j(e_\mu) = \sigma_{j\mu}e_\mu$; it is symmetric, $\sigma_{j\mu} = \sigma_{\mu j}$, and it reads

| | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $\iota_0$ | $+$ | $+$ | $+$ | $+$ |
| $\iota_1$ | $+$ | $+$ | $-$ | $-$ |
| $\iota_2$ | $+$ | $-$ | $+$ | $-$ |
| $\iota_3$ | $+$ | $-$ | $-$ | $+$ |

**Proposition.** The rows of $\sigma$ are pairwise orthogonal, and so are its columns:

$$
\sum_{j=0}^{3}\sigma_{j\mu}\sigma_{j\nu} = 4\delta_{\mu\nu} , \qquad \sum_{\mu=0}^{3}\sigma_{j\mu}\sigma_{m\mu} = 4\delta_{jm} .
$$

*Proof.* Both are read from the table. Each column has either four entries $+1$, when $\mu = 0$, or two entries $+1$ and two $-1$; two distinct columns agree in exactly two rows and differ in the other two, so the scalar product of two distinct columns is $0$, and the scalar product of a column with itself is $4$. The rows are the columns, the matrix being symmetric.

**Remark.** A matrix with entries $\pm1$ whose distinct rows are orthogonal is a **Hadamard matrix**; $\sigma$ is the smallest of order greater than two, and the orthogonality above is the reason the augmented description inverts as cleanly as it does.

### The Involution Group

**Proposition.** The four maps form a group under composition, isomorphic to $\mathbb{Z}/2\times\mathbb{Z}/2$:

$$
\iota_j\iota_m = \iota_{j\oplus m} , \qquad \iota_0\iota_j = \iota_j , \qquad \iota_j^2 = \iota_0 ,
$$

where $\oplus$ is the bitwise exclusive-or on the labels read in binary, so that $1\oplus2 = 3$, $2\oplus3 = 1$ and $3\oplus1 = 2$. In particular the four commute.

*Proof.* On a basis element $e_\mu$ the composition multiplies the two signs, $\sigma_{j\mu}\sigma_{m\mu}$, and the product of two rows of the sign matrix is a row again, with the label $\oplus$; the four rows are the characters of the Klein group.

### Recovering the Coordinates

**Proposition.** Every quaternion is recovered from its four involuted forms,

$$
q_\mu = \frac14\,e_\mu^{-1}\sum_{j=0}^{3}\sigma_{j\mu}\,\iota_j\tilde q , \qquad \mu = 0,1,2,3 ,
$$

and in particular

$$
\tilde{q}^{\natural} = \tfrac12\bigl(\iota_1\tilde q+\iota_2\tilde q+\iota_3\tilde q-\tilde q\bigr) .
$$

*Proof.* For the first, expand $\iota_j\tilde q = \sum_\nu\sigma_{j\nu}q_\nu e_\nu$ and use the column orthogonality; the inner sum becomes $4q_\mu e_\mu$. For the second, the sign pattern $\frac12(\sigma_{1\mu}+\sigma_{2\mu}+\sigma_{3\mu}-\sigma_{0\mu})$ equals $+1$ for $\mu = 0$ and $-1$ for $\mu = 1,2,3$, which is the sign pattern of quaternion conjugation.

The second identity is the reason the involutions may be read as four views of one quaternion: the conjugate, which is the only one of them that reverses products, is a fixed integer combination of the linear ones.

### Distinctness from the Conjugations

**Remark.** The word *involution* is used here for the maps $\iota_k$, and the corpus calls ${}^{\natural}$, $-{}^{\natural}$ and $-\mathrm{id}$ **the three involutions** of the algebra in *Worked Examples in the Quaternion Algebra* and in *The Scalar and Vector Subspaces of $\mathbb{H}$*. The two families are different, and the difference is the point of this article. Each $\iota_k$ is an algebra automorphism, hence linear and multiplicative, and it fixes the scalar line; each of the three conjugations is $\mathbb{R}$-linear and anti-multiplicative, or negates the scalar line, and only $-\mathrm{id}$ among them is an algebra map. What the two families share is order two; what separates them is that the $\iota_k$ are the linear ones and the conjugations are the anti-linear ones. The reflection of *Quaternion Rotations and Reflections* is the negative of an involution here, $\rho_{e_k} = -\iota_k$, because $\rho_v$ already multiplies the scalar line by $-1$ on the whole algebra. The general linear involution, about an arbitrary axis rather than a coordinate axis, is the subject of *Quaternion Involutions and Projections*, where the three maps $\iota_1,\iota_2,\iota_3$ appear as the coordinate instances $\iota_{e_1},\iota_{e_2},\iota_{e_3}$ of the family of one involution per axis line.

### The Involution of a Vector

**Definition.** For a quaternion vector $\tilde q = (\tilde q_1,\dots,\tilde q_n)^{\mathsf T}$ and $j\in\{0,1,2,3\}$, the **involution of the vector** is applied componentwise, $\iota_j\tilde q = (\iota_j\tilde q_1,\dots,\iota_j\tilde q_n)^{\mathsf T}$.

## The Augmented Vector

### Definition

**Definition.** The **augmented vector** of $\tilde q$ is the quaternion four-vector

$$
q^{a} = \begin{pmatrix}\tilde q\\ \iota_1\tilde q\\ \iota_2\tilde q\\ \iota_3\tilde q\end{pmatrix} .
$$

It has four quaternion components, equivalently sixteen real components; the pairing of the four real components of $\tilde q$ with the four involutions is what the next proposition makes explicit.

### The Basis Matrix

**Proposition.** Let $A$ be the $4\times4$ matrix with quaternion entries $A_{j\mu} = \sigma_{j\mu}e_\mu$, that is

$$
A = \begin{pmatrix} e_0 & e_1 & e_2 & e_3 \\ e_0 & e_1 & -e_2 & -e_3 \\ e_0 & -e_1 & e_2 & -e_3 \\ e_0 & -e_1 & -e_2 & e_3 \end{pmatrix} .
$$

Then

$$
q^{a} = A\begin{pmatrix}q_0\\ q_1\\ q_2\\ q_3\end{pmatrix} , \qquad A^{\mathsf H}A = 4I_4 , \qquad A^{-1} = \tfrac14 A^{\mathsf H} ,
$$

so that $(q_0,q_1,q_2,q_3)^{\mathsf T} = \frac14 A^{\mathsf H}q^{a}$.

*Proof.* The product $A(q_0,\dots,q_3)^{\mathsf T}$ has $j$-th entry $\sum_\mu\sigma_{j\mu}q_\mu e_\mu = \iota_j\tilde q$, which is the definition. For the second, $(A^{\mathsf H}A)_{\mu\nu} = \sum_j\overline{A_{j\mu}}A_{j\nu} = \sum_j\sigma_{j\mu}\sigma_{j\nu}e_\mu^{\natural} e_\nu$; the sum vanishes unless $\mu = \nu$, by the column orthogonality, and when $\mu = \nu$ it is $4e_\mu^{\natural} e_\mu = 4e_0$. Multiplying $A^{\mathsf H}A = 4I_4$ on the left by $\frac14A^{\mathsf H}$ turns the second factor into the identity and gives the inverse.

The matrix $A$ is the augmented basis in coordinates: its columns are the four real directions, its rows are the four involuted forms, and the factor $\frac14$ in the inverse is the normalisation of the sign matrix.

### What the Augmentation Adds and What It Does Not

**Proposition.** For every $j$ and every $\mu$, the $e_\mu$-component of $\iota_j\tilde q$ is $\sigma_{j\mu}$ times the $e_\mu$-component of $\tilde q$. Consequently the real spans coincide,

$$
\operatorname{span}_{\mathbb{R}}\{\tilde q,\iota_1\tilde q,\iota_2\tilde q,\iota_3\tilde q\} = \operatorname{span}_{\mathbb{R}}\{q_0,q_1,q_2,q_3\} ,
$$

and both have dimension $4$.

*Proof.* The component statement is $\iota_j(\tilde q)_\mu = \sigma_{j\mu}q_\mu$, read from the sign matrix, so each side of the displayed equality lies in the other; the dimension is four because the identity contributes the four components $q_\mu$ themselves.

**Remark.** The augmentation changes no information: a widely linear expression $\sum_j a_j^{\mathsf T}\iota_j\tilde q$ with quaternion coefficients and a real-linear expression in the four real components are the same class of maps, and the augmented notation is a bookkeeping in which quaternion multiplication acts on the coefficients. What the augmentation adds is not variables but symmetry: the four involuted forms are permuted among themselves by the involutions, so the class of widely linear expressions is closed under them, which the four real components are not.

## Quaternion Random Variables

### The Definition

**Definition.** A **quaternion-valued random variable** on a probability space is a map $\tilde q : \Omega\to\mathbb{H}$ whose four components $\tilde q = q_0e_0+q_1e_1+q_2e_2+q_3e_3$ are real measurable functions, the algebra being identified with $\mathbb{R}^4$ through the basis. The variable is **centred** when $\mathbb{E}[\tilde q] = 0$ and **square-integrable** when $\mathbb{E}[N(\tilde q)] = \sum_\mu\mathbb{E}[q_\mu^2]<\infty$. Two such variables are **jointly Gaussian** when their eight real components are jointly Gaussian in the real sense.

The identification with $\mathbb{R}^4$ carries the probability theory of *Measure-Theoretic Probability* over without change: a quaternion-valued random variable is a real random vector of length four, and its distribution is a Borel measure on $\mathbb{H}$.

### The Second-Order Forms

**Definition.** For centred square-integrable quaternion-valued random variables $\tilde p,\tilde q$, the four **involuted covariances** and the **pseudo-covariance** are

$$
R_k(\tilde p,\tilde q) = \mathbb{E}\bigl[\tilde p\,(\iota_k\tilde q)^{\natural}\bigr] , \quad k = 0,1,2,3 , \qquad P(\tilde p,\tilde q) = \mathbb{E}[\tilde p\tilde q] .
$$

$R_0(\tilde p,\tilde q) = \mathbb{E}[\tilde p\tilde q^{\natural}]$ is the **quaternion covariance**, $R_k(\tilde p,\tilde q)$ for $k\neq0$ is the **$\iota_k$-covariance**, and $P$ is the **pseudo-covariance**; the values at $\tilde p = \tilde q$ are the corresponding variances.

For the identity involution the definition returns the quaternion covariance of *Measure-Theoretic Probability*; the three further forms are the same construction with $\tilde q$ replaced by one of its involuted forms.

**Proposition (symmetry).** For every $k$,

$$
R_k(\tilde q,\tilde p) = (\iota_k\bigl(R_k(\tilde p,\tilde q)\bigr))^{\natural} .
$$

For $k = 0$ this is the Hermitian symmetry $R_0(\tilde q,\tilde p) = (R_0(\tilde p,\tilde q))^{\natural}$ of the quaternion covariance. The pseudo-covariance has no such symmetry; $\mathbb{E}[\tilde q\tilde p]$ is in general neither $\mathbb{E}[\tilde p\tilde q]$ nor its conjugate.

*Proof.* For fixed values, $\iota_k(\tilde p\,(\iota_k\tilde q)^{\natural}) = \iota_k\tilde p\cdot\tilde q^{\natural}$, because $\iota_k$ is an algebra automorphism and $\iota_k\iota_k = \mathrm{id}$; conjugating that gives $\tilde q\,(\iota_k\tilde p)^{\natural}$, and taking expectations is the identity. For the pseudo-covariance, $\mathbb{E}[\tilde p\tilde q]$ and $\mathbb{E}[\tilde q\tilde p]$ are sums of the two orders of the same products, which differ by commutators that need not vanish.

### The Five-Term Relation

**Theorem.** The pseudo-covariance is determined by the four involuted covariances,

$$
P(\tilde p,\tilde q) = \tfrac12\bigl(R_1+R_2+R_3-R_0\bigr)(\tilde p,\tilde q) .
$$

*Proof.* By the recovery of the conjugate, $\frac12(\iota_1\tilde q+\iota_2\tilde q+\iota_3\tilde q-\tilde q) = \tilde q^{\natural}$; conjugation is additive and real-linear, so the second factor of the right-hand side is $(\tilde q^{\natural})^{\natural} = \tilde q$.

**Corollary (four suffice).** Any four of the five forms determine the fifth; the five together carry $20-4 = 16$ independent real numbers, which is the number of real second-order forms of four components.

| Form | Definition | Value from the other four |
|---|---|---|
| $R_0$ | $\mathbb{E}[\tilde p\tilde q^{\natural}]$ | $R_1+R_2+R_3-2P$ |
| $R_1$ | $\mathbb{E}[\tilde p(\iota_1\tilde q)^{\natural}]$ | $2P-R_2-R_3+R_0$ |
| $R_2$ | $\mathbb{E}[\tilde p(\iota_2\tilde q)^{\natural}]$ | $2P-R_1-R_3+R_0$ |
| $R_3$ | $\mathbb{E}[\tilde p(\iota_3\tilde q)^{\natural}]$ | $2P-R_1-R_2+R_0$ |
| $P$ | $\mathbb{E}[\tilde p\tilde q]$ | $\frac12(R_1+R_2+R_3-R_0)$ |

## Second-Order Stationary Sequences

### The Definition

**Definition.** A quaternion-valued sequence $(\tilde q_n)_{n\in\mathbb{Z}}$ of centred square-integrable random variables is **second-order stationary** when each of the five forms $R_k(\tilde q_n,\tilde q_{n-\ell})$ and $P(\tilde q_n,\tilde q_{n-\ell})$ depends only on the lag $\ell$ and not on $n$. The common values

$$
R_k(\ell) = \mathbb{E}\bigl[\tilde q_n\,(\iota_k\tilde q_{n-\ell})^{\natural}\bigr] , \qquad P(\ell) = \mathbb{E}\bigl[\tilde q_n\tilde q_{n-\ell}\bigr] ,
$$

are the five **descriptor sequences** of the sequence: the **autocorrelation** $R_0$, the three **involuted autocorrelations** $R_1,R_2,R_3$, and the **pseudo-autocorrelation** $P$.

The existence of second-order stationary processes indexed by $\mathbb{Z}$ is the stationarity of *Markov Chains and Processes*, and the convergence of the sample averages $\frac1N\sum_n\tilde q_n(\iota_k\tilde q_{n-\ell})^{\natural}$ to the descriptors is the Birkhoff theorem of *Ergodic Theory*. The five-term relation holds at every lag.

### Symmetry in the Lag

**Proposition.** For every $k$ and every $\ell$,

$$
R_k(-\ell) = \overline{\iota_k R_k(\ell)} , \qquad N\bigl(R_k(-\ell)\bigr) = N\bigl(R_k(\ell)\bigr) , \qquad |R_k(-\ell)| = |R_k(\ell)| .
$$

In particular $R_0(-\ell) = \overline{R_0(\ell)}$, and for $k\neq0$ the value at the zero lag satisfies $R_k(0) = \overline{\iota_kR_k(0)}$, so its $e_k$-component vanishes.

*Proof.* The first identity is the symmetry of the previous section applied to the pair $(\tilde q_n,\tilde q_{n+\ell})$, with stationarity. The involution and the conjugation are orthogonal maps of $\mathbb{H}\cong\mathbb{R}^4$, so they preserve both $N$ and $|\cdot|$, which gives the next two. The vanishing of the $e_k$-component is the fixed-space statement of the first identity, since $\tilde q\mapsto\overline{\iota_k\tilde q}$ fixes exactly the quaternions with $q_k = 0$.

**Proposition (pure values).** If every value of the sequence is pure imaginary, then $P(\ell) = -R_0(\ell)$ for every $\ell$, since $\tilde q^{\natural} = -\tilde q$ for pure $\tilde q$, and the pseudo-autocorrelation is then conjugate symmetric, $P(-\ell) = \overline{P(\ell)}$.

*Proof.* The first part is immediate. For the second, both sides run over the same pairs of indices; conjugating $\tilde q_n\tilde q_{n+\ell}$ gives $\tilde q^{\natural}_n\tilde q^{\natural}_{n+\ell}$, which for pure values is $\tilde q_n\tilde q_{n+\ell}$ up to the sign of the product of two pure quaternions, and the two signs agree.

**Remark.** For general values the pseudo-autocorrelation is neither symmetric nor conjugate symmetric, and it is the descriptor that records the non-commutativity of the algebra. By the five-term relation it is not determined by the four involuted autocorrelations alone; exactly four of the five are needed.

### The Descriptor Matrices

**Definition.** For a second-order stationary sequence and $L\geq0$, the **descriptor matrices** are the $(L+1)\times(L+1)$ quaternion matrices with entries $(R_k)_{nm} = R_k(n-m)$ and $(R_P)_{nm} = P(n-m)$ for $0\leq n,m\leq L$.

**Proposition.** Each $R_k$ is a Toeplitz matrix, constant on its diagonals; $R_0$ is Hermitian, $R_0 = R_0^{\mathsf H}$; each $R_k$ with $k\neq0$ satisfies $R_k = \iota_k(R_k^{\mathsf H})$, the involution being applied entrywise; and the pseudo matrix is not symmetric, $R_P^{\mathsf T}\neq R_P$ in general.

*Proof.* The Toeplitz property is the dependence on $n-m$ alone. For $R_0$, the entries $(n,m)$ and $(m,n)$ are $R_0(n-m)$ and $\overline{R_0(n-m)}$ by the lag symmetry, so the matrix is Hermitian. For $R_k$, the same computation carries the involution along, giving $R_k = \iota_k(R_k^{\mathsf H})$. For the pseudo matrix, $R_P^{\mathsf T}$ has entries $P(m-n)$ where $R_P$ has $P(n-m)$; these differ whenever the pseudo-autocorrelation is not symmetric, which is the general case by the previous remark.

| Matrix | Diagonal | Symmetry |
|---|---|---|
| $R_0$ | $R_0(0) = \mathbb{E}[N(\tilde q_n)]$, real and non-negative | Hermitian, $R_0 = R_0^{\mathsf H}$ |
| $R_1,R_2,R_3$ | $R_k(0)$, with vanishing $e_k$-component | $R_k = \iota_k(R_k^{\mathsf H})$ |
| $R_P$ | $P(0) = \mathbb{E}[\tilde q_n^2]$, not real in general | none |

**Remark.** The metrical reading of the table is that $R_0$ is the Gram matrix of the quaternion inner product $\langle\tilde p,\tilde q\rangle = \mathrm{Sc}(\tilde p\tilde q^{\natural})$, hence Hermitian and positive semi-definite; each $R_k$ with $k\neq0$ is the Gram matrix of the same inner product in the involution frame, $(R_k)_{nm} = \langle\tilde q_n,\iota_k\tilde q_m\rangle$; and the pseudo matrix is the Gram matrix of the quaternion-valued bilinear pairing $\tilde p\tilde q$, whose scalar part is the symmetric form $\mathrm{Sc}(\tilde p\tilde q)$ of signature $(1,3)$ and whose vector part is the cross product. The pairing is not an inner product, and that is why its matrix carries no symmetry.

## Duality with the Real Second-Order Structure

### The Sixteen Real Forms

**Definition.** For a second-order stationary sequence with real components $q_0,q_1,q_2,q_3$, the **real autocorrelations** are

$$
r_{\mu\nu}(\ell) = \mathbb{E}\bigl[q_\mu(n)\,q_\nu(n-\ell)\bigr] , \qquad \mu,\nu\in\{0,1,2,3\} .
$$

There are sixteen of them at each lag, and the symmetry $r_{\nu\mu}(\ell) = r_{\mu\nu}(-\ell)$ relates the two signs of the lag; the complete second-order information of the sequence is the sixteen functions.

**Definition.** For $\tilde p,\tilde q\in\mathbb{H}$ put $B_j = \tilde p\,(\iota_j\tilde q)^{\natural}$, and write $B_{j,\mu}$ for the $e_\mu$-component of $B_j$, $j,\mu\in\{0,1,2,3\}$.

### The Diagonal Duality

**Theorem.** For every $\mu$,

$$
p_\mu q_\mu = \frac14\sum_{j=0}^{3}\sigma_{j\mu}\,B_{j,0} .
$$

*Proof.* By the coordinate form of the involutions, $B_{j,0} = \mathrm{Sc}\bigl(\tilde p\,(\iota_j\tilde q)^{\natural}\bigr) = \sum_\nu\sigma_{j\nu}p_\nu q_\nu$. Summing over $j$ with the weights $\sigma_{j\mu}$ and using the row orthogonality leaves $4p_\mu q_\mu$ and nothing else.

The four diagonal real forms are therefore the inverse sign transform of the scalar parts of the four quaternion forms, and the transform is its own inverse up to the factor $4$: it is the Hadamard transform of order four attached to the sign matrix.

### The Off-Diagonal Duality

**Theorem.** Let $k\in\{1,2,3\}$ and let $(k,l,m)$ be cyclic. Then

$$
\frac14\sum_{j=0}^{3}B_{j,k} = q_0p_k , \qquad \frac14\sum_{j=0}^{3}\sigma_{jk}B_{j,k} = -p_0q_k ,
$$

$$
\frac14\sum_{j=0}^{3}\sigma_{jl}B_{j,k} = p_mq_l , \qquad \frac14\sum_{j=0}^{3}\sigma_{jm}B_{j,k} = -p_lq_m .
$$

Together with the diagonal theorem, these formulas express each of the sixteen products $p_\mu q_\nu$ as $\pm\frac14$ times a signed sum of the four entries $B_{0,\kappa},B_{1,\kappa},B_{2,\kappa},B_{3,\kappa}$ for a single $\kappa$.

*Proof.* By the product rule of *Quaternion Algebra*, the product with the conjugate is

$$
\tilde q\tilde p^{\natural} = (q_0p_0+\mathbf q\cdot\mathbf p)+(p_0\mathbf q-q_0\mathbf p-\mathbf q\times\mathbf p) ,
$$

so the $e_k$-component of $\tilde q\tilde p^{\natural}$ is $p_0q_k-q_0p_k-(\mathbf q\times\mathbf p)_k$. Taking $\tilde q = \tilde p$ and $\tilde p = \iota_j\tilde q$, whose components are $q_0$ and $\sigma_{j\nu}q_\nu$, gives

$$
B_{j,k} = q_0p_k-p_0\sigma_{jk}q_k-p_l\sigma_{jm}q_m+p_m\sigma_{jl}q_l ,
$$

with $(k,l,m)$ cyclic, since $(\mathbf q\times\mathbf p)_k = q_lp_m-q_mp_l$. Summing over $j$ with any of the four weight rows $\sigma_{j\cdot}$ kills every term whose indices are not the chosen pair, by the row orthogonality, and leaves exactly one of the four products displayed.

### Consequences

**Corollary.** The sixteen real autocorrelations are determined by the five descriptor sequences, and conversely; the augmented description and the real description of the second-order structure are equivalent, and the passage between them is the sign transform of the two theorems above.

*Proof.* Substituting $\tilde p = \tilde q_n$ and $\tilde q = \tilde q_{n-\ell}$ and taking expectations converts the pointwise identities into identities among the $r_{\mu\nu}(\ell)$ and the $R_k(\ell)$, since expectation is linear and commutes with the fixed signs.

**Remark.** The duality is not a coincidence of dimension four: it states that the four involutions are an orthogonal basis of the real-linear functionals of the pair generated by the quaternion product, so that the sixteen forms $B_{j,\kappa}$ and the sixteen forms $p_\mu q_\nu$ are two bases of the same space of real bilinear forms, related by a Hadamard transform in each variable. Four of the five quaternion forms carry sixteen real numbers, which is the count of the real forms, and the two theorems show the matching is exact.

## Widely Linear Estimation

### The Two Classes

Let $\tilde p$ and the regressor $\tilde q = (\tilde q_1,\dots,\tilde q_m)^{\mathsf T}$ be centred, square-integrable and jointly Gaussian, and let the estimator be chosen by minimising $\mathbb{E}[N(\tilde p-\hat{\tilde p})]$. Two classes are natural. The **linear** class consists of the estimators $\hat{\tilde p} = a^{\mathsf T}\tilde q$ with $a\in\mathbb{H}^m$; the **widely linear** class consists of

$$
\hat{\tilde p} = \sum_{j=0}^{3}a_j^{\mathsf T}\,\iota_j\tilde q = a^{a\mathsf T}q^{a} , \qquad a^{a} = (a_0,a_1,a_2,a_3)^{\mathsf T} ,
$$

which is linear in the augmented regressor; the linear class is the case $a_1 = a_2 = a_3 = 0$. By the span proposition the widely linear class is exactly the class of real-linear functions of the $4m$ real components of the regressor, so no estimator is lost by the restriction to quaternion coefficients, and the gain of the class over the linear one is the gain of the involution frames.

### The Conditional Expectation

**Theorem.** Let $\tilde p$ and $\tilde q$ be centred and jointly Gaussian. Then the conditional expectation is widely linear,

$$
\mathbb{E}[\tilde p\,|\,\tilde q] = g^{\mathsf T}\tilde q+h^{\mathsf T}\iota_1\tilde q+u^{\mathsf T}\iota_2\tilde q+v^{\mathsf T}\iota_3\tilde q ,
$$

with constant quaternion coefficient vectors, and it minimises $\mathbb{E}[N(\tilde p-\hat{\tilde p})]$ over the widely linear class.

*Proof.* Conditioning on $\tilde q$ is conditioning on the $\sigma$-algebra generated by its $4m$ real components; for jointly Gaussian vectors the conditional expectation of one coordinate is an affine function of the conditioning coordinates, and it is linear here because the variables are centred. The conditional expectation of a square-integrable variable is the $L^2$ projection onto the subspace of measurable functions of that algebra, by *Independence and Conditional Expectation*. That subspace contains the regressors and hence, being closed under real-linear combinations, contains their real span, which is the widely linear class by the span proposition; the projection therefore lies in the class and is its minimiser.

### The Coefficient Matrix

**Proposition.** Let $\hat{\tilde p} = \sum_j a_j^{\mathsf T}\iota_j\tilde q$ be widely linear. Then the augmented estimator is $p^{a} = Mq^{a}$, where the $4\times4$ block matrix $M$ has entries $M_{jm} = \iota_j(a_{j\oplus m})$, the four rows being the involutions of the first row in the order permuted by $\oplus$. For the linear subclass the matrix is diagonal, $M = \operatorname{diag}(a_0,\iota_1a_0,\iota_2a_0,\iota_3a_0)$.

*Proof.* Apply $\iota_j$ to the estimator and use that the involution is an algebra automorphism, $\iota_j\iota_n\tilde q = \iota_{j\oplus n}\tilde q$; the coefficient of $\iota_m\tilde q$ in the $j$-th augmented component is then $\iota_j(a_{j\oplus m})$. When $a_1 = a_2 = a_3 = 0$ the entry is non-zero only for $j = m$.

**Remark.** The block matrix exhibits the symmetry that the augmentation adds: its four rows are determined by the first together with the action of the Klein group, and the structure $R_k = \iota_k(R_k^{\mathsf H})$ of the descriptor matrices is the same symmetry on the side of the normal equations.

### Least Squares

**Theorem.** Among the widely linear estimators of $\tilde p$ from $\tilde q$ there is a unique mean-square minimiser, and it is characterised by the orthogonality conditions

$$
\mathbb{E}\bigl[(\tilde p-\hat{\tilde p})\,(\iota_j\tilde q_k)^{\natural}\bigr] = 0 , \qquad j\in\{0,1,2,3\} , \quad k\in\{1,\dots,m\} .
$$

The matrix of the resulting normal equations is built from the descriptors, the inner product of two augmented regressors being

$$
\bigl\langle \iota_j\tilde q_k,\iota_n\tilde q_p\bigr\rangle = \mathrm{Sc}\bigl(R_{j\oplus n}(\tilde q_k,\tilde q_p)\bigr) ,
$$

and the right-hand side is built in the same way from the crossed forms of $\tilde p$ and $\tilde q$.

*Proof.* The mean square error is the square of the norm for the inner product $\langle\tilde p,\tilde q\rangle = \mathrm{Sc}(\tilde p\tilde q^{\natural})$, which makes the square-integrable quaternion-valued random variables a real Hilbert space; the projection theorem gives existence, uniqueness and the orthogonality characterisation. For the inner product identity, $\iota_j\tilde q_k\,(\iota_n\tilde q_p)^{\natural} = \iota_j\bigl(\tilde q_k(\iota_{j\oplus n}\tilde q_p)^{\natural}\bigr)$, which follows from $\iota_j\tilde q^{\natural} = (\iota_j\tilde q)^{\natural}$ and $\iota_j\iota_j = \mathrm{id}$; taking scalar parts removes the involution from the front.

## Worked Example

### The Sequence

Take the three-sample quaternion sequence

$$
\tilde q_0 = -1-10e_1+e_2-e_3 , \qquad \tilde q_1 = -2-4e_1-6e_2+3e_3 , \qquad \tilde q_2 = -4-5e_1+3e_2+e_3 ,
$$

and let each descriptor be the sample average $\frac13\sum_n$ over the pairs of indices at the required separation, the lag convention being $R_k(\ell) = \frac13\sum_n\tilde q_n(\iota_k\tilde q_{n-\ell})^{\natural}$, so that $R_k(\ell)$ compares the value at $n$ with the value at $n-\ell$.

### The Five Descriptor Sequences

At the zero lag,

$$
R_0(0) = 73 , \qquad R_1(0) = 35+4e_2-\tfrac{20}{3}e_3 , \qquad R_2(0) = -\tfrac{85}{3}+\tfrac{44}{3}e_1-\tfrac{16}{3}e_3 ,
$$

$$
R_3(0) = -\tfrac{155}{3}+36e_1-\tfrac{16}{3}e_2 , \qquad P(0) = -59+\tfrac{76}{3}e_1-\tfrac23e_2-6e_3 ,
$$

and at the first two lags,

$$
R_0(1) = \tfrac{46}{3}-\tfrac{40}{3}e_1+\tfrac13e_2+9e_3 , \qquad R_0(2) = \tfrac{56}{3}-\tfrac{31}{3}e_1+\tfrac{16}{3}e_2-10e_3 ,
$$

$$
R_1(1) = \tfrac{94}{3}-\tfrac43e_1+\tfrac{67}{3}e_2+\tfrac{59}{3}e_3 , \qquad R_2(1) = -\tfrac{74}{3}+\tfrac{62}{3}e_1-15e_2-\tfrac{89}{3}e_3 ,
$$

$$
R_3(1) = -\tfrac{26}{3}+\tfrac{38}{3}e_1-\tfrac{23}{3}e_2-\tfrac{17}{3}e_3 , \qquad P(1) = -\tfrac{26}{3}+\tfrac{68}{3}e_1-\tfrac13e_2-\tfrac{37}{3}e_3 .
$$

The values at the negative lags are the involutions of the conjugates of these, and the checks below use them.

### The Symmetries and Their Failures

The involuted autocorrelations are $\iota_k$-conjugate-symmetric at every lag: the value

$$
R_1(-1) = \tfrac{94}{3}+\tfrac43e_1+\tfrac{67}{3}e_2+\tfrac{59}{3}e_3
$$

is $\iota_1(\overline{R_1(1)})$, so at the first lag the pair $R_1(1),R_1(-1)$ differs only in the sign of the $e_1$-component, and the same computation with $e_2$ and $e_3$ in place of $e_1$ gives the other two. At the zero lag the $e_k$-component of $R_k(0)$ vanishes, which is visible in the displayed values: $R_1(0)$ has no $e_1$-component, $R_2(0)$ none in $e_2$, and $R_3(0)$ none in $e_3$.

The magnitudes of the four autocorrelations are symmetric in the lag, $|R_k(-\ell)| = |R_k(\ell)|$, by the same proposition. The pseudo-autocorrelation is not: its modulus is about $27.22$ at the lag one and about $20.48$ at the lag minus one, and it is neither symmetric nor conjugate symmetric. The failure is the non-commutativity of the algebra, and it disappears for pure-imaginary values, whose conjugate is their negative: the pure-imaginary sequence $-10e_1+e_2-e_3$, $-4e_1-6e_2+3e_3$, $-5e_1+3e_2+e_3$ has $P(0) = -66$, the negative of its autocorrelation at the zero lag, and a pseudo-autocorrelation that is conjugate symmetric.

### The Real Description Recovered

The five displayed forms determine the sixteen real autocorrelations of the four component sequences by the two duality theorems, and the check is arithmetic. For the pair $(\tilde q_1,\tilde q_0)$, which is the first lag, the four values $B_j = \tilde q_1(\iota_j\tilde q_0)^{\natural}$ have scalar parts $33,51,-41,-35$, whose signed average $\frac14(33+51-41-35) = 2$ is the diagonal real form $p_0q_0 = (-2)(-1)$, as the diagonal theorem requires; and their $e_1$-components are $-19,-13,33,15$, whose signed average with the weights $\sigma_{j2}$ is $\frac14(-19+13+33-15) = 3$, which is the off-diagonal real form $p_3q_2 = 3\cdot1$, as the off-diagonal theorem requires for $k = 1$, $l = 2$, $m = 3$ and the weight $j' = 2$.

## Summary

A quaternion-valued random variable is described at the second order by four involuted covariances $\mathbb{E}[\tilde p(\iota_k\tilde q)^{\natural}]$, one for the identity and one for each of the three involutions about the coordinate axes, and by the pseudo-covariance $\mathbb{E}[\tilde p\tilde q]$; the five are related by $P = \frac12(R_1+R_2+R_3-R_0)$, so four of them determine the fifth. The involutions form a Klein group, they are linear, they fix the scalar line, and they are not the anti-linear conjugations that the corpus separately calls the involutions of $\mathbb{H}$; the conjugate itself is the fixed combination $\frac12(\iota_1+\iota_2+\iota_3-\mathrm{id})$ of them.

The involutions give the augmented vector $q^{a} = (\tilde q,\iota_1\tilde q,\iota_2\tilde q,\iota_3\tilde q)^{\mathsf T}$, related to the four real components by the basis matrix $A$, with $A^{\mathsf H}A = 4I_4$; the augmentation is a change of basis of the same real span, not an enlargement, and it is the frame in which the quaternion product preserves a finite symmetry. In that frame the descriptor matrices are Toeplitz, the standard one Hermitian and the other three involuted-Hermitian, while the pseudo matrix has no symmetry and records the non-commutativity.

The four involuted forms together with the pseudo-form carry exactly the sixteen real second-order forms of the four components, and the passage is a sign transform of Hadamard type in each variable: the diagonal real forms are the transform of the scalar parts and the twelve off-diagonal ones are the transforms of the imaginary parts, with the signs of the sign matrix. The widely linear estimator $\hat{\tilde p} = \sum_ja_j^{\mathsf T}\iota_j\tilde q$ is exactly the real-linear estimator in the components, its augmented form is a block matrix whose rows are the involutions of the first, and its least-squares solution is the $L^2$ projection, the involuted covariances being the entries of the normal equations.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\iota_k$, $k = 1,2,3$ | Involution about the axis $e_k$, $\iota_k(\tilde q) = e_k\tilde qe_k^{-1}$; $\iota_0 = \mathrm{id}$ |
| $\sigma_{j\mu}$ | Sign matrix, $\iota_j(e_\mu) = \sigma_{j\mu}e_\mu$, a Hadamard matrix of order four |
| $\iota_j\iota_m = \iota_{j\oplus m}$ | Klein group law on the four involutions |
| $q_\mu = \frac14 e_\mu^{-1}\sum_j\sigma_{j\mu}\iota_j\tilde q$ | Recovery of the components from the involuted forms |
| $q^{a} = (\tilde q,\iota_1\tilde q,\iota_2\tilde q,\iota_3\tilde q)^{\mathsf T}$ | Augmented vector |
| $A$, $A_{j\mu} = \sigma_{j\mu}e_\mu$ | Augmented basis matrix, $A^{\mathsf H}A = 4I_4$, $A^{-1} = \frac14A^{\mathsf H}$ |
| $R_k(\tilde p,\tilde q) = \mathbb{E}[\tilde p(\iota_k\tilde q)^{\natural}]$ | Involuted covariances; $R_0$ the quaternion covariance |
| $P(\tilde p,\tilde q) = \mathbb{E}[\tilde p\tilde q]$ | Pseudo-covariance |
| $P = \frac12(R_1+R_2+R_3-R_0)$ | Five-term relation |
| $R_k(\ell)$, $P(\ell)$ | Descriptor sequences of a second-order stationary sequence |
| $R_k(-\ell) = \overline{\iota_kR_k(\ell)}$ | Conjugate-involuted symmetry in the lag |
| $R_k = \iota_k(R_k^{\mathsf H})$ | Involuted-Hermitian structure of the descriptor matrix |
| $r_{\mu\nu}(\ell) = \mathbb{E}[q_\mu(n)q_\nu(n-\ell)]$ | Sixteen real autocorrelations of the components |
| $B_j = \tilde p(\iota_j\tilde q)^{\natural}$, $B_{j,\mu}$ | Forms of the duality; the $e_\mu$-component of $B_j$ |
| $\sum_ja_j^{\mathsf T}\iota_j\tilde q$ | Widely linear estimator |
| $M_{jm} = \iota_j(a_{j\oplus m})$ | Block matrix of the augmented estimator |

## Further Reading

- Todd A. Ell and Stephen J. Sangwine, "Quaternion involutions and anti-involutions", *Computers & Mathematics with Applications* **53** (2007), 137–143, for the involutions $q^{\eta}$ and their algebra.
- Clive Cheong Took and Danilo P. Mandic, "Augmented second-order statistics of quaternion random signals", *Signal Processing* **91** (2011), 214–224, for the augmented statistics and the widely linear model.
- Danilo P. Mandic and Vanessa Su Lee Goh, *Complex Valued Nonlinear Adaptive Filters: Noncircularity, Widely Linear and Neural Models* (Wiley, 2009), for the complex case that the quaternion case generalises.
- Bernard Picinbono, "Second-order complex random vectors and normal distributions", *IEEE Transactions on Signal Processing* **44** (1996), 2637–2640, for the pseudo-covariance and the circularity of the complex case.
- Peter J. Schreier and Louis L. Scharf, *Statistical Signal Processing of Complex-Valued Data: The Theory of Improper and Noncircular Signals* (Cambridge University Press, 2010), for the duality between the complex and the real second-order descriptions.
- John Voight, *Quaternion Algebras* (Springer, 2021), for the algebra and its automorphisms.
