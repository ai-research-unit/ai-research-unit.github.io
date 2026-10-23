# __Eigenbasis of a Biquaternion__

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

Here the coefficients $\lambda_\pm$ are the eigenvalues and the idempotents $\tilde\Pi_\pm$ are the eigenprojections. The eigenvalues are distinct in this regime. The article is the noncommutative counterpart of *Eigenbasis of a Split-Complex Number* and *Eigenbasis of a Reduced Biquaternion*. The general definition and the existence theorem are those of *The Eigenvalue Decomposition of an Element*; the biquaternion content is that, in the regime of distinct eigenvalues, the pair is the pair of idempotents of a pure root of $+1$, and the decomposition is the Peirce decomposition attached to that root in *Ideals and Peirce Decomposition of the Biquaternion Algebra*.

**The results.** The spectrum of $\tilde Q=Q_te_t+\vec Q$ is $\{Q_t+i\sqrt{Q_x^2+Q_y^2+Q_z^2},Q_t-i\sqrt{Q_x^2+Q_y^2+Q_z^2}\}$, and in the distinct case $Q_x^2+Q_y^2+Q_z^2\neq0$ the eigenprojections are the two idempotents of the pure root $\vec\Xi=-i\vec Q/\sqrt{Q_x^2+Q_y^2+Q_z^2}$. They are noncentral and vary with $\tilde Q$, the eigenvalue decomposition is the Peirce decomposition relative to that root read on the element, and the diagonal part is the commutative plane $\mathbb{C}[\tilde Q]$. The polynomial calculus is the calculus on $\mathbb{C}[\tilde Q]$, the unit group is the invertible group with a surjective but non-injective eigenvalue map, and the nilpotent regime is the one case with no eigenvalue decomposition. The article also constructs the Q-adapted Peirce basis, the two nilpotents of the mixed corners, and the eigenbasis of left multiplication; it separates the eigenspaces of left multiplication, which are the two right ideals, from the left ideals, which are the spinor spaces. The two minimal left ideals $S_\pm=\mathbb{B}\tilde\Pi_\pm$ are the spinor spaces; each is a complex plane and a spinor is a pair of complex coordinates.

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
| Spinor spaces | $S_\pm=\mathbb{B}\tilde\Pi_\pm\cong\mathbb{C}^2$; two complex spinor coordinates per chirality |
| Unit group | $\mathbb{B}^\times$; the eigenvalue map is surjective, not injective, not a homomorphism |

**Conventions.** The notation is fixed in *Conventions in Mathematics*: the base is $e_t,\vec e_x,\vec e_y,\vec e_z$, a general element is $\tilde Q=Q_te_t+\vec Q$ with $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ and complex coefficients, an idempotent is $\tilde\Pi$, a root of $+1$ is $\tilde\Xi$ and a pure root is $\vec\Xi$, and a pure nilpotent is $\vec\Upsilon$. Put $B=\sqrt{Q_x^2+Q_y^2+Q_z^2}$. In the distinct case the Q-adapted basis is $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$, the general element in it is $\tilde Q_{\mathrm{sp}}=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},21}\vec\Upsilon_++Q_{\mathrm{sp},22}\tilde\Pi_-$, and the two spinor spaces are $S_\pm=\mathbb{B}\tilde\Pi_\pm$, with coordinates $(Q_{\mathrm{sp},11},Q_{\mathrm{sp},21})$ on $S_+$ and $(Q_{\mathrm{sp},12},Q_{\mathrm{sp},22})$ on $S_-$. The characteristic polynomial, the spectrum and the eigenvalues $\lambda_\pm=Q_t\pm iB$ are those of *Biquaternion Spectral Theory*, §*The Biquaternion Spectrum*; the root of $+1$, the halving map and the primitive idempotents are those of *Square Roots of One and the Idempotents of the Biquaternion Algebra*, §*The Idempotents*; the four Peirce corners are those of *Ideals and Peirce Decomposition of the Biquaternion Algebra*, §*The Peirce Decomposition*; the centraliser and the diagonal part are those of *The Centraliser and the Diagonal Peirce Part*; the off-diagonal components are those of *Off-Diagonal Peirce Components and Noncentral Idempotents*; the reduced norm and the invertibility criterion are those of *Introduction to the Biquaternion Algebra*, §*The Reduced Norm and Invertibility*; the eigenvalue formula and the parity-matched lattice are developed in §*The Algebraic Fibre of the Decomposition* and used in *Biquaternion Elementary Functions*, §*The Eigenvalue Formula*.

**Boundaries.** The split-complex and reduced biquaternion cases are those of *Eigenbasis of a Split-Complex Number* and *Eigenbasis of a Reduced Biquaternion*; the quaternion case, with its left and right eigenvalues, is the subject of *Quaternion Spectral Theory*; the exponential and the logarithm built on the decomposition are those of *Biquaternion Elementary Functions*; and the spectral theorem in its general form is that of *Biquaternion Spectral Theory*. The Q-adapted construction, the nilpotents and the spinor spaces are developed here; the standard Peirce decomposition is that of *Ideals and Peirce Decomposition of the Biquaternion Algebra*. The article cites these and does not restate them. The other products of the biquaternion space carry nilpotents and idempotents relative to the product, and are outside its scope.

## The Spectrum and the Characteristic Polynomial

**Definition.** Let $\tilde Q\in\mathbb{B}$. A complex scalar $\mu$ is an **eigenvalue** of $\tilde Q$ if $\tilde Q-\mu e_t$ is not a unit in $\mathbb{B}$; the set of eigenvalues is the **spectrum** $\sigma(\tilde Q)$. This is the definition of *The Eigenvalue Decomposition of an Element*, §*The Eigenvalues of an Element*.

**Notation.** The two eigenvalues are written $\lambda_\pm=Q_t\pm i\sqrt{Q_x^2+Q_y^2+Q_z^2}$ when their values are exhibited, the radical being one of the two square roots. The test scalar of the definition is $\mu$, so the letter $\lambda$ is reserved for the two eigenvalues. The pair is the analogue of $\lambda_\pm=q\pm q'$ of *Eigenbasis of a Split-Complex Number* and of $\lambda_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown}$ of *Eigenbasis of a Reduced Biquaternion*.

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
so by *Introduction to the Biquaternion Algebra*, §*The Reduced Norm and Invertibility*, $\tilde Q-\mu e_t$ is not a unit exactly when $(Q_t-\mu)^2=-(Q_x^2+Q_y^2+Q_z^2)$, that is exactly when $\mu=\lambda_\pm$.

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
the two idempotents of the root $\vec\Xi$ under the halving map of *Square Roots of One and the Idempotents of the Biquaternion Algebra*, §*The Idempotents*. By that article the pair is complete and orthogonal, $\tilde\Pi_++\tilde\Pi_-=e_t$ and $\tilde\Pi_+\tilde\Pi_-=0$, and the root is their difference, $\vec\Xi=\tilde\Pi_+-\tilde\Pi_-$; by *Ideals and Peirce Decomposition of the Biquaternion Algebra*, §*Idempotents and Orthogonal Idempotents*, each member is primitive.

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

**Dependence on the element.** The eigenprojections $\tilde\Pi_\pm$ vary with $\tilde Q$: they are the two idempotents of the pure root $\vec\Xi=-i\vec Q/\sqrt{Q_x^2+Q_y^2+Q_z^2}$, and the root is recovered from them as $\vec\Xi=\tilde\Pi_+-\tilde\Pi_-$. This is the structural difference from the split-complex and reduced biquaternion cases, where the eigenprojections are the fixed central idempotents $\Pi_\pm$ (*Eigenbasis of a Split-Complex Number*, §*The Eigenprojections*; *Eigenbasis of a Reduced Biquaternion*, §*The Eigenprojections*). Here the dependence on the element lies in both the eigenvalues and the idempotents.

The pair is collected in the table.

| Idempotent | Definition | Eigenvalue | Properties |
|---|---|---|---|
| $\tilde\Pi_+$ | $\tfrac12(e_t+\vec\Xi)$ | $\lambda_+=Q_t+i\sqrt{Q_x^2+Q_y^2+Q_z^2}$ | $\tilde\Pi_+^2=\tilde\Pi_+$, noncentral, primitive |
| $\tilde\Pi_-$ | $\tfrac12(e_t-\vec\Xi)$ | $\lambda_-=Q_t-i\sqrt{Q_x^2+Q_y^2+Q_z^2}$ | $\tilde\Pi_-^2=\tilde\Pi_-$, noncentral, primitive |

The two idempotents are complementary and orthogonal, $\tilde\Pi_++\tilde\Pi_-=e_t$ and $\tilde\Pi_+\tilde\Pi_-=0$. The Q-adapted basis that completes this pair, the construction of the nilpotents $\vec\Upsilon_\pm$ from the two mixed corners, and the eigenbasis of $L_{\tilde Q}$ are given in §*The Q-Adapted Peirce Basis, the Nilpotents, and the Eigenbasis*.

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
be the Peirce corners of the pair, in the notation of *Ideals and Peirce Decomposition of the Biquaternion Algebra*, §*The Biquaternion Case*. The Peirce decomposition is
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

