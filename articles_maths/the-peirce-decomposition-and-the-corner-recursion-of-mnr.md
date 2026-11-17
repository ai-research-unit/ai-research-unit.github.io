# __The Peirce Decomposition and the Corner Recursion of $M_n(\mathbb{R})$__

## Introduction

**A single real idempotent of rank $r$ cuts $M_{n}(\mathbb{R})$ into four corners of dimensions $r^{2}$, $r(n-r)$, $(n-r)r$ and $(n-r)^{2}$, and the cut is a recursion: the algebra contains $M_{r}(\mathbb{R})$, $M_{n-r}(\mathbb{R})$ and two bimodules between them.**

The article states the four corners, identifies the two diagonal corners with matrix algebras and the two off-diagonal ones with spaces of rectangular matrices, proves that the block multiplication is the multiplication of the algebra, reads the recursion and its termination after $n$ steps, and computes the trace form on the four corners, where the off-diagonal pair carries a perfect pairing. The ledger is $1+2+2+4=9$ at $n=3$ with $r=1$, and $4+4+4+4=16$ at $n=4$ with $r=2$. It assumes *The Peirce Basis and the Corners over $\mathbb{R}$* for the frame, and it defers the finer decomposition of a full frame to *The Peirce Decomposition and the Two Halves over $\mathbb{R}$*.

## The Four Corners of an Idempotent

**An idempotent and its complement cut the algebra into four blocks.** Let $P\in M_{n}(\mathbb{R})$ satisfy $P^{2}=P$, with rank $r$ and $1\le r\le n-1$, and put $Q=\mathrm{I}-P$, which is also idempotent, of rank $n-r$, with $PQ=QP=0$ and $P+Q=\mathrm{I}$. The four corners are

$$
A=PMP,\qquad B=PMQ,\qquad C=QMP,\qquad D=QMQ .
$$

**Proposition.** The four corners are independent and sum to the algebra, and

$$
\dim A=r^{2},\qquad \dim B=r(n-r),\qquad \dim C=(n-r)r,\qquad \dim D=(n-r)^{2},
$$

with $r^{2}+2r(n-r)+(n-r)^{2}=n^{2}$.

*Proof.* Expand $\mathrm{I}=P+Q$ on both sides of $X$:

$$
X=(P+Q)X(P+Q)=PXP+PXQ+QXP+QXQ .
$$

Independence follows by multiplying a vanishing sum by $P$ or $Q$ on each side. For the dimensions, $A=\operatorname{End}(\operatorname{im}P)$ has dimension $r^{2}$, $D=\operatorname{End}(\operatorname{im}Q)$ has dimension $(n-r)^{2}$, and $B=\operatorname{Hom}(\operatorname{im}Q,\operatorname{im}P)$, $C=\operatorname{Hom}(\operatorname{im}P,\operatorname{im}Q)$ both have dimension $r(n-r)$.

**The two off-diagonal corners have the same dimension and are dual to each other.** A map $\operatorname{im}Q\to\operatorname{im}P$ and a map $\operatorname{im}P\to\operatorname{im}Q$ compose to an endomorphism of $\operatorname{im}P$ or of $\operatorname{im}Q$, which is the multiplication rule of the next section.

**The corners are the eigenspaces of the two Peirce operators of $P$.** With $L(X)=PX$ and $R(X)=XP$, the corners are

$$
A=\{L=1,R=1\},\qquad B=\{L=1,R=0\},\qquad C=\{L=0,R=1\},\qquad D=\{L=0,R=0\},
$$

read as the joint eigenvalues of the commuting pair $(L,R)$. The eigenvalues are the real numbers $0$ and $1$, so the cut is a real cut with no complex number in it.

## The Corner Isomorphisms

