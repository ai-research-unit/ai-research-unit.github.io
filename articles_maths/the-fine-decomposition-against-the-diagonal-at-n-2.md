# __The Fine Decomposition against the Diagonal at $n=2$__

## Introduction

**Against a complete family of rank-one projections the algebra splits into four lines, one for each pair of indices, and the multiplication of the lines is the multiplication of a two-by-two table.**

The article proves the fine decomposition $M_2(\mathbb{C})=\bigoplus_{k,l}A_{kl}$ against the diagonal, computes the dimension of each corner, states the corner multiplication rule, and reads the trace, the determinant and the symmetric half in these coordinates. It assumes *The Ideals, the Centre and the Simplicity of $M_2(\mathbb{C})$* for the minimal left ideals, and *The Matrix Algebra $M_2(\mathbb{C})$* for the units.

It defers the Peirce operators that produce the same decomposition to *The Peirce Basis in $n$ Dimensions*, and the frame of the biquaternion algebra to *The Peirce Basis of the Biquaternion Algebra*. In the biquaternion language the four lines are the four corners $\mathbb{B}_{st}$ of *The Peirce Decomposition of the Biquaternion Algebra*.

## The Complete Family and the Four Projections

**Definition.** A **complete family** of idempotents in $M_2(\mathbb{C})$ is a pair $P_{1},P_{2}$ with

$$
P_{k}^{2}=P_{k},\qquad P_{k}P_{l}=0\ (k\neq l),\qquad P_{1}+P_{2}=I .
$$

**Proposition.** A complete family consists of two projections of rank one, so each $P_{k}$ has trace $1$, and the pair is exactly a choice of two complementary lines in $\mathbb{C}^{2}$.

**Proof.** Taking traces in $P_{1}+P_{2}=I$ gives $\operatorname{tr}P_{1}+\operatorname{tr}P_{2}=2$, and each trace is a nonnegative integer because an idempotent of order two has eigenvalues $0$ or $1$; neither is $0$ since the sum is $I$. The image of $P_{k}$ is a line and the two lines are complementary.

**Example.** $P_{1}=E_{11}$ and $P_{2}=E_{22}$ is the standard complete family, the one attached to the coordinate lines.

**There are as many complete families as there are direct sums $\mathbb{C}^{2}=L_{1}\oplus L_{2}$.** That set is the complement of the diagonal in $\mathbb{P}^{1}\times\mathbb{P}^{1}$, an open dense set, and the standard family is one point of it.

## The Four Corners

**Definition.** The **corners** of a complete family are the spaces

$$
A_{kl}=P_{k}M_2(\mathbb{C})P_{l}=\{P_{k}XP_{l}:X\in M_2(\mathbb{C})\}.
$$

**Theorem.** Each corner is a line: $\dim_{\mathbb{C}}A_{kl}=1$ for all four pairs, the four corners are independent, and their sum is the algebra:

$$
M_2(\mathbb{C})=\bigoplus_{k,l=1}^{2}A_{kl},\qquad \dim_{\mathbb{C}}=1+1+1+1=4 .
$$

**Proof.** The product $P_{k}XP_{l}$ depends only on the composition of the four maps $\mathbb{C}^{2}\to L_{l}\to\mathbb{C}^{2}\to L_{k}$, and the space of maps $L_{l}\to L_{k}$ between two lines is one-dimensional; so each corner is a line, and it is nonzero because $P_{k}P_{l}$ is nonzero when $k=l$. For the sum, every $X$ satisfies $X=\sum_{k,l}P_{k}XP_{l}$ because $\sum_{k}P_{k}=I$; for independence, if $\sum_{k,l}X_{kl}=0$ with $X_{kl}\in A_{kl}$ then multiplying on the left by $P_{m}$ and on the right by $P_{n}$ leaves $X_{mn}=0$.

**Corollary (the equality is a refinement).** The fine decomposition is a refinement of the split into the two columns: $A_{k1}\oplus A_{k2}$ is the minimal left ideal $M_2P_{k}$ and $A_{1l}\oplus A_{2l}$ is the minimal right ideal $P_{l}M_2$.

**Proof.** The left multiplication by $P_{k}$ keeps the first index and the right multiplication by $P_{l}$ keeps the second; the space $M_2P_{k}$ consists of the elements whose second index is $k$.

