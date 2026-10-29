# __Spectral Regularity and Degeneracy in the Reduced Biquaternion Algebra__

## Introduction

The reduced biquaternion algebra
$$
\mathbb{B}_{\mathrm r}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}
$$
is commutative, associative and unital, of complex dimension two. An element is
$$
\breve Q=Q_\blacktriangle+jQ_\blacktriangledown,
\qquad j^{2}=+1,\qquad ij=ji,\qquad i^{2}=-1,
$$
and the idempotents $\Pi_\pm=\tfrac12(1\pm j)$ give the idempotent coordinates $Q_\pm=Q_\blacktriangle\pm Q_\blacktriangledown$ and the decomposition
$$
\breve Q=Q_+\Pi_+ + Q_-\Pi_-.
$$
This article studies the eigenvalue problem of $\breve Q$ and the one condition that decides whether its two eigenvalues can be told apart. The eigenvalues are $Q_+$ and $Q_-$. The element is **spectrally regular** when $Q_+\neq Q_-$ and **spectrally degenerate** when $Q_+=Q_-$; equivalently, regular when $Q_\blacktriangledown\neq0$ and degenerate when $Q_\blacktriangledown=0$. The characteristic polynomial is $(X-Q_+)(X-Q_-)$, of discriminant $(Q_+-Q_-)^2=4Q_\blacktriangledown^2$. The article proves the criterion, computes the characteristic and minimal polynomials, identifies the eigenspaces as the two idempotent lines, proves that every element is semisimple, and explains why the product structure $\mathbb{C}\oplus\mathbb{C}$ removes the defective cone that the biquaternion algebra possesses.

**Notation.** The algebra and its idempotents are *Reduced Biquaternion Space*; the reduced norm $Q_+Q_-$ and the unit criterion are *Norm and Invertibility in the Algebra of the Reduced Biquaternions*; the zero divisors are *Zero Divisors of the Algebra of the Reduced Biquaternions*. The eigenvalue decomposition is *Eigenvalue Decomposition and Eigenbasis of a Reduced Biquaternion*; the matrix reading is *Eigenbasis of a Reduced Biquaternion in Matrix Elements Representations*; the computed cases are *Worked Examples of Eigenbasis a Reduced Biquaternion*; left multiplication is *Reduced Biquaternion Spectral Theory*. The biquaternion comparison is *The Spectrum*. The companion articles are *Relations between the Reduced Norm and Spectral Regularity and Degeneracy* and *The Four Sectors of the Reduced Biquaternion Algebra*.

## The Eigenvalue Problem in Idempotent Coordinates

**Definition (eigenvalue).** A complex scalar $\lambda$ is an **eigenvalue** of $\breve Q$ if $\breve Q-\lambda 1$ is not a unit of $\mathbb{B}_{\mathrm r}$. The set of eigenvalues is the **spectrum** $\sigma(\breve Q)$.

**Definition (eigenvector and eigenspace).** A nonzero $v\in\mathbb{B}_{\mathrm r}$ is an **eigenvector** for $\lambda$ if $\breve Qv=\lambda v$. The **eigenspace** is
$$
E_\lambda=\{v\in\mathbb{B}_{\mathrm r}:\breve Qv=\lambda v\},
$$
a $\mathbb{C}$-linear subspace. The algebra is commutative, so the left and right eigenvalue problems coincide and there is only one notion of eigenvector.

**Theorem (the spectrum).** For every $\breve Q$,
$$
\sigma(\breve Q)=\{Q_+,Q_-\}.
$$

*Proof.* In the idempotent coordinates,
$$
\breve Q-\lambda 1=(Q_+-\lambda)\Pi_+ +(Q_--\lambda)\Pi_-.
$$
By the criterion of *Norm and Invertibility in the Algebra of the Reduced Biquaternions*, an element is a unit exactly when both idempotent coordinates are nonzero. Hence $\breve Q-\lambda 1$ is not a unit exactly when one coordinate vanishes, that is when $\lambda=Q_+$ or $\lambda=Q_-$.

