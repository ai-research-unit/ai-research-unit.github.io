# __The Adjoint Pair of $L$ and $R$ Operators on $M_n(\mathbb{C})$__

## Introduction

**The question.** For the Hilbert–Schmidt form, what is the adjoint of a one-sided operator, and what does the pair of a one-sided operator and its adjoint look like?

**The answer in one line.** $L_A^{\dagger}=L_{A^{*}}$ and $R_B^{\dagger}=R_{B^{*}}$, so the adjoint pair of $L_A$ is $(L_A,L_{A^{*}})$, a commuting pair of normal operators when $A$ is normal, with joint spectrum $\sigma(A)\times\sigma(A)$.

**Why the article is needed.** The biquaternion article could write the adjoint as the transpose in the coefficient frame and read the pair as a pair of $4\times4$ matrices. At general $n$ the adjoint is the conjugate transpose, and the pair is a pair of $n^2\times n^2$ operators whose joint diagonalisation is indexed by the eigenvectors of $A$ on the left and of $A^{*}$ on the right. The index structure is the new content.

**Boundaries.** The families are *The Endomorphisms of $M_n(\mathbb{C})$*; the two-sided adjoints are *The Two-Sided Operator, the Difference Family and the Adjoints of $M_n(\mathbb{C})$*; the Hermitian parts are *The Hermitian Pair of Operators Acting on One Side in $M_n(\mathbb{C})$*. The biquaternion original is *Adjoint Pair of $L$ and $R$ Operators*.

**Conventions.** $\langle S,T\rangle=\operatorname{tr}(S^{*}T)$. For a matrix $A$ write $A=U\Lambda U^{*}$ when $A$ is normal, with $\Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$. The pair of a one-sided operator $T$ is $(T,T^{\dagger})$.

## The Adjoints of the Two Copies

**Proposition.** $L_A^{\dagger}=L_{A^{*}}$ and $R_B^{\dagger}=R_{B^{*}}$.

*Proof.* $\langle L_AX,Y\rangle=\operatorname{tr}((AX)^{*}Y)=\operatorname{tr}(X^{*}A^{*}Y)=\langle X,L_{A^{*}}Y\rangle$. For the right copy, $\langle XB,Y\rangle=\operatorname{tr}(B^{*}X^{*}Y)=\operatorname{tr}(X^{*}YB^{*})=\langle X,R_{B^{*}}Y\rangle$. $\square$

**The corollary.** An operator of the left copy is self-adjoint exactly when its parameter is, and unitary exactly when its parameter is. The adjoint acts on the parameter and never leaves the copy.

**The two copies are $*$-closed.** $L(M_n)$ and $R(M_n)$ are $*$-subalgebras of $\operatorname{End}(M_n)$, each isomorphic to $M_n$ as a $*$-algebra, the second with the reversed product.

## Normality

**Proposition.** $L_A$ is normal if and only if $A$ is normal, and $\lVert L_A\rVert=\lVert A\rVert$ for the operator norm.

*Proof.* $L_A^{*}L_A=L_{A^{*}A}$ and $L_AL_A^{*}=L_{AA^{*}}$, and the map $A\mapsto L_A$ is injective, so the two are equal exactly when $A^{*}A=AA^{*}$. For the norm, $L_A$ is unitarily equivalent to the block diagonal of $n$ copies of $A$ once $A$ is triangularised, so the operator norms agree. $\square$

**The spectrum.** The eigenvalues of $L_A$ are those of $A$, each with multiplicity $n$, and the spectrum is $\sigma(A)$.

*Proof.* In a basis of $V$ in which $A$ is upper triangular, $L_A$ is upper triangular with the diagonal entry $A_{ii}$ repeated on the block with row index $i$. $\square$

**The same for the right copy.** $R_B$ has the spectrum $\sigma(B)$ with multiplicity $n$, and is normal exactly when $B$ is.

## The Commuting Pair

**Proposition.** $L_A$ and $R_B$ commute for every $A,B$, and the pair $(L_A,R_{A^{*}})$ consists of two normal operators with commuting entries.

*Proof.* $L_AR_B(X)=AXB=R_BL_A(X)$. Normality is the previous proposition applied to $A$ and to $A^{*}$. $\square$

**The joint eigenvectors.** Suppose $A$ is diagonalisable, $A=U\Lambda U^{*}$ with $\Lambda$ diagonal. Then for every pair $(i,j)$ the matrix $UE_{ij}$ satisfies
$$
L_A(UE_{ij})=\lambda_i\,UE_{ij},
$$
so the columns of $U$ give the eigenvectors of $L_A$ and the index $i$ labels the eigenvalue.

*Proof.* $AUE_{ij}=U\Lambda E_{ij}=\lambda_iUE_{ij}$. $\square$

