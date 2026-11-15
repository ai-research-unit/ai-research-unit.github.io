# __The Peirce Decomposition in Two Dimensions__

## Introduction

**A rank-one idempotent $e$ splits $M_2(\mathbb{C})$ into four Peirce spaces $A_{11}$, $A_{12}$, $A_{21}$, $A_{00}$ of dimension one each, and the product of two elements follows the index rule $A_{ij}A_{jk}\subseteq A_{ik}$.**

The article defines the Peirce spaces as the joint eigenspaces of the two multiplication operators $L_{e}$ and $R_{e}$, proves the index rule, computes the four dimensions, writes the spaces explicitly for the idempotent $E_{11}$ and for a general rank-one idempotent $uv^{\mathsf T}$, and compares the decomposition with the splitting into the two halves. It assumes *Lagrange Idempotents of a $2\times2$ Matrix with Simple Spectrum*, *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$* and *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian at $n=2$*.

It defers the basis adapted to the frame and the gauge to *The Peirce Basis and the Corners at $n=2$*, and the Jordan-algebra reading to *The Peirce Decomposition of $\operatorname{Sym}_2$ as a Jordan Algebra*.

## The Two Operators of an Idempotent

**Definition.** For an element $e$ the **left** and **right multiplication operators** are $L_{e}(x)=ex$ and $R_{e}(x)=xe$.

**Proposition.** For an idempotent the two operators satisfy $L_{e}^{2}=L_{e}$ and $R_{e}^{2}=R_{e}$, and they commute.

**Proof.** $e(ex)=(e^{2})x=ex$ and $(xe)e=xe^{2}=xe$; and $e(xe)=(ex)e$ by associativity.

**Corollary.** Each operator is a projection of the eight-dimensional real space, so the space splits into the kernel and the image of each, and jointly into four pieces.

**Proof.** A projection with commuting partner gives the joint splitting into the four combinations of the two images, and each piece is the intersection of an image or a kernel with an image or a kernel.

**Definition.** The **Peirce spaces** are

$$
A_{11}=\operatorname{im}L_{e}\cap\operatorname{im}R_{e},\quad
A_{12}=\operatorname{im}L_{e}\cap\ker R_{e},\quad
A_{21}=\ker L_{e}\cap\operatorname{im}R_{e},\quad
A_{00}=\ker L_{e}\cap\ker R_{e}.
$$

**Corollary.** In coordinates the four spaces are the conditions $ex=x$ or $ex=0$ together with $xe=x$ or $xe=0$.

**Proof.** The image of $L_{e}$ is the set of fixed vectors of $L_{e}$ and its kernel is the set of vectors sent to zero; combining the two conditions gives the four displays.

## The Dimensions

**Theorem.** For a rank-one idempotent the four Peirce spaces have dimension one each, and the dimensions sum to four, the complex dimension of the algebra.

**Proof.** Choose a basis with $e=E_{11}$, which is possible because two idempotents of the same rank are conjugate. Then the four spaces are the spans of $E_{11}$, $E_{12}$, $E_{21}$, $E_{22}$, each of dimension one, and $1+1+1+1=4$.

**Corollary.** The decomposition does not depend on the idempotent chosen, only on its rank.

**Proof.** Any two rank-one idempotents are conjugate, and conjugation carries the Peirce spaces of one to those of the other.

**Corollary.** For the idempotents $0$ and $I$ the decomposition degenerates: all of the space lies in one Peirce piece.

**Proof.** The operator $L_{0}$ is zero, so the only nonempty piece is the one with both indices zero; and $L_{I}$ is the identity, so the only nonempty piece is the one with both indices one.

## The Multiplication Rules

**Theorem.** The Peirce spaces multiply by the index rule

$$
A_{ij}A_{jk}\subseteq A_{ik},\qquad A_{ij}A_{kl}=0\ \text{when}\ j\ne k .
$$

**Proof.** Take $x\in A_{ij}$ and $y\in A_{kl}$. Then $e(xy)=(ex)y=(ix)y=ixy$ and $(xy)e=x(ye)=x(ly)=l\,xy$, so the product lies in $A_{il}$ when $j=k$; when $j\ne k$ one of the two computations gives $0$ because $j$ and $k$ are different eigenvalues of the same projection.

