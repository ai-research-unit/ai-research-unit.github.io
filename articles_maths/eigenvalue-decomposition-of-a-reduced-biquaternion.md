# __Eigenvalue Decomposition of a Reduced Biquaternion__

## Introduction

The reduced biquaternion algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$ is commutative, associative and unital. It is four-dimensional over $\mathbb{R}$ and two-dimensional over $\mathbb{C}$, with real basis $1,i,j,ij$ and complex basis $1,j$; the multiplication is fixed by $i^{2}=-1$, $j^{2}=1$ and $ij=ji$. This article reads the **eigenvalue decomposition** of a reduced biquaternion: the writing of $\breve Q$ as a complex linear combination of the two idempotents of the complete orthogonal pair $\Pi_+,\Pi_-$, with the eigenvalues as coefficients. The general definition and the existence and uniqueness theorems are those of *The Eigenvalue Decomposition of an Element*. The reduced biquaternion content is that, for a non-scalar element, the eigenprojections are the standard idempotents $\Pi_\pm$, that they are central and independent of the element, and that the Peirce decomposition of *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions* relative to either of them is the decomposition of the whole algebra.

**Placement and conventions.** The article follows *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions* in the Advanced Properties section and precedes *The Group of Units of the Algebra of the Reduced Biquaternions*. The notation is fixed in *Conventions in Mathematics*: the general element is $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$, with $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$ and $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$ complex; the idempotents are $\Pi_\pm=\tfrac12(1\pm j)$; and the idempotent coordinates are $Q_+=Q_{\blacktriangle}+Q_{\blacktriangledown}$ and $Q_-=Q_{\blacktriangle}-Q_{\blacktriangledown}$, so that $\breve Q=Q_+\Pi_++Q_-\Pi_-$. The reduced norm is $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=Q_+Q_-$. The spectrum and the characteristic polynomial are those of *Reduced Biquaternion Spectral Theory*, §*The Spectrum of an Element*, and the spectral projections are those of its §*Eigenspaces and Their Dimensions*; the idempotents are those of *Square Roots of One and the Idempotents of the Algebra of the Reduced Biquaternions*, §*The Idempotents*; the Peirce decomposition is that of *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*, §*The Peirce Decomposition*; the reduced norm and the invertibility criterion are those of *Norm and Invertibility in the Algebra of the Reduced Biquaternions*, §*The Reduced Norm and the Invertibility Criterion*; and the unit group is that of *The Group of Units of the Algebra of the Reduced Biquaternions*, §*The Group and Its Structure*.

**Scope.** The article proves the eigenvalue decomposition in the regime of distinct eigenvalues, identifies its eigenprojections with $\Pi_\pm$, reads the decomposition as the Peirce decomposition relative to $\Pi_+$, and treats the two degenerate regimes: the scalar element, where the eigenvalue is repeated, and the zero divisor, where one eigenvalue vanishes. The nilpotent regime of the biquaternion case is absent, because the algebra is reduced.

## The Spectrum and the Characteristic Polynomial

**Definition.** Let $\breve Q\in\mathbb{B}_{\mathrm{r}}$. A complex scalar $\lambda$ is an **eigenvalue** of $\breve Q$ if $\breve Q-\lambda 1$ is not a unit in $\mathbb{B}_{\mathrm{r}}$; the set of eigenvalues is the **spectrum** $\sigma(\breve Q)$. This is the definition of *The Eigenvalue Decomposition of an Element*, §*The Eigenvalues of an Element*.

**Theorem (the spectrum is the coordinate pair).** The spectrum of $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ is
$$
\sigma(\breve Q)=\{Q_+,Q_-\}=\{Q_{\blacktriangle}+Q_{\blacktriangledown},\,Q_{\blacktriangle}-Q_{\blacktriangledown}\}.
$$

*Proof.* In the idempotent coordinates,
$$
\breve Q-\lambda 1=(Q_+-\lambda)\Pi_++(Q_--\lambda)\Pi_-.
$$
By the criterion of *Norm and Invertibility in the Algebra of the Reduced Biquaternions*, §*The Reduced Norm and the Invertibility Criterion*, an element is a unit exactly when both idempotent coordinates are nonzero. Hence $\breve Q-\lambda 1$ is not a unit exactly when $Q_+-\lambda=0$ or $Q_--\lambda=0$, that is, when $\lambda=Q_+$ or $\lambda=Q_-$.

