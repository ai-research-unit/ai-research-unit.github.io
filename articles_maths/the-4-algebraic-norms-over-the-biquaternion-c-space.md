# __The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space__

## Introduction

The twelve products of *The 12 Products of the Biquaternion Complex Space*, read as the twelve algebraic structures of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, carry four **forms** and no more, and this article starts from them. The four forms are the four **scalar parts** of the four general products, and they are counted and defined in *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*, read off the third column of the table of the twelve: the **general plain bilinear form** $B$, the **general quaternionic bilinear form** $N$, the **general plain sesquilinear form** $H$, also called the **Hermitian form**, and the **general quaternionic sesquilinear form** $K$, also called the **Krein form**, each written with the one bracket of *Conventions in the Biquaternion Universe* whose subscript records the pair $(a,b)$,

$$
B(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle,
\qquad
N(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{\natural},
\qquad
H(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{*},
\qquad
K(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{\natural*},
$$

for the four pairs $(\mathrm{id},\mathrm{id})$, $({}^{\natural},\mathrm{id})$, $(\mathrm{id},{}^{*})$, $({}^{\natural},{}^{*})$ read in that order. The chain of the section is the table of the twelve, then the four forms, then the four algebraic norms of this article, and the passage from the second to the third is one operation: the **diagonal**.

**Definition (the four algebraic norms).** The **algebraic norm** of a form is its **diagonal**, the form read at $\tilde P=\tilde Q$:

$$
B(\tilde Q)=B(\tilde Q,\tilde Q),\qquad
N(\tilde Q)=N(\tilde Q,\tilde Q),\qquad
H(\tilde Q)=H(\tilde Q,\tilde Q),\qquad
K(\tilde Q)=K(\tilde Q,\tilde Q).
$$

The four forms therefore give **four algebraic norms**, one to a form, written on the coordinates as

$$
B(\tilde Q)=\langle\tilde Q,\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^{2},\qquad
N(\tilde Q)=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2},\qquad
H(\tilde Q)=\langle\tilde Q,\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2},\qquad
K(\tilde Q)=\langle\tilde Q,\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2},
$$

with $\varepsilon=(1,-1,-1,-1)$. **One letter, two arities.** A letter names the **form** when it carries two arguments and the **algebraic norm** when it carries one; the norm is the form of the same name with its two arguments equated, and the four equations above are the whole of the definition. Read with one argument, the value is complex for $B$ and $N$ and real for $H$ and $K$, because a sesquilinear form has a real diagonal; the same equation written for a general form, $\varphi(\tilde Q)=\varphi(\tilde Q,\tilde Q)$, is the definition of §*The Algebraic Norm of an Operation*. The four names are $B$ the **general plain bilinear algebraic norm**, the diagonal of $B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)$; $N$ the **general quaternionic bilinear algebraic norm**, the diagonal of $N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$; $H$ the **general plain sesquilinear algebraic norm**, the diagonal of $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})$, also called the Hermitian algebraic norm; and $K$ the **general quaternionic sesquilinear algebraic norm**, the diagonal of $K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})$, also called the Krein algebraic norm. The symmetrisation of a family keeps the scalar part of the general product, so it keeps the form and its diagonal; the antisymmetrisation kills the scalar part, so it has neither. That is the whole of the count, and §*From the Four Forms to the Four Algebraic Norms* proves it.

The four algebraic norms are separated by three properties and no two of them share all three. The **value** lies in $\mathbb{C}$ for $B$ and $N$ and in $\mathbb{R}$ for $H$ and $K$. The **vanishing set** is the complex cone $\sum_\mu\varepsilon_\mu Q_\mu^{2}=0$ for $B$, the zero-divisor cone $\mathcal N$ for $N$, the origin alone for $H$, and the real cone $\mathcal K$ for $K$. **Multiplicativity** holds for $N$ alone and **definiteness** for $H$ alone; no one of the four is both, and that impossibility is the zero divisor of *Biquaternion Norm and Invertibility*.

