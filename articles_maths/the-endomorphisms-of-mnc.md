# __The Endomorphisms of $M_n(\mathbb{C})$__

## Introduction

**The question.** What is the algebra of all linear maps of the matrix algebra into itself, and how do the three families of maps $L_A$, $R_B$ and $T_{A,B}$ sit inside it?

**The answer in one line.** It is the tensor square,
$$
\operatorname{End}_{\mathbb{C}}(M_n)=M_n\otimes M_n^{\mathrm{op}}\cong M_{n^2}(\mathbb{C}),
$$
of complex dimension $n^4$, and the three families are its one-sided and two-sided slices.

**Why the article is needed.** The operator articles of the biquaternion series worked in one size, $4\times4$, because both the algebra and its endomorphism algebra could be written in that size. At general $n$ two sizes appear, $n$ for the elements and $n^2$ for the operators, and the difference carries all of the new structure. Without this article the later ones read $n^4$ as an accident of bookkeeping.

**Boundaries.** The matrix algebra and its ideals are *The Matrix Algebra $M_n(\mathbb{C})$* and *The Ideals, the Centre and the Simplicity of $M_n(\mathbb{C})$*. The one-sided families are *The One-Sided Operators of $M_n(\mathbb{C})$*; the two-sided family is *The Two-Sided Operators and the Segre Cone of $M_n(\mathbb{C})$*; the general ladder of dimensions is *The Regular Representation in Dimension $n$*. The biquaternion original is *The Endomorphisms of the Biquaternion Algebra*.

**Conventions.** $V=\mathbb{C}^n$, $M_n=M_n(\mathbb{C})=\operatorname{End}_{\mathbb{C}}(V)$, and $n\ge2$. The maps are
$$
L_A(X)=AX,\qquad R_B(X)=XB,\qquad T_{A,B}(X)=AXB,
$$
so that $T_{A,B}=L_AR_B=R_BL_A$. The Hilbert–Schmidt form on $\operatorname{End}(M_n)$ is $\langle S,T\rangle=\operatorname{tr}(S^{*}T)$. Column stacking writes $X\in M_n$ as the column $\operatorname{vec}X$ of length $n^2$, in which
$$
\operatorname{vec}(AXB)=(B^{\mathsf T}\otimes A)\operatorname{vec}X .
$$

## The Algebra of Endomorphisms

**Proposition (the tensor square).** The rule $A\otimes B\mapsto L_AR_B$ is an isomorphism of algebras
$$
M_n\otimes M_n^{\mathrm{op}}\longrightarrow\operatorname{End}_{\mathbb{C}}(M_n),
$$
and both sides have complex dimension $n^4$.

*Proof.* The rule is bilinear and multiplicative: $(L_AR_B)(L_CL_D)=L_{AC}R_{DB}$, and $AC\otimes DB$ is the product in $M_n\otimes M_n^{\mathrm{op}}$. Injectivity: the products $E_{ij}\otimes E_{kl}$ are linearly independent and their images are the matrix units of the index pair $((i,k),(j,l))$, which are independent. Both spaces have dimension $n^4$, so injectivity is bijectivity. $\square$

**The index pair.** Under the isomorphism an operator is a matrix whose rows are indexed by a pair $(i,k)$ and whose columns by a pair $(j,l)$, and $L_AR_B$ has the single entry $A_{ij}B_{lk}$ in the slot $((i,k),(j,l))$. This is the whole content of the tensor reading, and the rest of the series unpacks it.

**The real reading.** Over $\mathbb{R}$ the same object is $\operatorname{End}_{\mathbb{R}}(M_n)\cong M_{2n^2}(\mathbb{R})$, of real dimension $2n^4$. The complex-linear operators are the ones commuting with multiplication by $i$, and they form a real subspace of half the dimension, $2n^4/2=n^4$.

## The Three Families