The definition is the algebraic one; it agrees with the spectrum of left multiplication computed in *Reduced Biquaternion Spectral Theory*, §*The Spectrum of an Element*, because the algebra is commutative and the coefficients are complex.

**Characteristic polynomial.** By *Reduced Biquaternion Spectral Theory*, §*The Spectrum of an Element*, the characteristic polynomial of the left multiplication is
$$
\chi_{\breve Q}(X)=X^{2}-\operatorname{tr}(\breve Q)X+\det(\breve Q)=(X-Q_+)(X-Q_-),
$$
with
$$
\operatorname{tr}(\breve Q)=2Q_{\blacktriangle}=Q_++Q_-,\qquad
\det(\breve Q)=\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=Q_+Q_-.
$$
The discriminant is
$$
(Q_+-Q_-)^{2}=(2Q_{\blacktriangledown})^{2}=4Q_{\blacktriangledown}^{2},
$$
so the eigenvalues are distinct exactly when $Q_{\blacktriangledown}\neq0$.

**Minimal polynomial.** When $Q_{\blacktriangledown}\neq0$, the characteristic polynomial is squarefree and is the minimal polynomial. When $Q_{\blacktriangledown}=0$, the element is the complex scalar $Q_{\blacktriangle}$ and the minimal polynomial is $X-Q_{\blacktriangle}$. In the zero-divisor regime $Q_+Q_-=0$ with $\breve Q\neq0$, one coordinate is zero and the other is nonzero, and the minimal polynomial is $X(X-Q_\pm)$, where $Q_\pm$ denotes the nonzero eigenvalue. In every case the minimal polynomial is squarefree, so every element is semisimple.

**Real coordinates.** In the real basis $1,i,j,ij$ the two eigenvalues read
$$
Q_+=(q_{\blacktriangle}+q_{\blacktriangledown})+i(q'_{\blacktriangle}+q'_{\blacktriangledown}),
\qquad
Q_-=(q_{\blacktriangle}-q_{\blacktriangledown})+i(q'_{\blacktriangle}-q'_{\blacktriangledown}).
$$

## The Eigenprojections

**The eigenprojections of a non-scalar reduced biquaternion are the two fixed central idempotents $\Pi_\pm$.**

By *Square Roots of One and the Idempotents of the Algebra of the Reduced Biquaternions*, §*The Two Nontrivial Idempotents*, the two nontrivial idempotents are
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
\breve Q\Pi_+=Q_+\Pi_+,\qquad \breve Q\Pi_-=Q_-\Pi_-.
$$
Indeed, writing $\breve Q=Q_+\Pi_++Q_-\Pi_-$,
$$
(Q_+\Pi_++Q_-\Pi_-)\Pi_+=Q_+\Pi_+^{2}+Q_-\Pi_-\Pi_+=Q_+\Pi_+,
$$
since $\Pi_+^{2}=\Pi_+$ and $\Pi_-\Pi_+=0$; the computation with $\Pi_-$ is the same.

Equivalently, by the Lagrange–Sylvester eigenprojector formula of *The Lagrange–Sylvester Eigenprojector Formula*, §*The Eigenprojector Formula*,
$$
\Pi_+=\frac{\breve Q-Q_-}{Q_+-Q_-},\qquad
\Pi_-=\frac{\breve Q-Q_+}{Q_--Q_+},\qquad
Q_+-Q_-=2Q_{\blacktriangledown}.
$$
The formula applies when $Q_{\blacktriangledown}\neq0$; it exhibits $\Pi_\pm$ as polynomials in $\breve Q$. When $Q_{\blacktriangledown}=0$ the denominator vanishes and the formula does not apply.

**Independence of the element.** The formulae collapse to the fixed idempotents $\Pi_\pm$: the eigenprojections do not depend on $\breve Q$. This is the structural difference from the biquaternion case, where the eigenprojections are the idempotents of the pure root $\vec\Xi=-i\vec Q/B$ of the vector part and therefore vary with $\tilde Q$ (*Eigenvalue Decomposition of a Biquaternion*, §*The Eigenprojections*). Here the pair $\Pi_+,\Pi_-$ is fixed for the whole algebra, and the dependence on the element lies in the eigenvalues alone.