The two signs of the pair are the two eigenvalues of multiplication by the root: an element of $\mathbb{B}_{\sigma\tau}$ is multiplied by $\sigma$ on the left and by $\tau$ on the right by $\vec\Xi$ (§*The Biquaternion Case*). The diagonal corners are the components on which the two signs agree; $\tilde Q$ acts on them by $\lambda_+$ and $\lambda_-$ respectively. The construction of the mixed generators $\vec\Upsilon_\pm$ and the eigenbasis of left multiplication are the subject of the next section.

## The Q-Adapted Peirce Basis, the Nilpotents, and the Eigenbasis

**Fix $\tilde Q$ with $Q_x^2+Q_y^2+Q_z^2\neq0$. Its own root carries a Peirce pair, the two mixed corners carry a pair of nilpotents, and the four elements form a basis in which left multiplication by $\tilde Q$ is diagonal. The basis is an eigenbasis of left multiplication; the two minimal left ideals are the eigenspaces of right multiplication, not of left multiplication.**

### The Root, the Idempotents, and the Eigenvalues

Let
$$
\tilde Q=Q_te_t+\vec Q,\qquad
\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,\qquad
Q_x^2+Q_y^2+Q_z^2\neq0,
$$
and fix a square root of $Q_x^2+Q_y^2+Q_z^2$. Define
$$
\vec U=\frac{\vec Q}{\sqrt{Q_x^2+Q_y^2+Q_z^2}},\qquad
\vec\Xi=-i\vec U=-\frac{i\vec Q}{\sqrt{Q_x^2+Q_y^2+Q_z^2}},\qquad
\tilde\Pi_\pm=\frac{e_t\pm\vec\Xi}{2},\qquad
\lambda_\pm=Q_t\pm i\sqrt{Q_x^2+Q_y^2+Q_z^2}.
$$
Then
$$
\vec\Xi^2=e_t,\qquad
\tilde\Pi_\pm^2=\tilde\Pi_\pm,\qquad
\tilde\Pi_+\tilde\Pi_-=\tilde\Pi_-\tilde\Pi_+=0,\qquad
\tilde\Pi_++\tilde\Pi_-=e_t,
$$
and
$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-.
$$
The pair $(\tilde\Pi_+,\tilde\Pi_-)$ is attached to $\tilde Q$: it is the pair of the root $\vec\Xi$, not an arbitrary pair of idempotents. The signs are fixed by
$$
\vec\Xi\tilde\Pi_\pm=\tilde\Pi_\pm\vec\Xi=\pm\tilde\Pi_\pm,\qquad
\tilde Q\tilde\Pi_\pm=\lambda_\pm\tilde\Pi_\pm.
$$
Choosing the negative square root sends $\vec\Xi$ to $-\vec\Xi$, exchanges $\tilde\Pi_+$ and $\tilde\Pi_-$, and exchanges $\lambda_+$ and $\lambda_-$; the unordered pair and the unordered spectrum are unchanged.

### The Peirce Corners and the Nilpotents

Define the four **Peirce corners**
$$
\mathbb{B}_{st}=\tilde\Pi_s\mathbb{B}\tilde\Pi_t,\qquad s,t\in\{+,-\}.
$$
Each is one complex line. The two diagonal corners are the lines of the idempotents, and the two mixed corners are square-zero: an element $x\in\mathbb{B}_{st}$ with $s\neq t$ has zero scalar part, because its trace is zero, and its square is zero, because
$$
x^2\in\tilde\Pi_s\mathbb{B}\tilde\Pi_t\tilde\Pi_s\mathbb{B}\tilde\Pi_t=0
\qquad(s\neq t).
$$

**Construction of the two nilpotents.** Choose a nonzero
$$
\vec\Upsilon_+\in\mathbb{B}_{-+}=\tilde\Pi_-\mathbb{B}\tilde\Pi_+.
$$
Consider the map
$$
\mathbb{B}_{+-}\longrightarrow\mathbb{C}\tilde\Pi_-,\qquad x\longmapsto\vec\Upsilon_+x.
$$
It is linear between complex lines, and it is nonzero. Otherwise $\vec\Upsilon_+x=0$ for every $x\in\mathbb{B}_{+-}$, hence $\vec\Upsilon_+\tilde\Pi_-\mathbb{B}\tilde\Pi_-=0$, and then $\mathbb{B}\vec\Upsilon_+\mathbb{B}\tilde\Pi_-=0$. But $\vec\Upsilon_+\neq0$, so the two-sided ideal $\mathbb{B}\vec\Upsilon_+\mathbb{B}$ is the whole simple algebra $\mathbb{B}$, and $\mathbb{B}\tilde\Pi_-\neq0$, a contradiction. A nonzero linear map between complex lines is an isomorphism. Hence there is a unique
$$
\vec\Upsilon_-\in\mathbb{B}_{+-}
\qquad\text{with}\qquad
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-.
$$
The other product is then forced. It lies in $\mathbb{C}\tilde\Pi_+$, say $\vec\Upsilon_-\vec\Upsilon_+=\alpha\tilde\Pi_+$, and
$$
\vec\Upsilon_+=\tilde\Pi_-\vec\Upsilon_+=\vec\Upsilon_+(\vec\Upsilon_-\vec\Upsilon_+)=\alpha\vec\Upsilon_+\tilde\Pi_+=\alpha\vec\Upsilon_+,
$$
so $\alpha=1$. Therefore
$$
\boxed{\ \vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,\qquad
\vec\Upsilon_+^2=\vec\Upsilon_-^2=0.\ }
$$
The construction makes one choice, the nonzero element $\vec\Upsilon_+$ of the line $\mathbb{B}_{-+}$. That choice determines $\vec\Upsilon_-$ uniquely. No intermediate scalar and no square root enter. A square root appears only when the generator is parametrised by a transverse vector, as in the closed forms below.

The corners and their generators are collected in the table.

| Corner | Definition | Generator |
|---|---|---|
| $\mathbb{B}_{++}$ | $\tilde\Pi_+\mathbb{B}\tilde\Pi_+$ | $\tilde\Pi_+$ |
| $\mathbb{B}_{+-}$ | $\tilde\Pi_+\mathbb{B}\tilde\Pi_-$ | $\vec\Upsilon_-$ |
| $\mathbb{B}_{-+}$ | $\tilde\Pi_-\mathbb{B}\tilde\Pi_+$ | $\vec\Upsilon_+$ |
| $\mathbb{B}_{--}$ | $\tilde\Pi_-\mathbb{B}\tilde\Pi_-$ | $\tilde\Pi_-$ |

**The two signs.** The index is fixed by the left ideal, not by the corner: $\vec\Upsilon_+$ lies in $\mathbb{B}_{-+}$ and, together with $\tilde\Pi_+$, generates $S_+=\mathbb{B}\tilde\Pi_+$; $\vec\Upsilon_-$ lies in $\mathbb{B}_{+-}$ and, together with $\tilde\Pi_-$, generates $S_-=\mathbb{B}\tilde\Pi_-$. Thus
$$
S_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+,\qquad
S_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi_-.
$$

**Uniqueness up to rescaling.** The pair is determined by the products and squares only up to
$$
\vec\Upsilon_+\longmapsto\mu\,\vec\Upsilon_+,\qquad
\vec\Upsilon_-\longmapsto\mu^{-1}\vec\Upsilon_-,\qquad
\mu\in\mathbb{C}^{\times},
$$
which preserves both products and both squares. Indeed, $\mu^{-1}\vec\Upsilon_-$ is the unique element of $\mathbb{B}_{+-}$ whose product with $\mu\vec\Upsilon_+$ is $\tilde\Pi_-$, so the construction forces $\vec\Upsilon_-'=\mu^{-1}\vec\Upsilon_-$. Conversely every pair with the same products and squares arises this way, because the mixed corners are lines. The construction therefore defines the pair up to this one rescaling, and no further choice enters.

**The corner, without a preferred axis.** For every pure biquaternion $\vec X$,
$$
\tilde\Pi_-\vec X\tilde\Pi_+=\frac12\left(\vec X_\perp+i\,\vec U\times\vec X\right)
=\frac12\left(\vec X-\frac{\vec X\cdot\vec Q}{B^2}\vec Q\right)+\frac{i}{4B}\,[\vec Q,\vec X],
$$
$$
\tilde\Pi_+\vec X\tilde\Pi_-=\frac12\left(\vec X_\perp-i\,\vec U\times\vec X\right)
=\frac12\left(\vec X-\frac{\vec X\cdot\vec Q}{B^2}\vec Q\right)-\frac{i}{4B}\,[\vec Q,\vec X],
$$
where $\vec X_\perp=\vec X-\dfrac{\vec X\cdot\vec Q}{B^2}\vec Q$. No axis is singled out. When $\vec X_\perp^2\neq0$ both projections are nonzero.

**The two nilpotents from a transverse vector.** Let $\vec X$ be a pure vector with $\vec X_\perp^2\neq0$, and put
$$
u_+=\tilde\Pi_-\vec X\tilde\Pi_+,\qquad u_-=\tilde\Pi_+\vec X\tilde\Pi_-.
$$
Then
$$
u_+u_-=\vec X_\perp^2\,\tilde\Pi_-,\qquad
u_-u_+=\vec X_\perp^2\,\tilde\Pi_+,\qquad
u_\pm^2=0,
$$
as the expansion of the two projections shows: the cross terms cancel because $\vec X_\perp\cdot(\vec U\times\vec X_\perp)=0$. Then
$$
\vec\Upsilon_\pm=\frac{u_\pm}{\sqrt{\vec X_\perp^2}}
$$
satisfy $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$, $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$, $\vec\Upsilon_\pm^2=0$. Every admissible pair arises this way, and two choices of $\vec X$ give pairs differing by the reciprocal rescaling. The scalar is
$$
\vec X_\perp^2=\vec X^2+\frac{(\vec X\cdot\vec Q)^2}{B^2}.
$$

