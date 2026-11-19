# __The Isomorphisms and Their Dimensions__

## Introduction

Four statements are needed before any physics of this block can be written, and they are four because they count dimensions differently. The biquaternion algebra is a complex algebra isomorphic to the $2\times2$ complex matrices. Its scalar-free part, read under the commutator, is a real Lie algebra of dimension six, and that algebra is the Lorentz algebra. The whole algebra under the commutator is a larger real Lie algebra, and it is not a Lorentz algebra. The complexification of the Lorentz algebra is a six-dimensional complex algebra that splits into two copies of the three-dimensional complex algebra of traceless matrices.

These are not four ways of saying one thing. They are four different objects with four different dimensions, and every error in this neighbourhood comes from running them into a single chain. This article keeps them apart, gives the dimension of each, and states which convention the block uses where a convention has to be chosen.

The article assumes the base of *Algebra and Element Conventions* and the $2\times2$ isomorphism of *Matrix Representations Conventions*, §*The $2\times2$ Pauli Representation*. It proves the four statements, it verifies the one that needs a computation, and it says what no statement depends on.

## Three Kinds of Structure on One Vector Space

### The Vector Space

The biquaternion algebra is the real vector space $\mathbb{B}$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, given the multiplication of the quaternions and the central scalar $i$. As a complex vector space it has the four basis elements $e_t,\vec e_x,\vec e_y,\vec e_z$, and the scalar $i$ is a complex number, not a fifth basis element. So

$$
\dim_{\mathbb{C}}\mathbb{B}=4,\qquad \dim_{\mathbb{R}}\mathbb{B}=8 .
$$

The two numbers are both correct and they describe the same set. A basis over $\mathbb{R}$ is $e_t,\vec e_x,\vec e_y,\vec e_z,ie_t,i\vec e_x,i\vec e_y,i\vec e_z$, eight elements.

### The Three Structures

On that one vector space three structures are defined, and only the first is an algebra in the sense of a bilinear product.

| structure | the operation | what it is |
|---|---|---|
| associative algebra | the biquaternion product $\tilde Q\tilde P$ | $\mathbb{B}$ itself |
| Lie algebra | the commutator $[\tilde Q,\tilde P]=\tilde Q\tilde P-\tilde P\tilde Q$ on all of $\mathbb{B}$ | $\mathfrak{gl}(2,\mathbb{C})$ read as a real Lie algebra |
| Lie algebra | the same commutator restricted to the scalar-free part | $\mathfrak{so}(1,3)$ |

The word *algebra* in this block therefore always needs its adjective. The associative algebra is where the rotors live. The two Lie algebras are where the generators live, and only the second of them is the Lorentz algebra.

## The Associative Isomorphism

### The Statement

$$
\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\;\cong\;M_2(\mathbb{C}),
$$

as associative algebras over $\mathbb{C}$, and the isomorphism is written $\mathsf{M}_2$ in this block.

The tensor product is the precise form of a claim that is easy to say loosely: a biquaternion is a quaternion with complex coefficients, and a quaternion is a real four-dimensional algebra. Tensoring the quaternions with the complex numbers over the reals gives a complex four-dimensional algebra, and a complex four-dimensional algebra that is simple and central is a matrix algebra.

### The Map

The isomorphism is written here once, because every entry of this block uses it. In the basis above,

$$
\mathsf{M}_2(\tilde Q)=
\begin{pmatrix}
Q_t-iQ_z & -iQ_x-Q_y\\
-iQ_x+Q_y & Q_t+iQ_z
\end{pmatrix},
$$

and the four unit images are read off by setting one coefficient to one:

$$
\mathsf{M}_2(e_t)=I_2,\qquad
\mathsf{M}_2(\vec e_x)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\qquad
\mathsf{M}_2(\vec e_y)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
\mathsf{M}_2(\vec e_z)=\begin{pmatrix}-i&0\\0&i\end{pmatrix}.
$$