## The Eigenvalue Decomposition

**Every reduced biquaternion with distinct eigenvalues is the complex linear combination of the two fixed idempotents with its eigenvalues as coefficients.**

Summing the two eigenvalue relations gives
$$
\boxed{\ \breve Q=Q_+\Pi_++Q_-\Pi_-\ }.
$$
Equivalently, in the basis $1,j$,
$$
\breve Q=(Q_{\blacktriangle}+Q_{\blacktriangledown})\Pi_++(Q_{\blacktriangle}-Q_{\blacktriangledown})\Pi_-=Q_{\blacktriangle}+jQ_{\blacktriangledown}.
$$

This is an eigenvalue decomposition in the sense of *The Eigenvalue Decomposition of an Element*, §*The Eigenvalue Decomposition*: the coefficients $Q_\pm$ are distinct when $Q_{\blacktriangledown}\neq0$, the idempotents $\Pi_\pm$ are nonzero, orthogonal and complete, and they are the eigenprojections.

Under left multiplication in the basis $1,j$, the matrix is
$$
\mathsf{M}_{L}(\breve Q)=\begin{pmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix},
$$
and the decomposition is the diagonalisation
$$
P^{-1}\mathsf{M}_{L}(\breve Q)P=\operatorname{diag}(Q_+,Q_-),
\qquad
P=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
P^{-1}=\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
$$

**Uniqueness.** By the uniqueness theorem of *The Eigenvalue Decomposition of an Element*, §*Uniqueness*, an element with distinct eigenvalues has a unique eigenprojection attached to each eigenvalue. Here the two eigenprojections are $\Pi_\pm$, and they are fixed for the whole algebra. The unordered pair $\{Q_+,Q_-\}$ is the spectrum and is determined by $\breve Q$; the ordered pair is determined once the labelling $\Pi_+,\Pi_-$ is fixed. The only ambiguity is the exchange of the two labels by the tessarine sign $j\mapsto-j$, which sends $\Pi_+\leftrightarrow\Pi_-$ and $Q_+\leftrightarrow Q_-$. There is no continuous family of idempotents and no branch choice.

**Semisimplicity.** Since $Q_+\neq Q_-$, the minimal polynomial is squarefree and $\breve Q$ is semisimple. The decomposition is the diagonalisation of $\breve Q$ with respect to the central idempotents $\Pi_\pm$. When $Q_+=Q_-$, the element is scalar and the spectrum is a single value; the eigenvalue decomposition then has one term, as §*Degenerate Regimes* explains.

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
The two lines are the minimal ideals of *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*, §*The Two-Sided Ideals*, so $\Pi_\pm$ are primitive idempotents.

On $\breve Q$ the Peirce decomposition reads
$$
\breve Q=Q_+\Pi_++Q_-\Pi_-,
$$
with zero mixed components. The eigenvalue decomposition is therefore the Peirce decomposition read on the element: the element lies in the diagonal part, and its two diagonal Peirce coordinates are its eigenvalues.

By *The Centraliser and the Diagonal Peirce Part*, §*The theorem*, the diagonal part is the centraliser of $\breve Q$. Here both are the whole algebra:
$$
C(\breve Q)=\mathbb{B}_{\mathrm{r}}
$$
for every $\breve Q$, because the algebra is commutative. The subalgebra generated by $\breve Q$ is $\mathbb{C}[\breve Q]=\operatorname{span}_{\mathbb{C}}\{1,\breve Q\}$; it equals the whole algebra when $Q_{\blacktriangledown}\neq0$, and it is the scalar line $\mathbb{C}\cdot1$ when $Q_{\blacktriangledown}=0$. This is the commutative shadow of the biquaternion Peirce decomposition: there the idempotents are noncentral, the mixed corners are nonzero, and the diagonal part is only the centraliser $\mathbb{C}[\tilde Q]$ (*Eigenvalue Decomposition of a Biquaternion*, §*The Peirce Decomposition Relative to the Eigenprojection*).