## The Fine Decomposition

**The coordinates are four scalars.** In the standard family every matrix is

$$
A=aE_{11}+bE_{12}+cE_{21}+dE_{22}=\begin{pmatrix}a&b\\ c&d\end{pmatrix},
$$

so the fine decomposition is the decomposition of a matrix into its four entries.

**Proposition (the grading).** Assign to $A_{kl}$ the degree $(k,l)\in(\mathbb{Z}/2)^{2}$. The product of two homogeneous elements of degrees $\alpha$ and $\beta$ is homogeneous of degree $\alpha+\beta$ when the product is nonzero.

**Proof.** $A_{kl}A_{lm}\subseteq A_{km}$ because $P_{l}P_{l}=P_{l}$, and $A_{kl}A_{mn}=0$ when $l\neq m$ because $P_{l}P_{m}=0$. So the degree of a product is $(k,m)$, the sum of $(k,l)$ and $(l,m)$ in the group where $1+1=0$ and the indices are read modulo $2$.

**Corollary (the grading is fine).** The algebra is graded by $(\mathbb{Z}/2)^{2}$ with all four homogeneous components of dimension one, so the grading is fine; at order $n$ the same construction gives a grading by $(\mathbb{Z}/n)^{2}$ with components of dimension one, which is the fine grading of *The Peirce Basis in $n$ Dimensions*.

**The diagonal part and the off-diagonal part.** The diagonal corners $A_{11}\oplus A_{22}$ form the subalgebra of matrices diagonal in the frame, isomorphic to $\mathbb{C}\times\mathbb{C}$; the off-diagonal corners $A_{12}\oplus A_{21}$ form a two-dimensional space which is not a subalgebra, since its product lands in the diagonal.

## The Multiplication of the Corners

**Theorem.** The four lines multiply by the rule

$$
A_{kl}A_{lm}\subseteq A_{km},\qquad A_{kl}A_{mn}=0\ \text{when }l\neq m,
$$

and the product of two lines filling a chain is onto: $A_{kl}A_{lm}=A_{km}$.

**Proof.** The inclusions are the proof of the grading. Surjectivity: for nonzero $X\in A_{kl}$ and $Y\in A_{lm}$ the product $XY$ is a nonzero element of the line $A_{km}$, because $X$ maps $L_{l}$ isomorphically onto $L_{k}$ and $Y$ maps $L_{m}$ isomorphically onto $L_{l}$.

**Corollary (the system of matrix units).** In the standard family the four lines are spanned by $E_{11},E_{12},E_{21},E_{22}$, and the multiplication table is $E_{kl}E_{mn}=\delta_{lm}E_{kn}$.

**Proof.** $E_{kl}E_{mn}$ sends $e_{n}$ to $e_{l}$ and then to $e_{k}$, which is $\delta_{ln}e_{k}$; the two indices inside must match.

**The biquaternion reading.** The four lines are the four corners $\mathbb{B}_{++},\mathbb{B}_{+-},\mathbb{B}_{-+},\mathbb{B}_{--}$ of the corpus, each of real dimension $2$ because the biquaternion algebra is over $\mathbb{R}$ and each corner is a complex line read as a real plane. The companion nilpotents $\vec\Upsilon_{+-},\vec\Upsilon_{-+}$ are the two off-diagonal units: that is *The Companion Nilpotents of the Biquaternion Algebra*.

## The Trace and the Determinant in Corner Coordinates

**Proposition.** In the standard corner coordinates

$$
\operatorname{tr}A=a+d,\qquad \det A=ad-bc .
$$

**Proof.** The trace is the sum of the diagonal entries. For the determinant, expand $\det(A)$ in the entries, or note that $ad-bc$ is the product of the two eigenvalues of the two-by-two matrix, which is the identity of *The Elementary Symmetric Functions: $\operatorname{tr}$ and $\det$ in Dimension Two* read in these coordinates.

**Corollary.** The trace is the sum of the two diagonal corners and the determinant is the difference of the two products of diagonal and off-diagonal corners.

**Proof.** $ad$ is the product of the two diagonal corners and $bc$ the product of the two off-diagonal ones; the determinant is their difference, which is the classical rule of Sarrus at order two.

