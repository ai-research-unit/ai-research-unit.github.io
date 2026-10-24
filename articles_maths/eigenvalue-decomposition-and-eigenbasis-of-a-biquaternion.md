# __Eigenvalue Decomposition and Eigenbasis of a Biquaternion__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is simple and four-dimensional over $\mathbb{C}$. This article reads the **eigenvalue decomposition** of a biquaternion $\tilde Q=Q_te_t+\vec Q$ in the distinct case $Q_x^2+Q_y^2+Q_z^2\neq0$: the writing

$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-,
\qquad
\lambda_\pm=Q_t\pm i\sqrt{Q_x^2+Q_y^2+Q_z^2},
\quad
\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi),
\qquad
\vec\Xi=-\frac{i\vec Q}{\sqrt{Q_x^2+Q_y^2+Q_z^2}}.
$$

Here the coefficients $\lambda_\pm$ are the eigenvalues and the idempotents $\tilde\Pi_\pm$ are the eigenprojections. The eigenvalues are distinct in this regime. The article is the noncommutative counterpart of *Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number* and *Eigenvalue Decomposition and Eigenbasis of a Reduced Biquaternion*. The general definition and the existence theorem are those of *The Eigenvalue Decomposition of an Element*; the biquaternion content is that, in the regime of distinct eigenvalues, the pair is the pair of idempotents of a pure root of $+1$, and the decomposition is the Peirce decomposition attached to that root in *Ideals and Peirce Decompositions of the Biquaternion Algebra*.

**The results.** The spectrum of $\tilde Q=Q_te_t+\vec Q$ is $\{Q_t+i\sqrt{Q_x^2+Q_y^2+Q_z^2},Q_t-i\sqrt{Q_x^2+Q_y^2+Q_z^2}\}$, and in the distinct case $Q_x^2+Q_y^2+Q_z^2\neq0$ the eigenprojections are the two idempotents of the pure root $\vec\Xi=-i\vec Q/\sqrt{Q_x^2+Q_y^2+Q_z^2}$. They are noncentral and vary with $\tilde Q$, the eigenvalue decomposition is the Peirce decomposition relative to that root read on the element, and the diagonal part is the commutative plane $\mathbb{C}[\tilde Q]$. The polynomial calculus is the calculus on $\mathbb{C}[\tilde Q]$, the unit group is the invertible group with a surjective but non-injective eigenvalue map, and the Jordan and nilpotent regimes are the cases with no eigenvalue decomposition. The article also constructs the Q-adapted Peirce basis, the two nilpotents of the mixed corners, and the eigenbasis of left multiplication; it separates the eigenspaces of left multiplication, which are the two right ideals, from the left ideals, which are the spinor spaces. The two minimal left ideals $S_\pm=\mathbb{B}\tilde\Pi_\pm$ are the spinor spaces; each is a complex plane and a spinor is a pair of complex coordinates.

| Question | Answer |
|---|---|
| Algebra | $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, simple |
| Element | $\tilde Q=Q_te_t+\vec Q$ |
| Spectrum | $\sigma(\tilde Q)=\{\lambda_+,\lambda_-\}=\left\{Q_t+i\sqrt{Q_x^2+Q_y^2+Q_z^2},Q_t-i\sqrt{Q_x^2+Q_y^2+Q_z^2}\right\}$ |
| Distinctness | $\lambda_+\neq\lambda_-\iff Q_x^2+Q_y^2+Q_z^2\neq0$ |
| Eigenprojections | $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$, with $\vec\Xi=-i\vec Q/\sqrt{Q_x^2+Q_y^2+Q_z^2}$; they depend on $\tilde Q$ |
| Eigenprojections central? | no |
| Eigenvalue decomposition | $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ |
| Peirce decomposition | $\mathbb{B}=\mathbb{C}\tilde\Pi_+\oplus\mathbb{B}_{+-}\oplus\mathbb{B}_{-+}\oplus\mathbb{C}\tilde\Pi_-$, with two square-zero mixed lines |
| Eigenbasis of $L_{\tilde Q}$ | $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$; diagonal values $(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$ |
| Matrix model | $M_2^Q(\tilde Q)=\operatorname{diag}(\lambda_+,\lambda_-)$; the two columns are $S_+,S_-$ |
| Spinor spaces | $S_\pm=\mathbb{B}\tilde\Pi_\pm\cong\mathbb{C}^2$; two complex spinor coordinates per chirality |
| Unit group | $\mathbb{B}^\times$; the eigenvalue map is surjective, not injective, not a homomorphism |

**Scope.** The eigenbasis construction — the Q-adapted Peirce basis, the two nilpotents and the eigenbasis of $L_{\tilde Q}$ — is in *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*The Q-Adapted Peirce Basis, the Nilpotents, and the Eigenbasis*. This article keeps the eigenvalue decomposition and its consequences, and states where the decomposition exists.

**Conventions.** The notation is fixed in *Conventions in Mathematics*: the base is $e_t,\vec e_x,\vec e_y,\vec e_z$, a general element is $\tilde Q=Q_te_t+\vec Q$ with $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ and complex coefficients, an idempotent is $\tilde\Pi$, a root of $+1$ is $\tilde\Xi$ and a pure root is $\vec\Xi$, and a pure nilpotent is $\vec\Upsilon$. Put $B=\sqrt{Q_x^2+Q_y^2+Q_z^2}$. In the distinct case the Q-adapted basis is $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$, the general element in it is $\tilde Q_{\mathrm{sp}}=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},21}\vec\Upsilon_++Q_{\mathrm{sp},22}\tilde\Pi_-$, and the two spinor spaces are $S_\pm=\mathbb{B}\tilde\Pi_\pm$, with coordinates $(Q_{\mathrm{sp},11},Q_{\mathrm{sp},21})$ on $S_+$ and $(Q_{\mathrm{sp},12},Q_{\mathrm{sp},22})$ on $S_-$. The characteristic polynomial, the spectrum and the eigenvalues $\lambda_\pm=Q_t\pm iB$ are those of *Biquaternion Spectral Theory*, §*The Biquaternion Spectrum*; the root of $+1$, the halving map and the primitive idempotents are those of *Square Roots of One and the Idempotents of the Biquaternion Algebra*, §*The Idempotents*; the four Peirce corners are those of *Ideals and Peirce Decompositions of the Biquaternion Algebra*, §*The Peirce Decompositions*; the centraliser and the diagonal part are those of *The Centraliser and the Diagonal Peirce Part*; the off-diagonal components are those of *Off-Diagonal Peirce Components and Noncentral Idempotents*; the reduced norm and the invertibility criterion are those of *The Biquaternion Algebra and Its Vector Spaces*, §*The Reduced Norm and Invertibility*; the eigenvalue formula and the parity-matched lattice are developed in §*The Algebraic Fibre of the Decomposition* and used in *Biquaternion Elementary Functions*, §*The Eigenvalue Formula*.

**Boundaries.** The split-complex and reduced biquaternion cases are those of *Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number* and *Eigenvalue Decomposition and Eigenbasis of a Reduced Biquaternion*; the quaternion case, with its left and right eigenvalues, is the subject of *Quaternion Spectral Theory*; the exponential and the logarithm built on the decomposition are those of *Biquaternion Elementary Functions*; and the spectral theorem in its general form is that of *Biquaternion Spectral Theory*. The Q-adapted construction, the nilpotents and the spinor spaces are developed here; the standard Peirce decomposition is that of *Ideals and Peirce Decompositions of the Biquaternion Algebra*. The article cites these and does not restate them. The other products of the biquaternion space carry nilpotents and idempotents relative to the product, and are outside its scope.

## The Spectrum and the Characteristic Polynomial

