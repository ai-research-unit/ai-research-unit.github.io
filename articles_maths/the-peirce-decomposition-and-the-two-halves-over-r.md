# __The Peirce Decomposition and the Two Halves over $\mathbb{R}$__

## Introduction

**The transpose sends the corner $A_{kl}$ to the corner $A_{lk}$, so each corner pair splits into a symmetric and an antisymmetric part of equal dimension, and the two halves of $M_{n}(\mathbb{R})$ are thereby graded by the frame.**

The article shows that a symmetric frame makes the transpose permute the corners, computes both halves of a corner pair and of a diagonal corner, proves the total identity for the symmetric dimensions, and checks it on the rank vectors $(2,2)$, $(3,1)$ and $(2,1,1)$ at $n=4$. It assumes *The Peirce Basis and the Corners over $\mathbb{R}$* for the corners and the frame, and it defers the Jordan reading of the symmetric half to *The Peirce Decomposition of $\operatorname{Sym}_n$ as a Jordan Algebra*.

## The Frame and the Transpose

**A frame is called symmetric when every idempotent is symmetric.** This article treats frames with

$$
P_{k}^{\mathsf T}=P_{k},\qquad k=1,\dots,n,
$$

together with $P_{k}P_{l}=\delta_{kl}P_{k}$ and $\sum_{k}P_{k}=\mathrm{I}$. A symmetric frame is an orthogonal decomposition $\mathbb{R}^{n}=V_{1}\oplus\cdots\oplus V_{n}$ into pairwise orthogonal subspaces, with $P_{k}$ the orthogonal projection onto $V_{k}$ and $\operatorname{rk}P_{k}=r_{k}$.

**The transpose acts on the corners of a symmetric frame by exchanging the two indices.** Because $P_{k}^{\mathsf T}=P_{k}$,

$$
(P_{k}XP_{l})^{\mathsf T}=P_{l}^{\mathsf T}X^{\mathsf T}P_{k}^{\mathsf T}=P_{l}X^{\mathsf T}P_{k}\in A_{lk}.
$$

So $A_{kl}^{\mathsf T}\subseteq A_{lk}$, and applying the same computation to $A_{lk}$ gives equality of dimensions and the identity

$$
A_{kl}^{\mathsf T}=A_{lk}.
$$

**For a non-symmetric frame the statement changes.** The transpose of a corner of $P$ is a corner of the transposed frame, not of $P$, so the exchange of indices needs the frame to be fixed by the transpose.

**The transpose is $\mathbb{R}$-linear, so it acts inside the real algebra.** It is not conjugate linear and it fixes every real scalar. Its fixed space is $\operatorname{Sym}_n$ and its space of eigenvalue $-1$ is $\operatorname{Skew}_n$, of dimensions $n(n+1)/2$ and $n(n-1)/2$.

## The Transpose on the Corner Pair

**A corner pair $A_{kl}+A_{lk}$ is invariant under the transpose.** The transpose carries $A_{kl}$ to $A_{lk}$ and $A_{lk}$ to $A_{kl}$, so it preserves their sum. On that sum it is an involution, and the sum splits into its two eigenspaces.

**Proposition.** For $k\ne l$,

$$
\operatorname{Sym}(A_{kl}+A_{lk})=\{B+B^{\mathsf T}:B\in A_{kl}\},\qquad
\operatorname{Skew}(A_{kl}+A_{lk})=\{B-B^{\mathsf T}:B\in A_{kl}\},
$$

and both have dimension $r_{k}r_{l}$.

*Proof.* An element of the sum is $X=B+C$ with $B\in A_{kl}$ and $C\in A_{lk}$. Then $X^{\mathsf T}=C^{\mathsf T}+B^{\mathsf T}$, so $X$ is symmetric exactly when $C=B^{\mathsf T}$, and antisymmetric exactly when $C=-B^{\mathsf T}$. The map $B\mapsto B+B^{\mathsf T}$ is injective on $A_{kl}$, because $B+B^{\mathsf T}=0$ with $B\in A_{kl}$ forces $B=-B^{\mathsf T}\in A_{kl}\cap A_{lk}=0$; likewise for $B\mapsto B-B^{\mathsf T}$. Both images therefore have the dimension $r_{k}r_{l}$ of $A_{kl}$, and $r_{k}r_{l}+r_{k}r_{l}=2r_{k}r_{l}=\dim(A_{kl}+A_{lk})$.

