# __Eigenvalue Decomposition and Eigenbasis of a Reduced Biquaternion__

## Introduction

The reduced biquaternion algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$ is commutative, associative and unital. It is four-dimensional over $\mathbb{R}$ and two-dimensional over $\mathbb{C}$, with real basis $1,i,j,ij$ and complex basis $1,j$; the multiplication is fixed by $i^{2}=-1$, $j^{2}=1$ and $ij=ji$. This article reads the **eigenvalue decomposition** of a reduced biquaternion $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ in the distinct case $Q_{\blacktriangledown}\neq0$: the writing

$$
\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-,
\qquad
\lambda_+=Q_+=Q_{\blacktriangle}+Q_{\blacktriangledown},
\quad
\lambda_-=Q_-=Q_{\blacktriangle}-Q_{\blacktriangledown},
$$

Here the coefficients $\lambda_+,\lambda_-$ are the eigenvalues and the idempotents $\Pi_\pm$ are the eigenprojections. The eigenvalues are therefore the idempotent coordinates, and their values are displayed with them throughout. The article is the four-dimensional commutative counterpart of *The Biquaternion Eigenvalue Decomposition* and the complex analogue of *Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number*. The general definition and the existence and uniqueness theorems are those of *The Eigenvalue Decomposition of an Element*. The reduced biquaternion content is threefold: for a non-scalar element the eigenprojections are the standard idempotents $\Pi_\pm$; they are central and independent of the element; and the Peirce decomposition of *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions* relative to either of them is the decomposition of the whole algebra.

**The results.** The spectrum of $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ is $\{Q_{\blacktriangle}+Q_{\blacktriangledown},Q_{\blacktriangle}-Q_{\blacktriangledown}\}$, and in the distinct case $Q_{\blacktriangledown}\neq0$ the two eigenprojections are the standard idempotents $\Pi_\pm=\tfrac12(1\pm j)$. They are central and independent of $\breve Q$, the eigenvalue decomposition is the direct-product decomposition $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$ read on the element, and the Peirce decomposition relative to $\Pi_+$ has two vanishing off-diagonal corners. The polynomial calculus is the componentwise calculus on $\mathbb{C}\times\mathbb{C}$, and the unit group is $\mathbb{C}^\times\times\mathbb{C}^\times$. The idempotents form a complex eigenbasis of the multiplication operator, with eigenvalues $\lambda_+$ and $\lambda_-$. The scalar regime has a repeated eigenvalue, the zero-divisor regime keeps a two-term decomposition with one zero eigenvalue, and there is no nilpotent regime. The two minimal ideals $S_\pm=\mathbb{C}\Pi_\pm$ are the spinor spaces: a spinor is a single complex coefficient on one of them.

| Question | Answer |
|---|---|
| Algebra | $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$ |
| Element | $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ |
| Spectrum | $\sigma(\breve Q)=\{\lambda_+,\lambda_-\}=\{Q_{\blacktriangle}+Q_{\blacktriangledown},Q_{\blacktriangle}-Q_{\blacktriangledown}\}$ |
| Distinctness | $\lambda_+\neq\lambda_-\iff Q_{\blacktriangledown}\neq0$ |
| Eigenprojections | $\Pi_\pm=\tfrac12(1\pm j)$, independent of $\breve Q$ |
| Eigenprojections central? | yes |
| Eigenvalue decomposition | $\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-$ |
| Peirce decomposition | $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$, with zero off-diagonal corners |
| Eigenbasis | $(\Pi_+,\Pi_-)$, with eigenvalues $\lambda_+,\lambda_-$ |
| Matrix model | $M(\breve Q_2)=\operatorname{diag}(A_1,A_2)$; the regular matrix is $\begin{pmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix}$ |
| Spinor spaces | $S_\pm=\mathbb{C}\Pi_\pm$, two complex lines; one complex spinor coordinate per chirality |
| Unit group | $\mathbb{B}_{\mathrm{r}}^\times\cong\mathbb{C}^\times\times\mathbb{C}^\times$ |

**Conventions.** The notation is fixed in *Conventions in Mathematics*: the general element is $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$, with $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$ and $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$ complex; the idempotents are $\Pi_\pm=\tfrac12(1\pm j)$; and the idempotent coordinates are $Q_+=Q_{\blacktriangle}+Q_{\blacktriangledown}$ and $Q_-=Q_{\blacktriangle}-Q_{\blacktriangledown}$, so that $\breve Q=Q_+\Pi_++Q_-\Pi_-$. The eigenvalues are $\lambda_+=Q_+$ and $\lambda_-=Q_-$, so that $\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-$. The reduced norm is $\langle\breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=\lambda_+\lambda_-$. The two spinor spaces are $S_\pm=\mathbb{C}\Pi_\pm$, with complex spinor coordinates $A_1,A_2$, the two diagonal entries of the matrix in the eigenbasis. The base field is $\mathbb{C}$.

**Boundaries.** The split-complex case is the subject of *Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number*; the biquaternion case is *The Biquaternion Eigenvalue Decomposition*; the spectral theory is *Reduced Biquaternion Spectral Theory*; the Peirce and ideal theory is *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*; the exponential and the logarithm built on the decomposition are those of *Reduced Biquaternion Elementary Functions*; and the polar forms are those of *Modulus–Unit Polar Decomposition of Reduced Biquaternions* and *Exponential Polar Decomposition of Reduced Biquaternions*. The general definition, existence and uniqueness of the eigenvalue decomposition are those of *The Eigenvalue Decomposition of an Element* and are not restated.

## The Spectrum and the Characteristic Polynomial

**Definition.** Let $\breve Q\in\mathbb{B}_{\mathrm{r}}$. A complex scalar $\mu$ is an **eigenvalue** of $\breve Q$ if $\breve Q-\mu 1$ is not a unit in $\mathbb{B}_{\mathrm{r}}$; the set of eigenvalues is the **spectrum** $\sigma(\breve Q)$. This is the definition of *The Eigenvalue Decomposition of an Element*, §*The Eigenvalues of an Element*.

**Notation.** The two eigenvalues are the idempotent coordinates, and their values are
$$
\lambda_+=Q_+=Q_{\blacktriangle}+Q_{\blacktriangledown}
=(q_{\blacktriangle}+q_{\blacktriangledown})+i(q'_{\blacktriangle}+q'_{\blacktriangledown}),
$$
$$
\lambda_-=Q_-=Q_{\blacktriangle}-Q_{\blacktriangledown}
=(q_{\blacktriangle}-q_{\blacktriangledown})+i(q'_{\blacktriangle}-q'_{\blacktriangledown}).
$$
They are written $\lambda_\pm$ when their values are exhibited, and $Q_\pm$ when they are read as the idempotent coordinates. The test scalar of the definition is written $\mu$, so the letter $\lambda$ is reserved for the two eigenvalues, as in the conventions of *Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number*, §*Introduction*. The pair is the analogue of $\lambda_\pm=Q_t\pm i\sqrt{Q_x^2+Q_y^2+Q_z^2}$ of *The Biquaternion Eigenvalue Decomposition*, with the scalar part $Q_t$ replaced by $Q_{\blacktriangle}$ and the vector-part radical $i\sqrt{Q_x^2+Q_y^2+Q_z^2}$ by $Q_{\blacktriangledown}$.

**Theorem.** The spectrum of $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ is
$$
\boxed{\; \sigma(\breve Q)=\{\lambda_+,\lambda_-\}=\{Q_+,Q_-\}=\{Q_{\blacktriangle}+Q_{\blacktriangledown},\,Q_{\blacktriangle}-Q_{\blacktriangledown}\} \;}.
$$

