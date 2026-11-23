# __The Four Forms and Their Algebraic Norms at $n=2$__

## Introduction

**The star can be read in each slot or in neither, and this gives exactly four forms on $M_2(\mathbb{C})$ — two complex bilinear of inertia $(4,4)$ and two Hermitian of inertia $(8,0)$ — whose values at two equal arguments are the four algebraic norms.**

The article lists the four forms, proves which of them are symmetric and which conjugate-symmetric, computes their inertias over the reals, computes the four norms $\operatorname{tr}(X^{2})$, $\operatorname{tr}(X^{*}X)$, $\operatorname{tr}(XX^{*})$ and $\operatorname{tr}(X^{*}X^{*})$, proves that the determinant is the multiplicative norm and the Hilbert–Schmidt norm the definite one, and proves that no norm of the four is both. It assumes *The Hilbert–Schmidt Form at $n=2$* and *The Trace Form and Its Inertia on the Two Halves of $M_2(\mathbb{R})$*, and it takes the determinant from *The Element: Rank, Trace, Determinant, Characteristic Polynomial at $n=2$*.

On the biquaternion side the same four objects are developed in *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, and the dictionary between the two languages is *$M_2(\mathbb{C})$ Pauli Representation*.

## The Four Ways of Reading the Star

**Definition.** The **four forms** are

$$
P(X,Y)=\operatorname{tr}(XY),\quad H(X,Y)=\operatorname{tr}(X^{*}Y),\quad H'(X,Y)=\operatorname{tr}(XY^{*}),\quad \mathrm{Kr}(X,Y)=\operatorname{tr}(X^{*}Y^{*}).
$$

**Proposition.** There are exactly four, and they are the four choices of placing the conjugate transpose in the two slots of $\operatorname{tr}(XY)$.

**Proof.** Each slot accepts the star or not, which gives four combinations, and the trace pairs the second slot with the first, so no other placement produces a new function.

**Corollary.** The form $P$ is complex bilinear and symmetric; $H$ and $H'$ are sesquilinear and conjugate-symmetric; $\mathrm{Kr}$ is complex bilinear and symmetric.

**Proof.** The star is conjugate-linear, so a starred slot makes the form sesquilinear and contributes one conjugation to the symmetry; the two starred slots of $\mathrm{Kr}$ contribute two, which cancel.

**Corollary.** The four forms are not independent: $H'(X,Y)=H(Y,X)$ and $\mathrm{Kr}(X,Y)=\overline{P(X^{*},Y^{*})}$.

**Proof.** The first is the conjugate symmetry of $H$ read in the other order, and the second is the identity $\operatorname{tr}(X^{*}Y^{*})=\overline{\operatorname{tr}(XY)}$ applied to the starred pair.

## The Inertias

**Theorem.** Over the reals the four quadratic forms have the inertias $(4,4)$, $(8,0)$, $(8,0)$ and $(4,4)$.

**Proof.** On the Gram matrix of $P$ in the eight real matrices $E_{ij}$ and $iE_{ij}$ the eigenvalues are four positive and four negative; on that of $H$ they are eight positive; $H'$ has the same Gram matrix as $H$ after transposition of the pair; and $\mathrm{Kr}$ has the same as $P$ after conjugation.

**Corollary.** The two bilinear forms are indefinite of the maximal split type, and the two sesquilinear forms are positive definite.

**Proof.** A form of inertia $(4,4)$ on a real space of dimension eight has the maximal possible number of negative directions, and $(8,0)$ is the definite case.

**Corollary.** On the real matrices the four forms collapse in pairs: $P=\mathrm{Kr}$ and $H=H'$, because the star is the transpose there.

**Proof.** For real $X$ and $Y$ one has $\operatorname{tr}(X^{\mathsf T}Y^{\mathsf T})=\operatorname{tr}((YX)^{\mathsf T})=\operatorname{tr}(YX)=P(X,Y)$ and $\operatorname{tr}(XY^{\mathsf T})=\sum_{ij}x_{ij}y_{ij}=\operatorname{tr}(X^{\mathsf T}Y)$.

## The Four Algebraic Norms

**Definition.** The **algebraic norm** of a form is its value at two equal arguments: $P(X)=\operatorname{tr}(X^{2})$, $H(X)=\operatorname{tr}(X^{*}X)$, $H'(X)=\operatorname{tr}(XX^{*})$ and $\mathrm{Kr}(X)=\operatorname{tr}(X^{*}X^{*})$.

**Proposition.** The four norms are $\operatorname{tr}(X^{2})$, the sum of the squares of the moduli of the entries, the same sum, and the conjugate of $\operatorname{tr}(X^{2})$.

**Proof.** $H(X)=\sum_{ij}\lvert x_{ij}\rvert^{2}=H'(X)$ by the cyclic property of the trace, and $\mathrm{Kr}(X)=\overline{\operatorname{tr}(X^{2})}$.

**Corollary.** Two of the four norms are real and positive semidefinite, and the other two are complex and indefinite.

**Proof.** The first two are sums of squares; and $\operatorname{tr}(X^{2})$ takes the value $-2$ at $J$ and $2$ at $I$.

**Corollary.** The norm $P(X)$ is the sum of the squares of the eigenvalues, counted with multiplicity.

**Proof.** $\operatorname{tr}(X^{2})=\lambda_{1}^{2}+\lambda_{2}^{2}$, and the eigenvalues of a two-by-two matrix are the two roots of its characteristic polynomial.

**Corollary.** The norm $H(X)$ is the square of the Hilbert–Schmidt norm, and it vanishes only at the zero matrix.

**Proof.** The formula of *The Hilbert–Schmidt Form at $n=2$* identifies the two, and the sum of the squares of the moduli vanishes only when all entries vanish.

