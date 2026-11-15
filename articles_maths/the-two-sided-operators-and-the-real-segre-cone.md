# __The Two-Sided Operators and the Real Segre Cone__

## Introduction

**The operator $X\mapsto AXB$ is linear in $X$ and bilinear in the pair $(A,B)$, and the set of all such operators is a cone of dimension $2n^{2}-1$ inside the $n^{4}$-dimensional space of operators.** The cone is not a subspace. Three rules govern it: the product $T_{A,B}T_{C,D}=T_{AC,DB}$, the rank $\operatorname{rank}T_{A,B}=(\operatorname{rank}A)(\operatorname{rank}B)$, and the description of the rank-one part as the cone over the real Segre variety.

The article defines $T_{A,B}$ and proves the three rules. It gives the Segre variety by its $2\times2$ minors, separates its two rulings and reads them as the left and the right factor, and stratifies the cone by rank. It assumes *The Matrix Algebra $M_n(\mathbb{R})$* for the matrix units, the rank and the transpose, and it defers the minimal number of summands to *The Length and the Two Ranks*.

Throughout $n\ge2$, $V=\mathbb{R}^{n}$ and $M_n=M_n(\mathbb{R})$.

## The Two-Sided Operators

**Definition.** For $A,B\in M_n$ the **two-sided operator** $T_{A,B}$ is

$$
T_{A,B}(X)=AXB .
$$

The **left** and the **right** multiplication are the cases $B=\mathrm{I}$ and $A=\mathrm{I}$:

$$
L_A=T_{A,\mathrm{I}},\qquad R_B=T_{\mathrm{I},B}.
$$

**The one-sided operators commute.** $L_A R_B(X)=A(XB)=(AX)B=R_B L_A(X)$, so $T_{A,B}=L_A R_B=R_B L_A$. The two-sided operators are therefore the composites of a left and a right multiplication, and the two orders agree.

**The map is bilinear in the pair.** For scalars $\lambda,\mu$ and matrices $A,A',B,B'$,

$$
T_{\lambda A+\mu A',B}=\lambda T_{A,B}+\mu T_{A',B},\qquad T_{A,\lambda B+\mu B'}=\lambda T_{A,B}+\mu T_{A,B'} .
$$

So $(A,B)\mapsto T_{A,B}$ is a bilinear map $M_n\times M_n\to\operatorname{End}(M_n)$, and it is not linear: $T_{A+A',B+B'}$ has the two mixed terms that $T_{A,B}+T_{A',B'}$ lacks.

**The two-sided operators span the whole operator space.** The product $E_{ij}XE_{kl}$ is $X_{jk}E_{il}$. So $T_{E_{ij},E_{kl}}$ reads the entry $(j,k)$ of $X$ and writes it in the position $(i,l)$. The $n^{4}$ operators $T_{E_{ij},E_{kl}}$ are linearly independent, because they carry $X$ to $n^{4}$ independent arrays, and they span $\operatorname{End}(M_n)$. Hence

$$
\dim\operatorname{End}(M_n)=n^{4}.
$$

## The Composition Rule

**Theorem.** For all $A,B,C,D\in M_n$,

$$
T_{A,B}T_{C,D}=T_{AC,DB}.
$$

*Proof.* Evaluate on $X$: $T_{A,B}(T_{C,D}X)=A(CXD)B=(AC)X(DB)$.

**The order of the right factors is reversed.** The left factors multiply in the order of the composition, the right factors in the reverse order. So $\operatorname{End}(M_n)$ with this product is the tensor product of the algebra with its opposite algebra,

$$
\operatorname{End}(M_n)\cong M_n\otimes M_n^{\mathrm{op}},\qquad T_{A,B}\leftrightarrow A\otimes B .
$$

**The operator algebra is a full matrix algebra.** The tensor product of two central simple algebras is central simple, and $M_n\otimes M_n^{\mathrm{op}}$ has dimension $n^{4}$. By Wedderburn it is $M_{n^{2}}(\mathbb{R})$. So the algebra of operators on $M_n$ is a full matrix algebra of degree $n^{2}$, and its simplicity is the one proved in *The Ideals, the Centre and the Simplicity of $M_n(\mathbb{R})$*.

