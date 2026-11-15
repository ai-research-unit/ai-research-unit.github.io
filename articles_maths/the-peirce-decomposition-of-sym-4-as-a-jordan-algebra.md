# __The Peirce Decomposition of $\operatorname{Sym}_4$ as a Jordan Algebra__

## Introduction

**At a rank-$k$ idempotent $E$ of the symmetric half the Jordan multiplication $L_E$ has the eigenvalues $1$, $\tfrac12$, $0$, and the symmetric half of complex dimension $10$ splits into $V_1$, $V_\frac12$, $V_0$ of dimensions $\tfrac{k(k+1)}{2}$, $k(4-k)$ and $\tfrac{(4-k)(5-k)}{2}$, with the rule $V_i\circ V_j\subseteq V_{i+j}$ except that $V_\frac12\circ V_\frac12\subseteq V_1\oplus V_0$.**

The article writes the Jordan product, diagonalises the multiplication by an idempotent in a basis where the idempotent is diagonal, computes the three dimensions for every rank, proves the six Peirce rules, identifies the corner with a smaller symmetric half and the middle space with a rectangular block, and reads the ten as a sum of three pieces.

It assumes *The Jordan Algebra $\operatorname{Sym}_4$* for the product and the identity, and *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric* for the dimension. The model at order two is *The Peirce Decomposition of $\operatorname{Sym}_2$ as a Jordan Algebra*; the Hermitian version is *The Peirce Decomposition and the Two Halves at $n=4$*, and the corner recursion is *The Peirce Decomposition and the Corner Recursion of $M_4(\mathbb{C})$*.

## The Jordan Product and the Idempotent

**Definition.** $X\circ Y=\tfrac12(XY+YX)$ on $\operatorname{Sym}_4$.

**Proposition.** The product is commutative, the symmetric half is closed under it, and the unit is $\mathrm I_4$.

**Proof.** Commutativity and closure are the symmetry of the display and the symmetry of the transpose; $\mathrm I_4\circ X=X$ is immediate.

**Definition.** An **idempotent** of the Jordan algebra is $E$ with $E\circ E=E$, and its **rank** is $\operatorname{tr}E$. A **Hermitian idempotent** is one with $E^{\ast}=E$, equivalently an orthogonal projection.

**Proposition.** For a Hermitian idempotent $E$ the operator $L_E(X)=E\circ X$ is diagonalisable with the eigenvalues $1$, $\tfrac12$, $0$, and the multiplicities are the three block dimensions.

**Proof.** Conjugate by a unitary so that $E=\operatorname{diag}(1,\dots,1,0,\dots,0)$ with $k$ ones. In blocks $X=\begin{pmatrix}A&B\\B^{\mathsf T}&C\end{pmatrix}$, one has $E\circ X=\begin{pmatrix}A&\tfrac12B\\ \tfrac12B^{\mathsf T}&0\end{pmatrix}$, so $A$ is an eigenvector with eigenvalue $1$, $B$ with eigenvalue $\tfrac12$ and $C$ with eigenvalue $0$.

**Corollary.** The three eigenspaces are
$$
V_1=\Bigl\{\begin{pmatrix}A&0\\0&0\end{pmatrix}\Bigr\},\qquad V_\frac12=\Bigl\{\begin{pmatrix}0&B\\B^{\mathsf T}&0\end{pmatrix}\Bigr\},\qquad V_0=\Bigl\{\begin{pmatrix}0&0\\0&C\end{pmatrix}\Bigr\},
$$
and their direct sum is the symmetric half.

**Proof.** The eigenvalues are distinct and the three blocks span the space of symmetric matrices.

## The Three Peirce Spaces

**Definition.** $V_i=\{X\in\operatorname{Sym}_4: L_EX=iX\}$ for $i\in\{1,\tfrac12,0\}$ are the **Peirce spaces** of $E$.

**Theorem.** $\operatorname{Sym}_4=V_1\oplus V_\frac12\oplus V_0$, and the dimensions at rank $k$ are $\tfrac{k(k+1)}{2}$, $k(4-k)$ and $\tfrac{(4-k)(5-k)}{2}$.

**Proof.** $A$ is a symmetric $k\times k$ block, $C$ a symmetric $(4-k)\times(4-k)$ block and $B$ an arbitrary $k\times(4-k)$ block, so the dimensions are the counts of the independent entries of a symmetric block and of a rectangular block.

**Corollary.** The three dimensions sum to $10$ for every $k$, and the terms are
$$
k=1:\ 1+3+6,\qquad k=2:\ 3+4+3,\qquad k=3:\ 6+3+1.
$$

**Proof.** Substitution in the formula, with $\tfrac{k(k+1)}{2}+\tfrac{(4-k)(5-k)}{2}+k(4-k)=10$.