## Multiplicativity and Definiteness

**Theorem.** The determinant is multiplicative, $\det(XY)=\det X\det Y$, and it is the only one of the four norms that is multiplicative.

**Proof.** Multiplicativity is the product formula for the determinant. The norm $P$ fails at $X=E_{12}$ and $Y=E_{21}$: $P(XY)=1$ while $P(X)P(Y)=0$. The norm $H$ fails at the identity: $H(I)=2$ while $H(I)H(I)=4$, and the same pair of values applies to $H'$ and to $\mathrm{Kr}$.

**Corollary.** The determinant is not definite: it vanishes at every nilpotent, and the nilpotent $E_{12}$ is nonzero.

**Proof.** A nilpotent two-by-two matrix has the single eigenvalue $0$, so its determinant is $0$.

**Corollary.** No one of the four norms is both definite and multiplicative.

**Proof.** A definite multiplicative norm would vanish only at the zero matrix; the determinant is multiplicative and vanishes at $E_{12}$, and the other three are not multiplicative.

**Corollary.** The failure is the measure of the algebra being a full matrix algebra rather than a division algebra: a definite multiplicative norm exists on $\mathbb{H}$ and on $\mathbb{C}$, and not on $M_2(\mathbb{C})$.

**Proof.** On the quaternions the norm $\lvert a\rvert^{2}+\lvert b\rvert^{2}$ is multiplicative and definite, and the algebra is a division algebra; a nonzero nilpotent in $M_2(\mathbb{C})$ rules this out.

## The Two Real Forms

**Proposition.** On the real matrices the form $P$ is the trace form of inertia $(3,1)$, and the form $H$ is the entrywise product of inertia $(4,0)$.

**Proof.** For real matrices $X^{*}=X^{\mathsf T}$, so $P$ is $\operatorname{tr}(XY)$ and $H$ is $\operatorname{tr}(X^{\mathsf T}Y)$, and the inertias are those computed in *The Trace Form and Its Inertia on the Two Halves of $M_2(\mathbb{R})$* and *The Hilbert–Schmidt Form at $n=2$*.

**Proposition.** On the quaternionic real form, the matrices $X=\begin{pmatrix}a&b\\-\bar b&\bar a\end{pmatrix}$, the determinant is $\lvert a\rvert^{2}+\lvert b\rvert^{2}$, positive definite.

**Proof.** $\det X=a\bar a+b\bar b$ by the direct expansion of the two-by-two determinant.

**Corollary.** The two real forms separate by their norms: on $\mathbb{H}$ the determinant is definite, and on $M_2(\mathbb{R})$ it is indefinite of inertia $(2,2)$.

**Proof.** The determinant on $M_2(\mathbb{R})$ has the eigenvalues $1,1,-1,-1$ in the basis of matrix units, while on $\mathbb{H}$ it is a sum of two squares.

## The Names of the Corpus

**Proposition.** The plain form of the corpus corresponds to $P$, the Hermitian form to $H$, and the quaternionic algebraic norm to the determinant.

**Proof.** The plain form is the scalar part of the plain product, which is half the trace of the matrix product; the Hermitian form uses the Hermitian conjugation, which is the star; and the quaternionic norm is the determinant of the matrix model.

**Corollary.** The Krein form of the corpus is the form with the two conjugations, and at order two it is the conjugate of the plain form.

**Proof.** The two conjugations compose to the entrywise conjugation, which is the operation taking $P$ to $\mathrm{Kr}$.

## Summary

The four forms are $P(X,Y)=\operatorname{tr}(XY)$, $H(X,Y)=\operatorname{tr}(X^{*}Y)$, $H'(X,Y)=\operatorname{tr}(XY^{*})$ and $\mathrm{Kr}(X,Y)=\operatorname{tr}(X^{*}Y^{*})$, the four placements of the star, with the inertias $(4,4)$, $(8,0)$, $(8,0)$ and $(4,4)$ over the reals; the first and the last are complex bilinear and the middle two are Hermitian.

Their norms are $\operatorname{tr}(X^{2})$, the sum of the squares of the moduli of the entries twice, and the conjugate of $\operatorname{tr}(X^{2})$. The determinant is multiplicative but not definite, the Hilbert–Schmidt norm definite but not multiplicative, and no norm of the four is both: a nonzero nilpotent forbids it. On $\mathbb{H}$ the determinant is definite, on $M_2(\mathbb{R})$ it has the inertia $(2,2)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P(X,Y)$ | $\operatorname{tr}(XY)$, the plain form |
| $H(X,Y)$ | $\operatorname{tr}(X^{*}Y)$, the Hermitian form |
| $H'(X,Y)$ | $\operatorname{tr}(XY^{*})$, the Hermitian form in the other order |
| $\mathrm{Kr}(X,Y)$ | $\operatorname{tr}(X^{*}Y^{*})$, the form with two conjugations |
| $X^{*}$ | the conjugate transpose |
| $\det$ | the multiplicative norm |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the determinant, its multiplicativity and the nilpotent case.
- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the Hilbert–Schmidt norm and its submultiplicativity.
- [The Hilbert–Schmidt Form at $n=2$](the-hilbert-schmidt-form-at-n-2.html), for the definite form among the four.
- [The Trace Form and Its Inertia on the Two Halves of $M_2(\mathbb{R})$](the-trace-form-and-its-inertia-on-the-two-halves-of-m2r.html), for the split form among the four.
- [The Two Base Fields: $M_2(\mathbb{R})$ inside $M_2(\mathbb{C})$](the-two-base-fields-m2r-inside-m2c.html), for the two real forms on which the norms separate.
