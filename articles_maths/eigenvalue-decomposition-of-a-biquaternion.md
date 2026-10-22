# __Eigenvalue Decomposition of a Biquaternion__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is simple and four-dimensional over $\mathbb{C}$, and the matrix model $\mathsf{M}_2$ identifies it with $M_2(\mathbb{C})$. This article reads the **eigenvalue decomposition** of a biquaternion: the writing of $\tilde Q$ as a complex linear combination of the two idempotents of a complete orthogonal pair, with the eigenvalues as coefficients. The general definition and the existence theorem are those of *The Eigenvalue Decomposition of an Element*; the biquaternion content is that, in the regime of distinct eigenvalues, the pair is the pair of a pure root of $+1$ and that the decomposition is the Peirce decomposition attached to that root in *Ideals and Peirce Decomposition of the Biquaternion Algebra*.

The notation is fixed in *Conventions in Mathematics*: the base is $e_t,\vec e_x,\vec e_y,\vec e_z$, a general element is $\tilde Q=Q_te_t+\vec Q$ with $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ and complex coefficients, an idempotent is $\tilde\Pi$, a root of $+1$ is $\tilde\Xi$ and a pure root is $\vec\Xi$, and a pure nilpotent is $\vec\Upsilon$. The characteristic polynomial, the spectrum and the eigenvalues $Q_t\pm iB$ are those of *Biquaternion Spectral Theory*, §*The Biquaternion Spectrum*; the root of $+1$, the halving map and the primitive idempotents are those of *Square Roots of One and the Idempotents of the Biquaternion Algebra*, §*The Idempotents*; the four Peirce corners are those of *Ideals and Peirce Decomposition of the Biquaternion Algebra*, §*The Peirce Decomposition*; the centraliser and the diagonal part are those of *The Centraliser and the Diagonal Peirce Part*; the off-diagonal components are those of *Off-Diagonal Peirce Components and Noncentral Idempotents*; and the eigenvalue formula and the parity-matched lattice are those of *Biquaternion Elementary Functions*, §*The Eigenvalue Formula*.

**Scope.** The article proves the eigenvalue decomposition in the regime of distinct eigenvalues, identifies its eigenprojections with the idempotents of a pure root of $+1$, reads the decomposition as the Peirce decomposition relative to one of them, and treats the two degenerate regimes: the nilpotent vector part, where no such decomposition exists, and the scalar element, where the two-projector writing is not unique.

**Boundaries.** The quaternion case, with its left and right eigenvalues, is the subject of *Quaternion Spectral Theory*; the reduced-biquaternion case is that of *Reduced Biquaternion Spectral Theory*; the exponential and the logarithm built on the decomposition are those of *Biquaternion Elementary Functions*; and the spectral theorem in its general form is that of *Biquaternion Spectral Theory*. The article cites these and does not restate them. The other products of the biquaternion space carry nilpotents and idempotents relative to the product, and are outside its scope.

## The Pure Root of the Vector Part

The square of the vector part is central,
$$
\vec Q^2=-(Q_x^2+Q_y^2+Q_z^2)e_t,
$$
as in *Biquaternion Spectral Theory*, §*The Biquaternion Spectrum*. Let $B$ be a square root of $Q_x^2+Q_y^2+Q_z^2$, so that $\vec Q^2=-B^2e_t$.

Assume $B\neq0$. Put
$$
\vec U=\frac{\vec Q}{B},\qquad \vec\Xi=-i\vec U=-\frac{i\vec Q}{B}.
$$
Then $\vec U$ is a pure unit element of the biquaternion layer, $\vec U^2=-e_t$, and $\vec\Xi$ is a pure root of $+1$:
$$
\vec\Xi^2=(-i)^2\vec U^2=e_t.
$$
Conversely $\vec Q=B\vec U=iB\vec\Xi$. The root is pure, so it carries the arrow and not the tilde (§*Pure Elements and their Coefficients* of *Conventions in Mathematics*), and it belongs to the roots classified in *Square Roots of One and the Idempotents of the Biquaternion Algebra*, §*The Roots of One*. For a real vector part, $B$ may be taken real and positive, $\vec U$ is then the real unit vector $\vec u$, and $\vec\Xi=-i\vec u$ lies in the family $i\vec u$ of the pure roots; for a general complex vector part, $\vec U$ and $\vec\Xi$ are genuinely complex.