**The identity operator is the pure tensor $\mathrm{I}\otimes\mathrm{I}$.** $T_{\mathrm{I},\mathrm{I}}(X)=X$. It is a single two-sided operator, and this is the reason for the count of the length in *The Length and the Two Ranks*.

## The Rank Formula

**The vectorisation turns the two-sided operator into a Kronecker product.** Write $\operatorname{vec}X$ for the column of the entries of $X$, taken column by column. Then

$$
\operatorname{vec}(AXB)=(B^{\mathsf T}\otimes A)\operatorname{vec}X .
$$

The identity is a comparison of entries: the entry $(i,j)$ of $AXB$ is $\sum_{k,l}A_{ik}X_{kl}B_{lj}$, and the coefficient of $X_{kl}$ is $A_{ik}B_{lj}$, which is the entry of $B^{\mathsf T}\otimes A$ in the row $(i,j)$ and the column $(k,l)$.

**Theorem.** $\operatorname{rank}T_{A,B}=(\operatorname{rank}A)(\operatorname{rank}B)$.

*Proof.* By the vectorisation the rank of $T_{A,B}$ is the rank of $B^{\mathsf T}\otimes A$. Factor $A=PQ$ and $B^{\mathsf T}=UV$ with $P,Q,U,V$ of full rank $\operatorname{rank}A$ and $\operatorname{rank}B$. Then

$$
B^{\mathsf T}\otimes A=(U\otimes P)(V\otimes Q),
$$

where $U\otimes P$ has full column rank $\operatorname{rank}A\cdot\operatorname{rank}B$ and $V\otimes Q$ has full row rank of the same value. A product of a full-column-rank and a full-row-rank matrix has the common rank, so the rank is the product.

**The rank is a product of two integers between $1$ and $n$.** The values attained are $rs$ with $1\le r,s\le n$. At $n=3$ this gives $1,2,3,4,6,9$, and the value $5$ is not attained, although it is a rank of an operator on $M_3(\mathbb{R})$. Measured at $n=3$ on random pairs of ranks $1,1$; $1,2$; $2,3$; $3,3$, the rank of $T_{A,B}$ is $1,2,6,9$.

## The Segre Variety of Rank-One Matrices

**A rank-one matrix is a product of a column and a row.** $A=ac^{\mathsf T}$ with $a,c\in V$ nonzero, and the map

$$
\mathbb{P}^{n-1}\times\mathbb{P}^{n-1}\longrightarrow\mathbb{P}(M_n),\qquad ([a],[c])\longmapsto[ac^{\mathsf T}]
$$

is injective, because $ac^{\mathsf T}$ determines the line $\mathbb{R}a$ as its image and the hyperplane $c^{\perp}$ as its kernel. Its image is the **Segre variety**, of dimension

$$
(n-1)+(n-1)=2n-2 .
$$

**The defining equations are the $2\times2$ minors.** A matrix $A$ has rank at most one exactly when

$$
A_{ij}A_{kl}-A_{il}A_{kj}=0
$$

for all $i,j,k,l$. There are $\binom{n}{2}^{2}$ such minors, nine at $n=3$, and they generate the ideal of the variety. At $n=2$ the single minor is $\det A$, and the Segre variety is the quadric cone $\{\det=0\}$ of $\mathbb{P}^{3}$. Measured on a rank-one matrix at $n=3$, all nine minors vanish to order $10^{-12}$.

**The real points are the products of real lines.** Every real point of the Segre variety is $ac^{\mathsf T}$ with $a,c$ real and nonzero. The image is the real line $\mathbb{R}a$ and the kernel is the real hyperplane $c^{\perp}$. So the real locus is exactly the set of rank-one real matrices, and it is Zariski dense.

## The Two Rulings

**Through a point of the Segre variety pass two families of lines.** Fix $c$ and let $a$ run: the matrices $ac^{\mathsf T}$ form the set of rank-one matrices with kernel $c^{\perp}$, and its projectivisation is a line $\mathbb{P}^{n-1}$. Fix $a$ and let $c$ run: the matrices with image $\mathbb{R}a$, again a line. The two families are the **rulings**, each a copy of $\mathbb{P}^{n-1}$.

