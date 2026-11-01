# __The Length and the Two Ranks on $M_n(\mathbb{C})$__

## Introduction

**The question.** A general endomorphism of $M_{n}(\mathbb{C})$ is not a single two-sided product, but it is a finite sum of them. Two numbers measure it: the **length** $\ell(M)$, the least number of products in a decomposition, and the **rank** $\operatorname{rank}M$, the ordinary rank of the $n^{2}\times n^{2}$ matrix. This article proves that the length is the rank of a certain $n^{2}\times n^{2}$ array of coefficients, computes the strata of each length, and shows that the two numbers are independent.

**The result in one line.** The length is the rank of the coefficient array $c(M)$, its values are $0,1,\dots,n^{2}$, the set of arrays of length at most $r$ is the determinantal variety of dimension $2rn^{2}-r^{2}$, and the generic matrix has length $n^{2}$.

**The one identity that carries everything.** With the $n^{4}$ basis products $T_{\mu\nu}=L_{E_{\mu}}R_{E_{\nu}}$ and an orthonormal basis of the algebra,
$$
c(T_{A,B})=[A]\,[B]^{\mathsf T},
$$
so a product has a coefficient array of rank one and every array of rank one is a product. **The product condition becomes a rank condition, and the length becomes the rank of the array**; nothing else in the article is needed for the two theorems.

**Boundaries.** The products and their cone are *The Two-Sided Operators and the Segre Cone of $M_n(\mathbb{C})$*; the one-sided families are *The One-Sided Operators of $M_n(\mathbb{C})$*; the abstract setting is *The Regular Representation in Dimension $n$*. At $n=2$ the same theorem with the sixteen Peirce-frame operators is *$M_4(\mathbb{C})$ Standard Peirce Representation : Operators*, and the coefficient matrix there is the $4\times4$ array of that article. The general statement for an algebra of dimension $N$ is the tensor form of *The Regular Representation in Dimension $n$*.

**Conventions.** The algebra is $A=M_{n}(\mathbb{C})$ of complex dimension $N=n^{2}$; the endomorphism algebra has complex dimension $N^{2}=n^{4}$. The matrix units are $E_{\mu}=E_{ij}$ with $\mu$ running over the $N$ pairs, and they are orthonormal for the Hilbert–Schmidt form, $\operatorname{tr}(E_{\mu}^{*}E_{\nu})=\delta_{\mu\nu}$. The basis products are $T_{\mu\nu}=L_{E_{\mu}}R_{E_{\nu}}$. The coefficient array of $M\in\operatorname{End}(A)$ is $c(M)$, an $N\times N$ array. The length is $\ell(M)$.

## The Coefficient Array

### The Basis of Products

**Theorem.** The $N^{2}=n^{4}$ operators $T_{\mu\nu}$ are a basis of $\operatorname{End}(M_{n}(\mathbb{C}))$, and they are orthonormal for the Hilbert–Schmidt form:
$$
\operatorname{tr}\bigl(T_{\mu\nu}^{*}T_{\rho\sigma}\bigr)=\delta_{\mu\rho}\delta_{\nu\sigma}.
$$

*Proof.* The matrix of $T_{\mu\nu}$ is $E_{\nu}^{\mathsf T}\otimes E_{\mu}$, so
$$
\operatorname{tr}\bigl(T_{\mu\nu}^{*}T_{\rho\sigma}\bigr)
=\operatorname{tr}\bigl(E_{\nu}^{\mathsf T*}E_{\sigma}^{\mathsf T}\bigr)\operatorname{tr}\bigl(E_{\mu}^{*}E_{\rho}\bigr)
=\delta_{\nu\sigma}\delta_{\mu\rho},
$$
using the orthonormality of the matrix units in each factor.

**The consequence.** Every operator has the unique expansion
$$
M=\sum_{\mu,\nu}c(M)_{\mu\nu}T_{\mu\nu},\qquad c(M)_{\mu\nu}=\operatorname{tr}\bigl(T_{\mu\nu}^{*}M\bigr),
$$
and the assignment $M\mapsto c(M)$ is a linear isomorphism of $\operatorname{End}(A)$ onto the space of $N\times N$ arrays.