**Proof.** In the idempotent coordinates,
$$
\breve Q-\mu 1=(Q_+-\mu)\Pi_++(Q_--\mu)\Pi_-.
$$
By the criterion of *Norm and Invertibility in the Algebra of the Reduced Biquaternions*, §*The Reduced Norm and the Invertibility Criterion*, an element is a unit exactly when both idempotent coordinates are nonzero. Hence $\breve Q-\mu 1$ is not a unit exactly when $Q_+-\mu=0$ or $Q_--\mu=0$, that is, when $\mu=Q_+$ or $\mu=Q_-$.

The definition is the algebraic one; it agrees with the spectrum of left multiplication computed in *Reduced Biquaternion Spectral Theory*, §*The Spectrum of an Element*, because the algebra is commutative and the coefficients are complex.

**Characteristic polynomial.** By *Reduced Biquaternion Spectral Theory*, §*The Spectrum of an Element*, the characteristic polynomial of the left multiplication is
$$
p_{\breve Q}(X)=X^{2}-\operatorname{tr}(\breve Q)X+\det(\breve Q)=(X-\lambda_+)(X-\lambda_-),
$$
with
$$
\operatorname{tr}(\breve Q)=\lambda_++\lambda_-=2Q_{\blacktriangle},\qquad
\det(\breve Q)=\lambda_+\lambda_-=\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}.
$$
The discriminant is
$$
(\lambda_+-\lambda_-)^{2}=(2Q_{\blacktriangledown})^{2}=4Q_{\blacktriangledown}^{2},
$$
so the eigenvalues are distinct exactly when $Q_{\blacktriangledown}\neq0$, the analogue of $Q_x^2+Q_y^2+Q_z^2\neq0$ in the biquaternion case and of $q'\neq0$ for $Q=q+jq'$ in the split-complex case.

**Minimal polynomial.** When $Q_{\blacktriangledown}\neq0$, the characteristic polynomial is squarefree and is the minimal polynomial. In the zero-divisor subcase $\lambda_+\lambda_-=0$ with $\breve Q\neq0$ one factor is $X$: the polynomial is $X(X-\lambda_+)$ when $\lambda_-=0$ and $X(X-\lambda_-)$ when $\lambda_+=0$. When $Q_{\blacktriangledown}=0$, the element is the complex scalar $Q_{\blacktriangle}$ and the minimal polynomial is $X-Q_{\blacktriangle}$. In every case the minimal polynomial is squarefree, so every element is semisimple.

The data of the spectrum are collected in the table.

| Quantity | Value |
|---|---|
| Spectrum | $\sigma(\breve Q)=\{\lambda_+,\lambda_-\}$ |
| Eigenvalues | $\lambda_+=Q_{\blacktriangle}+Q_{\blacktriangledown}$, $\lambda_-=Q_{\blacktriangle}-Q_{\blacktriangledown}$ |
| Sum | $\lambda_++\lambda_-=2Q_{\blacktriangle}$ |
| Product | $\lambda_+\lambda_-=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=\langle\breve Q\rangle_{\mathrm{ts}}$ |
| Discriminant | $(\lambda_+-\lambda_-)^{2}=4Q_{\blacktriangledown}^{2}$ |
| Characteristic polynomial | $p_{\breve Q}(X)=X^{2}-2Q_{\blacktriangle}X+\langle\breve Q\rangle_{\mathrm{ts}}=(X-\lambda_+)(X-\lambda_-)$ |
| Minimal polynomial | $(X-\lambda_+)(X-\lambda_-)$ if $Q_{\blacktriangledown}\neq0$; $X-Q_{\blacktriangle}$ if $Q_{\blacktriangledown}=0$ |

## The Eigenprojections

**The eigenprojections of a non-scalar reduced biquaternion are the two fixed central idempotents $\Pi_\pm$.**

By *Square Roots of One and the Idempotents of the Algebra of the Reduced Biquaternions*, §*The Standard Idempotents*, the two nontrivial idempotents are
$$
\Pi_+=\tfrac12(1+j),\qquad \Pi_-=\tfrac12(1-j),
$$
and they satisfy
$$
\Pi_+^{2}=\Pi_+,\qquad \Pi_-^{2}=\Pi_-,\qquad \Pi_+\Pi_-=\Pi_-\Pi_+=0,\qquad \Pi_++\Pi_-=1.
$$
They are central because the algebra is commutative, and the algebra has no other nontrivial idempotents.

They are the **eigenprojections** of $\breve Q$:
$$
\breve Q\Pi_+=\lambda_+\Pi_+,\qquad \breve Q\Pi_-=\lambda_-\Pi_-.
$$
Indeed, since $j\Pi_+=\Pi_+$ and $j\Pi_-=-\Pi_-$,
$$
\breve Q\Pi_+=(Q_{\blacktriangle}+jQ_{\blacktriangledown})\Pi_+=(Q_{\blacktriangle}+Q_{\blacktriangledown})\Pi_+=\lambda_+\Pi_+,
$$
and, with $Q_{\blacktriangle}-Q_{\blacktriangledown}$ in place of $Q_{\blacktriangle}+Q_{\blacktriangledown}$ and $\Pi_-$ in place of $\Pi_+$,
$$
\breve Q\Pi_-=\lambda_-\Pi_-.
$$

Equivalently, by the Lagrange–Sylvester eigenprojector formula of *The Lagrange–Sylvester Eigenprojector Formula*, §*The Eigenprojector Formula*,
$$
\boxed{\;
\Pi_+=\frac{\breve Q-\lambda_-}{\lambda_+-\lambda_-},\qquad
\Pi_-=\frac{\breve Q-\lambda_+}{\lambda_--\lambda_+},\qquad
\lambda_+-\lambda_-=2Q_{\blacktriangledown}
\;}.
$$
The formula applies when $Q_{\blacktriangledown}\neq0$; it exhibits $\Pi_\pm$ as polynomials in $\breve Q$. When $Q_{\blacktriangledown}=0$ the denominator vanishes and the formula does not apply.

**Independence of the element.** The formulae collapse to the fixed idempotents $\Pi_\pm$: the eigenprojections do not depend on $\breve Q$. This is the structural difference from the biquaternion case, where the eigenprojections are the idempotents built from the pure root $\vec\Xi=-i\vec Q/\sqrt{Q_x^2+Q_y^2+Q_z^2}$ of the vector part and therefore vary with $\tilde Q$ (*The Biquaternion Eigenvalue Decomposition*, §*The Eigenprojectors*). Here the pair $\Pi_+,\Pi_-$ is fixed for the whole algebra, and the dependence on the element lies in the eigenvalues alone.

The pair is collected in the table.

| Idempotent | Definition | Eigenvalue | Properties |
|---|---|---|---|
| $\Pi_+$ | $\tfrac12(1+j)$ | $\lambda_+=Q_{\blacktriangle}+Q_{\blacktriangledown}$ | $\Pi_+^2=\Pi_+$, central, primitive |
| $\Pi_-$ | $\tfrac12(1-j)$ | $\lambda_-=Q_{\blacktriangle}-Q_{\blacktriangledown}$ | $\Pi_-^2=\Pi_-$, central, primitive |

The two idempotents are complementary and orthogonal, $\Pi_++\Pi_-=1$ and $\Pi_+\Pi_-=0$.

## The Eigenvalue Decomposition

**Every reduced biquaternion with distinct eigenvalues is the complex linear combination of the two fixed idempotents with its eigenvalues as coefficients.**

Summing the two eigenvalue relations,

$$
\boxed{\ \breve Q=\lambda_+\Pi_++\lambda_-\Pi_-
=(Q_{\blacktriangle}+Q_{\blacktriangledown})\Pi_++(Q_{\blacktriangle}-Q_{\blacktriangledown})\Pi_-\ }.
$$

Equivalently, exhibiting the values in the basis $1,j$,

$$
\breve Q
=
\frac{\lambda_++\lambda_-}{2}
+
\frac{\lambda_+-\lambda_-}{2}j
=
Q_{\blacktriangle}+jQ_{\blacktriangledown}.
$$

So the decomposition writes $\breve Q$ as a complex linear combination of the two primitive idempotents, with the eigenvalues as coefficients.