**Definition.** Let $\tilde Q\in\mathbb{B}$. A complex scalar $\mu$ is an **eigenvalue** of $\tilde Q$ if $\tilde Q-\mu e_t$ is not a unit in $\mathbb{B}$; the set of eigenvalues is the **spectrum** $\sigma(\tilde Q)$. This is the definition of *The Eigenvalue Decomposition of an Element*, §*The Eigenvalues of an Element*.

**Notation.** The two eigenvalues are written $\lambda_\pm=Q_t\pm i\sqrt{Q_x^2+Q_y^2+Q_z^2}$ when their values are exhibited, the radical being one of the two square roots. The test scalar of the definition is $\mu$, so the letter $\lambda$ is reserved for the two eigenvalues. The pair is the analogue of $\lambda_\pm=q\pm q'$ of *Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number* and of $\lambda_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown}$ of *Eigenvalue Decomposition and Eigenbasis of a Reduced Biquaternion*.

**The pure root of the vector part.** The square of the vector part is central,
$$
\vec Q^2=-(Q_x^2+Q_y^2+Q_z^2)e_t,
$$
as in *Biquaternion Spectral Theory*, §*The Biquaternion Spectrum*.

Assume $Q_x^2+Q_y^2+Q_z^2\neq0$. Put
$$
\vec U=\frac{\vec Q}{\sqrt{Q_x^2+Q_y^2+Q_z^2}},\qquad \vec\Xi=-i\vec U=-\frac{i\vec Q}{\sqrt{Q_x^2+Q_y^2+Q_z^2}}.
$$
Then $\vec U$ is a pure unit element of the biquaternion layer, $\vec U^2=-e_t$, and $\vec\Xi$ is a pure root of $+1$:
$$
\vec\Xi^2=(-i)^2\vec U^2=e_t.
$$
Conversely $\vec Q=\sqrt{Q_x^2+Q_y^2+Q_z^2}\,\vec U=i\sqrt{Q_x^2+Q_y^2+Q_z^2}\,\vec\Xi$. The root is pure, so it carries the arrow and not the tilde (§*Pure Elements and their Coefficients* of *Conventions in Mathematics*), and it belongs to the roots classified in *Square Roots of One and the Idempotents of the Biquaternion Algebra*, §*The Roots of One*. For a real vector part, the square root may be taken real and positive, $\vec U$ is then the real unit vector $\vec u$, and $\vec\Xi=-i\vec u$ lies in the family $i\vec u$ of the pure roots. More generally, for $Q_x^2+Q_y^2+Q_z^2\neq0$, $\vec U$ is real exactly when $\vec Q$ is a complex multiple of a real vector, equivalently when $\tilde Q$ is normal (§*The Hermitian Case*); otherwise $\vec U$ and $\vec\Xi$ have nonzero imaginary parts.

The choice is two-fold: the negative of a square root is the other square root, and it replaces $\vec U$ and $\vec\Xi$ by their opposites. Only $Q_x^2+Q_y^2+Q_z^2$ is determined by $\tilde Q$, and with it the unordered pair $\{\vec\Xi,-\vec\Xi\}$; in the real case the convention that the square root be positive removes the choice.

**Theorem.** The spectrum of $\tilde Q=Q_te_t+\vec Q$ is
$$
\sigma(\tilde Q)=\{\lambda_+,\lambda_-\},
\qquad
\lambda_\pm=Q_t\pm i\sqrt{Q_x^2+Q_y^2+Q_z^2}.
$$
The radical is one of the two square roots, and the other choice exchanges $\lambda_+$ and $\lambda_-$. In the real case the positive root is taken, $\sqrt{Q_x^2+Q_y^2+Q_z^2}=|\vec Q|>0$.

**Proof.** Since $\vec Q=i\sqrt{Q_x^2+Q_y^2+Q_z^2}\,\vec\Xi$,
$$
(\tilde Q-Q_te_t)^2=\vec Q^2=-(Q_x^2+Q_y^2+Q_z^2)e_t,
$$
hence
$$
\tilde Q^2-2Q_t\tilde Q+\langle\tilde Q\rangle_{\natural}e_t=0,\qquad \langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2.
$$
This is the quadratic identity of *Biquaternion Spectral Theory*, §*The Biquaternion Spectrum*. The reduced norm of $\tilde Q-\mu e_t$ is
$$
(\tilde Q-\mu e_t)(\tilde Q-\mu e_t)^\natural=(Q_t-\mu)^2+Q_x^2+Q_y^2+Q_z^2,
$$
so by *The Biquaternion Algebra and Its Vector Spaces*, §*The Reduced Norm and Invertibility*, $\tilde Q-\mu e_t$ is not a unit exactly when $(Q_t-\mu)^2=-(Q_x^2+Q_y^2+Q_z^2)$, that is exactly when $\mu=\lambda_\pm$.

**Characteristic polynomial.** The characteristic polynomial of $\tilde Q$ is
$$
p_{\tilde Q}(X)=X^2-2Q_tX+\langle\tilde Q\rangle_{\natural}=(X-Q_t)^2+Q_x^2+Q_y^2+Q_z^2.
$$
Its discriminant is
$$
(\lambda_+-\lambda_-)^2=\left(2i\sqrt{Q_x^2+Q_y^2+Q_z^2}\right)^2=-4(Q_x^2+Q_y^2+Q_z^2),
$$
so the eigenvalues are distinct exactly when $Q_x^2+Q_y^2+Q_z^2\neq0$.

**Minimal polynomial.** For $Q_x^2+Q_y^2+Q_z^2\neq0$ the minimal polynomial is $p_{\tilde Q}$, which is squarefree. For $Q_x^2+Q_y^2+Q_z^2=0$, $\vec Q\neq0$, it is $(X-Q_t)^2$; for $\vec Q=0$, it is $X-Q_t$.

The data of the spectrum are collected in the table.

| Quantity | Value |
|---|---|
| Spectrum | $\sigma(\tilde Q)=\{\lambda_+,\lambda_-\}$ |
| Eigenvalues | $\lambda_\pm=Q_t\pm i\sqrt{Q_x^2+Q_y^2+Q_z^2}$ |
| Sum | $\lambda_++\lambda_-=2Q_t$ |
| Product | $\lambda_+\lambda_-=Q_t^2+Q_x^2+Q_y^2+Q_z^2=\langle\tilde Q\rangle_{\natural}$ |
| Discriminant | $(\lambda_+-\lambda_-)^2=-4(Q_x^2+Q_y^2+Q_z^2)$ |
| Characteristic polynomial | $p_{\tilde Q}(X)=X^2-2Q_tX+\langle\tilde Q\rangle_{\natural}=(X-\lambda_+)(X-\lambda_-)$ |
| Minimal polynomial | $(X-Q_t)^2+Q_x^2+Q_y^2+Q_z^2$ if $Q_x^2+Q_y^2+Q_z^2\neq0$; $(X-Q_t)^2$ if $Q_x^2+Q_y^2+Q_z^2=0$, $\vec Q\neq0$; $X-Q_t$ if $\vec Q=0$ |

## The Eigenprojections

**The eigenprojections of a biquaternion with $Q_x^2+Q_y^2+Q_z^2\neq0$ are the two primitive idempotents $\tilde\Pi_\pm$ of the pure root $\vec\Xi$.**

Put
$$
\tilde\Pi_+=\frac12(e_t+\vec\Xi),\qquad \tilde\Pi_-=\frac12(e_t-\vec\Xi),
$$
the two idempotents of the root $\vec\Xi$ under the halving map of *Square Roots of One and the Idempotents of the Biquaternion Algebra*, §*The Idempotents*. By that article the pair is complete and orthogonal, $\tilde\Pi_++\tilde\Pi_-=e_t$ and $\tilde\Pi_+\tilde\Pi_-=0$, and the root is their difference, $\vec\Xi=\tilde\Pi_+-\tilde\Pi_-$; by *Ideals and Peirce Decompositions of the Biquaternion Algebra*, §*Idempotents and Orthogonal Idempotents*, each member is primitive.

