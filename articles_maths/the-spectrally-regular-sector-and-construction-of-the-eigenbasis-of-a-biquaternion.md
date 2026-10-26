# __The Eigenbasis__

## Introduction

The eigenbasis of a biquaternion is a basis of the algebra that depends on the biquaternion. It exists, as a basis attached to the element, exactly when the two eigenvalues are distinct, that is when $B^2\neq0$, and it is the coordinate system in which left multiplication by the element is diagonal. The companion article *The Spectrum* proves that such a basis exists. This article constructs it, proves that the normalised Peirce representative is unique, proves that every biquaternion has a unique expansion in it, and reads the spinor spaces and chirality in it.

**Place among the Peirce decompositions.** This article is the regular particular case of *The Peirce Decomposition*. That article attaches a Peirce basis to any complete orthogonal pair of idempotents, and shows that the four basis vectors split into the two couples $\mathcal{C}_+=(\tilde\Pi_+,\vec\Upsilon_+)$ and $\mathcal{C}_-=(\vec\Upsilon_-,\tilde\Pi_-)$, on which left multiplication acts by the same Peirce matrix. Here the pair is the spectral pair: it exists exactly when $B^2\neq0$, it commutes with $\tilde Q$, and the Peirce matrix is $\operatorname{diag}(\lambda_+,\lambda_-)$. Each couple is therefore a pair of eigenvectors, and the Peirce basis is the eigenbasis. The general theory leaves a reciprocal $\mathbb{C}^\times$ of mixed bases; the normalisation below fixes it.

The construction has three steps. The root $\vec\Xi=-i\vec Q/B$ is a pure square root of $e_t$ and carries the two spectral idempotents $\tilde\Pi_\pm=(e_t\pm\vec\Xi)/2$. The two mixed Peirce corners are complex lines, and a generator $\vec\Upsilon_+$ of one of them determines a generator $\vec\Upsilon_-$ of the other by the product condition $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$. The pair is then determined up to the reciprocal rescaling $\vec\Upsilon_+\mapsto\mu\vec\Upsilon_+$, $\vec\Upsilon_-\mapsto\mu^{-1}\vec\Upsilon_-$. A normalisation fixes $\mu$, and with the normalisation fixed the quadruple

$$
\mathcal{B}(\tilde Q)=(\tilde\Pi_+,\ \vec\Upsilon_-,\ \vec\Upsilon_+,\ \tilde\Pi_-)
$$

is unique. The first two steps use only $B^2\neq0$, so the construction covers the whole spectral-regular sector.

The basis has a further property that is easy to miss: it depends on $\tilde Q$ only through the complex line spanned by the vector part. The elements $\tilde Q$ and $a\tilde Q+b e_t$, with $a\neq0$, share the same eigenbasis, while their eigenvalues move affinely. The eigenbasis is therefore attached to a point of $\mathbb{P}^2$, not to a point of $\mathbb{B}$.

The second part of the article reads spinors and chirality in this basis. The two minimal left ideals $S_\pm=\mathbb{B}\tilde\Pi_\pm$ are the two chiralities. Each has a basis made of one idempotent and one nilpotent of $\mathcal{B}(\tilde Q)$, and left multiplication by $\tilde Q$ acts on each by the same diagonal matrix $\operatorname{diag}(\lambda_+,\lambda_-)$. Chirality is a right-multiplication label, not a left eigenvalue: the two gradings are independent, and the four basis vectors are the four cells of their grid.

**Notation.** An element is $\tilde Q=Q_te_t+\vec Q$, with $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ and $\vec Q^2=-B^2e_t$, where

$$
B^2=Q_x^2+Q_y^2+Q_z^2.
$$

The number $B$ is a fixed complex square root of $B^2$; the other root exchanges the two labels. A general element is written $\tilde Q_2=Q_{2,t}e_t+\vec Q_2$; the subscript distinguishes it from the fixed element $\tilde Q$ whose eigenbasis is constructed. The plain product is the associative product of $\mathbb{B}$, with unit $e_t$ and natural conjugation $\tilde Q^{\natural}=Q_t-\vec Q$. The trace is $\operatorname{Tr}(\tilde Q_2)=2Q_{2,t}$, and $\langle\tilde Q_2\rangle_{\natural}=\operatorname{Sc}(\tilde Q_2^{\natural}\tilde Q_2)$ is the scalar of $\tilde Q_2^{\natural}\tilde Q_2$. The Peirce corners of a pair of idempotents are $\mathbb{B}_{st}=\tilde\Pi_s\mathbb{B}\tilde\Pi_t$. The letters $L_{\tilde Q_2}$ and $R_{\tilde Q_2}$ denote left and right multiplication by $\tilde Q_2$.

## The Spectral Condition and the Root

**Spectral regularity is the single hypothesis of the construction. It produces the root and the two idempotents, and nothing else is needed.**

### The Spectral-Regular Sector

The condition $B^2\neq0$ defines the complement of the spectral-degenerate cone $\mathcal S$. On it the two eigenvalues are distinct, the minimal polynomial is squarefree, and the spectral decomposition exists. Whether an eigenvalue vanishes is irrelevant to the construction: the formulas below treat both cases together.

On $B^2=0$ the element is $Q_te_t+\vec Q$ with $\vec Q^2=0$. For $\vec Q\neq0$ its minimal polynomial is $(X-Q_t)^2$, so $L_{\tilde Q}$ has a two-dimensional eigenspace and no eigenbasis; on the scalar line $\vec Q=0$, $L_{\tilde Q}$ is scalar and every basis is an eigenbasis. At the origin every basis is an eigenbasis. The construction below therefore covers exactly $B^2\neq0$.

### The Root

**Proposition (the root).** Let $B^2\neq0$ and

$$
\vec\Xi=-\frac{i\vec Q}{B}.
$$

Then $\vec\Xi$ is pure, $\vec\Xi^2=e_t$, and

$$
\tilde Q=Q_te_t+iB\vec\Xi.
$$

*Proof.* Since $\vec Q^2=-B^2e_t$, one has $\vec\Xi^2=(-i)^2\vec Q^2/B^2=-(-B^2e_t)/B^2=e_t$. The element is pure because $\vec Q$ is pure. The last identity is $\vec Q=iB\vec\Xi$.

The root is the vector part scaled to square $e_t$, up to the factor $-i$. It depends on $\vec Q$ only through its direction: replacing $\vec Q$ by $a\vec Q$ and $B$ by $aB$ leaves $\vec\Xi$ unchanged.

### The Idempotents

**Theorem (the spectral idempotents).** With $\vec\Xi$ as above, put

$$
\tilde\Pi_+=\frac{e_t+\vec\Xi}{2},\qquad
\tilde\Pi_-=\frac{e_t-\vec\Xi}{2}.
$$

Then $\tilde\Pi_\pm$ are non-zero idempotents, orthogonal, complete, and

$$
\tilde Q\tilde\Pi_\pm=\lambda_\pm\tilde\Pi_\pm,\qquad
\lambda_\pm=Q_t\pm iB,\qquad
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-.
$$

*Proof.* The idempotence is $\tilde\Pi_\pm^2=(e_t\pm2\vec\Xi+\vec\Xi^2)/4=\tilde\Pi_\pm$, the orthogonality is $\tilde\Pi_+\tilde\Pi_-=(e_t-\vec\Xi^2)/4=0$, and the sum is $e_t$. The action is

$$
\tilde Q\tilde\Pi_+=(Q_te_t+iB\vec\Xi)\frac{e_t+\vec\Xi}{2}
=\frac{(Q_t+iB)(e_t+\vec\Xi)}{2}=\lambda_+\tilde\Pi_+,
$$

and the other sign is the same. Adding the two identities gives the decomposition.

