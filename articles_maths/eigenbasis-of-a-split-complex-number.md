# __Eigenbasis of a Split-Complex Number__

## Introduction

The split-complex algebra $\mathbb{D}=\mathbb{R}[x]/(x^2-1)=\mathbb{R}[j]$, $j^2=+1$, is commutative, associative and two-dimensional over $\mathbb{R}$. The idempotent decomposition $\mathbb{D}=\mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_-$ makes it isomorphic to $\mathbb{R}\oplus\mathbb{R}$. This article reads the **eigenvalue decomposition** of a split-complex number $Q=q+jq'$ in the distinct case $q'\neq0$: the writing

$$
Q=\lambda_+\Pi_+ + \lambda_-\Pi_-,
\qquad
\lambda_+=q+q'=Q_+,
\quad
\lambda_-=q-q'=Q_-,
$$

Here the coefficients $\lambda_\pm$ are the eigenvalues and the idempotents $\Pi_\pm$ are the eigenprojections. The eigenvalues are therefore the idempotent coordinates, and their values are displayed with them throughout. The article is the two-dimensional commutative counterpart of *Eigenbasis of a Biquaternion* and the real analogue of *Eigenbasis of a Reduced Biquaternion*. The general definition, the existence theorem and the uniqueness theorem are those of *The Eigenvalue Decomposition of an Element*. The split-complex content is that, in the distinct case, the eigenprojections are the standard idempotents $\Pi_\pm$, that these idempotents are central, and that the Peirce decomposition relative to either of them is the decomposition of the whole algebra. There is no vector part, the generator $j$ is part of the presentation rather than a root extracted from the element, and there is no continuous family of idempotents: the algebra has exactly four idempotents, and the nontrivial pair is unique.

**The results.** The spectrum of $Q=q+jq'$ is $\{q+q',q-q'\}$, and in the distinct case $q'\neq0$ the two eigenprojections are the standard idempotents $\Pi_\pm=\tfrac12(1\pm j)$. They are central and independent of $Q$, the eigenvalue decomposition is the direct-product decomposition $\mathbb{D}=\mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_-$ read on the element, and the Peirce decomposition relative to $\Pi_+$ has two vanishing off-diagonal corners. The polynomial calculus is the componentwise calculus on $\mathbb{R}\times\mathbb{R}$, and the unit group is $\mathbb{R}^\times\times\mathbb{R}^\times$. The idempotents form an eigenbasis of the multiplication operator, with eigenvalues $\lambda_+$ and $\lambda_-$. The scalar regime has a repeated eigenvalue, the zero-divisor regime keeps a two-term decomposition with one zero eigenvalue, and there is no nilpotent regime. The two minimal ideals $S_\pm=\mathbb{R}\Pi_\pm$ are the spinor spaces: a spinor is a single real coefficient on one of them, and after complexification a single complex coefficient.

| Question | Answer |
|---|---|
| Algebra | $\mathbb{D}=\mathbb{R}[x]/(x^2-1)\cong\mathbb{R}\times\mathbb{R}$ |
| Element | $Q=q+jq'$ |
| Spectrum | $\sigma(Q)=\{\lambda_+,\lambda_-\}=\{q+q',q-q'\}$ |
| Distinctness | $\lambda_+\neq\lambda_-\iff q'\neq0$ |
| Eigenprojections | $\Pi_\pm=\tfrac12(1\pm j)$, independent of $Q$ |
| Eigenprojections central? | yes |
| Eigenvalue decomposition | $Q=\lambda_+\Pi_++\lambda_-\Pi_-$ |
| Peirce decomposition | $\mathbb{D}=\mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_-$, with zero off-diagonal corners |
| Eigenbasis | $(\Pi_+,\Pi_-)$, with eigenvalues $\lambda_+,\lambda_-$ |
| Spinor spaces | $S_\pm=\mathbb{R}\Pi_\pm$, two real lines; one real spinor coordinate per chirality |
| Unit group | $\mathbb{D}^\times\cong\mathbb{R}^\times\times\mathbb{R}^\times$ |

**Conventions.** The notation is fixed in *Conventions in Mathematics*: the algebra is $\mathbb{D}=\mathbb{R}[x]/(x^2-1)$, with basis $1,j$, $j^2=+1$, general element $Q=q+jq'$ with $q=\operatorname{Re}Q$ and $q'=\operatorname{Im}Q$, conjugate $\bar Q=q-jq'$, idempotents $\Pi_\pm=\tfrac12(1\pm j)$ and idempotent coordinates $Q_\pm=q\pm q'$, so that $Q=Q_+\Pi_+ + Q_-\Pi_-$. The norm is $\langle Q\rangle_{*}=Q\bar Q=q^2-q'^2$. The eigenvalues are written $\lambda_\pm=Q_\pm=q\pm q'$; a test scalar in the definition of an eigenvalue is written $\mu$, so the letter $\lambda$ is reserved for the two eigenvalues. The two spinor spaces are $S_\pm=\mathbb{R}\Pi_\pm$, with real spinor coordinates $a_1,a_2$, the two diagonal entries of the matrix in the eigenbasis; after complexification the coefficients are complex. The base is $\mathbb{R}$, as throughout the category.

**Boundaries.** The complex case is the subject of *Eigenvalues and Diagonalisation*; the reduced biquaternion case is *Eigenbasis of a Reduced Biquaternion*; the biquaternion case is *Eigenbasis of a Biquaternion*; the Peirce and ideal theory is *Ideals and Peirce Decomposition of the Split-Complex Algebra*; the exponential and the logarithm built on the decomposition are those of *Split-Complex Exponential and Lie Group Structure*; and the polar forms are those of *Modulus–Unit Polar Decomposition of Split-Complex Numbers* and *Exponential Polar Decomposition of Split-Complex Numbers*. The general definition, existence and uniqueness of the eigenvalue decomposition are those of *The Eigenvalue Decomposition of an Element* and are not restated.

## The Spectrum and the Characteristic Polynomial

**Definition.** Let $Q\in\mathbb{D}$. A real number $\mu$ is an **eigenvalue** of $Q$ if $Q-\mu$ is not invertible in $\mathbb{D}$; the set of eigenvalues is the **spectrum** $\sigma(Q)$. This is the definition of *The Eigenvalue Decomposition of an Element*, §*The Eigenvalues of an Element*.

**Notation.** The two eigenvalues are written $\lambda_\pm=q\pm q'$ when their values are exhibited, and $Q_\pm$ when they are read as idempotent coordinates. The test scalar of the definition is $\mu$, so the letter $\lambda$ is reserved for the two eigenvalues.

**Theorem.** The spectrum of $Q=q+jq'$ is

