# __The Two Halves as Orthogonal Complements__

## Introduction

**Whenever an involution preserves a form, its two eigenspaces are orthogonal for that form, and that single lemma produces the orthogonality of the two halves in every case the category uses.**

The article states and proves the lemma, applies it to the transpose with the trace bilinear form and to the conjugate transpose with the Hilbert–Schmidt form, and checks that in each case the two halves are not only orthogonal but complementary: the orthogonal complement of one half is the other. It then reads the two halves as the summands of an orthogonal direct sum, computes the restrictions of the form, notes that the matrix units are an orthonormal system for the Hilbert–Schmidt form while the two halves are not spanned by orthogonal lines of the coarse kind, and closes at $n=2$. It assumes *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric* and *The Two Halves over $\mathbb{C}$: Hermitian and Skew-Hermitian* for the two splits, and *The Involutions over $\mathbb{R}$ and over $\mathbb{C}$* for the involutions. It defers the signatures of the restrictions to *The Trace Form and Its Signature on the Two Halves* and the Hilbert–Schmidt form itself to *The Hilbert–Schmidt Form*.

## The Complement and the Lemma

**Two subspaces are orthogonal complements for a form when each is the annihilator of the other.** Let $B$ be a bilinear or Hermitian form on a space $V$ and $U\subseteq V$. Put

$$
U^{\perp}=\{v: B(u,v)=0\ \text{for all }u\in U\}.
$$

If $B$ is nondegenerate, then $\dim U^{\perp}=\dim V-\dim U$, and $V=U\oplus U^{\perp}$ as soon as $U\cap U^{\perp}=0$. The two conditions to check in each case are therefore the vanishing and the count.

**Lemma.** Let $\sigma$ be an involution of the algebra and $B$ a form with $B(\sigma A,\sigma C)=B(A,C)$ for all $A,C$. Then

$$
B(A,C)=0\qquad\text{for }A\in\operatorname{Fix}\sigma,\ C\in\operatorname{Anti}\sigma .
$$

*Proof.* Apply the invariance and then the eigenvalues:

$$
B(A,C)=B(\sigma A,\sigma C)=B(A,-C)=-B(A,C),
$$

so $2B(A,C)=0$. The same proof works for a Hermitian form and it works for the real part of a Hermitian form.

**The lemma is the whole content of the orthogonality, and it holds for every involution of the classification.** The transpose preserves the trace bilinear form, the conjugate transpose preserves the Hilbert–Schmidt form up to conjugation, the symplectic transpose preserves the same bilinear form, and the inner involutions preserve it too because they are conjugations by a unit. So the two halves are orthogonal in each case, and no case needs a separate computation.

## The Real Case

**The symmetric and antisymmetric halves are orthogonal complements for the trace bilinear form.** On $M_n(\mathbb{R})$ put $B(A,C)=\operatorname{tr}(A^{\mathsf T}C)$. The transpose satisfies $B(A^{\mathsf T},C^{\mathsf T})=\operatorname{tr}(AC^{\mathsf T})=\operatorname{tr}(C^{\mathsf T}A)=B(C,A)=B(A,C)$, so the lemma applies and

$$
\operatorname{tr}(S^{\mathsf T}K)=\operatorname{tr}(SK)=0\qquad(S^{\mathsf T}=S,\ K^{\mathsf T}=-K).
$$

The count closes the argument: $\dim\operatorname{Skew}_n=n(n-1)/2=n^{2}-n(n+1)/2$, so $\operatorname{Sym}_n^{\perp}=\operatorname{Skew}_n$ and

$$
M_n(\mathbb{R})=\operatorname{Sym}_n\perp\operatorname{Skew}_n .
$$

**The form is nondegenerate and its restriction to each half is definite.** For real $A$, $B(A,A)=\operatorname{tr}(A^{\mathsf T}A)=\sum_{ij}A_{ij}^{2}\ge0$ with equality only at $A=0$, so the form is positive definite on the whole algebra. On the symmetric half it is positive definite, of signature $\big(\tfrac{n(n+1)}{2},0\big)$; on the antisymmetric half it is negative definite, since $\operatorname{tr}(K^{2})=-\sum_{i<j}2K_{ij}^{2}$, of signature $\big(0,\tfrac{n(n-1)}{2}\big)$.

**The two projections are orthogonal projections for this form.** The maps $A\mapsto\tfrac12(A+A^{\mathsf T})$ and $A\mapsto\tfrac12(A-A^{\mathsf T})$ are idempotent with orthogonal images, and they are self-adjoint for $B$:

$$
B\big(\tfrac12(A+A^{\mathsf T}),C\big)=B\big(A,\tfrac12(C+C^{\mathsf T})\big),
$$

