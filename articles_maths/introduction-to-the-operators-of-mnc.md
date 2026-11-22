# __Introduction to the Operators of $M_n(\mathbb{C})$__

## Introduction

**The question.** Which operators on the matrix algebra $M_n(\mathbb{C})$ does this series study, how do they fit together, and in what order should they be read?

**The answer in one line.** Three families act on $M_n$,
$$
L_A(X)=AX,\qquad R_B(X)=XB,\qquad T_{A,B}(X)=AXB,
$$
they satisfy $T_{A,B}=L_AR_B=R_BL_A$, and every other object of the series is one of these three read through a basis, a block, an adjoint or a group action.

**Why the article is needed.** The biquaternion series is a single story of $4\times4$ matrices, and at $n=2$ the three families, the transpose, the conjugation and the structure group all sit in one frame. At general $n$ they separate: the elements are $n\times n$, the operators $n^2\times n^2$, the transpose is no longer a conjugation, and the two sides are no longer exchangeable by an element of the algebra. A reader who starts in the middle will import the $n=2$ habits.

**Boundaries.** The algebra itself is *The Matrix Algebra $M_n(\mathbb{C})$*. The one-sided families are *The One-Sided Operators of $M_n(\mathbb{C})$*, the two-sided one *The Two-Sided Operators and the Segre Cone of $M_n(\mathbb{C})$*, and the rank theory *The Length and the Two Ranks on $M_n(\mathbb{C})$*. The biquaternion originals are *Introduction to the Operators of the Biquaternion Algebra* and *Operators Acting on One Side*.

**Conventions.** $M_n=M_n(\mathbb{C})$, $n\ge2$, and $E_{ij}$ are the matrix units. Column stacking gives $L_A=\mathrm I\otimes A$, $R_B=B^{\mathsf T}\otimes\mathrm I$, $T_{A,B}=B^{\mathsf T}\otimes A$. The Hilbert–Schmidt form is $\langle S,T\rangle=\operatorname{tr}(S^{*}T)$. The principal copy of $SU(2)$ in $GL_n$ is fixed once and for all, with generators $J_x,J_y,J_z$ and carriers $V_k$, $0\le k\le n-1$.

## The Three Families at a Glance

| family | definition | dimension | product law |
|---|---|---|---|
| left | $L_A(X)=AX$ | $n^2$ | $L_AL_B=L_{AB}$ |
| right | $R_B(X)=XB$ | $n^2$ | $R_AR_B=R_{BA}$ |
| two-sided | $T_{A,B}(X)=AXB$ | spans $n^4$ | $T_{A,B}T_{C,D}=T_{AC,DB}$ |

**The four numbers.** $1$, the scalars; $n^2$, each one-sided copy; $2n^2-1$, the span of the two copies; $n^4$, the whole operator algebra. The ladder $1<n^2<2n^2-1<n^4$ holds for $n\ge2$, with the first two coinciding only at $n=1$.

**The two copies commute.** $L_AR_B=R_BL_A$, so the pair $(L_A,R_B)$ is a commuting pair, and the two-sided family is its product. This is the single most used fact of the series and the reason the tensor reading works.

## What Exists at Every $n$

**The carrier.** $M_n$ carries the two-sided action of $GL_n\times GL_n$ by $(G,H)\cdot X=GXH$, with kernel the scalars $(\lambda\mathrm I,\lambda^{-1}\mathrm I)$. The group of the action is $(GL_n\times GL_n)/\mathbb{C}^{\times}$, of complex dimension $2n^2-1$, the dimension of the one-sided span.

**The invariants.** The rank, $\operatorname{rank}(AXB)=\operatorname{rank}A\operatorname{rank}B$ at the level of a single product; the trace $n\operatorname{tr}A\operatorname{tr}B$; the determinant $(\det A\det B)^n$; the singular values $\sigma_i(A)\sigma_j(B)$.

**The adjoints.** $L_A^{\dagger}=L_{A^{*}}$ and $R_B^{\dagger}=R_{B^{*}}$ for the Hilbert–Schmidt form; $L_A^{\mathsf T}=L_{A^{\mathsf T}}$ for the transposed bilinear form. The two adjoints conjugate the parameters and exchange no slot, at every $n$.