The four algebraic norms of this article are the four degree-two functions of *The Four Pairings of the Biquaternion Algebra*, read on the diagonal of their pairings. Their names in the three-letter code of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* are read there; for the record, $B$ is carried by the general plain bilinear product and its symmetrisation, $N$ by the general quaternionic bilinear product and its symmetrisation, $H$ by the general plain sesquilinear product and its symmetrisation, and $K$ by the general quaternionic sesquilinear product and its symmetrisation, while the four antisymmetrisations carry no algebraic norm.

The one **topological** norm of the space, $\lVert\cdot\rVert_E$, is the square root of $H$ and it is unique; the other three are algebraic and give no distance. The distinction is that of *Introduction to Mathematics* and of *Hermitian Forms over Algebras and Norms*: the algebraic norm takes its value in the ring, and the topological norm is the selection of the positive real values among them, which is the passage to *The Norm Defined by a Form*.

## Notational Conventions

$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the biquaternion algebra, with basis $e_0,e_1,e_2,e_3$, $e_0=1$, $e_k^{2}=-e_0$, and central scalar imaginary $i$, $i^{2}=-1$. A general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$, written in the centre–vector split $\tilde Q=c+v$ with $c=Q_0e_0\in\mathbb{C}_{\mathbb{B}}$ and $v=\sum_{k=1}^{3}Q_ke_k\in\mathrm{Vect}(\mathbb{B})$. The scalar part is $\mathrm{Sc}$, the coefficientwise conjugation is $\bar{\cdot}$, the natural conjugation is ${}^{\natural}$, with $Q^{\natural}_\nu=\varepsilon_\nu Q_\nu$, and the Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$. The sign vector is $\varepsilon=(1,-1,-1,-1)$, and $\mathbb{B}$ is identified with $\mathbb{C}^{4}$ by $\tilde Q\mapsto(Q_0,Q_1,Q_2,Q_3)$. The vector parts carry the complex bilinear dot product $(\mathbf P,\mathbf Q)=\sum_{k=1}^{3}P_kQ_k$ and the cross product $\mathbf P\times\mathbf Q$. The four general forms are the four pairings of *Conventions in the Biquaternion Universe*, written there with one bracket $\langle\cdot,\cdot\rangle$ whose subscript records the pair $(a,b)$ — the natural conjugation ${}^{\natural}$ for a non-identity first slot and the star ${}^{*}$ for a non-identity second slot. In the letters of this article,