**Corollary (Lagrange form).** The idempotents are

$$
\tilde\Pi_\pm=\frac{\tilde Q-\lambda_\mp e_t}{\lambda_\pm-\lambda_\mp},
$$

and they are the unique spectral idempotents of $\tilde Q$.

*Proof.* The Lagrange form is the identity $\tilde Q-\lambda_\mp e_t=\pm 2iB\tilde\Pi_\pm$. For uniqueness, the minimal polynomial $(X-\lambda_+)(X-\lambda_-)$ is squarefree, so the spectral idempotents are the two idempotents of $\mathbb{C}[\tilde Q]\cong\mathbb{C}\times\mathbb{C}$, and they are determined by $\tilde Q$.

### The Two Branches

Replacing $B$ by $-B$ replaces $\vec\Xi$ by $-\vec\Xi$. This exchanges $\tilde\Pi_+$ and $\tilde\Pi_-$ and exchanges $\lambda_+$ and $\lambda_-$. The unordered pair of idempotents and the unordered spectrum are unchanged. The branch is therefore a labelling choice, not a second construction; throughout the article the square root is fixed by the normalisation, and the labels follow from it.

## The Corners and the Nilpotents

**The two idempotents split the algebra into four one-dimensional corners. The diagonal corners contain the idempotents; the mixed corners are the two lines on which the nilpotents live.**

### The Peirce Corners

**Definition (corners).** For $s,t\in\{+,-\}$ put

$$
\mathbb{B}_{st}=\tilde\Pi_s\mathbb{B}\tilde\Pi_t=\{\tilde Q_2:\ \tilde\Pi_s\tilde Q_2=\tilde Q_2,\ \tilde Q_2\tilde\Pi_t=\tilde Q_2\}.
$$

The corner rule is

$$
\mathbb{B}_{st}\mathbb{B}_{uv}\subseteq\delta_{tu}\mathbb{B}_{sv}.
$$

Each corner is a complex line (*The Peirce Decomposition*), and the direct sum is the algebra:

$$
\mathbb{B}=\mathbb{B}_{++}\oplus\mathbb{B}_{+-}\oplus\mathbb{B}_{-+}\oplus\mathbb{B}_{--}.
$$

In the eigenbasis of the next section the four corners are spanned by the four basis vectors. The two diagonal corners are spanned by the idempotents themselves:

$$
\mathbb{B}_{++}=\mathbb{C}\tilde\Pi_+,\qquad
\mathbb{B}_{--}=\mathbb{C}\tilde\Pi_-.
$$

The two mixed corners are the ones that carry the nilpotents:

$$
\mathbb{B}_{+-}=\mathbb{C}\vec\Upsilon_-,\qquad
\mathbb{B}_{-+}=\mathbb{C}\vec\Upsilon_+.
$$

The order of the indices is fixed by $\mathbb{B}_{+-}=\tilde\Pi_+\mathbb{B}\tilde\Pi_-$: the first index is the left multiplication side, the second the right multiplication side.

### The Nilpotent Pair

**Lemma (one generator determines the other).** Let $0\neq u\in\mathbb{B}_{-+}$. Then there is a unique $v\in\mathbb{B}_{+-}$ with $uv=\tilde\Pi_-$. It satisfies

$$
vu=\tilde\Pi_+,\qquad v^2=0.
$$

*Proof.* The map $\mathbb{B}_{+-}\to\mathbb{C}\tilde\Pi_-$, $x\mapsto ux$, is linear between complex lines. It is non-zero: if $u\mathbb{B}_{+-}=0$, then for every $b\in\mathbb{B}$ the element $\tilde\Pi_+b\tilde\Pi_-$ lies in $\mathbb{B}_{+-}$, so $u\tilde\Pi_+b\tilde\Pi_-=0$; since $u\tilde\Pi_+=u$, this gives $u\mathbb{B}\tilde\Pi_-=0$. Multiplying on the left by $\mathbb{B}$ gives $\mathbb{B}u\mathbb{B}\tilde\Pi_-=0$, contradicting the simplicity of $\mathbb{B}$ and $\tilde\Pi_-\neq0$. A non-zero linear map between lines is an isomorphism, so a unique $v$ maps to $\tilde\Pi_-$. Then $u(vu)=(uv)u=u$, and $vu\in\mathbb{C}\tilde\Pi_+$, so $vu=\tilde\Pi_+$. Finally $v^2\in\mathbb{B}_{+-}\mathbb{B}_{+-}=0$.

**Theorem (the pair).** Let $0\neq\vec\Upsilon_+\in\mathbb{B}_{-+}$ and let $\vec\Upsilon_-\in\mathbb{B}_{+-}$ be the element of the lemma. Then

$$
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,\qquad
\vec\Upsilon_\pm^2=0.
$$

Conversely, every pair with these three properties arises this way, and every admissible pair is obtained from $(\vec\Upsilon_+,\vec\Upsilon_-)$ by the reciprocal rescaling

$$
\vec\Upsilon_+\longmapsto\mu\vec\Upsilon_+,\qquad
\vec\Upsilon_-\longmapsto\mu^{-1}\vec\Upsilon_-,\qquad
\mu\in\mathbb{C}^{\times}.
$$

*Proof.* The three identities are the lemma. Conversely, a pair with these properties has $(\mu\vec\Upsilon_+)(\mu^{-1}\vec\Upsilon_-)=\tilde\Pi_-$, and the mixed corners are lines, so every pair is of this form.

**Remark (the residual freedom).** The theorem says that the algebraic data determine the pair only up to one complex scalar. The scale is not a property of the element; it is the freedom of choosing a generator in the one-dimensional corner. A normalisation is precisely a rule that selects one pair in each orbit.

### The Transverse-Vector Construction

**A fixed auxiliary vector turns the lemma into a formula. Every pure $V$ with $V_\perp^2\neq0$ produces an admissible pair.**

Let $V$ be pure and put

$$
V_\perp=V-\frac{(V,\vec Q)}{B^2}\vec Q,\qquad
(V,\vec Q)=V_xQ_x+V_yQ_y+V_zQ_z,
$$

so that $V_\perp$ is the projection of $V$ on the orthogonal complement of $\vec Q$. Then

$$
V_\perp^2=V^2+\frac{(V,\vec Q)^2}{B^2},
$$

and $V_\perp^2\neq0$ means that the projection $V_\perp$ is not isotropic.

**Proposition (the pair from a transverse vector).** Let $V$ be pure with $V_\perp^2\neq0$, and put

$$
u_+=\tilde\Pi_-V\tilde\Pi_+,\qquad
u_-=\tilde\Pi_+V\tilde\Pi_-.
$$

Then $u_\pm\neq0$ and

$$
u_+u_-=V_\perp^2\,\tilde\Pi_-,\qquad
u_-u_+=V_\perp^2\,\tilde\Pi_+.
$$

Consequently, for either square root $\alpha$ of $V_\perp^2$,

$$
\vec\Upsilon_+=\frac{u_+}{\alpha},\qquad
\vec\Upsilon_-=\frac{u_-}{\alpha}
$$

is an admissible pair.

*Proof.* Write $V=V_\parallel+V_\perp$, with $V_\parallel=((V,\vec Q)/B^2)\vec Q$ proportional to $\vec Q$ and hence commuting with $\vec\Xi$. The component $V_\parallel$ commutes with both idempotents, so it contributes only to the diagonal corners and drops out of $u_\pm$. For $V_\perp$ one expands

$$
u_\pm=\frac12\left(V_\perp\pm V_\perp\times\vec\Xi+(V_\perp,\vec\Xi)\vec\Xi\right),
$$