## Powers, Polynomial Calculus, and the Group of Units

**The eigenvalue decomposition carries the polynomial calculus, the inverse and the group isomorphism of the unit group.**

For any polynomial $f\in\mathbb{C}[X]$, the eigenvalue decomposition gives
$$
f(\breve Q)=f(Q_+)\Pi_++f(Q_-)\Pi_-.
$$
This follows from
$$
\breve Q^{n}=Q_+^{n}\Pi_++Q_-^{n}\Pi_-,\qquad n\geq0,
$$
with $\Pi_++\Pi_-=1$ for $n=0$, and from linearity. When $\breve Q$ is a unit, both eigenvalues are nonzero, and the formula extends to negative powers:
$$
\breve Q^{-1}=Q_+^{-1}\Pi_++Q_-^{-1}\Pi_-.
$$
The result agrees with the inverse formula of *Norm and Invertibility in the Algebra of the Reduced Biquaternions*, §*The Reduced Norm and the Invertibility Criterion*,
$$
\breve Q^{-1}=\frac{\breve Q_{\mathrm{ts}}}{\langle \breve Q\rangle_{\mathrm{ts}}},
$$
since $\breve Q_{\mathrm{ts}}=Q_-\Pi_++Q_+\Pi_-$ and $\langle \breve Q\rangle_{\mathrm{ts}}=Q_+Q_-$.

**The group of units.** The map
$$
\mathbb{B}_{\mathrm{r}}^{\times}\longrightarrow\mathbb{C}^{\times}\times\mathbb{C}^{\times},
\qquad
\breve Q\longmapsto(Q_+,Q_-)
$$
is an isomorphism of groups: multiplication is coordinatewise, and $\breve Q$ is a unit exactly when both eigenvalues are nonzero, that is, exactly when $\langle \breve Q\rangle_{\mathrm{ts}}\neq0$. The identity is $1=(1,1)$, corresponding to $\Pi_++\Pi_-$. The inverse is the componentwise inverse displayed above.

## The Algebraic Fibre of the Decomposition

**The eigenvalue coordinates and the basis coordinates are two linear coordinate systems on the same algebra.**

Every element of the diagonal part, which is the whole algebra, is
$$
\breve Q_{1}=\mu_+\Pi_++\mu_-\Pi_-,\qquad \mu_\pm\in\mathbb{C},
$$
and the map $(\mu_+,\mu_-)\mapsto\breve Q_1$ is a $\mathbb{C}$-linear isomorphism $\mathbb{C}^{2}\to\mathbb{B}_{\mathrm{r}}$. For $\mu_+\neq\mu_-$ this is the eigenvalue decomposition of $\breve Q_1$, with the eigenprojections $\Pi_\pm$ and the eigenvalue data $(\mu_+,\mu_-)$. For $\mu_+=\mu_-=a$ the element is the scalar $a$, with the one-term decomposition $a\cdot1$.

The unordered spectrum is the image of the map $(\mu_+,\mu_-)\mapsto\{\mu_+,\mu_-\}$. Off the diagonal it is two-to-one: the two preimages of $\{\mu_+,\mu_-\}$ are $\mu_+\Pi_++\mu_-\Pi_-$ and $\mu_-\Pi_++\mu_+\Pi_-$, which differ by
$$
(\mu_+-\mu_-)(\Pi_+-\Pi_-)=(\mu_+-\mu_-)j\neq0.
$$
The ambiguity is exactly the exchange of the two labels.

### The Coordinate Change to Eigenvalue and Basis Data

The coordinate change to the basis $1,j$ is
$$
\breve Q_1=\frac{\mu_++\mu_-}{2}+\frac{\mu_+-\mu_-}{2}j=Q_{\blacktriangle}+jQ_{\blacktriangledown},
\qquad
Q_{\blacktriangle}=\frac{\mu_++\mu_-}{2},
\quad
Q_{\blacktriangledown}=\frac{\mu_+-\mu_-}{2}.
$$
The map $(\mu_+,\mu_-)\mapsto(Q_{\blacktriangle},Q_{\blacktriangledown})$ is a $\mathbb{C}$-linear isomorphism of $\mathbb{C}^{2}$; the two coordinate systems are the eigenvalue coordinates and the basis coordinates on the same algebra.