**The adjugate is the corner swap.** The adjugate of $A$ is $\begin{pmatrix}d&-b\\ -c&a\end{pmatrix}$, which exchanges the two diagonal corners and negates the two off-diagonal ones.

**Corollary.** $\operatorname{adj}(A)$ is obtained from $A$ by the involution $\tau_{J}$ of *The Involutions of $M_2(\mathbb{C})$ over $\mathbb{R}$ and over $\mathbb{C}$*, and $\operatorname{adj}A=A$ exactly for the matrices with $a=d$ and $b=c=0$.

## The Diagonal, the Two Halves and the Gauge

**The symmetric half meets each corner in a real line.** For symmetric $S$ in the standard frame, the corner $A_{11}$ part is $aE_{11}$ with $a$ real and the corner $A_{12}$ part is $bE_{12}$ with $b$ real; so $\operatorname{Sym}_2\cap A_{kl}$ is a real line for each pair.

**Proof.** The symmetric condition relates the $(1,2)$ and the $(2,1)$ entries and does not mix the diagonal ones, so each corner is cut by one real equation inside its complex line.

**Corollary.** $\operatorname{Sym}_2$ has real dimension $4$ inside the eight real dimensions, distributed as one real dimension in each of the four corners.

**The change of frame is the gauge.** Conjugating the family by $g\in\mathrm{GL}_2(\mathbb{C})$ sends $P_{k}$ to $gP_{k}g^{-1}$ and sends the corner $A_{kl}$ to $gA_{kl}g^{-1}$; the decomposition changes but the algebra of the four lines does not.

**Proposition.** Two complete families are conjugate, and the set of complete families modulo conjugation is a point; the stabiliser of the standard family is the group of diagonal matrices modulo scalars, of dimension $2$.

**Proof.** Two decompositions of $\mathbb{C}^{2}$ into two ordered lines differ by a linear map taking one pair of lines to the other, and that map is unique up to a map preserving each line, which is diagonal.

**The gauge is the rescaling of the frame.** The census of the biquaternion frame in *The Peirce Basis of the Biquaternion Algebra* has one freedom only, the reciprocal rescaling $u\mapsto\lambda u$, $v\mapsto\lambda^{-1}v$; in the matrix language that is the residual diagonal freedom $g=\operatorname{diag}(\lambda,\lambda^{-1})$ modulo the scalars, which is one dimension removed from the two above.

## Summary

A complete family of two rank-one projections cuts $M_2(\mathbb{C})$ into four lines $A_{kl}=P_{k}M_2P_{l}$, each of complex dimension one, and the sum is direct. In the standard family the four lines are spanned by $E_{11},E_{12},E_{21},E_{22}$ and the decomposition is the decomposition of a matrix into its four entries.

The product rule is $A_{kl}A_{lm}\subseteq A_{km}$ with the mixed product zero, so the algebra is graded by $(\mathbb{Z}/2)^{2}$ with all components of dimension one. In these coordinates the trace is $a+d$ and the determinant is $ad-bc$; the adjugate exchanges the diagonal corners and negates the off-diagonal ones. The symmetric half meets each corner in a real line, and a change of frame is the conjugation by $g$, with the residual freedom of the diagonal.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P_{1},P_{2}$ | a complete family of rank-one projections |
| $A_{kl}$ | the corner $P_{k}M_2P_{l}$, a line |
| $A_{11}\oplus A_{22}$ | the diagonal part, $\cong\mathbb{C}\times\mathbb{C}$ |
| $A_{12}\oplus A_{21}$ | the off-diagonal part, not a subalgebra |
| $E_{kl}$ | the matrix units, spanning the standard corners |
| $a,b,c,d$ | the four corner coordinates of a matrix |
| $(\mathbb{Z}/2)^{2}$ | the grading group |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition and the systems of matrix units.
- Yuri A. Drozd and Vladimir V. Kirichenko, *Finite Dimensional Algebras* (Springer, 1994), for fine gradings by finite abelian groups.
- [The Ideals, the Centre and the Simplicity of $M_2(\mathbb{C})$](the-ideals-the-centre-and-the-simplicity-of-m2c.html), for the minimal left and right ideals that the corners refine.
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the four corners in the biquaternion language.
- [The Peirce Basis of the Biquaternion Algebra](the-peirce-basis-of-the-biquaternion-algebra.html), for the frame, the matrix units and the gauge on the biquaternion side.