The choice is two-fold: the replacement $B\mapsto-B$ replaces $\vec U$ and $\vec\Xi$ by their opposites. Only $B^2$ is determined by $\tilde Q$, and with it the unordered pair $\{\vec\Xi,-\vec\Xi\}$; in the real case the convention $B>0$ removes the choice.

## Eigenvalues and the Characteristic Polynomial

Since $\vec Q=iB\vec\Xi$,
$$
(\tilde Q-Q_te_t)^2=\vec Q^2=-B^2e_t,
$$
hence
$$
\tilde Q^2-2Q_t\tilde Q+(Q_t^2+B^2)e_t=0,\qquad Q_t^2+B^2=\langle\tilde Q\rangle_{\natural}.
$$
This is the quadratic identity of *Biquaternion Spectral Theory*, §*The Biquaternion Spectrum*, and the characteristic polynomial is
$$
p_{\tilde Q}(X)=X^2-2Q_tX+\langle\tilde Q\rangle_{\natural}=(X-Q_t)^2+B^2,
$$
with roots
$$
\lambda_\pm=Q_t\pm iB.
$$
The discriminant is
$$
(\lambda_+-\lambda_-)^2=(2iB)^2=-4B^2\neq0,
$$
so the eigenvalues are distinct exactly when $B\neq0$. The minimal polynomial is then $p_{\tilde Q}$.

Under the matrix model the trace is $\operatorname{Tr}\mathsf{M}_2(\tilde Q)=2Q_t$ and the determinant is $\det\mathsf{M}_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ (§*The Matrix Model* of *Ideals and Peirce Decomposition of the Biquaternion Algebra*), so $p_{\tilde Q}$ is the characteristic polynomial of $\mathsf{M}_2(\tilde Q)$ and $\lambda_\pm$ are its eigenvalues.

## The Eigenprojections

Put
$$
\tilde\Pi_+=\frac12(e_t+\vec\Xi),\qquad \tilde\Pi_-=\frac12(e_t-\vec\Xi),
$$
the two idempotents of the root $\vec\Xi$ under the halving map of *Square Roots of One and the Idempotents of the Biquaternion Algebra*, §*The Idempotents*. By that article the pair is complete and orthogonal, $\tilde\Pi_++\tilde\Pi_-=e_t$ and $\tilde\Pi_+\tilde\Pi_-=0$, and the root is their difference, $\vec\Xi=\tilde\Pi_+-\tilde\Pi_-$; by *Ideals and Peirce Decomposition of the Biquaternion Algebra*, §*Idempotents and Orthogonal Idempotents*, each member is primitive.

They are the eigenprojections of $\tilde Q$:
$$
\tilde Q\tilde\Pi_+=\lambda_+\tilde\Pi_+,\qquad \tilde Q\tilde\Pi_-=\lambda_-\tilde\Pi_-.
$$
Indeed, since $\vec Q=iB\vec\Xi$ and $\vec\Xi^2=e_t$,
$$
\tilde Q\tilde\Pi_+=(Q_te_t+iB\vec\Xi)\frac12(e_t+\vec\Xi)=\frac12(Q_t+iB)(e_t+\vec\Xi)=\lambda_+\tilde\Pi_+,
$$
and, with $Q_t-iB$ in place of $Q_t+iB$ and $e_t-\vec\Xi$ in place of $e_t+\vec\Xi$,
$$
\tilde Q\tilde\Pi_-=\lambda_-\tilde\Pi_-.
$$

Equivalently, by the eigenprojector formula of *The Lagrange–Sylvester Eigenprojector Formula*, §*The Eigenprojector Formula*,
$$
\tilde\Pi_+=\frac{\tilde Q-\lambda_-e_t}{\lambda_+-\lambda_-},\qquad \tilde\Pi_-=\frac{\tilde Q-\lambda_+e_t}{\lambda_--\lambda_+},\qquad \lambda_+-\lambda_-=2iB.
$$
Hence $\tilde\Pi_\pm$ are polynomials in $\tilde Q$, and in particular commute with $\tilde Q$.

## The Eigenvalue Decomposition

