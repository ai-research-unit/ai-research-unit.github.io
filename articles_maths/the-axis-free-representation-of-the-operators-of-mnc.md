# __The Axis-Free $M_{n^2}(\mathbb{C})$ Representation of the Operators of $M_n(\mathbb{C})$__

## Introduction

**The question.** How is an operator on $M_n(\mathbb{C})$ written as an $n^2\times n^2$ matrix, and what is the status of the transpose that appears in the right multiplication?

**The answer in one line.** Column stacking gives, with no further choice,
$$
L_A=\mathrm I\otimes A,\qquad R_B=B^{\mathsf T}\otimes\mathrm I,\qquad T_{A,B}=B^{\mathsf T}\otimes A,
$$
and the transpose on $B$ cannot be removed by a change of carrier basis for $n\ge2$.

**Why the article is needed.** The biquaternion series wrote every operator in one $4\times4$ frame and called the resulting form axis-free because no imaginary unit had to be chosen. At general $n$ there is no imaginary unit to choose, but there is still a convention, and the transpose in $R_B$ is not a convention: it is the trace of the anti-representation law. A reader who tries to remove it will change the operator.

**Boundaries.** The families are *The Endomorphisms of $M_n(\mathbb{C})$*; the basis-free discussion of the two sides is *The Transposition of the Two Sides of $M_n(\mathbb{C})$*; the Weyl basis is *The Generalized Pauli Representation of the Operators of $M_n(\mathbb{C})$*. The biquaternion original is *$M_4(\mathbb{C})$ Axis-Free Representation*.

**Conventions.** $\operatorname{vec}$ is column stacking: $\operatorname{vec}X$ is the column with entries $X_{11},X_{21},\dots,X_{nn}$. The Kronecker product is the standard one, and $E_{ij}$ are the matrix units.

## The Three Formulas

**Proposition.** $\operatorname{vec}(AXB)=(B^{\mathsf T}\otimes A)\operatorname{vec}X$.

*Proof.* Both sides are bilinear in $X$, so it suffices to take $X=E_{kl}$. Then $AE_{kl}B=A_{\cdot k}B_{l\cdot}$ has the entry $A_{ik}B_{lj}$ at $(i,j)$, while $\operatorname{vec}E_{kl}=e_l\otimes e_k$ and $(B^{\mathsf T}\otimes A)(e_l\otimes e_k)=(B^{\mathsf T}e_l)\otimes(Ae_k)$ has the same entry. $\square$

**The three cases.** $B=\mathrm I$ gives $L_A=\mathrm I\otimes A$; $A=\mathrm I$ gives $R_B=B^{\mathsf T}\otimes\mathrm I$; the general case is the product.

**The index pair.** In the operator matrix, the row index is the pair $(i,k)$ and the column index $(j,l)$, and the entry is $A_{ij}B_{lk}$. The left multiplication moves the first index of the pair, the right multiplication the second.

## Why the Transpose Sits on $B$

**The anti-representation law.** $R_BR_C=R_{CB}$. If $R_B$ were written as $\mathrm I\otimes B$ the product law would be $\mathrm I\otimes B\cdot\mathrm I\otimes C=\mathrm I\otimes BC$, which is the wrong order. The transpose is exactly what converts the reversed product into the direct one:
$$
(B^{\mathsf T}\otimes\mathrm I)(C^{\mathsf T}\otimes\mathrm I)=(CB)^{\mathsf T}\otimes\mathrm I .
$$

**The one-line reason.** Column stacking reads $XB$ column by column, and the columns of $XB$ are the columns of $X$ acted on by $B^{\mathsf T}$ on the left.

**The consequence.** The transpose is not a defect of the notation. It records that the right action is an action of the opposite algebra, and any faithful matrix realisation of that action must contain an order-reversing map.

## Can the Transpose Be Removed?

**The row-stacking alternative.** If $X$ is stacked by rows instead, the two formulas exchange roles: $L_A=A^{\mathsf T}\otimes\mathrm I$ and $R_B=\mathrm I\otimes B$. The transpose moves to the other slot; it does not disappear.

**Proposition.** There is no invertible $S$ with $SBS^{-1}=B^{\mathsf T}$ for all $B\in M_n$ when $n\ge2$.

*Proof.* The map $B\mapsto B^{\mathsf T}$ is an anti-automorphism: $(BC)^{\mathsf T}=C^{\mathsf T}B^{\mathsf T}$, whereas an inner map is an automorphism. An anti-automorphism that is also inner would be an automorphism, and then $BC=CB$ for all $B,C$. $\square$

**The single-operator case.** For a single $B$ the transpose can be avoided exactly when $B$ is symmetric: then $B^{\mathsf T}=B$ and $R_B=\mathrm I\otimes B$. So the transpose is removable operator by operator, on the locus of symmetric parameters, and not uniformly.