Each of the three vector images squares to $-I_2$, which is what $\vec e_\eta^2=-e_t$ demands, and the three satisfy the quaternion relations among themselves. The three are $-i$ times the Pauli matrices of *Matrix Representations Conventions*, §*The $2\times2$ Pauli Representation*; this block does not print those arrays, and the three matrices above are the display of record.

### Why the Assignment Is Forced

The assignment of the three vector images is not a choice among equally good alternatives.

- $\vec e_\eta^2=-e_t$ forces the factor, because a real symmetric matrix squares to $+I_2$ and only an imaginary one squares to $-I_2$.
- $\vec e_x\vec e_y=\vec e_z$ fixes the relative sign of the three.
- The trace must vanish on vectors, and the three Pauli matrices, though traceless, are Hermitian, so a Hermitian image would put a real number where the algebra has $i$.

A reviewer must not "correct" the assignment by making the three images real, and must not negate all three. The first destroys the sector dictionary, and the second destroys the multiplication.

### What the Isomorphism Is Not

It is an isomorphism of associative algebras, and it also carries the corpus's involution ${}^{*}$: the star of an element is the conjugate transpose of its image, $\mathsf{M}_2(\tilde Q^{*})=\mathsf{M}_2(\tilde Q)^{\dagger}$. Conjugating the entries on their own is a different operation and is no involution of the algebra: it negates the images of $\vec e_x$ and $\vec e_z$ and leaves $\mathsf{M}_2(\vec e_y)$, whose array is real, untouched, so it maps no element to an element. The remaining conjugations $\natural$, $\bar{\phantom{Q}}$ and ${}^{\flat}$ are carried by explicit formulas, which *Element and Operator Representations: The Three Actions* records and this block uses.

The isomorphism is also not an isometry of the two quadratic forms that live on the two sides. On the algebra side the form is the biquaternion norm $N$. On the matrix side it is the determinant. Those two agree, which is the next statement, but neither is the Minkowski interval; that distinction is the subject of *The 2×2 Matrix Model: What It Computes and What It Cannot Show*.

### The Determinant Is the Norm

$$
\det\mathsf{M}_2(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}=N(\tilde Q).
$$

The identity is checked by multiplying the two diagonal entries, and it is the reason the numerical practice of this block runs through matrices: the algebra's quadratic form, its invertibility criterion, its group of invertibles and its unit-norm group are all read from one determinant. Checking it on a hundred random elements gives agreement to machine precision, better than $10^{-14}$.

The form $N$ is **complex**. On the element $e_t+i\vec e_x$ it takes the value $1+i^{2}=0$, and on $e_t+\vec e_x$ it takes the value $2$, while the Minkowski interval of the corresponding four-vector is $1-1=0$ in the second case. The two forms are different functions, and they agree only on the slice named in the next article.

## The Traceless Part Under the Commutator

### The Subspace

$$
\mathfrak{sl}(2,\mathbb{C})=\{\tilde X\in\mathbb{B}:\operatorname{Tr}\mathsf{M}_2(\tilde X)=0\}.
$$

Since $\operatorname{Tr}\mathsf{M}_2(\tilde Q)=2Q_t$, the traceless part is the set of elements with vanishing scalar part, that is the pure biquaternions. As a complex vector space it is spanned by $\vec e_x,\vec e_y,\vec e_z$, so

$$
\dim_{\mathbb{C}}\mathfrak{sl}(2,\mathbb{C})=3,\qquad \dim_{\mathbb{R}}\mathfrak{sl}(2,\mathbb{C})=6 .
$$

The second number is the one this block needs: six is the number of Lorentz generators, three rotations and three boosts.

### Closure and the Table

The traceless part is closed under the commutator, because the trace of a commutator vanishes in any associative algebra. Its six real generators are

$$
J_\eta=\tfrac12\vec e_\eta,\qquad K_\eta=\tfrac12 i\vec e_\eta,\qquad \eta=x,y,z,
$$

