# __Nilpotents of the Symmetric Quaternionic Algebra__

## Introduction

The powers of the block are governed by one formula: from the square on, every power is a multiple of $e_0$, $\tilde x^{\star k}=N(\tilde x)x_0^{k-2}e_0$. The formula makes a vanishing power an elementary event. The cube vanishes exactly on the pure elements, the non-vanishing coefficient and the definiteness of $N$ prevent any higher vanishing, and the square vanishes only at the origin. Over $\mathbb{R}$ the block therefore has nonzero nilpotents — the pure quaternions — each of index exactly three, and its square-zero set is the single point $\{0\}$. The three classes of element that the block separates are as far apart as its definite coefficient allows: the nilpotent set is the punctured vector subspace $\operatorname{Im}\mathbb{H}\setminus\{0\}$, the square-zero set is the origin, and the zero-divisor set is the whole punctured space. This article proves the power formula, decides the index, isolates the square-zero set, and reads the three classes against each other.

**Boundaries.** The definitions of a nilpotent, a square-zero element and the index of nilpotency are *Definitions for the Study of the 6 Algebraic Structures*; the product and its scalar law are *Introduction to the Symmetric Quaternionic Algebra of Quaternions*; the diagonal and the non-isotropic class are *Norm and Invertibility in the Symmetric Quaternionic Algebra*; the radicand zero and the level sets of the diagonal are *Square Roots of a General Element in the Symmetric Quaternionic Algebra*; the zero divisors are *Zero Divisors of the Symmetric Quaternionic Algebra*; the idempotents are *Idempotents of the Symmetric Quaternionic Algebra*; the radical and the isotropic elements are *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*; the class is also collected in *The Specificities of the Symmetric Quaternionic Algebra*.

**Conventions.** The algebra is $\mathbb{H}$ over $\mathbb{R}$ with basis $e_0=1,e_1,e_2,e_3$ and $e_1e_2=e_3$; an element is $\tilde x=x_0e_0+\mathbf x$. The **quaternion conjugation** is $\tilde x^{\natural}=x_0e_0-\mathbf x$; the bar is the identity, the star coincides with the natural sign ${}^{\natural}$. The **quaternion form** is $N(\tilde p,\tilde q)=p_0q_0+\mathbf p\cdot\mathbf q$, its diagonal is $N(\tilde x)=x_0^{2}+|\mathbf x|^{2}$, and the **symmetric quaternionic product** is $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0$. The centre is $\mathbb{R}e_0$ and the vector subspace is $\mathrm{Vect}(\mathbb{H})=\operatorname{Im}\mathbb{H}=\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3$. The **powers** are left-nested, $\tilde x^{\star1}=\tilde x$ and $\tilde x^{\star(k+1)}=\tilde x^{\star k}\star\tilde x$; the block is commutative, so the nesting is immaterial.

## The General Definition

**Definition (nilpotent, square-zero, index).** A **nilpotent** of the block is a **nonzero** element $\tilde x$ with $\tilde x^{\star k}=0$ for some $k\geq1$; the least such $k$ is the **index of nilpotency**. The case $k=2$, $\tilde x\star\tilde x=0$, is a **square-zero** element, and the case $k=3$, $\tilde x\star\tilde x\star\tilde x=0$, a **cube-zero** element. The origin satisfies every power-zero equation, but it is excluded by the definition, which requires a nonzero element; the origin is the only square-zero element of several blocks and is nevertheless not a nilpotent of any of them.

The vocabulary is quoted from *Definitions for the Study of the 6 Algebraic Structures*, and the article reads it on the block.

## The Powers of an Element

**Theorem (the powers).** For every $\tilde x$ and every $k\geq2$,

$$
\tilde x^{\star k}=N(\tilde x)\,x_0^{\,k-2}\,e_0 .
$$

*Proof.* For $k=2$ this is the square, $\tilde x\star\tilde x=N(\tilde x)e_0$. The induction step uses $\tilde x^{\star k}\star\tilde x=N(\tilde x)x_0^{k-2}e_0\star\tilde x=N(\tilde x)x_0^{k-2}(x_0e_0)=N(\tilde x)x_0^{k-1}e_0$, where the middle equality is $e_0\star\tilde x=x_0e_0$; the formula at $k+1$ follows.