**The check at $k=1$.** For $E=E_{11}$ the space $V_1$ is the line of $E$, $V_0$ is the symmetric half of the last three coordinates of dimension $6$, and $V_\frac12$ is the three-dimensional space of the entries $B_{1j}$ with their transposes.

**Proof.** The block counts at $k=1$.

**The check at $k=2$.** For $E=\operatorname{diag}(1,1,0,0)$ the three spaces have dimension $3$, $4$ and $3$: two copies of $\operatorname{Sym}_2$ and one rectangular block.

**Proof.** The block counts at $k=2$.

## The Peirce Rules

**Theorem.** In the Jordan algebra,
$$
V_1\circ V_1\subseteq V_1,\quad V_1\circ V_\frac12\subseteq V_\frac12,\quad V_1\circ V_0=0,
$$
$$
V_\frac12\circ V_\frac12\subseteq V_1\oplus V_0,\quad V_\frac12\circ V_0\subseteq V_\frac12,\quad V_0\circ V_0\subseteq V_0.
$$

**Proof.** The first five follow from the eigenvalue rule $V_i\circ V_j\subseteq V_{i+j}$ with $i+j$ taken in $\{1,\tfrac12,0\}$ and with the product $1\cdot0$ giving the zero eigenvalue. For the middle product take $X=\begin{pmatrix}0&B\\B^{\mathsf T}&0\end{pmatrix}$ and $Y=\begin{pmatrix}0&C\\C^{\mathsf T}&0\end{pmatrix}$: then $XY=\begin{pmatrix}BC^{\mathsf T}&0\\0&B^{\mathsf T}C\end{pmatrix}$, whose two diagonal blocks are symmetric, so $X\circ Y$ lies in $V_1\oplus V_0$.

**Corollary.** The single departure from the sum rule is $V_\frac12\circ V_\frac12\subseteq V_1\oplus V_0$, and the two summands are the products $BC^{\mathsf T}$ symmetrised in the corner and $B^{\mathsf T}C$ symmetrised in the complement.

**Proof.** The computation above, block by block.

**Corollary.** $V_1\circ V_0=0$: the two diagonal Peirce spaces annihilate one another.

**Proof.** $E\circ(\mathrm I_4-E)=0$.

**The dimension of the image.** At $k=2$ the middle product is a map from the symmetric square of $V_\frac12$, of dimension $10$, into the $6$-dimensional space $V_1\oplus V_0$, so it is never injective; its image is constrained further, since $BC^{\mathsf T}$ has rank at most $2$.

**Proof.** $B=\begin{pmatrix}1&0\\0&0\end{pmatrix}$ and $C=\begin{pmatrix}0&0\\0&1\end{pmatrix}$ give $BC^{\mathsf T}=0$ and $B^{\mathsf T}C=0$, so the kernel is nonzero; and $\operatorname{rank}(BC^{\mathsf T})\le\operatorname{rank}B\le2$.

## The Corner and the Rectangular Block

**Theorem.** $V_1$ with the restricted product and the unit $E$ is a Jordan algebra isomorphic to $\operatorname{Sym}_k$, and $V_0$ with the unit $\mathrm I_4-E$ is isomorphic to $\operatorname{Sym}_{4-k}$.

**Proof.** The map $A\mapsto\begin{pmatrix}A&0\\0&0\end{pmatrix}$ is a Jordan homomorphism onto $V_1$ by the block computation, and $E$ acts as its unit.

**Corollary.** The **corner** at $E$ is a smaller symmetric half, and the Peirce decomposition of the corner at the idempotent $E'$ inside it is the Peirce decomposition of the whole algebra at $E+E'$.

**Proof.** The block form of $E+E'$ is the block form of $E'$ inside the corner, padded by the complement.

**Definition.** $V_\frac12$ is the **rectangular block** at $E$: the space of off-diagonal blocks $B$, identified with $M_{k\times(4-k)}(\mathbb{C})$.

**Proposition.** $V_\frac12$ is a bimodule over the corner and over the complement: $V_1\circ V_\frac12\subseteq V_\frac12$ and $V_0\circ V_\frac12\subseteq V_\frac12$.

**Proof.** $A$ times $B$ is a $k\times(4-k)$ block, and the transpose product is its transpose; the same for $C$.

**Corollary.** $V_\frac12$ is not an algebra for $\circ$: its square lands in $V_1\oplus V_0$ and not in $V_\frac12$, unless $B=0$.

**Proof.** $X\circ X=\begin{pmatrix}BB^{\mathsf T}&0\\0&B^{\mathsf T}B\end{pmatrix}$, which is zero exactly when $B=0$.