They are the eigenprojections of $\tilde Q$:
$$
\tilde Q\tilde\Pi_+=\lambda_+\tilde\Pi_+,\qquad \tilde Q\tilde\Pi_-=\lambda_-\tilde\Pi_-.
$$
Indeed, since $\vec Q=i\sqrt{Q_x^2+Q_y^2+Q_z^2}\,\vec\Xi$ and $\vec\Xi^2=e_t$,
$$
\tilde Q\tilde\Pi_+=(Q_te_t+i\sqrt{Q_x^2+Q_y^2+Q_z^2}\,\vec\Xi)\frac12(e_t+\vec\Xi)=\frac12(Q_t+i\sqrt{Q_x^2+Q_y^2+Q_z^2})(e_t+\vec\Xi)=\lambda_+\tilde\Pi_+,
$$
and, with $Q_t-i\sqrt{Q_x^2+Q_y^2+Q_z^2}$ in place of $Q_t+i\sqrt{Q_x^2+Q_y^2+Q_z^2}$ and $e_t-\vec\Xi$ in place of $e_t+\vec\Xi$,
$$
\tilde Q\tilde\Pi_-=\lambda_-\tilde\Pi_-.
$$

Equivalently, by the eigenprojector formula of *The Lagrange–Sylvester Eigenprojector Formula*, §*The Eigenprojector Formula*,
$$
\tilde\Pi_+=\frac{\tilde Q-\lambda_-e_t}{\lambda_+-\lambda_-},\qquad \tilde\Pi_-=\frac{\tilde Q-\lambda_+e_t}{\lambda_--\lambda_+},\qquad \lambda_+-\lambda_-=2i\sqrt{Q_x^2+Q_y^2+Q_z^2}.
$$
Hence $\tilde\Pi_\pm$ are polynomials in $\tilde Q$, and in particular commute with $\tilde Q$.

**Dependence on the element.** The eigenprojections $\tilde\Pi_\pm$ vary with $\tilde Q$: they are the two idempotents of the pure root $\vec\Xi=-i\vec Q/\sqrt{Q_x^2+Q_y^2+Q_z^2}$, and the root is recovered from them as $\vec\Xi=\tilde\Pi_+-\tilde\Pi_-$. This is the structural difference from the split-complex and reduced biquaternion cases, where the eigenprojections are the fixed central idempotents $\Pi_\pm$ (*Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number*, §*The Eigenprojections*; *Eigenvalue Decomposition and Eigenbasis of a Reduced Biquaternion*, §*The Eigenprojections*). Here the dependence on the element lies in both the eigenvalues and the idempotents.

The pair is collected in the table.

| Idempotent | Definition | Eigenvalue | Properties |
|---|---|---|---|
| $\tilde\Pi_+$ | $\tfrac12(e_t+\vec\Xi)$ | $\lambda_+=Q_t+i\sqrt{Q_x^2+Q_y^2+Q_z^2}$ | $\tilde\Pi_+^2=\tilde\Pi_+$, noncentral, primitive |
| $\tilde\Pi_-$ | $\tfrac12(e_t-\vec\Xi)$ | $\lambda_-=Q_t-i\sqrt{Q_x^2+Q_y^2+Q_z^2}$ | $\tilde\Pi_-^2=\tilde\Pi_-$, noncentral, primitive |

The two idempotents are complementary and orthogonal, $\tilde\Pi_++\tilde\Pi_-=e_t$ and $\tilde\Pi_+\tilde\Pi_-=0$. The construction of the nilpotents $\vec\Upsilon_\pm$ from the two mixed corners, the Q-adapted basis that completes this pair and the eigenbasis of $L_{\tilde Q}$ are in *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*The Peirce Corners and the Nilpotents*, §*The Q-Adapted Peirce Basis* and §*The Eigenbasis of Left Multiplication*.

## The Eigenvalue Decomposition

**Every biquaternion with distinct eigenvalues is the complex linear combination of $\tilde\Pi_+,\tilde\Pi_-$ with its eigenvalues as coefficients.**

Summing the two eigenvalue relations,
$$
\boxed{\ \tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-\ }
=(Q_t+i\sqrt{Q_x^2+Q_y^2+Q_z^2})\tilde\Pi_++(Q_t-i\sqrt{Q_x^2+Q_y^2+Q_z^2})\tilde\Pi_-.
$$

Separating scalar and vector parts,
$$
\tilde Q=\frac{\lambda_++\lambda_-}{2}e_t+\frac{\lambda_+-\lambda_-}{2}\vec\Xi=Q_te_t+i\sqrt{Q_x^2+Q_y^2+Q_z^2}\,\vec\Xi=Q_te_t+\sqrt{Q_x^2+Q_y^2+Q_z^2}\,\vec U.
$$
So the decomposition writes $\tilde Q$ as a complex linear combination of the two primitive idempotents of $\vec\Xi$, with the eigenvalues as coefficients.

This is an eigenvalue decomposition in the sense of *The Eigenvalue Decomposition of an Element*, §*The Eigenvalue Decomposition*: the coefficients $\lambda_\pm$ are distinct, the idempotents $\tilde\Pi_\pm$ are nonzero, orthogonal and complete, and they are the eigenprojections (the eigenprojectors of that article).

**Example.** For $\tilde Q=(1+i)e_t+\vec e_x+i\vec e_y+\vec e_z$, $Q_x^2+Q_y^2+Q_z^2=1$, $\vec U=\vec e_x+i\vec e_y+\vec e_z$ and $\vec\Xi=-i\vec e_x+\vec e_y-i\vec e_z$, so $\tilde\Pi_\pm=\frac12(e_t\pm\vec\Xi)$, and
$$
(1+i)e_t+\vec e_x+i\vec e_y+\vec e_z=(1+2i)\tilde\Pi_++\tilde\Pi_-.
$$
The scalar-vector form confirms it: $\frac{\lambda_++\lambda_-}{2}e_t+\frac{\lambda_+-\lambda_-}{2}\vec\Xi=(1+i)e_t+i\vec\Xi=\tilde Q$.

The data of the decomposition are collected in the table.

| Item | Value |
|---|---|
| Element | $\tilde Q=Q_te_t+\vec Q$ |
| Eigenvalues | $\lambda_\pm=Q_t\pm i\sqrt{Q_x^2+Q_y^2+Q_z^2}$ |
| Eigenprojections | $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$ |
| Decomposition | $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ |
| Distinctness | $\lambda_+\neq\lambda_-\iff Q_x^2+Q_y^2+Q_z^2\neq0$ |
| Diagonal values | $(\lambda_+,\lambda_-)$ in the basis $(\tilde\Pi_+,\tilde\Pi_-)$ |

**Uniqueness.** By the uniqueness theorem of *The Eigenvalue Decomposition of an Element*, §*Uniqueness*, an element with distinct eigenvalues has a unique eigenprojection attached to each eigenvalue. Here the two eigenprojections are the two idempotents of the root $\vec\Xi$, and the root is read back from them as $\vec\Xi=\tilde\Pi_+-\tilde\Pi_-$. The unordered pair $\{\tilde\Pi_+,\tilde\Pi_-\}$ is determined by $\tilde Q$; the ordered pair is determined only up to the exchange that sends the square root to its negative and $\vec\Xi$ to $-\vec\Xi$. The labelling is canonical when the square root is chosen real and positive, which is possible exactly when $Q_x^2+Q_y^2+Q_z^2$ is a positive real number; otherwise the choice of square root is a convention.

**Semisimplicity.** Since $\lambda_+\neq\lambda_-$, the minimal polynomial $p_{\tilde Q}$ is squarefree, and $\tilde Q$ is semisimple (*Nilpotent Elements and the Jordan–Chevalley Decomposition*, §*Semisimple Elements*). The decomposition is the diagonalisation of $\tilde Q$ with respect to the noncentral idempotents $\tilde\Pi_\pm$.