**Corollary.** The mixed spaces are square-zero: $A_{12}^{2}=0$ and $A_{21}^{2}=0$.

**Proof.** The index rule with $j=1$, $k=2$ gives a product in $A_{12}A_{21}\subseteq A_{11}$ for one order and $A_{21}A_{12}\subseteq A_{00}$ for the other; the products of two elements of the same mixed space vanish by the second rule.

**Corollary.** $A_{12}A_{21}\subseteq A_{11}$ and $A_{21}A_{12}\subseteq A_{00}$, and both products are nonzero at the standard idempotent.

**Proof.** $E_{12}E_{21}=E_{11}$ and $E_{21}E_{12}=E_{22}$ by the multiplication of the matrix units.

## The Standard Idempotent

**Proposition.** At $e=E_{11}$ the four spaces are the four lines of the matrix units.

**Proof.** $E_{11}E_{11}=E_{11}$ and $E_{11}E_{22}=0$ give the diagonal pieces; $E_{11}E_{12}=E_{12}$ and $E_{12}E_{11}=0$ put $E_{12}$ in $A_{12}$; and $E_{21}$ is placed symmetrically in $A_{21}$.

**Corollary.** In the Peirce basis $(e,\upsilon_{+},\upsilon_{-},1-e)$ the matrix of left multiplication by $e$ is $\operatorname{diag}(1,1,0,0)$ and the matrix of right multiplication is $\operatorname{diag}(1,0,1,0)$.

**Proof.** The left multiplication fixes $A_{11}$ and $A_{12}$ and kills the other two, and the right multiplication fixes $A_{11}$ and $A_{21}$.

**Corollary.** An element $x$ decomposes as $x=x_{11}+x_{12}+x_{21}+x_{00}$ with $x_{11}=exe$, $x_{12}=ex(1-e)$, $x_{21}=(1-e)xe$, $x_{00}=(1-e)x(1-e)$.

**Proof.** Apply the two projections in the two orders, which gives the four combinations, and sum them, which gives back $x$.

## A General Rank-One Idempotent

**Proposition.** For $e=uv^{\mathsf T}$ with $v^{\mathsf T}u=1$ the four spaces are the lines spanned by $uv^{\mathsf T}$, $u\,w^{\mathsf T}$, $z\,v^{\mathsf T}$ and $zw^{\mathsf T}$, where $w$ and $z$ are vectors with $v^{\mathsf T}w=0$ and $z^{\mathsf T}u=0$.

**Proof.** $e(uw^{\mathsf T})=u(v^{\mathsf T}u)w^{\mathsf T}=uw^{\mathsf T}$ and $(uw^{\mathsf T})e=u(w^{\mathsf T}u)v^{\mathsf T}=0$, so $uw^{\mathsf T}$ lies in $A_{12}$; the other three cases are similar, and each space is one-dimensional.

**Corollary.** The four spaces are the four corners $eM_2e$, $eM_2(1-e)$, $(1-e)M_2e$, $(1-e)M_2(1-e)$.

**Proof.** The first corner consists of the elements $exe$, which is the intersection of the two images, and the others are the same computation with one or both projections replaced by their complements.

**Corollary.** The corner $A_{12}$ consists of the matrices whose image lies in the line of $u$ and whose kernel contains the line of $v$, so it is the space of rank-one maps in a fixed direction.

**Proof.** $ex(1-e)=x(1-e)$ for $x\in A_{12}$, so the image of $x$ lies in the image of $e$ and the kernel contains the kernel of $e$.

## The Comparison with the Two Halves

**Proposition.** The Peirce splitting refines neither half: the symmetric part of $A_{12}$ is not contained in $A_{12}$.

**Proof.** For $x=uw^{\mathsf T}$ the transpose is $wu^{\mathsf T}$, which lies in $A_{21}$ rather than in $A_{12}$, so the symmetric part $x+x^{\mathsf T}$ has components in both mixed spaces.