**The two halves of a corner pair are the symmetric and the antisymmetric maps between two orthogonal subspaces.** A map $B:V_{l}\to V_{k}$ has a transpose $B^{\mathsf T}:V_{k}\to V_{l}$, and the pair $(B,B^{\mathsf T})$ is symmetric while $(B,-B^{\mathsf T})$ is antisymmetric. The symmetric part is the graph of the transpose, the antisymmetric part the graph of its negative.

## The Diagonal Corner

**A diagonal corner is invariant under the transpose, and it splits into its symmetric and antisymmetric parts.** For $k=l$ the corner $A_{kk}$ is carried to itself, and

$$
A_{kk}=\operatorname{Sym}(A_{kk})\oplus\operatorname{Skew}(A_{kk}),
$$

with

$$
\dim\operatorname{Sym}(A_{kk})=\frac{r_{k}(r_{k}+1)}{2},\qquad
\dim\operatorname{Skew}(A_{kk})=\frac{r_{k}(r_{k}-1)}{2}.
$$

The two dimensions add to $r_{k}^{2}=\dim A_{kk}$, and the split is the one of *The Matrix Algebra $M_n(\mathbb{R})$* applied to the smaller algebra $A_{kk}\cong M_{r_{k}}(\mathbb{R})$.

**The two parts of a diagonal corner close under different products.** The symmetric elements are closed under $X\circ Y=\tfrac12(XY+YX)$ and the antisymmetric ones under $[X,Y]=XY-YX$; no single product closes on the whole corner.

**The trace form is positive definite on the symmetric part and negative definite on the antisymmetric part.** For a symmetric $S$ in the corner, $\operatorname{tr}(S^{2})=\sum S_{ij}^{2}>0$, and for an antisymmetric $K$, $\operatorname{tr}(K^{2})=-\sum K_{ij}^{2}<0$. The corner therefore contributes $r_{k}(r_{k}+1)/2$ positive and $r_{k}(r_{k}-1)/2$ negative directions to the inertia.

## The Total Identity

**The symmetric dimensions of all the corners add to $n(n+1)/2$.**

$$
\sum_{k=1}^{n}\frac{r_{k}(r_{k}+1)}{2}+\sum_{k<l}r_{k}r_{l}=\frac{n(n+1)}{2}.
$$

*Proof.* The second sum is half of $n^{2}-\sum_{k}r_{k}^{2}$, since $\big(\sum_{k}r_{k}\big)^{2}=\sum_{k}r_{k}^{2}+2\sum_{k<l}r_{k}r_{l}$ and $\sum_{k}r_{k}=n$. Hence the left side equals

$$
\frac{\sum_{k}r_{k}^{2}+n}{2}+\frac{n^{2}-\sum_{k}r_{k}^{2}}{2}=\frac{n^{2}+n}{2}.
$$

**The antisymmetric dimensions add to $n(n-1)/2$.** The same computation with $r_{k}(r_{k}-1)/2$ gives

$$
\frac{\sum_{k}r_{k}^{2}-n}{2}+\frac{n^{2}-\sum_{k}r_{k}^{2}}{2}=\frac{n^{2}-n}{2}.
$$

**The two totals are the dimensions of the two halves.** Summing them gives $n(n+1)/2+n(n-1)/2=n^{2}$, so the corner pairs account for the whole algebra, and the identity depends on the frame only through its rank vector.

## The Grading of the Symmetric Half

**The symmetric half is the direct sum of its corner contributions.**

$$
\operatorname{Sym}_n=\bigoplus_{k=1}^{n}\operatorname{Sym}(A_{kk})\ \oplus\ \bigoplus_{k<l}\operatorname{Sym}(A_{kl}+A_{lk}).
$$

*Proof.* Every $X\in\operatorname{Sym}_n$ splits as $X=\sum_{k,l}X_{kl}$ with $X_{kl}\in A_{kl}$, and the symmetry gives $X_{kl}^{\mathsf T}=X_{lk}$. So $X$ is determined by the diagonal blocks $X_{kk}\in A_{kk}$ and by the pairs $(X_{kl},X_{lk})$ with $k<l$, each pair symmetric in the sense of the corner-pair proposition. The sum of the displayed spaces is therefore the whole half, and the sum is direct because the corners are independent.