This is an eigenvalue decomposition in the sense of *The Eigenvalue Decomposition of an Element*, §*The Eigenvalue Decomposition*: the coefficients $\lambda_+,\lambda_-$ are distinct when $Q_{\blacktriangledown}\neq0$, the idempotents $\Pi_\pm$ are nonzero, orthogonal and complete, and they are the eigenprojections.

**Example.** For $\breve Q=2+3i+(1-i)j$ the coordinates are $Q_{\blacktriangle}=2+3i$ and $Q_{\blacktriangledown}=1-i$, so the eigenvalues are
$$
\lambda_+=(2+3i)+(1-i)=3+2i,\qquad
\lambda_-=(2+3i)-(1-i)=1+4i,
$$
with $\lambda_++\lambda_-=4+6i=2Q_{\blacktriangle}$ and $\lambda_+\lambda_-=-5+14i=\langle\breve Q\rangle_{\mathrm{ts}}$. The decomposition is
$$
\breve Q=(3+2i)\Pi_++(1+4i)\Pi_-.
$$

The data of the decomposition are collected in the table.

| Item | Value |
|---|---|
| Element | $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ |
| Eigenvalues | $\lambda_+=Q_{\blacktriangle}+Q_{\blacktriangledown}$, $\lambda_-=Q_{\blacktriangle}-Q_{\blacktriangledown}$ |
| Eigenprojections | $\Pi_\pm=\tfrac12(1\pm j)$ |
| Decomposition | $\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-$ |
| Distinctness | $\lambda_+\neq\lambda_-\iff Q_{\blacktriangledown}\neq0$ |
| Coordinates | $(\lambda_+,\lambda_-)$ in the basis $(\Pi_+,\Pi_-)$ |

**Uniqueness.** By the uniqueness theorem of *The Eigenvalue Decomposition of an Element*, §*Uniqueness*, an element with distinct eigenvalues has a unique eigenprojection attached to each eigenvalue. Here the two eigenprojections are $\Pi_\pm$, and they are fixed for the whole algebra. The unordered pair $\{\lambda_+,\lambda_-\}$ is the spectrum and is determined by $\breve Q$; the ordered pair is determined once the labelling $\Pi_+,\Pi_-$ is fixed. The only ambiguity is the exchange of the two labels by the tessarine sign $j\mapsto-j$, which sends $\Pi_+\leftrightarrow\Pi_-$ and $\lambda_+\leftrightarrow\lambda_-$. There is no continuous family of idempotents and no branch choice.

**Semisimplicity.** Since $\lambda_+\neq\lambda_-$, the minimal polynomial is squarefree and $\breve Q$ is semisimple. The decomposition is the diagonalisation of $\breve Q$ with respect to the central idempotents $\Pi_\pm$. When $\lambda_+=\lambda_-=Q_{\blacktriangle}$, the element is scalar and the spectrum is a single value; the eigenvalue decomposition then has one term, as §*Degenerate Regimes* explains.

## The Peirce Decomposition Relative to the Eigenprojection

**The Peirce decomposition relative to $\Pi_+$ is the direct product $\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$, with vanishing off-diagonal corners.**

Let $e=\Pi_+$ and $1-e=\Pi_-$. The **Peirce corners** of the pair are
$$
\mathbb{B}_{\sigma\tau}=\Pi_\sigma\mathbb{B}_{\mathrm{r}}\Pi_\tau,\qquad \sigma,\tau\in\{+,-\},
$$
in the notation of *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*, §*The Peirce Decomposition*. The Peirce decomposition is
$$
\mathbb{B}_{\mathrm{r}}=\mathbb{B}_{++}\oplus\mathbb{B}_{+-}\oplus\mathbb{B}_{-+}\oplus\mathbb{B}_{--}.
$$
Because the idempotents are central and orthogonal,
$$
\mathbb{B}_{+-}=\Pi_+\mathbb{B}_{\mathrm{r}}\Pi_-=0,\qquad
\mathbb{B}_{-+}=\Pi_-\mathbb{B}_{\mathrm{r}}\Pi_+=0,
$$
and
$$
\mathbb{B}_{++}=\mathbb{C}\Pi_+,\qquad \mathbb{B}_{--}=\mathbb{C}\Pi_-.
$$
The vanishing is the commutative case of *Off-Diagonal Peirce Components and Noncentral Idempotents*, where the mixed part measures the failure of the idempotent to be central. So the decomposition collapses to the direct product
$$
\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-\cong\mathbb{C}\times\mathbb{C}.
$$

The four corners are collected in the table.

| Corner | Definition | Value | Dimension over $\mathbb{C}$ |
|---|---|---|---|
| $\mathbb{B}_{++}$ | $\Pi_+\mathbb{B}_{\mathrm{r}}\Pi_+$ | $\mathbb{C}\Pi_+$ | $1$ |
| $\mathbb{B}_{+-}$ | $\Pi_+\mathbb{B}_{\mathrm{r}}\Pi_-$ | $0$ | $0$ |
| $\mathbb{B}_{-+}$ | $\Pi_-\mathbb{B}_{\mathrm{r}}\Pi_+$ | $0$ | $0$ |
| $\mathbb{B}_{--}$ | $\Pi_-\mathbb{B}_{\mathrm{r}}\Pi_-$ | $\mathbb{C}\Pi_-$ | $1$ |

The two lines are the minimal ideals of *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*, §*The Two-Sided Ideals*, and each is generated by its idempotent, so $\Pi_\pm$ are primitive idempotents.

On $\breve Q$ the Peirce decomposition reads
$$
\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-,
$$
with zero mixed components. The eigenvalue decomposition is therefore the Peirce decomposition read on the element: the element lies in the diagonal part, and its two diagonal Peirce coordinates are its eigenvalues.

For $Q_{\blacktriangledown}\neq0$, *The Centraliser and the Diagonal Peirce Part*, §*The theorem*, identifies the diagonal part with the centraliser of $\breve Q$. Here the diagonal part is the whole algebra, and the centraliser is the whole algebra as well:
$$
C(\breve Q)=\mathbb{B}_{\mathrm{r}}
$$
for every $\breve Q$, because the algebra is commutative. The subalgebra generated by $\breve Q$ is $\mathbb{C}[\breve Q]=\operatorname{span}_{\mathbb{C}}\{1,\breve Q\}$; it equals the whole algebra when $Q_{\blacktriangledown}\neq0$, and it is the scalar line $\mathbb{C}\cdot1$ when $Q_{\blacktriangledown}=0$. This is the commutative shadow of the biquaternion Peirce decomposition: there the idempotents are noncentral, the mixed corners are nonzero, and the diagonal part is only the centraliser $\mathbb{C}[\tilde Q]$ (*Ideals, Peirce Decompositions and Spinors in the Biquaternion Algebra*, §*The Peirce Decompositions*).

## The Eigenbasis

**In the distinct case the fixed idempotents $\Pi_\pm$ form a $\mathbb{C}$-basis of $\mathbb{B}_{\mathrm{r}}$, and in this basis multiplication by $\breve Q$ is diagonal.**

### The Basis

The two elements
$$
\Pi_+=\frac12(1+j),\qquad \Pi_-=\frac12(1-j)
$$
are idempotent and orthogonal,
$$
\Pi_+^2=\Pi_+,\qquad \Pi_-^2=\Pi_-,\qquad \Pi_+\Pi_-=\Pi_-\Pi_+=0,
$$
and they are complete, $\Pi_++\Pi_-=1$. They are linearly independent over $\mathbb{C}$: from $a\Pi_++b\Pi_-=0$ one reads $a+b=0$ and $a-b=0$, hence $a=b=0$. Therefore
$$
(\Pi_+,\Pi_-)
$$
is a $\mathbb{C}$-basis of $\mathbb{B}_{\mathrm{r}}$.