and direct multiplication gives

$$
[J_i,J_j]=\epsilon_{ijk}J_k,\qquad [J_i,K_j]=\epsilon_{ijk}K_k,\qquad [K_i,K_j]=-\epsilon_{ijk}J_k .
$$

The table is the Lorentz algebra. *The Six Generators and Their Commutators* derives it in full, writes the structure constants in the form the block uses and computes the invariant form; here the table is needed only to identify the object.

### Why This Is the Lorentz Algebra

Two independent warrants.

**The dimension and the bracket.** Six generators with the bracket above are $\mathfrak{so}(1,3)$: the three $J$ close as a rotation algebra, and the three $K$ transform as a vector under it, which is exactly the action of rotations on the boost generators of the Lorentz group.

**The invariant form.** The Killing form of the six-dimensional real algebra has eigenvalues $\pm4$ in the basis above and determinant $-4096$. It is therefore non-degenerate with inertia $(3,3)$, which is the inertia of $\\mathfrak{so}(1,3)$ and of nothing else in this neighbourhood: $\mathfrak{so}(4)$ has inertia $(6,0)$ and $\mathfrak{so}(2,2)$ has $(4,2)$. The computation runs on the structure constants, and it is the check that rules out the misreading in which the traceless part is called $\mathfrak{so}(4)$.

**The misreading to avoid.** The table has $[K_i,K_j]=-\epsilon_{ijk}J_k$ and not $+\epsilon_{ijk}J_k$. A plus sign gives $\mathfrak{so}(4)$, the Euclidean algebra, which is the algebra of a different real form of the same complex algebra. *The Cartan Subalgebra, the Roots and the Three Real Forms* puts the three real forms side by side and states which slice of the complex algebra each one is.

### The Generators Are Anti-Hermitian

With the corpus's involution $\vec e_\eta^{*}=-\vec e_\eta$ and $i^{*}=-i$. Hence

$$
J_\eta^{*}=-J_\eta,\qquad K_\eta^{*}=K_\eta .
$$

The rotations are anti-Hermitian and the boosts are Hermitian in this convention. This is a convention of the generator and not a statement about the group. Its consequences are that the structure constants above are real, that no explicit factor of $i$ appears in the bracket table, and that a Casimir written with the corpus's generators may differ in sign from the same Casimir written with the physicist's Hermitian generators $i\vec J$ and $i\vec K$. *The Two Casimirs of the Lorentz Algebra* states both forms and the dictionary between them.

## The Whole Algebra Under the Bracket

### The Statement for $\mathfrak{gl}(2,\mathbb{C})$

$$
\mathbb{B}\ \text{under }[-,-]\;\cong\;\mathfrak{gl}(2,\mathbb{C})\ \text{as a real Lie algebra},\qquad \dim_{\mathbb{R}}=8 .
$$

### The Decomposition

The scalar part is central: $[e_t,\tilde X]=0$ and $[ie_t,\tilde X]=0$ for every $\tilde X$. So the algebra splits as a direct sum of Lie algebras,

$$
\mathfrak{gl}(2,\mathbb{C})=\mathfrak{sl}(2,\mathbb{C})\oplus\mathbb{C}\,e_t,
$$

with the second summand of real dimension two, spanned by $e_t$ and $ie_t$, and abelian. The traceless part is the Lorentz algebra of the previous section; the centre is not.

### Why It Is Not a Lorentz Algebra

Three reasons, each sufficient.

- **Dimension.** Eight against six. A Lie algebra isomorphism preserves the dimension of the underlying real vector space.
- **Centre.** The centre is two-dimensional and nontrivial. The Lorentz algebra is semisimple, so its centre is zero.
- **The invariant form.** The Killing form of the eight-dimensional algebra is degenerate, with the two central directions in its radical, while the Lorentz algebra's form is non-degenerate.