**The symmetric closed form.** The vector $\vec w=\vec e_x+\vec e_y+\vec e_z$ is the only nonzero vector fixed by every permutation of the axes. Put $\sigma=\vec w\cdot\vec Q=Q_x+Q_y+Q_z$. Then
$$
\vec w_\perp=\vec w-\frac{\Sigma}{B^2}\vec Q,\qquad
\vec w_\perp^2=\vec w^2+\frac{\Sigma^2}{B^2}=-3+\frac{\Sigma^2}{B^2}=\frac{\Sigma^2-3B^2}{B^2}.
$$
Therefore
$$
\boxed{\ \vec\Upsilon_\pm=\frac{B\,\vec w-\dfrac{\Sigma}{B}\,\vec Q\pm\dfrac{i}{2}\,[\vec Q,\vec w]}{2\sqrt{\Sigma^2-3B^2}}\ }
$$
with $\vec w=\vec e_x+\vec e_y+\vec e_z$ and $\Sigma=Q_x+Q_y+Q_z$. In full coordinates,
$$
\vec\Upsilon_\pm=\frac{\Bigl(B-\dfrac{\Sigma Q_x}{B}\pm i(Q_y-Q_z)\Bigr)\vec e_x+\Bigl(B-\dfrac{\Sigma Q_y}{B}\pm i(Q_z-Q_x)\Bigr)\vec e_y+\Bigl(B-\dfrac{\Sigma Q_z}{B}\pm i(Q_x-Q_y)\Bigr)\vec e_z}{2\sqrt{\Sigma^2-3B^2}}.
$$
A permutation of the axes permutes the three components and leaves $B$ and $\Sigma$ unchanged, so the formula is symmetric in $x,y,z$. Expanding the brackets gives
$$
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,\qquad
\vec\Upsilon_\pm^2=0,
$$
and the denominator is
$$
2\sqrt{\Sigma^2-3B^2}=2\sqrt{-\bigl((Q_x-Q_y)^2+(Q_y-Q_z)^2+(Q_z-Q_x)^2\bigr)}.
$$

**The exceptional cone and the chart.** The symmetric formula degenerates exactly on the cone
$$
\Sigma^2=3B^2,
\qquad\text{that is,}\qquad
(Q_x-Q_y)^2+(Q_y-Q_z)^2+(Q_z-Q_x)^2=0,
$$
which for real $\vec Q$ is the line $Q_x=Q_y=Q_z$. On that cone use the axis chart: for $\mu\in\{x,y,z\}$,
$$
\vec\Upsilon_\pm=\frac{B\,\vec e_\mu-\dfrac{Q_\mu}{B}\,\vec Q\pm\dfrac{i}{2}\,[\vec Q,\vec e_\mu]}{2\sqrt{Q_\mu^2-B^2}},
$$
which is the transverse-vector construction with $\vec X=\vec e_\mu$. The chart with axis $\mu$ is defined when $Q_\mu^2\neq B^2$, that is, when $Q_\nu^2+Q_\rho^2\neq0$ for the two other coordinates. At least one of the three is defined whenever $B\neq0$: if all three failed, then $Q_x^2+Q_y^2=Q_y^2+Q_z^2=Q_z^2+Q_x^2=0$, hence $Q_x^2=Q_y^2=Q_z^2$ and $2Q_x^2=0$, so $B=0$. The charts are the one formula read with $\mu=x,y,z$, and the ones that are defined give pairs differing by the reciprocal rescaling. The symmetric formula off the cone and the axis charts on it cover every $\vec Q$ with $B\neq0$.

**Why no formula is axis-free everywhere.** A closed form with no auxiliary vector would be a map $F$ with $F(R\vec Q)=R\,F(\vec Q)$ for every rotation $R$, rational in $\vec Q$ and $B$. By invariant theory the only such maps are $F(\vec Q)=f(B^2)\vec Q$: the invariant tensors are $\delta_{ij}$ and $\epsilon_{ijk}$, and $\epsilon$ cannot build a vector from a single vector. But the corner is transverse to $\vec Q$, so $F$ would vanish. Every explicit generator therefore uses an auxiliary vector: the symmetric formula uses the permutation-invariant $\vec w$, the axis charts use $\vec e_x,\vec e_y,\vec e_z$. The corner line is a spinor line, and a spinor is not a function of $\vec Q$ alone.

**The standard pair.** For the opposite root, $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$, the corner generators of *Ideals and Peirce Decomposition of the Biquaternion Algebra*, §*The Biquaternion Case*, are
$$
\vec\Upsilon_x=\frac{i\vec e_x-\vec e_y}{2}\in\mathbb{B}_{+-},\qquad
\vec\Upsilon_y=\frac{i\vec e_x+\vec e_y}{2}\in\mathbb{B}_{-+},
$$
with $\vec\Upsilon_x\vec\Upsilon_y=\tilde\Pi_+$ and $\vec\Upsilon_y\vec\Upsilon_x=\tilde\Pi_-$. The present root is $\vec\Xi=-i\vec e_z$ when $Q_z>0$ with the choice $B=Q_z$, which is the negative of that one; the two corner labels and the two idempotent labels are therefore exchanged. In the present indexing
$$
\vec\Upsilon_+=\vec\Upsilon_x,\qquad \vec\Upsilon_-=\vec\Upsilon_y,
$$
and the products are $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$, $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$, as required.

### The Q-Adapted Peirce Basis

The four elements
$$
\tilde\Pi_+,\qquad \vec\Upsilon_-,\qquad \vec\Upsilon_+,\qquad \tilde\Pi_-
$$
form a $\mathbb{C}$-basis of $\mathbb{B}$. It is the **Q-adapted Peirce basis**. In this basis the multiplication by $\tilde Q$ is diagonal:
$$
\tilde Q\tilde\Pi_+=\lambda_+\tilde\Pi_+,\qquad
\tilde Q\vec\Upsilon_-=\lambda_+\vec\Upsilon_-,\qquad
\tilde Q\vec\Upsilon_+=\lambda_-\vec\Upsilon_+,\qquad
\tilde Q\tilde\Pi_-=\lambda_-\tilde\Pi_-.
$$
The diagonal values are
$$
\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-).
$$
The reason is the corner rule: an element of $\mathbb{B}_{st}$ has left sign $s$ and right sign $t$ under multiplication by the root $\vec\Xi$, and $\tilde Q=Q_te_t+i\sqrt{Q_x^2+Q_y^2+Q_z^2}\,\vec\Xi$ acts on it on the left by $Q_t+i\,s\sqrt{Q_x^2+Q_y^2+Q_z^2}=\lambda_s$ and on the right by $Q_t+i\,t\sqrt{Q_x^2+Q_y^2+Q_z^2}=\lambda_t$. The four basis elements, their corners, and the two diagonal readings are collected in the table.

| Basis element | Corner | Left eigenvalue $L_{\tilde Q}$ | Right eigenvalue $R_{\tilde Q}$ |
|---|---|---|---|
| $\tilde\Pi_+$ | $\mathbb{B}_{++}$ | $\lambda_+$ | $\lambda_+$ |
| $\vec\Upsilon_-$ | $\mathbb{B}_{+-}$ | $\lambda_+$ | $\lambda_-$ |
| $\vec\Upsilon_+$ | $\mathbb{B}_{-+}$ | $\lambda_-$ | $\lambda_+$ |
| $\tilde\Pi_-$ | $\mathbb{B}_{--}$ | $\lambda_-$ | $\lambda_-$ |

Thus the left action is diagonal with the values $\lambda_+,\lambda_+,\lambda_-,\lambda_-$, and the right action is diagonal with the values $\lambda_+,\lambda_-,\lambda_+,\lambda_-$, in the same basis.

### The Action of the Four Basis Elements