## The Peirce Decomposition Relative to the Eigenprojection

**The Peirce decomposition relative to $\tilde\Pi_+$ has two diagonal lines and two square-zero mixed lines, and its diagonal part is the centraliser of $\tilde Q$.**

Let
$$
\mathbb{B}_{\sigma\tau}=\tilde\Pi_\sigma\mathbb{B}\tilde\Pi_\tau,\qquad \sigma,\tau\in\{+,-\},
$$
be the Peirce corners of the pair, in the notation of *Ideals and Peirce Decompositions of the Biquaternion Algebra*, §*The Biquaternion Case*. The Peirce decomposition is
$$
\mathbb{B}=\mathbb{B}_{++}\oplus\mathbb{B}_{+-}\oplus\mathbb{B}_{-+}\oplus\mathbb{B}_{--}.
$$
Each corner is one complex line, the diagonal corners are $\mathbb{C}\tilde\Pi_+$ and $\mathbb{C}\tilde\Pi_-$, and the two mixed corners are square-zero. This is the decomposition attached to the root $\vec\Xi=-i\vec Q/\sqrt{Q_x^2+Q_y^2+Q_z^2}$ in §*The Peirce Decomposition* of that article.

The four corners are collected in the table.

| Corner | Definition | Value | Dimension over $\mathbb{C}$ |
|---|---|---|---|
| $\mathbb{B}_{++}$ | $\tilde\Pi_+\mathbb{B}\tilde\Pi_+$ | $\mathbb{C}\tilde\Pi_+$ | $1$ |
| $\mathbb{B}_{+-}$ | $\tilde\Pi_+\mathbb{B}\tilde\Pi_-$ | one complex line, square-zero | $1$ |
| $\mathbb{B}_{-+}$ | $\tilde\Pi_-\mathbb{B}\tilde\Pi_+$ | one complex line, square-zero | $1$ |
| $\mathbb{B}_{--}$ | $\tilde\Pi_-\mathbb{B}\tilde\Pi_-$ | $\mathbb{C}\tilde\Pi_-$ | $1$ |

The diagonal part is
$$
\mathbb{B}_{++}\oplus\mathbb{B}_{--}=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\tilde\Pi_-=\mathbb{C}[\tilde Q]=\operatorname{span}_{\mathbb{C}}\{e_t,\tilde Q\}.
$$
It is a commutative subalgebra isomorphic to $\mathbb{C}\times\mathbb{C}$. By *The Centraliser and the Diagonal Peirce Part*, §*The theorem*, applied to the eigenvalue decomposition, it is the centraliser of $\tilde Q$; by *Off-Diagonal Peirce Components and Noncentral Idempotents*, §*The Commutator Interpretation*, the mixed part is $[\tilde\Pi_+,\mathbb{B}]$, so an element commutes with $\tilde Q$ exactly when its two mixed Peirce components vanish.

On $\tilde Q$ the Peirce decomposition reads
$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-,
$$
with zero mixed components. The eigenvalue decomposition is therefore the Peirce decomposition read on the element: the element lies in the diagonal part, and its two diagonal Peirce coordinates are its eigenvalues $Q_t\pm i\sqrt{Q_x^2+Q_y^2+Q_z^2}$. The mixed corners are the directions that fail to commute with $\tilde Q$.

The two signs of the pair are the two eigenvalues of multiplication by the root: an element of $\mathbb{B}_{\sigma\tau}$ is multiplied by $\sigma$ on the left and by $\tau$ on the right by $\vec\Xi$ (§*The Biquaternion Case*). The diagonal corners are the components on which the two signs agree; $\tilde Q$ acts on them by $\lambda_+$ and $\lambda_-$ respectively. The construction of the mixed generators $\vec\Upsilon_\pm$ is the subject of §*The Peirce Corners and the Nilpotents*; the Q-adapted basis and the eigenbasis of left multiplication are the subject of §*The Q-Adapted Peirce Basis* and §*The Eigenbasis of Left Multiplication*.

## Powers, Polynomial Calculus, and the Group of Units

**The eigenvalue decomposition carries the polynomial calculus and the inverse, and it describes the eigenvalue map of the unit group.**

By Sylvester's formula of *The Lagrange–Sylvester Eigenprojector Formula*, §*Sylvester's Formula*, every polynomial $f\in\mathbb{C}[X]$ acts by $f(\tilde Q)=f(\lambda_+)\tilde\Pi_++f(\lambda_-)\tilde\Pi_-$; the calculus and its truncation on $B^2=0$ are in *Biquaternion Elementary Functions*, §*The Eigenvalue Formula*. In this regime, when $\tilde Q$ is a unit, the two eigenvalues are nonzero, since $\lambda_+\lambda_-=\langle\tilde Q\rangle_{\natural}\neq0$ (*The Biquaternion Algebra and Its Vector Spaces*, §*The Reduced Norm and Invertibility*), and the formula extends to negative powers:
$$
\tilde Q^{-1}=\lambda_+^{-1}\tilde\Pi_++\lambda_-^{-1}\tilde\Pi_-.
$$
The result agrees with the inverse formula $\tilde Q^{-1}=\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$ of that article, since $\lambda_+\lambda_-=\langle\tilde Q\rangle_{\natural}$ and $\lambda_-\tilde\Pi_++\lambda_+\tilde\Pi_-=Q_te_t-\sqrt{Q_x^2+Q_y^2+Q_z^2}\,\vec U=\tilde Q^{\natural}$.

**The group of units.** The eigenvalue map
$$
\mathbb{B}^{\times}\longrightarrow\mathbb{C}^{\times}\times\mathbb{C}^{\times},
\qquad
\tilde Q\longmapsto(\lambda_+,\lambda_-)
$$
is surjective, because $\lambda_+\lambda_-=\langle\tilde Q\rangle_{\natural}$ and every pair of nonzero complex numbers occurs. It is not injective: two units with the same eigenvalues differ by an element of the mixed Peirce part $\mathbb{B}_{+-}\oplus\mathbb{B}_{-+}$. It is not a group homomorphism either, because the eigenvalues of a product are not determined by the eigenvalues of the factors. The polynomial calculus is a statement about the diagonal part $\mathbb{C}[\tilde Q]$, where the eigenvalues are coordinates; it does not extend as a coordinatewise calculus to the whole unit group.

The results are collected in the table.

| Operation | Formula | Validity |
|---|---|---|
| Powers | $\tilde Q^n=\lambda_+^n\tilde\Pi_++\lambda_-^n\tilde\Pi_-$ | $n\geq0$ |
| Polynomials | $f(\tilde Q)=f(\lambda_+)\tilde\Pi_++f(\lambda_-)\tilde\Pi_-$ | every $f\in\mathbb{C}[X]$ |
| Inverse | $\tilde Q^{-1}=\lambda_+^{-1}\tilde\Pi_++\lambda_-^{-1}\tilde\Pi_-$ | $\tilde Q$ a unit |
| Unit criterion | $\tilde Q\in\mathbb{B}^\times\iff\lambda_+\lambda_-\neq0$ | — |
| Group of units | $\mathbb{B}^\times$; the eigenvalue map $\tilde Q\mapsto(\lambda_+,\lambda_-)$ is surjective, not injective, not a homomorphism | — |

## The Algebraic Fibre of the Decomposition

**The eigenvalue coordinates and the basis coordinates are two linear coordinate systems on the same diagonal part.**

