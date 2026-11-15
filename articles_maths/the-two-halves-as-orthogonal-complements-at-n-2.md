# __The Two Halves as Orthogonal Complements at $n=2$__

## Introduction

**The symmetric and the antisymmetric halves are exact orthogonal complements for the trace form, and the reason is that the transpose is self-adjoint for that form.**

The article proves the orthogonality of the two halves over $\mathbb{R}$ and over $\mathbb{C}$, computes the Gram matrices of the trace form on each half with the eigenvalues $1,1,2$ and $-2$, states the general criterion by which the eigenspaces of an involution are orthogonal, and lists the orthogonal complements of the subspaces that recur in the series. It assumes *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$*, *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian at $n=2$* and *The Involutions of $M_2(\mathbb{C})$ over $\mathbb{R}$ and over $\mathbb{C}$*.

It defers the definite form on the complex algebra to *The Hilbert–Schmidt Form at $n=2$*, the signature statements to *The Trace Form and Its Signature on the Two Halves of $M_2(\mathbb{R})$*, and the subspaces of the triangular kind to *The Triangular Decomposition $h\oplus n_+\oplus n_-$ of $M_2(\mathbb{C})$*.

## The Two Forms on the Real Matrices

**Definition.** On $M_2(\mathbb{R})$ the **trace form** is $\langle X,Y\rangle=\operatorname{tr}(XY)$ and the **Hilbert–Schmidt form** is $\langle X,Y\rangle_{\mathrm{HS}}=\operatorname{tr}(X^{\mathsf T}Y)$.

**Proposition.** On the real matrices the two forms agree.

**Proof.** On real matrices $\operatorname{tr}(X^{\mathsf T}Y)=\sum_{i,j}x_{ij}y_{ij}$ and $\operatorname{tr}(XY)=\sum_{i,j}x_{ij}y_{ji}$, and the second sum is the first after renaming the indices.

**Both forms are nondegenerate.** The trace pairing of two matrix units is $\operatorname{tr}(E_{ij}E_{kl})=\delta_{jk}\delta_{il}$, so the four units form a basis dual to themselves and the form is nondegenerate; its signature on the four real dimensions is $(3,1)$, as *The Trace Form and Its Signature on the Two Halves of $M_2(\mathbb{R})$* proves.

## Orthogonality of the Two Halves

**Theorem.** For symmetric $H$ and antisymmetric $K$ one has $\operatorname{tr}(HK)=0$, so the two halves are orthogonal for the trace form.

**Proof.** $\operatorname{tr}(HK)=\operatorname{tr}((HK)^{\mathsf T})=\operatorname{tr}(K^{\mathsf T}H^{\mathsf T})=\operatorname{tr}((-K)H)=-\operatorname{tr}(KH)=-\operatorname{tr}(HK)$, using cyclicity in the last step; a real number equal to its negative is zero.

**Corollary.** $\Lambda^{2}\mathbb{R}^{2}=\operatorname{Sym}_2(\mathbb{R})^{\perp}$ and $\operatorname{Sym}_2(\mathbb{R})=(\Lambda^{2}\mathbb{R}^{2})^{\perp}$.

**Proof.** The two spaces are orthogonal, their dimensions add to $4$, and the form is nondegenerate, so each is the orthogonal complement of the other.

**The symmetry is what does the work.** The two halves are the eigenspaces of the transpose, and the transpose is self-adjoint for the trace form: $ \langle A^{\mathsf T},B\rangle=\operatorname{tr}(A^{\mathsf T}B)$ and $\langle A,B^{\mathsf T}\rangle=\operatorname{tr}(AB^{\mathsf T})$ agree.

## The Gram Matrices

**Proposition.** In the basis $E_{11},E_{22},E_{12}+E_{21}$ of $\operatorname{Sym}_2(\mathbb{R})$ the Gram matrix of the trace form is