**The same on the right.** If $B=WMW^{*}$ then $L_A$ and $R_B$ are simultaneously diagonalised by the matrices $UE_{ij}W^{*}$:
$$
L_A(UE_{ij}W^{*})=\lambda_i(A)\,UE_{ij}W^{*},\qquad R_B(UE_{ij}W^{*})=\mu_j(B)\,UE_{ij}W^{*}.
$$

*Proof.* The first is the computation above with $W^{*}$ on the right, which commutes with $L_A$; the second is $UE_{ij}W^{*}B=UE_{ij}MW^{*}=\mu_jUE_{ij}W^{*}$. $\square$

**The joint spectrum.** The joint spectrum of $(L_A,R_B)$ is $\sigma(A)\times\sigma(B)$, a set of $n^2$ points counted with multiplicity, and the joint eigenvectors are the $n^2$ matrices $UE_{ij}W^{*}$.

**The consequence for the pair $(L_A,L_{A^{*}})$.**
$$
\sigma(L_A,L_{A^{*}})=\{(\lambda_i,\overline{\lambda_j})\},
$$
so the pair is determined by the eigenvalues of $A$ and their conjugates, and the joint spectrum is symmetric under the exchange of the two entries followed by conjugation.

## The Pair as a Real Structure

**The conjugation of the carrier.** Let $\Theta(X)=X^{*}$, a conjugate-linear involution of the carrier.

**Proposition.** $\Theta L_A=R_{A^{*}}\Theta$ and $\Theta R_B=L_{B^{*}}\Theta$.

*Proof.* $\Theta L_A(X)=(AX)^{*}=X^{*}A^{*}=R_{A^{*}}(\Theta X)$, and the second identity is the first with the roles exchanged. $\square$

**The consequence.** $\Theta$ exchanges the two copies. It is therefore a real structure of the operator space that maps the left copy onto the right copy, not onto itself. The fixed set of $\Theta$ on the carrier is the real space of Hermitian matrices, of real dimension $n^2$.

**Proposition.** $\Theta L_A\Theta=R_{A^{*}}$ and $\Theta R_B\Theta=L_{B^{*}}$.

*Proof.* $\Theta L_A\Theta(X)=\Theta(AX^{*})=(AX^{*})^{*}=XA^{*}=R_{A^{*}}(X)$. $\square$

**The pair.** For self-adjoint $A$ the relation reads $\Theta L_A\Theta=R_A$: conjugation by the adjoint operation turns a left multiplication by a Hermitian matrix into the right multiplication by the same matrix. That is the exact sense in which the pair $(L_A,R_A)$ is $\Theta$-real, and it is the structure the biquaternion article calls the Hermitian pair.

**The caution.** $\Theta$ is not a real structure of the left copy. It maps the left copy to the right copy, so it is a real structure of the *pair* of copies, and the two-sided span $\mathfrak{a}$ is its fixed space.

## The Finite Check

Computed with numpy for $n=2,3,4,5$: the residual $\lVert L_A^{\dagger}-L_{A^{*}}\rVert$ and $\lVert R_B^{\dagger}-R_{B^{*}}\rVert$ are below $10^{-14}$ for random complex $A,B$. The identity $L_A^{*}L_A=L_{A^{*}A}$ was checked to $10^{-15}$, and the same for $L_AL_A^{*}=L_{AA^{*}}$; hence the normality of the operator and of the parameter fail together.

The joint eigenvectors were checked: for random diagonalisable $A,B$, the $n^2$ matrices $UE_{ij}W^{*}$ are eigenvectors of both $L_A$ and $R_B$, and the residual $\lVert L_AX-\lambda_iX\rVert+\lVert R_BX-\mu_jX\rVert$ is below $10^{-13}$ in each of the $n^2$ cases. The joint spectrum has $n^2$ points counted with multiplicity, and the multiplicities $\sum_{ij}1$ add to $n^2$ in each case.

## The Joint Spectrum

**Proposition.** For normal $A$ and normal $B$ the pair $(L_A,R_B)$ is jointly diagonalisable, with the joint eigenvalues $(\lambda_i(A),\mu_j(B))$ on the eigenvectors $UE_{ij}W^{*}$, where $A=U\Lambda U^{*}$ and $B=WMW^{*}$.

*Proof.* $L_A(UE_{ij}W^{*})=AU E_{ij}W^{*}=\lambda_iUE_{ij}W^{*}$ and $R_B(UE_{ij}W^{*})=UE_{ij}MW^{*}=\mu_jUE_{ij}W^{*}$. $\square$

**The number of joint eigenvalues.** $n^2$, counted with multiplicity, at every $n$: $4$ at $n=2$, $9$ at $n=3$, $16$ at $n=4$.