**The matrices.** In column stacking the three families are $\mathrm I\otimes A$, $B^{\mathsf T}\otimes\mathrm I$ and $B^{\mathsf T}\otimes A$. The transpose on the right is the trace of the anti-representation law and cannot be removed by a change of carrier basis.

**The spin content.** Under conjugation by the principal copy, $M_n=\bigoplus_{k=0}^{n-1}V_k$ with each carrier once, and $\mathfrak{sl}_n=\bigoplus_{k=1}^{n-1}V_k$. This is *The Spin Decomposition of $M_n(\mathbb{C})$*, and the operator series uses it but does not reprove it.

## What Collapses at $n=2$

**One size.** At $n=2$ the element algebra has dimension $4$ and the operator algebra $16$, so both are written with $4$ rows: elements as $4\times1$ columns in a basis, operators as $4\times4$ matrices. At $n\ge3$ the two sizes are $n$ and $n^2$.

**The transpose is a conjugation.** In the coefficient basis of the biquaternion algebra the structure constants are real, so the transpose of a regular matrix is the quaternion conjugation. At $n\ge3$ the transpose is not an inner automorphism of $M_n$ and not a two-sided product.

**The side exchange has a matrix at $n=2$.** The operator $F(X)=X^{\mathsf T}$ exchanges the two copies, $FL_AF=R_{A^{\mathsf T}}$, at every $n$. No element of the algebra does it: $DR_AD^{-1}=L_A$ for all $A$ forces $D$ to be scalar. At $n=2$ the transpose is written by a $4\times4$ permutation matrix in the coefficient frame, and that same matrix is the quaternion conjugation of the regular representation, so the exchange has a familiar name. At $n\ge3$ the operator $F$ is still there and still exchanges the sides, but it is no longer multiplication by an element and no longer looks like a conjugation.

**Half-integers.** At $n=2$ the module has spin $\tfrac12$ and the algebra has spins $0,1$. At general $n$ the module has spin $\tfrac{(n-1)}{2}$, half-integral exactly when $n$ is even, while the algebra always carries integer spins only. The biquaternion half-integral carriers are therefore a property of the module, not of the algebra.

**The four sectors.** The reduced biquaternion algebra has four sectors and one of them is the origin. In $M_n$ the four sectors still exist as a partition, but the degenerate one is no longer a point for $n\ge3$. *The Operators on the Four Sectors of $M_n(\mathbb{C})$* states which parts survive.

## The Metric Layer

**The form.** The Hilbert–Schmidt form makes $\operatorname{End}(M_n)$ a complex Hilbert space of dimension $n^4$. Its real and imaginary parts are the Euclidean metric and the symplectic form of the operator space, and the adjoint $T\mapsto T^{\dagger}$ is a conjugate-linear involution of the operator algebra with fixed set the self-adjoint operators.

**The two norms.** For a single product,
$$
\lVert T_{A,B}\rVert_{\mathrm{HS}}=\lVert A\rVert_{\mathrm{HS}}\lVert B\rVert_{\mathrm{HS}},\qquad \lVert T_{A,B}\rVert_{2}=\lVert A\rVert_{2}\lVert B\rVert_{2},
$$
the first because the Frobenius norm of a Kronecker product is the product of the norms, the second because the singular values of $B^{\mathsf T}\otimes A$ are the products $\sigma_i(A)\sigma_j(B)$.

**The two ranks.** A single product has operator rank $(\operatorname{rank}A)(\operatorname{rank}B)$ and length one. A general operator has length $\ell(M)=\operatorname{rank}c(M)$, the least number of products, and the two ranks are independent. The length theory is *The Length and the Two Ranks on $M_n(\mathbb{C})$*.

## The Structures and the Sectors

**The structures.** The operator algebra is $M_{n^2}(\mathbb{C})$. Its real forms are $M_{n^2}(\mathbb{R})$ always, and $M_{n^2/2}(\mathbb{H})$ when $n$ is even. Its complexifications are $M_{n^2}(\mathbb{C})\oplus M_{n^2}(\mathbb{C})$ over $\mathbb{R}$ and $M_{2n^2}(\mathbb{C})$ from the real operator algebra.