**The rulings are the left and the right factor.** The first family is obtained by fixing the right factor $c$ and varying the left factor $a$; the second by fixing $a$ and varying $c$. A point lies on one line of each family. So the rulings are the fibres of the two projections of $\mathbb{P}^{n-1}\times\mathbb{P}^{n-1}$, and the two projections are the left factor and the right factor of the product.

**The transpose exchanges the two rulings.** It sends $ac^{\mathsf T}$ to $ca^{\mathsf T}$, so a point is fixed only when $a$ and $c$ are proportional, at the symmetric rank-one matrices $aa^{\mathsf T}$.

## The Real Segre Cone

**The image of $(A,B)\mapsto T_{A,B}$ is a cone.** If $T=T_{A,B}$ then $\lambda T=T_{\lambda A,B}$, so the image is closed under scaling. It is the **real Segre cone**

$$
\mathcal{C}=\{T_{A,B}:A,B\in M_n\}\subset\operatorname{End}(M_n).
$$

**Two pairs give the same operator only up to a common scalar.** If $A\otimes B=A'\otimes B'$ with both tensors nonzero, then $A'=\lambda A$ and $B'=\lambda^{-1}B$. So the map

$$
\mathbb{P}(M_n)\times\mathbb{P}(M_n)\longrightarrow\mathbb{P}(\operatorname{End}(M_n)),\qquad ([A],[B])\longmapsto[T_{A,B}]
$$

is injective. Its image has dimension

$$
(n^{2}-1)+(n^{2}-1)=2n^{2}-2,
$$

and the cone $\mathcal{C}$ over it has dimension $2n^{2}-1$. At $n=2$ that is $7$ inside the $16$-dimensional operator space; at $n=3$ it is $17$ inside $81$.

**The cone is not a subspace.** The diagonal projection $D(X)=\operatorname{diag}(X)$ is not two-sided. If $D=T_{A,B}$ then $n=\operatorname{rank}D=(\operatorname{rank}A)(\operatorname{rank}B)$, so one factor has rank one; say $\operatorname{rank}A=1$. Then the image of $T_{A,B}$ lies in the image of $A$, which is a line, while the image of $D$ is the diagonal, of dimension $n$. So $\mathcal{C}$ is not closed under addition: $D=T_{E_{11},E_{11}}+\cdots+T_{E_{nn},E_{nn}}$ is a sum of $n$ two-sided operators and is not one. A least-squares fit of $D$ by a two-sided operator at $n=3$ leaves a residual of $1.41$ against a target norm of $1.73$.

**The cone spans the whole space.** The $n^{4}$ operators $T_{E_{ij},E_{kl}}$ are a basis, so the linear span of $\mathcal{C}$ is $\operatorname{End}(M_n)$.

## The Rank-One Two-Sided Operators

**Theorem.** $\operatorname{rank}T_{A,B}=1$ exactly when $\operatorname{rank}A=\operatorname{rank}B=1$.

The theorem is the product formula with both factors equal to one. On such a pair, with $A=ac^{\mathsf T}$ and $B=bd^{\mathsf T}$,

$$
T_{A,B}(X)=a\,(c^{\mathsf T}Xb)\,d^{\mathsf T},
$$

a rank-one operator whose image is the line $\mathbb{R}ad^{\mathsf T}$ and whose kernel is the hyperplane $\{X:c^{\mathsf T}Xb=0\}$. Measured on random rank-one pairs at $n=2$ and $n=3$, the rank of $T_{A,B}$ is one in both cases.

**Their set is a product of two Segre varieties.** The pair $([A],[B])$ runs over the product of the Segre variety with itself, since each factor must have rank one. The projectivised set has dimension

$$
(2n-2)+(2n-2)=4n-4,
$$

and the cone over it has dimension $4n-3$. Each factor is a copy of $\mathbb{P}^{n-1}\times\mathbb{P}^{n-1}$.

**The two rulings of the larger product are again the left and the right factor.** Fix $[B]$ and let $[A]$ run over the Segre variety: a linear space of dimension $2n-2$ inside the cone. Fix $[A]$ and let $[B]$ run: a second family of the same dimension. A rank-one two-sided operator lies on one member of each family; the left factor labels one family and the right factor the other.

## The Stratification by Rank