$$
B(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu Q_\mu,
\qquad
N(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=\sum_\mu P_\mu Q_\mu,
$$
$$
H(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu\overline{Q_\mu},
\qquad
K(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu},
$$

each being the trace form of its own pair up to the factor of the trace convention, $2h_{a,b}(\tilde P,\tilde Q)=\mathrm{Tr}(\tilde P^{a}\tilde Q^{b})$, for the four pairs $(\mathrm{id},\mathrm{id})$, $({}^{\natural},\mathrm{id})$, $(\mathrm{id},{}^{*})$, $({}^{\natural},{}^{*})$ read in that order. The four algebraic norms are the diagonals, $B(\tilde Q)=\langle\tilde Q,\tilde Q\rangle$, $N(\tilde Q)=\langle\tilde Q,\tilde Q\rangle_{\natural}$, $H(\tilde Q)=\langle\tilde Q,\tilde Q\rangle_{*}$ and $K(\tilde Q)=\langle\tilde Q,\tilde Q\rangle_{\natural*}$: the **general plain bilinear algebraic norm**, the **general quaternionic bilinear algebraic norm**, the **general plain sesquilinear algebraic norm** and the **general quaternionic sesquilinear algebraic norm**. The names, the bracket and the pair of each are the convention of *Conventions in the Biquaternion Universe*, which reads the four on the algebra and on the material sector; $H$ is also the Hermitian algebraic norm and $K$ the Krein algebraic norm, and the letters $B$, $N$, $H$, $K$ are the short names of this article. The Euclidean norm is $\lVert\tilde Q\rVert_E=\bigl(\sum_\mu\lvert Q_\mu\rvert^{2}\bigr)^{1/2}$.

## The Algebraic Norm of an Operation

**Definition (algebraic norm).** Let $f$ be an operation on $\mathbb{B}$ with scalar-part form $\varphi(\tilde P,\tilde Q)=\mathrm{Sc}\,f(\tilde P,\tilde Q)$. The **algebraic norm of the operation $f$** is the diagonal

$$
\varphi(\tilde Q)=\varphi(\tilde Q,\tilde Q),
$$

a function of one element taking its value in $\mathbb{C}$ when $f$ is $\mathbb{C}$-bilinear and in $\mathbb{R}$ when $f$ is Hermitian. For an operation whose scalar part vanishes identically the algebraic norm is the zero function.

The definition is the one of *Introduction to Mathematics*: the algebraic norm is the quadratic form $Q(x)=B(x,x)$ read on the diagonal of a form, valued in the ring. It records the size of an element only in the sense of the ring; it is not a distance, and it becomes a distance only when it is selected to take positive real values.

The four algebraic norms of the biquaternion algebra are then the four functions of the introduction, $B$, $N$, $H$ and $K$: the diagonals of the four forms of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*.

## From the Four Forms to the Four Algebraic Norms

The count of the four is taken, one step, in *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*: the symmetrisation of a family keeps the scalar part and the antisymmetrisation kills it, so the eight operations of the four $\mathrm G/\mathrm S$ rows carry the four forms two by two and the four antisymmetric operations carry the zero form. The twelve products are named in the three-letter code of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* — the general, symmetric and antisymmetric operation of each family, the plain and quaternionic family lettered $\mathrm P$ and $\mathrm Q$ and the algebra and sesqualgebra lettered $\mathrm A$ and $\mathrm S$, so that the twelve are $\mathrm{GPA},\mathrm{SPA},\mathrm{APA}$ in the plain algebra, $\mathrm{GQA},\mathrm{SQA},\mathrm{AQA}$ in the quaternionic algebra, and $\mathrm{GPS},\mathrm{SPS},\mathrm{APS}$, $\mathrm{GQS},\mathrm{SQS},\mathrm{AQS}$ in the two sesqualgebras.

**Proposition (the twelve operations carry four algebraic norms).** The twelve operations have exactly four distinct non-zero algebraic norms, the diagonals of the four forms above, each attained by two operations, and four operations have the zero algebraic norm.

*Proof.* The algebraic norm is the diagonal of the form, so the count of the four algebraic norms is the count of the four forms, which is the proposition of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*; the symmetrisation of a family therefore carries the same algebraic norm as the general product and the antisymmetrisation the zero one. Hence the algebraic norms of the twelve are those of the four general products, each on the two operations $\mathrm G$ and $\mathrm S$ of its family: $B$ on $\mathrm{GPA}$ and $\mathrm{SPA}$, $N$ on $\mathrm{GQA}$ and $\mathrm{SQA}$, $H$ on $\mathrm{GPS}$ and $\mathrm{SPS}$, $K$ on $\mathrm{GQS}$ and $\mathrm{SQS}$; and $0$ on $\mathrm{APA}$, $\mathrm{AQA}$, $\mathrm{APS}$ and $\mathrm{AQS}$. The four are distinct as functions of one element: on $e_1$ and on $ie_0$ their value pairs are

$$
B=(-1,-1),\qquad N=(1,-1),\qquad H=(1,1),\qquad K=(-1,1),
$$

which are four different pairs. $\square$

**Remark (the zero diagonal is not an algebraic norm).** The four antisymmetric operations have the zero algebraic norm because their scalar part is identically zero — $\mathbf P\times\mathbf Q$ for $\mathrm{APA}$ and $\mathrm{AQA}$, and the alternating forms of the two Hermitian forms for $\mathrm{APS}$ and $\mathrm{AQS}$. A vanishing quadratic form is not an algebraic norm, and its vanishing set is the whole space, so the four operations are counted with no algebraic norm rather than with a zero one.

## The Four Algebraic Norms

### The General Plain Bilinear Algebraic Norm $B$

$$
B(\tilde Q)=B(\tilde Q,\tilde Q)=\sum_\mu\varepsilon_\mu Q_\mu^{2}=Q_0^{2}-Q_1^{2}-Q_2^{2}-Q_3^{2},
$$

the diagonal of the general plain bilinear form $B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)=P_0Q_0-(\mathbf P,\mathbf Q)$. It is complex-valued and $\mathbb{C}$-quadratic, its Gram matrix on the coefficient basis is the sign matrix $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$, and its realification is of signature $(4,4)$. Its vanishing set is the complex cone $B(\tilde Q)=0$, already the complex quadric of *The Four Pairings of the Biquaternion Algebra*. It is not multiplicative. The algebraic norm is the diagonal of the **plain product**, the multiplication of the algebra, and it is the one algebraic norm the plain product carries.

### The General Quaternionic Bilinear Algebraic Norm $N$

$$
N(\tilde Q)=N(\tilde Q,\tilde Q)=\sum_\mu Q_\mu^{2}=Q_0^{2}+Q_1^{2}+Q_2^{2}+Q_3^{2},
$$

the diagonal of the general quaternionic bilinear form $N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$. It is complex-valued, its Gram matrix is the identity $\mathrm I_4$, and its realification is of signature $(4,4)$. Its vanishing set is the zero-divisor cone $\mathcal N=\{N(\tilde Q)=0\}$, of real dimension $6$, and the algebraic norm is the reason $\mathbb{B}$ has zero divisors at all.

**Proposition (multiplicativity).** $N$ is multiplicative:
$$
N(\tilde P\tilde Q)=N(\tilde P)\,N(\tilde Q).
$$

*Proof.* Under the matrix representation $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$, $\mathsf{M}_2(e_k)=-i\sigma_k$, the algebraic norm is the determinant, $N(\tilde Q)=\det\mathsf{M}_2(\tilde Q)$, as the computation of the determinant of $\mathsf{M}_2(\tilde Q)=Q_0\mathrm I-i\sum_kQ_k\sigma_k$ shows. The map $\mathsf{M}_2$ is an algebra homomorphism and the determinant is multiplicative, so $N$ is. $\square$

The algebraic norm is the **reduced norm** of the algebra, it is the only multiplicative one of the four, and it is the biquaternion algebraic norm of *Biquaternion Norm and Invertibility*: an element is invertible if and only if $N(\tilde Q)\neq0$, and the unit group is the norm-one group $\{N(\tilde Q)=1\}$, a non-compact real $6$-manifold homotopy equivalent to $S^{3}$.

### The General Plain Sesquilinear Algebraic Norm $H$

$$
H(\tilde Q)=H(\tilde Q,\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2}=\lvert Q_0\rvert^{2}+\lvert Q_1\rvert^{2}+\lvert Q_2\rvert^{2}+\lvert Q_3\rvert^{2},
$$

the diagonal of the general plain sesquilinear form $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})=P_0\overline{Q_0}+(\mathbf P,\overline{\mathbf Q})$. It is real-valued, $\mathbb{R}$-quadratic and positive definite, $H(\tilde Q)>0$ for $\tilde Q\neq0$; its Gram matrix is $\mathrm I_4$ and its realification is of signature $(8,0)$. Its vanishing set is the origin alone, and it is the square of the topological norm, $H(\tilde Q)=\lVert\tilde Q\rVert_E^{2}$.