## Degenerate Regimes

An eigenvalue decomposition with distinct eigenvalues requires $Q_{\blacktriangledown}\neq0$. Two degenerate cases remain, and the nilpotent regime of the biquaternion case is absent.

### The Scalar Regime

**A scalar element has a repeated eigenvalue, the one-term eigenprojection $1$, and a unique two-term refinement.**

Suppose $Q_{\blacktriangledown}=0$. Then $Q_+=Q_-=Q_{\blacktriangle}$ and
$$
\breve Q=Q_{\blacktriangle}\cdot1,
$$
a complex scalar. The characteristic polynomial is $(X-Q_{\blacktriangle})^{2}$ and the minimal polynomial is $X-Q_{\blacktriangle}$; the element is central and semisimple, with the single eigenvalue $Q_{\blacktriangle}$ and eigenprojection $1$. In the sense of the general definition the eigenvalue decomposition is the one-term writing
$$
\breve Q=Q_{\blacktriangle}\cdot1.
$$

A two-term writing with the repeated coefficient is
$$
\breve Q=Q_{\blacktriangle}\Pi_++Q_{\blacktriangle}\Pi_-.
$$
It is unique, because $\{\Pi_+,\Pi_-\}$ is the only nontrivial complementary pair of idempotents: the idempotents of the algebra are $0,1,\Pi_+,\Pi_-$. This is a difference from the biquaternion scalar regime, where every complete orthogonal pair gives a two-term writing and the pair is not determined by the element; it agrees with the split-complex scalar regime (*Eigenvalue Decomposition of a Split-Complex Number*, §*The Scalar Regime*).

### The Zero-Divisor Regime

**A nonzero zero divisor has one zero eigenvalue and one nonzero eigenvalue, and it admits an eigenvalue decomposition even though it is not a unit.**

Suppose $\langle \breve Q\rangle_{\mathrm{ts}}=Q_+Q_-=0$ with $\breve Q\neq0$. Then one eigenvalue is zero and the other is nonzero. If $Q_+=0$ and $Q_-\neq0$, then
$$
\breve Q=Q_-\Pi_-,
$$
with eigenvalues $(0,Q_-)$; if $Q_-=0$ and $Q_+\neq0$, then $\breve Q=Q_+\Pi_+$, with eigenvalues $(Q_+,0)$. In either case the eigenvalues are distinct, and
$$
\breve Q=Q_\pm\Pi_\pm+0\cdot\Pi_\mp
$$
is a genuine eigenvalue decomposition. The element is a nonzero scalar multiple of an idempotent, and the minimal polynomial is $X(X-Q_\pm)$, where $Q_\pm$ is the nonzero eigenvalue; it is squarefree. This is the zero-divisor regime of the split-complex case, with $\mathbb{R}$ replaced by $\mathbb{C}$. This regime is distinct from the biquaternion nilpotent regime, which has no analogue here.

### The Absence of Nilpotents

**There are no nonzero nilpotent elements, so there is no Jordan-block regime.**

The algebra is $\mathbb{C}\times\mathbb{C}$, a product of fields, hence **reduced** (no nonzero nilpotents). If $\breve Q^{2}=0$, then in the idempotent coordinates $Q_+^{2}=Q_-^{2}=0$, so $Q_+=Q_-=0$ and $\breve Q=0$. Therefore the nilpotent regime of the biquaternion case has no analogue. Every element is semisimple, and the only failure of distinct eigenvalues is the scalar case $Q_{\blacktriangledown}=0$.

## Remarks

1. **Relation to $\mathbb{C}\times\mathbb{C}$.** Under $\mathbb{B}_{\mathrm{r}}\cong\mathbb{C}\times\mathbb{C}$, the eigenvalue decomposition is literally the product decomposition: $Q_+$ and $Q_-$ are the two complex components, $\Pi_+$ and $\Pi_-$ are the standard minimal central idempotents, and the Lagrange–Sylvester formulas are the interpolation formulas in the product algebra.