**The one-sided copies.** The sets
$$
L(M_n)=\{L_A:A\in M_n\},\qquad R(M_n)=\{R_B:B\in M_n\}
$$
are subalgebras of $\operatorname{End}(M_n)$, each of complex dimension $n^2$. The first is isomorphic to $M_n$ and the second to $M_n^{\mathrm{op}}$; the second reverses products, $R_BR_C=R_{CB}$.

**Proposition (the intersection).** $L(M_n)\cap R(M_n)=\mathbb{C}\mathrm I$.

*Proof.* If $L_A=R_B$ then $AX=XB$ for all $X$. At $X=\mathrm I$ this gives $A=B$, and then $AX=XA$ for all $X$, so $A$ is central, hence scalar. $\square$

**Proposition (the two-sided family spans).** The $n^4$ operators $T_{E_{ij},E_{kl}}$ are linearly independent, hence a basis of $\operatorname{End}(M_n)$.

*Proof.* In the index pair of the previous section, $T_{E_{ij},E_{kl}}$ has the single entry $1$ in the slot $((i,k),(j,l))$ and $0$ elsewhere; these are the matrix units of the $n^2\times n^2$ operator matrix. $\square$

**The families are not closed under addition.** $L_A+L_B=L_{A+B}$ stays in the left copy, and $R_A+R_B$ in the right one, but $L_A+R_B$ is in neither unless one of the two vanishes. The one-sided families are subspaces; the two-sided family is a spanning set and not a subspace, since $T_{A,B}+T_{C,D}$ need not be a single product.

## Which Generate and Which Do Not

**The span of the one-sided families.** Write
$$
\mathfrak{a}=\operatorname{span}\{L_A,R_B:A,B\in M_n\}=\{L_A+R_B\}.
$$
Then $\dim_{\mathbb{C}}\mathfrak{a}=2n^2-1$, because the two copies have dimension $n^2$ and meet in the line of scalars.

**Proposition.** $\mathfrak{a}$ is not a subalgebra of $\operatorname{End}(M_n)$ for $n\ge2$.

*Proof.* Suppose $L_AR_B=L_C+R_D$, that is $AXB=CX+XD$ for all $X$. The $(i,j)$ entry of $AE_{kl}B$ is $A_{ik}B_{lj}$, and that of $CE_{kl}+E_{kl}D$ is $C_{ik}\delta_{lj}+\delta_{ik}D_{lj}$. For $i\neq k$ and $l\neq j$ the second vanishes, so $A_{ik}B_{lj}=0$ for every such quadruple. If $A$ has an off-diagonal entry $A_{ik}\neq0$, then $B_{lj}=0$ for all $l\neq j$, so $B$ is diagonal. Taking $i=k$ and $l\neq j$ then gives $A_{ii}B_{lj}=D_{lj}$ for every $i$, so all $A_{ii}$ with $B_{lj}\neq0$ coincide; if $B$ has an off-diagonal entry this makes $A$ scalar. The symmetric argument with the roles exchanged gives: either $A$ or $B$ is scalar. A scalar parameter stays in $\mathfrak{a}$, since $L_{\lambda\mathrm I}R_B=\lambda R_B$. $\square$

**The exact statement.** $T_{A,B}\in\mathfrak{a}$ if and only if $A$ or $B$ is a scalar. So the one-sided span contains exactly the degenerate products, and every genuine two-sided product, with both parameters non-scalar, lies outside it.

**Proposition (the generated algebra).** The smallest subalgebra of $\operatorname{End}(M_n)$ containing $L(M_n)\cup R(M_n)$ is the whole algebra.

*Proof.* It contains every product $L_AR_B=T_{A,B}$ and hence, being closed under addition, their span, which is everything by the basis theorem above. $\square$

So the three statements are different and all three are needed: the one-sided families generate the operator algebra, their linear span is a proper subspace, and the two-sided family spans the algebra without being a subspace.

## The Two Readings of One Operator