The algebraic norm is definite, and it is the one of the four whose square root is the topological norm: $\lVert\tilde Q\rVert_E$ is the unique topological norm of the real vector space $\mathbb{B}\cong\mathbb{R}^{8}$, up to equivalence, and it is the topological norm under which every one of the twelve operations is read in *Topology and Metric for Each of the Twelve Operations*. It is not multiplicative.

### The General Quaternionic Sesquilinear Algebraic Norm $K$

$$
K(\tilde Q)=K(\tilde Q,\tilde Q)=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}=\lvert Q_0\rvert^{2}-\lvert Q_1\rvert^{2}-\lvert Q_2\rvert^{2}-\lvert Q_3\rvert^{2},
$$

the diagonal of the general quaternionic sesquilinear form $K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q})$; it is the **Krein algebraic norm** of the algebra, the diagonal of the Krein form. It is real-valued and indefinite, its Gram matrix is the sign matrix $\mathrm E$, and its realification is of signature $(2,6)$. Its vanishing set is the real cone $\mathcal K=\{\lVert c\rVert_E=\lVert v\rVert_E\}$ of the centre–vector split, and by the identity $K(\tilde Q)=\lVert c\rVert_E^{2}-\lVert v\rVert_E^{2}$ it is the null cone of the indefinite metric. It is not multiplicative. The algebraic norm is the one that the **Krein structure** of the algebra produces, the pair of a definite and an indefinite form, and its positive and negative value-one sets are $S^{1}\times\mathbb{R}^{6}$ and $S^{5}\times\mathbb{R}^{2}$.