**The diagonal corners are matrix algebras over $\mathbb{R}$.** Choosing a real basis of $\operatorname{im}P$ identifies $A=PMP$ with $M_{r}(\mathbb{R})$ and $D=QMQ$ with $M_{n-r}(\mathbb{R})$. The identification is an isomorphism of algebras: the product in $A$ is the product of the arrays, and the unit of $A$ is $P$, which is the identity of the smaller algebra.

**The off-diagonal corners are spaces of rectangular arrays.** With bases adapted to the decomposition $\mathbb{R}^{n}=\operatorname{im}P\oplus\operatorname{im}Q$, the corner $B$ is the space of $r\times(n-r)$ real arrays and $C$ is the space of $(n-r)\times r$ arrays. So

$$
A\cong M_{r}(\mathbb{R}),\qquad B\cong M_{r\times(n-r)}(\mathbb{R}),\qquad C\cong M_{(n-r)\times r}(\mathbb{R}),\qquad D\cong M_{n-r}(\mathbb{R}).
$$

**The two off-diagonal corners see each other through the products $BC$ and $CB$.** The product of an array of $B$ with an array of $C$ is an $r\times r$ array, in $A$, and the product in the other order is an $(n-r)\times(n-r)$ array, in $D$. This is why the recursion below is a recursion and not a decomposition into four separate algebras.

## The Multiplication Table of the Four Corners

**The four corners multiply by the block rule of the matrix product.**

$$
A\cdot A\subseteq A,\quad A\cdot B\subseteq B,\quad B\cdot C\subseteq A,\quad B\cdot D\subseteq B,
$$

$$
C\cdot A\subseteq C,\quad C\cdot B\subseteq D,\quad D\cdot C\subseteq C,\quad D\cdot D\subseteq D,
$$

and the products $A\cdot C$, $B\cdot A$, $C\cdot D$, $D\cdot B$, $B\cdot B$, $C\cdot C$ vanish.

*Proof.* Write each factor as a product of $P$'s and $Q$'s and use $P^{2}=P$, $Q^{2}=Q$ and $PQ=QP=0$. For instance an element of $B$ is $PXQ$ with $X\in M$, and an element of $C$ is $QYP$, so $PXQ\cdot QYP=PXQYP\in A$. Each vanishing product contains a factor $Q\cdot P$ or $P\cdot Q$.

**The table is the table of a block matrix.** In the adapted basis the four corners are the four blocks

$$
X=\begin{pmatrix}A_{0}&B_{0}\\ C_{0}&D_{0}\end{pmatrix},
$$

and the table above is the rule for the product of two such block matrices. So the Peirce decomposition is the block decomposition, written without a basis.

**The corners of the pair generate each other.** $B\cdot C\subseteq A$ and $C\cdot B\subseteq D$ mean that the two off-diagonal corners, multiplied in the two orders, recover both diagonal corners. In particular if $B$ and $C$ are nonzero then $A$ and $D$ are nonzero, so the algebra is generated by its off-diagonal corners together with one diagonal corner.

## The Recursion

**The algebra contains the two smaller matrix algebras and the two bimodules, and this is the recursion.**

$$
M_{n}(\mathbb{R})=M_{r}(\mathbb{R})\ \oplus\ M_{n-r}(\mathbb{R})\ \oplus\ B\ \oplus\ C,
$$

where $B$ is a left module over $M_{r}$ and a right module over $M_{n-r}$, and $C$ is the other way round. The displayed identity is a decomposition of vector spaces, and the multiplication table makes it a decomposition of algebras with bimodule structure.

**The Peirce rule makes the recursion an isomorphism of algebras.** The map

$$
X\longmapsto \begin{pmatrix}PXP& PXQ\\ QXP& QXQ\end{pmatrix}
$$

is $\mathbb{R}$-linear, injective by the independence of the corners, surjective by the dimension count, and multiplicative because the block product is the product of the matrices. Its inverse is the sum of the four components. So $M_{n}(\mathbb{R})$ is the algebra of $2\times2$ block matrices with entries in $M_{r}$, $M_{r\times(n-r)}$, $M_{(n-r)\times r}$ and $M_{n-r}$.