**Corollary (all powers from the square on are central).** From the second power on, every power of an element is a real multiple of $e_0$: the square is $N(\tilde x)e_0$, the cube is $N(\tilde x)x_0e_0$, and every higher power is $N(\tilde x)x_0^{k-2}e_0$. The vector part of the element disappears at the first power and never returns.

## The Criterion and the Index

**Theorem (the nilpotents are the pure elements).** An element $\tilde x$ is a nilpotent of the block if and only if it is nonzero and pure,

$$
\tilde x\ \text{nilpotent}\iff \mathbf x\neq0\ \text{and}\ x_0=0,
$$

that is, if and only if $\tilde x\in\operatorname{Im}\mathbb{H}\setminus\{0\}$. Every nonzero pure element has index exactly three.

*Proof.* By the power formula the cube is $\tilde x^{\star3}=N(\tilde x)x_0e_0$. If $x_0=0$ the cube vanishes, so the index is at most three. If $x_0\neq0$, then $N(\tilde x)=x_0^{2}+|\mathbf x|^{2}\geq x_0^{2}>0$, so $N(\tilde x)x_0\neq0$ and the cube is nonzero; by the formula $N(\tilde x)x_0^{k-2}\neq0$ for every $k\geq2$, so no power vanishes and $\tilde x$ is not nilpotent. Hence a nilpotent has $x_0=0$. Conversely a nonzero pure element has $N(\tilde x)=|\mathbf x|^{2}>0$, so its square is $N(\tilde x)e_0\neq0$ and its cube is $0$: its index is exactly three, and not two.

**Corollary (the nilpotent set).** The nilpotent set of the block is the punctured vector subspace

$$
\{\text{nilpotents}\}=\{\tilde x:x_0=0,\ \tilde x\neq0\}=\operatorname{Im}\mathbb{H}\setminus\{0\},
$$

whose closure is the vector subspace $\operatorname{Im}\mathbb{H}=\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3$ of real dimension three. There is no nonzero element of index two, and the index is bounded by three.

*Proof.* The criterion gives the set and the index; an index-two nilpotent would be a nonzero element with a vanishing square, which the next section shows impossible.

**Corollary (the vanishing powers).** For an element with $x_0\neq0$ no power vanishes. For a nonzero pure element the powers are $\tilde x,\ N(\tilde x)e_0,\ 0,\ 0,\dots$, so the cube is the only vanishing power. The only vanishing power of any element other than the origin is the cube of a nonzero pure element.

*Proof.* The power formula gives $N(\tilde x)x_0^{k-2}e_0$; the coefficient vanishes exactly when $N(\tilde x)=0$, that is at $\tilde x=0$, or when $k\geq3$ and $x_0=0$.

## The Square-Zero Elements

**Theorem (the square-zero set is the origin).** An element has a vanishing square only at the origin,

$$
\{\tilde x:\tilde x\star\tilde x=0\}=\{0\}.
$$

There is no nonzero square-zero element, hence no nilpotent of index two.

*Proof.* The square is $N(\tilde x)e_0$, and $N(\tilde x)=x_0^{2}+|\mathbf x|^{2}$ is a sum of four squares, which vanishes exactly when every coordinate of $\tilde x$ vanishes. The origin has the vanishing square, and it is the only element that does.

**Corollary (the two classes).** The square-zero set is the singleton $\{0\}$ and the nilpotent set is $\operatorname{Im}\mathbb{H}\setminus\{0\}$; the nilpotents of index two are none, and the nilpotents of index three are the nonzero pure elements. The block is thus a product with a nontrivial nilpotent family and a trivial square-zero set, and the two notions are pulled apart by the definiteness of the coefficient.

## The Relation to the Zero Divisors and to the Idempotents