**The trace.** $\operatorname{tr}L_A=n\operatorname{tr}A$ and $\operatorname{tr}R_B=n\operatorname{tr}B$, because the spectrum of $L_A$ is that of $A$ repeated $n$ times. Hence $\operatorname{tr}T_{A,B}=n\operatorname{tr}A\operatorname{tr}B$ and $\det T_{A,B}=(\det A\det B)^n$.

**The identity.** $\mathrm I_{\operatorname{End}}=L_{\mathrm I}=R_{\mathrm I}$, the operator $X\mapsto X$. It is the single point where the three families meet: $T_{A,B}=\mathrm I$ forces $A$ and $B$ to be scalars with product one.

**Proposition (the centre).** $\operatorname{End}(M_n)$ is a full matrix algebra, so its centre is $\mathbb{C}\mathrm I$.

*Proof.* The operator algebra is $M_{n^2}(\mathbb{C})$, whose centre is the scalars. $\square$

**The commutant of one element.** Operators commuting with a single $L_A$ are the maps $X\mapsto CX+XA'$ with $A'$ commuting with $A$; the count is $n^2\dim C(A)$, where $C(A)$ is the centraliser of $A$ in $M_n$. At $A$ nonderogatory this is $n^3$, the value used in *The One-Sided Operators of $M_n(\mathbb{C})$*.

## The Biquaternion Accident

At $n=2$ the carrier $V=\mathbb{C}^2$ has dimension $2$, the algebra $M_2$ has complex dimension $4$, and the operator algebra $\operatorname{End}(M_2)$ has complex dimension $16$. The biquaternion algebra $\mathbb{B}$ is $M_2(\mathbb{C})$ read with a particular real basis, so it also has complex dimension $4$ and real dimension $8$, and its endomorphisms have complex dimension $16$ and real dimension $64$.

**Why one size served both.** The biquaternion series wrote the elements of $\mathbb{B}$ as $4\times4$ complex matrices in the coefficient basis and the operators on $\mathbb{B}$ also as $4\times4$ complex matrices. Both readings are correct at $n=2$: the element algebra is $4$-dimensional, so its left regular representation is $4\times4$, and the operator algebra is $16$-dimensional, so its matrices are $4\times4$ with entries in $\mathbb{C}$. One size, $4$, serves the elements and the operators.

**What breaks.** At $n\ge3$ the elements are $n\times n$ and the operators are $n^2\times n^2$. The element algebra has dimension $n^2$ and the operator algebra $n^4$; the ratio is $n^2$, not $1$. A $4\times4$ reading of the operators exists only at $n=2$, and there it hides the tensor square: the sixteen entries of a $4\times4$ operator matrix are the sixteen pairs of the index pair, and the split $4=2\cdot2$ of the carrier is what makes the three families visible.

**The real dimension.** At $n=2$ the real operator algebra has dimension $64=8^2$, so it is $M_8(\mathbb{R})$. The biquaternion series called this the real reading of the same $4\times4$ matrices, which is true only because $4$ complex dimensions are $8$ real dimensions and the real matrix size doubles.

## The Adjoints of the Three Families

**Proposition.** For the Hilbert–Schmidt form, $L_A^{\dagger}=L_{A^{*}}$, $R_B^{\dagger}=R_{B^{*}}$ and $T_{A,B}^{\dagger}=T_{A^{*},B^{*}}$.

*Proof.* $\langle L_AX,Y\rangle=\operatorname{tr}((AX)^{*}Y)=\operatorname{tr}(X^{*}A^{*}Y)=\langle X,L_{A^{*}}Y\rangle$. The right case is the same with the trace cycled, and the product follows from $L_AR_B$ with $L^{\dagger},R^{\dagger}$ applied in reverse order. $\square$

**Proposition.** For the transposed bilinear form $\langle S,T\rangle_{\mathsf T}=\operatorname{tr}(S^{\mathsf T}T)$, the adjoints are $L_A^{\mathsf T}=L_{A^{\mathsf T}}$ and $R_B^{\mathsf T}=R_{B^{\mathsf T}}$.