**Corollary (the characteristic polynomial).** In the basis $(\Pi_+,\Pi_-)$ the left multiplication $L_{\breve Q}$ has matrix $\operatorname{diag}(Q_+,Q_-)$, so
$$
p_{\breve Q}(X)=\det(X1-L_{\breve Q})=(X-Q_+)(X-Q_-)
=X^2-2Q_\blacktriangle X+(Q_\blacktriangle^2-Q_\blacktriangledown^2).
$$
Its trace is $2Q_\blacktriangle$, its determinant is the reduced norm $Q_+Q_-$, and its discriminant is
$$
\Delta=(Q_+-Q_-)^2=4Q_\blacktriangledown^2.
$$

**Theorem (the minimal polynomial).** The minimal polynomial of $\breve Q$ is the squarefree part of the characteristic polynomial:
$$
m_{\breve Q}(X)=
\begin{cases}
(X-Q_+)(X-Q_-), & Q_+\neq Q_-,\\[2pt]
X-Q_+, & Q_+=Q_-.
\end{cases}
$$
In both cases $m_{\breve Q}$ is squarefree.

*Proof.* If $Q_+\neq Q_-$, then
$$
\breve Q-Q_+=(Q_--Q_+)\Pi_-,\qquad
\breve Q-Q_-=(Q_+-Q_-)\Pi_+,
$$
so the product $(X-Q_+)(X-Q_-)$ annihilates $\breve Q$ because $\Pi_+\Pi_-=0$. Neither factor alone annihilates it, since $(Q_--Q_+)\Pi_-\neq0$ and $(Q_+-Q_-)\Pi_+\neq0$. If $Q_+=Q_-$, then $\breve Q=Q_+1$, so $X-Q_+$ annihilates and no nonzero constant does. A single linear factor, or a product of two distinct linear factors, is squarefree.

**Definition (defective).** An element is **defective** when its minimal polynomial has a repeated root.

**Corollary (semisimplicity).** Every element of $\mathbb{B}_{\mathrm r}$ is semisimple. There are no defective elements.

*Proof.* By the definition, a defective element has a minimal polynomial with a repeated root. By the theorem, every minimal polynomial is squarefree. Equivalently, the matrix of $L_{\breve Q}$ in the basis $(\Pi_+,\Pi_-)$ is diagonal, so every element is diagonalisable in its regular representation.

## The Spectral Criterion

**Theorem (the spectral criterion).** For $\breve Q$, the following are equivalent:

1. $Q_+\neq Q_-$;
2. $Q_\blacktriangledown\neq0$;
3. the two eigenvalues are distinct;
4. the discriminant $\Delta=4Q_\blacktriangledown^2$ is nonzero;
5. $\breve Q$ is not a scalar.

The negations are the equivalent conditions $Q_+=Q_-$, $Q_\blacktriangledown=0$, a repeated eigenvalue, a vanishing discriminant, and $\breve Q\in\mathbb{C}\cdot1$.

*Proof.* The identity $Q_+-Q_-=2Q_\blacktriangledown$ gives (1)$\iff$(2) and (3)$\iff$(4). The eigenvalues are $Q_\pm$ by the spectrum theorem, so (1)$\iff$(3). Finally, $Q_\blacktriangledown=0$ gives $\breve Q=Q_\blacktriangle 1$, and conversely a scalar has $Q_\blacktriangledown=0$; this is (2)$\iff$(5).

**Definition (spectral decomposition).** A **spectral decomposition** of $\breve Q$ is the one-term writing $\breve Q=Q_+1$ when $\breve Q$ is scalar, and otherwise a two-term writing
$$
\breve Q=\lambda_+e_+ +\lambda_-e_-
$$
with $\lambda_+\neq\lambda_-$ and nonzero idempotents $e_+,e_-$ satisfying
$$
e_+^{2}=e_+,\qquad e_-^{2}=e_-,\qquad e_+e_-=e_-e_+=0,\qquad e_++e_-=1.
$$