Summing the two eigenvalue relations,
$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-.
$$
This is an eigenvalue decomposition in the sense of *The Eigenvalue Decomposition of an Element*, §*The definition*: the coefficients $\lambda_\pm$ are distinct, the idempotents $\tilde\Pi_\pm$ are nonzero, orthogonal and complete, and they are the eigenprojections. Separating scalar and vector parts,
$$
\tilde Q=\frac{\lambda_++\lambda_-}{2}e_t+\frac{\lambda_+-\lambda_-}{2}\vec\Xi=Q_te_t+iB\vec\Xi=Q_te_t+B\vec U.
$$
So the decomposition writes $\tilde Q$ as a complex linear combination of the two primitive idempotents of $\vec\Xi$, with the eigenvalues as coefficients.

**Uniqueness.** By the uniqueness theorem of *The Eigenvalue Decomposition of an Element*, §*Uniqueness*, an element with distinct eigenvalues has a unique eigenprojection attached to each eigenvalue. Here the two eigenprojections are the two idempotents of the root $\vec\Xi$, and the root is read back from them as $\vec\Xi=\tilde\Pi_+-\tilde\Pi_-$. The unordered pair $\{\tilde\Pi_+,\tilde\Pi_-\}$ is determined by $\tilde Q$; the ordered pair is determined only up to the swap that sends $B$ to $-B$ and $\vec\Xi$ to $-\vec\Xi$. The labelling is canonical when $B^2$ has a distinguished square root, as it does for a real vector part, where $B$ is taken real and positive; for a general complex vector part no canonical choice exists.

**Semisimplicity.** Since $\lambda_+\neq\lambda_-$, the minimal polynomial $p_{\tilde Q}$ is squarefree, and $\tilde Q$ is semisimple (*Nilpotent Elements and the Jordan–Chevalley Decomposition*, §*Semisimple Elements*). The decomposition is the diagonalisation of $\tilde Q$ with respect to the noncentral idempotents $\tilde\Pi_\pm$.

Under the matrix model, $\mathsf{M}_2(\tilde\Pi_\pm)$ are the rank-one eigenprojections of $\mathsf{M}_2(\tilde Q)$.

## The Peirce Decomposition Relative to the Eigenprojection

Let
$$
\mathbb{B}_{st}=\tilde\Pi_s\mathbb{B}\tilde\Pi_t,\qquad s,t\in\{+,-\},
$$
be the Peirce corners of the pair, in the notation of *Ideals and Peirce Decomposition of the Biquaternion Algebra*, §*The Biquaternion Case*. The Peirce decomposition is
$$
\mathbb{B}=\mathbb{B}_{++}\oplus\mathbb{B}_{+-}\oplus\mathbb{B}_{-+}\oplus\mathbb{B}_{--}.
$$
Each corner is one complex line, the diagonal corners are $\mathbb{C}\tilde\Pi_+$ and $\mathbb{C}\tilde\Pi_-$, and the two mixed corners are square-zero. This is the decomposition attached to the root $\vec\Xi=-i\vec Q/B$ in §*The Peirce Decomposition* of that article.

The diagonal part is
$$
\mathbb{B}_{++}\oplus\mathbb{B}_{--}=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\tilde\Pi_-=\mathbb{C}[\tilde Q]=\operatorname{span}_{\mathbb{C}}\{e_t,\tilde Q\}.
$$
It is a commutative subalgebra isomorphic to $\mathbb{C}\times\mathbb{C}$. By *The Centraliser and the Diagonal Peirce Part*, §*The theorem*, applied to the eigenvalue decomposition, it is the centraliser of $\tilde Q$; by *Off-Diagonal Peirce Components and Noncentral Idempotents*, §*The Commutator Interpretation*, the mixed part is $[\tilde\Pi_+,\mathbb{B}]$, so an element commutes with $\tilde Q$ exactly when its two mixed Peirce components vanish.

On $\tilde Q$ the Peirce decomposition reads
$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-,
$$
with zero mixed components. The eigenvalue decomposition is therefore the Peirce decomposition read on the element: the element lies in the diagonal part, and its two diagonal Peirce coordinates are its eigenvalues. The mixed corners are the directions that fail to commute with $\tilde Q$.

The two signs of the pair are the two eigenvalues of multiplication by the root: an element of $\mathbb{B}_{st}$ is multiplied by $s$ on the left and by $t$ on the right by $\vec\Xi$ (§*The Biquaternion Case*). The diagonal corners are the components on which the two signs agree; $\tilde Q$ acts on them by $\lambda_+$ and $\lambda_-$ respectively.