The statement matters because the adjoint action of the group on the algebra is an eight-dimensional representation, and a computation that reads it as a Lorentz representation of dimension eight gets the wrong decomposition. The correct reading is the six-dimensional adjoint plus two trivial directions, which is what *The Two Commuting Complex Triples* uses.

### What the Centre Does Physically

The two central directions are the scale and the phase of a biquaternion, $r$ and $e^{i\theta_{\mathrm{pha}}}$. Neither is a Lorentz transformation. They are the two factors that must be divided out before a biquaternion is a frame change, which is why *The Cartan Decomposition: Every Lorentz Transformation as a Boost and a Rotation* removes them first and only then splits.

## The Complexification

### The Statement for the Complexification

$$
\mathfrak{so}(1,3)_{\mathbb{C}}\;\cong\;\mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C}),
$$

as complex Lie algebras, of complex dimension six and real dimension twelve.

### Reading the Symbols

This is the statement most often written wrongly, because the same letters appear on both sides with different meanings. The two meanings are:

| symbol | as written | complex dimension | real dimension |
|---|---|---|---|
| $\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}$ | the traceless part as a **real** Lie algebra | — | $6$ |
| $\mathfrak{sl}(2,\mathbb{C})$ | the traceless part as a **complex** Lie algebra | $3$ | $6$ |
| $\mathfrak{so}(1,3)_{\mathbb{C}}$ | the complexification of the real Lorentz algebra | $6$ | $12$ |

The identity $\mathfrak{so}(1,3)\cong\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}$ is an isomorphism of **real** Lie algebras. The identity $\mathfrak{so}(1,3)_{\mathbb{C}}\cong\mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C})$ is an isomorphism of **complex** Lie algebras, and its two summands are two copies of the three-dimensional complex algebra. The subscript decides which statement is meant, and a sentence that drops the subscript is a sentence that cannot be checked.

Why the complexification doubles: the traceless part is already a complex vector space, and complexifying a complex Lie algebra regarded as real gives two copies, one for $+i$ and one for $-i$. The two copies are the self-dual and the anti-self-dual bivectors.

### What the Summands Are

Every traceless element splits into a self-dual and an anti-self-dual part under the Hodge star on bivectors. On the algebra side the split is written by the two triples

$$
\vec J_{\pm}=\tfrac12\bigl(\vec J\pm i\vec K\bigr),
$$

and each triple closes as a complex rotation algebra while commuting with the other. *The Two Commuting Complex Triples* proves the closure and the commutation, and warns that the two triples are not the real $\mathfrak{su}(2)$ inside $\mathfrak{so}(1,3)$.

### Why the Representation Theory Lives Here

An irreducible finite-dimensional representation of the complexified algebra is a tensor product of one representation of the first summand with one of the second, and each summand's irreducible representations are labelled by a half-integer. The label is therefore a pair $(m,n)$, and that pair is the whole classification. *The Finite-Dimensional Representations and Their Unitarity Defect* gives the dimensions and the tensor products; *The Two Casimirs of the Lorentz Algebra* gives the two numbers that name the pair.

The summands are also what the two chiralities mean. The first summand's fundamental representation is $(\tfrac12,0)$ and the second's is $(0,\tfrac12)$, and those two are the two Weyl spinors. The pair $(m,n)$ is not a pair of spins of one object; it is one label for each of the two independent complex algebras.

## Why No Physical Prediction Depends on the Pauli Convention

### The Convention

The convention is the one printed above: which of the three vector images carries which sign, and the overall factor $-i$. It is fixed by the algebra and by the requirement that the sector dictionary survives, so within this corpus there is no freedom left. Between this corpus and another book there is freedom, and the article must say why it does not matter.

### The Argument

A physical prediction is a number computed from a frame transformation and a physical object. Three transformations of the bookkeeping leave every such number unchanged.