**The stratum of rank $rs$ is the image of the pairs of ranks $r$ and $s$.** Let $M_{n}^{\le r}$ be the set of matrices of rank at most $r$, of dimension $2nr-r^{2}$. The pairs with $\operatorname{rank}A\le r$ and $\operatorname{rank}B\le s$ form a set of dimension $(2nr-r^{2})+(2ns-s^{2})$, and the scaling $T_{\lambda A,B}=\lambda T_{A,B}$ removes one dimension. So

$$
\dim\{T_{A,B}:\operatorname{rank}A\le r,\ \operatorname{rank}B\le s\}=(2nr-r^{2})+(2ns-s^{2})-1 .
$$

At $r=s=1$ this is $4n-3$, the cone of the rank-one operators; at $r=s=n$ it is $2n^{2}-1$, the whole cone. The two ends match the earlier counts.

**The rank strata of the cone are not the rank strata of the operator space.** The operator space has strata of every rank $1,\dots,n^{2}$, of dimension $k(2n^{2}-k)$. The cone meets only the ranks that factor, and inside a fixed rank $rs$ it is a proper subset of the stratum. At $n=3$ the stratum of rank $5$ has dimension $65$, and the cone has no point in it.

**The rank bounds the length.** Each two-sided operator has rank at most $n^{2}$, and a sum of $k$ of them has rank at most $kn^{2}$. So an operator of rank $m$ needs at least $m/n^{2}$ summands. The exact count, and the proof that every operator is a sum of at most $n^{2}$ two-sided operators, is *The Length and the Two Ranks*.

## Summary

The two-sided operator $T_{A,B}(X)=AXB$ is the composite of a left and a right multiplication, and $(A,B)\mapsto T_{A,B}$ is bilinear with image the real Segre cone of dimension $2n^{2}-1$ inside the $n^{4}$-dimensional operator space. The operators compose by $T_{A,B}T_{C,D}=T_{AC,DB}$, so the operator algebra is $M_n\otimes M_n^{\mathrm{op}}\cong M_{n^{2}}(\mathbb{R})$. The rank multiplies, $\operatorname{rank}T_{A,B}=(\operatorname{rank}A)(\operatorname{rank}B)$, so the ranks attained in the cone are the products $rs$. The rank-one members are the pairs of rank-one matrices, and their set is the cone over the product of two real Segre varieties, of dimension $4n-4$ projectively and $4n-3$ affinely. The Segre variety itself has dimension $2n-2$, is defined by the $2\times2$ minors, and its two rulings are the left and the right factor. The cone is not a subspace: the diagonal projection is a sum of $n$ two-sided operators and is not one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_{A,B}(X)=AXB$ | the two-sided operator |
| $L_A=T_{A,\mathrm{I}}$, $R_B=T_{\mathrm{I},B}$ | the left and the right multiplication |
| $\operatorname{End}(M_n)$ | the algebra of operators on $M_n$, of dimension $n^{4}$ |
| $\mathcal{C}$ | the real Segre cone, of dimension $2n^{2}-1$ |
| $ac^{\mathsf T}$ | a rank-one matrix, the product of a column and a row |
| $\mathbb{P}^{n-1}\times\mathbb{P}^{n-1}$ | the Segre variety, of dimension $2n-2$ |
| $A_{ij}A_{kl}-A_{il}A_{kj}$ | the $2\times2$ minors, the equations of the Segre variety |
| rulings | the two families of $\mathbb{P}^{n-1}$ on the Segre variety, the left and the right factor |
| $M_{n}^{\le r}$ | the matrices of rank at most $r$, of dimension $2nr-r^{2}$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the tensor product of matrix algebras, the opposite algebra and the two-sided multiplication.
- Igor R. Shafarevich, *Basic Algebraic Geometry 1* (Springer, 2013), for the Segre varieties, their rulings and their minors.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the matrix units, the rank and the transpose.
- [The Ideals, the Centre and the Simplicity of $M_n(\mathbb{R})$](the-ideals-the-centre-and-the-simplicity-of-mnr.html), for the simplicity of the operator algebra.
- [The Length and the Two Ranks](the-length-and-the-two-ranks-over-r.html), for the minimal number of summands and the two ranks of an operator.