## Powers and Polynomial Calculus

By Sylvester's formula of *The Lagrange–Sylvester Eigenprojector Formula*, §*Sylvester's Formula*, every polynomial $f\in\mathbb{C}[X]$ acts as
$$
f(\tilde Q)=f(\lambda_+)\tilde\Pi_++f(\lambda_-)\tilde\Pi_-.
$$
In particular
$$
\tilde Q^n=\lambda_+^n\tilde\Pi_++\lambda_-^n\tilde\Pi_-,\qquad n\geq0,
$$
with $\tilde\Pi_++\tilde\Pi_-=e_t$ for $n=0$. When $\tilde Q$ is a unit, the two eigenvalues are nonzero (§*The Unit and the Group of Units* of *Norm and Invertibility in the Biquaternion Algebra*), and the formula extends to negative powers:
$$
\tilde Q^{-1}=\lambda_+^{-1}\tilde\Pi_++\lambda_-^{-1}\tilde\Pi_-.
$$
The result agrees with the inverse formula $\tilde Q^{-1}=\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$ of that article, since $\lambda_+\lambda_-=\langle\tilde Q\rangle_{\natural}$ and $\lambda_-\tilde\Pi_++\lambda_+\tilde\Pi_-=Q_te_t-B\vec U=\tilde Q^{\natural}$.

## The Algebraic Fibre of the Decomposition

Fix the pair, that is, fix the root $\vec\Xi$ up to sign. Every element of $\mathbb{C}[\tilde Q]$ is
$$
\tilde Q_1=\mu_+\tilde\Pi_++\mu_-\tilde\Pi_-,\qquad \mu_\pm\in\mathbb{C},
$$
and the map $(\mu_+,\mu_-)\mapsto\tilde Q_1$ is a $\mathbb{C}$-linear isomorphism $\mathbb{C}^2\to\mathbb{C}[\tilde Q]$.

For $\mu_+\neq\mu_-$ this is the eigenvalue decomposition of $\tilde Q_1$, with the eigenprojections $\tilde\Pi_\pm$ and the eigenvalue data $(\mu_+,\mu_-)$. For $\mu_+=\mu_-=a$ the element is $\tilde Q_1=ae_t$, scalar; the writing is still valid but every complete orthogonal pair gives it, so the two-projector pair is not determined by $\tilde Q_1$, although the eigenprojection $e_t$ of the one-term decomposition is.

The unordered pair $\{\mu_+,\mu_-\}$ is the spectrum when $\mu_+\neq\mu_-$. For $\mu_+\neq\mu_-$, with the pair of idempotents fixed, the coordinate map to the unordered spectrum is two-to-one: the two preimages of $\{\mu_+,\mu_-\}$ are $\mu_+\tilde\Pi_++\mu_-\tilde\Pi_-$ and $\mu_-\tilde\Pi_++\mu_+\tilde\Pi_-$, which differ by $(\mu_+-\mu_-)(\tilde\Pi_+-\tilde\Pi_-)\neq0$. For eigenvalues constrained to subsets $S_\pm\subseteq\mathbb{C}$, the corresponding elements are
$$
\{\mu_+\tilde\Pi_++\mu_-\tilde\Pi_-:\ \mu_+\in S_+,\ \mu_-\in S_-\}.
$$

### The Coordinate Change to Scalar and Vector Data

The scalar and vector coordinates of $\tilde Q_1$ are
$$
\tilde Q_1=\frac{\mu_++\mu_-}{2}e_t+\frac{\mu_+-\mu_-}{2}\vec\Xi=ae_t+\Theta\vec U,
\qquad a=\frac{\mu_++\mu_-}{2},\quad \Theta=\frac{\mu_+-\mu_-}{2i},
$$
the second equality using $\vec\Xi=-i\vec U$. The map $(\mu_+,\mu_-)\mapsto(a,\Theta)$ is a $\mathbb{C}$-linear isomorphism of $\mathbb{C}^2$; the scalar $a$ is the scalar part and $\Theta$ is the complex angle along the axis $\vec U$ used in *Biquaternion Elementary Functions*, §*The Eigenvalue Formula*. The two coordinate systems are the eigenvalue coordinates and the scalar-vector coordinates on the same diagonal part.