$$
\begin{pmatrix}1&0&0\\ 0&1&0\\ 0&0&2\end{pmatrix},
$$

with eigenvalues $1,1,2$, all positive.

**Proof.** $\operatorname{tr}(E_{11}^{2})=\operatorname{tr}(E_{22}^{2})=1$, the cross term $\operatorname{tr}(E_{11}E_{22})=0$, and $\operatorname{tr}((E_{12}+E_{21})^{2})=\operatorname{tr}(E_{12}E_{21}+E_{21}E_{12})=2$.

**Proposition.** On the antisymmetric line, spanned by $J$, the trace form is $-2$.

**Proof.** $J^{2}=-I$, so $\operatorname{tr}(J^{2})=-2$.

**Corollary.** The trace form is positive definite on the symmetric half and negative definite on the antisymmetric line, so its signature on $M_2(\mathbb{R})$ is $(3,1)$.

**Proof.** The two halves are orthogonal and carry definite forms of ranks $3$ and $1$.

**The antisymmetric direction is the timelike one.** A matrix $H+kJ$ with $H$ symmetric has $\operatorname{tr}((H+kJ)^{2})=\operatorname{tr}(H^{2})-2k^{2}$, so the set $\{\operatorname{tr}(X^{2})=0\}$ is a genuine cone in four real dimensions, with the line $\mathbb{R}J$ inside it.

## The Involution Criterion

**Theorem.** Let $\theta$ be an involution of $M_2(\mathbb{R})$ or of $M_2(\mathbb{C})$ that is self-adjoint for a bilinear form, that is $\langle\theta X,Y\rangle=\langle X,\theta Y\rangle$. Then the two eigenspaces of $\theta$ are orthogonal.

**Proof.** For $X$ in the $+1$ eigenspace and $Y$ in the $-1$ eigenspace, $\langle X,Y\rangle=\langle\theta X,Y\rangle=\langle X,\theta Y\rangle=-\langle X,Y\rangle$, so the pairing vanishes.

**Corollary (the real case).** The transpose is self-adjoint for the trace form, so the symmetric and the antisymmetric halves are orthogonal.

**Corollary (the complex case).** The conjugate transpose is self-adjoint for the Hermitian form $\langle X,Y\rangle=\operatorname{tr}(X^{*}Y)$, so $\operatorname{Herm}_2$ and $\mathfrak{u}(2)$ are orthogonal for it.

**Proof.** For that form $\langle\theta X,Y\rangle=\operatorname{tr}(XY)$ and $\langle X,\theta Y\rangle=\operatorname{tr}(X^{*}Y^{*})=\operatorname{tr}((YX)^{*})=\overline{\operatorname{tr}(YX)}=\overline{\operatorname{tr}(XY)}$, so the two sides are conjugate and the form is Hermitian, which is the self-adjointness required.

**The criterion is the whole mechanism.** Every orthogonal split in the series comes from an involution that is self-adjoint for the form in use, and the list of splits is the list of involutions of *The Involutions of $M_2(\mathbb{C})$ over $\mathbb{R}$ and over $\mathbb{C}$*.

## The Complex Case and the Two Forms

**Theorem.** For $H$ Hermitian and $K$ anti-Hermitian the real number $\operatorname{Re}\operatorname{tr}(H^{*}K)$ is zero, so the two halves are orthogonal for the real part of the Hermitian form.

**Proof.** $\operatorname{tr}(H^{*}K)=\operatorname{tr}(HK)$ and $K=iS$ with $S$ Hermitian, so $\operatorname{tr}(HK)=i\operatorname{tr}(HS)$ is purely imaginary by the trace statement of *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian at $n=2$*; its real part vanishes.

**Proposition.** The two halves are not orthogonal for the complex bilinear form $\operatorname{tr}(XY)$.

**Proof.** With $H=I$ and $K=iI$ one has $\operatorname{tr}(HK)=2i\neq0$, and $I$ is Hermitian while $iI$ is anti-Hermitian.