using $V_\perp\times\vec\Xi=\tfrac12(V_\perp\vec\Xi-\vec\Xi V_\perp)$. Multiplying the two expressions and using $\vec\Xi^2=e_t$ and $(V_\perp,\vec\Xi)=0$ gives $u_+u_-=V_\perp^2\tilde\Pi_-$. The other product is the same computation with the signs exchanged.

**Corollary (the closed forms).** Take $V=\vec w=\vec e_x+\vec e_y+\vec e_z$ and $\Sigma=Q_x+Q_y+Q_z$. Then $V_\perp^2=(\Sigma^2-3B^2)/B^2$, and, off the exceptional cone $\Sigma^2=3B^2$,

$$
\vec\Upsilon_\pm=
\frac{B\,\vec w-\dfrac{\Sigma}{B}\,\vec Q\pm\dfrac{i}{2}\,[\vec Q,\vec w]}
{2\sqrt{\Sigma^2-3B^2}}.
$$

On the exceptional cone, take $V=\vec e_\mu$ for any $\mu\in\{x,y,z\}$ with $Q_\mu^2\neq B^2$. Then

$$
\vec\Upsilon_\pm=
\frac{B\,\vec e_\mu-\dfrac{Q_\mu}{B}\,\vec Q\pm\dfrac{i}{2}\,[\vec Q,\vec e_\mu]}
{2\sqrt{Q_\mu^2-B^2}}.
$$

At least one of the three axes satisfies $Q_\mu^2\neq B^2$ when $B^2\neq0$, because otherwise $Q_x^2=Q_y^2=Q_z^2=B^2$ would give $B^2=3B^2$.

The two formulas are the same construction with two different auxiliary vectors. On their common domain they differ by the reciprocal rescaling of the theorem, because both pairs satisfy the same product conditions.

**Remark (the normalisation used in this article).** The convention is: use the symmetric formula when $\Sigma^2\neq3B^2$; otherwise use the axis chart of the first $\mu\in\{x,y,z\}$, in that order, with $Q_\mu^2\neq B^2$; and fix the square roots at one representative of each direction $[\vec Q]$, extending along the fibre by $B(a\tilde Q+b e_t)=aB(\tilde Q)$ and $\sqrt{a^2s}=a\sqrt s$ for $a\neq0$. The condition $\Sigma^2=3B^2$ and the axis choice depend on $[\vec Q]$ only. This selects one pair at every spectral-regular $\tilde Q$, and the displayed formulas are homogeneous of degree zero. The choice is pointwise: it assigns a pair to each element, and no continuity of the branch is required. It is a normalisation in the sense of the previous subsection, and it is the one used in the displayed formulas. The axis charts are only a coordinate device: they cover the exceptional cone, where the symmetric formula is singular, and they do not add a second eigenbasis.

## The Eigenbasis

**With the normalisation fixed, the four vectors are a basis, and left and right multiplication by $\tilde Q$ are diagonal in it.**

### The Basis and the Multiplication Table

**Definition (the eigenbasis).** For a spectral-regular $\tilde Q$ with the normalisation above, the **eigenbasis** is

$$
\mathcal{B}(\tilde Q)=(\tilde\Pi_+,\ \vec\Upsilon_-,\ \vec\Upsilon_+,\ \tilde\Pi_-).
$$

**Theorem (basis and diagonalisation).** The four vectors are non-zero and lie in the four corners $\mathbb{B}_{++},\mathbb{B}_{+-},\mathbb{B}_{-+},\mathbb{B}_{--}$ respectively. They form a basis of $\mathbb{B}$, and

$$
L_{\tilde Q}=\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-),\qquad
R_{\tilde Q}=\operatorname{diag}(\lambda_+,\lambda_-,\lambda_+,\lambda_-)
$$

in that basis.

*Proof.* The corner of each vector is read from the indices: $\tilde\Pi_+\in\mathbb{B}_{++}$, $\vec\Upsilon_-\in\mathbb{B}_{+-}$, $\vec\Upsilon_+\in\mathbb{B}_{-+}$, $\tilde\Pi_-\in\mathbb{B}_{--}$. The corners are lines and their direct sum is $\mathbb{B}$, so four non-zero vectors, one in each, form a basis. For the left action, $\tilde Q\tilde\Pi_\pm=\lambda_\pm\tilde\Pi_\pm$ and

$$
\tilde Q\vec\Upsilon_-=(\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-)\vec\Upsilon_-=\lambda_+\tilde\Pi_+\vec\Upsilon_-=\lambda_+\vec\Upsilon_-,
$$

$$
\tilde Q\vec\Upsilon_+=(\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-)\vec\Upsilon_+=\lambda_-\tilde\Pi_-\vec\Upsilon_+=\lambda_-\vec\Upsilon_+.
$$

For the right action, $\vec\Upsilon_-\tilde Q=\lambda_-\vec\Upsilon_-$ and $\vec\Upsilon_+\tilde Q=\lambda_+\vec\Upsilon_+$, with the idempotents as stated.

The multiplication of the four basis vectors is the table. The row is the left factor and the column is the right factor.

| product | $\tilde\Pi_+$ | $\vec\Upsilon_-$ | $\vec\Upsilon_+$ | $\tilde\Pi_-$ |
|---|---|---|---|---|
| $\tilde\Pi_+$ | $\tilde\Pi_+$ | $\vec\Upsilon_-$ | $0$ | $0$ |
| $\vec\Upsilon_-$ | $0$ | $0$ | $\tilde\Pi_+$ | $\vec\Upsilon_-$ |
| $\vec\Upsilon_+$ | $\vec\Upsilon_+$ | $\tilde\Pi_-$ | $0$ | $0$ |
| $\tilde\Pi_-$ | $0$ | $0$ | $\vec\Upsilon_+$ | $\tilde\Pi_-$ |

The table is the corner rule written out. It shows that the basis is a system of matrix units, with $\tilde\Pi_+$ and $\tilde\Pi_-$ the two diagonal units and the nilpotents the two off-diagonal units.

**Remark (in what sense the eigenbasis is unique).** The uniqueness is that of the normalised Peirce representative. The operator $L_{\tilde Q}$ has two distinct eigenvalues, and each eigenspace is two-dimensional; any basis of each eigenspace is therefore an eigenbasis of $L_{\tilde Q}$, and the set of eigenbases is not unique. What is unique, with the normalisation of §*The Transverse-Vector Construction*, is the quadruple made of the two spectral idempotents and the two normalised corner generators. Every statement of uniqueness in this article refers to that quadruple.

### The Fourier Reading of the Basis

Put $\rho=i\vec\Xi=\vec Q/B$, a pure root of $-1$. Choose a pure $\nu$ with $\nu^2=1$ and $\nu\cdot\rho=0$, and put $\xi=\rho\nu$; then $(e_t,\rho,\nu,\xi)$ is the root-adapted basis of *Biquaternion Continuous Harmonic Analysis*, §*The Change of Basis*, and

$$
L_\rho\sim
\begin{pmatrix}
0&-1&0&0\\
1&0&0&0\\
0&0&0&-1\\
0&0&1&0
\end{pmatrix},
$$

the block of the complex structure repeated on the two planes.