Fix the ordered pair $(\tilde\Pi_+,\tilde\Pi_-)$, equivalently the root $\vec\Xi=\tilde\Pi_+-\tilde\Pi_-$. The fibre of the map that sends an element with distinct eigenvalues to its ordered pair of eigenprojections is the set of elements $\mu_+\tilde\Pi_++\mu_-\tilde\Pi_-$ with $\mu_+\neq\mu_-$. Every element of the plane $\mathbb{C}[\tilde Q]$ is
$$
\tilde Q_4=\mu_+\tilde\Pi_++\mu_-\tilde\Pi_-,\qquad \mu_\pm\in\mathbb{C},
$$
and the map $(\mu_+,\mu_-)\mapsto\tilde Q_4$ is a $\mathbb{C}$-linear isomorphism $\mathbb{C}^2\to\mathbb{C}[\tilde Q]$.

For $\mu_+\neq\mu_-$ this is the eigenvalue decomposition of $\tilde Q_4$, with the eigenprojections $\tilde\Pi_\pm$ and the eigenvalue data $(\mu_+,\mu_-)$. For $\mu_+=\mu_-=a$ the element is $\tilde Q_4=ae_t$, scalar; the writing is still valid but every complete orthogonal pair gives it, so the two-projector pair is not determined by $\tilde Q_4$, although the eigenprojection $e_t$ of the one-term decomposition is. The eigenvalue decomposition is then the one-term writing $\tilde Q_4=ae_t$ of §*The Scalar Regime*.

For $\mu_+\neq\mu_-$ the unordered pair $\{\mu_+,\mu_-\}$ is the spectrum, and with the pair of idempotents fixed the coordinate map to the unordered spectrum is two-to-one: the two preimages of $\{\mu_+,\mu_-\}$ are $\mu_+\tilde\Pi_++\mu_-\tilde\Pi_-$ and $\mu_-\tilde\Pi_++\mu_+\tilde\Pi_-$, which differ by $(\mu_+-\mu_-)(\tilde\Pi_+-\tilde\Pi_-)\neq0$. For eigenvalues constrained to subsets $S_\pm\subseteq\mathbb{C}$, the corresponding elements are
$$
\{\mu_+\tilde\Pi_++\mu_-\tilde\Pi_-:\ \mu_+\in S_+,\ \mu_-\in S_-\}.
$$

### The Coordinate Change to Basis Coordinates

The scalar and vector coordinates of $\tilde Q_4$ are
$$
\tilde Q_4=\frac{\mu_++\mu_-}{2}e_t+\frac{\mu_+-\mu_-}{2}\vec\Xi=ae_t+\Theta\vec U,
\qquad a=\frac{\mu_++\mu_-}{2},\quad \Theta=\frac{\mu_+-\mu_-}{2i},
$$
the second equality using $\vec\Xi=-i\vec U$. The map $(\mu_+,\mu_-)\mapsto(a,\Theta)$ is a $\mathbb{C}$-linear isomorphism of $\mathbb{C}^2$; the scalar $a$ is the scalar part and $\Theta$ is the complex angle along the axis $\vec U$ used in *Biquaternion Elementary Functions*, §*The Eigenvalue Formula*. The two coordinate systems are the eigenvalue coordinates and the basis coordinates on the same diagonal part. They are compared in the table.

| Coordinate system | Coordinates | Element | Eigenvalues |
|---|---|---|---|
| Eigenvalue coordinates | $(\mu_+,\mu_-)$ | $\tilde Q_4=\mu_+\tilde\Pi_++\mu_-\tilde\Pi_-$ | $\mu_+,\mu_-$ |
| Basis coordinates | $(a,\Theta)$ | $\tilde Q_4=ae_t+\Theta\vec U$ | $\lambda_\pm=a\pm i\Theta$ |
| Change | $\mu_\pm=a\pm i\Theta$; $a=(\mu_++\mu_-)/2$, $\Theta=(\mu_+-\mu_-)/(2i)$ | — | — |

In the Q-adapted basis of *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*The Q-Adapted Peirce Basis, the Nilpotents, and the Eigenbasis*, the Peirce coordinates of $\tilde Q_4$ are $(\mu_+,\mu_-)$. The eigenvalue coordinates $(\mu_+,\mu_-)$ are therefore the diagonal Peirce coordinates, and the basis coordinates $(a,\Theta)$ are the same data written in the scalar-vector basis $(e_t,\vec U)$.

### The Lattice of Eigenvalue Data

The eigenvalue coordinates in $2\pi i\mathbb{Z}^2$ give
$$
L=\bigl\{2\pi i k_+\tilde\Pi_++2\pi i k_-\tilde\Pi_-:\ k_\pm\in\mathbb{Z}\bigr\}.
$$
Using $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$,
$$
2\pi i k_+\tilde\Pi_++2\pi i k_-\tilde\Pi_-=\pi i(k_++k_-)e_t+\pi i(k_+-k_-)\vec\Xi.
$$
With $m=k_++k_-$ and $n=k_+-k_-$ one has $m-n=2k_-$, so $m\equiv n\pmod2$; conversely every pair $(m,n)$ of the same parity comes from the integers $k_\pm=(m\pm n)/2$. Hence
$$
L=\bigl\{\pi i m\,e_t+\pi i n\,\vec\Xi:\ m,n\in\mathbb{Z},\ m\equiv n\pmod2\bigr\}
=\bigl\{\pi i m\,e_t+\pi n\,\vec U:\ m,n\in\mathbb{Z},\ m\equiv n\pmod2\bigr\}.
$$
This is the parity-matched lattice. In this regime it is the kernel of the exponential on the diagonal part, and *Biquaternion Elementary Functions*, §*The Eigenvalue Formula*, uses it for the logarithm. It is not the rectangular lattice $2\pi i\mathbb{Z}e_t\oplus2\pi\mathbb{Z}\vec U$: the rectangular lattice is the sublattice of index two in $L$ on which $m$ and $n$ are both even, the other coset is $\pi i e_t+\pi\vec U$, and the scalar and the vector coordinate cannot be chosen independently, because the idempotents $\tilde\Pi_\pm$ mix the two directions.

### The Hermitian Case

**The eigenprojections are Hermitian exactly when $\vec U$ is real, and the decomposition is then the spectral theorem.**

Two further notions enter. Hermitian conjugation is the star, and normality is the condition $\tilde Q\tilde Q^{*}=\tilde Q^{*}\tilde Q$, as in *Biquaternion Spectral Theory*, §*Hermitian and Normal Elements* (§*The Conjugations* of *Conventions in Mathematics*). The proposition below identifies the case in which the pair is Hermitian.

**Proposition.** Let $Q_x^2+Q_y^2+Q_z^2\neq0$. The following are equivalent: (i) $\tilde\Pi_\pm$ are Hermitian; (ii) $\vec U$ is real; (iii) $\vec\Xi$ is purely imaginary; (iv) $\tilde Q$ is normal.

**Proof.** Since $\vec\Xi=-i\vec U$ and $\vec\Xi^{*}=-\overline{\vec\Xi}$,
$$
\tilde\Pi_\pm^{*}=\frac12\bigl(e_t\pm\vec\Xi^{*}\bigr)=\frac12\bigl(e_t\mp i\overline{\vec U}\bigr),
$$
so (i) holds exactly when $\overline{\vec U}=\vec U$, which is (ii); and (ii) and (iii) are the same condition, since $\vec U=i\vec\Xi$. If (ii) holds, then $\tilde Q^{*}=\overline{Q_t}e_t-\overline{\sqrt{Q_x^2+Q_y^2+Q_z^2}}\,\vec U$ lies in $\mathbb{C}[\tilde Q]$, so $\tilde Q$ commutes with $\tilde Q^{*}$ and (iv) holds. Conversely, if (iv) holds, Theorem 11.2 of *Biquaternion Spectral Theory*, §*The Spectral Theorem*, writes $\tilde Q=\lambda_1\tilde\Pi_1+\lambda_2\tilde\Pi_2$ with Hermitian idempotents; since $Q_x^2+Q_y^2+Q_z^2\neq0$ the eigenvalues are distinct, and the formulas of that theorem identify $\tilde\Pi_1,\tilde\Pi_2$ with $\tilde\Pi_\pm$, so (i) holds.