**The three-piece geometry.** The corner, the complement and the rectangle give the dimension count $3+4+3$ at $k=2$, which is the symmetric half read as two smaller symmetric halves and one rectangular space.

**Proof.** The theorem above at $k=2$.

## The Refinement of the Ten

**Proposition.** The Peirce decomposition refines the dimension $10$ into three pieces whose sizes depend on the rank, and at $k=2$ the pieces are $3$, $4$, $3$.

**Proof.** The dimension theorem.

**The Hermitian reading.** For the real algebra $\operatorname{Herm}_4$ of real dimension $16$ the same computation with Hermitian blocks gives the dimensions $k^{2}$, $(4-k)^{2}$ and $2k(4-k)$, which sum to $16$; the two readings differ by the conjugation, which doubles the off-diagonal block and changes the count of the symmetric block.

**Proof.** A Hermitian $k\times k$ block has $k^{2}$ real parameters, a Hermitian $(4-k)\times(4-k)$ block has $(4-k)^{2}$, and a rectangular block and its conjugate have $2k(4-k)$; a complex symmetric block has $k(k+1)/2$ complex parameters, that is $k(k+1)$ real ones.

**Corollary.** At $k=2$ the Hermitian count is $4+8+4=16$ and the symmetric count is $3+4+3=10$; both obey the same six Peirce rules, and only the dimensions of the blocks differ.

**Proof.** Substitution of $k=2$ in the two formulas.

**The refinement against the associative one.** The associative Peirce decomposition of $M_4$ at the same idempotent has the dimensions $k^{2}$, $(4-k)^{2}$ and $2k(4-k)$, summing to $16$, and it separates the two mixed corners, which the commutative product merges into one.

**Proof.** The associative Peirce spaces are $EME$, $(1-E)M(1-E)$, $EM(1-E)$ and $(1-E)ME$, while the Jordan middle space is the symmetrisation of the last two.

**Corollary.** The Jordan decomposition of the symmetric half is the associative decomposition of the whole algebra with the two mixed corners identified, and the identification loses the antisymmetric part.

**Proof.** The symmetrisation map from the two mixed corners onto $V_\frac12$ has the antisymmetric space as kernel.

**The moral.** The Peirce decomposition of the Jordan algebra is coarser than the associative one by exactly the antisymmetric part, and it is finer than the plain dimension count by the rank of the idempotent.

**Proof.** The two comparisons above.

## Summary

A Hermitian idempotent $E$ of rank $k$ splits the symmetric half of complex dimension $10$ into three Peirce spaces: the corner $V_1$ of dimension $\tfrac{k(k+1)}{2}$, the rectangular block $V_\frac12$ of dimension $k(4-k)$, and the complement $V_0$ of dimension $\tfrac{(4-k)(5-k)}{2}$. At $k=2$ the count is $3+4+3$.

The six Peirce rules hold, with $V_\frac12\circ V_\frac12\subseteq V_1\oplus V_0$ the single departure from the sum rule and $V_1\circ V_0=0$. The corner is a smaller symmetric half with unit $E$, the middle space is a bimodule and not an algebra, and its square is the sum of a corner product and a complement product.

Over the real Hermitian algebra the same rules give the dimensions $k^{2}$, $(4-k)^{2}$ and $2k(4-k)$, summing to $16$. Against the associative Peirce decomposition the Jordan one merges the two mixed corners, and the kernel of the merge is the antisymmetric part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X\circ Y$ | $\tfrac12(XY+YX)$, the Jordan product |
| $L_E$ | Jordan multiplication by the idempotent $E$ |
| $V_1,V_\frac12,V_0$ | the three Peirce spaces |
| $k$ | the rank $\operatorname{tr}E$ |
| $\tfrac{k(k+1)}{2}$, $k(4-k)$, $\tfrac{(4-k)(5-k)}{2}$ | their complex dimensions |
| $k^{2}$, $(4-k)^{2}$, $2k(4-k)$ | their real dimensions in the Hermitian reading |

## Further Reading

- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the Peirce decomposition and the rules $V_i\circ V_j\subseteq V_{i+j}$.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (AMS, 1968), for the corner construction and the rectangular bimodule.
- [The Jordan Algebra $\operatorname{Sym}_4$](the-jordan-algebra-sym-4.html), for the product, the identity and the cone.
- [The Peirce Decomposition and the Two Halves at $n=4$](the-peirce-decomposition-and-the-two-halves-at-n-4.html), for the Hermitian reading and the trace pairing on each space.
- [The Peirce Decomposition of $\operatorname{Sym}_2$ as a Jordan Algebra](the-peirce-decomposition-of-sym-2-as-a-jordan-algebra.html), for the case of rank one at order two.