**The normalisation.** The normalisation is the one of an orthonormal basis of the algebra. In the biquaternion articles the basis $e_{t},\vec e_{x},\vec e_{y},\vec e_{z}$ has $\operatorname{tr}(\mathsf M_{2}(e_{\mu})^{*}\mathsf M_{2}(e_{\nu}))=2\delta_{\mu\nu}$, so the products have Hilbert–Schmidt norm two, $\operatorname{tr}(T_{\mu\nu}^{*}T_{\mu\nu})=4$, and the coefficient is $\tfrac14$ of the scalar product. **The array is the same object in both normalisations; only the factor of $4$ differs.**

### The Array of a Product

**Theorem.** For every pair,
$$
c(T_{A,B})=[A]\,[B]^{\mathsf T},
$$
where $[A]$ is the column of coordinates of $A$ in the basis $E_{\mu}$, $[A]_{\mu}=\operatorname{tr}(E_{\mu}^{*}A)$.

*Proof.* By definition $T_{A,B}=\sum_{\mu,\nu}A_{\mu}B_{\nu}T_{\mu\nu}$ with $A=\sum A_{\mu}E_{\mu}$ and $B=\sum B_{\nu}E_{\nu}$, since the map $(A,B)\mapsto T_{A,B}$ is bilinear and the basis products are the images of the basis pairs. The array of coefficients is therefore the outer product of the two coordinate columns.

**Three readings of one identity.** The rank of $[A][B]^{\mathsf T}$ is one when both vectors are nonzero; the array is zero when either is; and the array determines the operator by the basis expansion. **The rank-one condition is therefore exactly the product condition, and it is a condition on an $N\times N$ array and not on the $N\times N$ matrix $M$.**

**The array of a one-sided operator.** The array of $L_{A}=T_{A,I}$ is the outer product of $[A]$ with the coordinate column of the identity, which is the column of the diagonal units. Its rank is one unless $A=0$, so **every one-sided operator has length one**, as it must.

## The Length

### The Definition and the Theorem

**Definition.** The **length** of $M$ is
$$
\ell(M)=\min\{r\ge0: M=T_{A_{1},B_{1}}+\cdots+T_{A_{r},B_{r}}\},
$$
with $\ell(0)=0$.

**Theorem (the length is the rank of the array).** For every $M\in\operatorname{End}(M_{n}(\mathbb{C}))$,
$$
\ell(M)=\operatorname{rank}c(M).
$$

*Proof.* If $M$ is a sum of $r$ products, then $c(M)=\sum_{i\le r}[A_{i}][B_{i}]^{\mathsf T}$ is a sum of $r$ arrays of rank one, so its rank is at most $r$; hence $\ell(M)\ge\operatorname{rank}c(M)$. Conversely let $c=c(M)$ have rank $r$ and factor it as $c=UV$ with $U$ of size $N\times r$ and $V$ of size $r\times N$. The $i$-th column of $U$ is the coordinate column of a matrix $A_{i}$ and the $i$-th row of $V$ is the transpose of the coordinate column of a matrix $B_{i}$, so $c=\sum_{i\le r}[A_{i}][B_{i}]^{\mathsf T}$ and $M=\sum_{i\le r}T_{A_{i},B_{i}}$; hence $\ell(M)\le r$.

**The values.** The length takes the values $0,1,\dots,n^{2}$. The value $0$ is the zero operator; the value $1$ is the cone of products; the value $n^{2}$ is the complement of the determinantal variety of the arrays of rank at most $n^{2}-1$, which is open and dense. **Every endomorphism of $M_{n}(\mathbb{C})$ is a sum of at most $n^{2}$ two-sided products, and a generic one needs exactly $n^{2}$.**

**The case $n=2$.** The statement is the four of the Peirce article: every $4\times4$ matrix is a sum of at most four products, and a generic matrix needs four.

### The Strata

**Theorem (the stratum of length at most $r$).** The set
$$
\mathcal{C}_{r}=\{M:\ell(M)\le r\}=\{M:\operatorname{rank}c(M)\le r\}
$$
is an irreducible closed algebraic cone of complex dimension
$$
2rn^{2}-r^{2}
$$
for $0\le r\le n^{2}$, and it is smooth away from the origin for $r=1$.