The pair is then the Hermitian pair of the root $\vec\Xi=-i\vec u$ over a real unit vector $\vec u$ (§*The Families of Idempotents* of *Square Roots of One and the Idempotents of the Biquaternion Algebra*), and the decomposition is the spectral theorem of *Biquaternion Spectral Theory*, §*The Spectral Theorem*, read in the biquaternion algebra. When in addition $\tilde Q$ is Hermitian, $Q_t\in\mathbb{R}$ and $\vec Q=i\vec q'$ with $\vec q'$ real, and the square root of $Q_x^2+Q_y^2+Q_z^2$ is $i|\vec q'|$, so that $\lambda_\pm=Q_t\mp|\vec q'|$ are real.

## Degenerate Regimes

The eigenvalue decomposition exists exactly when the minimal polynomial is split and squarefree (*The Eigenvalue Decomposition of an Element*, §*Existence and Uniqueness*). The spectrum separates the cases as follows. For $Q_x^2+Q_y^2+Q_z^2\neq0$ the minimal polynomial is $p_{\tilde Q}=(X-Q_t)^2+Q_x^2+Q_y^2+Q_z^2$, which is squarefree: the element is semisimple, with distinct eigenvalues, and the decomposition exists. When in addition $\langle\tilde Q\rangle_{\natural}=0$, one eigenvalue vanishes: this is the zero-divisor regime. For $Q_x^2+Q_y^2+Q_z^2=0$ the characteristic polynomial is $(X-Q_t)^2$; the minimal polynomial is $(X-Q_t)^2$ when $\vec Q\neq0$, and $X-Q_t$ when $\vec Q=0$. The first splits by the scalar part, and neither part admits an eigenvalue decomposition: it is the Jordan regime when $Q_t\neq0$, a unit with a single Jordan block, and the nilpotent regime when $Q_t=0$, a non-zero nilpotent on the null cone. The second is the scalar regime, with the one-term decomposition.

| Regime | Condition | Spectrum | Eigenvalue decomposition |
|---|---|---|---|
| Distinct | $Q_x^2+Q_y^2+Q_z^2\neq0$, $\langle\tilde Q\rangle_{\natural}\neq0$ | $\{\lambda_+,\lambda_-\}$ | $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ |
| Zero divisor | $Q_x^2+Q_y^2+Q_z^2\neq0$, $\langle\tilde Q\rangle_{\natural}=0$ | $\{2Q_t,0\}$ | $\tilde Q=2Q_t\tilde\Pi_\sigma$ |
| Scalar | $\vec Q=0$ | $\{Q_t\}$ | $\tilde Q=Q_te_t$ |
| Jordan | $Q_x^2+Q_y^2+Q_z^2=0$, $\vec Q\neq0$, $Q_t\neq0$ | $\{Q_t\}$ | none; the element is a unit |
| Nilpotent | $Q_x^2+Q_y^2+Q_z^2=0$, $\vec Q\neq0$, $Q_t=0$ | $\{0\}$ | none; the element is a nonzero zero divisor |

### The Three Regimes of the Cone

Off the vertex, the cone splits into the scalar regime ($\vec Q=0$), the Jordan regime ($Q_t\neq0$) and the nilpotent regime ($Q_t=0$); the spectrum, the minimal polynomial, the centraliser and the adapted Peirce decomposition of each are those of *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*The Three Regimes of the Cone*.

- **Scalar.** One eigenvalue $Q_t$, minimal polynomial $X-Q_t$, central element: the decomposition has one term, $\tilde Q=Q_te_t$, and a two-projector refinement exists but is not determined by $\tilde Q$.
- **Jordan.** One eigenvalue $Q_t$, minimal polynomial $(X-Q_t)^2$, a unit with a single Jordan block: no eigenvalue decomposition.
- **Nilpotent.** Spectrum $\{0\}$, minimal polynomial $X^2$, a non-zero zero divisor: no eigenvalue decomposition.

## Remarks

1. **Relation to the Lagrange–Sylvester formula.** The formulas for $\tilde\Pi_\pm$ are the Lagrange–Sylvester formulas applied to the quadratic $p_{\tilde Q}$: they are the eigenprojections of the multiplication $L_{\tilde Q}$ on the commutative plane $\mathbb{C}[\tilde Q]$. The biquaternion-specific content is the identification of the eigenprojections with the idempotents of a pure root of $+1$, and of the eigenvalue data with the scalar part and the complex angle along $\vec U$.

2. **Centrality and the Peirce decomposition.** The idempotents $\tilde\Pi_\pm$ are noncentral: they commute with $\tilde Q$ and with its centraliser, but not with all of $\mathbb{B}$. There is no nontrivial central idempotent in $\mathbb{B}$, since the algebra is simple (§*The Two-Sided Ideals* of *Ideals and Peirce Decompositions of the Biquaternion Algebra*). The decomposition is therefore a Peirce decomposition relative to an element-dependent idempotent, not a decomposition of the algebra into ideals.

3. **Uniqueness and labelling.** The decomposition is canonical only as the unordered set of pairs $\{(\lambda_+,\tilde\Pi_+),(\lambda_-,\tilde\Pi_-)\}$. The labelling is interchanged by replacing the square root by its negative and sending $\vec\Xi$ to $-\vec\Xi$; it is fixed by the convention of §*The Eigenvalue Decomposition* exactly when the square root can be taken real and positive.

4. **Degenerate regimes.** The eigenvalue decomposition is a property of semisimple elements; the number of its terms is the number of distinct eigenvalues. The zero-divisor regime is semisimple with one eigenvalue zero and keeps a two-term decomposition. The Jordan and nilpotent regimes are non-semisimple and admit none. The scalar regime is semisimple with a repeated eigenvalue: the general decomposition has one term, and any two-projector refinement is non-unique.

5. **The commutative cases.** The split-complex and reduced biquaternion decompositions are the two commutative shadows of the present one: their eigenprojections are central and fixed, the Peirce corners reduce to the two diagonal lines, and the unit group is a direct product. The biquaternion-specific phenomena are the noncentrality of $\tilde\Pi_\pm$, the two square-zero mixed corners, and the failure of the eigenvalue map to be injective or a homomorphism.

## Summary

For a biquaternion with $Q_x^2+Q_y^2+Q_z^2\neq0$, the eigenvalue decomposition is the writing
$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-,
\qquad
\lambda_\pm=Q_t\pm i\sqrt{Q_x^2+Q_y^2+Q_z^2},
\qquad
\tilde\Pi_\pm=\frac12(e_t\pm\vec\Xi).
$$
Here the radical is $\sqrt{Q_x^2+Q_y^2+Q_z^2}$, equal to $|\vec Q|$ in the real case, and $\vec\Xi=-i\vec Q/\sqrt{Q_x^2+Q_y^2+Q_z^2}$ is the pure root of $+1$ of the vector part. The eigenvalues are distinct, the idempotents are primitive, orthogonal and complete, and they are the eigenprojections. The decomposition is unique up to the exchange of the two labels.

### Main Results