### The Parity-Matched Lattice

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
This is the parity-matched lattice of *Biquaternion Elementary Functions*, §*The Eigenvalue Formula*, written there with the axis $\vec u$; for a real vector part $\vec U=\vec u$, and the two lattices are the same. It is the kernel of the exponential on the diagonal part. It is not the rectangular lattice $2\pi i\mathbb{Z}e_t\oplus2\pi\mathbb{Z}\vec U$: the rectangular lattice is the sublattice of index two in $L$ on which $m$ and $n$ are both even, the other coset is $\pi i e_t+\pi\vec U$, and the scalar and the vector coordinate cannot be chosen independently, because the idempotents $\tilde\Pi_\pm$ mix the two directions.

## Degenerate Regimes

The eigenvalue decomposition exists exactly when the minimal polynomial is split with distinct roots (*The Eigenvalue Decomposition of an Element*, §*Existence and Uniqueness*). Here $p_{\tilde Q}$ always splits over $\mathbb{C}$, and its roots are distinct exactly when $B\neq0$. The two degenerate regimes are separated by whether the vector part vanishes.

### The Nilpotent Regime

Let $B=0$ and $\vec Q\neq0$. Then $\vec Q^2=0$, so $\vec\Upsilon=\vec Q$ is a pure nilpotent, written with the arrow and without the tilde by §*The Nilpotent Convention* of *Conventions in Mathematics*, and
$$
\tilde Q=Q_te_t+\vec\Upsilon,\qquad \vec\Upsilon^2=0.
$$
The element is a unit exactly when $Q_t\neq0$ (§*The Unit and the Group of Units* of *Norm and Invertibility in the Biquaternion Algebra*), and its minimal polynomial is
$$
p_{\tilde Q}(X)=(X-Q_t)^2,
$$
which is not squarefree. By the theorem of *The Eigenvalue Decomposition of an Element*, §*Existence and Uniqueness*, $\tilde Q$ has no eigenvalue decomposition. In the matrix model $\mathsf{M}_2(\tilde Q)$ is a single Jordan block, conjugate to
$$
\begin{pmatrix}Q_t&1\\0&Q_t\end{pmatrix}.
$$

The centraliser of $\tilde Q$ is
$$
\{ae_t+b\vec\Upsilon:\ a,b\in\mathbb{C}\}.
$$
It contains no nontrivial idempotent: if $(ae_t+b\vec\Upsilon)^2=ae_t+b\vec\Upsilon$, then $a^2=a$ and $2ab=b$, so $(a,b)=(0,0)$ or $(1,0)$, giving $0$ or $e_t$. Hence no complete orthogonal pair other than the trivial one commutes with $\tilde Q$, and there is no Peirce decomposition adapted to $\tilde Q$ into two primitive idempotents.

### The Scalar Regime

Let $\vec Q=0$, so $\tilde Q=Q_te_t$. The element is central and semisimple, with the single eigenvalue $Q_t$ and minimal polynomial $X-Q_t$; its centraliser is all of $\mathbb{B}$.

In the sense of the general definition the eigenvalue decomposition has one term, $\tilde Q=Q_te_t$, with the single eigenprojection $e_t$, and it is unique. A decomposition into two primitive idempotents with the repeated coefficient $Q_t$ is a different object: every complete orthogonal pair $\tilde\Pi_1,\tilde\Pi_2$ gives
$$
\tilde Q=Q_t\tilde\Pi_1+Q_t\tilde\Pi_2,
$$
and the pair is not determined by $\tilde Q$. The eigenvalue data therefore determine nothing beyond the scalar, and the two-projector writing is non-unique.

## The Hermitian Case

The idempotents $\tilde\Pi_\pm$ are Hermitian exactly when the axis $\vec U$ is real.

**Proposition.** Let $B\neq0$. The following are equivalent: (i) $\tilde\Pi_\pm$ are Hermitian; (ii) $\vec U$ is real; (iii) $\vec\Xi$ is purely imaginary; (iv) $\tilde Q$ is normal.