**In the eigenbasis $\mathcal{B}=(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ the multiplication of the four basis elements is the table, and the left and right actions on the basis are read from it.**

The multiplication is the table.

| $PX$ | $\tilde\Pi_+$ | $\vec\Upsilon_-$ | $\vec\Upsilon_+$ | $\tilde\Pi_-$ |
|---|---|---|---|---|
| $\tilde\Pi_+$ | $\tilde\Pi_+$ | $\vec\Upsilon_-$ | $0$ | $0$ |
| $\vec\Upsilon_-$ | $0$ | $0$ | $\tilde\Pi_+$ | $\vec\Upsilon_-$ |
| $\vec\Upsilon_+$ | $\vec\Upsilon_+$ | $\tilde\Pi_-$ | $0$ | $0$ |
| $\tilde\Pi_-$ | $0$ | $0$ | $\vec\Upsilon_+$ | $\tilde\Pi_-$ |

**The left action.** For $\tilde Q_{\mathrm{sp}}\in\mathbb{B}$ write $L_{\tilde Q_{\mathrm{sp}}}(X)=\tilde Q_{\mathrm{sp}}X$. Reading the table row by row,
$$
L_{\tilde\Pi_+}(\tilde\Pi_+)=\tilde\Pi_+,\quad
L_{\tilde\Pi_+}(\vec\Upsilon_-)=\vec\Upsilon_-,\quad
L_{\tilde\Pi_+}(\vec\Upsilon_+)=0,\quad
L_{\tilde\Pi_+}(\tilde\Pi_-)=0,
$$
$$
L_{\vec\Upsilon_-}(\tilde\Pi_+)=0,\quad
L_{\vec\Upsilon_-}(\vec\Upsilon_-)=0,\quad
L_{\vec\Upsilon_-}(\vec\Upsilon_+)=\tilde\Pi_+,\quad
L_{\vec\Upsilon_-}(\tilde\Pi_-)=\vec\Upsilon_-,
$$
$$
L_{\vec\Upsilon_+}(\tilde\Pi_+)=\vec\Upsilon_+,\quad
L_{\vec\Upsilon_+}(\vec\Upsilon_-)=\tilde\Pi_-,\quad
L_{\vec\Upsilon_+}(\vec\Upsilon_+)=0,\quad
L_{\vec\Upsilon_+}(\tilde\Pi_-)=0,
$$
$$
L_{\tilde\Pi_-}(\tilde\Pi_+)=0,\quad
L_{\tilde\Pi_-}(\vec\Upsilon_-)=0,\quad
L_{\tilde\Pi_-}(\vec\Upsilon_+)=\vec\Upsilon_+,\quad
L_{\tilde\Pi_-}(\tilde\Pi_-)=\tilde\Pi_-.
$$
The four lists are the Peirce identities read as left multiplication: $\tilde\Pi_+$ keeps the two vectors of $S_+$ and kills $S_-$, $\tilde\Pi_-$ does the reverse, and the two nilpotents exchange the two spinor spaces in the two directions. In particular
$$
L_{\tilde\Pi_+}+L_{\tilde\Pi_-}=\mathrm{id},
\qquad
L_{\vec\Upsilon_+}L_{\vec\Upsilon_-}=L_{\tilde\Pi_-},
\qquad
L_{\vec\Upsilon_-}L_{\vec\Upsilon_+}=L_{\tilde\Pi_+},
\qquad
L_{\vec\Upsilon_\pm}^2=0,
$$
which are $\tilde\Pi_++\tilde\Pi_-=e_t$, $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$, $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$ and $\vec\Upsilon_\pm^2=0$.

For $\tilde Q$ itself the left action is diagonal,
$$
L_{\tilde Q}(\tilde\Pi_+)=\lambda_+\tilde\Pi_+,\quad
L_{\tilde Q}(\vec\Upsilon_-)=\lambda_+\vec\Upsilon_-,\quad
L_{\tilde Q}(\vec\Upsilon_+)=\lambda_-\vec\Upsilon_+,\quad
L_{\tilde Q}(\tilde\Pi_-)=\lambda_-\tilde\Pi_-,
$$
with the values $\lambda_+,\lambda_+,\lambda_-,\lambda_-$ on the four basis vectors in the order $\mathcal{B}$. This is the eigenbasis property of the article: each basis vector is an eigenvector of $L_{\tilde Q}$.

**The right action.** For $R_{\tilde Q_{\mathrm{sp}}}(X)=X\tilde Q_{\mathrm{sp}}$ the same table read column by column gives
$$
R_{\tilde\Pi_+}(\tilde\Pi_+)=\tilde\Pi_+,\quad
R_{\tilde\Pi_+}(\vec\Upsilon_-)=0,\quad
R_{\tilde\Pi_+}(\vec\Upsilon_+)=\vec\Upsilon_+,\quad
R_{\tilde\Pi_+}(\tilde\Pi_-)=0,
$$
$$
R_{\vec\Upsilon_-}(\tilde\Pi_+)=\vec\Upsilon_-,\quad
R_{\vec\Upsilon_-}(\vec\Upsilon_-)=0,\quad
R_{\vec\Upsilon_-}(\vec\Upsilon_+)=\tilde\Pi_-,\quad
R_{\vec\Upsilon_-}(\tilde\Pi_-)=0,
$$
$$
R_{\vec\Upsilon_+}(\tilde\Pi_+)=0,\quad
R_{\vec\Upsilon_+}(\vec\Upsilon_-)=\tilde\Pi_+,\quad
R_{\vec\Upsilon_+}(\vec\Upsilon_+)=0,\quad
R_{\vec\Upsilon_+}(\tilde\Pi_-)=\vec\Upsilon_+,
$$
$$
R_{\tilde\Pi_-}(\tilde\Pi_+)=0,\quad
R_{\tilde\Pi_-}(\vec\Upsilon_-)=\vec\Upsilon_-,\quad
R_{\tilde\Pi_-}(\vec\Upsilon_+)=0,\quad
R_{\tilde\Pi_-}(\tilde\Pi_-)=\tilde\Pi_-,
$$
and for $\tilde Q$
$$
R_{\tilde Q}(\tilde\Pi_+)=\lambda_+\tilde\Pi_+,\quad
R_{\tilde Q}(\vec\Upsilon_-)=\lambda_-\vec\Upsilon_-,\quad
R_{\tilde Q}(\vec\Upsilon_+)=\lambda_+\vec\Upsilon_+,\quad
R_{\tilde Q}(\tilde\Pi_-)=\lambda_-\tilde\Pi_-,
$$
with the values $\lambda_+,\lambda_-,\lambda_+,\lambda_-$. The left and right actions do not coincide: $R_{\tilde Q}$ and $L_{\tilde Q}$ agree on an element exactly when the element is central, that is, on $\mathbb{C}e_t$.

**A general element.** For $\tilde Q_{\mathrm{sp}}=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},21}\vec\Upsilon_++Q_{\mathrm{sp},22}\tilde\Pi_-$ the left action on the basis is
$$
L_{\tilde Q_{\mathrm{sp}}}(\tilde\Pi_+)=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},21}\vec\Upsilon_+,\qquad
L_{\tilde Q_{\mathrm{sp}}}(\vec\Upsilon_-)=Q_{\mathrm{sp},11}\vec\Upsilon_-+Q_{\mathrm{sp},21}\tilde\Pi_-,
$$
$$
L_{\tilde Q_{\mathrm{sp}}}(\vec\Upsilon_+)=Q_{\mathrm{sp},12}\tilde\Pi_++Q_{\mathrm{sp},22}\vec\Upsilon_+,\qquad
L_{\tilde Q_{\mathrm{sp}}}(\tilde\Pi_-)=Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},22}\tilde\Pi_-,
$$
and the right action is
$$
R_{\tilde Q_{\mathrm{sp}}}(\tilde\Pi_+)=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},12}\vec\Upsilon_-,\qquad
R_{\tilde Q_{\mathrm{sp}}}(\vec\Upsilon_-)=Q_{\mathrm{sp},21}\tilde\Pi_++Q_{\mathrm{sp},22}\vec\Upsilon_-,
$$
$$
R_{\tilde Q_{\mathrm{sp}}}(\vec\Upsilon_+)=Q_{\mathrm{sp},11}\vec\Upsilon_++Q_{\mathrm{sp},12}\tilde\Pi_-,\qquad
R_{\tilde Q_{\mathrm{sp}}}(\tilde\Pi_-)=Q_{\mathrm{sp},21}\vec\Upsilon_++Q_{\mathrm{sp},22}\tilde\Pi_-.
$$
The two actions are diagonal exactly on the diagonal subalgebra $\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\tilde\Pi_-$, of which $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ is the member with the prescribed eigenvalues. This is the precise sense in which the Peirce coordinates of $\tilde Q$ are the eigenvalues: $Q_{\mathrm{sp},12}=Q_{\mathrm{sp},21}=0$ is the condition that both actions be diagonal, and $\tilde Q$ is the member with $Q_{\mathrm{sp},11}=\lambda_+$ and $Q_{\mathrm{sp},22}=\lambda_-$.

**The four elements of the fixed basis.** The coordinates of $e_t,\vec e_x,\vec e_y,\vec e_z$ in $\mathcal{B}$ are read from the expansions. In the standard case, $Q_x=Q_y=0$ with the standard root $i\vec e_z$, that is $B=-Q_z$ and $\lambda_\pm=Q_t\mp iQ_z$, the nilpotents are
$$
\vec\Upsilon_-=\frac{i\vec e_x-\vec e_y}{2},\qquad
\vec\Upsilon_+=\frac{i\vec e_x+\vec e_y}{2},
$$
and
$$
e_t=\tilde\Pi_++\tilde\Pi_-,\qquad
\vec e_x=-i(\vec\Upsilon_-+\vec\Upsilon_+),\qquad
\vec e_y=\vec\Upsilon_+-\vec\Upsilon_-,\qquad
\vec e_z=-i\tilde\Pi_++i\tilde\Pi_-.
$$
Their coordinates are
$$
e_t=(1,0,0,1),\qquad
\vec e_x=(0,-i,-i,0),\qquad
\vec e_y=(0,-1,1,0),\qquad
\vec e_z=(-i,0,0,i),
$$
and the left action of the four on the basis is read from the table. In particular $\vec e_x,\vec e_y,\vec e_z$ satisfy $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, as the fixed basis does, so the same identities hold for their left actions.

