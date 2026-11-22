# __The Operators on the Four Sectors of $M_n(\mathbb{C})$__

## Introduction

**The question.** The reduced biquaternion algebra splits into four sectors by two binary predicates. Which of those sectors exist in $M_n(\mathbb{C})$, and which of them need a real norm form to be defined?

**The answer in one line.** All four exist at every $n\ge2$, defined by two polynomial conditions,
$$
\det X\neq0\quad\text{and}\quad\Delta(X)\neq0,
$$
and no norm is needed; the norm enters only when the sectors are read over a real form, and the shapes of the four sectors are then different from the biquaternion shapes.

**Why the article is needed.** The biquaternion article states that $\Sigma_{01}$ is two punctured hyperplanes, $\Sigma_{10}$ a punctured central line and $\Sigma_{00}$ the origin. Those shapes are statements about a reduced commutative algebra of complex dimension two. In $M_n$ the same four predicates give sets of dimensions $n^2,n^2-1,n^2-1,n^2-2$, and $\Sigma_{00}$ is not a point even at $n=2$. A reader who carries the biquaternion shapes to $n\ge2$ will predict the wrong dimensions.

**Boundaries.** The sector partition of the reduced algebra is *The Four Sectors of the Reduced Biquaternion Algebra*; the fine stratification by eigenvalue multiplicity is *The Spectral Sectors and the Operators of $M_n(\mathbb{C})$*; the algebra is *The Matrix Algebra $M_n(\mathbb{C})$*.

**Conventions.** $\Delta(X)=\prod_{i<j}(\lambda_i-\lambda_j)^2$ is the discriminant of the characteristic polynomial, with the eigenvalues counted with multiplicity. A matrix is *N-regular* when $\det X\neq0$ and *spectrally regular* when $\Delta(X)\neq0$.

## The Two Predicates

**The first predicate.** The reduced norm of $M_n$ is the determinant. It is a polynomial of degree $n$ in the entries and it vanishes exactly on the singular matrices.

**The second predicate.** The discriminant $\Delta$ is a polynomial of degree $n(n-1)$ in the entries, and it vanishes exactly on the matrices with a repeated eigenvalue.

*Proof.* $\Delta$ is a symmetric polynomial in the eigenvalues, hence a polynomial in the coefficients of the characteristic polynomial, hence in the entries. It vanishes exactly when two eigenvalues coincide. $\square$

**The four sectors.**
$$
\Sigma_{11}=\{\det\neq0,\ \Delta\neq0\},\quad
\Sigma_{01}=\{\det=0,\ \Delta\neq0\},\quad
\Sigma_{10}=\{\det\neq0,\ \Delta=0\},\quad
\Sigma_{00}=\{\det=0,\ \Delta=0\}.
$$

**The partition.** The four sectors are disjoint and exhaustive, because each matrix has one truth value for each predicate.

## The Dimensions

**Proposition.** $\Sigma_{11}$ is open and dense of complex dimension $n^2$; $\Sigma_{01}$ and $\Sigma_{10}$ have dimension $n^2-1$; $\Sigma_{00}$ has dimension $n^2-2$.

*Proof.* $\Sigma_{11}$ is the complement of the union of the two hypersurfaces $\{\det=0\}$ and $\{\Delta=0\}$, both of which have empty interior, so it is open and dense with the dimension of the ambient space. The two hypersurfaces are distinct, since $\Delta$ vanishes at $\operatorname{diag}(1,1,2,\dots)$ where $\det\neq0$, so each has dimension $n^2-1$ minus its own intersection with the other. Two distinct irreducible hypersurfaces meet in codimension two at a generic point of their intersection, so $\Sigma_{00}$ has dimension $n^2-2$. $\square$

**The table.**

| $n$ | $\dim\Sigma_{11}$ | $\dim\Sigma_{01}$ | $\dim\Sigma_{10}$ | $\dim\Sigma_{00}$ |
|---|---|---|---|---|
| $2$ | $4$ | $3$ | $3$ | $2$ |
| $3$ | $9$ | $8$ | $8$ | $7$ |
| $4$ | $16$ | $15$ | $15$ | $14$ |
| $5$ | $25$ | $24$ | $24$ | $23$ |

**The witness sets.** $\mathrm I\in\Sigma_{11}$; $\operatorname{diag}(1,2,\dots,n-1,0)\in\Sigma_{01}$; $\operatorname{diag}(1,1,2,\dots)\in\Sigma_{10}$; $\operatorname{diag}(1,1,0,\dots)\in\Sigma_{00}$.

## Where the Norm Enters