**Theorem (the decomposition is the idempotent decomposition).** For every $\breve Q$,
$$
\breve Q=Q_+\Pi_+ + Q_-\Pi_-.
$$
When $Q_+\neq Q_-$ this is the unique spectral decomposition of $\breve Q$. When $Q_+=Q_-$ it reduces to the one-term writing $\breve Q=Q_+1$.

*Proof.* The identity is the idempotent decomposition of *Reduced Biquaternion Space*. In the distinct case, $\breve Q\Pi_\pm=Q_\pm\Pi_\pm$, so the coefficients are the eigenvalues and the idempotents are the eigenprojections. The Lagrange formulas
$$
e_+=\frac{\breve Q-Q_-}{Q_+-Q_-}=\Pi_+,\qquad
e_-=\frac{\breve Q-Q_+}{Q_--Q_+}=\Pi_-
$$
show that any spectral idempotents are forced; equivalently, $\Pi_\pm$ are the only nontrivial idempotents (*Square Roots of One and the Idempotents of the Algebra of the Reduced Biquaternions*). In the scalar case, $\breve Q=Q_+(\Pi_++\Pi_-)=Q_+1$.

**Remark (degenerate is not defective).** The word **degenerate** here is spectral: it means that the two eigenvalues coincide. It does not mean defective. On the scalar line the spectrum degenerates, but the element is semisimple, with a linear minimal polynomial. In the reduced algebra no spectrally degenerate element is defective.

## The Eigenspaces

**Theorem (the eigenspaces are the idempotent lines).** If $Q_+\neq Q_-$, then
$$
E_{Q_+}=\mathbb{C}\Pi_+,\qquad E_{Q_-}=\mathbb{C}\Pi_-,
$$
each of complex dimension one. If $Q_+=Q_-$, then $E_{Q_+}=\mathbb{B}_{\mathrm r}$, of complex dimension two.

*Proof.* Write $v=v_+\Pi_+ +v_-\Pi_-$. Then
$$
\breve Qv=Q_+v_+\Pi_+ +Q_-v_-\Pi_-.
$$
For $\lambda=Q_+$, the equation $\breve Qv=Q_+v$ is $(Q_--Q_+)v_-\Pi_-=0$, hence $v_-=0$ when $Q_+\neq Q_-$; thus $v=v_+\Pi_+\in\mathbb{C}\Pi_+$. The other eigenvalue is the same with the signs exchanged. If $Q_+=Q_-$, then $\breve Q=Q_+1$ and every $v$ satisfies $\breve Qv=Q_+v$.

**Corollary (eigenbasis).** If $Q_+\neq Q_-$, the pair $(\Pi_+,\Pi_-)$ is a $\mathbb{C}$-basis of $\mathbb{B}_{\mathrm r}$ consisting of eigenvectors, with eigenvalues $(Q_+,Q_-)$. If $Q_+=Q_-$, every $\mathbb{C}$-basis of $\mathbb{B}_{\mathrm r}$ is an eigenbasis.

*Proof.* The idempotents $\Pi_\pm$ are nonzero, orthogonal and complete, hence linearly independent and spanning; they are eigenvectors by the theorem. In the scalar case every vector is an eigenvector.

## The Scalar Stratum

**Definition (the scalar line).** The **scalar line** is
$$
\mathbb{C}\cdot1=\{Q_\blacktriangle1:Q_\blacktriangle\in\mathbb{C}\}
=\{Q_\blacktriangledown=0\}
=\{Q_+=Q_-\}.
$$
It is a subalgebra isomorphic to $\mathbb{C}$, of complex dimension one and real dimension two. It is the fixed set of the involution $j\mapsto -j$.

**Theorem (the scalar stratum is the spectrally degenerate set).** For $\breve Q=Q_\blacktriangle1$,
$$
\sigma(\breve Q)=\{Q_\blacktriangle\},\qquad
p_{\breve Q}(X)=(X-Q_\blacktriangle)^{2},\qquad
m_{\breve Q}(X)=X-Q_\blacktriangle.
$$
The spectral decomposition is the one-term writing $\breve Q=Q_\blacktriangle1$, the eigenspace is all of $\mathbb{B}_{\mathrm r}$, and every basis is an eigenbasis. Conversely, every spectrally degenerate element lies on the scalar line.