**A general pure element.** Off the axis the coordinates of $\vec e_x,\vec e_y,\vec e_z$ depend on $\vec Q$. For any pure $\vec X$,
$$
\vec X=i\,\frac{\vec X\cdot\vec Q}{B}\,(\tilde\Pi_+-\tilde\Pi_-)+X_{12}\vec\Upsilon_-+X_{21}\vec\Upsilon_+,
\qquad
X_{12}\tilde\Pi_-=\vec\Upsilon_+\vec X\tilde\Pi_-,
\qquad
X_{21}\tilde\Pi_+=\vec\Upsilon_-\vec X\tilde\Pi_+,
$$
so its coordinates in $\mathcal{B}$ are
$$
\vec X=\Bigl(i\,\frac{\vec X\cdot\vec Q}{B},\;X_{12},\;X_{21},\;-i\,\frac{\vec X\cdot\vec Q}{B}\Bigr).
$$
The standard case is $\vec Q=Q_z\vec e_z$, $B=-Q_z$.

### The Eigenbasis of Left Multiplication

**A basis of $\mathbb{B}$ is an eigenbasis of $L_{\tilde Q}$ if each of its vectors $b$ satisfies $\tilde Qb=\mu b$ for some scalar $\mu$. The Q-adapted Peirce basis is one; because each eigenspace is two-dimensional, it is not unique.**

Write
$$
L_{\tilde Q}(\tilde Q_{\mathrm{sp}})=\tilde Q\tilde Q_{\mathrm{sp}},\qquad R_{\tilde Q}(\tilde Q_{\mathrm{sp}})=\tilde Q_{\mathrm{sp}}\tilde Q.
$$
An eigenvector of $L_{\tilde Q}$ with eigenvalue $\mu$ is a nonzero element $\tilde Q_{\mathrm{sp}}$ with $\tilde Q\tilde Q_{\mathrm{sp}}=\mu\tilde Q_{\mathrm{sp}}$. The diagonal property of the Q-adapted basis reads
$$
\tilde Q\tilde\Pi_+=\lambda_+\tilde\Pi_+,\qquad
\tilde Q\vec\Upsilon_-=\lambda_+\vec\Upsilon_-,\qquad
\tilde Q\vec\Upsilon_+=\lambda_-\vec\Upsilon_+,\qquad
\tilde Q\tilde\Pi_-=\lambda_-\tilde\Pi_-,
$$
so the basis is an eigenbasis; the left action in it is diagonal with the values $\lambda_+,\lambda_+,\lambda_-,\lambda_-$.

**The two eigenspaces.** The eigenspaces are two-dimensional:
$$
\ker(L_{\tilde Q}-\lambda_+)=\tilde\Pi_+\mathbb{B}=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_-,
\qquad
\ker(L_{\tilde Q}-\lambda_-)=\tilde\Pi_-\mathbb{B}=\mathbb{C}\vec\Upsilon_+\oplus\mathbb{C}\tilde\Pi_-.
$$
These are the two minimal **right** ideals. The basis $(\tilde\Pi_+,\vec\Upsilon_-)$ is a basis of the first, $(\vec\Upsilon_+,\tilde\Pi_-)$ a basis of the second.

**Uniqueness.** An eigenbasis of $L_{\tilde Q}$ is any pair of bases of these two eigenspaces. It is therefore unique only up to an invertible change of basis on each eigenspace. The Q-adapted basis is the choice singled out by the Peirce structure: it orders each eigenspace as $(\tilde\Pi_+,\vec\Upsilon_-)$ and $(\vec\Upsilon_+,\tilde\Pi_-)$, the diagonal idempotent of the Peirce pair first.

**The left ideals are eigenspaces of right multiplication.** The two minimal left ideals
$$
S_+=\mathbb{B}\tilde\Pi_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+,
\qquad
S_-=\mathbb{B}\tilde\Pi_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi_-
$$
are not eigenspaces of $L_{\tilde Q}$: each contains one eigenvector for $\lambda_+$ and one for $\lambda_-$. They are the eigenspaces of $R_{\tilde Q}$,
$$
\ker(R_{\tilde Q}-\lambda_+)=S_+,\qquad
\ker(R_{\tilde Q}-\lambda_-)=S_-,
$$
and the right action in the same basis is diagonal with the values $\lambda_+,\lambda_-,\lambda_+,\lambda_-$.
The reason is the side of the multiplication: $L_{\tilde Q}$ multiplies on the left and preserves each right ideal, $R_{\tilde Q}$ multiplies on the right and preserves each left ideal.

The two readings are compared in the table.

| Operator | Eigenvalue | Eigenspace | Dimension over $\mathbb{C}$ | Basis |
|---|---|---|---|---|
| $L_{\tilde Q}$ | $\lambda_+$ | $\tilde\Pi_+\mathbb{B}$ | $2$ | $(\tilde\Pi_+,\vec\Upsilon_-)$ |
| $L_{\tilde Q}$ | $\lambda_-$ | $\tilde\Pi_-\mathbb{B}$ | $2$ | $(\vec\Upsilon_+,\tilde\Pi_-)$ |
| $R_{\tilde Q}$ | $\lambda_+$ | $\mathbb{B}\tilde\Pi_+=S_+$ | $2$ | $(\tilde\Pi_+,\vec\Upsilon_+)$ |
| $R_{\tilde Q}$ | $\lambda_-$ | $\mathbb{B}\tilde\Pi_-=S_-$ | $2$ | $(\vec\Upsilon_-,\tilde\Pi_-)$ |

**Restriction to one left ideal.** On $S_+$ the operator $L_{\tilde Q}$ has the two distinct eigenvalues $\lambda_+,\lambda_-$, with eigenbasis $(\tilde\Pi_+,\vec\Upsilon_+)$; on $S_-$ it has the same two eigenvalues, with eigenbasis $(\vec\Upsilon_-,\tilde\Pi_-)$. On each, the eigenvalues are distinct, so the eigenbasis is unique up to two independent scales.

**The eigenprojection and the projector.** The element $\tilde\Pi_+$ is the eigenprojection of the eigenvalue decomposition. The operator $L_{\tilde\Pi_+}$ is the spectral projector onto the $\lambda_+$-eigenspace of $L_{\tilde Q}$: it sends $\tilde Q_{\mathrm{sp}}$ to $\tilde\Pi_+\tilde Q_{\mathrm{sp}}$, the first Peirce component, and its image is the two-dimensional right ideal $\tilde\Pi_+\mathbb{B}$. The two objects must not be confused: $L_{\tilde\Pi_+}$ is an operator on the four-dimensional algebra, while the spectral projector of the multiplication map is defined on the algebra itself.

### The Spinor Spaces and their Coordinates

**A spinor space of $\mathbb{B}$ is a minimal nonzero left ideal. The two spinor spaces are $S_+=\mathbb{B}\tilde\Pi_+$ and $S_-=\mathbb{B}\tilde\Pi_-$, each a complex plane, and the algebra is their direct sum.**

The two spaces are
$$
S_+=\mathbb{B}\tilde\Pi_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+,
\qquad
S_-=\mathbb{B}\tilde\Pi_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi_-,
$$
each of complex dimension two, and
$$
\mathbb{B}=S_+\oplus S_-.
$$
A **spinor of first chirality** is an element of $S_+$; a **spinor of second chirality** is an element of $S_-$.

**The module structure.** Left multiplication makes $S_+$ and $S_-$ left $\mathbb{B}$-modules, and each is a complex plane: a spinor has two complex coordinates. The two are isomorphic as left modules: right multiplication by $\vec\Upsilon_-$ maps $S_+$ onto $S_-$, with inverse right multiplication by $\vec\Upsilon_+$, because
$$
\tilde\Pi_+\vec\Upsilon_-=\vec\Upsilon_-,\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,
\qquad
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,
\qquad
\tilde\Pi_-\vec\Upsilon_+=\vec\Upsilon_+.
$$
They are nevertheless distinct subspaces of $\mathbb{B}$, and the direct sum is the whole algebra.

In the eigenbasis $(\tilde\Pi_+,\vec\Upsilon_+)$ of $S_+$, a spinor of first chirality is
$$
\xi_+=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},21}\vec\Upsilon_+,\qquad Q_{\mathrm{sp},11},Q_{\mathrm{sp},21}\in\mathbb{C},
$$
with the coordinate pair $(Q_{\mathrm{sp},11},Q_{\mathrm{sp},21})$, the first column of the matrix of $\xi_+$. Under left multiplication by $\tilde Q$,
$$
\tilde Q\xi_+=\lambda_+Q_{\mathrm{sp},11}\tilde\Pi_++\lambda_-Q_{\mathrm{sp},21}\vec\Upsilon_+,
$$
so the coordinate pair is sent to
$$
(Q_{\mathrm{sp},11},Q_{\mathrm{sp},21})\longmapsto(\lambda_+Q_{\mathrm{sp},11},\;\lambda_-Q_{\mathrm{sp},21}).
$$
A spinor of second chirality is an element of $S_-$,
$$
\xi_-=Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},22}\tilde\Pi_-,\qquad Q_{\mathrm{sp},12},Q_{\mathrm{sp},22}\in\mathbb{C}.
$$
The order of the coefficients follows the eigenbasis $(\vec\Upsilon_-,\tilde\Pi_-)$ of $S_-$, in which the eigenvalues are $(\lambda_+,\lambda_-)$, so the coordinate pair is $(Q_{\mathrm{sp},12},Q_{\mathrm{sp},22})$, the second column of the matrix of $\xi_-$, and
$$
\tilde Q\xi_-=\lambda_+Q_{\mathrm{sp},12}\vec\Upsilon_-+\lambda_-Q_{\mathrm{sp},22}\tilde\Pi_-
\longmapsto
(\lambda_+Q_{\mathrm{sp},12},\;\lambda_-Q_{\mathrm{sp},22}).
$$
**Left versus right multiplication.** The diagonal action displayed above is the action of $L_{\tilde Q}$ on each spinor space, and it carries both eigenvalues. The space $S_+$ is not an eigenspace of $L_{\tilde Q}$; it is the $\lambda_+$-eigenspace of the right multiplication $R_{\tilde Q}$, and $S_-$ is the $\lambda_-$-eigenspace. The distinction is the side on which $\tilde Q$ multiplies: $R_{\tilde Q}$ is scalar on each $S_\pm$, while $L_{\tilde Q}$ carries the two eigenvalues on each. This is the content of §*The Eigenbasis of Left Multiplication*.