2. **Centrality and direct-sum structure.** The idempotents $\Pi_\pm$ are central, so the Peirce decomposition is a direct sum of two-sided ideals and the off-diagonal components vanish. This is the commutative shadow of the biquaternion Peirce decomposition, and it is structurally identical to the split-complex case with $\mathbb{R}$ replaced by $\mathbb{C}$.

3. **Uniqueness.** The pair $\{\Pi_+,\Pi_-\}$ is the unique nontrivial complementary pair of idempotents in the algebra. The labels are exchanged by the tessarine sign $j\mapsto-j$, which sends $Q_{\blacktriangledown}$ to $-Q_{\blacktriangledown}$. There is no non-discrete family of eigenprojections and no branch ambiguity: the decomposition is a direct-product decomposition, not a matrix spectral decomposition.

4. **Failure in degenerate regimes.** The eigenvalue decomposition with distinct eigenvalues requires $Q_{\blacktriangledown}\neq0$. The scalar regime has a repeated eigenvalue, the eigenprojection $1$, and a unique two-term refinement. The zero-divisor regime has one eigenvalue equal to $0$ and still admits an eigenvalue decomposition. There is no nilpotent regime, because the algebra is reduced.

5. **The matrix model of left multiplication.** In the basis $1,j$ the left multiplication is the matrix $\begin{pmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix}$, whose eigenvalues are $Q_\pm$ and whose eigenvectors are the coordinate vectors of $\Pi_\pm$; the decomposition is its diagonalisation in the idempotent basis. This is the matrix of left multiplication used in *Reduced Biquaternion Spectral Theory*, not the diagonal matrix element representation $\varphi(\breve Q)=\operatorname{diag}(Q_+,Q_-)$ of *The Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions*, which is the decomposition itself.

## Summary

For a reduced biquaternion with $Q_{\blacktriangledown}\neq0$, the eigenvalue decomposition is the writing
$$
\breve Q=Q_+\Pi_++Q_-\Pi_-,
\qquad
Q_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown},
\qquad
\Pi_\pm=\tfrac12(1\pm j).
$$
The eigenvalues are distinct complex numbers, the idempotents are primitive, orthogonal, complete and central, and they are the eigenprojections. The decomposition is unique up to the exchange of the two labels by the tessarine sign $j\mapsto-j$.

| Regime | Condition | Spectrum | Minimal polynomial | Eigenvalue decomposition |
|---|---|---|---|---|
| Non-scalar, general | $Q_{\blacktriangledown}\neq0$ | $\{Q_+,Q_-\}$, distinct | $(X-Q_+)(X-Q_-)$ | $\breve Q=Q_+\Pi_++Q_-\Pi_-$ |
| Non-scalar, zero divisor | $Q_+Q_-=0$, $\breve Q\neq0$ | $\{Q_\pm,0\}$ | $X(X-Q_\pm)$ | $\breve Q=Q_\pm\Pi_\pm$ |
| Scalar | $Q_{\blacktriangledown}=0$ | $\{Q_{\blacktriangle}\}$ | $X-Q_{\blacktriangle}$ | $\breve Q=Q_{\blacktriangle}\cdot1$; refinement $Q_{\blacktriangle}\Pi_++Q_{\blacktriangle}\Pi_-$ |
| Nilpotent (nonzero) | none | — | — | — |

The zero-divisor row is the subcase of the non-scalar row in which one eigenvalue vanishes.