$$
\boxed{\;\sigma(Q)=\{\lambda_+,\lambda_-\},
\qquad
\lambda_+=q+q'=Q_+,
\qquad
\lambda_-=q-q'=Q_-\;}.
$$

Thus the two eigenvalues are the two idempotent coordinates, and their sum and product are

$$
\lambda_++\lambda_-=2q,
\qquad
\lambda_+\lambda_-=q^2-q'^2=\langle Q\rangle_{*}.
$$

**Proof.** The element $Q-\mu=(q-\mu)+jq'$ has norm $(q-\mu)^2-q'^2$. By the criterion of *Norm and Invertibility in the General Split-Complex Algebra*, §*The Criterion*, it is invertible exactly when its norm is nonzero. Hence $Q-\mu$ is not invertible exactly when $(q-\mu)^2=q'^2$, that is, when $\mu=q+q'$ or $\mu=q-q'$. These two numbers are $\lambda_+$ and $\lambda_-$.

**Characteristic polynomial.** The characteristic polynomial of $Q$ is

$$
\boxed{\;p_Q(X)=X^2-2qX+\langle Q\rangle_{*}
=(X-\lambda_+)(X-\lambda_-),
\qquad
\lambda_\pm=q\pm q'\;}.
$$

It is the characteristic polynomial of the multiplication operator, whose trace is $\lambda_++\lambda_-=2q$ and whose determinant is $\lambda_+\lambda_-=\langle Q\rangle_{*}$. Its discriminant is

$$
(\lambda_+-\lambda_-)^2=(2q')^2=4q'^2,
$$

so the eigenvalues are distinct exactly when $q'\neq0$, that is, exactly when $\lambda_+\neq\lambda_-$.

**Minimal polynomial.** The minimal polynomial is $p_Q$ when $q'\neq0$, and $X-q$ when $q'=0$, in which case $\lambda_+=\lambda_-=q$. Since $q,q'\in\mathbb{R}$, the spectrum is always real and the characteristic polynomial splits over $\mathbb{R}$.

The data of the spectrum are collected in the table.

| Quantity | Value |
|---|---|
| Spectrum | $\sigma(Q)=\{\lambda_+,\lambda_-\}$ |
| Eigenvalues | $\lambda_+=q+q'$, $\lambda_-=q-q'$ |
| Sum | $\lambda_++\lambda_-=2q$ |
| Product | $\lambda_+\lambda_-=q^2-q'^2=\langle Q\rangle_{*}$ |
| Discriminant | $(\lambda_+-\lambda_-)^2=4q'^2$ |
| Characteristic polynomial | $p_Q(X)=X^2-2qX+\langle Q\rangle_{*}=(X-\lambda_+)(X-\lambda_-)$ |
| Minimal polynomial | $(X-\lambda_+)(X-\lambda_-)$ if $q'\neq0$; $X-q$ if $q'=0$ |

## The Eigenprojections

**The eigenprojections of a non-scalar split-complex number are the two standard idempotents $\Pi_\pm$.**

Put

$$
\Pi_+=\frac{1+j}{2},\qquad \Pi_-=\frac{1-j}{2}.
$$

By *Square Roots of One and the Idempotents of the Split-Complex Algebra*, §*The Standard Idempotents*, they satisfy

$$
\Pi_+^2=\Pi_+,\qquad \Pi_-^2=\Pi_-,\qquad \Pi_+\Pi_-=\Pi_-\Pi_+=0,\qquad \Pi_++\Pi_-=1.
$$

They are therefore **complementary orthogonal idempotents**. In $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$ each is a minimal idempotent, and the pair $(\Pi_+,\Pi_-)$ is a **resolution of the identity** into minimal idempotents. Since $\mathbb{D}$ is commutative, $\Pi_\pm$ are **central**. By the classification of *Square Roots of One and the Idempotents of the Split-Complex Algebra*, §*The Classification of the Idempotents*, the algebra has exactly four idempotents, $0,1,\Pi_+,\Pi_-$, so $\{\Pi_+,\Pi_-\}$ is the only nontrivial complementary pair.

For $q'\neq0$, they are the **eigenprojections** of $Q$, with eigenvalues $\lambda_+=q+q'$ and $\lambda_-=q-q'$:

$$
\boxed{\;Q\Pi_+=\lambda_+\Pi_+=(q+q')\Pi_+,
\qquad
Q\Pi_-=\lambda_-\Pi_-=(q-q')\Pi_-\;}.
$$

Indeed,

$$
(q+jq')\frac{1+j}{2}
=
\frac{q+qj+q'j+q'}{2}
=
\frac{(q+q')(1+j)}{2}
=\lambda_+\Pi_+,
$$

and the computation with $1-j$ and $q-q'$ gives the second relation.

Equivalently, by the Lagrange–Sylvester interpolation formula of *The Lagrange–Sylvester Eigenprojector Formula*, §*The Eigenprojector Formula*,

$$
\Pi_+=\frac{Q-\lambda_-}{\lambda_+-\lambda_-}
=\frac{Q-(q-q')}{2q'},
\qquad
\Pi_-=\frac{Q-\lambda_+}{\lambda_--\lambda_+}
=\frac{Q-(q+q')}{-2q'},
$$

with $\lambda_+-\lambda_-=2q'$. Hence $\Pi_\pm$ are polynomials in $Q$ when $q'\neq0$, and in particular commute with $Q$. When $q'=0$ the denominator vanishes and the formula does not apply: the eigenprojection of the single eigenvalue $\lambda_+=\lambda_-=q$ is then $1$, not $\Pi_\pm$.

**Independence of the element.** The eigenprojections are the fixed pair $\Pi_\pm$: they do not depend on $Q$. This is the commutative counterpart of the biquaternion case, where the eigenprojections are the idempotents of the pure root $\vec\Xi=-i\vec Q/\sqrt{Q_x^2+Q_y^2+Q_z^2}$ and therefore vary with $\tilde Q$ (*Eigenbasis of a Biquaternion*, §*The Eigenprojections*). Here the dependence on the element lies in the eigenvalues alone.

The pair is collected in the table.

| Idempotent | Definition | Eigenvalue | Properties |
|---|---|---|---|
| $\Pi_+$ | $\tfrac12(1+j)$ | $\lambda_+=q+q'$ | $\Pi_+^2=\Pi_+$, central, primitive |
| $\Pi_-$ | $\tfrac12(1-j)$ | $\lambda_-=q-q'$ | $\Pi_-^2=\Pi_-$, central, primitive |

The two idempotents are complementary and orthogonal, $\Pi_++\Pi_-=1$ and $\Pi_+\Pi_-=0$.

## The Eigenvalue Decomposition

**Every split-complex number with distinct eigenvalues is the real linear combination of the two standard idempotents with its eigenvalues as coefficients.**

For $q'\neq0$, summing the two eigenvalue relations gives

$$
\boxed{\;Q=\lambda_+\Pi_+ + \lambda_-\Pi_-
=(q+q')\Pi_+ + (q-q')\Pi_-\;}.
$$

Equivalently, separating the $1$ and $j$ parts,

$$
Q
=
\frac{\lambda_++\lambda_-}{2}
+
\frac{\lambda_+-\lambda_-}{2}j
=
q+jq'.
$$

In the distinct case the decomposition writes $Q$ as a real linear combination of two primitive idempotents, with its eigenvalues $\lambda_\pm=q\pm q'$ as coefficients.

This is an eigenvalue decomposition in the sense of *The Eigenvalue Decomposition of an Element*, §*The Eigenvalue Decomposition*: the coefficients $\lambda_\pm$ are distinct when $q'\neq0$, the idempotents $\Pi_\pm$ are nonzero, orthogonal and complete, and they are the eigenprojections.

The scalar case $q'=0$, where $\lambda_+=\lambda_-=q$, is deferred to §*The Scalar Regime*.

**Example.** For $Q=2+3j$ the eigenvalues are
$$
\lambda_+=2+3=5,\qquad \lambda_-=2-3=-1,
$$
and the decomposition is
$$
Q=5\Pi_+-\Pi_-.
$$
The scalar-vector form confirms it: $\frac{5+(-1)}{2}+\frac{5-(-1)}{2}j=2+3j$.

The data of the decomposition are collected in the table.

| Item | Value |
|---|---|
| Element | $Q=q+jq'$ |
| Eigenvalues | $\lambda_+=q+q'$, $\lambda_-=q-q'$ |
| Eigenprojections | $\Pi_\pm=\tfrac12(1\pm j)$ |
| Decomposition | $Q=\lambda_+\Pi_++\lambda_-\Pi_-$ |
| Distinctness | $\lambda_+\neq\lambda_-\iff q'\neq0$ |
| Coordinates | $(\lambda_+,\lambda_-)$ in the basis $(\Pi_+,\Pi_-)$ |

**Uniqueness.** In the distinct case, the unordered pair $\{\lambda_+,\lambda_-\}=\{q+q',q-q'\}$ is determined by $Q$: it is the spectrum, the set of roots of $p_Q$. The ordered pair $(\lambda_+,\lambda_-)=(q+q',q-q')$ is determined once the two idempotents are labelled. The algebra alone, without the choice of the generator $j$, does not distinguish the labels, because the automorphism $j\mapsto-j$ exchanges $\Pi_+$ and $\Pi_-$ and with them $\lambda_+$ and $\lambda_-$. Relative to the convention, which fixes $j$, the ordered pair is the coordinate pair in the basis $(\Pi_+,\Pi_-)$. No other pair of eigenprojections exists, since $\{\Pi_+,\Pi_-\}$ is the only nontrivial complementary pair.

**Semisimplicity.** For $q'\neq0$, the minimal polynomial $p_Q=(X-\lambda_+)(X-\lambda_-)$ is squarefree, so $Q$ is semisimple. The eigenvalue decomposition is the diagonalisation of $Q$ with respect to the central idempotents $\Pi_\pm$.

## The Peirce Decomposition Relative to the Eigenprojection

**The Peirce decomposition relative to $\Pi_+$ is the direct product $\mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_-$, with vanishing mixed corners.**

Let $e=\Pi_+$, so that $1-e=\Pi_-$. The **Peirce decomposition** of the algebra $\mathbb{D}$ relative to $e$ is

$$
\mathbb{D}
=
e\mathbb{D}e\oplus e\mathbb{D}(1-e)\oplus(1-e)\mathbb{D}e\oplus(1-e)\mathbb{D}(1-e).
$$

Write $\mathbb{D}_{\sigma\tau}=\Pi_\sigma\mathbb{D}\Pi_\tau$ for $\sigma,\tau\in\{+,-\}$, in the notation of *Ideals and Peirce Decomposition of the Split-Complex Algebra*, §*The Peirce Decomposition*. Because $\mathbb{D}$ is commutative and $\Pi_+\Pi_-=0$, the off-diagonal Peirce components vanish:

$$
\mathbb{D}_{+-}=\Pi_+\mathbb{D}\Pi_-=0,
\qquad
\mathbb{D}_{-+}=\Pi_-\mathbb{D}\Pi_+=0.
$$

Hence the Peirce decomposition collapses to a **direct sum of algebras**

$$
\mathbb{D}
=
\mathbb{D}_{++}\oplus\mathbb{D}_{--}
=
\mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_-,
$$

of total dimension $1+1+0+0=2$. The summands $\mathbb{D}_{\pm\pm}=\mathbb{R}\Pi_\pm$ are the minimal two-sided ideals of $\mathbb{D}$, as in *Ideals and Peirce Decomposition of the Split-Complex Algebra*, §*The Two-Sided Ideals*.

The four corners are collected in the table.

| Corner | Definition | Value | Dimension over $\mathbb{R}$ |
|---|---|---|---|
| $\mathbb{D}_{++}$ | $\Pi_+\mathbb{D}\Pi_+$ | $\mathbb{R}\Pi_+$ | $1$ |
| $\mathbb{D}_{+-}$ | $\Pi_+\mathbb{D}\Pi_-$ | $0$ | $0$ |
| $\mathbb{D}_{-+}$ | $\Pi_-\mathbb{D}\Pi_+$ | $0$ | $0$ |
| $\mathbb{D}_{--}$ | $\Pi_-\mathbb{D}\Pi_-$ | $\mathbb{R}\Pi_-$ | $1$ |

The element $Q$ and every polynomial in $Q$ lie in the diagonal part

$$
\mathbb{D}_{++}\oplus\mathbb{D}_{--}
=
\operatorname{span}_{\mathbb{R}}\{\Pi_+,\Pi_-\}
=
\mathbb{D}.
$$

The last equality is the commutative phenomenon: the diagonal part is the whole algebra, because the off-diagonal corners vanish. Since $\mathbb{D}$ is commutative, the centraliser of $Q$ is $\mathbb{D}$ for every $Q$. The subalgebra generated by $Q$ is different: $\mathbb{R}[Q]=\mathbb{D}$ when $q'\neq0$, since $\{1,Q\}$ is then a basis, while $\mathbb{R}[Q]=\mathbb{R}$ in the scalar regime $q'=0$.

On $Q$ the Peirce decomposition reads

$$
Q=\lambda_+\Pi_+ + \lambda_-\Pi_-
=(q+q')\Pi_+ + (q-q')\Pi_-,
$$

with zero mixed components. The eigenvalue decomposition is therefore the Peirce decomposition read on the element: the element lies in the diagonal part, and its two diagonal Peirce coordinates are its eigenvalues $\lambda_+=q+q'$ and $\lambda_-=q-q'$. This is the commutative shadow of the biquaternion case, where the idempotents are noncentral, the mixed corners are nonzero, and the diagonal part is only the centraliser.

## The Eigenbasis

**In the distinct case the fixed idempotents $\Pi_\pm$ form a basis of $\mathbb{D}$, and in this basis multiplication by $Q$ is diagonal.**

### The Basis

The two elements
$$
\Pi_+=\frac12(1+j),\qquad \Pi_-=\frac12(1-j)
$$
are idempotent and orthogonal,
$$
\Pi_+^2=\Pi_+,\qquad \Pi_-^2=\Pi_-,\qquad \Pi_+\Pi_-=\Pi_-\Pi_+=0,
$$
and they are complete, $\Pi_++\Pi_-=1$. They are linearly independent: from $a\Pi_++b\Pi_-=0$ one reads $a+b=0$ and $a-b=0$, hence $a=b=0$. Therefore
$$
(\Pi_+,\Pi_-)
$$
is a basis of the plane $\mathbb{D}$.

**Coordinates.** Expanding a general element $Q_{\mathrm{sp}}=x_0+x_1j$ gives
$$
Q_{\mathrm{sp}}=(x_0+x_1)\Pi_++(x_0-x_1)\Pi_-,
$$
so the coordinates of $Q_{\mathrm{sp}}$ in this basis are $(x_0+x_1,\,x_0-x_1)$. For $Q$ itself,
$$
Q=q+jq'\quad\longleftrightarrow\quad(\lambda_+,\lambda_-)=(q+q',\,q-q').
$$

**The coordinates.** The coordinates of $Q_{\mathrm{sp}}$ in the eigenbasis are its two idempotent coordinates $(\xi_+,\xi_-)$, and the decomposition is the identity $Q_{\mathrm{sp}}=\xi_+\Pi_++\xi_-\Pi_-$. No further data are carried by the eigenbasis.

### The Action of $Q$ and the Eigenbasis

**Definition.** An **eigenvector** of $Q$ is a nonzero $Q_{\mathrm{sp}}$ with $QQ_{\mathrm{sp}}=\mu Q_{\mathrm{sp}}$ for some scalar $\mu$, and $\mu$ is the **eigenvalue**. An **eigenbasis** of $Q$ is a basis of $\mathbb{D}$ consisting of eigenvectors.

In the basis $(\Pi_+,\Pi_-)$ the action is diagonal:
$$
Q\Pi_+=\lambda_+\Pi_+,\qquad Q\Pi_-=\lambda_-\Pi_-.
$$
The basis vectors, their coordinates, and their eigenvalues are collected in the table.

| Basis vector | Coordinates in $(1,j)$ | Eigenvalue |
|---|---|---|
| $\Pi_+$ | $\tfrac12(1,1)$ | $\lambda_+=q+q'$ |
| $\Pi_-$ | $\tfrac12(1,-1)$ | $\lambda_-=q-q'$ |

So $(\Pi_+,\Pi_-)$ is an eigenbasis of $Q$, with eigenvalues $\lambda_+$ and $\lambda_-$.

### Uniqueness of the Eigenbasis

When $q'\neq0$ the eigenvalues are distinct, so the eigenspaces are the two lines $\mathbb{R}\Pi_+$ and $\mathbb{R}\Pi_-$. Every eigenbasis is then
$$
(\alpha\Pi_+,\beta\Pi_-),\qquad \alpha,\beta\in\mathbb{R}^{\times},
$$
and no other eigenbasis exists. The pair $(\Pi_+,\Pi_-)$ is the normalised choice $\alpha=\beta=1$: the eigenbasis is unique up to the two independent scales.

When $q'=0$ the element is the scalar $Q=q$, the operator is $L_Q=q\,\mathrm{id}$, every nonzero vector is an eigenvector, and every basis is an eigenbasis. The idempotent basis is then a choice, not a consequence of $Q$.

### The Properties in the Eigenbasis

The decomposition $Q=\lambda_+\Pi_++\lambda_-\Pi_-$ gives every power, every polynomial, and the inverse by the same rule: apply the function to the two eigenvalues and keep the two idempotents. The results are collected in the table.

| Quantity | In the basis $(1,j)$ | In the eigenbasis $(\Pi_+,\Pi_-)$ |
|---|---|---|
| Element $Q$ | $q+jq'$ | $(\lambda_+,\lambda_-)$ |
| Power $Q^n$, $n\geq0$ | — | $(\lambda_+^n,\lambda_-^n)$ |
| Polynomial $f(Q)$ | — | $(f(\lambda_+),f(\lambda_-))$ |
| Inverse $Q^{-1}$, $q'\neq0$ | $\dfrac{q-jq'}{q^2-q'^2}$ | $(\lambda_+^{-1},\lambda_-^{-1})$ |
| Norm $\langle Q\rangle_{*}$ | $q^2-q'^2$ | $\lambda_+\lambda_-$ |
| Trace | $2q$ | $\lambda_++\lambda_-$ |

The eigenbasis is the basis in which the two Peirce coordinates of $Q$ are the two eigenvalues.

**Nilpotents.** There are none. If $N=\nu_+\Pi_++\nu_-\Pi_-$ satisfies $N^2=0$, then $\nu_+^2=\nu_-^2=0$, and over $\mathbb{R}$ this forces $\nu_+=\nu_-=0$, hence $N=0$. The off-diagonal Peirce corners $\mathbb{D}_{+-}$ and $\mathbb{D}_{-+}$ both vanish, so there is no off-diagonal direction in which a nilpotent could live. The nilpotent construction that the biquaternion case requires has no analogue in the split-complex algebra.

### The Spinor Spaces

**A spinor space of $\mathbb{D}$ is a minimal nonzero ideal; the two spinor spaces are the real lines $\mathbb{R}\Pi_+$ and $\mathbb{R}\Pi_-$, and a spinor is one real coefficient on one of them.**

Since $\mathbb{D}$ is commutative, its left, right and two-sided ideals coincide. The minimal nonzero ideals are
$$
S_+=\mathbb{D}\Pi_+=\mathbb{R}\Pi_+,
\qquad
S_-=\mathbb{D}\Pi_-=\mathbb{R}\Pi_-,
$$
each one-dimensional over $\mathbb{R}$, and
$$
\mathbb{D}=S_+\oplus S_-.
$$
The notation $S_\pm$ is reserved for these two spaces.

A **spinor of first chirality** is an element of $S_+$,
$$
\xi_+=a_1\Pi_+,\qquad a_1\in\mathbb{R},
$$
and a **spinor of second chirality** is an element of $S_-$,
$$
\xi_-=a_2\Pi_-,\qquad a_2\in\mathbb{R}.
$$
In the eigenbasis their coordinates are
$$
\xi_+\longleftrightarrow(a_1,0),
\qquad
\xi_-\longleftrightarrow(0,a_2).
$$
The two spinor spaces are the two coordinate axes of the eigenbasis.

The element $Q=\lambda_+\Pi_++\lambda_-\Pi_-$ acts on them by
$$
Q\xi_+=\lambda_+\xi_+,
\qquad
Q\xi_-=\lambda_-\xi_-,
$$
so $S_+$ is the $\lambda_+$-eigenspace and $S_-$ the $\lambda_-$-eigenspace. In coordinates,
$$
a_1\longmapsto\lambda_+a_1,
\qquad
a_2\longmapsto\lambda_-a_2.
$$
A general element $Q_{\mathrm{sp}}=\xi_++\xi_-$ is not a spinor: it is the sum of one spinor of each chirality, and its two components $(\xi_+,\xi_-)$ are the coordinates in the direct sum.

**Complexification.** The article is over $\mathbb{R}$, so the spinors above have real coefficients. After extension of scalars, $\mathbb{D}_{\mathbb{C}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{D}\cong\mathbb{C}\times\mathbb{C}$, the same formulas hold with $a_1,a_2\in\mathbb{C}$ and $\lambda_\pm\in\mathbb{C}$, and the spinor spaces become the complex lines
$$
S_+^{\mathbb{C}}=\mathbb{C}\Pi_+,
\qquad
S_-^{\mathbb{C}}=\mathbb{C}\Pi_-.
$$
Each is one-dimensional over $\mathbb{C}$ and two-dimensional over $\mathbb{R}$. This complexified form is the one that matches the reduced-biquaternion article, where the base field is already $\mathbb{C}$.

## Powers, Polynomial Calculus, and the Group of Units

**The eigenvalue decomposition carries the polynomial calculus, the inverse and the group isomorphism of the unit group.**

For any polynomial $f\in\mathbb{R}[X]$, the idempotent writing $Q=\lambda_+\Pi_++\lambda_-\Pi_-$ gives

$$
f(Q)=f(\lambda_+)\Pi_+ + f(\lambda_-)\Pi_-
=f(q+q')\Pi_+ + f(q-q')\Pi_-.
$$

This follows from $Q^n=\lambda_+^n\Pi_+ + \lambda_-^n\Pi_-$ for $n\geq0$ (with $\Pi_++\Pi_-=1$ for $n=0$) and linearity. In particular,

$$
Q^n=\lambda_+^n\Pi_+ + \lambda_-^n\Pi_-
=(q+q')^n\Pi_+ + (q-q')^n\Pi_-,
\qquad n\geq0.
$$

When $Q$ is a unit, both eigenvalues are nonzero, and the formula extends to negative powers:

$$
Q^{-1}=\lambda_+^{-1}\Pi_+ + \lambda_-^{-1}\Pi_-
=\frac{1}{q+q'}\Pi_+ + \frac{1}{q-q'}\Pi_-.
$$

The result agrees with the inverse formula of *Norm and Invertibility in the General Split-Complex Algebra*, §*The Criterion*,

$$
Q^{-1}=\frac{\bar Q}{\langle Q\rangle_{*}},
$$

since $\bar Q=\lambda_-\Pi_+ + \lambda_+\Pi_-$ and $\langle Q\rangle_{*}=\lambda_+\lambda_-$.

**The group of units.** The map

$$
\mathbb{D}^\times\longrightarrow\mathbb{R}^\times\times\mathbb{R}^\times,
\qquad
Q\longmapsto(\lambda_+,\lambda_-)=(q+q',q-q')
$$

is an isomorphism of groups: multiplication is coordinatewise, and $Q$ is a unit if and only if both eigenvalues are nonzero, that is, if and only if $\lambda_+\lambda_-=\langle Q\rangle_{*}\neq0$. The identity is $1=(1,1)$, corresponding to $\Pi_++\Pi_-$. The inverse is the componentwise inverse displayed above.

The results are collected in the table.

| Operation | Formula | Validity |
|---|---|---|
| Powers | $Q^n=\lambda_+^n\Pi_++\lambda_-^n\Pi_-$ | $n\geq0$ |
| Polynomials | $f(Q)=f(\lambda_+)\Pi_++f(\lambda_-)\Pi_-$ | every $f\in\mathbb{R}[X]$ |
| Inverse | $Q^{-1}=\lambda_+^{-1}\Pi_++\lambda_-^{-1}\Pi_-$ | $Q$ a unit |
| Unit criterion | $Q\in\mathbb{D}^\times\iff\lambda_+\lambda_-\neq0$ | — |
| Group of units | $\mathbb{D}^\times\cong\mathbb{R}^\times\times\mathbb{R}^\times$ | — |

## The Algebraic Fibre of the Decomposition

**The eigenvalue coordinates and the basis coordinates are two linear coordinate systems on the same algebra.**

Fix the pair, that is, fix the labelling of $\Pi_+$ and $\Pi_-$. Every element of $\mathbb{D}$ is

$$
Q_2=\mu_+\Pi_+ + \mu_-\Pi_-,
\qquad \mu_\pm\in\mathbb{R},
$$

and the map $(\mu_+,\mu_-)\mapsto Q_2$ is an $\mathbb{R}$-linear isomorphism $\mathbb{R}^2\to\mathbb{D}$. For $\mu_+\neq\mu_-$ this is the eigenvalue decomposition of $Q_2$, with the eigenprojections $\Pi_\pm$ and the eigenvalue data $(\mu_+,\mu_-)$. For $\mu_+=\mu_-=a$ the element is $Q_2=a$, scalar; the two-term writing is still valid, but its coefficients are not distinct, so it is not an eigenvalue decomposition in the sense of the general definition. The eigenvalue decomposition is then the one-term writing $Q_2=a\cdot1$ of §*The Scalar Regime*.

The unordered spectrum is the image of the map $(\mu_+,\mu_-)\mapsto\{\mu_+,\mu_-\}$. Off the diagonal it is two-to-one: the two preimages of $\{\mu_+,\mu_-\}$ are $\mu_+\Pi_+ + \mu_-\Pi_-$ and $\mu_-\Pi_+ + \mu_+\Pi_-$, which differ by $(\mu_+-\mu_-)(\Pi_+-\Pi_-)=(\mu_+-\mu_-)j\neq0$. The ambiguity is exactly the exchange of the two labels.

### The Coordinate Change to Basis Coordinates

The scalar and split-imaginary coordinates of $Q_2$ are

$$
Q_2
=
\frac{\mu_++\mu_-}{2}
+
\frac{\mu_+-\mu_-}{2}j
=
q+jq',
\qquad
q=\frac{\mu_++\mu_-}{2},
\quad
q'=\frac{\mu_+-\mu_-}{2}.
$$

The map $(\mu_+,\mu_-)\mapsto(q,q')$ is an $\mathbb{R}$-linear isomorphism of $\mathbb{R}^2$. The two coordinate systems are the eigenvalue coordinates and the basis coordinates on the same algebra: $(\Pi_+,\Pi_-)$ is a basis of idempotents, and $(1,j)$ is the basis of the algebra. In the eigenvalue coordinates the eigenvalues are simply the coordinates themselves. The two systems are compared in the table.

| Coordinate system | Coordinates | Element | Eigenvalues |
|---|---|---|---|
| Eigenvalue coordinates | $(\mu_+,\mu_-)$ | $Q_2=\mu_+\Pi_++\mu_-\Pi_-$ | $\mu_+,\mu_-$ |
| Basis coordinates | $(q,q')$ | $Q_2=q+jq'$ | $\lambda_\pm=q\pm q'$ |
| Change | $\mu_\pm=q\pm q'$; $q=(\mu_++\mu_-)/2$, $q'=(\mu_+-\mu_-)/2$ | — | — |

### The Lattice of Eigenvalue Data

If the eigenvalue coordinates are restricted to $\mathbb{Z}^2$, that is, if $\mu_\pm=k_\pm\in\mathbb{Z}$, the basis-coordinate pair $(q,q')$ runs over the lattice

$$
L=\left\{\left(\frac{m}{2},\frac{n}{2}\right):\ m,n\in\mathbb{Z},\ m\equiv n\pmod2\right\}.
$$

Indeed, for $\mu_\pm=k_\pm\in\mathbb{Z}$ one has

$$
q=\frac{\mu_++\mu_-}{2}=\frac{k_++k_-}{2}=\frac{m}{2},
\qquad
q'=\frac{\mu_+-\mu_-}{2}=\frac{k_+-k_-}{2}=\frac{n}{2},
$$

with $m=k_++k_-$ and $n=k_+-k_-$. Then $m-n=2k_-$, so $m\equiv n\pmod2$; conversely, every pair $(m,n)$ of the same parity comes from the integers $k_\pm=(m\pm n)/2$. The parity condition reflects the fact that the idempotents mix the $1$ and $j$ directions: the integral shifts in the eigenvalue coordinates do not map to the rectangular lattice $\mathbb{Z}^2$ in the basis coordinates. For example, $\mu_+=\mu_-=1$ gives $(q,q')=(1,0)$ and $Q=1$, while $\mu_+=2$, $\mu_-=0$ gives $(q,q')=(1,1)$ and $Q=1+j=2\Pi_+$, a zero divisor.

The lattice $L$ is a coordinate lattice, not an intrinsic invariant of $Q$. Nor does it arise as the kernel of an exponential: the split-complex exponential is injective (*Split-Complex Exponential and Lie Group Structure*, §*The Exponential Map: Image and Kernel*). This is a difference from the biquaternion parity-matched lattice, where the corresponding lattice is the kernel of the exponential on the diagonal part.

### The Hyperbolic Polar Form

**On the identity component the decomposition is the hyperbolic polar form $Q=r(\cosh t+j\sinh t)$.**

Let $Q$ be a unit with $\langle Q\rangle_{*}>0$ and $q>0$, so that $Q$ lies in the identity component of $\mathbb{D}^\times$. Then $\lambda_+=q+q'>0$ and $\lambda_-=q-q'>0$. Put

$$
r=\sqrt{\lvert\langle Q\rangle_{*}\rvert}=\sqrt{\lambda_+\lambda_-}>0,
\qquad
t=\operatorname{artanh}\!\left(\frac{q'}{q}\right).
$$

Then

$$
Q=r\bigl(\cosh t+j\sinh t\bigr),
\qquad
\lambda_+=r\exp(t),
\qquad
\lambda_-=r\exp(-t).
$$

In this form,

$$
\lambda_+\lambda_-=r^2=\langle Q\rangle_{*},
\qquad
\frac{\lambda_+}{\lambda_-}=\exp(2t).
$$

Thus $\eta=\exp(t)=\lambda_+/r$ satisfies $\eta^2=\lambda_+/\lambda_-$, and

$$
\lambda_+=r\eta,
\qquad
\lambda_-=r\eta^{-1}.
$$

The eigenvalue formula and the hyperbolic polar form are related by the invertible coordinate change

$$
\lambda_\pm=q\pm q',
\qquad
q=\frac{\lambda_++\lambda_-}{2},
\quad
q'=\frac{\lambda_+-\lambda_-}{2}.
$$

The four components of $\mathbb{D}^\times$ are cut out by the signs of $\lambda_+$ and $\lambda_-$, in the patterns $(+,+)$, $(-,-)$, $(+,-)$ and $(-,+)$. The identity component is the pattern $(+,+)$. On the opposite timelike component, where $\langle Q\rangle_{*}>0$ and $q<0$, the pattern is $(-,-)$, and with the same $r$ and $t=\operatorname{artanh}(q'/q)$ the writing $Q=-r(\cosh t+j\sinh t)$ gives $\lambda_\pm=-r\exp(\pm t)$. In the spacelike regime $\langle Q\rangle_{*}<0$, the two eigenvalues have opposite signs; with the same modulus $r=\sqrt{\lvert\langle Q\rangle_{*}\rvert}$ and with $\varepsilon=\operatorname{sgn}q'\in\{\pm1\}$, one has $q=r\sinh s$, $q'=\varepsilon r\cosh s$, and

$$
\lambda_+=\varepsilon r\exp(\varepsilon s),
\qquad
\lambda_-=-\varepsilon r\exp(-\varepsilon s).
$$

The full modulus–unit statement is *Modulus–Unit Polar Decomposition of Split-Complex Numbers*, §*The Two Factors*. On the identity component the polar form writes $Q$ as a positive scale times a unit factor, while the eigenvalue decomposition writes $Q$ as a linear combination of the two idempotents with the eigenvalues $\lambda_\pm=q\pm q'$ as coefficients. The two readings carry the same data: the scale is $r=\sqrt{\lambda_+\lambda_-}$ and the unit factor is $\exp(tj)$, whose eigenvalues are $\exp(\pm t)$.

## Degenerate Regimes

The eigenvalue decomposition with distinct eigenvalues requires $q'\neq0$, equivalently $\lambda_+\neq\lambda_-$. The scalar and zero-divisor cases remain; the Jordan and nilpotent regimes of the biquaternion case are absent, because the algebra is reduced.

| Regime | Condition | Spectrum | Eigenvalue decomposition |
|---|---|---|---|
| Distinct | $q'\neq0$, $\langle Q\rangle_{*}\neq0$ | $\{\lambda_+,\lambda_-\}$ | $Q=\lambda_+\Pi_++\lambda_-\Pi_-$ |
| Zero divisor | $q'\neq0$, $\langle Q\rangle_{*}=0$ | $\{2q,0\}$ | $Q=2q\Pi_\sigma$ |
| Scalar | $q'=0$ | $\{q\}$ | $Q=q\cdot1$ |
| Jordan | absent: the algebra is reduced | — | — |
| Nilpotent | absent: only $Q=0$ | — | — |

### The Scalar Regime

**A scalar element has a repeated eigenvalue, the one-term eigenprojection $1$, and a unique two-term refinement.**

Suppose $q'=0$, so that $Q=q$ with $q\in\mathbb{R}$. Then $\lambda_+=\lambda_-=q$, a **repeated** eigenvalue: the characteristic polynomial is $(X-q)^2$, and the minimal polynomial is $X-q$. In the sense of the general definition the eigenvalue decomposition is the one-term writing

$$
Q=q\cdot 1=\lambda_+\cdot 1,
$$

with the single eigenprojection $1$.

A two-term writing with the repeated coefficient $q$ is a different object:

$$
Q=q\Pi_+ + q\Pi_-=\lambda_+\Pi_+ + \lambda_-\Pi_-,
\qquad
\lambda_+=\lambda_-=q.
$$

Every complete orthogonal pair of nontrivial idempotents gives such a writing, but the algebra has only one nontrivial pair, $\{\Pi_+,\Pi_-\}$. The nontrivial two-term refinement is therefore unique even though the eigenvalue is repeated. This is in contrast with the biquaternion scalar regime, where every complete orthogonal pair gives a two-term writing and the pair is not determined by the element.

### The Zero-Divisor Regime

**A nonzero zero divisor has one zero eigenvalue and one nonzero eigenvalue, and it admits an eigenvalue decomposition even though it is not a unit.**

Suppose $\langle Q\rangle_{*}=q^2-q'^2=0$ with $Q\neq0$. Then $q'=\pm q$ and $q\neq0$, so

$$
Q=q(1\pm j)=2q\,\Pi_\pm.
$$

Such an element is a nonzero scalar multiple of an idempotent. Its eigenvalues are

$$
\lambda_+=2q,\quad \lambda_-=0
\qquad\text{for } Q=2q\Pi_+,
$$

and the two values are exchanged for $Q=2q\Pi_-$. They are distinct because $q\neq0$. Hence $Q$ **does** admit an eigenvalue decomposition

$$
Q=2q\,\Pi_+ + 0\cdot\Pi_-=\lambda_+\Pi_+ + \lambda_-\Pi_-,
\qquad
\lambda_+=2q,\quad \lambda_-=0,
$$

even though it is not a unit. This is not a failure of the eigenvalue decomposition: it is the case in which one eigenvalue vanishes. The element is semisimple, with minimal polynomial $X(X-2q)$: this is $X(X-\lambda_+)$ for $Q=2q\Pi_+$ and $X(X-\lambda_-)$ for $Q=2q\Pi_-$.

### The Nilpotent Regime

**There are no nonzero nilpotent elements, so there is no Jordan-block regime.**

The algebra $\mathbb{D}\cong\mathbb{R}\times\mathbb{R}$ is a product of fields, hence reduced: it has **no nonzero nilpotent elements**. Indeed, if $Q^2=0$ then $\lambda_+^2=\lambda_-^2=0$, so $\lambda_+=\lambda_-=0$ and $Q=0$. Therefore the nilpotent (Jordan-block) regime of the biquaternion case has no analogue here. Every element of $\mathbb{D}$ has a squarefree minimal polynomial and is semisimple: $p_Q=(X-\lambda_+)(X-\lambda_-)$ for $q'\neq0$ (which is $X(X-2q)$ in the zero-divisor subcase, where $\{\lambda_+,\lambda_-\}=\{2q,0\}$), and $X-q=X-\lambda_+$ for $q'=0$. The only failure of distinct eigenvalues is the scalar case $q'=0$, where $\lambda_+=\lambda_-=q$.

## Remarks

1. **Relation to the model algebra.** Under $\mathbb{D}\cong\mathbb{R}\times\mathbb{R}$, the eigenvalue decomposition is literally the product decomposition: $\lambda_+=q+q'$ and $\lambda_-=q-q'$ are the two components, $\Pi_+$ and $\Pi_-$ are the standard minimal idempotents, and the Lagrange–Sylvester formulas are the interpolation formulas in the product algebra.

2. **Centrality and the Peirce decomposition.** The idempotents $\Pi_\pm$ are central, so the Peirce decomposition is a direct sum of two-sided ideals $\mathbb{D}=\mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_-\cong\mathbb{R}\oplus\mathbb{R}$, and the off-diagonal Peirce components vanish. This is the commutative shadow of the biquaternion Peirce decomposition, where the idempotents are noncentral and the off-diagonal components are nonzero.

3. **Uniqueness and labelling.** The pair $\{\Pi_+,\Pi_-\}$ is the only nontrivial complementary pair of idempotents in $\mathbb{D}$. The labels are exchanged by $j\mapsto-j$, which sends $q'$ to $-q'$ and exchanges $\lambda_+=q+q'$ and $\lambda_-=q-q'$. Unlike the biquaternion case, there is no non-discrete family of eigenprojections.

4. **Degenerate regimes.** The eigenvalue decomposition with distinct eigenvalues requires $q'\neq0$, equivalently $\lambda_+\neq\lambda_-$. The scalar regime $q'=0$ has the repeated eigenvalue $\lambda_+=\lambda_-=q$, the one-term eigenprojection $1$, and a unique two-term refinement. The zero-divisor regime $\langle Q\rangle_{*}=0$, $Q\neq0$, consists of scalar multiples of idempotents and still admits an eigenvalue decomposition, with eigenvalues $2q$ and $0$. There is no Jordan or nilpotent regime, because the algebra is reduced, and every element is semisimple.

5. **The base field.** The corpus fixes the base $\mathbb{R}$. The computations use only that $2$ is invertible: over any field $k$ of characteristic not $2$, the algebra $k[j]$, $j^2=1$, has the same idempotents $\Pi_\pm$, the same eigenvalues $\lambda_\pm=q\pm q'$ for $q'\neq0$, and the same decomposition. The norm, its sign, the polar form and the topology use the order or the real structure and are not part of that general statement.

## Summary

For a split-complex number $Q=q+jq'$ with $q'\neq0$, the eigenvalue decomposition is the writing

$$
Q=\lambda_+\Pi_+ + \lambda_-\Pi_-
=(q+q')\Pi_+ + (q-q')\Pi_-,
\qquad
\Pi_\pm=\frac{1\pm j}{2}.
$$

The eigenvalues are the two values

$$
\lambda_+=q+q'=Q_+,
\qquad
\lambda_-=q-q'=Q_-,
$$

which are real; they are distinct exactly when $q'\neq0$. In that case the idempotents are primitive, orthogonal, complete and central, and they are the eigenprojections. The decomposition is then unique up to the exchange of the two labels.

### Main Results

| Result | Expression |
|---|---|
| Spectrum | $\sigma(Q)=\{\lambda_+,\lambda_-\}=\{q+q',q-q'\}$ |
| Characteristic polynomial | $p_Q(X)=X^2-2qX+\langle Q\rangle_{*}=(X-\lambda_+)(X-\lambda_-)$ |
| Distinctness | $\lambda_+\neq\lambda_-\iff q'\neq0$ |
| Eigenprojections | $\Pi_\pm=\tfrac12(1\pm j)$ |
| Eigenvalue decomposition | $Q=\lambda_+\Pi_++\lambda_-\Pi_-=(q+q')\Pi_++(q-q')\Pi_-$ |
| Peirce decomposition | $\mathbb{D}=\mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_-$ |
| Eigenbasis | $(\Pi_+,\Pi_-)$, with eigenvalues $\lambda_+,\lambda_-$ |
| Nilpotents | none; the algebra is reduced, so $N^2=0$ implies $N=0$ |
| Spinor spaces | $S_\pm=\mathbb{R}\Pi_\pm$, the two minimal ideals; spinors $a_1\Pi_+$ and $a_2\Pi_-$ |
| Polynomial calculus | $f(Q)=f(\lambda_+)\Pi_++f(\lambda_-)\Pi_-$ |
| Group of units | $\mathbb{D}^\times\cong\mathbb{R}^\times\times\mathbb{R}^\times$ |

### Regimes

The zero-divisor row is a subcase of the distinct row, separated because one eigenvalue vanishes; the scalar row includes $Q=0$.

| Regime | Condition | Spectrum | Minimal polynomial | Eigenvalue decomposition |
|---|---|---|---|---|
| Distinct | $q'\neq0$, $\langle Q\rangle_{*}\neq0$ | $\{\lambda_+,\lambda_-\}$, distinct | $(X-\lambda_+)(X-\lambda_-)$ | $Q=\lambda_+\Pi_+ + \lambda_-\Pi_-$ |
| Zero divisor | $q'\neq0$, $\langle Q\rangle_{*}=0$ | $\{\lambda_\sigma,\lambda_{-\sigma}\}=\{2q,0\}$ | $X(X-2q)$ | $Q=2q\Pi_\sigma + 0\cdot\Pi_{-\sigma}$ |
| Scalar | $q'=0$ | $\{q\}$ | $X-q$ | $Q=q\cdot1$; refinement $Q=q\Pi_+ + q\Pi_-$ |
| Jordan | absent: the algebra is reduced | — | — | — |
| Nilpotent | absent; only $Q=0$ | — | — | — |

The Peirce decomposition relative to $\Pi_+$ has corners $\mathbb{D}_{\sigma\tau}=\Pi_\sigma\mathbb{D}\Pi_\tau$. Its off-diagonal corners vanish, and its diagonal part is the whole algebra $\mathbb{D}=\mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_-$. The element $Q$ has the diagonal coordinates $\lambda_+=q+q'$ and $\lambda_-=q-q'$ and zero mixed coordinates. The centraliser of $Q$ is all of $\mathbb{D}$; the subalgebra $\mathbb{R}[Q]$ is all of $\mathbb{D}$ exactly when $Q$ is not scalar. The polynomial calculus, the inverse and the group isomorphism $\mathbb{D}^\times\cong\mathbb{R}^\times\times\mathbb{R}^\times$ all follow from the decomposition. The hyperbolic polar form gives the same data as $\lambda_\pm=r \exp(\pm t)$ on the identity component.

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
| Coordinates of a general element in the eigenbasis | $(\xi_+,\xi_-)$ | $(\xi_+,\xi_-)$ | $(a_{11},a_{12},a_{21},a_{22})$ |
| Nilpotents in the eigenbasis | none | none | $\vec\Upsilon_\pm$ in the two mixed corners |
| Spinor spaces | $S_\pm=\mathbb{R}\Pi_\pm$, real lines | $S_\pm=\mathbb{C}\Pi_\pm$, complex lines | $S_\pm=\mathbb{B}\tilde\Pi_\pm\cong\mathbb{C}^2$, complex planes |
| Spinor coordinates | one real coefficient per chirality | one complex coefficient per chirality | two complex coefficients per chirality |
| Action of $Q$ on a spinor | scalar: $\lambda_+$ on $S_+$, $\lambda_-$ on $S_-$ | scalar: $\lambda_+$ on $S_+$, $\lambda_-$ on $S_-$ | $\lambda_+$ on the first coordinate, $\lambda_-$ on the second |
| Unit group | $\cong\mathbb{R}^\times\times\mathbb{R}^\times$ | $\cong\mathbb{C}^\times\times\mathbb{C}^\times$ | $\mathbb{B}^\times$; eigenvalue map surjective, not injective, not a homomorphism |

Read down a column for one algebra and across a row for one concept. The rows down to the eigenprojections follow one pattern; the rows below them record where the algebras part: whether the idempotents depend on the element and whether they are central, the two mixed square-zero lines of the biquaternion Peirce decomposition, and the biquaternion unit group, which is no longer a product. The last rows record the spinor content: one real coefficient per chirality for the split-complex algebra, one complex coefficient per chirality for the reduced biquaternion algebra, and two complex coefficients per chirality, forming a complex plane, for the biquaternion algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}=\mathbb{R}[x]/(x^2-1)$ | Split-complex algebra, dimension $2$ over $\mathbb{R}$ |
| $Q=q+jq'$ | General split-complex number, $q,q'\in\mathbb{R}$ |
| $\bar Q=q-jq'$ | Split-complex conjugate |
| $\langle Q\rangle_{*}=Q\bar Q=q^2-q'^2=\lambda_+\lambda_-$ | Norm, signature $(1,1)$ |
| $\operatorname{tr}(Q)=2q=\lambda_++\lambda_-$ | Trace |
| $\Pi_\pm=\tfrac12(1\pm j)$ | Standard idempotents; the eigenprojections when $q'\neq0$ |
| $Q_\pm=q\pm q'$ | Idempotent coordinates, equal to the eigenvalues: $Q_\pm=\lambda_\pm$ |
| $\lambda_\pm=q\pm q'$ | Eigenvalues, with $\lambda_+=q+q'$ and $\lambda_-=q-q'$ |
| $\sigma(Q)=\{\lambda_+,\lambda_-\}=\{q+q',q-q'\}$ | Spectrum |
| $p_Q(X)=X^2-2qX+\langle Q\rangle_{*}=(X-\lambda_+)(X-\lambda_-)$ | Characteristic polynomial |
| $L_Q(X)=QX$ | Multiplication operator; eigenvalues $\lambda_+,\lambda_-$ in the eigenbasis |
| $a_1,a_2$ | Spinor coordinates on $S_+$ and $S_-$, the two diagonal entries of the matrix in the eigenbasis |
| $\alpha,\beta$ | Scales of the eigenbasis $(\alpha\Pi_+,\beta\Pi_-)$ |
| $S_\pm=\mathbb{D}\Pi_\pm=\mathbb{R}\Pi_\pm$ | The two spinor spaces, the two minimal ideals (real lines) |
| $\mathbb{D}_{\sigma\tau}=\Pi_\sigma\mathbb{D}\Pi_\tau$ | Peirce corners of the pair $\Pi_\pm$, $\sigma,\tau\in\{+,-\}$ |
| $\mathbb{R}[Q]$ | Subalgebra generated by $Q$ |
| $C(Q)=\mathbb{D}$ | Centraliser; the algebra is commutative |
| $\mathbb{D}^\times=\{Q\in\mathbb{D}:\langle Q\rangle_{*}\neq0\}$ | Group of units, characterised by $\lambda_+\lambda_-\neq0$ |
| $L=\{(m/2,n/2):m,n\in\mathbb{Z},\ m\equiv n\pmod2\}$ | Lattice of basis-coordinate data for integral eigenvalue coordinates $\mu_\pm\in\mathbb{Z}$ |
| $r=\sqrt{\lvert\langle Q\rangle_{*}\rvert}$, $t=\operatorname{artanh}(q'/q)$ | Modulus and hyperbolic angle, with $\lambda_\pm=r \exp(\pm t)$ on the identity component |
| $Q_{\mathrm{sp}}=a_1\Pi_++a_2\Pi_-$ | General element in the spinor coordinates, with matrix $\operatorname{diag}(a_1,a_2)$ |
| $Q_2=\mu_+\Pi_++\mu_-\Pi_-$ | General element in the eigenvalue coordinates |
| $\mu$ | A test scalar in the definition of an eigenvalue |
| $\mu_\pm$ | Eigenvalue coordinates on the diagonal part |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for idempotents, Peirce decompositions and the structure of finite-dimensional algebras.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, Graduate Texts in Mathematics 131, 2nd ed. 2001), for semisimplicity and the structure of finite-dimensional algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split-complex algebra as a Clifford algebra and its norm.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the hyperbolic geometry of the split-complex plane.
- The corpus articles: [The Eigenvalue Decomposition of an Element](the-eigenvalue-decomposition-of-an-element.html), [The Lagrange–Sylvester Eigenprojector Formula](the-lagrange-sylvester-eigenprojector-formula.html), [Split-Complex Algebra](split-complex-algebra.html), [Square Roots of One and the Idempotents of the Split-Complex Algebra](square-roots-of-one-and-the-idempotents-of-the-split-complex-algebra.html), [Ideals and Peirce Decomposition of the Split-Complex Algebra](ideals-and-peirce-decomposition-of-the-split-complex-algebra.html), [Norm and Invertibility in the General Split-Complex Algebra](norm-and-invertibility-in-the-general-split-complex-algebra.html), [Split-Complex Regular Element Representation](split-complex-regular-element-representation.html), [Split-Complex Exponential and Lie Group Structure](split-complex-exponential-and-lie-group-structure.html), [Modulus–Unit Polar Decomposition of Split-Complex Numbers](modulus-unit-polar-decomposition-of-split-complex-numbers.html), [Exponential Polar Decomposition of Split-Complex Numbers](exponential-polar-decomposition-of-split-complex-numbers.html), [Eigenbasis of a Reduced Biquaternion](eigenbasis-of-a-reduced-biquaternion.html), [Eigenbasis of a Biquaternion](eigenbasis-of-a-biquaternion.html) and [Conventions in Mathematics](conventions-in-mathematics.html).