*Proof.* The set is the inverse image under the linear isomorphism $c$ of the determinantal variety of $N\times N$ arrays of rank at most $r$, whose dimension is the classical $r(2N-r)=2rN-r^{2}$. The cone property is the linearity of $c$. The smoothness for $r=1$ is the statement that the Segre cone is smooth off its vertex.

**The table of dimensions.** For $N=n^{2}=4$, that is $n=2$, the dimensions are

| $r$ | $\dim\mathcal{C}_{r}$ | the set |
|---|---|---|
| $0$ | $0$ | the zero operator |
| $1$ | $7$ | the cone of products |
| $2$ | $12$ | the sums of two products |
| $3$ | $15$ | the complement of the arrays of rank four |
| $4$ | $16$ | the whole space |

and for $N=9$, that is $n=3$,

| $r$ | $\dim\mathcal{C}_{r}$ |
|---|---|
| $0$ | $0$ |
| $1$ | $17$ |
| $2$ | $32$ |
| $3$ | $45$ |
| $4$ | $56$ |
| $5$ | $65$ |
| $6$ | $72$ |
| $7$ | $77$ |
| $8$ | $80$ |
| $9$ | $81$ |

**Every $r$ from $0$ to $N$ is a length, and the table has no gaps.** What has gaps is the table of the *ordinary* rank of a product, which skips every number that is not a product of two integers at most $n$. The two stratifications are different, and this is the subject of the next section.

**The jump.** The increments of the dimension are $2N-2r+1$: from $r-1$ to $r$ the stratum grows by that number. At $n=2$ the increments are $7,5,3,1$, the last being the single condition $\det c\ne0$; at $n=3$ they are $17,15,13,11,9,7,5,3,1$. **The top stratum is the complement of a hypersurface in the arrays, while the bottom one is far from it: the products have codimension $(n^{2}-1)^{2}=n^{4}-2n^{2}+1$ in the operator space, which at $n=2$ is $9$ and at $n=3$ is $64$.**

### The Criterion of a Single Product

**Theorem.** For $M\neq0$,
$$
\ell(M)=1\iff c(M)=[A][B]^{\mathsf T}\ \text{for some }A,B\neq0\iff\operatorname{rank}c(M)=1 .
$$

*Proof.* The first equivalence is the array of a product, and the second is the criterion that an $N\times N$ array of rank one is exactly an outer product of two nonzero columns.

**The test on $M$ alone.** The criterion is a test on the coefficients and not on the matrix: the rank of $M$ tells nothing, because a product can have rank $1$ and a matrix of rank $1$ can have length $n^{2}$. The test is
$$
M\ \text{is a product}\iff\text{the }2\times2\text{ minors of }c(M)\text{ vanish},
$$
that is $N^{2}(N-1)^{2}/4$ polynomial conditions, which define a variety of codimension $(N-1)^{2}$ in the arrays of size $N$.

**How to read the parameters off the array.** If $\operatorname{rank}c=1$, take $[A]$ to be a nonzero column of $c$ and $[B]^{\mathsf T}$ to be the corresponding row divided by the pivot entry. If $\operatorname{rank}c=r>1$, a rank factorisation $c=UV$ gives the $r$ products, one per column of $U$ against the corresponding row of $V$.

## The Two Ranks

### The Independence

**Theorem.** Neither number determines the other.

*Proof.* Two counterexamples at $n=2$ suffice, and both generalise.

**A product of rank one and of length one.** Take $A$ and $B$ of rank one; then $\operatorname{rank}T_{A,B}=1$ and $\ell=1$.

**A matrix of rank one and of length four.** Take $M=uv^{\mathsf T}$ with $u,v$ generic columns of length $4$; the array $c(M)$ has rank $4$ for generic $u,v$, so $\ell(M)=4$ while $\operatorname{rank}M=1$. The set is not small: the rank-one matrices of length four form a dense open subset of the rank-one variety, and the computation is the one of the worked case $M_{1}$ of the Peirce article. **At $n=3$ the same construction gives a matrix of rank one and length $n^{2}=9$**, and the phenomenon is not an accident of the small case.