**The recursion is read with $r=1$.** Taking a rank-one idempotent gives

$$
M_{n}(\mathbb{R})\cong \mathbb{R}\ \oplus\ M_{n-1}(\mathbb{R})\ \oplus\ \mathbb{R}^{n-1}\ \oplus\ (\mathbb{R}^{n-1})^{*},
$$

so the algebra is the scalars, one smaller matrix algebra, and a vector space with its dual. Iterating with $r=1$ at each step splits off one line at a time.

**The recursion terminates in $n$ steps.** Each step with $r=1$ replaces $n$ by $n-1$ and adds a line, its dual and a scalar; after $n-1$ steps the algebra $M_{n-1}$ is reduced to $M_{1}(\mathbb{R})=\mathbb{R}$, and the last step gives

$$
n+\sum_{k=1}^{n-1}2k=n+n(n-1)=n^{2}
$$

real dimensions, which is $\dim M_{n}(\mathbb{R})$. So $M_{n}(\mathbb{R})$ is built from $n^{2}$ copies of $\mathbb{R}$ by $n-1$ corner splits, each split adding one scalar and one line with its dual.

## The Trace Form on the Corners

**The trace form restricts to the trace forms of the two diagonal corners.** For $X,Y\in A$ the product $XY$ lies in $A$, and $\operatorname{tr}(XY)$ is the trace form of $A\cong M_{r}(\mathbb{R})$; the same holds in $D$. So the restriction of the form to $A$ has inertia $\big(r(r+1)/2,\,r(r-1)/2\big)$ and its restriction to $D$ has inertia $\big((n-r)(n-r+1)/2,\,(n-r)(n-r-1)/2\big)$.

**The off-diagonal corners carry a perfect pairing.**

$$
B\times C\longrightarrow\mathbb{R},\qquad (Y,Z)\longmapsto\operatorname{tr}(YZ).
$$