*Proof.* The spectrum, the polynomials and the eigenspace are the formulas of the previous sections at $Q_+=Q_-=Q_\blacktriangle$. The converse is the spectral criterion.

**Remark (the scalar line is not the centre).** The algebra is commutative, so its centre is the whole algebra $\mathbb{B}_{\mathrm r}$. The line $\mathbb{C}\cdot1$ is the canonical copy of $\mathbb{C}$ inside the algebra, and the word *central* in *central line* refers to its scalar elements, not to the centre. Every element is central, but only the scalar line is spectrally degenerate.

**Remark (the two-term refinement).** A scalar can also be written $Q_\blacktriangle1=Q_\blacktriangle\Pi_+ +Q_\blacktriangle\Pi_-$, but the coefficients are equal, so this is not a spectral decomposition; it is the idempotent decomposition with a repeated eigenvalue.

## Contrast with the Biquaternion Cone

**The biquaternion algebra has a defective cone; the product structure removes it.**

In the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$, write $\tilde Q=Q_te_t+\vec Q$ and $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$. The characteristic polynomial is $(X-Q_t)^{2}+B^{2}$, with eigenvalues $Q_t\pm iB$ and discriminant $-4B^{2}$. On the cone $\mathcal{S}=\{B^{2}=0\}$ with $\vec Q\neq0$ the minimal polynomial is $(X-Q_t)^{2}$: the element is defective, the left multiplication has Jordan type $(2,2)$, and there is no eigenbasis. This is a genuine defective cone, of complex dimension three and real dimension six, minus its scalar line. The details are *The Spectrum*, §*The Two Cases*.

**Why the reduced algebra has none.** The algebra $\mathbb{B}_{\mathrm r}\cong\mathbb{C}\oplus\mathbb{C}$ is a product of two fields, hence **reduced**: its only nilpotent is zero, because a nilpotent has both idempotent coordinates nilpotent and a field has none. A defective element of a finite-dimensional algebra over $\mathbb{C}$ has a nonzero nilpotent part (*Nilpotent Elements and the Jordan–Chevalley Decomposition*). In $\mathbb{B}_{\mathrm r}$ the direct argument is shorter: a repeated eigenvalue means $Q_+=Q_-$, so $\breve Q=Q_+1$ is scalar, and a scalar is semisimple.

**The role of the matrix algebra.** The algebra $M_2(\mathbb{C})$ is not reduced: $\begin{pmatrix}0&1\\0&0\end{pmatrix}$ has square zero, and the nilpotent vector parts with $B^{2}=0$ are these nonzero nilpotents. Simplicity is not the point: $M_2(\mathbb{C})$ is simple and defective, while $\mathbb{C}\oplus\mathbb{C}$ is not simple and reduced. Both are semisimple; only the second is reduced, and reducedness removes the defect.

## Summary

The reduced biquaternion algebra is $\mathbb{C}\oplus\mathbb{C}$, with element $\breve Q=Q_+\Pi_+ +Q_-\Pi_-$. The eigenvalue problem is the pair of coordinates: $\sigma(\breve Q)=\{Q_+,Q_-\}$, because $\breve Q-\lambda1$ is a unit exactly when both $Q_+-\lambda$ and $Q_--\lambda$ are nonzero. The characteristic polynomial is $(X-Q_+)(X-Q_-)$, of discriminant $4Q_\blacktriangledown^2$; the minimal polynomial is its squarefree part, $(X-Q_+)(X-Q_-)$ when $Q_+\neq Q_-$ and $X-Q_+$ when $Q_+=Q_-$. In both cases it is squarefree, so every element is semisimple and there are no defective elements.