which was verified for random pairs at $n=2,3,4$. A self-adjoint idempotent is the orthogonal projection onto its image, so the split is the orthogonal direct sum in the strongest sense.

## The Complex Case

**The Hermitian and skew-Hermitian halves are orthogonal complements for the real part of the Hilbert–Schmidt form.** Put $\langle A,C\rangle=\operatorname{tr}(A^{*}C)$ and let $B=\operatorname{Re}\langle\cdot,\cdot\rangle$, a real inner product on $M_n(\mathbb{C})$ of real dimension $2n^{2}$. The conjugate transpose satisfies

$$
\overline{\langle A^{*},C^{*}\rangle}=\operatorname{tr}(A C^{*})=\overline{\operatorname{tr}(A^{*}C)}=\overline{\langle A,C\rangle},
$$

so $\operatorname{Re}\langle A^{*},C^{*}\rangle=\operatorname{Re}\langle A,C\rangle$ and the lemma applies. Hence

$$
\operatorname{Re}\operatorname{tr}(H^{*}K)=0\qquad(H^{*}=H,\ K^{*}=-K),
$$

and since $\dim_{\mathbb{R}}\operatorname{Herm}_n=\dim_{\mathbb{R}}\operatorname{SkewHerm}_n=n^{2}$ with $2n^{2}$ the total,

$$
M_n(\mathbb{C})=\operatorname{Herm}_n\perp\operatorname{SkewHerm}_n .
$$

**The Hermitian form itself does not vanish on the pair, and the lemma is applied to its real part.** The number $\operatorname{tr}(H^{*}K)=\operatorname{tr}(HK)$ is purely imaginary, so its real part is zero and its imaginary part generally is not. The distinction is the one recorded in *The Two Halves over $\mathbb{C}$: Hermitian and Skew-Hermitian*: the two halves are orthogonal for the Euclidean structure and not for the Hermitian one, and every statement about orthogonality in the category means the Euclidean statement.

**The two forms give the same complement and different restrictions.** For the Hermitian form $\langle A,C\rangle$ the two halves have restrictions of signature $(n^{2},0)$ and $(0,n^{2})$ in the real sense, so each restriction is definite and the direct sum is orthogonal for the real part. What fails is only the vanishing of the complex-valued form on the pair, and that failure is the source of the symplectic structure of the following articles.

## The Matrix Units as an Orthonormal System

**The matrix units are orthonormal for the Hilbert–Schmidt form.** For all indices,

$$
\langle E_{ij},E_{kl}\rangle=\operatorname{tr}(E_{ij}^{*}E_{kl})=\operatorname{tr}(E_{ji}E_{kl})=\delta_{il}\delta_{jk},
$$

so the $n^{2}$ units form an orthonormal basis of $M_n(\mathbb{C})$ for the form, and the coordinates of $A$ in that basis are its entries. The identity was verified for all quadruples at $n=2,3,4$.

**The fine decomposition is therefore an orthogonal direct sum, and the coarse one is not spanned by its own lines.** The grading of *The Fine Decomposition against the Diagonal* splits the algebra into the $n^{2}$ lines $\mathbb{C}E_{ij}$, and those lines are mutually orthogonal for the Hilbert–Schmidt form. The two halves are spanned by these lines combined in pairs: the symmetric line $\mathbb{C}(E_{ij}+E_{ji})$ is orthogonal to the skew line $\mathbb{C}(E_{ij}-E_{ji})$, and this orthogonality is again the lemma applied to the transposed pair.

**Orthonormality gives the coordinates of the trace forms.** For $A=\sum A_{ij}E_{ij}$ and $C=\sum C_{ij}E_{ij}$,

$$
\operatorname{tr}(A^{*}C)=\sum_{i,j}\overline{A_{ij}}C_{ij},\qquad \operatorname{tr}(A^{\mathsf T}C)=\sum_{i,j}A_{ij}C_{ij}
$$

for real matrices, which are the two forms of the article written in the basis of units. The real part of the first is the Euclidean form of $\mathbb{R}^{2n^{2}}$, and the real part of the second is indefinite of signature $(n^{2},n^{2})$ on the complex algebra and of signature $(n(n+1)/2,\,n(n-1)/2)$ on the real matrices.

## What the Complementarity Gives

**An orthogonal direct sum splits every form into two forms and every quadratic form into two squares.** Since $M_n=\operatorname{Sym}\perp\operatorname{Skew}$,

$$
\operatorname{tr}(A^{2})=\operatorname{tr}(S^{2})+\operatorname{tr}(K^{2})
$$

for $A=S+K$ real, the cross term vanishing by orthogonality. The quadratic form $\operatorname{tr}(A^{2})$ is therefore the sum of a positive definite form on the symmetric half and a negative definite one on the skew half, and its signature is read from the two halves separately.