The basis $(\vec\Upsilon_-,\tilde\Pi_-)$ is part of the definition: writing the two vectors in the other order would exchange the two diagonal values.

The two spinor spaces and their coordinates are collected in the table.

| Spinor space | Eigenbasis | Spinor | Coordinates |
|---|---|---|---|
| $S_+=\mathbb{B}\tilde\Pi_+$ | $(\tilde\Pi_+,\vec\Upsilon_+)$ | $Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},21}\vec\Upsilon_+$ | $(Q_{\mathrm{sp},11},Q_{\mathrm{sp},21})$, column $1$ |
| $S_-=\mathbb{B}\tilde\Pi_-$ | $(\vec\Upsilon_-,\tilde\Pi_-)$ | $Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},22}\tilde\Pi_-$ | $(Q_{\mathrm{sp},12},Q_{\mathrm{sp},22})$, column $2$ |

**A general element is a pair of spinors.** Every $\tilde Q_{\mathrm{sp}}\in\mathbb{B}$ splits as
$$
\tilde Q_{\mathrm{sp}}=\tilde Q_{\mathrm{sp}}\tilde\Pi_++\tilde Q_{\mathrm{sp}}\tilde\Pi_-,
$$
and the two summands are a spinor of first chirality and a spinor of second chirality. In the Q-adapted coordinates they are
$$
\tilde Q_{\mathrm{sp}}\longmapsto(Q_{\mathrm{sp},11},Q_{\mathrm{sp},12},Q_{\mathrm{sp},21},Q_{\mathrm{sp},22}),
\qquad
\tilde Q_{\mathrm{sp}}\tilde\Pi_+\longmapsto(Q_{\mathrm{sp},11},Q_{\mathrm{sp},21}),
\qquad
\tilde Q_{\mathrm{sp}}\tilde\Pi_-\longmapsto(Q_{\mathrm{sp},12},Q_{\mathrm{sp},22}).
$$
A general element is therefore not a spinor: it has one spinor component of each chirality.

**Complex dimensions.** Each spinor has two complex components, hence four real parameters. The two spinor spaces have complex dimension two and real dimension four each, and their direct sum has the complex dimension four and the real dimension eight of $\mathbb{B}$. The label "first" versus "second" is fixed by the convention $\tilde\Pi_+=(e_t+\vec\Xi)/2$; replacing the square root by its negative, or exchanging the two labels, exchanges the two chiralities.

### What Depends on $\tilde Q$ and What Does Not

The Q-adapted data depend on $\tilde Q$ through its root. The comparison is collected in the table.

| Object | Depends on $\tilde Q$? |
|---|---|
| Root $\vec\Xi$ and idempotents $\tilde\Pi_\pm$ | yes |
| Corner lines $\mathbb{B}_{+-},\mathbb{B}_{-+}$ as subspaces | yes |
| Left ideals $S_+=\mathbb{B}\tilde\Pi_+$ and $S_-=\mathbb{B}\tilde\Pi_-$ | yes |
| Pair $(\vec\Upsilon_+,\vec\Upsilon_-)$ | up to the reciprocal $\mathbb{C}^{\times}$ |
| Diagonal values $(\lambda_+,\lambda_-)$ of $L_{\tilde Q}$ | yes |
| Peirce coordinates of a general element $\tilde Q_{\mathrm{sp}}$ | yes |

The Q-adapted basis is not the standard Peirce basis attached to the fixed root $i\vec e_z$. The two coincide, up to the reciprocal rescaling, exactly when $\vec Q$ is parallel to $\vec e_z$, that is, when $Q_x=Q_y=0$. In that case $\vec\Xi=\pm i\vec e_z$, the pair is the standard pair up to the exchange of its two members, and the nilpotents are $\vec\Upsilon_x,\vec\Upsilon_y$, in one order or the other, up to the reciprocal rescaling.

### The Degenerate Case $Q_x^2+Q_y^2+Q_z^2=0$

The construction uses $Q_x^2+Q_y^2+Q_z^2\neq0$. When $Q_x^2+Q_y^2+Q_z^2=0$ and $\vec Q\neq0$:
- the root $\vec\Xi=-i\vec Q/\sqrt{Q_x^2+Q_y^2+Q_z^2}$ is undefined;
- no Peirce pair is attached to $\tilde Q$;
- there is no Q-adapted Peirce basis;
- the nilpotents $\vec\Upsilon_\pm$ adapted to $\tilde Q$ do not exist;
- there is no eigenbasis of $L_{\tilde Q}$.

The standard Peirce decomposition of the root $i\vec e_z$ still exists, with its two nilpotents, but it is not attached to $\tilde Q$. In any Peirce basis the Peirce coordinates of $\tilde Q$ have trace $2Q_t$ and determinant $Q_t^2$, because the characteristic polynomial is $(X-Q_t)^2$. They are not diagonalisable, since the minimal polynomial is $(X-Q_t)^2$ when $\vec Q\neq0$. In the Jordan regime $Q_t\neq0$ the multiplication $L_{\tilde Q}$ is a single Jordan block with eigenvalue $Q_t$; in the nilpotent regime $Q_t=0$ it is a nonzero nilpotent.
The nilpotent construction of the standard pair remains available, but it is not the construction of the present section: the present construction takes the nilpotents from the mixed corners of the pair of $\tilde Q$'s own root, and that root does not exist when $Q_x^2+Q_y^2+Q_z^2=0$.

For $\vec Q=0$ the element is scalar, $\tilde Q=Q_te_t$, and $L_{\tilde Q}=Q_t\,\mathrm{id}$ on the whole algebra: every basis is an eigenbasis, the Q-adapted construction is absent, and there is no Jordan or nilpotent regime.

### Summary Block

Given $\tilde Q$ with $Q_x^2+Q_y^2+Q_z^2\neq0$, the following data are attached to $\tilde Q$:
$$
\vec\Xi=-\frac{i\vec Q}{\sqrt{Q_x^2+Q_y^2+Q_z^2}},\qquad
\tilde\Pi_\pm=\frac{e_t\pm\vec\Xi}{2},\qquad
\lambda_\pm=Q_t\pm i\sqrt{Q_x^2+Q_y^2+Q_z^2},
$$
$$
\vec\Upsilon_+\in\mathbb{B}_{-+},\qquad
\vec\Upsilon_-\in\mathbb{B}_{+-},\qquad
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,\qquad
\vec\Upsilon_\pm^2=0,
$$
with the symmetric closed form
$$
\vec\Upsilon_\pm=\frac{B\,\vec w-\dfrac{\Sigma}{B}\,\vec Q\pm\dfrac{i}{2}\,[\vec Q,\vec w]}{2\sqrt{\Sigma^2-3B^2}},
\qquad
\vec w=\vec e_x+\vec e_y+\vec e_z,\quad \Sigma=Q_x+Q_y+Q_z,
$$
valid off the cone $\Sigma^2=3B^2$; on that cone the axis charts
$$
\vec\Upsilon_\pm=\frac{B\,\vec e_\mu-\dfrac{Q_\mu}{B}\,\vec Q\pm\dfrac{i}{2}\,[\vec Q,\vec e_\mu]}{2\sqrt{Q_\mu^2-B^2}},
\qquad \mu=x,y,z,
$$
cover the pair, at least one of the three being defined, and the defined readings differ by the reciprocal rescaling.
$$
\mathbb{B}=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\vec\Upsilon_+\oplus\mathbb{C}\tilde\Pi_-,
$$
$$
S_+=\mathbb{B}\tilde\Pi_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+,\qquad
S_-=\mathbb{B}\tilde\Pi_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi_-,
$$
and every $\tilde Q_{\mathrm{sp}}\in\mathbb{B}$ has the unique expansion
$$
\tilde Q_{\mathrm{sp}}=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},21}\vec\Upsilon_++Q_{\mathrm{sp},22}\tilde\Pi_-,
\qquad a_{ij}\in\mathbb{C},
$$
with $\tilde Q$ itself having $Q_{\mathrm{sp},11}=\lambda_+$, $Q_{\mathrm{sp},22}=\lambda_-$ and $Q_{\mathrm{sp},12}=Q_{\mathrm{sp},21}=0$.