**A product of full rank and of length one.** Take $A$ and $B$ invertible; then $\operatorname{rank}T_{A,B}=n^{2}$ and $\ell=1$. So a matrix of the largest rank can have the smallest length.

**The table at $n=2$.**

| $M$ | $\operatorname{rank}M$ | $\operatorname{rank}c(M)$ | $\ell(M)$ |
|---|---|---|---|
| $T_{A,B}$ with $A,B$ units | $4$ | $1$ | $1$ |
| $T_{A,B}$ with $A,B$ of rank one | $1$ | $1$ | $1$ |
| a generic sum of three products | $4$ | $3$ | $3$ |
| a generic sum of two products | $4$ | $2$ | $2$ |
| a generic matrix of rank $1$ | $1$ | $4$ | $4$ |
| a generic matrix | $4$ | $4$ | $4$ |

**The lesson.** The ordinary rank of $M$ is a property of $M$ as a linear map of $\mathbb{C}^{n^{2}}$; the length is a property of $M$ as an element of $M_{n}\otimes M_{n}^{\mathrm{opp}}$. **The two are ranks of two different matrices attached to the same operator, and there is no inequality between them in either direction** — beyond the trivial bounds $0\le\ell\le n^{2}$ and $0\le\operatorname{rank}M\le n^{2}$, which are the dimensions of two unrelated spaces.

### The Rank of a Product

**Theorem.** For a product,
$$
\operatorname{rank}T_{A,B}=\operatorname{rank}A\cdot\operatorname{rank}B\in\{rs:0\le r,s\le n\}.
$$

*Proof.* The matrix is $B^{\mathsf T}\otimes A$ and the rank of a Kronecker product is the product of the ranks.

**The two ends of the same pair.** At one end, $\ell=1$ for every product whatever its rank; at the other end, the products of full rank form the open dense part of the cone and the products of rank one form the closed part. **The cone of products is stratified by the ordinary rank with strata of dimensions $r(2n-r)+s(2n-s)-1$, and by the length with a single stratum $\ell=1$.**

### The Generic Values

**Theorem.** On an open dense subset of $\operatorname{End}(M_{n}(\mathbb{C}))$,
$$
\ell(M)=n^{2},\qquad \operatorname{rank}M=n^{2}.
$$

*Proof.* The condition $\det c(M)\ne0$ is the nonvanishing of a polynomial, hence open and dense, and it gives $\ell=n^{2}$. The condition $\det M\ne0$ is likewise open and dense and gives the full rank. The two conditions are simultaneously generic, since the intersection of two dense open sets is dense and open.

**The degenerate coincidence.** The two generic values agree, and this is a coincidence of numbers and not a relation: they agree because both are the dimension $n^{2}$ of the two spaces, and the agreement fails on every stratum of positive codimension. **A statement true generically and false on a dense-in-itself closed set is exactly what the length is for.**

## When the Theorem Fails

### The Commutative Case

**The collapse.** Let $A$ be commutative. Then $A^{\mathrm{opp}}=A$ and $T_{A,B}=L_{AB}$, so the product set is the one-sided family of dimension $N$, and every nonzero member has length one. The theorem $\ell=\operatorname{rank}c$ survives in the form "the length is $0$ or $1$", and it becomes empty.

**The array is not well defined.** In the commutative case the map $A\otimes A\to\operatorname{End}(A)$ has kernel of dimension $N^{2}-N$, so an operator has many coefficient arrays, of different ranks. The dual numbers give the example: $\varepsilon X\varepsilon=0$ for every $X$, so the tensor $\varepsilon\otimes\varepsilon$ lies in the kernel, and the operator $L_{1}$ has the array of $1\otimes1$, of rank one, and also the array of $1\otimes1+\varepsilon\otimes\varepsilon$, of rank two. **The rank of the array is then a property of the chosen expansion and not of the operator.**

**The criterion.** The identity $\ell(M)=\operatorname{rank}c(M)$ holds for an algebra $A$ exactly when the multiplication map $A\otimes A^{\mathrm{opp}}\to\operatorname{End}(A)$ is injective, that is exactly when $A$ is central simple. Over $\mathbb{C}$ these are the algebras $M_{n}(\mathbb{C})$, so **the theorem is a theorem about matrix algebras and about nothing else**: a split algebra, a commutative algebra or a product of two matrix algebras all fail it.