## The Table of the Four Algebraic Norms

| algebraic norm | bracket of the form | diagonal, $B(\tilde Q)=B(\tilde Q,\tilde Q)$ | pairing | value | Gram | signature over $\mathbb{R}$ | vanishing set | multiplicative | definite |
|---|---|---|---|---|---|---|---|---|---|
| $B$ | $\langle\cdot,\cdot\rangle$ | $B(\tilde Q)=B(\tilde Q,\tilde Q)=\sum_\mu\varepsilon_\mu Q_\mu^{2}$ | the general plain bilinear form | $\mathbb{C}$ | $\mathrm E$ | $(4,4)$ | complex cone | no | — |
| $N$ | $\langle\cdot,\cdot\rangle_{\natural}$ | $N(\tilde Q)=N(\tilde Q,\tilde Q)=\sum_\mu Q_\mu^{2}$ | the general quaternionic bilinear form | $\mathbb{C}$ | $\mathrm I_4$ | $(4,4)$ | $\mathcal N$, the zero divisors | **yes** | — |
| $H$ | $\langle\cdot,\cdot\rangle_{*}$ | $H(\tilde Q)=H(\tilde Q,\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2}$ | the general plain sesquilinear form, the Hermitian form | $\mathbb{R}$ | $\mathrm I_4$ | $(8,0)$ | $\{0\}$ | no | **yes** |
| $K$ | $\langle\cdot,\cdot\rangle_{\natural*}$ | $K(\tilde Q)=K(\tilde Q,\tilde Q)=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$ | the general quaternionic sesquilinear form, the Krein form | $\mathbb{R}$ | $\mathrm E$ | $(2,6)$ | $\mathcal K$ | no | no |

The table separates the four by the field of their values, by the Gram matrix and the signature of their pairing, by their vanishing set, and by the two properties that single out one algebraic norm each: multiplicativity for $N$, definiteness for $H$.

## What the Four Algebraic Norms Separate

**Proposition (no algebraic norm is both definite and multiplicative).** No function on $\mathbb{B}$ is both definite and multiplicative.

*Proof.* The algebra has zero divisors, $(e_0+ie_1)(e_0-ie_1)=0$ with $e_0\pm ie_1\neq0$ and $N(e_0\pm ie_1)=1+i^{2}=0$. A multiplicative function $\varphi$ would give $\varphi(e_0+ie_1)\varphi(e_0-ie_1)=\varphi(0)=0$, so one of the two values is zero, on a nonzero element; a definite function is nonzero off the origin. No function is both. $\square$