**Coordinates.** Expanding a general element $\breve Q_2=Q_{2,\blacktriangle}+jQ_{2,\blacktriangledown}$ gives
$$
\breve Q_2=(Q_{2,\blacktriangle}+Q_{2,\blacktriangledown})\Pi_++(Q_{2,\blacktriangle}-Q_{2,\blacktriangledown})\Pi_-,
$$
so the coordinates of $\breve Q_2$ in this basis are $(Q_{2,\blacktriangle}+Q_{2,\blacktriangledown},\,Q_{2,\blacktriangle}-Q_{2,\blacktriangledown})$. For $\breve Q$ itself,
$$
\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}
\quad\longleftrightarrow\quad
(\lambda_+,\lambda_-)=(Q_{\blacktriangle}+Q_{\blacktriangledown},\,Q_{\blacktriangle}-Q_{\blacktriangledown}).
$$

**The coordinates.** The coordinates of $\breve Q_2$ in the eigenbasis are its two idempotent coordinates $(A_1,A_2)$, and the decomposition is the identity $\breve Q_2=A_1\Pi_++A_2\Pi_-$. No further data are carried by the eigenbasis.

### The Action of $\breve Q$ and the Eigenbasis

**Definition.** An **eigenvector** of $\breve Q$ is a nonzero $\breve Q_2$ with $\breve Q\breve Q_2=\mu\breve Q_2$ for some scalar $\mu$, and $\mu$ is the **eigenvalue**. An **eigenbasis** of $\breve Q$ is a $\mathbb{C}$-basis of $\mathbb{B}_{\mathrm{r}}$ consisting of eigenvectors.

In the basis $(\Pi_+,\Pi_-)$ the action is diagonal:
$$
\breve Q\Pi_+=\lambda_+\Pi_+,\qquad \breve Q\Pi_-=\lambda_-\Pi_-.
$$
The basis vectors, their coordinates, and their eigenvalues are collected in the table.

| Basis vector | Coordinates in $(1,j)$ | Eigenvalue |
|---|---|---|
| $\Pi_+$ | $\tfrac12(1,1)$ | $\lambda_+=Q_{\blacktriangle}+Q_{\blacktriangledown}$ |
| $\Pi_-$ | $\tfrac12(1,-1)$ | $\lambda_-=Q_{\blacktriangle}-Q_{\blacktriangledown}$ |

So $(\Pi_+,\Pi_-)$ is an eigenbasis of $\breve Q$, with eigenvalues $\lambda_+$ and $\lambda_-$.

### Uniqueness of the Eigenbasis

When $Q_{\blacktriangledown}\neq0$ the eigenvalues are distinct, so the eigenspaces are the two complex lines $\mathbb{C}\Pi_+$ and $\mathbb{C}\Pi_-$. Every eigenbasis is then
$$
(\alpha\Pi_+,\beta\Pi_-),\qquad \alpha,\beta\in\mathbb{C}^{\times},
$$
and no other eigenbasis exists. The pair $(\Pi_+,\Pi_-)$ is the normalised choice $\alpha=\beta=1$: the eigenbasis is unique up to the two independent complex scales. Over $\mathbb{R}$ the four vectors $\Pi_+,\Pi_-,i\Pi_+,i\Pi_-$ form a real basis; the complex eigenbasis packages them in pairs, which is the natural choice because the eigenvalues are complex.

When $Q_{\blacktriangledown}=0$ the element is the complex scalar $Q_{\blacktriangle}$, the operator is $L_{\breve Q}=Q_{\blacktriangle}\,\mathrm{id}$, every nonzero vector is an eigenvector, and every complex basis is an eigenbasis. The idempotent basis is then a choice, not a consequence of $\breve Q$.

### The Properties in the Eigenbasis

The decomposition $\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-$ gives every power, every polynomial, and the inverse by the same rule: apply the function to the two eigenvalues and keep the two idempotents. The results are collected in the table.

| Quantity | In the basis $(1,j)$ | In the eigenbasis $(\Pi_+,\Pi_-)$ |
|---|---|---|
| Element $\breve Q$ | $Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | $(\lambda_+,\lambda_-)$ |
| Power $\breve Q^n$, $n\geq0$ | — | $(\lambda_+^n,\lambda_-^n)$ |
| Polynomial $f(\breve Q)$ | — | $(f(\lambda_+),f(\lambda_-))$ |
| Inverse $\breve Q^{-1}$, $Q_{\blacktriangledown}\neq0$ | $\dfrac{\breve Q_{\mathrm{ts}}}{\langle\breve Q\rangle_{\mathrm{ts}}}$ | $(\lambda_+^{-1},\lambda_-^{-1})$ |
| Reduced norm $\langle\breve Q\rangle_{\mathrm{ts}}$ | $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2$ | $\lambda_+\lambda_-$ |
| Trace | $2Q_{\blacktriangle}$ | $\lambda_++\lambda_-$ |

The eigenbasis is the basis in which the two Peirce coordinates of $\breve Q$ are the two eigenvalues.

**Nilpotents.** There are none. If $N=\nu_+\Pi_++\nu_-\Pi_-$ satisfies $N^2=0$, then $\nu_+^2=\nu_-^2=0$, and over $\mathbb{C}$ this forces $\nu_+=\nu_-=0$, hence $N=0$. The off-diagonal Peirce corners $\mathbb{B}_{\mathrm{r},+-}$ and $\mathbb{B}_{\mathrm{r},-+}$ both vanish, so there is no off-diagonal direction in which a nilpotent could live. The nilpotent regime is empty.

### The Spinor Spaces

**A spinor space of $\mathbb{B}_{\mathrm{r}}$ is a minimal nonzero ideal; the two spinor spaces are the complex lines $\mathbb{C}\Pi_+$ and $\mathbb{C}\Pi_-$, and a spinor is one complex coefficient on one of them.**

Since $\mathbb{B}_{\mathrm{r}}$ is commutative, its left, right and two-sided ideals coincide. The minimal nonzero ideals are
$$
S_+=\mathbb{B}_{\mathrm{r}}\Pi_+=\mathbb{C}\Pi_+,
\qquad
S_-=\mathbb{B}_{\mathrm{r}}\Pi_-=\mathbb{C}\Pi_-,
$$
each one-dimensional over $\mathbb{C}$, and
$$
\mathbb{B}_{\mathrm{r}}=S_+\oplus S_-.
$$
The notation $S_\pm$ is reserved for these two spaces.

A **spinor of first chirality** is an element of $S_+$,
$$
\xi_+=A_1\Pi_+,\qquad A_1\in\mathbb{C},
$$
and a **spinor of second chirality** is an element of $S_-$,
$$
\xi_-=A_2\Pi_-,\qquad A_2\in\mathbb{C}.
$$
In the eigenbasis their coordinates are
$$
\xi_+\longleftrightarrow(A_1,0),
\qquad
\xi_-\longleftrightarrow(0,A_2).
$$
The two spinor spaces are the two coordinate axes of the eigenbasis.

The element $\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-$ acts on them by
$$
\breve Q\xi_+=\lambda_+\xi_+,
\qquad
\breve Q\xi_-=\lambda_-\xi_-,
$$
so $S_+$ is the $\lambda_+$-eigenspace and $S_-$ the $\lambda_-$-eigenspace. In coordinates,
$$
A_1\longmapsto\lambda_+A_1,
\qquad
A_2\longmapsto\lambda_-A_2.
$$
A general element $\breve Q_2=\xi_++\xi_-$ is not a spinor: it is the sum of one spinor of each chirality, and its two components $\xi_+,\xi_-$ are the two summands in the direct sum.

**One complex component per chirality.** The base field is $\mathbb{C}$, so each spinor space is a one-dimensional complex vector space, of real dimension two. A spinor has a single complex component, not a pair: the two components displayed above belong to the two different chiralities. The biquaternion case is the one in which a single spinor space is two-dimensional over $\mathbb{C}$ and therefore carries a pair of complex components. The extra dimension there is supplied by the nilpotent direction $\vec\Upsilon_\pm$, which is absent here.