| Result | Expression |
|---|---|
| Spectrum | $\sigma(\tilde Q)=\{\lambda_+,\lambda_-\}=\left\{Q_t+i\sqrt{Q_x^2+Q_y^2+Q_z^2},Q_t-i\sqrt{Q_x^2+Q_y^2+Q_z^2}\right\}$ |
| Characteristic polynomial | $p_{\tilde Q}(X)=X^2-2Q_tX+\langle\tilde Q\rangle_{\natural}=(X-\lambda_+)(X-\lambda_-)$ |
| Distinctness | $\lambda_+\neq\lambda_-\iff Q_x^2+Q_y^2+Q_z^2\neq0$ |
| Eigenprojections | $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$ |
| Eigenvalue decomposition | $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-=(Q_t+i\sqrt{Q_x^2+Q_y^2+Q_z^2})\tilde\Pi_++(Q_t-i\sqrt{Q_x^2+Q_y^2+Q_z^2})\tilde\Pi_-$ |
| Peirce decomposition | $\mathbb{B}=\mathbb{C}\tilde\Pi_+\oplus\mathbb{B}_{+-}\oplus\mathbb{B}_{-+}\oplus\mathbb{C}\tilde\Pi_-$ |
| Eigenbasis of $L_{\tilde Q}$ | $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$; the eigenvalues in this order are $\lambda_+,\lambda_+,\lambda_-,\lambda_-$ |
| Action on the eigenbasis | $L_{\tilde Q}$ has the values $\lambda_+,\lambda_+,\lambda_-,\lambda_-$ on $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$; $R_{\tilde Q}$ has the values $\lambda_+,\lambda_-,\lambda_+,\lambda_-$; a general $\tilde Q_{\mathrm{sp}}$ mixes the two spinor spaces |
| Nilpotents | $\vec\Upsilon_\pm$, with $\vec\Upsilon_\pm^2=0$ |
| Spinor spaces | $S_\pm=\mathbb{B}\tilde\Pi_\pm\cong\mathbb{C}^2$; spinors $(Q_{\mathrm{sp},11},Q_{\mathrm{sp},21})$ on $S_+$ and $(Q_{\mathrm{sp},12},Q_{\mathrm{sp},22})$ on $S_-$ |
| Matrix model | $M_2^Q(\tilde Q)=\operatorname{diag}(\lambda_+,\lambda_-)$; $M_2^Q(P)=\begin{pmatrix}Q_{\mathrm{sp},11}&Q_{\mathrm{sp},12}\\Q_{\mathrm{sp},21}&Q_{\mathrm{sp},22}\end{pmatrix}$; the two columns are $S_+,S_-$ |
| Polynomial calculus | $f(\tilde Q)=f(\lambda_+)\tilde\Pi_++f(\lambda_-)\tilde\Pi_-$ |
| Group of units | $\mathbb{B}^\times$; the eigenvalue map to $\mathbb{C}^\times\times\mathbb{C}^\times$ is surjective, not injective and not a group homomorphism |

The eigenvalue decomposition exists in two-term form on the distinct and zero-divisor rows, in one-term form on the scalar row, and not at all on the Jordan and nilpotent rows; the table is in §*Degenerate Regimes*.

The Peirce decomposition relative to $\tilde\Pi_+$ has corners $\mathbb{B}_{\sigma\tau}=\tilde\Pi_\sigma\mathbb{B}\tilde\Pi_\tau$. Its diagonal part is the centraliser $\mathbb{C}[\tilde Q]=\operatorname{span}_{\mathbb{C}}\{e_t,\tilde Q\}$, and $\tilde Q$ has the diagonal coordinates $\lambda_\pm$ and zero mixed coordinates. The mixed corners are the directions that fail to commute with $\tilde Q$. The polynomial calculus, the inverse and the parity-matched lattice all follow from the decomposition. The eigenvalue map on the unit group is surjective but not injective, and it is not a group homomorphism. The idempotents are Hermitian exactly when $\vec U$ is real, and the decomposition is then the spectral theorem.

### Comparison with the Neighbouring Cases

The table compares the decomposition across the three algebras; in the biquaternion column, the distinct case is $Q_x^2+Q_y^2+Q_z^2\neq0$, $\vec\Xi=-i\vec Q/\sqrt{Q_x^2+Q_y^2+Q_z^2}$, and $\vec\Upsilon_\pm$ are the two nilpotents of the Q-adapted basis, one in each mixed corner.

| Feature | Split-complex | Reduced biquaternion | Biquaternion |
|---|---|---|---|
| Algebra | $\mathbb{R}[x]/(x^2-1)\cong\mathbb{R}\times\mathbb{R}$ | $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$ | $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, simple |
| Element | $Q=q+jq'$ | $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | $\tilde Q=Q_te_t+\vec Q$ |
| Eigenvalues | $\lambda_\pm=q\pm q'$ | $\lambda_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown}$ | $\lambda_\pm=Q_t\pm i\sqrt{Q_x^2+Q_y^2+Q_z^2}$ |
| Distinctness | $q'\neq0$ | $Q_{\blacktriangledown}\neq0$ | $Q_x^2+Q_y^2+Q_z^2\neq0$ |
| Eigenprojections | $\Pi_\pm=\tfrac12(1\pm j)$ | $\Pi_\pm=\tfrac12(1\pm j)$ | $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$ |
| Eigenprojections depend on the element? | no | no | yes |
| Eigenprojections central? | yes | yes | no |
| Peirce decomposition | $\mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_-$ | $\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$ | $\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\tilde\Pi_-$ plus two mixed square-zero lines |
| Eigenbasis | $(\Pi_+,\Pi_-)$; eigenvalues $\lambda_+,\lambda_-$ | $(\Pi_+,\Pi_-)$; eigenvalues $\lambda_+,\lambda_-$ | $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$; eigenvalues $\lambda_+,\lambda_+,\lambda_-,\lambda_-$ |
| General element in the eigenbasis | coordinates $(a_1,a_2)$ | coordinates $(A_1,A_2)$ | coordinates $(Q_{\mathrm{sp},11},Q_{\mathrm{sp},12},Q_{\mathrm{sp},21},Q_{\mathrm{sp},22})$ |
| Nilpotents in the eigenbasis | none | none | $\vec\Upsilon_\pm$ |
| Spinor spaces | $S_\pm=\mathbb{R}\Pi_\pm$, real lines | $S_\pm=\mathbb{C}\Pi_\pm$, complex lines | $S_\pm=\mathbb{B}\tilde\Pi_\pm\cong\mathbb{C}^2$, complex planes |
| Spinor coordinates | one real coefficient per chirality | one complex coefficient per chirality | two complex coefficients per chirality |
| Action of $Q$ on a spinor | scalar: $\lambda_+$ on $S_+$, $\lambda_-$ on $S_-$ | scalar: $\lambda_+$ on $S_+$, $\lambda_-$ on $S_-$ | $\lambda_+$ on the first coordinate, $\lambda_-$ on the second |
| Unit group | $\cong\mathbb{R}^\times\times\mathbb{R}^\times$ | $\cong\mathbb{C}^\times\times\mathbb{C}^\times$ | $\mathbb{B}^\times$; eigenvalue map surjective, not injective, not a homomorphism |