**The graded pieces are the eigenspaces of the frame's Peirce operators cut by the transpose.** The piece labelled $k$ is $\operatorname{Sym}(A_{kk})$, the fixed part of the corner $A_{kk}$; the piece labelled $k<l$ is the fixed part of $A_{kl}+A_{lk}$. The labels are the unordered pairs $\{k,l\}$, and there are $n(n+1)/2$ of them.

**At a complete frame every piece is a line.** With all $r_{k}=1$ the diagonal pieces have dimension $1$ and the pair pieces too, so the symmetric half is a direct sum of $n+n(n-1)/2=n(n+1)/2$ lines. This is the finest grading the frame gives.

**The grading refines the two-block Peirce decomposition.** Taking the coarse frame $P_{1}=E$, $P_{2}=\mathrm{I}-E$ with ranks $r$ and $n-r$ gives three pieces: $\operatorname{Sym}(A_{11})$ of dimension $r(r+1)/2$, $\operatorname{Sym}(A_{22})$ of dimension $(n-r)(n-r+1)/2$ and $\operatorname{Sym}(A_{12}+A_{21})$ of dimension $r(n-r)$. These are the three Peirce spaces of the Jordan algebra $\operatorname{Sym}_n$ relative to $E$, in the order $1$, $0$, $\tfrac12$.

## The Grading of the Antisymmetric Half

**The antisymmetric half is graded the same way.**

$$
\operatorname{Skew}_n=\bigoplus_{k=1}^{n}\operatorname{Skew}(A_{kk})\ \oplus\ \bigoplus_{k<l}\operatorname{Skew}(A_{kl}+A_{lk}).
$$

The proof is the same computation with $X_{lk}=-X_{kl}^{\mathsf T}$, and the dimensions are $r_{k}(r_{k}-1)/2$ and $r_{k}r_{l}$. At a complete frame the diagonal pieces vanish, and the antisymmetric half is a direct sum of $n(n-1)/2$ lines, one for each pair $k<l$.

**The antisymmetric half is a Lie algebra graded by its corners.** $\operatorname{Skew}_n=\mathfrak{so}(n)$ is closed under the commutator, and the bracket of two corner pieces lands in the piece named by the surviving indices, which is the root-space pattern of $\mathfrak{so}(n)$ read in the frame.

## The Two Halves over $\mathbb{R}$ and over $\mathbb{C}$

**Over $\mathbb{R}$ the two halves are different algebras.** $\operatorname{Sym}_n$ is closed under the anticommutator and is a formally real Jordan algebra; $\operatorname{Skew}_n$ is closed under the commutator and is the Lie algebra $\mathfrak{so}(n)$ of the orthogonal group. The dimensions differ, $n(n+1)/2$ against $n(n-1)/2$, and the trace form has opposite signs on the two halves.

**Over $\mathbb{C}$ the same two eigenspaces exist, and the form on them is isotropic.** Complexifying gives $\operatorname{Sym}_n(\mathbb{C})$ and $\operatorname{Skew}_n(\mathbb{C})$, of complex dimensions $n(n+1)/2$ and $n(n-1)/2$, and the corner exchange $A_{kl}^{\mathsf T}=A_{lk}$ holds for a complex symmetric frame word for word. What the complex picture loses is the sign: over $\mathbb{C}$ the form $\operatorname{tr}(XY)$ vanishes on nonzero elements of both halves. A symmetric example at $n=2$ is

$$
X=\begin{pmatrix}1&i\\ i&-1\end{pmatrix},\qquad X^{2}=0,
$$

and an antisymmetric one at $n=3$ is built from $Y_{12}=1$, $Y_{13}=i$, whose square has zero trace. So over $\mathbb{C}$ neither half is definite and the sign that separates them over $\mathbb{R}$ has no meaning.

**The inertia of the trace form is the real invariant.** Over $\mathbb{R}$ the form $\langle X,Y\rangle=\operatorname{tr}(XY)$ has inertia $\big(n(n+1)/2,\,n(n-1)/2\big)$, positive on $\operatorname{Sym}_n$ and negative on $\operatorname{Skew}_n$. A complex bilinear form has no inertia, so the definite split computed here is a real statement.

**The grading is a real statement about the transpose.** The eigenvalues $\pm1$ are real numbers, so the pieces of the grading are real subspaces of real dimensions $r_{k}r_{l}$ and $r_{k}(r_{k}\pm1)/2$, and the two halves are the two real eigenspaces of one $\mathbb{R}$-linear involution. The Jordan algebra $\operatorname{Sym}_n$ is formally real, while $\operatorname{Sym}_n(\mathbb{C})$ contains the nilpotent $X$ above; that difference, not the existence of the splitting, is what the base field decides.