**The real Lie algebra.** The exponentials of $L_A$ and $R_B$ generate $(GL_n\times GL_n)/\mathbb{C}^{\times}$, of complex dimension $2n^2-1$. Its compact real form is $(U(n)\times U(n))/U(1)$, of real dimension $2n^2-1$.

**The four sectors.** With $N$-regular meaning invertible and spectrally regular meaning $n$ distinct eigenvalues, the four sectors have complex dimensions
$$
n^2,\qquad n^2-1,\qquad n^2-1,\qquad n^2-2 ,
$$
the last at any $n\ge2$. The fourth is never a point in $M_n$: at $n=2$ it is the nilpotent cone, of complex dimension $2$. The sector that collapses to the origin belongs to the commutative reduced biquaternion algebra, not to $M_2(\mathbb{C})$. The spectral side is a hypersurface cut by the discriminant, of degree $n(n-1)$ in the entries.

## The Spin Layer in One Table

| $n$ | carriers $V_k$ | $\dim M_n$ | Casimir values | generating carriers |
|---|---|---|---|---|
| $2$ | $V_0,V_1$ | $4$ | $0,2$ | $V_1$ |
| $3$ | $V_0,V_1,V_2$ | $9$ | $0,2,6$ | $V_1,V_2$ |
| $4$ | $V_0,\dots,V_3$ | $16$ | $0,2,6,12$ | $V_1,V_2,V_3$ |
| $5$ | $V_0,\dots,V_4$ | $25$ | $0,2,6,12,20$ | $V_1,\dots,V_4$ |

**Reading the table.** The scalars are the unique carrier that does not generate. Every other carrier generates the whole algebra, so the carriers are not ordered by size in their role. The Casimir values are $k(k+1)$ and the multiplicities are $2k+1$; the total is $n^2$ complex dimensions, that is $2n^2$ real dimensions for the carrier space.

## The Reading Order

**First, the ambient algebra.** *The Endomorphisms of $M_n(\mathbb{C})$*, then this article.

**Then the families and their matrix forms.** *Operator Chirality on $M_n(\mathbb{C})$* for the transpose split; *The Axis-Free $M_{n^2}(\mathbb{C})$ Representation of the Operators* for the column-stacking formulas; *The Generalized Pauli Representation* for the Weyl basis; *The Block Reading of the Operators* for the Peirce corners.

**Then the two sides together.** *The Transposition of the Two Sides*, *The Enveloping Operator Algebra and the Bi-module Structure*, *The Adjoint Pair of $L$ and $R$ Operators*, *The Hermitian Pair of Operators Acting on One Side*, *The Hermitian Pair of Operators Acting on Two Sides*.

**Then the metric layer.** *The SVD of Endomorphisms of $M_n(\mathbb{C})$* for the singular values and the operator norm.

**Then the structures.** *The Classification of the Structures of the Operators*, then the real and the complex volumes, each with its Lie algebras and Lie groups.

**Then the sectors.** *The Operators on the Four Sectors* and *The Spectral Sectors and the Operators*.

**Then the spin.** *From the Spin of a Pair of Operators to the Spin of $M_n(\mathbb{C})$*, *The Spin-Zero Carrier*, *Where the Half-Integers Go in $M_n(\mathbb{C})$*, *The Spin-One Carrier*, *The Carriers, the Closures and the Spin*, *The $SU(2)$ of $M_n(\mathbb{C})$ Acting on $n^2$ Dimensions*, and *The Odd Rows*.

## The Five Questions

Every article of the series asks the same five questions of its family, and the answers are what the reader should be able to reproduce.

1. **Matrix.** What is the operator in the column-stacking basis, and which tensor slot does it act on?
2. **Spectrum.** What are the eigenvalues, with multiplicity, and what is the determinant?
3. **Adjoint.** What is the adjoint for the Hilbert–Schmidt form, and for the transposed bilinear form, and do the two agree?
4. **Rank.** What is the rank, and what are the singular values, of a single product?
5. **Spin.** How does the principal copy act, and which carriers appear?