**Corollary.** $N$ is multiplicative and not definite; $H$ is definite and not multiplicative; and no third algebraic norm of the four repairs the split. The multiplicative one and the definite one are different objects, and that difference is the failure of the biquaternions to be a normed division algebra — the four normed division algebras $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, $\mathbb{O}$ of the Hurwitz theorem are exactly the ones in which the two senses coincide.

**Proposition (only $N$ is multiplicative).** Of the four algebraic norms, $N$ alone satisfies $\varphi(\tilde P\tilde Q)=\varphi(\tilde P)\varphi(\tilde Q)$.

*Proof.* $N$ is multiplicative by the proposition of its section. The other three are not, each refuted by one substitution. For $B$: $B(e_1e_2)=B(e_3)=-1$ while $B(e_1)B(e_2)=(-1)(-1)=1$. For $H$: $H(e_1+ie_2)=1+1=2$ while $(e_1+ie_2)^{2}=e_1^{2}+(ie_2)^{2}=-e_0+e_0=0$ and $H(0)=0$. For $K$: $K(e_0+e_1)=1-1=0$ while $(e_0+e_1)^{2}=e_0^{2}+e_0e_1+e_1e_0+e_1^{2}=-e_0+e_1-e_1-e_0=-2e_0$ and $K(-2e_0)=4$. $\square$

**Remark (the two senses of *norm*).** Two different things carry the name. The **algebraic norm** of this article is a map into the ring — $B$ and $N$ into $\mathbb{C}$, $H$ and $K$ into $\mathbb{R}$ — and it is algebra: diagonals, quadratic forms, polarisations, zero divisors. The **topological norm** is the one selection of positive real values, $\lVert\tilde Q\rVert_E=\bigl(H(\tilde Q)\bigr)^{1/2}$, and it is topology: distance, balls, convergence, completeness. Only $H$ of the four yields it, because only $H$ is real and definite; $B$ and $N$ are complex-valued, and $K$ is real but indefinite. The two senses are the two layers of *Introduction to Mathematics*, and no third function holds them together.

**Remark (the four collapse to two on real elements).** For real $\tilde P,\tilde Q$ the coefficientwise conjugation is the identity, so $K(\tilde P,\tilde Q)=B(\tilde P,\tilde Q)$ and $H(\tilde P,\tilde Q)=N(\tilde P,\tilde Q)$. On the real part of the space the four algebraic norms are the two, $B=K$ and $N=H$, and the four operations of the two bilinear rows and of the two sesquilinear rows coincide there. This is the real-form caution of *The 12 Products of the Biquaternion Complex Space* read on the diagonal: a computation restricted to real elements sees two algebraic norms and hides the other two. On the six distinguished real subspaces the four algebraic norms restrict to the two real forms in the same way, and the restrictions, their signatures and the definiteness of each on each are the subject of *The Six Subspaces and the Four Algebraic Norms*.

## Summary

The twelve products of *The 12 Products of the Biquaternion Complex Space* carry four forms and, as their diagonals, four algebraic norms and no more: the symmetrisation of a family keeps the scalar part and the antisymmetrisation kills it, so the eight operations of the four $\mathrm G/\mathrm S$ rows carry the diagonals of the four forms two by two and the four antisymmetric operations carry the zero diagonal. The four are the general plain bilinear algebraic norm $B=\sum_\mu\varepsilon_\mu Q_\mu^{2}$, the general quaternionic bilinear algebraic norm $N=\sum_\mu Q_\mu^{2}$, the general plain sesquilinear algebraic norm $H=\sum_\mu\lvert Q_\mu\rvert^{2}$ and the general quaternionic sesquilinear algebraic norm $K=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$.