The Peirce decomposition relative to $\Pi_+$ has corners $\mathbb{B}_{\sigma\tau}=\Pi_\sigma\mathbb{B}_{\mathrm{r}}\Pi_\tau$. Its off-diagonal corners vanish, and its diagonal part is the whole algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$. The element $\breve Q$ has the diagonal coordinates $Q_\pm$ and zero mixed coordinates. The centraliser of $\breve Q$ is the whole algebra; the subalgebra $\mathbb{C}[\breve Q]$ is the whole algebra exactly when $\breve Q$ is not scalar. The polynomial calculus, the inverse and the group isomorphism $\mathbb{B}_{\mathrm{r}}^{\times}\cong\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ all follow from the decomposition. There is no nilpotent regime, because the algebra is a product of fields.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ | Reduced biquaternion algebra, dimension $4$ over $\mathbb{R}$, $2$ over $\mathbb{C}$ |
| $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | General reduced biquaternion, $Q_{\blacktriangle},Q_{\blacktriangledown}\in\mathbb{C}$ |
| $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$, $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$ | Complex basis coordinates |
| $\Pi_\pm=\tfrac12(1\pm j)$ | The two nontrivial central idempotents, the eigenprojections |
| $Q_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown}$ | Idempotent coordinates, the eigenvalues |
| $\breve Q=Q_+\Pi_++Q_-\Pi_-$ | Idempotent decomposition; eigenvalue decomposition when $Q_{\blacktriangledown}\neq0$ |
| $\sigma(\breve Q)=\{Q_+,Q_-\}$ | Spectrum |
| $\chi_{\breve Q}(X)=X^{2}-2Q_{\blacktriangle}X+\langle \breve Q\rangle_{\mathrm{ts}}$ | Characteristic polynomial, $(X-Q_+)(X-Q_-)$ |
| $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=Q_+Q_-$ | Reduced norm and determinant |
| $\operatorname{tr}(\breve Q)=2Q_{\blacktriangle}=Q_++Q_-$ | Reduced trace |
| $\mathbb{B}_{\sigma\tau}=\Pi_\sigma\mathbb{B}_{\mathrm{r}}\Pi_\tau$ | Peirce corners of the pair $\Pi_\pm$ |
| $\mathbb{C}[\breve Q]=\operatorname{span}_{\mathbb{C}}\{1,\breve Q\}$ | Subalgebra generated by $\breve Q$ |
| $C(\breve Q)=\mathbb{B}_{\mathrm{r}}$ | Centraliser of $\breve Q$ |
| $\mathbb{B}_{\mathrm{r}}^{\times}\cong\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ | Group of units, the coordinatewise nonzero pairs |
| $\mathsf{M}_{L}(\breve Q)$ | Matrix of left multiplication in the basis $1,j$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for idempotents, Peirce decompositions and the structure of finite-dimensional algebras.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 1985), for the eigenvalue decomposition, the Lagrange–Sylvester formula and the spectral projections.
- Nicholas J. Higham, *Functions of Matrices: Theory and Computation* (SIAM, Philadelphia, 2008), for the functional calculus and the matrix inverse.
- G. Baley Price, *An Introduction to Multicomplex Spaces and Functions* (Marcel Dekker, 1991), for the idempotent decomposition and the coordinatewise product of the multicomplex algebra.
- M. Elena Luna-Elizarrarás, Michael Shapiro, Daniele C. Struppa and Adrian Vajiac, *Bicomplex Holomorphic Functions* (Birkhäuser, 2015), for the commutative two-component algebra and its idempotent coordinates.
- The corpus articles: [The Eigenvalue Decomposition of an Element](the-eigenvalue-decomposition-of-an-element.html), [The Lagrange–Sylvester Eigenprojector Formula](the-lagrange-sylvester-eigenprojector-formula.html), [The Centraliser and the Diagonal Peirce Part](the-centraliser-and-the-diagonal-peirce-part.html), [Off-Diagonal Peirce Components and Noncentral Idempotents](off-diagonal-peirce-components-and-noncentral-idempotents.html), [Reduced Biquaternion Spectral Theory](reduced-biquaternion-spectral-theory.html), [Square Roots of One and the Idempotents of the Algebra of the Reduced Biquaternions](square-roots-of-one-and-the-idempotents-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), [Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions](ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), [Norm and Invertibility in the Algebra of the Reduced Biquaternions](norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.html), [The Group of Units of the Algebra of the Reduced Biquaternions](the-group-of-units-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), [Zero Divisors of the Algebra of the Reduced Biquaternions](zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), [The Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions](the-general-plain-algebra-in-the-2x2-matrix-element-representation-of-the-reduced-biquaternions.html), [Eigenvalue Decomposition of a Biquaternion](eigenvalue-decomposition-of-a-biquaternion.html), [Eigenvalue Decomposition of a Split-Complex Number](eigenvalue-decomposition-of-a-split-complex-number.html) and [Conventions in Mathematics](conventions-in-mathematics.html).