**Proposition (against the zero divisors).** Every nilpotent is a zero divisor, since every nonzero element of the block is a zero divisor (*Zero Divisors of the Symmetric Quaternionic Algebra*); but the nilpotent set is strictly smaller than the zero-divisor set. The element $e_0$ is a zero divisor, $e_0\star e_1=0$ with $e_1\neq0$, and it is not a nilpotent, its powers being $e_0$ at every index. So

$$
\operatorname{Im}\mathbb{H}\setminus\{0\}\subsetneq\mathbb{H}\setminus\{0\},
$$

the inclusion being strict at $e_0$.

*Proof.* The nilpotents are the nonzero pure elements, a vector subspace minus its origin; the zero divisors are all the nonzero elements; $e_0$ is nonzero, central, hence not pure, and it is a zero divisor by the displayed annihilation. The zero-divisor set is computed in *Zero Divisors of the Symmetric Quaternionic Algebra*.

**Proposition (against the idempotents).** The idempotents of the block are $0$ and $e_0$, the nilpotents are the nonzero pure elements, and the two sets are disjoint. The idempotent $e_0$ is not a nilpotent, and a nonzero pure element is not an idempotent, its square $N(\tilde x)e_0$ being central while the element is not. The origin is the only element at which the two defining equations $\tilde x\star\tilde x=\tilde x$ and $\tilde x\star\tilde x=0$ hold together, and it is excluded from the nilpotent class by the definition.

*Proof.* The idempotents are classified in *Idempotents of the Symmetric Quaternionic Algebra*; the intersection of the two sets is empty because a pure element is not central unless it is $0$, and $0$ is an idempotent but is excluded from the nilpotents by the definition; the equations together give $\tilde x=0$.

**Remark (the meeting of the three classes).** The idempotent set $\{0,e_0\}$, the nilpotent set $\operatorname{Im}\mathbb{H}\setminus\{0\}$ and the square-zero set $\{0\}$ overlap only at the origin: the idempotents and the nilpotents meet nowhere, the square-zero element is the origin, and the origin is the only point common to the idempotent set, the square-zero set and the closure $\operatorname{Im}\mathbb{H}$ of the nilpotent set. This is the element-theoretic content of the absence of a unit and of the definiteness of the coefficient.

## The Conjugation

**Proposition (the single conjugation preserves the class).** Over $\mathbb{R}$ the natural conjugation ${}^{\natural}$ is the only nontrivial conjugation, the star coincides with it and the bar is the identity. The natural conjugation preserves $x_0$ and $N$, hence preserves the nilpotent set and the index: $\tilde x$ is a nilpotent of index $k$ if and only if $\tilde x^{\natural}$ is. The complex chapter's invariance group of conjugations collapses here to the invariance under the single natural sign.

*Proof.* The natural conjugation reverses the vector part and fixes the scalar part, so $N(\tilde x^{\natural})=N(\tilde x)$ and the power formula is unchanged; the collapse of the conjugations is the convention of the real chapter.

## The Matrix Model

**Proposition (the nilpotents in the $2\times2$ model).** In the realization $\mathsf{M}_2$ of *The Symmetric Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* the quaternion $\tilde x$ has the matrix with $\operatorname{Tr}\mathsf{M}_2(\tilde x)=2x_0$ and $\det\mathsf{M}_2(\tilde x)=N(\tilde x)$. Therefore the nilpotents of the block are exactly the matrices of the model that are trace-free, that is the images of the pure elements; a nonzero pure element has a trace-free matrix of determinant $N(\tilde x)>0$ and is a nilpotent of index three; and the square-zero elements are the trace-free matrices that are also singular, which over $\mathbb{R}$ reduces to the zero matrix, because a nonzero pure element has $N(\tilde x)>0$ and a singular matrix of the model has $N(\tilde x)=0$, hence is the image of the origin.

*Proof.* The trace and the determinant are the invariants of the model; a pure element has $x_0=0$, hence a trace-free matrix, and $\det=N(\tilde x)=|\mathbf x|^{2}>0$ for a nonzero pure element, so the matrix is not singular; a singular matrix of the model has $\det=N(\tilde x)=0$, hence $\tilde x=0$ by definiteness. The criteria of the two preceding sections give the index.