**The complementarity makes the projections computable and the adjoints visible.** The orthogonal projection onto a half is $\tfrac12(\mathrm{I}\pm\sigma)$, and the adjoint of a map that preserves the split is computed half by half. The same mechanism is used for the operator space of *The Symmetric and Antisymmetric Parts of the Operator Space*, where the two-sided operators carry their own split.

**The complementarity does not survive every form.** For a form that the involution does not preserve, the two halves are not orthogonal: the Killing form of $\mathfrak{so}(n)$ vanishes at $n=2$ while the trace form does not, and on a non-reductive algebra the radical is its own orthogonal complement. The condition of the lemma is a real hypothesis, and the article *The Killing Form, Its Radical and the Triangular Case* records what happens when it fails.

## The Case $n=2$

**At $n=2$ the real split is $4=3\perp1$.** The symmetric half is spanned by $\mathrm{I},\sigma_1,\sigma_3$ and the antisymmetric half by $J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, and

$$
\operatorname{tr}(\mathrm{I}J)=\operatorname{tr}(\sigma_1J)=\operatorname{tr}(\sigma_3J)=0,
$$

so the single skew direction is orthogonal to the three symmetric ones. The form has signature $(3,1)$ on $M_2(\mathbb{R})$.

**At $n=2$ the complex split is $8=4\perp4$.** The Hermitian half is spanned over $\mathbb{R}$ by the Pauli list and the skew-Hermitian half by $i$ times it, and the two four-dimensional real spaces are orthogonal for the Euclidean form. In the biquaternion reading this is the split into the two sectors, and the orthogonality is the statement that the sectors do not mix under the Hilbert–Schmidt form.

**The complementarity is the statement the two halves are the annihilator of each other, and that is what makes them a split and not a choice.** Any complement of $\operatorname{Skew}_n$ has dimension $n(n+1)/2$; only one of them is orthogonal to it and only one is the fixed half of the involution, and in the transpose case the two coincide. The triangular algebra $UT_n$ is a complement with the right dimension and neither property, which is the precise content of the next comparison.

## Summary

If an involution preserves a form, its two eigenspaces are orthogonal for that form. Applied to the transpose and the trace bilinear form this gives $M_n(\mathbb{R})=\operatorname{Sym}_n\perp\operatorname{Skew}_n$, with $\operatorname{Sym}_n^{\perp}=\operatorname{Skew}_n$ by the dimension count $n(n+1)/2+n(n-1)/2=n^{2}$; applied to the conjugate transpose and the real part of the Hilbert–Schmidt form it gives $M_n(\mathbb{C})=\operatorname{Herm}_n\perp\operatorname{SkewHerm}_n$ with $n^{2}+n^{2}=2n^{2}$. The Hermitian form itself is purely imaginary on the pair and does not vanish, so the orthogonality is Euclidean. The matrix units are orthonormal for the Hilbert–Schmidt form, so the fine decomposition is orthogonal, and the projections $\tfrac12(\mathrm{I}\pm\sigma)$ are the orthogonal projections. The complementarity fails exactly when the form is not preserved by the involution.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $B(A,C)=\operatorname{tr}(A^{\mathsf T}C)$ | the trace bilinear form on the real algebra |
| $\langle A,C\rangle=\operatorname{tr}(A^{*}C)$ | the Hilbert–Schmidt form on the complex algebra |
| $U^{\perp}$ | the annihilator of $U$ for the chosen form |
| $\operatorname{Fix}\sigma$, $\operatorname{Anti}\sigma$ | the two eigenspaces of the involution |
| $E_{ij}$ | the matrix unit, orthonormal for $\langle\cdot,\cdot\rangle$ |
| $\tfrac12(\mathrm{I}\pm\sigma)$ | the two projections onto the halves |
| $(3,1)$ and $(4,4)$ | the signatures at $n=2$ of the two forms |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for orthogonal projections, self-adjoint idempotents and orthogonal direct sums.
- Werner Greub, *Linear Algebra* (Springer, 1975), for nondegenerate forms, annihilators and the dimension count of a complement.
- Rajendra Bhatia, *Positive Definite Matrices* (Princeton, 2007), for the Hilbert–Schmidt form and the geometry of the cone.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric](the-two-halves-over-r-symmetric-and-antisymmetric.html), for the real split and the trace form on each half.
- [The Two Halves over $\mathbb{C}$: Hermitian and Skew-Hermitian](the-two-halves-over-c-hermitian-and-skew-hermitian.html), for the complex split and the purely imaginary cross term.
- [The Fine Decomposition against the Diagonal](the-fine-decomposition-against-the-diagonal.html), for the weight lines that the orthonormal units span.
- [The Involutions over $\mathbb{R}$ and over $\mathbb{C}$](the-involutions-over-r-and-over-c.html), for the classification of the involutions that the lemma applies to.