**The locus.** The symmetric parameters form a complex subspace of dimension $n(n+1)/2$ inside $M_n$, so the removable locus is a proper subvariety of the parameter space, of codimension $n(n-1)/2$.

## The Change of Frame

**What a change of frame does.** Conjugating all operators by $P\otimes P$ for $P$ invertible replaces $A$ by $PAP^{-1}$ and $B^{\mathsf T}$ by $PB^{\mathsf T}P^{-1}=(P^{-\mathsf T}BP^{\mathsf T})^{\mathsf T}$. So the formula is preserved with $B$ replaced by $P^{-\mathsf T}BP^{\mathsf T}$.

**The invariant statement.** The pair of formulas is equivariant under the change of frame, and the transpose stays in the second slot. No choice of $P$ moves it to the first slot, because that would require $P^{-\mathsf T}BP^{\mathsf T}=B$ for all $B$, that is $P^{\mathsf T}P$ central, which makes $P$ a scalar multiple of an orthogonal matrix, and then $B^{\mathsf T}=B$ for all $B$.

**The unitary case.** For $P$ unitary the formula reads $R_B=\overline{P}\ldots$, and the transpose becomes a conjugation of the entries. This is the exact form in which the biquaternion series met it.

## The Case $n=2$

**The matrices.** At $n=2$, $L_A$ is the block matrix $\operatorname{diag}(A,A)$ and $R_B$ is the block matrix with blocks $B_{lk}\mathrm I$:
$$
R_B=\begin{pmatrix}B_{11}\mathrm I&B_{21}\mathrm I\\ B_{12}\mathrm I&B_{22}\mathrm I\end{pmatrix}.
$$

**Why it looked removable.** At $n=2$ the transpose $B\mapsto B^{\mathsf T}$ is the quaternion conjugation in the coefficient frame, and that conjugation is written by a permutation matrix of the $4$-dimensional carrier. So the transpose has a name and a matrix, and the biquaternion series could absorb it into the frame. At $n\ge3$ the transpose has no such name: it is not inner, and it is not a conjugation by an element of the algebra.

**What is genuinely axis-free.** At every $n$ the formulas need no choice of imaginary unit, no choice of a maximal torus and no choice of a Cartan subalgebra. The only choice is the stacking convention, and the two conventions differ by the flip of the two slots.

## Two Consequences

**The spectra in the frame.** $L_A$ and $R_{B}$ have the eigenvalues of $A$ and of $B$, each repeated $n$ times, because $\mathrm I\otimes A$ and $B^{\mathsf T}\otimes\mathrm I$ are Kronecker products. The transpose in $R_B$ preserves the spectrum, since $B$ and $B^{\mathsf T}$ have the same characteristic polynomial.

**The invariants.** $\operatorname{tr}T_{A,B}=n\operatorname{tr}A\operatorname{tr}B$ and $\det T_{A,B}=(\det A\det B)^n$, both read off from the Kronecker product. The rank is $(\operatorname{rank}A)(\operatorname{rank}B)$.

**The table.**

| $n$ | $n^2$ = carrier of operators | $n^4$ = operator dimension | $n(n+1)/2$ symmetric parameters |
|---|---|---|---|
| $2$ | $4$ | $16$ | $3$ |
| $3$ | $9$ | $81$ | $6$ |
| $4$ | $16$ | $256$ | $10$ |
| $5$ | $25$ | $625$ | $15$ |

## The Finite Check

Computed with numpy for $n=2,3,4,5$ on random complex $A,B,X$: the residual $\lVert\operatorname{vec}(AXB)-(B^{\mathsf T}\otimes A)\operatorname{vec}X\rVert$ is below $10^{-14}$; the same for the two one-sided cases. The product law was checked by comparing $R_BR_C$ with $R_{CB}$ entrywise, and the residual with the untransposed form $\mathrm I\otimes B$ is bounded away from zero.

The search for a global $S$ was run as a least-squares problem on the $n^4\times n^2$ system $SB-B^{\mathsf T}S=0$ over all $B$ in a basis: the solution space has dimension $0$ for $n\ge2$, so no such $S$ exists, in agreement with the anti-automorphism argument. At $n=2$ the transpose matrix is the $4\times4$ permutation of trace $2$ and determinant $-1$.

## The Two Conventions

**The column convention.** With $\operatorname{vec}(X)$ stacking the columns, $\operatorname{vec}(AXB)=(B^{\mathsf T}\otimes A)\operatorname{vec}(X)$, so $L_A=\mathrm I\otimes A$, $R_B=B^{\mathsf T}\otimes\mathrm I$ and $T_{A,B}=B^{\mathsf T}\otimes A$.