The criterion is $Q_+\neq Q_-$, equivalently $Q_\blacktriangledown\neq0$, equivalently a non-scalar element. Then the eigenspaces are the idempotent lines $\mathbb{C}\Pi_+$ and $\mathbb{C}\Pi_-$, each of complex dimension one, and the spectral decomposition is $\breve Q=Q_+\Pi_+ +Q_-\Pi_-$, unique because $\Pi_\pm$ are the only nontrivial idempotents. The spectrally degenerate set is the scalar line $\mathbb{C}\cdot1=\{Q_\blacktriangledown=0\}=\{Q_+=Q_-\}$; on it the spectrum is $\{Q_\blacktriangle\}$, the minimal polynomial is linear, the eigenspace is the whole algebra, and the spectral decomposition is $Q_\blacktriangle1$.

The biquaternion algebra $M_2(\mathbb{C})$ has a genuine defective cone at $B^{2}=0$ away from the scalar line; the reduced algebra $\mathbb{C}\times\mathbb{C}$ has no nonzero nilpotent, so a repeated eigenvalue forces a scalar, and a scalar is semisimple. The product structure removes the defect. The two conditions and their four combinations are the subjects of the two companion articles.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}_{\mathrm r}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$ | the reduced biquaternion algebra |
| $\breve Q=Q_\blacktriangle+jQ_\blacktriangledown$ | a general element |
| $\Pi_\pm=\tfrac12(1\pm j)$ | the two complementary idempotents |
| $Q_\pm=Q_\blacktriangle\pm Q_\blacktriangledown$ | the idempotent coordinates |
| $\sigma(\breve Q)=\{Q_+,Q_-\}$ | the spectrum |
| $p_{\breve Q}(X)=(X-Q_+)(X-Q_-)$ | the characteristic polynomial |
| $m_{\breve Q}(X)$ | the minimal polynomial, the squarefree part of $p_{\breve Q}$ |
| $\Delta=(Q_+-Q_-)^{2}=4Q_\blacktriangledown^{2}$ | the discriminant |
| $E_\lambda=\{v:\breve Qv=\lambda v\}$ | the eigenspace |
| $\mathbb{C}\cdot1=\{Q_\blacktriangledown=0\}=\{Q_+=Q_-\}$ | the scalar line |
| $Q_+Q_-=Q_\blacktriangle^{2}-Q_\blacktriangledown^{2}$ | the reduced norm |
| $\mathcal{S}=\{B^{2}=0\}$ | the biquaternion spectral-degenerate cone |

## Further Reading

- [Relations between the Reduced Norm and Spectral Regularity and Degeneracy](relations-between-the-reduced-norm-and-spectral-regularity-and-degeneracy.html), for the comparison of $Q_+Q_-$ with $(Q_+-Q_-)^{2}$, the independence of the conditions and the chain of invariants.
- [The Four Sectors of the Reduced Biquaternion Algebra](the-four-sectors-of-the-reduced-biquaternion-algebra.html), for the four nonempty cells, their dimensions and their closures.
- [Eigenvalue Decomposition and Eigenbasis of a Reduced Biquaternion](eigenvalue-decomposition-and-eigenbasis-of-a-reduced-biquaternion.html), for the eigenprojections, the Peirce decomposition and the eigenbasis.
- [Eigenbasis of a Reduced Biquaternion in Matrix Elements Representations](eigenbasis-of-a-reduced-biquaternion-in-matrix-elements-representations.html), for the $2\times2$ and $4\times4$ readings of the same decomposition.
- [Worked Examples of Eigenbasis a Reduced Biquaternion](worked-examples-of-eigenbasis-a-reduced-biquaternion.html), for the computed cases.
- [Norm and Invertibility in the Algebra of the Reduced Biquaternions](norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the unit criterion.
- [Zero Divisors of the Algebra of the Reduced Biquaternions](zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the two punctured idempotent lines.
- [The Spectrum](the-spectrum.html), for the defective cone and the Jordan type $(2,2)$.
- [Nilpotent Elements and the Jordan–Chevalley Decomposition](nilpotent-elements-and-the-jordan-chevalley-decomposition.html), for the semisimple and nilpotent parts.