**What the series does not contain.** There is no general-$n$ analogue of the Fierz–Kofink identity. That identity is a statement about four components and the $4\times4$ gamma frame, and it has no form that survives the passage to $n^2$ dimensions.

## Three Warnings

**The chirality is not the spin.** The split of $M_n$ into symmetric and antisymmetric matrices is the eigenspace split of the transpose, an anti-automorphism. The split into carriers $V_k$ is the isotypic split of the conjugation action of the principal copy. The first is not invariant under the second, and $[J_z,E_{01}+E_{10}]=E_{01}-E_{10}$ at $n=4$ is the shortest witness.

**Seven is not the operator dimension.** At $n=2$ the one-sided span has dimension $7=2n^2-1$, and the operator algebra has dimension $16=n^4$. The biquaternion series used both numbers, for different objects. Neither is the dimension of the other.

**The norm split needs no real form.** Whether a matrix is invertible is a complex-algebraic condition, $\det A\neq0$. The $N$-regular and $N$-degenerate split therefore does not depend on a choice of real form. What does depend on a real form is the *value* of a norm, and at $n\ge3$ there is no multiplicative quadratic norm on $M_n$ at all.

## The Finite Check

**The counts.** For $n=2,3,4,5$ the span of the copies $\{L_A+R_B\}$ was computed to have dimension $7,17,31,49$, that is $2n^{2}-1$, and the span of the products $T_{A,B}$ to have dimension $16,81,256,625$, that is $n^{4}$.

| family | the set | size | spans $\operatorname{End}$ | what it is |
|---|---|---|---|---|
| $L_A$ | $\{L_A\}$ | $n^2$ | no | left multiplication |
| $R_B$ | $\{R_B\}$ | $n^2$ | no | right multiplication |
| $L$ and $R$ | the span of the two copies | $2n^2-1$ | no | the bimodule operators |
| $T_{A,B}$ | $\{T_{A,B}\}$ | $n^4$ | yes | all endomorphisms |
| inner | $\{T_{g,g^{-1}}\}$ | $n^2-1$ | no | the conjugations |

**The gap.** $2n^{2}-1<n^{4}$ for every $n\ge2$, and the gap $(n^{2}-1)^{2}$ is $9,64,225,576$ at $n=2,3,4,5$.

**What changes at $n=2$.** The gap is small enough that one four-dimensional frame can display both families side by side. At $n=4$ the gap is twenty-five times larger, and no frame displays the two families at once.

## Summary

Three families, four numbers, five questions. The one-sided families are $n^2$-dimensional subalgebras meeting in the scalars; their span has dimension $2n^2-1$; the two-sided products span $n^4$. At $n=2$ a single frame holds everything, and the rest of the series is the systematic separation of what that frame joined.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_A,R_B$ | the one-sided multiplications |
| $T_{A,B}$ | the two-sided map $X\mapsto AXB$ |
| $V_k$ | the carrier of spin $k$ in $M_n$, $0\le k\le n-1$ |
| $\mathfrak{a}$ | the span of the one-sided families |
| $\mathsf F$ | the flip of the two tensor slots |

## Further Reading
- [The Endomorphisms of $M_n(\mathbb{C})$](the-endomorphisms-of-mnc.html), for the ambient algebra and the dimension ladder.
- [The One-Sided Operators of $M_n(\mathbb{C})$](the-one-sided-operators-of-mnc.html), for the two copies in detail.
- [The Two-Sided Operators and the Segre Cone of $M_n(\mathbb{C})$](the-two-sided-operators-and-the-segre-cone-of-mnc.html), for the two-sided family as a cone.
- [The Spin Decomposition of $M_n(\mathbb{C})$](the-spin-decomposition-of-mnc.html), for the carriers used throughout.
- [Introduction to the Operators of the Biquaternion Algebra](introduction-to-the-operators-of-the-biquaternion-algebra.html), for the case $n=2$.
- [Operators Acting on One Side](operators-acting-on-one-side.html), for the one-sided theory in the biquaternion frame.