### The Matrix Model and the Two Columns

**In the eigenbasis the Peirce matrix of every element is diagonal, the two diagonal entries are the spinor coordinates, and the two columns are the two spinor spaces.**

Write a general element in the eigenbasis as
$$
\breve Q_2=A_1\Pi_++A_2\Pi_-,
\qquad A_1,A_2\in\mathbb{C}
$$

Its coordinates are $(A_1,A_2)$.
Assign
$$
\Pi_+\mapsto E_{11},\qquad \Pi_-\mapsto E_{22},
$$
where $E_{ij}$ is the matrix unit with $1$ in row $i$ and column $j$. Then
$$
M(\breve Q_2)=\begin{pmatrix}A_1&0\\0&A_2\end{pmatrix},
\qquad
[L_{\breve Q}]_{(\Pi_+,\Pi_-)}=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}.
$$
The two columns are the two spinor spaces:
$$
S_+=\mathbb{C}\Pi_+\longleftrightarrow\operatorname{span}\{E_{11}\}=\text{column }1,
\qquad
S_-=\mathbb{C}\Pi_-\longleftrightarrow\operatorname{span}\{E_{22}\}=\text{column }2.
$$
A spinor of first chirality $A_1\Pi_+$ is the first column $(A_1,0)^{T}$; a spinor of second chirality $A_2\Pi_-$ is the second column $(0,A_2)^{T}$. The off-diagonal entries are zero: the mixed Peirce corners vanish, and the matrix units $E_{12},E_{21}$ do not occur. The image of the Peirce model is the diagonal subalgebra of $M_2(\mathbb{C})$, isomorphic to $\mathbb{C}\times\mathbb{C}$.

In the basis $(1,j)$ the regular representation is
$$
[L_{\breve Q}]_{(1,j)}=\begin{pmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix},
$$
and the change of basis to the eigenbasis is
$$
P=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
P^{-1}=2P,
\qquad
P^{-1}[L_{\breve Q}]_{(1,j)}P=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}.
$$
The matrix $[L_{\breve Q}]_{(1,j)}$ is symmetric, and it is conformal for the complex bilinear form $G=\operatorname{diag}(1,-1)$: $[L_{\breve Q}]_{(1,j)}^{T}G[L_{\breve Q}]_{(1,j)}=\langle\breve Q\rangle_{\mathrm{ts}}G$. The eigenbasis diagonalises it. The vanishing of the off-diagonal entries is the matrix statement that the Peirce decomposition has no mixed part.

**Nilpotents in the matrix model.** Since the image of the Peirce model is the diagonal subalgebra, no nonzero nilpotent matrix is in it: a diagonal matrix with square zero is zero. The matrix units $E_{12}$ and $E_{21}$ are square-zero in $M_2(\mathbb{C})$, but they are not in the image of $\mathbb{B}_{\mathrm{r}}$. The absence is the matrix form of the reducedness of the algebra.

## Powers, Polynomial Calculus, and the Group of Units

**The eigenvalue decomposition carries the polynomial calculus, the inverse and the group isomorphism of the unit group.**

For any polynomial $f\in\mathbb{C}[X]$, the eigenvalue decomposition gives
$$
\boxed{\; f(\breve Q)=f(\lambda_+)\Pi_++f(\lambda_-)\Pi_- \;}.
$$
This follows from
$$
\breve Q^{n}=\lambda_+^{n}\Pi_++\lambda_-^{n}\Pi_-,\qquad n\geq0,
$$
with $\Pi_++\Pi_-=1$ for $n=0$, and from linearity. When $\breve Q$ is a unit, both eigenvalues are nonzero, and the formula extends to negative powers:
$$
\breve Q^{-1}=\lambda_+^{-1}\Pi_++\lambda_-^{-1}\Pi_-.
$$
The result agrees with the inverse formula of *Norm and Invertibility in the Algebra of the Reduced Biquaternions*, §*The Reduced Norm and the Invertibility Criterion*,
$$
\breve Q^{-1}=\frac{\breve Q_{\mathrm{ts}}}{\langle \breve Q\rangle_{\mathrm{ts}}},
$$
since $\breve Q_{\mathrm{ts}}=Q_-\Pi_++Q_+\Pi_-$ and $\langle \breve Q\rangle_{\mathrm{ts}}=\lambda_+\lambda_-$.

**The group of units.** The map
$$
\mathbb{B}_{\mathrm{r}}^{\times}\longrightarrow\mathbb{C}^{\times}\times\mathbb{C}^{\times},
\qquad
\breve Q\longmapsto(\lambda_+,\lambda_-)
$$
is an isomorphism of groups: multiplication is coordinatewise, and $\breve Q$ is a unit exactly when both eigenvalues are nonzero, that is, exactly when $\langle \breve Q\rangle_{\mathrm{ts}}\neq0$. The identity is $1=(1,1)$, corresponding to $\Pi_++\Pi_-$. The inverse is the componentwise inverse displayed above.

The results are collected in the table.

| Operation | Formula | Validity |
|---|---|---|
| Powers | $\breve Q^n=\lambda_+^n\Pi_++\lambda_-^n\Pi_-$ | $n\geq0$ |
| Polynomials | $f(\breve Q)=f(\lambda_+)\Pi_++f(\lambda_-)\Pi_-$ | every $f\in\mathbb{C}[X]$ |
| Inverse | $\breve Q^{-1}=\lambda_+^{-1}\Pi_++\lambda_-^{-1}\Pi_-$ | $\breve Q$ a unit |
| Unit criterion | $\breve Q\in\mathbb{B}_{\mathrm{r}}^\times\iff\lambda_+\lambda_-\neq0$ | — |
| Group of units | $\mathbb{B}_{\mathrm{r}}^\times\cong\mathbb{C}^\times\times\mathbb{C}^\times$ | — |

## The Algebraic Fibre of the Decomposition

**The eigenvalue coordinates and the basis coordinates are two linear coordinate systems on the same algebra.**

Every element of the diagonal part, which is the whole algebra, is
$$
\breve Q_{1}=\mu_+\Pi_++\mu_-\Pi_-,\qquad \mu_\pm\in\mathbb{C},
$$
and the map $(\mu_+,\mu_-)\mapsto\breve Q_2$ is a $\mathbb{C}$-linear isomorphism $\mathbb{C}^{2}\to\mathbb{B}_{\mathrm{r}}$. For $\mu_+\neq\mu_-$ this is the eigenvalue decomposition of $\breve Q_2$, with the eigenprojections $\Pi_\pm$ and the eigenvalue data $(\mu_+,\mu_-)$. For $\mu_+=\mu_-=a$ the element is the scalar $a$, with the one-term decomposition $a\cdot1$.

The unordered spectrum is the image of the map $(\mu_+,\mu_-)\mapsto\{\mu_+,\mu_-\}$. Off the diagonal it is two-to-one: the two preimages of $\{\mu_+,\mu_-\}$ are $\mu_+\Pi_++\mu_-\Pi_-$ and $\mu_-\Pi_++\mu_+\Pi_-$, which differ by
$$
(\mu_+-\mu_-)(\Pi_+-\Pi_-)=(\mu_+-\mu_-)j\neq0.
$$
The ambiguity is exactly the exchange of the two labels.

### The Coordinate Change to Basis Coordinates

The coordinate change to the basis $1,j$ is
$$
\breve Q_2=\frac{\mu_++\mu_-}{2}+\frac{\mu_+-\mu_-}{2}j=Q_{\blacktriangle}+jQ_{\blacktriangledown},
\qquad
Q_{\blacktriangle}=\frac{\mu_++\mu_-}{2},
\quad
Q_{\blacktriangledown}=\frac{\mu_+-\mu_-}{2}.
$$
The map $(\mu_+,\mu_-)\mapsto(Q_{\blacktriangle},Q_{\blacktriangledown})$ is a $\mathbb{C}$-linear isomorphism of $\mathbb{C}^{2}$; the two coordinate systems are the eigenvalue coordinates and the basis coordinates on the same algebra. They are compared in the table.