- **Relabelling the three axes.** A rotation of the names $x,y,z$ permutes the three images and the three Pauli matrices with them. The multiplication table is preserved up to the same permutation, and no scalar invariant sees it.
- **An overall unitary change of the module.** Conjugating every image by one fixed unitary matrix $S$ gives another isomorphism $\mathsf{M}_{2,\mathrm{S}}=S\mathsf{M}_2S^{-1}$, with the same determinant, the same trace and the same bracket. Only the entries change, and no entry is physical.
- **The sign of $i$.** Sending $i\to-i$ sends the algebra to its opposite, replaces $\mathsf{M}_2(\tilde Q)$ by its transpose and reverses the sign of every commutator. That would change the bracket table, so this one is **not** free: the corpus fixes the sign of $i$ once, in *Algebra and Element Conventions*, and every article inherits it.

So the convention is a choice of coordinates on a space of representations, and physical predictions are invariant under the choices that remain. What is not invariant is the bracket table, and the table is what the next articles compute.

## Summary

The four statements, with their dimensions, in the order in which a reader needs them:

| statement | the object | dimension |
|---|---|---|
| $\mathbb{B}\cong M_2(\mathbb{C})$ | associative complex algebra | $\dim_{\mathbb{C}}=4$, $\dim_{\mathbb{R}}=8$ |
| $\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}\cong\mathfrak{so}(1,3)$ | real Lie algebra, scalar-free part under $[-,-]$ | $\dim_{\mathbb{R}}=6$ |
| $\mathbb{B}$ under $[-,-]\cong\mathfrak{gl}(2,\mathbb{C})$ | real Lie algebra, whole algebra | $\dim_{\mathbb{R}}=8$, centre of dimension $2$ |
| $\mathfrak{so}(1,3)_{\mathbb{C}}\cong\mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C})$ | complex Lie algebra | $\dim_{\mathbb{C}}=6$ |

The determinant of the image is the algebra's complex quadratic form and not the interval. The traceless part is the Lorentz algebra because its bracket table is the Lorentz table and because its Killing form has inertia $(3,3)$. The complexification splits, and the split is where the label $(m,n)$ comes from. The Pauli convention is fixed here, and no prediction depends on the part of it that could have been otherwise.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $\mathsf{M}_2$ | the isomorphism $\mathbb{B}\to M_2(\mathbb{C})$ |
| $N(\tilde Q)$ | the biquaternion norm $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ |
| $\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}$ | the scalar-free part as a real Lie algebra, the Lorentz algebra |
| $\mathfrak{gl}(2,\mathbb{C})$ | the whole algebra under the commutator |
| $J_\eta=\tfrac12\vec e_\eta$ | the rotation generators, anti-Hermitian |
| $K_\eta=\tfrac12 i\vec e_\eta$ | the boost generators, Hermitian |
| $\vec J_\pm=\tfrac12(\vec J\pm i\vec K)$ | the two complex triples |
| $(m,n)$ | the pair of half-integers labelling an irreducible finite-dimensional representation |

## Further Reading

- B. C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction*, 2nd ed., Springer, 2015 — the isomorphisms of the classical algebras and the real forms, with the dimension bookkeeping done carefully.
- S. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, Academic Press, 1978 — the Killing form, semisimplicity, and the real forms of a complex simple algebra.
- W. Fulton and J. Harris, *Representation Theory: A First Course*, Springer, 1991 — the complexification of $\mathfrak{sl}(2,\mathbb{C})$ and the origin of the pair of half-integer labels.
- P. Lounesto, *Clifford Algebras and Spinors*, 2nd ed., Cambridge University Press, 2001 — the identification of the biquaternions with the $2\times2$ complex matrices and the place of the Pauli matrices in it.
- *Matrix Representations Conventions*, §*The $2\times2$ Pauli Representation*, and *Algebra and Element Conventions* — the corpus's own statements of the map and of the base.
- *The Six Generators and Their Commutators*, *The Two Commuting Complex Triples*, *The Cartan Subalgebra, the Roots and the Three Real Forms* — the articles that carry each of the four statements into its consequences.