*Proof.* The same computation with the transpose in place of the conjugate transpose, using $\operatorname{tr}(S^{\mathsf T}T)=\operatorname{tr}(ST^{\mathsf T})$. $\square$

So the two adjoints act on the parameters and never exchange a slot. At $n=2$ the biquaternion conjugation is the transpose of the coefficient frame, and this is where the two stories meet; *The Two-Sided Operator, the Difference Family and the Adjoints of $M_n(\mathbb{C})$* treats the coincidence.

## The Finite Check

Computed with numpy, in the column-stacking basis, for $n=2,3,4,5$:

| $n$ | $\dim\operatorname{End}$ $=n^4$ | $\dim\operatorname{span}\{L,R\}$ | $2n^2-1$ | gap $(n^2-1)^2$ |
|---|---|---|---|---|
| $2$ | $16$ | $7$ | $7$ | $9$ |
| $3$ | $81$ | $17$ | $17$ | $64$ |
| $4$ | $256$ | $31$ | $31$ | $225$ |
| $5$ | $625$ | $49$ | $49$ | $576$ |

The rank of the $n^4\times 2n^2$ matrix of the $2n^2$ one-sided operators reproduces the fourth column exactly, and the rank of the $n^4\times n^4$ matrix of the $n^4$ products reproduces $n^4$ exactly. The gap is the dimension of the orthogonal complement of $\mathfrak{a}$ for the Hilbert–Schmidt form; it is computed directly in *The Enveloping Operator Algebra of $M_n(\mathbb{C})$ and the Bi-module Structure*.

## The Count

**The numbers.** $n^{4}$ is $16,81,256,625$ and $2n^{2}-1$ is $7,17,31,49$ for $n=2,3,4,5$. The second sequence is the span of the two copies, the first the algebra they generate.

## Summary

$\operatorname{End}(M_n)$ is the tensor square $M_n\otimes M_n^{\mathrm{op}}$ and has complex dimension $n^4$. The left and right copies are $n^2$-dimensional subalgebras meeting in the scalars. Their linear span has dimension $2n^2-1$ and is not a subalgebra; the subalgebra they generate is everything; the two-sided products already span everything. At $n=2$ one matrix size, $4$, describes both the elements and the operators, and that coincidence is the reason the biquaternion series could work with a single size.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M_n$ | $M_n(\mathbb{C})$, the algebra of $n\times n$ complex matrices |
| $L_A$ | left multiplication $X\mapsto AX$ |
| $R_B$ | right multiplication $X\mapsto XB$ |
| $T_{A,B}$ | the two-sided map $X\mapsto AXB$ |
| $\mathfrak{a}$ | the span of the one-sided families, of dimension $2n^2-1$ |
| $\operatorname{vec}$ | column stacking of a matrix into a column of length $n^2$ |

## Further Reading
- Horn and Johnson, *Topics in Matrix Analysis* (Cambridge University Press, 1991), for the Kronecker product and column stacking.
- [The Matrix Algebra $M_n(\mathbb{C})$](the-matrix-algebra-mnc.html), for the algebra and its dimension.
- [The Ideals, the Centre and the Simplicity of $M_n(\mathbb{C})$](the-ideals-the-centre-and-the-simplicity-of-mnc.html), for the centre and the simplicity used above.
- [The One-Sided Operators of $M_n(\mathbb{C})$](the-one-sided-operators-of-mnc.html), for the two copies in detail.
- [The Two-Sided Operators and the Segre Cone of $M_n(\mathbb{C})$](the-two-sided-operators-and-the-segre-cone-of-mnc.html), for the two-sided family as a cone.
- [The Regular Representation in Dimension $n$](the-regular-representation-in-dimension-n.html), for the same ladder in a general algebra.
- [The Endomorphisms of the Biquaternion Algebra](the-endomorphisms-of-the-biquaternion-algebra.html), for the case $n=2$ in the coefficient frame.