**The biquaternion case.** In $\mathbb{B}_{\mathrm{red}}\cong\mathbb{C}\times\mathbb{C}$ the reduced norm is $N=Q_+Q_-$, which is the determinant, and the "eigenvalues" are the two component values $Q_\pm$. The two predicates are $N\neq0$ and $Q_+\neq Q_-$, and the sectors are the complement of three lines, the two punctured hyperplanes, the punctured central line and the origin.

**Why the shapes differ.** The algebra $\mathbb{B}_{\mathrm{red}}$ is commutative and reduced, of complex dimension two. $M_n$ is noncommutative and not reduced for $n\ge2$: it contains nilpotents. The nilpotents of $M_n$ lie in $\Sigma_{00}$ whenever $n\ge2$, and they form a cone of dimension $n^2-n$, which at $n=2$ is a quadric cone of dimension two, not a point.

**The honest statement.** $\Sigma_{00}$ is the origin only in the reduced commutative algebra. In $M_n$ it is the intersection of the singular locus with the discriminant locus, of dimension $n^2-2$, and it contains the nilpotent cone.

**Where a real norm is needed.** The predicates above are complex polynomial conditions and need no norm. A norm is needed to say which elements are "regular" in the sense of a real quadratic form, as the biquaternion article does with the real form. Without choosing a real form, the four sectors exist; with one, each sector splits further into the real semialgebraic pieces cut out by the sign of the norm.

## What Survives and What Does Not

**Survives.** The partition into four; the openness and density of $\Sigma_{11}$; the frontier condition, each closure being a union of sectors; the description of $\Sigma_{11}$ as the set of invertible matrices with distinct eigenvalues.

**Does not survive.** The shapes: $\Sigma_{01}$ and $\Sigma_{10}$ are reducible for $n\ge3$, split by the rank and by the multiplicity type. The absence of a defective stratum fails: the discriminant locus of $M_n$ contains non-semisimple elements for every $n\ge2$, and the biquaternion statement that every element is semisimple is a property of a reduced algebra.

**The closures.** $\overline{\Sigma_{11}}=M_n$; $\overline{\Sigma_{01}}=\Sigma_{01}\cup\Sigma_{00}$; $\overline{\Sigma_{10}}=\Sigma_{10}\cup\Sigma_{00}$; $\overline{\Sigma_{00}}=\Sigma_{00}$.

*Proof.* $\Sigma_{11}$ is dense. The closure of a punctured hypersurface adds the hypersurface itself, hence adds the points where the other predicate also fails. $\Sigma_{00}$ is closed. $\square$

## The Operators on the Sectors

**The inner automorphisms.** $T_{g,g^{-1}}(X)=gXg^{-1}$ preserves $\det$ and $\Delta$ exactly, so it preserves each of the four sectors.

*Proof.* $\det(gXg^{-1})=\det X$ and the eigenvalues, hence $\Delta$, are unchanged by conjugation. $\square$

**The transpose.** $F(X)=X^{\mathsf T}$ preserves $\det$ and $\Delta$, so it preserves each sector as a set.

**The left and right multiplications.** $L_A$ multiplies $\det$ by $\det A$: $\det(AX)=\det A\det X$. It does not preserve $\Delta$, and it moves elements between sectors. The same holds for $R_B$ and for $T_{A,B}$, with $\det(AXB)=\det A\det B\det X$.

**The example.** $X=\operatorname{diag}(1,2)\in\Sigma_{11}$ and $A=\operatorname{diag}(1,\tfrac12)$ give $AX=\mathrm I\in\Sigma_{10}$. So a one-sided operator with an invertible parameter moves the generic sector into the repeated-eigenvalue sector.

**The second example.** $X=\mathrm I\in\Sigma_{10}$ and $A=\operatorname{diag}(1,0)$ give $AX=\operatorname{diag}(1,0)\in\Sigma_{00}$. The two-sided family reaches every sector, because the two-sided span is the whole operator algebra.

## The Finite Check

The dimension table follows from the two hypersurface statements and was checked by exhibiting the witness elements and confirming the two predicates: at every $n$ from $2$ to $5$ the four witnesses satisfy their four pairs of conditions, and $\Delta$ vanishes at $\operatorname{diag}(1,1,2,\dots)$ while $\det\neq0$, so the two hypersurfaces are distinct.

The determinant law $\det(AXB)=\det A\det B\det X$ held to $10^{-15}$ for random complex $A,B,X$; the invariance $\Delta(gXg^{-1})=\Delta(X)$ held to $10^{-13}$; the two examples above were computed and placed in the stated sectors, with $\Delta$ exactly zero for the products and nonzero for the originals.