**The reduced biquaternion case.** The algebra $\mathbb{C}\times\mathbb{C}$ is commutative, of dimension two, and its operator space has dimension four. The products fill a two-dimensional subspace, every nonzero member has length one, and the length of the identity is one and not two. **The algebra has the same complex dimension as the dual numbers and the same failure of the theorem; the failure follows from the commutativity and not from the size.**

### The Two-Theory Reading

**The array is the tensor.** The coefficient array is the tensor of $M$ in $A\otimes A^{\mathrm{opp}}$, read in the basis of the products. The length is the tensor rank. For a tensor with two factors the tensor rank is the rank of the flattening, and this is the whole content of the theorem. **For a tensor with three factors the two notions part company, and this is why the statement is not a general fact about tensor rank.**

**The place of the theorem.** The corpus uses the same identity three times: in the biquaternion Peirce frame with sixteen operators, in the canonical frame with the same sixteen in another basis, and here with $n^{4}$ operators. The three statements are one statement read in three frames, and the frame changes the array by a linear conjugation and not the rank.

## Summary

The $n^{4}$ products $T_{\mu\nu}=L_{E_{\mu}}R_{E_{\nu}}$ are an orthonormal basis of the endomorphism algebra, so every operator $M$ has a coefficient array $c(M)$ of size $n^{2}\times n^{2}$, and the array of a product is the outer product $[A][B]^{\mathsf T}$ of the two coordinate columns.

The length, the least number of products in a decomposition, equals the rank of $c(M)$. It takes the values $0,\dots,n^{2}$; the set of length at most $r$ is the determinantal variety of dimension $2rn^{2}-r^{2}$; a product is exactly a matrix of coefficient rank one; and a generic matrix has length $n^{2}$.

The length and the ordinary rank are independent: a product of full rank has length one, and a generic matrix of rank one has length $n^{2}$. The theorem holds exactly for the central simple algebras, that is for $M_{n}(\mathbb{C})$; for a commutative or split algebra the coefficient array is not unique and the length collapses to $\{0,1\}$. **The length is the tensor rank in $M_{n}\otimes M_{n}^{\mathrm{opp}}$, exact because the tensor has two factors, and it is the only invariant of the endomorphism algebra that the ordinary rank does not see.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E_{\mu}$ | the matrix units, an orthonormal basis of the algebra |
| $N=n^{2}$ | the dimension of the algebra |
| $T_{\mu\nu}=L_{E_{\mu}}R_{E_{\nu}}$ | the orthonormal basis of products |
| $c(M)$ | the coefficient array of $M$, of size $N\times N$ |
| $[A]$ | the coordinate column of $A$ in the units |
| $\ell(M)$ | the length, the least number of products |
| $\mathcal{C}_{r}$ | the set of operators of length at most $r$ |
| $2rn^{2}-r^{2}$ | the complex dimension of $\mathcal{C}_{r}$ |
| $r(2n-r)+s(2n-s)-1$ | the dimension of the stratum of parameter ranks $(r,s)$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge, 1991), for the Kronecker product, the rank of a product and the determinantal varieties of a matrix space.
- Joe Harris, *Algebraic Geometry: A First Course* (Springer, 1992), for the determinantal varieties and their dimensions.
- [The Two-Sided Operators and the Segre Cone of $M_n(\mathbb{C})$](the-two-sided-operators-and-the-segre-cone-of-mnc.html), for the case $r=1$ and the cone of products.
- [The Regular Representation in Dimension $n$](the-regular-representation-in-n-dimensions.html), for the tensor form and the central simple criterion.
- [The One-Sided Operators of $M_n(\mathbb{C})$](the-one-sided-operators-of-mnc.html), for the one-sided operators of length one.
- [$M_4(\mathbb{C})$ Standard Peirce Representation : Operators](m4c-standard-peirce-representation-operators.html), for the same theorem with the sixteen Peirce-frame operators.
- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the abstract family at $n=2$.