| Coordinate system | Coordinates | Element | Eigenvalues |
|---|---|---|---|
| Eigenvalue coordinates | $(\mu_+,\mu_-)$ | $\breve Q_2=\mu_+\Pi_++\mu_-\Pi_-$ | $\mu_+,\mu_-$ |
| Basis coordinates | $(Q_{\blacktriangle},Q_{\blacktriangledown})$ | $\breve Q_2=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | $\lambda_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown}$ |
| Change | $\mu_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown}$; $Q_{\blacktriangle}=(\mu_++\mu_-)/2$, $Q_{\blacktriangledown}=(\mu_+-\mu_-)/2$ | — | — |

### The Lattice of Eigenvalue Data

If the eigenvalue coordinates are restricted to the Gaussian integers, $\mu_\pm\in\mathbb{Z}[i]$, the basis-coordinate pair $(Q_{\blacktriangle},Q_{\blacktriangledown})$ runs over the lattice

$$
L=\left\{\left(\frac{m}{2},\frac{n}{2}\right):\ m,n\in\mathbb{Z}[i],\ m\equiv n\pmod2\right\},
$$

where $m\equiv n\pmod2$ means that $m-n$ is divisible by $2$ in $\mathbb{Z}[i]$. Indeed, for $\mu_\pm\in\mathbb{Z}[i]$ one has

$$
Q_{\blacktriangle}=\frac{\mu_++\mu_-}{2}=\frac{m}{2},
\qquad
Q_{\blacktriangledown}=\frac{\mu_+-\mu_-}{2}=\frac{n}{2},
$$

with $m=\mu_++\mu_-$ and $n=\mu_+-\mu_-$. Then $m-n=2\mu_-$, so $m\equiv n\pmod2$; conversely, every pair $(m,n)$ of the same parity comes from the Gaussian integers $\mu_\pm=(m\pm n)/2$. The parity condition reflects the fact that the idempotents mix the $1$ and $j$ directions: the Gaussian-integral shifts in the eigenvalue coordinates do not map to the rectangular lattice $\mathbb{Z}[i]^2$ in the basis coordinates. For example, $\mu_+=\mu_-=1$ gives $(Q_{\blacktriangle},Q_{\blacktriangledown})=(1,0)$ and $\breve Q=1$, while $\mu_+=2$, $\mu_-=0$ gives $(Q_{\blacktriangle},Q_{\blacktriangledown})=(1,1)$ and $\breve Q=1+j=2\Pi_+$, a zero divisor.

The lattice $L$ is a coordinate lattice, not an intrinsic invariant of $\breve Q$. The exponential kernel is the sublattice $2\pi i\mathbb{Z}^2$ of the eigenvalue coordinates; in the basis coordinates it is

$$
\{\pi i m+\pi i n j:\ m,n\in\mathbb{Z},\ m\equiv n\pmod2\},
$$

the parity-matched lattice, the analogue of the biquaternion lattice of the same name.

### The Split-Complex Plane

**On the real plane $\mathbb{R}\{1,j\}$ the decomposition reduces to the split-complex decomposition.**

Suppose $Q_{\blacktriangle},Q_{\blacktriangledown}\in\mathbb{R}$. Then $\lambda_+=Q_{\blacktriangle}+Q_{\blacktriangledown}$ and $\lambda_-=Q_{\blacktriangle}-Q_{\blacktriangledown}$ are real, and the decomposition is the split-complex decomposition of *Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number* read in the real plane $\mathbb{R}\{1,j\}$. With $q=Q_{\blacktriangle}$ and $q'=Q_{\blacktriangledown}$,
$$
\lambda_+=q+q',\qquad \lambda_-=q-q',
\qquad
\breve Q=q+jq'=\lambda_+\Pi_++\lambda_-\Pi_-.
$$
The reduced norm is $\langle\breve Q\rangle_{\mathrm{ts}}=q^2-q'^2=\lambda_+\lambda_-$. The real plane is a real subalgebra of $\mathbb{B}_{\mathrm{r}}$ isomorphic to the split-complex algebra $\mathbb{D}=\mathbb{R}[x]/(x^2-1)$, and on it the eigenvalue decomposition, the Peirce decomposition and the spectral calculus reduce to those of the split-complex article.

## Degenerate Regimes

An eigenvalue decomposition with distinct eigenvalues requires $Q_{\blacktriangledown}\neq0$, equivalently $\lambda_+\neq\lambda_-$. The scalar and zero-divisor cases remain; the Jordan and nilpotent regimes of the biquaternion case are absent, because the algebra is reduced.

| Regime | Condition | Spectrum | Eigenvalue decomposition |
|---|---|---|---|
| Distinct | $Q_{\blacktriangledown}\neq0$, $\lambda_+\lambda_-\neq0$ | $\{\lambda_+,\lambda_-\}$ | $\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-$ |
| Zero divisor | $Q_{\blacktriangledown}\neq0$, $\lambda_+\lambda_-=0$ | $\{2Q_{\blacktriangle},0\}$ | $\breve Q=2Q_{\blacktriangle}\Pi_\sigma$ |
| Scalar | $Q_{\blacktriangledown}=0$ | $\{Q_{\blacktriangle}\}$ | $\breve Q=Q_{\blacktriangle}\cdot1$ |
| Jordan | absent: the algebra is reduced | — | — |
| Nilpotent | absent: only $\breve Q=0$ | — | — |

### The Scalar Regime

**A scalar element has a repeated eigenvalue, the one-term eigenprojection $1$, and a unique two-term refinement.**

Suppose $Q_{\blacktriangledown}=0$. Then
$$
\lambda_+=\lambda_-=Q_+=Q_-=Q_{\blacktriangle},
\qquad
\breve Q=\lambda_+\cdot1=Q_{\blacktriangle}\cdot1,
$$
a complex scalar. The characteristic polynomial is $(X-\lambda_+)^{2}=(X-Q_{\blacktriangle})^{2}$ and the minimal polynomial is $X-\lambda_+=X-Q_{\blacktriangle}$; the element is central and semisimple, with the single eigenvalue $\lambda_+=Q_{\blacktriangle}$ and eigenprojection $1$. In the sense of the general definition the eigenvalue decomposition is the one-term writing
$$
\breve Q=\lambda_+\cdot1=Q_{\blacktriangle}\cdot1.
$$

A two-term writing with the repeated coefficient is
$$
\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-=Q_{\blacktriangle}\Pi_++Q_{\blacktriangle}\Pi_-.
$$
It is unique, because $\{\Pi_+,\Pi_-\}$ is the only nontrivial complementary pair of idempotents: the idempotents of the algebra are $0,1,\Pi_+,\Pi_-$. This is a difference from the biquaternion scalar regime, where every complete orthogonal pair gives a two-term writing and the pair is not determined by the element; it agrees with the split-complex scalar regime (*Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number*, §*The Scalar Regime*).

### The Zero-Divisor Regime

**A nonzero zero divisor has one zero eigenvalue and one nonzero eigenvalue, and it admits an eigenvalue decomposition even though it is not a unit.**