## Checks at $n=4$

**The identity holds for the rank vectors $(2,2)$, $(3,1)$ and $(2,1,1)$.** For each vector, the symmetric total is

| ranks | diagonal terms | pair terms | total |
|---|---|---|---|
| $(2,2)$ | $3+3$ | $4$ | $10$ |
| $(3,1)$ | $6+1$ | $3$ | $10$ |
| $(2,1,1)$ | $3+1+1$ | $2+2+1$ | $10$ |

and $10=4\cdot5/2$ in all three cases. The antisymmetric totals are $1+1+4=6$, $3+0+3=6$ and $1+0+0+2+2+1=6$, which is $4\cdot3/2$.

**The corner dimensions are the predicted ones.** With the rank vector $(2,1,1)$ the corner pairs give symmetric and antisymmetric dimensions $2,2$ for $(0,1)$ and $(0,2)$, and $1,1$ for $(1,2)$; the diagonal corner of rank $2$ gives $3,1$ and the two corners of rank $1$ give $1,0$. The numbers agree with $r_{k}r_{l}$ and $r_{k}(r_{k}\pm1)/2$.

## Summary

A symmetric frame $P_{k}=P_{k}^{\mathsf T}$ makes the transpose exchange the corners, $A_{kl}^{\mathsf T}=A_{lk}$, so each corner pair $A_{kl}+A_{lk}$ with $k\ne l$ splits into a symmetric part and an antisymmetric part, both of dimension $r_{k}r_{l}$, and each diagonal corner $A_{kk}$ splits into $\operatorname{Sym}(A_{kk})$ of dimension $r_{k}(r_{k}+1)/2$ and $\operatorname{Skew}(A_{kk})$ of dimension $r_{k}(r_{k}-1)/2$. The symmetric dimensions satisfy $\sum_{k}r_{k}(r_{k}+1)/2+\sum_{k<l}r_{k}r_{l}=n(n+1)/2$ and the antisymmetric ones $n(n-1)/2$, the two sums adding to $n^{2}$; at $n=4$ the rank vectors $(2,2)$, $(3,1)$ and $(2,1,1)$ all give $10$ and $6$. The two halves are therefore graded by the frame, with the pairs $\{k,l\}$ as index set. The grading is a real statement: the eigenvalues are $\pm1$, the pieces are real subspaces of real dimensions $r_{k}r_{l}$, the trace form has inertia $(n(n+1)/2,n(n-1)/2)$, and over $\mathbb{C}$ the same two subspaces exist but the form is isotropic on both.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P_{k}$ | A symmetric idempotent of the frame, $P_{k}^{\mathsf T}=P_{k}$ |
| $r_{k}=\operatorname{rk}P_{k}$ | The rank of $P_{k}$, with $\sum_{k}r_{k}=n$ |
| $A_{kl}=P_{k}M_{n}(\mathbb{R})P_{l}$ | The corner, with $A_{kl}^{\mathsf T}=A_{lk}$ |
| $\operatorname{Sym}(A_{kl}+A_{lk})$ | The symmetric part of a corner pair, of dimension $r_{k}r_{l}$ |
| $\operatorname{Skew}(A_{kl}+A_{lk})$ | The antisymmetric part of a corner pair, of dimension $r_{k}r_{l}$ |
| $\operatorname{Sym}(A_{kk})$ | The symmetric part of a diagonal corner, of dimension $r_{k}(r_{k}+1)/2$ |
| $\operatorname{Skew}(A_{kk})$ | The antisymmetric part of a diagonal corner, of dimension $r_{k}(r_{k}-1)/2$ |
| $\{k,l\}$ | The label of a graded piece, with $k\le l$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for symmetric and antisymmetric matrices and the transpose.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for Peirce decompositions and the relation between a Jordan algebra and its corners.
- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (American Mathematical Society, 2001), for the graded structure of $\mathfrak{so}(n)$ and its root spaces.
- [The Peirce Basis and the Corners over $\mathbb{R}$](the-peirce-basis-and-the-corners-over-r.html), for the corners and the frame that the grading uses.
- [The Peirce Decomposition of $\operatorname{Sym}_n$ as a Jordan Algebra](the-peirce-decomposition-of-sym-n-r-as-a-jordan-algebra.html), for the symmetric half read as a Jordan algebra.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the trace form, its inertia and the two halves.