**Diagonal property.**
$$
\tilde Q\tilde\Pi_+=\lambda_+\tilde\Pi_+,\qquad
\tilde Q\vec\Upsilon_-=\lambda_+\vec\Upsilon_-,\qquad
\tilde Q\vec\Upsilon_+=\lambda_-\vec\Upsilon_+,\qquad
\tilde Q\tilde\Pi_-=\lambda_-\tilde\Pi_-.
$$
The Q-adapted Peirce basis is an eigenbasis of $L_{\tilde Q}$ with eigenvalues
$$
(\lambda_+,\lambda_+,\lambda_-,\lambda_-).
$$
The $\lambda_+$-eigenspace of $L_{\tilde Q}$ is the right ideal $\tilde\Pi_+\mathbb{B}$, with basis $(\tilde\Pi_+,\vec\Upsilon_-)$; the $\lambda_-$-eigenspace is $\tilde\Pi_-\mathbb{B}$, with basis $(\vec\Upsilon_+,\tilde\Pi_-)$. The two left ideals $S_+,S_-$ are the eigenspaces of $R_{\tilde Q}$, with eigenvalues $\lambda_+,\lambda_-$ respectively. On each left ideal the restriction of $L_{\tilde Q}$ has the distinct eigenvalues $(\lambda_+,\lambda_-)$, so the eigenbasis of that restriction is unique up to scale.

**Spinors.**
A spinor of first chirality is an element of $S_+$,
$$
\xi_+=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},21}\vec\Upsilon_+,
\qquad (Q_{\mathrm{sp},11},Q_{\mathrm{sp},21})\in\mathbb{C}^2,
$$
and under left multiplication
$$
\tilde Q\xi_+=\lambda_+Q_{\mathrm{sp},11}\tilde\Pi_++\lambda_-Q_{\mathrm{sp},21}\vec\Upsilon_+,
\qquad\text{that is,}\qquad
(Q_{\mathrm{sp},11},Q_{\mathrm{sp},21})\longmapsto(\lambda_+Q_{\mathrm{sp},11},\;\lambda_-Q_{\mathrm{sp},21}).
$$
A spinor of second chirality is an element of $S_-$,
$$
\xi_-=Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},22}\tilde\Pi_-,
\qquad (Q_{\mathrm{sp},12},Q_{\mathrm{sp},22})\in\mathbb{C}^2,
$$
and under left multiplication
$$
\tilde Q\xi_-=\lambda_+Q_{\mathrm{sp},12}\vec\Upsilon_-+\lambda_-Q_{\mathrm{sp},22}\tilde\Pi_-,
\qquad\text{that is,}\qquad
(Q_{\mathrm{sp},12},Q_{\mathrm{sp},22})\longmapsto(\lambda_+Q_{\mathrm{sp},12},\;\lambda_-Q_{\mathrm{sp},22}).
$$
The two spinor spaces are the two minimal left ideals; under left multiplication each is a complex plane carrying the two eigenvalues $\lambda_+,\lambda_-$.

**Degenerate case.**
$$
Q_x^2+Q_y^2+Q_z^2=0:\quad
\text{no Q-adapted Peirce basis and no Q-adapted nilpotents.}
$$
For $\vec Q\neq0$ there is no eigenbasis of $L_{\tilde Q}$: in any Peirce basis the multiplication by $\tilde Q$ is a single Jordan block when $Q_t\neq0$ and a nonzero nilpotent when $Q_t=0$, so it is not diagonal. For $\vec Q=0$ the element is scalar, $L_{\tilde Q}=Q_t\,\mathrm{id}$, and every basis is an eigenbasis; the Q-adapted construction is then absent, but an eigenbasis is not.

## Powers, Polynomial Calculus, and the Group of Units

**The eigenvalue decomposition carries the polynomial calculus and the inverse, and it describes the eigenvalue map of the unit group.**

By Sylvester's formula of *The Lagrange–Sylvester Eigenprojector Formula*, §*Sylvester's Formula*, every polynomial $f\in\mathbb{C}[X]$ acts as
$$
f(\tilde Q)=f(\lambda_+)\tilde\Pi_++f(\lambda_-)\tilde\Pi_-.
$$
In particular
$$
\tilde Q^n=\lambda_+^n\tilde\Pi_++\lambda_-^n\tilde\Pi_-,\qquad n\geq0,
$$
with $\tilde\Pi_++\tilde\Pi_-=e_t$ for $n=0$. In this regime, when $\tilde Q$ is a unit, the two eigenvalues are nonzero, since $\lambda_+\lambda_-=\langle\tilde Q\rangle_{\natural}\neq0$ (*Introduction to the Biquaternion Algebra*, §*The Reduced Norm and Invertibility*), and the formula extends to negative powers:
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

In the Q-adapted basis of §*The Q-Adapted Peirce Basis, the Nilpotents, and the Eigenbasis*, the Peirce coordinates of $\tilde Q_4$ are $(\mu_+,\mu_-)$. The eigenvalue coordinates $(\mu_+,\mu_-)$ are therefore the diagonal Peirce coordinates, and the basis coordinates $(a,\Theta)$ are the same data written in the scalar-vector basis $(e_t,\vec U)$.

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

The eigenvalue decomposition exists exactly when the minimal polynomial is split and squarefree (*The Eigenvalue Decomposition of an Element*, §*Existence and Uniqueness*). The spectrum separates the cases as follows. For $Q_x^2+Q_y^2+Q_z^2\neq0$ the minimal polynomial is $p_{\tilde Q}=(X-Q_t)^2+Q_x^2+Q_y^2+Q_z^2$, which is squarefree: the element is semisimple, with distinct eigenvalues, and the decomposition exists. When in addition $\langle\tilde Q\rangle_{\natural}=0$, one eigenvalue vanishes: this is the zero-divisor regime. For $Q_x^2+Q_y^2+Q_z^2=0$ the characteristic polynomial is $(X-Q_t)^2$; the minimal polynomial is $(X-Q_t)^2$ when $\vec Q\neq0$, and $X-Q_t$ when $\vec Q=0$. The first is the nilpotent regime, named for the vector part, with no eigenvalue decomposition; the element is a unit in the Jordan subcase $Q_t\neq0$ and a pure nilpotent in the subcase $Q_t=0$. The second is the scalar regime, with the one-term decomposition.

| Regime | Condition | Spectrum | Eigenvalue decomposition |
|---|---|---|---|
| Distinct | $Q_x^2+Q_y^2+Q_z^2\neq0$, $\langle\tilde Q\rangle_{\natural}\neq0$ | $\{\lambda_+,\lambda_-\}$ | $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ |
| Zero divisor | $Q_x^2+Q_y^2+Q_z^2\neq0$, $\langle\tilde Q\rangle_{\natural}=0$ | $\{2Q_t,0\}$ | $\tilde Q=2Q_t\tilde\Pi_\sigma$ |
| Scalar | $\vec Q=0$ | $\{Q_t\}$ | $\tilde Q=Q_te_t$ |
| Jordan | $Q_x^2+Q_y^2+Q_z^2=0$, $\vec Q\neq0$, $Q_t\neq0$ | $\{Q_t\}$ | none; the element is a unit |
| Nilpotent | $Q_x^2+Q_y^2+Q_z^2=0$, $\vec Q\neq0$, $Q_t=0$ | $\{0\}$ | none; the element is a nonzero zero divisor |

### The Scalar Regime

**A scalar element has a repeated eigenvalue, the one-term eigenprojection $e_t$, and a non-unique two-projector refinement.**

Let $\vec Q=0$, so $\tilde Q=Q_te_t$. The element is central and semisimple, with the single eigenvalue $Q_t$ and minimal polynomial $X-Q_t$; its centraliser is all of $\mathbb{B}$.

In the sense of the general definition the eigenvalue decomposition has one term, $\tilde Q=Q_te_t$, with the single eigenprojection $e_t$, and it is unique. A decomposition into two primitive idempotents with the repeated coefficient $Q_t$ is a different object: every complete orthogonal pair $\tilde\Pi_1,\tilde\Pi_2$ gives
$$
\tilde Q=Q_t\tilde\Pi_1+Q_t\tilde\Pi_2,
$$
and the pair is not determined by $\tilde Q$. The eigenvalue data therefore determine nothing beyond the scalar, and the two-projector writing is non-unique.

### The Zero-Divisor Regime

**A zero divisor with distinct eigenvalues has one eigenvalue equal to zero and still admits an eigenvalue decomposition.**

Suppose $Q_x^2+Q_y^2+Q_z^2\neq0$ and $\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2=0$. Then $Q_t=\pm i\sqrt{Q_x^2+Q_y^2+Q_z^2}$ and $Q_t\neq0$, and the eigenvalues are
$$
\lambda_\sigma=Q_t+\sigma i\sqrt{Q_x^2+Q_y^2+Q_z^2}=2Q_t,\qquad
\lambda_{-\sigma}=Q_t-\sigma i\sqrt{Q_x^2+Q_y^2+Q_z^2}=0,
$$
where $\sigma\in\{+,-\}$ is the sign for which $Q_t=\sigma i\sqrt{Q_x^2+Q_y^2+Q_z^2}$. They are distinct because $Q_x^2+Q_y^2+Q_z^2\neq0$. The minimal polynomial is
$$
p_{\tilde Q}(X)=X^2-2Q_tX=X(X-2Q_t),
$$
which is squarefree, so $\tilde Q$ is semisimple. The eigenvalue decomposition is
$$
\tilde Q=2Q_t\tilde\Pi_\sigma+0\cdot\tilde\Pi_{-\sigma},
$$
and $\tilde Q=2Q_t\tilde\Pi_\sigma$ is a nonzero scalar multiple of the idempotent $\tilde\Pi_\sigma$. The element is a zero divisor, since $\tilde Q\tilde\Pi_{-\sigma}=0$ with $\tilde\Pi_{-\sigma}\neq0$, and it is not a unit; the decomposition survives because one eigenvalue vanishes, exactly as in the split-complex and reduced biquaternion cases. The nilpotent regime of §*The Nilpotent Regime* is different: there the minimal polynomial has a repeated root.