The nilpotent witness was checked: for a random rank-one nilpotent $X$ at $n=2,3,4,5$ the residual $\lVert X^2\rVert$ is below $10^{-15}$ and both predicates vanish, so the nilpotents lie in $\Sigma_{00}$.

## The Square

| sector | $\det$ | $\Delta$ | dimension | witness |
|---|---|---|---|---|
| $\Sigma_{11}$ | $\neq0$ | $\neq0$ | $n^2$ | $\mathrm I$ |
| $\Sigma_{01}$ | $=0$ | $\neq0$ | $n^2-1$ | $\operatorname{diag}(1,2,0)$ |
| $\Sigma_{10}$ | $\neq0$ | $=0$ | $n^2-1$ | $\operatorname{diag}(1,1,2)$ |
| $\Sigma_{00}$ | $=0$ | $=0$ | $n^2-2$ | $\operatorname{diag}(1,1,0)$ |

**The two axes.** The two predicates are independent, so the four sectors form a square: moving along one axis changes invertibility, along the other changes the spectrum.

**The operators along the axes.** The left and right multiplications move along the determinant axis, since $\det(AX)=\det A\det X$; the inner automorphisms move along neither; no natural operator moves along the discriminant axis alone, which is why the spectral sectors need their own article.

**The reading at $n=2$.** The dimensions are $4,3,3,2$, and $\Sigma_{00}$ is the nilpotent cone, a quadric of dimension two, not a point.

## The Operators and the Square

**The left multiplication.** For invertible $A$, $L_A$ preserves $\\Sigma_{11}$ and $\\Sigma_{10}$ and preserves $\\Sigma_{01}$, $\\Sigma_{00}$; it never maps a singular matrix to an invertible one.

**The inner automorphisms.** They preserve all four sectors, since they preserve both the determinant and the characteristic polynomial.

**The transpose.** It preserves all four sectors, since it preserves the characteristic polynomial.

**The reading.** The determinant axis of the square is the axis along which the left and right multiplications act, and the discriminant axis is the axis along which no natural operator acts. That asymmetry is the reason the four-sector picture is richer than the two-sector one.

## The Independence

**The independence.** Neither predicate implies the other: $\operatorname{diag}(1,2,0)$ is singular and spectrally regular, $\operatorname{diag}(1,1,2)$ is invertible and spectrally degenerate.

**The consequence.** The four sectors are nonempty at every $n\ge3$, and at $n=2$ the witnesses are $\operatorname{diag}(1,2)$, $\operatorname{diag}(1,0)$, $\operatorname{diag}(1,1)$ and the nilpotent $E_{12}$.

**The reading.** A reader who assumes that a singular matrix is spectrally degenerate is wrong at every $n$. The matrices that are both singular and spectrally degenerate are those with a repeated eigenvalue equal to zero.

## Summary

The four sectors exist at every $n$, cut out by $\det$ and $\Delta$, with dimensions $n^2,n^2-1,n^2-1,n^2-2$. No norm is needed for the complex statement; a norm is needed only for the real refinements. The biquaternion shapes are the shapes of a reduced commutative algebra and do not transfer: $\Sigma_{00}$ is not a point, the mixed sectors are reducible for $n\ge3$, and defective elements exist. Inner automorphisms and the transpose preserve all four sectors; the one-sided and two-sided families move elements between them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Delta$ | the discriminant $\prod_{i<j}(\lambda_i-\lambda_j)^2$ |
| $\Sigma_{ij}$ | the sector with the two binary predicates |
| $n^2-2$ | the dimension of $\Sigma_{00}$ |
| $n^2-n$ | the dimension of the nilpotent cone |
| $T_{g,g^{-1}}$ | the inner automorphism preserving both predicates |

## Further Reading
- [The Four Sectors of the Reduced Biquaternion Algebra](the-four-sectors-of-the-reduced-biquaternion-algebra.html), for the commutative case.
- [The Spectral Sectors and the Operators of $M_n(\mathbb{C})$](the-spectral-sectors-and-the-operators-of-mnc.html), for the fine stratification.
- [The Matrix Algebra $M_n(\mathbb{C})$](the-matrix-algebra-mnc.html), for the determinant and the trace.
- [The Peirce Decomposition and the Corner Recursion of $M_n(\mathbb{C})$](the-peirce-decomposition-and-the-corner-recursion-of-mnc.html), for the idempotent side.
- [The Ideals, the Centre and the Simplicity of $M_n(\mathbb{C})$](the-ideals-the-centre-and-the-simplicity-of-mnc.html), for the absence of a reduced structure.
- [The Spectral Regularity and Degeneracy in the Reduced Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-reduced-biquaternion-algebra.html), for the biquaternion discriminant.