*Proof.* Since $\vec\Xi=-i\vec U$ and $\vec\Xi^{*}=-\overline{\vec\Xi}$,
$$
\tilde\Pi_\pm^{*}=\frac12\bigl(e_t\pm\vec\Xi^{*}\bigr)=\frac12\bigl(e_t\mp i\overline{\vec U}\bigr),
$$
so (i) holds exactly when $\overline{\vec U}=\vec U$, which is (ii); and (ii) and (iii) are the same condition, since $\vec U=i\vec\Xi$. If (ii) holds, then $\tilde Q^{*}=\overline{Q_t}e_t-\overline{B}\,\vec U$ lies in $\mathbb{C}[\tilde Q]$, so $\tilde Q$ commutes with $\tilde Q^{*}$ and (iv) holds. Conversely, if (iv) holds, Theorem 11.2 of *Biquaternion Spectral Theory*, §*The Spectral Theorem*, writes $\tilde Q=\lambda_1\tilde\Pi_1+\lambda_2\tilde\Pi_2$ with Hermitian idempotents; since $B\neq0$ the eigenvalues are distinct, and the formulas of that theorem identify $\tilde\Pi_1,\tilde\Pi_2$ with $\tilde\Pi_\pm$, so (i) holds.

The pair is then the Hermitian pair of the root $\vec\Xi=-i\vec u$ over a real unit vector $\vec u$ (§*The Families of Idempotents* of *Square Roots of One and the Idempotents of the Biquaternion Algebra*), and the decomposition is the spectral theorem of *Biquaternion Spectral Theory*, §*The Spectral Theorem*, read in the biquaternion algebra.

## Remarks

1. **Relation to $M_2(\mathbb{C})$.** Under the matrix model the above is the eigenvalue decomposition of a $2\times2$ complex matrix with distinct eigenvalues: $\lambda_\pm$ are the eigenvalues, $\mathsf{M}_2(\tilde\Pi_\pm)$ are the rank-one eigenprojections, and the two formulas are the Lagrange–Sylvester formulas. The biquaternion-specific content is the identification of the eigenprojections with the idempotents of a pure root of $+1$, and of the eigenvalue data with the scalar part and the complex angle along $\vec U$.

2. **Noncentrality.** The idempotents $\tilde\Pi_\pm$ are noncentral: they commute with $\tilde Q$ and with its centraliser, but not with all of $\mathbb{B}$. There is no central idempotent in $\mathbb{B}$, since the algebra is simple (§*The Two-Sided Ideals: Simplicity of $\mathbb{B}$* of *Ideals and Peirce Decomposition of the Biquaternion Algebra*). The decomposition is therefore a Peirce decomposition relative to an element-dependent idempotent, not a decomposition of the algebra into ideals.

3. **Labelling.** The decomposition is canonical only as the unordered set of pairs $\{(\lambda_+,\tilde\Pi_+),(\lambda_-,\tilde\Pi_-)\}$. The labelling is interchanged by $B\mapsto-B$ and $\vec\Xi\mapsto-\vec\Xi$. It is canonical when $B^2$ has a distinguished square root, as for a real vector part with $B>0$, and not otherwise.

4. **Failure in the degenerate regimes.** The eigenvalue decomposition is a property of semisimple elements with distinct eigenvalues. The nilpotent regime is non-semisimple and admits none. The scalar regime is semisimple with a repeated eigenvalue: the general decomposition has one term, and any two-projector refinement is non-unique.

## Summary

For a biquaternion with $B\neq0$, the eigenvalue decomposition is the writing
$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-,
\qquad
\lambda_\pm=Q_t\pm iB,
\qquad
\tilde\Pi_\pm=\frac12(e_t\pm\vec\Xi),
$$
where $B^2=Q_x^2+Q_y^2+Q_z^2$ and $\vec\Xi=-i\vec Q/B$ is the pure root of $+1$ of the vector part. The eigenvalues are distinct, the idempotents are primitive, orthogonal and complete, and they are the eigenprojections. The decomposition is unique up to the simultaneous swap of the two labels.

| Regime | Condition | Spectrum | Minimal polynomial | Two-projector decomposition |
|---|---|---|---|---|
| Distinct | $B\neq0$ | $\{Q_t+iB,Q_t-iB\}$ | $(X-Q_t)^2+B^2$ | $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$, unique unordered pair |
| Nilpotent | $B=0$, $\vec Q\neq0$ | $\{Q_t\}$ | $(X-Q_t)^2$ | none |
| Scalar | $\vec Q=0$ | $\{Q_t\}$ | $X-Q_t$ | $Q_t\tilde\Pi_1+Q_t\tilde\Pi_2$ for every complete pair |