Suppose $\langle \breve Q\rangle_{\mathrm{ts}}=\lambda_+\lambda_-=Q_+Q_-=0$ with $\breve Q\neq0$. Then one eigenvalue is zero and the other is nonzero. If $\lambda_+=0$, then $\lambda_-=Q_-\neq0$ and
$$
\breve Q=0\cdot\Pi_++\lambda_-\Pi_-=\lambda_-\Pi_-,
\qquad
(\lambda_+,\lambda_-)=(0,Q_-);
$$
if $\lambda_-=0$, then $\lambda_+=Q_+\neq0$ and
$$
\breve Q=\lambda_+\Pi_++0\cdot\Pi_-=\lambda_+\Pi_+,
\qquad
(\lambda_+,\lambda_-)=(Q_+,0).
$$
In either case the eigenvalues are distinct, and the displayed writing is a genuine eigenvalue decomposition, even though $\breve Q$ is not a unit: the nonzero eigenvalue multiplies its eigenprojection and the zero eigenvalue multiplies the other. The element is a nonzero scalar multiple of an idempotent, and the minimal polynomial is $X(X-\lambda_-)$ in the first case and $X(X-\lambda_+)$ in the second; it is squarefree. This is the zero-divisor regime of the split-complex case, with $\mathbb{R}$ replaced by $\mathbb{C}$. This regime is distinct from the biquaternion nilpotent regime, which has no analogue here.

### The Nilpotent Regime

**There are no nonzero nilpotent elements, so there is no Jordan-block regime.**

The algebra is $\mathbb{C}\times\mathbb{C}$, a product of fields, hence **reduced** (no nonzero nilpotents). If $\breve Q^{2}=0$, then in the idempotent coordinates $\lambda_+^{2}=\lambda_-^{2}=0$, so $\lambda_+=\lambda_-=0$ and $\breve Q=0$. Therefore the nilpotent regime of the biquaternion case has no analogue. Every element is semisimple, and the only failure of distinct eigenvalues is the scalar case $Q_{\blacktriangledown}=0$.

## Remarks

1. **Relation to the model algebra.** Under $\mathbb{B}_{\mathrm{r}}\cong\mathbb{C}\times\mathbb{C}$, the eigenvalue decomposition is literally the product decomposition: $\lambda_+=Q_+$ and $\lambda_-=Q_-$ are the two complex components, $\Pi_+$ and $\Pi_-$ are the standard minimal central idempotents, and the Lagrange–Sylvester formulas are the interpolation formulas in the product algebra.

2. **Centrality and the Peirce decomposition.** The idempotents $\Pi_\pm$ are central, so the Peirce decomposition is a direct sum of two-sided ideals and the off-diagonal components vanish. This is the commutative shadow of the biquaternion Peirce decomposition, and it is structurally identical to the split-complex case with $\mathbb{R}$ replaced by $\mathbb{C}$.

3. **Uniqueness and labelling.** The pair $\{\Pi_+,\Pi_-\}$ is the unique nontrivial complementary pair of idempotents in the algebra. The labels are exchanged by the tessarine sign $j\mapsto-j$, which sends $Q_{\blacktriangledown}$ to $-Q_{\blacktriangledown}$ and $\lambda_+\leftrightarrow\lambda_-$. There is no non-discrete family of eigenprojections and no branch ambiguity: the decomposition is a direct-product decomposition.

4. **Degenerate regimes.** The eigenvalue decomposition with distinct eigenvalues requires $Q_{\blacktriangledown}\neq0$. The scalar regime has a repeated eigenvalue, the eigenprojection $1$, and a unique two-term refinement. The zero-divisor regime has one eigenvalue equal to $0$ and still admits an eigenvalue decomposition. There is no nilpotent regime, because the algebra is reduced.

## Summary

For a reduced biquaternion with $Q_{\blacktriangledown}\neq0$, the eigenvalue decomposition is the writing
$$
\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-,
\qquad
\lambda_+=Q_+=Q_{\blacktriangle}+Q_{\blacktriangledown},
\quad
\lambda_-=Q_-=Q_{\blacktriangle}-Q_{\blacktriangledown},
\qquad
\Pi_\pm=\tfrac12(1\pm j).
$$
The eigenvalues are distinct complex numbers, the idempotents are primitive, orthogonal, complete and central, and they are the eigenprojections. The decomposition is unique up to the exchange of the two labels by the tessarine sign $j\mapsto-j$.

### Main Results

| Result | Expression |
|---|---|
| Spectrum | $\sigma(\breve Q)=\{\lambda_+,\lambda_-\}=\{Q_+,Q_-\}$ |
| Characteristic polynomial | $p_{\breve Q}(X)=X^2-2Q_{\blacktriangle}X+\langle\breve Q\rangle_{\mathrm{ts}}=(X-\lambda_+)(X-\lambda_-)$ |
| Distinctness | $\lambda_+\neq\lambda_-\iff Q_{\blacktriangledown}\neq0$ |
| Eigenprojections | $\Pi_\pm=\tfrac12(1\pm j)$ |
| Eigenvalue decomposition | $\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-=(Q_{\blacktriangle}+Q_{\blacktriangledown})\Pi_++(Q_{\blacktriangle}-Q_{\blacktriangledown})\Pi_-$ |
| Peirce decomposition | $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$ |
| Eigenbasis | $(\Pi_+,\Pi_-)$, with eigenvalues $\lambda_+,\lambda_-$ |
| Matrix model | $M(\breve Q_2)=\operatorname{diag}(A_1,A_2)$; the regular matrix is $\begin{pmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix}$ |
| Nilpotents | none; the algebra is reduced, so $N^2=0$ implies $N=0$ |
| Spinor spaces | $S_\pm=\mathbb{C}\Pi_\pm$, the two minimal ideals; spinors $A_1\Pi_+$ and $A_2\Pi_-$ |
| Polynomial calculus | $f(\breve Q)=f(\lambda_+)\Pi_++f(\lambda_-)\Pi_-$ |
| Group of units | $\mathbb{B}_{\mathrm{r}}^\times\cong\mathbb{C}^\times\times\mathbb{C}^\times$ |

### Regimes

The zero-divisor row is a subcase of the distinct row, separated because one eigenvalue vanishes; the scalar row includes $\breve Q=0$.

| Regime | Condition | Spectrum | Minimal polynomial | Eigenvalue decomposition |
|---|---|---|---|---|
| Distinct | $Q_{\blacktriangledown}\neq0$, $\lambda_+\lambda_-\neq0$ | $\{\lambda_+,\lambda_-\}$, distinct | $(X-\lambda_+)(X-\lambda_-)$ | $\breve Q=\lambda_+\Pi_+ + \lambda_-\Pi_-$ |
| Zero divisor | $Q_{\blacktriangledown}\neq0$, $\lambda_+\lambda_-=0$ | $\{\lambda_\sigma,\lambda_{-\sigma}\}=\{2Q_{\blacktriangle},0\}$ | $X(X-2Q_{\blacktriangle})$ | $\breve Q=2Q_{\blacktriangle}\Pi_\sigma + 0\cdot\Pi_{-\sigma}$ |
| Scalar | $Q_{\blacktriangledown}=0$ | $\{Q_{\blacktriangle}\}$ | $X-Q_{\blacktriangle}$ | $\breve Q=Q_{\blacktriangle}\cdot1$; refinement $Q_{\blacktriangle}\Pi_+ + Q_{\blacktriangle}\Pi_-$ |
| Jordan | absent: the algebra is reduced | — | — | — |
| Nilpotent | absent; only $\breve Q=0$ | — | — | — |

The Peirce decomposition relative to $\Pi_+$ has corners $\mathbb{B}_{\sigma\tau}=\Pi_\sigma\mathbb{B}_{\mathrm{r}}\Pi_\tau$. Its off-diagonal corners vanish, and its diagonal part is the whole algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$. The element $\breve Q$ has the diagonal coordinates $\lambda_+,\lambda_-$ and zero mixed coordinates. The centraliser of $\breve Q$ is the whole algebra; the subalgebra $\mathbb{C}[\breve Q]$ is the whole algebra exactly when $\breve Q$ is not scalar. The polynomial calculus, the inverse and the group isomorphism $\mathbb{B}_{\mathrm{r}}^{\times}\cong\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ all follow from the decomposition. There is no Jordan or nilpotent regime, because the algebra is a product of fields.

### Comparison with the Neighbouring Cases