$B$ and $N$ are complex-valued and $H$ and $K$ real-valued. $N$ is the multiplicative one, the reduced norm and the criterion of invertibility; $H$ is the definite one, and its square root is the unique topological norm of the space; $B$ and $K$ are the two indefinite ones of the plain and of the Krein form. Multiplicativity and definiteness are held by no single one of the four, and the zero divisors are the reason.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $B(\tilde Q)=B(\tilde Q,\tilde Q)=\sum_\mu\varepsilon_\mu Q_\mu^{2}$ | the general plain bilinear algebraic norm, the diagonal of the general plain bilinear form |
| $N(\tilde Q)=N(\tilde Q,\tilde Q)=\sum_\mu Q_\mu^{2}$ | the general quaternionic bilinear algebraic norm, the diagonal of the general quaternionic bilinear form; multiplicative, the reduced norm |
| $H(\tilde Q)=H(\tilde Q,\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2}$ | the general plain sesquilinear algebraic norm, the diagonal of the general plain sesquilinear form; definite, $\lVert\tilde Q\rVert_E^{2}$ |
| $K(\tilde Q)=K(\tilde Q,\tilde Q)=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$ | the general quaternionic sesquilinear algebraic norm, the diagonal of the general quaternionic sesquilinear form; the Krein algebraic norm |
| $B(\tilde Q)=B(\tilde Q,\tilde Q)$ | one letter, two arities: two arguments give the form, one argument the algebraic norm |
| $\varepsilon=(1,-1,-1,-1)$ | the sign vector |
| $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$ | the Gram matrix of $B$ and of $K$; $\mathrm I_4$ is the Gram matrix of $N$ and of $H$ |
| $(4,4)$, $(4,4)$, $(8,0)$, $(2,6)$ | the realifications of $B$, $N$, $H$, $K$ |
| $\mathcal N$, $\mathcal K$ | the zero-divisor cone, the null cone of the Krein algebraic norm |
| $\lVert\tilde Q\rVert_E$ | the Euclidean norm, the square root of $H$, the unique topological norm |

## Further Reading

- *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*, the article that immediately precedes this one, for the table of the twelve, the count of the four forms and their definition with the one bracket whose subscript records the pair; this article starts from it.
- *The 12 Products of the Biquaternion Complex Space*, for the twelve products, their scalar parts and their two-slot construction, on which the reduction to four algebraic norms rests.
- *Conventions in the Biquaternion Universe*, for the convention of the four pairings — the one bracket $\langle\cdot,\cdot\rangle$ with the subscript that records the pair, the four names, the pairs $(\mathrm{id},\mathrm{id})$, $({}^{\natural},\mathrm{id})$, $(\mathrm{id},{}^{*})$, $({}^{\natural},{}^{*})$, the trace form $2h_{a,b}=\mathrm{Tr}(\tilde P^{a}\tilde Q^{b})$ and the readings of the four on the algebra and on the material sector.
- *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, for the twelve names $\mathrm{GPA},\dots,\mathrm{AQS}$ that carry the four algebraic norms two by two and the zero diagonal.
- *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, and *Comparison Between the Four General Products*, for the four general forms whose diagonals are the four algebraic norms, with their Gram matrices, their signatures and their symmetries.
- *The Four Pairings of the Biquaternion Algebra*, for the four pairings and the four degree-two functions, the separation of the two senses of *norm*, and the four general forms whose diagonals the four algebraic norms are.
- *The Six Subspaces and the Four Algebraic Norms*, for the restriction of the four algebraic norms to the six distinguished subspaces, with their signatures and the definiteness of each.
- *Biquaternion Norm and Invertibility*, for the multiplicative algebraic norm $N$, the zero divisors, the criterion of invertibility and the norm-one group.
- *Topology and Metric for Each of the Twelve Operations*, for the one topology and the one Euclidean norm of the space, and for the diagonal route that reaches a definite algebraic norm for $\mathrm{GPS}$ and $\mathrm{SPS}$ alone.
- *The Norm Defined by a Form*, *Hermitian Forms over Algebras and Norms* and *Introduction to Mathematics*, for the distinction between the algebraic norm, whose value is an element, and the topological norm, whose value is a positive real.