### The Nilpotent Regime

**A nonzero nilpotent vector part makes the element non-semisimple, and no eigenvalue decomposition exists. The regime is named for the vector part: the element itself is nilpotent exactly when $Q_t=0$, in which case it is a nonzero zero divisor.**

Let $Q_x^2+Q_y^2+Q_z^2=0$ and $\vec Q\neq0$. Then $\vec Q^2=0$, so $\vec\Upsilon=\vec Q$ is a pure nilpotent, written with the arrow and without the tilde by §*The Nilpotent Convention* of *Conventions in Mathematics*, and
$$
\tilde Q=Q_te_t+\vec\Upsilon,\qquad \vec\Upsilon^2=0.
$$
The element is a unit exactly when $Q_t\neq0$, since $\langle\tilde Q\rangle_{\natural}=Q_t^2$ (*Introduction to the Biquaternion Algebra*, §*The Reduced Norm and Invertibility*), and its minimal polynomial is
$$
(X-Q_t)^2,
$$
which is not squarefree. By the theorem of *The Eigenvalue Decomposition of an Element*, §*Existence and Uniqueness*, $\tilde Q$ has no eigenvalue decomposition. The multiplication $L_{\tilde Q}$ is a single Jordan block with eigenvalue $Q_t$.

The centraliser of $\tilde Q$ is
$$
\{ae_t+b\vec\Upsilon:\ a,b\in\mathbb{C}\}.
$$
Its only idempotents are $0$ and $e_t$: if $(ae_t+b\vec\Upsilon)^2=ae_t+b\vec\Upsilon$, then $a^2=a$ and $2ab=b$, so $(a,b)=(0,0)$ or $(1,0)$. Hence no pair of nonzero orthogonal idempotents summing to $e_t$ lies in it, and there is no Peirce decomposition adapted to $\tilde Q$ into two primitive idempotents.

## Remarks

1. **Relation to the Lagrange–Sylvester formula.** The formulas for $\tilde\Pi_\pm$ are the Lagrange–Sylvester formulas applied to the quadratic $p_{\tilde Q}$: they are the eigenprojections of the multiplication $L_{\tilde Q}$ on the commutative plane $\mathbb{C}[\tilde Q]$. The biquaternion-specific content is the identification of the eigenprojections with the idempotents of a pure root of $+1$, and of the eigenvalue data with the scalar part and the complex angle along $\vec U$.

2. **Centrality and the Peirce decomposition.** The idempotents $\tilde\Pi_\pm$ are noncentral: they commute with $\tilde Q$ and with its centraliser, but not with all of $\mathbb{B}$. There is no nontrivial central idempotent in $\mathbb{B}$, since the algebra is simple (§*The Two-Sided Ideals* of *Ideals and Peirce Decomposition of the Biquaternion Algebra*). The decomposition is therefore a Peirce decomposition relative to an element-dependent idempotent, not a decomposition of the algebra into ideals.

3. **Uniqueness and labelling.** The decomposition is canonical only as the unordered set of pairs $\{(\lambda_+,\tilde\Pi_+),(\lambda_-,\tilde\Pi_-)\}$. The labelling is interchanged by replacing the square root by its negative and sending $\vec\Xi$ to $-\vec\Xi$; it is fixed by the convention of §*The Eigenvalue Decomposition* exactly when the square root can be taken real and positive.

4. **Degenerate regimes.** The eigenvalue decomposition is a property of semisimple elements; the number of its terms is the number of distinct eigenvalues. The zero-divisor regime is semisimple with one eigenvalue zero and keeps a two-term decomposition. The nilpotent regime is non-semisimple and admits none. The scalar regime is semisimple with a repeated eigenvalue: the general decomposition has one term, and any two-projector refinement is non-unique.

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
| Polynomial calculus | $f(\tilde Q)=f(\lambda_+)\tilde\Pi_++f(\lambda_-)\tilde\Pi_-$ |
| Group of units | $\mathbb{B}^\times$; the eigenvalue map to $\mathbb{C}^\times\times\mathbb{C}^\times$ is surjective, not injective and not a group homomorphism |

### Regimes

The zero-divisor row is a subcase of the distinct-eigenvalue case $Q_x^2+Q_y^2+Q_z^2\neq0$, separated because the norm vanishes and one eigenvalue is zero; the scalar row includes $\tilde Q=0$. The nilpotent regime is split into the invertible Jordan case and the pure nilpotent.

| Regime | Condition | Spectrum | Minimal polynomial | Eigenvalue decomposition |
|---|---|---|---|---|
| Distinct | $Q_x^2+Q_y^2+Q_z^2\neq0$, $\langle\tilde Q\rangle_{\natural}\neq0$ | $\{\lambda_+,\lambda_-\}$, distinct | $(X-Q_t)^2+Q_x^2+Q_y^2+Q_z^2$ | $\tilde Q=\lambda_+\tilde\Pi_+ + \lambda_-\tilde\Pi_-$ |
| Zero divisor | $Q_x^2+Q_y^2+Q_z^2\neq0$, $\langle\tilde Q\rangle_{\natural}=0$ | $\{\lambda_\sigma,\lambda_{-\sigma}\}=\{2Q_t,0\}$ | $X(X-2Q_t)$ | $\tilde Q=2Q_t\tilde\Pi_\sigma + 0\cdot\tilde\Pi_{-\sigma}$ |
| Scalar | $\vec Q=0$ | $\{Q_t\}$ | $X-Q_t$ | $\tilde Q=Q_t e_t$; refinement $Q_t\tilde\Pi_1 + Q_t\tilde\Pi_2$ |
| Jordan | $Q_x^2+Q_y^2+Q_z^2=0$, $\vec Q\neq0$, $Q_t\neq0$ | $\{Q_t\}$ | $(X-Q_t)^2$ | none; the element is a unit |
| Nilpotent | $Q_x^2+Q_y^2+Q_z^2=0$, $\vec Q\neq0$, $Q_t=0$ | $\{0\}$ | $X^2$ | none; the element is a nonzero zero divisor |

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
| General element in the eigenbasis | coordinates $(\xi_+,\xi_-)$ | coordinates $(\xi_+,\xi_-)$ | coordinates $(Q_{\mathrm{sp},11},Q_{\mathrm{sp},12},Q_{\mathrm{sp},21},Q_{\mathrm{sp},22})$ |
| Nilpotents in the eigenbasis | none | none | $\vec\Upsilon_\pm$ |
| Spinor spaces | $S_\pm=\mathbb{R}\Pi_\pm$, real lines | $S_\pm=\mathbb{C}\Pi_\pm$, complex lines | $S_\pm=\mathbb{B}\tilde\Pi_\pm\cong\mathbb{C}^2$, complex planes |
| Spinor coordinates | one real coefficient per chirality | one complex coefficient per chirality | two complex coefficients per chirality |
| Action of $Q$ on a spinor | scalar: $\lambda_+$ on $S_+$, $\lambda_-$ on $S_-$ | scalar: $\lambda_+$ on $S_+$, $\lambda_-$ on $S_-$ | the two scalars $\lambda_+,\lambda_-$ on each $S_\pm$ |
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
- The corpus articles: [The Eigenvalue Decomposition of an Element](the-eigenvalue-decomposition-of-an-element.html), [The Lagrange–Sylvester Eigenprojector Formula](the-lagrange-sylvester-eigenprojector-formula.html), [The Centraliser and the Diagonal Peirce Part](the-centraliser-and-the-diagonal-peirce-part.html), [Off-Diagonal Peirce Components and Noncentral Idempotents](off-diagonal-peirce-components-and-noncentral-idempotents.html), [Biquaternion Spectral Theory](biquaternion-spectral-theory.html), [Ideals and Peirce Decomposition of the Biquaternion Algebra](ideals-and-peirce-decomposition-of-the-biquaternion-algebra.html), [Square Roots of One and the Idempotents of the Biquaternion Algebra](square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), [Introduction to the Biquaternion Algebra](introduction-to-the-biquaternion-algebra.html), [Nilpotent Elements and the Jordan–Chevalley Decomposition](nilpotent-elements-and-the-jordan-chevalley-decomposition.html), [Quaternion Spectral Theory](quaternion-spectral-theory.html), [Reduced Biquaternion Spectral Theory](reduced-biquaternion-spectral-theory.html), [The Biquaternion Eigenvalue Decomposition](the-biquaternion-eigenvalue-decomposition.html), [Eigenbasis of a Split-Complex Number](eigenbasis-of-a-split-complex-number.html), [Eigenbasis of a Reduced Biquaternion](eigenbasis-of-a-reduced-biquaternion.html) and [Conventions in Mathematics](conventions-in-mathematics.html).