The table compares the decomposition across the three algebras; in the biquaternion column, the distinct case is $Q_x^2+Q_y^2+Q_z^2\neq0$, $\vec\Xi=-i\vec Q/\sqrt{Q_x^2+Q_y^2+Q_z^2}$, and $\vec\Upsilon_\pm$ are the two nilpotents of the eigenbasis, one in each mixed corner.

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
| Coordinates of a general element in the eigenbasis | $(a_1,a_2)$ | $(A_1,A_2)$ | $(a_{11},a_{12},a_{21},a_{22})$ |
| Nilpotents in the eigenbasis | none | none | $\vec\Upsilon_\pm$ in the two mixed corners |
| Spinor spaces | $S_\pm=\mathbb{R}\Pi_\pm$, real lines | $S_\pm=\mathbb{C}\Pi_\pm$, complex lines | $S_\pm=\mathbb{B}\tilde\Pi_\pm\cong\mathbb{C}^2$, complex planes |
| Spinor coordinates | one real coefficient per chirality | one complex coefficient per chirality | two complex coefficients per chirality |
| Action of $Q$ on a spinor | scalar: $\lambda_+$ on $S_+$, $\lambda_-$ on $S_-$ | scalar: $\lambda_+$ on $S_+$, $\lambda_-$ on $S_-$ | $\lambda_+$ on the first coordinate, $\lambda_-$ on the second |
| Unit group | $\cong\mathbb{R}^\times\times\mathbb{R}^\times$ | $\cong\mathbb{C}^\times\times\mathbb{C}^\times$ | $\mathbb{B}^\times$; eigenvalue map surjective, not injective, not a homomorphism |

Read down a column for one algebra and across a row for one concept. The rows down to the eigenprojections follow one pattern; the rows below them record where the algebras part: whether the idempotents depend on the element and whether they are central, the two mixed square-zero lines of the biquaternion Peirce decomposition, and the biquaternion unit group, which is no longer a product. The last rows record the spinor content: one real coefficient per chirality for the split-complex algebra, one complex coefficient per chirality for the reduced biquaternion algebra, and two complex coefficients per chirality, forming a complex plane, for the biquaternion algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ | Reduced biquaternion algebra, dimension $4$ over $\mathbb{R}$, $2$ over $\mathbb{C}$ |
| $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | General reduced biquaternion, $Q_{\blacktriangle},Q_{\blacktriangledown}\in\mathbb{C}$ |
| $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$, $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$ | Complex basis coordinates |
| $\breve Q_{\mathrm{ts}}=Q_{\blacktriangle}-jQ_{\blacktriangledown}=Q_-\Pi_++Q_+\Pi_-$ | Tessarine conjugate |
| $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=\lambda_+\lambda_-$ | Reduced norm and determinant |
| $\operatorname{tr}(\breve Q)=2Q_{\blacktriangle}=\lambda_++\lambda_-$ | Reduced trace |
| $\Pi_\pm=\tfrac12(1\pm j)$ | The two nontrivial central idempotents, the eigenprojections |
| $Q_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown}$ | Idempotent coordinates; equal to $\lambda_\pm$ |
| $\lambda_\pm=Q_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown}$ | The values of the eigenvalues |
| $\sigma(\breve Q)=\{\lambda_+,\lambda_-\}=\{Q_+,Q_-\}$ | Spectrum |
| $p_{\breve Q}(X)=X^{2}-2Q_{\blacktriangle}X+\langle \breve Q\rangle_{\mathrm{ts}}$ | Characteristic polynomial, $(X-\lambda_+)(X-\lambda_-)$ |
| $L_{\breve Q}=R_{\breve Q}$ | Multiplication operator $X\mapsto\breve QX$; eigenvalues $\lambda_+,\lambda_-$ in the eigenbasis |
| $[L_{\breve Q}]_{(1,j)}$ | Matrix of $L_{\breve Q}$ in the basis $(1,j)$, $\begin{pmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix}$ |
| $[L_{\breve Q}]_{(\Pi_+,\Pi_-)}$ | Diagonal matrix of $L_{\breve Q}$ in the eigenbasis, $\operatorname{diag}(\lambda_+,\lambda_-)$ |
| $M(\breve Q_2)$ | Peirce matrix of a general element, $\operatorname{diag}(A_1,A_2)$ |
| $E_{ij}$ | Matrix units of the $2\times2$ model |
| $A_1,A_2$ | Spinor coordinates on $S_+$ and $S_-$, the two diagonal entries of the matrix in the eigenbasis |
| $\alpha,\beta$ | Scales of the eigenbasis $(\alpha\Pi_+,\beta\Pi_-)$ |
| $S_\pm=\mathbb{B}_{\mathrm{r}}\Pi_\pm=\mathbb{C}\Pi_\pm$ | The two spinor spaces, the two minimal ideals (complex lines) |
| $\mathbb{B}_{\sigma\tau}=\Pi_\sigma\mathbb{B}_{\mathrm{r}}\Pi_\tau$ | Peirce corners of the pair $\Pi_\pm$ |
| $\mathbb{C}[\breve Q]=\operatorname{span}_{\mathbb{C}}\{1,\breve Q\}$ | Subalgebra generated by $\breve Q$ |
| $C(\breve Q)=\mathbb{B}_{\mathrm{r}}$ | Centraliser of $\breve Q$ |
| $\mathbb{B}_{\mathrm{r}}^{\times}\cong\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ | Group of units, the coordinatewise nonzero pairs |
| $L=\{(m/2,n/2):m,n\in\mathbb{Z}[i],\ m\equiv n\pmod2\}$ | Lattice of basis-coordinate data for Gaussian-integral eigenvalue coordinates $\mu_\pm\in\mathbb{Z}[i]$ |
| $\breve Q_2=A_1\Pi_++A_2\Pi_-$ | General element in the spinor coordinates, with matrix $\operatorname{diag}(A_1,A_2)$ |
| $\breve Q_2=\mu_+\Pi_++\mu_-\Pi_-$ | General element in the eigenvalue coordinates |
| $\mu$ | A test scalar in the definition of an eigenvalue |
| $\mu_\pm$ | Eigenvalue coordinates on the diagonal part |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for idempotents, Peirce decompositions and the structure of finite-dimensional algebras.
- G. Baley Price, *An Introduction to Multicomplex Spaces and Functions* (Marcel Dekker, 1991), for the idempotent decomposition and the coordinatewise product of the multicomplex algebra.
- M. Elena Luna-Elizarrarás, Michael Shapiro, Daniele C. Struppa and Adrian Vajiac, *Bicomplex Holomorphic Functions* (Birkhäuser, 2015), for the commutative two-component algebra and its idempotent coordinates.
- The corpus articles: [The Eigenvalue Decomposition of an Element](the-eigenvalue-decomposition-of-an-element.html), [The Lagrange–Sylvester Eigenprojector Formula](the-lagrange-sylvester-eigenprojector-formula.html), [The Centraliser and the Diagonal Peirce Part](the-centraliser-and-the-diagonal-peirce-part.html), [Off-Diagonal Peirce Components and Noncentral Idempotents](off-diagonal-peirce-components-and-noncentral-idempotents.html), [Reduced Biquaternion Spectral Theory](reduced-biquaternion-spectral-theory.html), [Square Roots of One and the Idempotents of the Algebra of the Reduced Biquaternions](square-roots-of-one-and-the-idempotents-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), [Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions](ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), [Norm and Invertibility in the Algebra of the Reduced Biquaternions](norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.html), [The Group of Units of the Algebra of the Reduced Biquaternions](the-group-of-units-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), [Zero Divisors of the Algebra of the Reduced Biquaternions](zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), [The Biquaternion Eigenvalue Decomposition](the-biquaternion-eigenvalue-decomposition.html), [Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number](eigenvalue-decomposition-and-eigenbasis-of-a-split-complex-number.html) and [Conventions in Mathematics](conventions-in-mathematics.html).