The Peirce decomposition relative to $\tilde\Pi_+$ has corners $\mathbb{B}_{st}=\tilde\Pi_s\mathbb{B}\tilde\Pi_t$. Its diagonal part is the centraliser $\mathbb{C}[\tilde Q]=\operatorname{span}_{\mathbb{C}}\{e_t,\tilde Q\}$, and $\tilde Q$ has the diagonal coordinates $\lambda_\pm$ and zero mixed coordinates. The mixed corners are the directions that fail to commute with $\tilde Q$. The polynomial calculus, the inverse and the parity-matched lattice all follow from the decomposition. The idempotents are Hermitian exactly when $\vec U$ is real, and the decomposition is then the spectral theorem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, dimension $4$ over $\mathbb{C}$ |
| $\tilde Q=Q_te_t+\vec Q$ | General biquaternion, $Q_\mu\in\mathbb{C}$ |
| $\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ | Algebraic norm and determinant |
| $B$ | A square root of $Q_x^2+Q_y^2+Q_z^2$ |
| $\vec U=\vec Q/B$ | Pure unit element, $\vec U^2=-e_t$, for $B\neq0$ |
| $\vec\Xi=-i\vec U=-\dfrac{i\vec Q}{B}$ | Pure root of $+1$, $\vec\Xi^2=e_t$ |
| $\lambda_\pm=Q_t\pm iB$ | Eigenvalues |
| $\tilde\Pi_\pm=\frac12(e_t\pm\vec\Xi)$ | Eigenprojections, primitive orthogonal idempotents |
| $\tilde\Pi_1,\tilde\Pi_2$ | A complete orthogonal pair, used in the scalar regime |
| $\mathbb{B}_{st}=\tilde\Pi_s\mathbb{B}\tilde\Pi_t$ | Peirce corners of the pair |
| $\mathbb{C}[\tilde Q]=\operatorname{span}_{\mathbb{C}}\{e_t,\tilde Q\}$ | Commutative subalgebra and centraliser of $\tilde Q$ |
| $\mu_\pm$ | Eigenvalue coordinates on the diagonal part |
| $a=(\mu_++\mu_-)/2$, $\Theta=(\mu_+-\mu_-)/(2i)$ | Scalar and angle coordinates on the diagonal part |
| $L=\{\pi i m\,e_t+\pi n\,\vec U:\ m,n\in\mathbb{Z},\ m\equiv n\pmod2\}$ | Parity-matched lattice, the kernel of $\exp$ on the diagonal part |
| $\vec\Upsilon=\vec Q$ | Pure nilpotent, in the regime $B=0$ and $\vec Q\neq0$ |
| $\mathsf{M}_2$ | Matrix model $\mathbb{B}\cong M_2(\mathbb{C})$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 1985), for the eigenvalue decomposition, the Lagrange–Sylvester formula and the spectral theorem.
- Nicholas J. Higham, *Functions of Matrices: Theory and Computation* (SIAM, Philadelphia, 2008), for the functional calculus and the matrix inverse.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the Peirce decomposition and the structure theory of finite-dimensional algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the algebraic structure of the biquaternion algebra.
- Vladimir V. Rodman, *Topics in Quaternion Linear Algebra* (Princeton University Press, 2014), for the spectral theory of quaternionic matrices.
- The corpus articles: [The Eigenvalue Decomposition of an Element](the-eigenvalue-decomposition-of-an-element.html), [The Lagrange–Sylvester Eigenprojector Formula](the-lagrange-sylvester-eigenprojector-formula.html), [The Centraliser and the Diagonal Peirce Part](the-centraliser-and-the-diagonal-peirce-part.html), [Off-Diagonal Peirce Components and Noncentral Idempotents](off-diagonal-peirce-components-and-noncentral-idempotents.html), [Biquaternion Spectral Theory](biquaternion-spectral-theory.html), [Ideals and Peirce Decomposition of the Biquaternion Algebra](ideals-and-peirce-decomposition-of-the-biquaternion-algebra.html), [Square Roots of One and the Idempotents of the Biquaternion Algebra](square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), [Norm and Invertibility in the Biquaternion Algebra](norm-and-invertibility-in-the-biquaternion-algebra.html) and [Conventions in Mathematics](conventions-in-mathematics.html).