**Corollary.** Over $\mathbb{C}$ the correct orthogonal complement statement uses the real part of the Hilbert–Schmidt form, and the complex bilinear form does not see the split.

**Proof.** The real part is positive definite, so the orthogonal complement of a subspace has the complementary dimension; the complex bilinear form is not definite and pairs the two halves.

## The Complements of the Recurring Subspaces

**Proposition.** For the trace form on $M_2(\mathbb{C})$,

$$
(\mathbb{C}I)^{\perp}=\mathfrak{sl}_2(\mathbb{C}),\qquad
(\mathfrak{sl}_2(\mathbb{C}))^{\perp}=\mathbb{C}I,\qquad
(\text{diagonal})^{\perp}=\mathbb{C}E_{12}\oplus\mathbb{C}E_{21} .
$$

**Proof.** $\operatorname{tr}(X)=0$ is the condition $\langle X,I\rangle=0$, and it defines the traceless space of dimension $3$. For the diagonal space, $\langle E_{ii},E_{12}\rangle=\operatorname{tr}(E_{ii}E_{12})=0$, and the off-diagonal space has dimension $2$, which is $4-2$.

**Proposition.** In the standard frame the orthogonal complement of the corner $A_{kl}$ is spanned by the three units other than $E_{lk}$.

**Proof.** $\operatorname{tr}(E_{kl}E_{mn})=\delta_{lm}\delta_{kn}$, so two matrix units pair nontrivially exactly when each is the transpose of the other.

**The corner statement is the origin of the transpose pairing.** The matrix units are paired by the trace exactly along the transpose, which is why the corner decomposition of *The Fine Decomposition against the Diagonal at $n=2$* and the trace form fit together.

## Summary

On the real matrices the trace form and the Hilbert–Schmidt form agree and are nondegenerate of signature $(3,1)$. The symmetric and the antisymmetric halves are orthogonal, because the transpose is self-adjoint for the trace form; the Gram matrix on the symmetric half is $\operatorname{diag}(1,1,2)$ and the form on the antisymmetric line is $-2$, so the symmetric half is positive definite and the antisymmetric line is negative definite and timelike.

The same argument with the conjugate transpose gives the orthogonality of $\operatorname{Herm}_2$ and $\mathfrak{u}(2)$ for the real part of the Hermitian form, while the complex bilinear form $\operatorname{tr}(XY)$ does not vanish on the pair $I,iI$ and therefore does not see the split. The complements of the recurring subspaces are $\mathfrak{sl}_2$ for the scalars, the off-diagonal span for the diagonal, and all units but the transpose for a corner.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle X,Y\rangle$ | the trace form $\operatorname{tr}(XY)$ |
| $\langle X,Y\rangle_{\mathrm{HS}}$ | the Hilbert–Schmidt form $\operatorname{tr}(X^{\mathsf T}Y)$ |
| $\operatorname{tr}(X^{*}Y)$ | the Hermitian form on the complex algebra |
| $W^{\perp}$ | the orthogonal complement for the form in use |
| $(3,1)$ | the signature of the trace form on $M_2(\mathbb{R})$ |
| $\operatorname{Herm}_2$, $\mathfrak{u}(2)$ | the two complex halves |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the trace pairing, its definiteness and the Gram matrices of the symmetric and skew spaces.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for the criterion by which the eigenspaces of a self-adjoint involution are orthogonal.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$](the-two-halves-over-r-symmetric-and-antisymmetric-at-n-2.html), for the two halves and their bracket.
- [The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian at $n=2$](the-two-halves-over-c-hermitian-and-skew-hermitian-at-n-2.html), for the complex halves and their traces.
- [The Involutions of $M_2(\mathbb{C})$ over $\mathbb{R}$ and over $\mathbb{C}$](the-involutions-of-m2c-over-r-and-over-c.html), for the list of involutions that produce the splits.