**The row convention.** With $\operatorname{vec}(X)$ stacking the rows, the same computation gives $L_A=A\otimes\mathrm I$, $R_B=\mathrm I\otimes B^{\mathsf T}$ and $T_{A,B}=A\otimes B^{\mathsf T}$.

**The relation.** The two conventions differ by the flip of the two tensor factors, which is the permutation matrix of the swap. Both are correct, and the choice is a convention; the transpose on the right parameter appears in both, on the left factor in one and on the right factor in the other.

**The check.** In the column convention the residual $\lVert\operatorname{vec}(AXB)-(B^{\mathsf T}\otimes A)\operatorname{vec}(X)\rVert$ is below $10^{-15}$ at $n=2,3,4,5$, and in the row convention $\lVert\operatorname{vec}(AXB)-(A\otimes B^{\mathsf T})\operatorname{vec}(X)\rVert$ is below $10^{-15}$.

**The warning.** A computation that mixes the two conventions produces the formula $\mathrm I\otimes A$ for $L_A$ and $B\otimes\mathrm I$ for $R_B$, which is wrong in both conventions: the parameter $B$ would be transposed in one and not in the other, and the error is invisible at $n=2$ for symmetric $B$.

## The Uniform Statement

**What cannot be removed.** There is no change of frame that removes the transpose for all parameters at once. The proof is the one above: it would make the transpose inner, and the transpose is an anti-automorphism.

**What can be removed.** For a single parameter the transpose can be moved into the frame, because $B^{\mathsf T}$ is similar to $B$: both have the same rational canonical form. The change of frame is not unitary in general, and it is not induced by an automorphism of the algebra.

**The honest reading.** "The transpose cannot be removed" is a statement about uniformity, not about a single operator. A frame exists in which $R_B= B\otimes\mathrm I$ for one fixed $B$; no frame exists in which this holds for every $B$.

**The unitary case.** If the frame change is required to be unitary, the removal is possible only when $B$ is unitarily similar to its transpose, which fails for a generic $B$ with a complex spectrum: the spectrum of $B^{\mathsf T}$ is that of $B$, and a unitary similarity preserves the spectrum, so the condition is that the spectrum be closed under conjugation.

**The consequence for $n=2$.** At $n=2$ every symmetric parameter has $B^{\mathsf T}=B$, and the generic $2\times2$ matrix is not symmetric, so even at $n=2$ the removal is operator by operator and not uniform.

## The Rank and the Trace

**The trace.** $\operatorname{tr}T_{A,B}=\operatorname{tr}A\operatorname{tr}B$, since the eigenvalues are the products.

**The determinant.** $\det T_{A,B}=(\det A)^{n}(\det B)^{n}$, since the eigenvalue list is the list of products.

**The rank.** $\operatorname{rank}T_{A,B}=\operatorname{rank}(A)\operatorname{rank}(B)$.

**The reading.** All three invariants factor through the two parameters, and all three are multiplicative. The frame sees only the products, which is why no invariant of the frame can separate the two factors.

## The Count

**The numbers.** The large matrices are $n^{2}\times n^{2}$: $16,81,256,625$ entries at $n=2,3,4,5$. The transpose in $R$ is the only place where the anti-representation law shows.

## Summary

Column stacking gives the three formulas with no axis chosen. The transpose on $B$ is forced by the anti-representation law of the right copy and cannot be removed by a change of frame for $n\ge2$. It can be removed operator by operator exactly on symmetric parameters. At $n=2$ it coincides with the quaternion conjugation, which is why the biquaternion series could treat it as part of the frame; at $n\ge3$ it is not inner and the coincidence disappears.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{vec}$ | column stacking |
| $\otimes$ | the Kronecker product |
| $L_A,R_B,T_{A,B}$ | the three families |
| $P\otimes P$ | a change of carrier frame |
| $n(n+1)/2$ | the dimension of the symmetric parameters |

## Further Reading
- Horn and Johnson, *Topics in Matrix Analysis* (Cambridge University Press, 1991), for the Kronecker product and $\operatorname{vec}$.
- [The Endomorphisms of $M_n(\mathbb{C})$](the-endomorphisms-of-mnc.html), for the tensor square.
- [The Transposition of the Two Sides of $M_n(\mathbb{C})$](the-transposition-of-the-two-sides-of-mnc.html), for the flip and the side exchange.
- [The Generalized Pauli Representation of the Operators of $M_n(\mathbb{C})$](the-generalized-pauli-representation-of-the-operators-of-mnc.html), for a basis adapted to the two sides.
- [$M_4(\mathbb{C})$ Axis-Free Representation](m4c-axis-free-representation.html), for the case $n=2$ in the coefficient frame.
- [Coda: $M_4(\mathbb{C})$ and the Kronecker Reading](coda-m4c-and-the-kronecker-reading.html), for the $n=2$ version of this article.