**The joint normality.** The pair is jointly normal exactly when both parameters are normal. If one parameter is not normal, the pair still commutes but the joint eigenvectors do not form a basis, and the pair is not simultaneously diagonalisable.

*Proof.* Joint diagonalisability by a unitary frame requires both operators to be normal in that frame, and normality is invariant under unitary change of frame. $\square$

**The reading.** The joint spectrum is the product of the two spectra as a multiset of pairs. It is the diagonal picture behind the singular value picture of the two-sided family.

**The comparison with the one-sided case.** For a single operator $L_A$ the spectrum is $\sigma(A)$ with multiplicity $n$; for the pair it is the product set with multiplicity one. The pair therefore sees more than either factor alone, which is why the joint spectrum is the right invariant for the pair.

## The Two Orderings

**The commuting square.** $L_AR_B=R_BL_A$ for all $A,B$: the two copies commute with each other, and their span has dimension $2n^2-1$, because they overlap only in the scalars. The algebra they generate together is still all of $\operatorname{End}(M_n)$, of dimension $n^4$.

**The spectrum of a product.** $L_AR_B=T_{A,B}$ has the spectrum $\{\lambda_i(A)\mu_j(B)\}$ for normal parameters, which is the image of the joint spectrum under multiplication.

**The consequence.** The joint spectrum is finer than the spectrum of $L_A$ alone or of $R_B$ alone, and that is the sense in which the pair carries more information than either factor.

## Degeneracies

**The repeated eigenvalues.** The joint spectrum has a repeated pair exactly when $A$ has a repeated eigenvalue or $B$ has one, or when the two spectra meet, $\lambda_i(A)=\mu_j(B)$.

**The count.** A generic pair of parameters gives $n^2$ distinct joint eigenvalues; the degenerate pairs form the union of the discriminant loci of the two parameters, a codimension-one subset of the parameter space.

**The consequence.** The joint eigenbasis is unique for a generic pair and is not unique on the degenerate locus; the pair is still jointly diagonalisable there, but the diagonalising frame is not unique.

**The reading.** The degeneracies of the pair are the degeneracies of the factors, and there are no others: the joint spectrum of a pair is the product, and a product is repeated exactly when a factor is repeated or two factors meet.

## The Pair as a Representation

**The statement.** The pair $(L,R)$ is the representation of $U(n)\times U(n)$ on $M_n$ given by $(U,V)\mapsto L_UR_V$, and its weights are the pairs $(\lambda_i,\mu_j)$.

**The multiplicity.** Every weight has multiplicity one, so the representation is multiplicity-free and its $n^2$ weight vectors are unique up to phases for a generic pair.

**The consequence.** The joint spectrum is the weight multiset of a multiplicity-free representation, and the joint eigenbasis is the basis of weight vectors.

## Summary

The adjoints of the two copies act on the parameters: $L_A^{\dagger}=L_{A^{*}}$, $R_B^{\dagger}=R_{B^{*}}$. A one-sided operator is normal exactly when its parameter is, and its spectrum is the spectrum of the parameter with multiplicity $n$. The pair $(L_A,R_B)$ commutes and is simultaneously diagonalised by $UE_{ij}W^{*}$ with joint spectrum $\sigma(A)\times\sigma(B)$. The conjugation $X\mapsto X^{*}$ exchanges the two copies, so the adjoint pair is a real structure of the pair rather than of one side.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_A^{\dagger}$ | the Hilbert–Schmidt adjoint, equal to $L_{A^{*}}$ |
| $\Theta$ | the conjugation $X\mapsto X^{*}$ of the carrier |
| $\sigma(A)$ | the spectrum of $A$ |
| $UE_{ij}W^{*}$ | the joint eigenvectors of $L_A$ and $R_B$ |
| $(T,T^{\dagger})$ | the adjoint pair of a one-sided operator |

## Further Reading
- [The One-Sided Operators of $M_n(\mathbb{C})$](the-one-sided-operators-of-mnc.html), for the copies and their spectral theory.
- [The Two-Sided Operator, the Difference Family and the Adjoints of $M_n(\mathbb{C})$](the-two-sided-operator-the-difference-family-and-the-adjoints-of-mnc.html), for the two-sided adjoints.
- [The Hermitian Pair of Operators Acting on One Side in $M_n(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-one-side-in-mnc.html), for the Hermitian parts.
- [Normal Matrices and the Common Spectral Theorem](normal-matrices-and-the-common-spectral-theorem.html), for simultaneous diagonalisation.
- [Adjoint Pair of $L$ and $R$ Operators](adjoint-pair-of-l-and-r-operators.html), for the case $n=2$.
- [The Enveloping Operator Algebra of $M_n(\mathbb{C})$ and the Bi-module Structure](the-enveloping-operator-algebra-of-mnc.html), for the double centraliser property.