**Corollary.** The transpose exchanges $A_{12}$ and $A_{21}$ and fixes $A_{11}$ and $A_{00}$.

**Proof.** The transpose of $ex(1-e)$ is $(1-e)x^{\mathsf T}e$, which lies in the corner with the indices exchanged.

**Corollary.** The symmetric half is the graph of a map from $A_{11}\oplus A_{00}$ to the mixed spaces, of dimension three.

**Proof.** A symmetric element is determined by its two diagonal pieces, of dimension two, and one mixed component, of dimension one, which gives three.

## The Orthogonality of the Four Spaces

**Proposition.** The four Peirce spaces are mutually orthogonal for the trace form, except the two mixed ones, whose pairing is $\operatorname{tr}(E_{12}E_{21})=1$.

**Proof.** $L_{e}$ is self-adjoint for the trace form because $\operatorname{tr}(exy)=\operatorname{tr}(xey)$, so its eigenspaces are orthogonal; the two mixed spaces share the eigenvalue of $L_{e}$ and are separated only by $R_{e}$, which is not self-adjoint, and the computation at the matrix units gives the value $1$.

**Corollary.** The two blocks $A_{11}\oplus A_{12}$ and $A_{21}\oplus A_{00}$ are orthogonal and of dimension two each.

**Proof.** They are the two eigenspaces of $L_{e}$, of eigenvalues $1$ and $0$, and $L_{e}$ is self-adjoint.

## The Corpus Translation

**Proposition.** The four Peirce spaces are the four corners $\mathbb{B}_{st}$ of the biquaternion algebra.

**Proof.** The corpus writes the corners as the four products of the idempotent pair with the algebra on the two sides, which is the same four-corner pattern as the display of this article, under the matrix model of *$M_2(\mathbb{C})$ Pauli Representation*.

**Corollary.** The dimensions one, one, one, one are the dimensions of the corners, and their sum is the dimension of the algebra over the field.

**Proof.** Each corner is spanned by one matrix unit and its multiple by the scalar $i$, so it is one complex line, and the four lines add to dimension four.

## Summary

A rank-one idempotent $e$ gives two commuting projections $L_{e}$ and $R_{e}$, and their joint eigenspaces are the four Peirce spaces $A_{11}$, $A_{12}$, $A_{21}$, $A_{00}$, of dimension one each. They are the four corners $eMe$, $eM(1-e)$, $(1-e)Me$, $(1-e)M(1-e)$, they multiply by the index rule $A_{ij}A_{jk}\subseteq A_{ik}$ and vanish when the middle indices differ, and the mixed spaces are square-zero.

At the standard idempotent the spaces are the four lines of the matrix units, and for a general idempotent $uv^{\mathsf T}$ they are the lines of $uv^{\mathsf T}$, $uw^{\mathsf T}$, $zv^{\mathsf T}$ and $zw^{\mathsf T}$. The four are mutually orthogonal for the trace form except the two mixed ones, and the transpose exchanges the mixed pair.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e$ | a rank-one idempotent |
| $L_{e},R_{e}$ | left and right multiplication by $e$ |
| $A_{ij}$ | the Peirce spaces, $i,j\in\{1,0\}$ |
| $u,v$ | the vectors with $e=uv^{\mathsf T}$ and $v^{\mathsf T}u=1$ |
| $w,z$ | the vectors orthogonal to $v$ and to $u$ |

## Further Reading

- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the Peirce decomposition of an algebra by an idempotent.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce spaces of a finite-dimensional algebra and the corner notation.
- [Lagrange Idempotents of a $2\times2$ Matrix with Simple Spectrum](lagrange-idempotents-of-a-2x2-matrix-with-simple-spectrum.html), for the idempotents used as the frame.
- [The Peirce Basis of the Biquaternion Algebra](the-peirce-basis-of-the-biquaternion-algebra.html), for the same decomposition in the biquaternion language.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$](the-two-halves-over-r-symmetric-and-antisymmetric-at-n-2.html), for the splitting that the Peirce splitting refines.