**Remark (the contrast with the complex parent).** In the biquaternion chapter the same model gives the nilpotents as the matrices that are trace-free or singular, the singular ones being square-zero, of index two, and the trace-free non-singular ones of index three. Over $\mathbb{R}$ the singular branch collapses: the determinant $N(\tilde x)$ is definite, the singular matrices of the model reduce to the zero matrix, and only the trace-free branch survives.

## The Comparison with the Other Real Blocks

**Remark (the four square-zero sets).** The square-zero set is $\{0\}$ for the four structures of the real chapter whose coefficient is definite or whose product is a division product — the general and symmetric plain and the general and symmetric quaternionic — and it is the whole space for the two antisymmetric structures, whose squares vanish identically and whose nilpotent class is therefore the whole space apart from the origin (*Definitions for the Study of the 6 Algebraic Structures*; *Nilpotents of the General Plain Algebra*; *Nilpotents of the Symmetric Plain Algebra*). Within the four, the symmetric quaternionic block is distinguished by its nilpotent class: it is the one of the four with a nonzero nilpotent family, the pure quaternions of index three, the other three having no nonzero nilpotent. The distinction between a nilpotent and a square-zero element is therefore visible in this block and invisible in the other three: here the cube, and not the square, is what vanishes.

## Summary

The powers of the symmetric quaternionic block obey $\tilde x^{\star k}=N(\tilde x)x_0^{k-2}e_0$ from the square on, so the cube vanishes exactly on the pure elements and no higher power vanishes off the origin. The nilpotents are the nonzero pure quaternions, $\operatorname{Im}\mathbb{H}\setminus\{0\}$, each of index exactly three; there is no nilpotent of index two and none of index greater than three. The square-zero set is the single point $\{0\}$, because the coefficient $N(\tilde x)=x_0^{2}+|\mathbf x|^{2}$ is definite and vanishes only at the origin. The nilpotent set is strictly contained in the zero-divisor set, the strictness witnessed by $e_0$, which annihilates $e_1$ and has no vanishing power; the nilpotents and the idempotents are disjoint, and the origin is the only element at which the defining equations of all three classes of element come together. In the $2\times2$ model the nilpotents are the trace-free matrices, and the singular matrices of the model reduce to zero; over $\mathbb{R}$ the singular branch of the complex chapter collapses, and the trace-free branch alone survives.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde x^{\star k}=N(\tilde x)x_0^{k-2}e_0$, $k\geq2$ | the powers of the block |
| nilpotent | nonzero $\tilde x$ with $\tilde x^{\star k}=0$; here the nonzero pure elements |
| $\operatorname{Im}\mathbb{H}\setminus\{0\}$ | the nilpotent set, the pure quaternions |
| index three | the index of every nonzero pure element |
| $\{\tilde x:\tilde x\star\tilde x=0\}=\{0\}$ | the square-zero set |
| $x_0\neq0$ | no vanishing power |
| $\operatorname{Tr}\mathsf{M}_2=2x_0$, $\det\mathsf{M}_2=N(\tilde x)$ | the matrix invariants; nilpotent $\iff$ trace-free |

## Further Reading

- *Definitions for the Study of the 6 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-6-algebraic-structures.md`), for the nilpotent, the square-zero element and the index of nilpotency
- *Norm and Invertibility in the Symmetric Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the definite norm whose vanishing decides the square-zero set
- *Square Roots of a General Element in the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the level sets of the diagonal and the radicand zero
- *Zero Divisors of the Symmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the maximal zero-divisor set that contains the nilpotent set strictly
- *The Specificities of the Symmetric Quaternionic Algebra* (`articles_maths/the-specificities-of-the-symmetric-quaternionic-algebra-of-quaternions.md`), where the powers and the nilpotent class are collected
- *The Symmetric Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-symmetric-quaternionic-algebra-in-the-2x2-matrix-element-representation-of-quaternions.md`), for the realization $\mathsf{M}_2$, its trace and its determinant, and the reading of the block on it
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for nilpotents, the index of nilpotency and the trace-free matrices.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the quaternion matrices, their trace and their determinant.