**Proposition (the Fourier form of the eigenbasis).** With
$$
u_-=\tilde\Pi_+\nu=\tfrac12(\nu-i\xi),
\qquad
u_+=\tilde\Pi_-\nu=\tfrac12(\nu+i\xi),
$$
the quadruple $(\tilde\Pi_+,u_-,u_+,\tilde\Pi_-)$ is an eigenbasis of $L_{\tilde Q}$ with the eigenvalues $(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$, and $\rho u_-=+iu_-$, $\rho u_+=-iu_+$.

*Proof.* Since $\vec\Xi=-i\rho$ and $\rho\nu=\xi$, we have $\vec\Xi\nu=-i\xi$, so $\tilde\Pi_+\nu=\tfrac12(\nu-i\xi)=u_-$ and $\tilde\Pi_-\nu=\tfrac12(\nu+i\xi)=u_+$. From $\rho\nu=\xi$ and $\rho\xi=-\nu$, $\rho u_-=\tfrac12(\xi+i\nu)=iu_-$ and $\rho u_+=\tfrac12(\xi-i\nu)=-iu_+$. Left multiplication by $\tilde Q=Q_te_t+B\rho$ is $Q_t\mathrm{id}+BL_\rho$, which gives the stated eigenvalues.

**The two cuts.** In the matrix model of §*The Matrix Model*, the first Fourier plane is the diagonal subspace and the second is the off-diagonal subspace. The spectral eigenspaces are the two rows: $E_+=\operatorname{span}\{\tilde\Pi_+,u_-\}$ is the first row, $E_-=\operatorname{span}\{u_+,\tilde\Pi_-\}$ the second. Each row meets each Fourier plane in one line, so neither decomposition refines the other. The Fourier factorization keeps the planes and applies an ordinary complex transform to each; the spectral decomposition regroups the four lines by eigenvalue.

### The Four Labels

Each basis vector is a joint eigenvector of four operators: left and right multiplication by $\tilde Q$ and by $\vec\Xi$. The labels are the corner indices.

| vector | corner | left ideal | $L_{\tilde Q}$ | $R_{\tilde Q}$ | $L_{\vec\Xi}$ | $R_{\vec\Xi}$ |
|---|---|---|---|---|---|---|
| $\tilde\Pi_+$ | $\mathbb{B}_{++}$ | $S_+$ | $\lambda_+$ | $\lambda_+$ | $+1$ | $+1$ |
| $\vec\Upsilon_-$ | $\mathbb{B}_{+-}$ | $S_-$ | $\lambda_+$ | $\lambda_-$ | $+1$ | $-1$ |
| $\vec\Upsilon_+$ | $\mathbb{B}_{-+}$ | $S_+$ | $\lambda_-$ | $\lambda_+$ | $-1$ | $+1$ |
| $\tilde\Pi_-$ | $\mathbb{B}_{--}$ | $S_-$ | $\lambda_-$ | $\lambda_-$ | $-1$ | $-1$ |

The identity $\tilde Q=Q_te_t+iB\vec\Xi$ explains the table: the left value is $Q_t+iBs$, the right value is $Q_t+iBt$, where $s$ and $t$ are the two signs. The two gradings, by left index and by right index, are independent, and the four rows are their four combinations.

### The Matrix Model

Assign the four basis vectors to the matrix units by

$$
\tilde\Pi_+\longmapsto E_{11},\qquad
\vec\Upsilon_-\longmapsto E_{12},\qquad
\vec\Upsilon_+\longmapsto E_{21},\qquad
\tilde\Pi_-\longmapsto E_{22}.
$$

Then every element $\tilde Q_2\in\mathbb{B}$ has the unique expansion

$$
\tilde Q_2=Q_{2,11}\tilde\Pi_++Q_{2,12}\vec\Upsilon_-+Q_{2,21}\vec\Upsilon_++Q_{2,22}\tilde\Pi_-,
\qquad Q_{2,ij}\in\mathbb{C},
$$

and is represented by

$$
\mathsf M_2^{Q}(\tilde Q_2)=
\begin{pmatrix}
Q_{2,11}&Q_{2,12}\\
Q_{2,21}&Q_{2,22}
\end{pmatrix}.
$$

The assignment is an isomorphism of algebras, and the element $\tilde Q$ itself has the diagonal matrix

$$
\mathsf M_2^{Q}(\tilde Q)=
\begin{pmatrix}
\lambda_+&0\\
0&\lambda_-
\end{pmatrix}.
$$

The two columns are the two spinor spaces, and the two rows are the two spectral eigenspaces. The entries are indexed by the corner: $Q_{2,ij}$ is the coefficient of the basis vector in $\mathbb{B}_{ij}$.

**Proposition (trace and determinant).** For every $\tilde Q_2\in\mathbb{B}$,

$$
\operatorname{Tr}\mathsf M_2^{Q}(\tilde Q_2)=Q_{2,11}+Q_{2,22}=2Q_{2,t},\qquad
\det\mathsf M_2^{Q}(\tilde Q_2)=Q_{2,11}Q_{2,22}-Q_{2,12}Q_{2,21}=\langle\tilde Q_2\rangle_{\natural}.
$$

*Proof.* The trace is $2Q_{2,t}$ because the trace is a similarity invariant and $\operatorname{Tr}\tilde Q_2=2Q_{2,t}$. The determinant is the central scalar, because the matrix model is an algebra isomorphism and $\det\mathsf M_2(\tilde Q_2)=\langle\tilde Q_2\rangle_{\natural}$.

### The Trace Pairing

The trace pairing $\langle\tilde Q_2,\tilde P\rangle=\operatorname{Tr}(\tilde Q_2\tilde P)$ is non-degenerate on $\mathbb{B}$. In the eigenbasis its Gram matrix is

$$
G=
\begin{pmatrix}
1&0&0&0\\
0&0&1&0\\
0&1&0&0\\
0&0&0&1
\end{pmatrix},
$$

because $\operatorname{Tr}(\tilde\Pi_\pm)=1$, $\operatorname{Tr}(\vec\Upsilon_\pm)=0$ and $\operatorname{Tr}(\vec\Upsilon_+\vec\Upsilon_-)=\operatorname{Tr}(\tilde\Pi_-)=1$. The trace matrix of the basis is not the identity: the two idempotents have trace $1$, the two nilpotents have trace $0$, and the two mixed products have trace $1$. The matrix is its own inverse, so the dual basis of $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ is $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$: the two nilpotents are exchanged and the two idempotents are self-dual. Consequently

$$
Q_{2,11}=\operatorname{Tr}(\tilde\Pi_+\tilde Q_2),\qquad
Q_{2,12}=\operatorname{Tr}(\vec\Upsilon_+\tilde Q_2),\qquad
Q_{2,21}=\operatorname{Tr}(\vec\Upsilon_-\tilde Q_2),\qquad
Q_{2,22}=\operatorname{Tr}(\tilde\Pi_-\tilde Q_2).
$$

## Expansion of Every Biquaternion

**The eigenbasis is a basis: every biquaternion has one expansion in it. The expansion is not a spectral decomposition of the expanded element; it is its reading in the coordinates of $\tilde Q$.**

### The Expansion Theorem

**Theorem (unique expansion).** Let $\tilde Q\in\mathbb{B}$ with $B^2\neq0$. Its normalised basis

$$
\mathcal{B}(\tilde Q)=(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)
$$

is unique, and every $\tilde Q_2\in\mathbb{B}$ has the unique expansion

$$
\tilde Q_2=Q_{2,11}\tilde\Pi_++Q_{2,12}\vec\Upsilon_-+Q_{2,21}\vec\Upsilon_++Q_{2,22}\tilde\Pi_-,
\qquad Q_{2,ij}\in\mathbb{C},
$$

with the coordinates given by the trace formulas above. The element $\tilde Q$ has the coordinates $(\lambda_+,0,0,\lambda_-)$.

*Proof.* The four vectors are a basis by the theorem of the previous section, so the expansion exists and is unique. The coordinates of $\tilde Q$ are read from its diagonal left action, or from the Lagrange form.

**Corollary (the coordinate map).** The assignment $\tilde Q_2\mapsto\mathsf M_2^{Q}(\tilde Q_2)$ is an isomorphism of complex algebras from $\mathbb{B}$ onto $M_2(\mathbb{C})$. Consequently the coordinates of a product are the product of the coordinates, the coordinates of the inverse are the inverse matrix, and the spectrum of $\tilde Q_2$ is the spectrum of its coordinate matrix.

The expansion of a general $\tilde Q_2$ is not a diagonalisation of $\tilde Q_2$: it is diagonal in $\mathcal{B}(\tilde Q)$ exactly when $Q_{2,12}=Q_{2,21}=0$. The basis is the eigenbasis of $\tilde Q$, not of $\tilde Q_2$.

### The Diagonal Subalgebra

**Proposition (what the basis diagonalises).** For $\tilde Q_2\in\mathbb{B}$ the following are equivalent:

1. $\tilde Q_2$ is diagonal in $\mathcal{B}(\tilde Q)$;
2. $\tilde Q_2\in\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\tilde\Pi_-$;
3. $\tilde Q_2\in\operatorname{span}_{\mathbb{C}}\{e_t,\tilde Q\}$.

*Proof.* The diagonal elements are $Q_{2,11}\tilde\Pi_++Q_{2,22}\tilde\Pi_-$, which is the second statement. Since $\tilde\Pi_\pm=(e_t\pm\vec\Xi)/2$ and $\vec\Xi=(\tilde Q-Q_te_t)/(iB)$, this is the plane spanned by $e_t$ and $\tilde Q$.

Thus the eigenbasis of $\tilde Q$ diagonalises simultaneously the whole pencil $\{a\tilde Q+b e_t\}$, and no other elements. This is the precise sense in which the basis is attached to $\tilde Q$: it is attached to the two-dimensional commutative subalgebra generated by $\tilde Q$.

### A Worked Example

Take

$$
\tilde Q=\vec e_x+\vec e_y,\qquad B^2=2,\qquad B=\sqrt2,\qquad \lambda_\pm=\pm i\sqrt2.
$$

Then

$$
\tilde\Pi_\pm=\frac12\mp\frac{i}{2\sqrt2}(\vec e_x+\vec e_y),
$$

$$
\vec\Upsilon_+=\frac{\vec e_x-\vec e_y}{2\sqrt2}-\frac{i}{2}\vec e_z,\qquad
\vec\Upsilon_-=-\frac{\vec e_x-\vec e_y}{2\sqrt2}-\frac{i}{2}\vec e_z.
$$

The four basis vectors satisfy the multiplication table, and $\tilde Q=i\sqrt2\,\tilde\Pi_+-i\sqrt2\,\tilde\Pi_-$. The coordinates of the fixed units in this basis are

| element | $\tilde\Pi_+$ | $\vec\Upsilon_-$ | $\vec\Upsilon_+$ | $\tilde\Pi_-$ |
|---|---|---|---|---|
| $e_t$ | $1$ | $0$ | $0$ | $1$ |
| $\vec e_x$ | $i/\sqrt2$ | $-1/\sqrt2$ | $1/\sqrt2$ | $-i/\sqrt2$ |
| $\vec e_y$ | $i/\sqrt2$ | $1/\sqrt2$ | $-1/\sqrt2$ | $-i/\sqrt2$ |
| $\vec e_z$ | $0$ | $i$ | $i$ | $0$ |
| $\tilde Q$ | $i\sqrt2$ | $0$ | $0$ | $-i\sqrt2$ |

The table gives the coordinates of the fixed units. Every biquaternion is a complex linear combination of these units, so its coordinates are the same combination of the rows. For instance

$$
\vec e_x=\frac{i}{\sqrt2}\tilde\Pi_+-\frac{1}{\sqrt2}\vec\Upsilon_-+\frac{1}{\sqrt2}\vec\Upsilon_+-\frac{i}{\sqrt2}\tilde\Pi_-.
$$

### Change of Basis

For two spectral-regular elements $\tilde Q$ and $\tilde Q'$, let $D_{\tilde Q,\tilde Q'}$ be the matrix whose columns are the coordinates of the basis $\mathcal{B}(\tilde Q')$ in the basis $\mathcal{B}(\tilde Q)$. If $x$ and $x'$ are the coordinates of the same element in the two bases, then

$$
x=D_{\tilde Q,\tilde Q'}\,x'.
$$

The matrix is invertible, generally full, and satisfies the cocycle relation

$$
D_{\tilde Q,\tilde Q''}=D_{\tilde Q,\tilde Q'}\,D_{\tilde Q',\tilde Q''}.
$$

The change is not diagonal: two different elements have different idempotents and different nilpotents, so their eigenbases are related by a general change of basis. The matrix is the biquaternion analogue of the matrix $\mathsf C_Q$ of *The Spectrally Regular Sector and Eigenbasis of a Biquaternion in Matrix Element Representations*, and the cocycle is the same.

## The Frame Attached to the Direction

**The eigenbasis is a function of the complex line spanned by the vector part. This is the sharp form of the statement that the construction uses only $B^2\neq0$.**

### Dependence on the Line

**Theorem (the basis depends on the direction).** Let $\tilde Q$ be spectral regular and let $a\in\mathbb{C}^{\times}$, $b\in\mathbb{C}$. Put

$$
\tilde Q'=a\tilde Q+b e_t.
$$

Then $\tilde Q'$ is spectral regular. With the normalisation fixed, its root is the root of $\tilde Q$, its idempotents are the idempotents of $\tilde Q$, and its eigenbasis is the eigenbasis of $\tilde Q$. Its eigenvalues are

$$
\lambda_\pm'=a\lambda_\pm+b.
$$

*Proof.* The vector part of $\tilde Q'$ is $a\vec Q$, so $B'^2=a^2B^2$ and, by the scaling rule of the normalisation, $B'=aB$. Hence

$$
\vec\Xi'=-\frac{i(a\vec Q)}{aB}=\vec\Xi.
$$

The idempotents depend on $\vec\Xi$ only. The closed forms are homogeneous of degree zero in $(\vec Q,B)$, so the pair is unchanged. The eigenvalues are $Q_t'\pm iB'=(aQ_t+b)\pm iaB=a\lambda_\pm+b$.

**Corollary (the projective reading).** The eigenbasis is a function on the complement of the conic $B^2=0$ in $\mathbb{P}^2$, the projective space of the vector part. The element $\tilde Q$ projects to the point $[\vec Q]$, and the fibre of the projection is the affine line $\{a\tilde Q+b e_t\}$. On that fibre the eigenbasis is constant and the spectrum is affine. The spectral cone is the conic $B^2=0$, and it is exactly the locus where the construction stops.

This explains why the central scalar does not enter: it changes along the fibre, while the eigenbasis does not.

### Equivariance under Inner Automorphisms

**Proposition (conjugation).** Let $S$ be a unit of $\mathbb{B}$ and put $\tilde Q'=S\tilde QS^{-1}$. Then $S\tilde\Pi_\pm S^{-1}$ are the idempotents of $\tilde Q'$, and

$$
S\,\mathcal{B}(\tilde Q)\,S^{-1}
=\bigl(\tilde\Pi_+',\ \mu\vec\Upsilon_-',\ \mu^{-1}\vec\Upsilon_+',\ \tilde\Pi_-'\bigr)
$$

for some $\mu\in\mathbb{C}^{\times}$. The construction is therefore equivariant up to the reciprocal rescaling.

*Proof.* Conjugation preserves the product, the unit, the trace and the square of the vector part. It sends the root of $\tilde Q$ to the root of $\tilde Q'$, and the corners to the corners. It preserves the product normalisation, so the image of an admissible pair is admissible for $\tilde Q'$, and two admissible pairs differ by the reciprocal rescaling.

The closed-form normalisation is not exactly equivariant, because the auxiliary vector $\vec w$ is fixed in the frame and is not invariant under conjugation. The equivariance is a property of the construction up to scale, not of the particular representative.

### The Boundary

The construction is defined on $\{B^2\neq0\}$ and stops on the spectral-degenerate cone $\mathcal S=\{B^2=0\}$. On the cone the two eigenvalues coalesce, the root $\vec\Xi=-i\vec Q/B$ is undefined, and the two spectral idempotents have no limit independent of the path: a sequence of spectral-regular elements converging to a point of the cone produces idempotents whose limit depends on the path. The cone is not one case but three, and each stratum has canonical data of its own.

**The scalar stratum.** $\vec Q=0$. Then $\tilde Q=Q_te_t$ and $L_{\tilde Q}=Q_t\mathrm{id}$; every basis is an eigenbasis, and the one-term writing $\tilde Q=Q_te_t$ is canonical. No refinement is canonical: every idempotent commutes with $\tilde Q$, so every complete pair $(e,f)$ gives the trivial Peirce form

$$
e\tilde Qe=Q_te,\qquad e\tilde Qf=0,\qquad f\tilde Qe=0,\qquad f\tilde Qf=Q_tf,
$$

with both off-diagonal corners zero, and the two diagonal coefficients equal. The gauge is the whole idempotent variety, of complex dimension two. At the origin the eigenvalue is zero as well, and the one-term writing is $0=0\cdot e_t$.

**The nilpotent stratum.** $Q_t=0$, $\vec Q\neq0$, $\vec Q^2=0$. Write $\vec N=\vec Q$. The canonical data are the line $\mathbb{C}\vec N$, the plane $\ker L_{\vec N}=\operatorname{im}L_{\vec N}$, and the flag

$$
0\subset\mathbb{C}\vec N\subset\ker L_{\vec N}\subset\mathbb{B}.
$$

Every idempotent $e$ with $e\vec N=\vec N$ and $\vec Ne=0$ gives the Peirce form

$$
e\tilde Qe=0,\qquad e\tilde Qf=\vec N,\qquad f\tilde Qe=0,\qquad f\tilde Qf=0,\qquad f=e_t-e.
$$

This is a Peirce form, not a spectral decomposition: the two diagonal coefficients are equal, and the whole defect sits in the off-diagonal corner. Those idempotents are exactly the affine line

$$
e_b=e+b\vec N,\qquad b\in\mathbb{C},
$$

and the product identity $e_b\vec Nf_b=\vec N$ holds, with $f_b=e_t-e_b$. Equivalently, $e_b$ is the unique non-zero idempotent on the complement line $\mathbb{C}e_b$ to $\mathbb{C}\vec N$ in $\ker L_{\vec N}$; the parameter $b$ is the choice of that complement. The opposite corner $f_b\mathbb{B}e_b$ is a line that moves with $b$, so the Peirce quadruple is not a function of the element **for the plain product**. A canonical choice of complement on the cone, hence of one quadruple, is made in *The Jordan Normal Form*, §*The Jordan Basis*. The element has no eigenbasis, because its eigenspace is $\ker L_{\vec N}$, of complex dimension two.

**The unipotent stratum.** $Q_t\neq0$, $\vec Q\neq0$. Put $\vec\Upsilon=\vec Q/Q_t$. Then $\vec\Upsilon^2=0$ and

$$
\tilde Q=Q_tu,\qquad u=e_t+\vec\Upsilon,\qquad (u-e_t)^2=0.
$$

The element $u$ is unipotent, and $u^n=e_t+n\vec\Upsilon$ for every integer $n$; in particular $u^{-1}=e_t-\vec\Upsilon$ and $\tilde Q^{-1}=Q_t^{-1}(e_t-\vec\Upsilon)$. The canonical data are those of the nilpotent stratum applied to $\vec Q$: the line, the flag, the same affine family of Peirce idempotents. The Peirce form of $\tilde Q$ relative to $e_b$ is $\operatorname{diag}(Q_t,Q_t)$ with off-diagonal $\vec Q$, and it does not depend on $b$. The scalar part is central and adds nothing to the Peirce corners but the eigenvalue $Q_t$. There is no eigenbasis, for the same reason: the eigenspace is $\ker L_{\vec Q}$, of complex dimension two.

**The two actions.** The right action does not supply a basis, on either defective stratum. The operators $L_{\vec Q}$ and $R_{\vec Q}$ commute, both have rank two, both have the single eigenvalue zero, and their common eigenspace is the line

$$
\ker L_{\vec Q}\cap\ker R_{\vec Q}=\mathbb{C}\vec Q.
$$

A simultaneous eigenbasis would need four independent common eigenvectors, and there is one. In the Peirce basis $(e,\vec Q,\vec X,f)$, where $\vec X$ spans $f\mathbb{B}e$, the two nilpotent parts are

$$
L_{\vec Q}:\ e\mapsto0,\quad \vec Q\mapsto0,\quad \vec X\mapsto c\,e,\quad f\mapsto\vec Q,
$$

$$
R_{\vec Q}:\ e\mapsto\vec Q,\quad \vec Q\mapsto0,\quad \vec X\mapsto c\,f,\quad f\mapsto0,
$$

with $c\neq0$ depending on the scale of $\vec X$. The left chains are $(\vec X,e)$ and $(f,\vec Q)$; the right chains are $(e,\vec Q)$ and $(\vec X,f)$. The two pairings of the four vectors differ. If a basis put both operators in Jordan form, both would equal $J_2(0)\oplus J_2(0)$ in that basis, hence $L_{\vec Q}=R_{\vec Q}$; but $L_{\vec Q}(e)=0$ and $R_{\vec Q}(e)=\vec Q\neq0$. The right action supplies a second flag,

$$
0\subset\mathbb{C}\vec Q\subset\ker R_{\vec Q}\subset\mathbb{B},
$$

not a second basis. Choosing the complement to $\mathbb{C}\vec Q$ in $\ker L_{\vec Q}$ fixes $e$, and then $f=e_t-e$ fixes the complement in $\ker R_{\vec Q}$; the affine family $e_b=e+b\vec Q$ is the freedom of that single choice. The scale of $\vec X$ is a second freedom. The eigenbasis of the regular case is replaced, on the defective strata, by a Jordan basis; a canonical choice of the complement removes both freedoms and selects one quadruple, constructed in *The Jordan Normal Form*.

## Spinors and Chirality

**The eigenbasis exhibits the two spinor spaces as the two columns of its matrix model. Each column is a minimal left ideal, each is a complex plane, and each carries both eigenvalues under left multiplication. Chirality is the right index, not the left one.**

The general statement is in *The Peirce Decomposition*, §*Spinors and the Two Couples*: the four Peirce vectors split into the couples $\mathcal{C}_+=(\tilde\Pi_+,\vec\Upsilon_+)$ and $\mathcal{C}_-=(\vec\Upsilon_-,\tilde\Pi_-)$, and left multiplication acts on each couple by the same Peirce matrix. Here that matrix is $\operatorname{diag}(\lambda_+,\lambda_-)$, so each couple is a pair of eigenvectors.

### The Two Spinor Spaces

**Definition (spinor space).** A **spinor space** of $\mathbb{B}$ is a minimal non-zero left ideal. The two spinor spaces attached to $\tilde Q$ are

$$
S_+=\mathbb{B}\tilde\Pi_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+,
\qquad
S_-=\mathbb{B}\tilde\Pi_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi_-.
$$

A **spinor of first chirality** is an element of $S_+$; a **spinor of second chirality** is an element of $S_-$. Each spinor space has complex dimension two, and

$$
\mathbb{B}=S_+\oplus S_-.
$$

The two spaces are the two columns of the matrix model: $S_+$ is the first column and $S_-$ the second. They are isomorphic as left $\mathbb{B}$-modules, by right multiplication by $\vec\Upsilon_-$ with inverse right multiplication by $\vec\Upsilon_+$:

$$
S_+\longrightarrow S_-,\quad \xi_+\longmapsto \xi_+\vec\Upsilon_-,
\qquad
S_-\longrightarrow S_+,\quad \xi_-\longmapsto \xi_-\vec\Upsilon_+.
$$

The two maps are inverse because $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$ and $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$. They are distinct subspaces of $\mathbb{B}$ nevertheless. Chirality is therefore not an invariant of the left module; it is a property of the embedding of the module in the algebra.

### The Left Action on a Spinor

A spinor of first chirality is

$$
\xi_+=Q_{2,11}\tilde\Pi_++Q_{2,21}\vec\Upsilon_+,
$$

with coordinates $(Q_{2,11},Q_{2,21})$, the first column. Under left multiplication by $\tilde Q$,

$$
\tilde Q\xi_+=\lambda_+Q_{2,11}\tilde\Pi_++\lambda_-Q_{2,21}\vec\Upsilon_+,
$$

so the coordinate pair is sent to $(\lambda_+Q_{2,11},\lambda_-Q_{2,21})$. In the basis $(\tilde\Pi_+,\vec\Upsilon_+)$ of $S_+$, the left action is

$$
L_{\tilde Q}|_{S_+}=\operatorname{diag}(\lambda_+,\lambda_-).
$$

A spinor of second chirality is

$$
\xi_-=Q_{2,12}\vec\Upsilon_-+Q_{2,22}\tilde\Pi_-,
$$

with coordinates $(Q_{2,12},Q_{2,22})$, the second column. In the basis $(\vec\Upsilon_-,\tilde\Pi_-)$ of $S_-$,

$$
\tilde Q\xi_-=\lambda_+Q_{2,12}\vec\Upsilon_-+\lambda_-Q_{2,22}\tilde\Pi_-,
\qquad
L_{\tilde Q}|_{S_-}=\operatorname{diag}(\lambda_+,\lambda_-).
$$

The same diagonal matrix acts on the two chiralities. Each chirality therefore contains both eigenvalues, and the spectrum is chirality-blind: knowing the chirality of a spinor tells nothing about which eigenvalue a component carries.

### The Right Action and the Definition of Chirality

Right multiplication by $\tilde Q$ is scalar on each spinor space:

$$
\xi_+\tilde Q=\lambda_+\xi_+\quad(\xi_+\in S_+),\qquad
\xi_-\tilde Q=\lambda_-\xi_-\quad(\xi_-\in S_-).
$$

Thus $S_+$ is the $\lambda_+$-eigenspace of $R_{\tilde Q}$ and $S_-$ the $\lambda_-$-eigenspace. Chirality is the eigenvalue of the right multiplication, in the same way that the spectral label is the eigenvalue of the left multiplication. The two statements are different: the left action carries both eigenvalues on each chirality, and the right action carries one eigenvalue on each. In particular, chirality is the eigenvalue of the involution $R_{\vec\Xi}$: it is $+1$ on $S_+$ and $-1$ on $S_-$.

**Proposition (the two gradings).** The following two decompositions coexist:

- the left spectral decomposition $\mathbb{B}=\tilde\Pi_+\mathbb{B}\oplus\tilde\Pi_-\mathbb{B}$, the eigenspaces of $L_{\tilde Q}$;
- the right chiral decomposition $\mathbb{B}=S_+\oplus S_-$, the eigenspaces of $R_{\tilde Q}$.

The four corners are the intersections:

$$
\mathbb{B}_{st}=\tilde\Pi_s\mathbb{B}\cap S_t.
$$

The four basis vectors are the four cells of the grid, with rows the left spectral index $s$ and columns the chiral index $t$:

|  | $t=+$ | $t=-$ |
|---|---|---|
| $s=+$ | $\tilde\Pi_+$ | $\vec\Upsilon_-$ |
| $s=-$ | $\vec\Upsilon_+$ | $\tilde\Pi_-$ |

The rows are the right ideals $\tilde\Pi_s\mathbb{B}$, the eigenspaces of $L_{\tilde Q}$; the columns are the left ideals $S_t$, the eigenspaces of $R_{\tilde Q}$. The two idempotents act on the two sides: left multiplication by $\tilde\Pi_s$ is the projection onto the row labelled $s$, and right multiplication by $\tilde\Pi_t$ is the projection onto the column labelled $t$.

### A General Element Is a Pair of Spinors

Every $\tilde Q_2\in\mathbb{B}$ splits as

$$
\tilde Q_2=\tilde Q_2\tilde\Pi_++\tilde Q_2\tilde\Pi_-,
$$

a spinor of first chirality plus a spinor of second chirality. In the matrix model the two summands are the two columns:

$$
\tilde Q_2\longmapsto
\begin{pmatrix}
Q_{2,11}&Q_{2,12}\\
Q_{2,21}&Q_{2,22}
\end{pmatrix},
\qquad
\tilde Q_2\tilde\Pi_+\longmapsto
\begin{pmatrix}
Q_{2,11}&0\\
Q_{2,21}&0
\end{pmatrix},
\qquad
\tilde Q_2\tilde\Pi_-\longmapsto
\begin{pmatrix}
0&Q_{2,12}\\
0&Q_{2,22}
\end{pmatrix}.
$$

A general element is therefore not a spinor: it has one spinor component of each chirality. Left multiplication by any $\tilde P\in\mathbb{B}$ acts on both columns by the same matrix $\mathsf M_2^{Q}(\tilde P)$,

$$
\tilde P\,\tilde Q_2\longmapsto
\mathsf M_2^{Q}(\tilde P)\,\mathsf M_2^{Q}(\tilde Q_2),
$$

so it preserves each chirality. The off-diagonal entries of $\mathsf M_2^{Q}(\tilde P)$ mix the two components inside one column, that is, the two spectral components inside one chirality; they do not mix the two columns.

**Remark (what mixes chirality).** A left multiplication by an element never changes chirality, because $S_\pm$ are left ideals. An operation that changes chirality has to act on the right, or be a two-sided operation. In the matrix picture, right multiplication multiplies the matrix on the right and mixes the two columns. This is the algebraic distinction behind the two kinds of operation: the left action is the action of the algebra on its left modules, and it is chirality-diagonal; a chirality-changing term is not a left multiplication.

### The Adjoint

The Hermitian adjoint sends a left ideal to a right ideal:

$$
S_+^*=(\mathbb{B}\tilde\Pi_+)^*=\tilde\Pi_+^*\mathbb{B}.
$$

It therefore does not act inside the chiral decomposition: the two chiralities are left ideals, and their images are right ideals. A minimal left ideal of $M_2(\mathbb{C})$ is not a right ideal, so the image is not one of the two chiralities. Chirality belongs to the left-ideal decomposition, not to the matrix adjoint. The spinor adjoints and the reality conditions are treated in *Spinors as Minimal Left Ideals with Inner Conjugation* and in the companion articles on the signed adjoints.

### Physical Interpretation

In the language of physics, the pair of columns is the algebraic image of a Dirac spinor: one spinor of each chirality. The two eigenvalues $\lambda_\pm$ play the role of the two mass or energy labels. A spinor of definite chirality has both labels: it is a two-component object whose components are its $\lambda_+$ and $\lambda_-$ parts. A gauge transformation is a left multiplication by a unit, so it preserves chirality; a mass term couples the two chiralities and is therefore not a left multiplication by an element. The general element of $\mathbb{B}$, which has off-diagonal entries, is a pair of spinors, one of each chirality, and its off-diagonal entries mix the two spectral components inside each chirality rather than the two chiralities.

## Summary

**With $B^2\neq0$, the normalised basis $\mathcal{B}(\tilde Q)=(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ is unique, and every $\tilde Q_2\in\mathbb{B}$ has the unique expansion $\tilde Q_2=Q_{2,11}\tilde\Pi_++Q_{2,12}\vec\Upsilon_-+Q_{2,21}\vec\Upsilon_++Q_{2,22}\tilde\Pi_-$. The two spinor spaces are its two columns.**

| question | answer |
|---|---|
| hypothesis | $B^2\neq0$; the central scalar is irrelevant |
| domain | $B^2\neq0$, the complement of the spectral cone |
| root | $\vec\Xi=-i\vec Q/B$, $\vec\Xi^2=e_t$, $\tilde Q=Q_te_t+iB\vec\Xi$ |
| idempotents | $\tilde\Pi_\pm=(e_t\pm\vec\Xi)/2$, unique |
| nilpotents | $\vec\Upsilon_+\in\mathbb{B}_{-+}$, $\vec\Upsilon_-\in\mathbb{B}_{+-}$, $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$ |
| scale | determined up to $(\mu,\mu^{-1})$; fixed by the normalisation |
| basis | $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$; the normalised Peirce basis, unique with the normalisation fixed |
| left action | $\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$ |
| right action | $\operatorname{diag}(\lambda_+,\lambda_-,\lambda_+,\lambda_-)$ |
| expansion | $\tilde Q_2=Q_{2,11}\tilde\Pi_++Q_{2,12}\vec\Upsilon_-+Q_{2,21}\vec\Upsilon_++Q_{2,22}\tilde\Pi_-$, unique |
| coordinates | algebra isomorphism onto $M_2(\mathbb{C})$, $\det=N$, $\operatorname{tr}=2Q_{2,t}$ |
| diagonal subalgebra | $\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\tilde\Pi_-=\operatorname{span}\{e_t,\tilde Q\}$ |
| dependence | on $[\vec Q]\in\mathbb{P}^2$ only; the spectrum is affine on the fibre |
| spinors | $S_\pm=\mathbb{B}\tilde\Pi_\pm$, minimal left ideals, complex dimension two |
| left action on spinors | $\operatorname{diag}(\lambda_+,\lambda_-)$ on each chirality |
| chirality | the right index, the eigenvalue of $R_{\tilde Q}$; independent of the left spectrum |
| boundary | $\mathcal S$ has three strata: the scalar one with no attached basis, the nilpotent and unipotent ones with a flag and a two-parameter gauge, and no eigenbasis |

The construction fails exactly on the spectral-degenerate cone, and the failure has three forms. On the scalar stratum and at the origin every basis is an eigenbasis and none is attached to the element; the one-term decomposition is canonical, and the gauge is the idempotent variety. On the nilpotent and unipotent strata there is no eigenbasis: the canonical data are the line, the flag, and the affine family $e_b=e+b\vec Q$ of Peirce idempotents, and the two-sided action does not repair the defect. The spectral condition is thus the exact domain of the construction, and the central scalar is not part of it.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $\tilde Q=Q_te_t+\vec Q$ | an element and its scalar–vector split |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the square of the vector part, the spectral discriminant |
| $B$ | a fixed square root of $B^2$ |
| $\vec\Xi=-i\vec Q/B$ | the root, a pure square root of $e_t$ |
| $\lambda_\pm=Q_t\pm iB$ | the two eigenvalues |
| $\tilde\Pi_\pm=(e_t\pm\vec\Xi)/2$ | the spectral idempotents |
| $\mathbb{B}_{st}=\tilde\Pi_s\mathbb{B}\tilde\Pi_t$ | the Peirce corners |
| $\vec\Upsilon_\pm$ | the normalised nilpotents, $\vec\Upsilon_+\in\mathbb{B}_{-+}$, $\vec\Upsilon_-\in\mathbb{B}_{+-}$ |
| $\mathcal S=\{B^2=0\}$ | the spectral-degenerate cone, the boundary of the construction |
| $\vec N=\vec Q$ on the nilpotent stratum | the nilpotent part |
| $e_b=e+b\vec Q$ | the affine family of Peirce idempotents on the cone |
| $\vec X$ | a generator of the corner $f\mathbb{B}e$ |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the spinor spaces, the two chiralities |
| $L_{\tilde Q_2}$, $R_{\tilde Q_2}$ | left and right multiplication by the general element |
| $\mathsf M_2^{Q}$ | the matrix model attached to the eigenbasis |
| $\operatorname{Tr}\tilde Q_2=2Q_{2,t}$ | the trace |
| $\langle\tilde Q_2\rangle_{\natural}=\operatorname{Sc}(\tilde Q_2^{\natural}\tilde Q_2)$ | the scalar of $\tilde Q_2^{\natural}\tilde Q_2$ |

## Further Reading

- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the spectral criterion, the two eigenvalues, the cone and the existence of the eigenbasis.
- [The N-Regular, Spectrally Regular Sector](the-n-regular-spectrally-regular-sector.html), for the sector $\Sigma_{11}$, the Peirce corners and the spinor spaces.
- [The N-Degenerate, Spectrally Regular Sector](the-n-degenerate-spectrally-regular-sector.html), for the sector $\Sigma_{01}$, the scaled idempotents and the same eigenbasis with a zero eigenvalue.
- [The N-Regular, Spectrally Degenerate Sector](the-n-regular-spectrally-degenerate-sector.html), for the scalar line and the Jordan part, where the construction stops.
- [The N-Degenerate, Spectrally Degenerate Sector](the-n-degenerate-spectrally-degenerate-sector.html), for the nilpotents and the origin.
- [The Spectrally Degenerate Sector and Construction of the Jordan Basis of a Biquaternion](the-spectrally-degenerate-sector-and-construction-of-the-jordan-basis-of-a-biquaternion.html), for the sector as a whole: the equation, the three strata, the geometry and the Jordan basis.
- [The Spectrally Regular Sector and Eigenbasis of a Biquaternion in Matrix Element Representations](m4c-representation-the-eigenbasis-and-the-diagonalising-matrix.html), for the fixed model $\mathsf M_2$, the diagonalising matrix $\mathsf C_Q$ and the 4×4 regular matrices.
- [Worked Examples of Eigenbasis of a Biquaternion](worked-examples-of-eigenbasis-of-a-biquaternion.html), for computed eigenbases of the standard elements.
- [Ideals, Peirce Decompositions and Spinors in the Biquaternion Algebra](ideals-peirce-decompositions-and-spinors-in-the-biquaternion-algebra.html), for the general Peirce construction, the two spinor spaces and the eigenbasis as a particular Peirce matrix.
- [Spinors as Minimal Left Ideals with Inner Conjugation](spinors-as-minimal-left-ideals-with-inner-conjugation.html), for the identification of the minimal left ideals with the spinor spaces and the chiral halves.
- [Relations between Quaternionic Norm and Spectral Regularity and Degeneracy](relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html), for the four sectors and the comparison of the two cones.
- [Relations between the Biquaternion Exponential and the Fourier Kernel](relations-between-the-biquaternion-exponential-and-the-fourier-kernel.html), for the eigenbasis read in a root-adapted Fourier basis and the transverse cuts of the two decompositions.
- [The Biquaternion Eigenvalue Decomposition](the-biquaternion-eigenvalue-decomposition.html), for the spectral decomposition in the wider theory.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (2nd edition, Cambridge University Press, 2013), for the spectral projectors, the trace pairing and the matrix models.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the identification of the biquaternion algebra with $M_2(\mathbb{C})$ and the spinor modules.
- Élie Cartan, *The Theory of Spinors* (Dover, 1981), for the classical theory of the two chiralities.