Read down a column for one algebra and across a row for one concept. The rows down to the eigenprojections follow one pattern; the rows below them record where the algebras part: whether the idempotents depend on the element and whether they are central, the two mixed square-zero lines of the biquaternion Peirce decomposition, and the biquaternion unit group, which is no longer a product. The last rows record the spinor content: one real coefficient per chirality for the split-complex algebra, one complex coefficient per chirality for the reduced biquaternion algebra, and two complex coefficients per chirality, forming a complex plane, for the biquaternion algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, dimension $4$ over $\mathbb{C}$ |
| $\tilde Q=Q_te_t+\vec Q$ | General biquaternion, $Q_\mu\in\mathbb{C}$ |
| $\tilde Q^{\natural}$, $\tilde Q^{*}$ | Quaternion conjugation and Hermitian conjugation |
| $\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ | Reduced norm, and the product of the two eigenvalues |
| $\operatorname{tr}(\tilde Q)=2Q_t=\lambda_++\lambda_-$ | Reduced trace |
| $\vec U=\vec Q/\sqrt{Q_x^2+Q_y^2+Q_z^2}$ | Pure unit element, $\vec U^2=-e_t$, for $Q_x^2+Q_y^2+Q_z^2\neq0$ |
| $\vec\Xi=-i\vec U=-\dfrac{i\vec Q}{\sqrt{Q_x^2+Q_y^2+Q_z^2}}$ | Pure root of $+1$, $\vec\Xi^2=e_t$ |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$ | Eigenprojections, primitive orthogonal idempotents |
| $\tilde\Pi_1,\tilde\Pi_2$ | A complete orthogonal pair, used in the scalar regime |
| $\lambda_\pm=Q_t\pm i\sqrt{Q_x^2+Q_y^2+Q_z^2}$ | Eigenvalues, the two roots of $p_{\tilde Q}$ |
| $\sigma(\tilde Q)=\{\lambda_+,\lambda_-\}=\left\{Q_t+i\sqrt{Q_x^2+Q_y^2+Q_z^2},Q_t-i\sqrt{Q_x^2+Q_y^2+Q_z^2}\right\}$ | Spectrum |
| $p_{\tilde Q}(X)=X^2-2Q_tX+\langle\tilde Q\rangle_{\natural}=(X-\lambda_+)(X-\lambda_-)$ | Characteristic polynomial |
| $\vec\Upsilon_\pm$ | Nilpotents of the Q-adapted basis, fixed up to the reciprocal rescaling, $\vec\Upsilon_+\in\mathbb{B}_{-+}$, $\vec\Upsilon_-\in\mathbb{B}_{+-}$, with $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$ and $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$ |
| $\vec w$ | $\vec e_x+\vec e_y+\vec e_z$, the permutation-invariant vector |
| $\Sigma$ | $Q_x+Q_y+Q_z=\vec w\cdot\vec Q$ |
| $L_{\tilde Q},R_{\tilde Q}$ | Left and right multiplication operators, $\tilde Q_{\mathrm{sp}}\mapsto\tilde Q\tilde Q_{\mathrm{sp}}$ and $\tilde Q_{\mathrm{sp}}\mapsto\tilde Q_{\mathrm{sp}}\tilde Q$ |
| $\mathcal{B}$ | The Q-adapted eigenbasis $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ |
| $L_{\tilde Q_{\mathrm{sp}}},R_{\tilde Q_{\mathrm{sp}}}$ | Left and right multiplication by $\tilde Q_{\mathrm{sp}}$, $L_{\tilde Q_{\mathrm{sp}}}(X)=\tilde Q_{\mathrm{sp}}X$ and $R_{\tilde Q_{\mathrm{sp}}}(X)=X\tilde Q_{\mathrm{sp}}$ |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | The two spinor spaces: minimal left ideals, complex planes |
| $\tilde Q_{\mathrm{sp}}=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},21}\vec\Upsilon_++Q_{\mathrm{sp},22}\tilde\Pi_-$ | The general element in the Q-adapted basis, the one whose coordinates are the spinor coordinates |
| $\tilde Q_3$ | General elements, used for products, inverses and coordinate changes |
| $\tilde Q_4=\mu_+\tilde\Pi_++\mu_-\tilde\Pi_-$ | A general element of the diagonal part in §*The Algebraic Fibre of the Decomposition* |
| $Q_{\mathrm{sp},11},Q_{\mathrm{sp},21}$ | Spinor coordinates on $S_+$ in the eigenbasis $(\tilde\Pi_+,\vec\Upsilon_+)$, the first column of the matrix |
| $Q_{\mathrm{sp},12},Q_{\mathrm{sp},22}$ | Spinor coordinates on $S_-$ in the eigenbasis $(\vec\Upsilon_-,\tilde\Pi_-)$, the second column of the matrix |
| $M_2^Q(P)$ | The Peirce matrix of $P$ in the assignment $\tilde\Pi_+\mapsto E_{11}$, $\vec\Upsilon_-\mapsto E_{12}$, $\vec\Upsilon_+\mapsto E_{21}$, $\tilde\Pi_-\mapsto E_{22}$ |
| $E_{ij}$ | Matrix units of the $2\times2$ model |
| $a_{ij}$ | Coefficients of $P$ in the Q-adapted basis, the entries of $M_2^Q(P)$ |
| $\mathbb{B}_{\sigma\tau}=\tilde\Pi_\sigma\mathbb{B}\tilde\Pi_\tau$ | Peirce corners of the pair |
| $\mathbb{C}[\tilde Q]=\operatorname{span}_{\mathbb{C}}\{e_t,\tilde Q\}$ | Commutative subalgebra; the centraliser of $\tilde Q$ when $Q_x^2+Q_y^2+Q_z^2\neq0$ |
| $\mathbb{B}^{\times}$ | Group of units, the invertible elements |
| $\mathbb{B}^{\times}\to\mathbb{C}^{\times}\times\mathbb{C}^{\times}$, $\tilde Q\mapsto(\lambda_+,\lambda_-)$ | Eigenvalue map on the unit group, surjective but not injective, and not a group homomorphism |
| $L=\{\pi i m\,e_t+\pi n\,\vec U:\ m,n\in\mathbb{Z},\ m\equiv n\pmod2\}$ | Lattice of basis-coordinate data for eigenvalues $\mu_\pm\in2\pi i\mathbb{Z}$; the kernel of $\exp$ on the diagonal part when $Q_x^2+Q_y^2+Q_z^2\neq0$ |
| $\vec\Upsilon=\vec Q$ | Pure nilpotent, in the regime $Q_x^2+Q_y^2+Q_z^2=0$ and $\vec Q\neq0$ |
| $\mu$ | A test scalar in the definition of an eigenvalue |
| $\mu_\pm$ | Eigenvalue coordinates on the diagonal part |
| $a=(\mu_++\mu_-)/2$, $\Theta=(\mu_+-\mu_-)/(2i)$ | Scalar and angle coordinates on the diagonal part |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the Peirce decomposition and the structure theory of finite-dimensional algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the algebraic structure of the biquaternion algebra.
- The corpus articles: [The Eigenvalue Decomposition of an Element](the-eigenvalue-decomposition-of-an-element.html), [The Lagrange–Sylvester Eigenprojector Formula](the-lagrange-sylvester-eigenprojector-formula.html), [The Centraliser and the Diagonal Peirce Part](the-centraliser-and-the-diagonal-peirce-part.html), [Off-Diagonal Peirce Components and Noncentral Idempotents](off-diagonal-peirce-components-and-noncentral-idempotents.html), [Biquaternion Spectral Theory](biquaternion-spectral-theory.html), [Ideals and Peirce Decompositions of the Biquaternion Algebra](ideals-and-peirce-decompositions-of-the-biquaternion-algebra.html), [Square Roots of One and the Idempotents of the Biquaternion Algebra](square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), [The Biquaternion Algebra and Its Vector Spaces](the-biquaternion-algebra-and-its-vector-spaces.html), [Nilpotent Elements and the Jordan–Chevalley Decomposition](nilpotent-elements-and-the-jordan-chevalley-decomposition.html), [Quaternion Spectral Theory](quaternion-spectral-theory.html), [Reduced Biquaternion Spectral Theory](reduced-biquaternion-spectral-theory.html), [The Biquaternion Eigenvalue Decomposition](the-biquaternion-eigenvalue-decomposition.html), [Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number](eigenvalue-decomposition-and-eigenbasis-of-a-split-complex-number.html), [Eigenvalue Decomposition and Eigenbasis of a Reduced Biquaternion](eigenvalue-decomposition-and-eigenbasis-of-a-reduced-biquaternion.html) and [Conventions in Mathematics](conventions-in-mathematics.html). The operator readings of the Q-adapted basis are in [One-Sided Operators on the Biquaternion Algebra](one-sided-operators-on-the-biquaternion-algebra.html), for the left and right multiplications, and [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the sandwich; the commutative companions are [Operator and the Polar Decomposition of a Split-Complex Number](operator-and-the-polar-decomposition-of-a-split-complex-number.html) and [Operator and the Polar Decomposition of a Reduced Biquaternion](operator-and-the-polar-decomposition-of-a-reduced-biquaternion.html).