*Proof.* For $Y=PMQ$ and $Z=QNP$ the product $YZ=PMQNP$ lies in $A$, so the trace is a real number. If $\operatorname{tr}(YZ)=0$ for every $Z\in C$, then $\operatorname{tr}(PMQNPN')=0$ for all $N$ and all $N'$, which forces $PMQ=0$, that is, $Y=0$. The same argument with the roles exchanged gives the other side. The pairing is therefore nondegenerate, and it is a pairing between spaces of equal dimension $r(n-r)$.

**The four corners are mutually orthogonal except across the pair.** The products $AB$, $AC$, $AD$, $BC$, $BD$, $CD$ vanish except for $BC$ and $CB$, and those lie in a diagonal corner. Hence

$$
\langle A,B\rangle=\langle A,C\rangle=\langle B,D\rangle=\langle C,D\rangle=\langle A,D\rangle=0,
$$

and the trace form is the sum of its restrictions to $A$, to $D$, and to the pairing between $B$ and $C$. So the recursion for the trace form is $A\perp D$ and $B$ paired with $C$.

**The inertia of the whole form is the sum of the four contributions.** The two diagonal corners contribute their own inertias and the off-diagonal pair contributes $r(n-r)$ positive and $r(n-r)$ negative directions, since the pairing is symmetric of split type. The total is

$$
\frac{r(r+1)}{2}+r(n-r)+\frac{(n-r)(n-r+1)}{2}=\frac{n(n+1)}{2}
$$

positive and the same count with the minus signs, that is $n(n-1)/2$ negative, which is the inertia of the trace form on $M_{n}(\mathbb{R})$.

## The Dimension Ledger

**At $n=3$ with $r=1$ the four dimensions are $1$, $2$, $2$ and $4$.**

$$
1+2+2+4=9=3^{2}.
$$

The diagonal corners are $M_{1}(\mathbb{R})=\mathbb{R}$ and $M_{2}(\mathbb{R})$, and the off-diagonal corners are the column space $\mathbb{R}^{2}$ and its dual.

**At $n=4$ with $r=2$ the four dimensions are equal.**

$$
4+4+4+4=16=4^{2}.
$$

Both diagonal corners are $M_{2}(\mathbb{R})$ and both off-diagonal corners have dimension $4$.

**The ledger at other ranks agrees with the formula.** At $n=5$ with $r=2$ the dimensions are $4$, $6$, $6$ and $9$, summing to $25$; at $n=4$ with $r=1$ they are $1$, $3$, $3$ and $9$, summing to $16$; at $n=3$ with $r=2$ they are $4$, $2$, $2$ and $1$, summing to $9$. In every case the four numbers are the four blocks of the adapted basis. The blocks were built from random projections of the stated ranks and their dimensions measured by rank, and the numbers above came out in every trial.

**The count is a count of real dimensions.** Each corner is a real vector space, the blocks are real arrays, and the sum is $n^{2}$, the real dimension of the algebra. Nothing in the ledger depends on a complexification.

## Summary

A real idempotent $P$ of rank $r$ with complement $Q=\mathrm{I}-P$ cuts $M_{n}(\mathbb{R})$ into the four corners $A=PMP$, $B=PMQ$, $C=QMP$ and $D=QMQ$, of dimensions $r^{2}$, $r(n-r)$, $(n-r)r$ and $(n-r)^{2}$, which sum to $n^{2}$ and are the joint eigenspaces of $L(X)=PX$ and $R(X)=XP$. The diagonal corners are the matrix algebras $M_{r}(\mathbb{R})$ and $M_{n-r}(\mathbb{R})$, the off-diagonal ones are the rectangular array spaces, and the block multiplication is the multiplication of the algebra, so the corners give an isomorphism $M_{n}(\mathbb{R})\cong M_{2}$ of block matrices. The recursion $M_{n}\cong M_{r}\oplus M_{n-r}\oplus B\oplus C$, iterated with $r=1$, builds the algebra from $M_{1}(\mathbb{R})=\mathbb{R}$ in $n$ steps, adding a line and its dual at each step. The trace form restricts to the trace forms of $A$ and $D$, vanishes across different corners, and pairs $B$ with $C$ perfectly through $(Y,Z)\mapsto\operatorname{tr}(YZ)$; its inertia is $\big(n(n+1)/2,\,n(n-1)/2\big)$. The ledger is $1+2+2+4=9$ at $n=3$ with $r=1$ and $4+4+4+4=16$ at $n=4$ with $r=2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P$ | An idempotent of rank $r$, with $1\le r\le n-1$ |
| $Q=\mathrm{I}-P$ | The complementary idempotent, of rank $n-r$ |
| $A=PMP$ | The upper-left corner, isomorphic to $M_{r}(\mathbb{R})$ |
| $B=PMQ$ | The upper-right corner, of dimension $r(n-r)$ |
| $C=QMP$ | The lower-left corner, of dimension $r(n-r)$ |
| $D=QMQ$ | The lower-right corner, isomorphic to $M_{n-r}(\mathbb{R})$ |
| $L,R$ | The Peirce operators $X\mapsto PX$ and $X\mapsto XP$ |
| $\{k,l\}$-blocks | The four blocks of the adapted basis |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for Peirce decompositions, corner isomorphisms and the module structure of the off-diagonal corners.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the corner isomorphisms of a matrix algebra and their use in the structure theory.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for block matrices, idempotents and the trace of a product.
- [The Peirce Basis and the Corners over $\mathbb{R}$](the-peirce-basis-and-the-corners-over-r.html), for the frame, its corners and the system of matrix units.
- [The Peirce Decomposition and the Corner Recursion of $M_n(\mathbb{C})$](the-peirce-decomposition-and-the-corner-recursion-of-mnc.html), for the complex version of the same recursion.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the trace form and its indefinite inertia.
