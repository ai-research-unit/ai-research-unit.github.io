# __The Four Forms and the Four Algebraic Norms__

## Introduction

The four **forms** are the scalar parts of the four general products, $\varphi(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}\,f(\tilde Q_1,\tilde Q_2)$, and, read at their two equal arguments, they give four **algebraic norms**, $\varphi(\tilde Q)=\varphi(\tilde Q,\tilde Q)$. The twelve products of *Symmetric and Antisymmetric Decomposition of the Four General Products* carry these four and no more: the symmetrisation of a family keeps the scalar part and the antisymmetrisation kills it, so the eight operations of the four $\mathrm G/\mathrm S$ rows carry the four forms two by two and the four antisymmetric operations carry the zero form.

This article defines the four forms, writes them on the coordinates, tabulates them, reads the groups that preserve each and the hyperbolic decomposition of the plain bilinear form, and states what the four separate. It then passes to the four algebraic norms: their definition as the diagonal of a form, the proof that the twelve operations carry exactly four, their coordinates, their table and what they separate — among it the definiteness of the Hermitian algebraic norm, the multiplicativity of the quaternionic one and the impossibility of one function being both.

The four forms are the scalar parts of the four general products of *The Four General Products and Their Relations*, which owns the products, their relations and their comparison. The distinction between the algebraic norm, whose value is an element of the ring, and the topological norm, whose value is a positive real, is *The Norm Defined by a Form*; the one topological norm of the space is the square root of the Hermitian algebraic norm.

## Notational Conventions

$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the biquaternion algebra, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, $e_t=1$, $\vec e_k^{2}=-e_t$, and central scalar imaginary $i$, $i^{2}=-1$. A general element is $\tilde Q_2=\sum_{\mu\in\{t,x,y,z\}}Q_{2,\mu} e_\mu$ with $Q_{2,\mu}\in\mathbb{C}$, written in the centre–vector split $\tilde Q_2=c+v$ with $c=Q_{2t}e_t\in\mathbb{C}_{\mathbb{B}}$ and $v=\sum_{k=1}^{3}Q_{2,k}\vec e_k\in\mathrm{Vect}(\mathbb{B})$. The scalar part is $\mathrm{Sc}$, the coefficientwise conjugation is $\bar{\cdot}$, the natural conjugation is ${}^{\natural}$, with $Q^{\natural}_\nu=\varepsilon_\nu Q_{2,\nu}$, and the Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$. The sign vector is $\varepsilon=(1,-1,-1,-1)$, and $\mathbb{B}$ is identified with $\mathbb{C}^{4}$ by $\tilde Q_2\mapsto(Q_{2t},Q_{2x},Q_{2y},Q_{2z})$. The vector parts carry the complex bilinear dot product $(\vec Q_1,\vec Q_2)=\sum_{k=1}^{3}Q_{1,k}Q_{2,k}$ and the cross product $\vec Q_1\times\vec Q_2$. The four forms are $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural}$ and $\langle\cdot,\cdot\rangle_{\natural*}$; their names, brackets and pairs are the convention of *Conventions in the Biquaternion Universe*, which reads the four on the algebra and on the material sector. $\langle\cdot,\cdot\rangle_{*}$ is also the Hermitian form and $\langle\cdot,\cdot\rangle_{\natural*}$ the Krein form, and the brackets $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{\natural*}$ are the short names of this article. A form is $\mathbb{C}$-**bilinear** when its second slot is read without the star, so that a scalar pulls out of it, and **sesquilinear** when the second slot is read with the star, so that the scalar pulls out conjugated. The Euclidean norm is $\lVert\tilde Q_2\rVert_E=\bigl(\sum_\mu\lvert Q_{2,\mu}\rvert^{2}\bigr)^{1/2}$, the square root of the algebraic norm of $\langle\cdot\rangle_{*}$.


## The Form of an Operation

**Definition (the form of an operation).** Let $f$ be an operation on $\mathbb{B}$ with scalar part $\varphi(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}\,f(\tilde Q_1,\tilde Q_2)$. The **form of the operation $f$** is $\varphi$. It is bilinear when the second slot of $f$ is read without the star, sesquilinear when it is read with the star. In both cases the value lies in $\mathbb{C}$, the conjugation of the second slot entering the value; a sesquilinear form is conjugate-symmetric, $\varphi(\tilde Q_1,\tilde Q_2)=\overline{\varphi(\tilde Q_2,\tilde Q_1)}$, so that its algebraic norm is real. For an operation whose scalar part vanishes identically the form is the zero form.

The definition is the one of *Introduction to Mathematics*: the form is the degree-two object attached to a product, it is a function of two elements, and the algebraic norm is that form at its two equal arguments, a function of one. The four forms of the biquaternion algebra are then the four functions of the introduction, $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural}$ and $\langle\cdot,\cdot\rangle_{\natural*}$, read on the third column of the table of the twelve.


## The Four Forms

The four forms are the scalar parts of the four general products, one to each pair of slots. Each is written on the coordinates of a pair, with its Gram matrix and its signature.

### The General Plain Bilinear Form

$$
\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)=Q_{1,0}Q_{2t}-(\vec Q_1,\vec Q_2),
$$

the scalar part of the general plain bilinear product. It is symmetric, $\mathbb{C}$-bilinear and complex-valued, its Gram matrix on the coefficient basis is the sign matrix $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$, and its realification is of signature $(4,4)$. It is non-degenerate. Its null set, the set of $\tilde Q$ with $\langle\tilde Q,\tilde Q\rangle=0$, is the complex cone $\sum_\mu\varepsilon_\mu Q_\mu^{2}=0$, of real dimension six, and it is neither the zero-divisor cone nor the null cone. In the physics of the corpus this is the form of **composition**: it pairs two material operations, and its algebraic norm carries the sector sign, negative on the anti-Hermitian sector and positive on the Hermitian one.

### The General Plain Sesquilinear Form, the Hermitian Form

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=Q_{1,0}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2}),
$$

the scalar part of the general plain sesquilinear product. It is conjugate-symmetric, $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\overline{\langle\tilde Q_2,\tilde Q_1\rangle_{*}}$, sesquilinear in the second slot, and its algebraic norm is real and positive definite, $\langle\tilde Q_2,\tilde Q_2\rangle_{*}>0$ for $\tilde Q_2\neq0$; its Gram matrix is $\mathrm I_4$ and its realification is of signature $(8,0)$. It is non-degenerate, and its null set is the origin alone, so it has no cone. This is the form of **probability**: it is the Born pairing, definite, and its algebraic norm is the square of the unique topological norm of the space, $\lVert\tilde Q_2\rVert_E^{2}$.

### The General Quaternionic Bilinear Form

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)=Q_{1,0}Q_{2t}+(\vec Q_1,\vec Q_2),
$$

the scalar part of the general quaternionic bilinear product: the same form as $\langle\cdot,\cdot\rangle$ read through the natural conjugation of the first slot, differing from it by the sign of the vector part alone. It is symmetric, $\mathbb{C}$-bilinear and complex-valued, its Gram matrix is the identity $\mathrm I_4$, and its realification is of signature $(4,4)$. It is non-degenerate. Its null set is the zero-divisor cone $\mathcal N=\{\langle\tilde Q,\tilde Q\rangle_{\natural}=0\}$, of real dimension six, which is the null cone of the physics corpus. This is the form of **causality**: its algebraic norm is the interval, and the pair of the first slot is what makes the square of a material element land on the interval rather than on the negative Euclidean square.

### The General Quaternionic Sesquilinear Form, the Krein Form

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})=Q_{1,0}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2}),
$$

the scalar part of the general quaternionic sesquilinear product: the same form as $\langle\cdot,\cdot\rangle_{*}$ read through the natural conjugation of the first slot, differing from it by the sign of the vector part alone. It is conjugate-symmetric and sesquilinear, its algebraic norm is real and indefinite, its Gram matrix is the sign matrix $\mathrm E$, and its realification is of signature $(2,6)$. It is non-degenerate, and its null set is the real cone $\mathcal K$, the null cone of the Krein form. This is the form of **gauge**: indefinite, of mixed signature on every sector, and the form of a constraint rather than of a state space.


## The Table of the Four Forms

| form | bracket | pair | coordinates | symmetry | Gram | signature over $\mathbb{R}$ | null set | algebraic norm lands in |
|---|---|---|---|---|---|---|---|---|
| the plain form | $\langle\cdot,\cdot\rangle$ | $(\mathrm{id},\mathrm{id})$ | $Q_{1,0}Q_{2t}-(\vec Q_1,\vec Q_2)$ | symmetric | $\mathrm E$ | $(4,4)$ | the complex cone | $\mathbb{C}$ |
| the Hermitian form | $\langle\cdot,\cdot\rangle_{*}$ | $(\mathrm{id},{}^{*})$ | $Q_{1,0}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$ | conjugate-symmetric | $\mathrm I_4$ | $(8,0)$ | $\{0\}$ | $\mathbb{R}$ |
| the quaternionic form | $\langle\cdot,\cdot\rangle_{\natural}$ | $({}^{\natural},\mathrm{id})$ | $Q_{1,0}Q_{2t}+(\vec Q_1,\vec Q_2)$ | symmetric | $\mathrm I_4$ | $(4,4)$ | $\mathcal N$, the zero divisors | $\mathbb{C}$ |
| the Krein form | $\langle\cdot,\cdot\rangle_{\natural*}$ | $({}^{\natural},{}^{*})$ | $Q_{1,0}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})$ | conjugate-symmetric | $\mathrm E$ | $(2,6)$ | $\mathcal K$ | $\mathbb{R}$ |

The table separates the four by their bracket and pair, by their symmetry, by the Gram matrix and the signature of the realification of their algebraic norm, by their null set, and by the field in which the algebraic norm lands — complex for the two bilinear forms and real for the two sesquilinear ones, the conjugating second slot being what makes a algebraic norm real.


## Why the Other Eight Operations Add No New Form

The four forms are the scalar parts of the four general products, and the eight remaining operations of *Symmetric and Antisymmetric Decomposition of the Four General Products* add none: a symmetric part keeps the scalar part of its general product and an antisymmetric part loses it.

**Lemma.** For a general product $f$ with parts $f^{\mathrm s}$ and $f^{\mathrm a}$, $\mathrm{Sc}\,f^{\mathrm s}=\mathrm{Sc}\,f$ and $\mathrm{Sc}\,f^{\mathrm a}=0$.

*Proof.* For the two bilinear families $\mathrm{Sc}$ is commutative, so the half-sum equals $\mathrm{Sc}\,f$ and the half-difference vanishes. For the two sesquilinear families the exchange conjugates the value, $\mathrm{Sc}\,f(\tilde Q_1,\tilde Q_2)=\overline{\mathrm{Sc}\,f(\tilde Q_2,\tilde Q_1)}$, and the half-sum and the half-difference give the same result.

**Proposition.** The twelve operations carry exactly four non-zero forms, each shared by a general product and its symmetric part: $\langle\cdot,\cdot\rangle$ on $\mathrm{GPA}$ and $\mathrm{SPA}$, $\langle\cdot,\cdot\rangle_{*}$ on $\mathrm{GPS}$ and $\mathrm{SPS}$, $\langle\cdot,\cdot\rangle_{\natural}$ on $\mathrm{GQA}$ and $\mathrm{SQA}$, and $\langle\cdot,\cdot\rangle_{\natural*}$ on $\mathrm{GQS}$ and $\mathrm{SQS}$; the four antisymmetric operations carry the zero form.

*Proof.* The lemma gives the first clause. The four are distinct: at $\tilde Q_1=\vec e_x$ and $\tilde Q_2=\vec e_x+i\vec e_x$ they take the four different values $-(1+i)$, $1-i$, $1+i$ and $-(1-i)$.

**Remark.** The zero form is not counted as a fifth: $\vec Q_1\times\vec Q_2$ for $\mathrm{APA}$ and $\mathrm{AQA}$, and the alternating parts of the two Hermitian forms for $\mathrm{APS}$ and $\mathrm{AQS}$.

## The Isometry Groups of the Four Forms

A $\mathbb{C}$-linear operator $T$ **preserves** a form $\varphi$ when $\varphi(T\tilde Q_1,T\tilde Q_2)=\varphi(\tilde Q_1,\tilde Q_2)$ for every pair, and the preserving operators form a group, the **isometry group** $\mathrm{Isom}(\varphi)$. The four forms are separated by their four groups, and the four groups are classical.

**Theorem (the four isometry groups).** The $\mathbb{C}$-linear operators preserving the four forms are, in the coefficient basis,

$$
\boxed{\;
\mathrm{Isom}(B)=\{T:T^{\mathsf T}\mathrm E T=\mathrm E\}=O_4(\mathbb{C}),
\qquad
\mathrm{Isom}(H)=\{T:T^{*}T=\mathrm I_4\}=\mathrm{U}(4)
\;},
$$
$$
\mathrm{Isom}(N)=\{T:T^{\mathsf T}T=\mathrm I_4\}=O_4(\mathbb{C}),
\qquad
\mathrm{Isom}(K)=\{T:T^{*}\mathrm E T=\mathrm E\}=\mathrm{U}(1,3),
$$

of real dimensions $12$, $16$, $12$ and $16$.

*Proof.* A form with Gram matrix $G$ is preserved by a $\mathbb{C}$-linear $T$ exactly when $T^{\mathsf T}GT=G$ in the bilinear case and $T^{*}GT=G$ in the Hermitian case, $T^{\mathsf T}$ the transpose and $T^{*}$ the conjugate transpose. With $G=\mathrm I_4$ these are the defining equations of the complex orthogonal group $O_4(\mathbb{C})$ and of the unitary group $\mathrm{U}(4)$. With $G=\mathrm E$ the sign matrix is congruent to the identity over $\mathbb{C}$, $\mathrm E=(S^{-1})^{\mathsf T}S^{-1}$ for $S=\operatorname{diag}(1,i,i,i)$, so that $T$ preserves $\langle\cdot,\cdot\rangle$ exactly when $STS^{-1}$ is orthogonal and $T$ preserves $\langle\cdot,\cdot\rangle_{\natural*}$ exactly when $STS^{-1}$ is unitary; the two groups with $\mathrm E$ are conjugates of the two groups with $\mathrm I_4$, and this is why the same name $O_4(\mathbb{C})$ serves both bilinear forms and why the second group is written $\mathrm{U}(1,3)$. The dimensions are the classical ones, $\dim_{\mathbb{R}}O_4(\mathbb{C})=12$ and $\dim_{\mathbb{R}}\mathrm{U}(4)=\dim_{\mathbb{R}}\mathrm{U}(1,3)=16$, and they were recomputed as the dimensions of the four Lie algebras $\{X:X^{\mathsf T}G+GX=0\}$.

**Remark (the two slots read on the groups).** The **second slot** decides whether the group is **orthogonal** or **unitary**, since it decides whether the form is bilinear or Hermitian; the **first slot** decides **which** orthogonal or unitary form, the sign matrix $\mathrm E$ against the identity $\mathrm I_4$ — the same division of labour that §*What the Four Forms Separate* reads on the symmetry and the signature.

**Remark (the natural conjugation lies in all four).** The natural conjugation is the operator $\mathrm E$ in the coefficient basis, and $\mathrm E$ preserves each of the four forms, since $\mathrm E^{\mathsf T}\mathrm E\,\mathrm E=\mathrm E$ and $\mathrm E^{*}\mathrm E\,\mathrm E=\mathrm E$ with $\mathrm E^{2}=\mathrm I_4$; the fundamental symmetry of the algebra therefore sits in all four groups of the theorem.


## The Hyperbolic Decomposition of the Plain Bilinear Form

The general plain bilinear form $\langle\cdot,\cdot\rangle$ is the complex-valued one of the four, of Gram matrix $\mathrm E$, and its null set is the complex cone of §*The Table of the Four Forms*. Its Gram matrix becomes the standard hyperbolic matrix in a suitable basis, and the basis exhibits the form as two hyperbolic planes.

**Theorem (the form is an orthogonal sum of two hyperbolic planes).** The four elements

$$
\boxed{\;
h_1=e_t+\vec e_x,\qquad h_2=\tfrac12(e_t-\vec e_x),\qquad h_3=\vec e_y+i\vec e_z,\qquad h_4=\tfrac12(i\vec e_z-\vec e_y)
\;}
$$

are isotropic for $\langle\cdot,\cdot\rangle$, the only non-zero pairings among them are $\langle h_1,h_2\rangle=1$ and $\langle h_3,h_4\rangle=1$, and the Gram matrix in this basis is

$$
\begin{pmatrix}0&1&0&0\\1&0&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}.
$$

The form is therefore the orthogonal sum of the two hyperbolic planes $\operatorname{span}\{e_t,\vec e_x\}$ and $\operatorname{span}\{\vec e_y,\vec e_z\}$, of index $1+1=2$ over $\mathbb{C}$ and $4$ over $\mathbb{R}$.

*Proof.* From the coefficient form $\langle\tilde Q_1,\tilde Q_2\rangle=\sum_\mu\varepsilon_\mu Q_{1,\mu} Q_{2,\mu}$ with $\varepsilon=(1,-1,-1,-1)$: inside the first plane $\varepsilon_0=1$ and $\varepsilon_1=-1$, so $\langle h_1,h_1\rangle=1-1=0$, $\langle h_2,h_2\rangle=\tfrac14(1-1)=0$ and $\langle h_1,h_2\rangle=\tfrac12\bigl(\langle e_t,e_t\rangle-\langle \vec e_x,\vec e_x\rangle\bigr)=\tfrac12(1+1)=1$; inside the second $\varepsilon_2=\varepsilon_3=-1$ with $\langle \vec e_y,i\vec e_z\rangle=\langle i\vec e_z,\vec e_y\rangle=0$, so $\langle h_3,h_3\rangle=\langle \vec e_y,\vec e_y\rangle+\langle i\vec e_z,i\vec e_z\rangle=-1+1=0$, $\langle h_4,h_4\rangle=\tfrac14\bigl(\langle i\vec e_z,i\vec e_z\rangle+\langle \vec e_y,\vec e_y\rangle\bigr)=\tfrac14(1-1)=0$ and $\langle h_3,h_4\rangle=\tfrac12\bigl(\langle i\vec e_z,i\vec e_z\rangle-\langle \vec e_y,\vec e_y\rangle\bigr)=\tfrac12(1+1)=1$; and the cross-pairings vanish because the two planes carry disjoint coefficient supports and meet in the origin. The index over $\mathbb{C}$ is the number of hyperbolic planes, hence $1+1=2$, and the realification of $\langle\cdot,\cdot\rangle$ has signature $(4,4)$ of §*The Table of the Four Forms*, of real index $4$, which is $2\cdot2$.

**Remark (the maximal isotropic subspaces).** The index $2$ is the largest complex dimension of a subspace on which $\langle\cdot,\cdot\rangle$ vanishes identically, half the dimension of the space; two such planes of this example are $\operatorname{span}_{\mathbb{C}}\{e_t+\vec e_x,\,\vec e_y+i\vec e_z\}$ and $\operatorname{span}_{\mathbb{C}}\{e_t-\vec e_x,\,\vec e_y-i\vec e_z\}$, each of complex dimension $2$, distinct, and meeting in the origin.


## The Two Slots

**The mechanism.** A form is obtained from a product by reading the first factor either as it stands or through the natural conjugation ${}^{\natural}$, and the second factor either as it stands or through the star ${}^{*}$; nothing else varies. The four forms are therefore indexed by a two-by-two grid, and the grid is the whole of the subject. The mechanism, the laws and the readings are shared with *The Four General Products and Their Relations* and with the physics companion *The Four General Products: Composition, Probability, Causality, Gauge*, which carries the signature table of the four on the remarkable subspaces.

**What each slot decides.**

- The **second slot** decides whether the form is a **composition** or a **pairing**. Read without the star the form is bilinear and symmetric and can be iterated; read with the star it is sesquilinear and conjugate-symmetric and can only be evaluated. It is the slot that separates the two bilinear forms from the two sesquilinear ones, and it is what makes the algebraic norm of a sesquilinear form real.
- The **first slot** decides the **Gram matrix** and the **signature**, and through them **definiteness on each sector**. Read as it stands the form is $\langle\cdot,\cdot\rangle$ or $\langle\cdot,\cdot\rangle_{*}$; read through the natural conjugation it is $\langle\cdot,\cdot\rangle_{\natural}$ or $\langle\cdot,\cdot\rangle_{\natural*}$. Since the natural conjugation multiplies the vector part by $-1$, the first slot toggles the coefficient $\varepsilon$ of the vector part and so turns the sign matrix $\mathrm E$ into the identity $\mathrm I_4$.

**The physical reading, and it is a reading and not a theorem.** The four forms are the four jobs a relativistic quantum theory needs: the general plain bilinear form is **composition**, the general plain sesquilinear form is **probability**, the general quaternionic bilinear form is **causality** and the general quaternionic sesquilinear form is **gauge**. The reading is the one of the physics companion (*The Four General Products: Composition, Probability, Causality, Gauge*); it is stated here and not proved, since what is proved here is the count of the four and their table.


## What the Four Forms Separate

**Proposition (no two of the four agree).** No two of the four forms are equal as functions of two elements.

*Proof.* On $\tilde Q_1=\vec e_x$, $\tilde Q_2=\vec e_x+i\vec e_x$ the four values are $-(1+i)$, $1+i$, $1-i$ and $-(1-i)$, four different complex numbers, as in the proposition of §*Why the Other Eight Operations Add No New Form*.

**The second slot gives the symmetry, the first slot the signature.** The four forms fall into two pairs by symmetry, $\{\langle\cdot,\cdot\rangle,\langle\cdot,\cdot\rangle_{\natural}\}$ bilinear and $\{\langle\cdot,\cdot\rangle_{*},\langle\cdot,\cdot\rangle_{\natural*}\}$ sesquilinear, and into two other pairs by Gram matrix, $\{\langle\cdot,\cdot\rangle,\langle\cdot,\cdot\rangle_{\natural*}\}$ of Gram $\mathrm E$ and $\{\langle\cdot,\cdot\rangle_{*},\langle\cdot,\cdot\rangle_{\natural}\}$ of Gram $\mathrm I_4$. The two divisions are independent, and their product is the four: each form is the intersection of one symmetry with one Gram matrix, which is the two-by-two grid of the two slots.

**The four collapse to two on real elements.** For real $\tilde Q_1,\tilde Q_2$ the coefficientwise conjugation is the identity, so $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\langle\tilde Q_1,\tilde Q_2\rangle$ and $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$. On the real part of the space the four forms are the two, and only the two slots together, not the complex structure, separate them.

**The null sets are four.** The null set of $\langle\cdot,\cdot\rangle$ is the complex cone, that of $\langle\cdot,\cdot\rangle_{*}$ the origin alone, that of $\langle\cdot,\cdot\rangle_{\natural}$ the zero-divisor cone $\mathcal N$ — the null cone —, and that of $\langle\cdot,\cdot\rangle_{\natural*}$ the real cone $\mathcal K$. Three of the four are cones: the complex cone and the zero-divisor cone, of real dimension six, and the Krein cone, of real dimension seven. The two of dimension six do not agree, so the complex cone of $\langle\cdot,\cdot\rangle$ is not the null cone of $\langle\cdot,\cdot\rangle_{\natural}$; the fourth null set is the origin, so the algebraic norm of $\langle\cdot\rangle_{*}$ is definite and has no cone. The three cones and the origin are what the physics reads as the two null cones and the two definite structures.


## The Algebraic Norm of an Operation

**Definition (algebraic norm).** Let $f$ be an operation on $\mathbb{B}$ with scalar-part form $\varphi(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}\,f(\tilde Q_1,\tilde Q_2)$. The **algebraic norm of the operation $f$** is the algebraic norm

$$
\varphi(\tilde Q)=\varphi(\tilde Q,\tilde Q),
$$

a function of one element taking its value in $\mathbb{C}$ when $f$ is $\mathbb{C}$-bilinear and in $\mathbb{R}$ when $f$ is Hermitian. For an operation whose scalar part vanishes identically the algebraic norm is the zero function.

The definition is the one of *Introduction to Mathematics*: the algebraic norm is the quadratic form $\mathfrak{Q}(x)=\langle x,x\rangle$ read at the two equal arguments of a form, valued in the ring. It records the size of an element only in the sense of the ring; it is not a distance, and it becomes a distance only when it is selected to take positive real values.

The four algebraic norms of the biquaternion algebra are then the four functions of the introduction, $\langle\cdot\rangle$, $\langle\cdot\rangle_{*}$, $\langle\cdot\rangle_{\natural}$ and $\langle\cdot\rangle_{\natural*}$: the four algebraic norms of the four forms of this article.


## From the Four Forms to the Four Algebraic Norms

The count of the four is taken, one step, in §*Why the Other Eight Operations Add No New Form*, above: the symmetrisation of a family keeps the scalar part and the antisymmetrisation kills it, so the eight operations of the four $\mathrm G/\mathrm S$ rows carry the four forms two by two and the four antisymmetric operations carry the zero form. The twelve products are named in the three-letter code defined in *Symmetric and Antisymmetric Decomposition of the Four General Products* — the general, symmetric and antisymmetric operation of each family, the plain and quaternionic family lettered $\mathrm P$ and $\mathrm Q$ and the algebra and sesqualgebra lettered $\mathrm A$ and $\mathrm S$, so that the twelve are $\mathrm{GPA}$, $\mathrm{GPS}$, $\mathrm{GQA}$, $\mathrm{GQS}$ the four general, $\mathrm{SPA}$, $\mathrm{SPS}$, $\mathrm{SQA}$, $\mathrm{SQS}$ the four symmetric and $\mathrm{APA}$, $\mathrm{APS}$, $\mathrm{AQA}$, $\mathrm{AQS}$ the four antisymmetric.

**Proposition (the twelve operations carry four algebraic norms).** The twelve operations have exactly four distinct non-zero algebraic norms, the four algebraic norms above, each attained by two operations, and four operations have the zero algebraic norm.

*Proof.* The algebraic norm is the form at the two equal arguments, so the count of the four algebraic norms is the count of the four forms, which is the proposition of §*Why the Other Eight Operations Add No New Form*, above; the symmetrisation of a family therefore carries the same algebraic norm as the general product and the antisymmetrisation the zero one. Hence the algebraic norms of the twelve are those of the four general products, each on the two operations $\mathrm G$ and $\mathrm S$ of its family: $\langle\cdot\rangle$ on $\mathrm{GPA}$ and $\mathrm{SPA}$, $\langle\cdot\rangle_{*}$ on $\mathrm{GPS}$ and $\mathrm{SPS}$, $\langle\cdot\rangle_{\natural}$ on $\mathrm{GQA}$ and $\mathrm{SQA}$, $\langle\cdot\rangle_{\natural*}$ on $\mathrm{GQS}$ and $\mathrm{SQS}$; and $0$ on $\mathrm{APA}$, $\mathrm{APS}$, $\mathrm{AQA}$ and $\mathrm{AQS}$. The four are distinct as functions of one element: on $\vec e_x$ and on $ie_t$ their value pairs are

$$
\boxed{\;
B=(-1,-1),\qquad H=(1,1),\qquad N=(1,-1),\qquad K=(-1,1)
\;},
$$

which are four different pairs.

**Remark (a vanishing form carries no algebraic norm).** The four antisymmetric operations have the zero algebraic norm because their scalar part is identically zero — $\vec Q_1\times\vec Q_2$ for $\mathrm{APA}$ and $\mathrm{AQA}$, and the alternating forms of the two Hermitian forms for $\mathrm{APS}$ and $\mathrm{AQS}$. A vanishing quadratic form is not an algebraic norm, and its vanishing set is the whole space, so the four operations are counted with no algebraic norm rather than with a zero one.


## The Four Algebraic Norms

Each algebraic norm is the diagonal of its form. The four are written on the coordinates of one element, with their value rings, their Gram matrices and their signatures.

### The General Plain Bilinear Algebraic Norm

$$
\boxed{\;
\langle\tilde Q\rangle=\langle\tilde Q,\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^{2}=Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2}
\;},
$$

the general plain bilinear algebraic norm $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)=Q_{1,0}Q_{2t}-(\vec Q_1,\vec Q_2)$. It is complex-valued and $\mathbb{C}$-quadratic, its Gram matrix on the coefficient basis is the sign matrix $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$, and its realification is of signature $(4,4)$. Its vanishing set is the complex cone $\langle\tilde Q\rangle=0$, already the complex quadric of §*The Four Forms*, above. It is not multiplicative. The algebraic norm is that of the **plain product**, the multiplication of the algebra, and it is the one algebraic norm the plain product carries.

### The General Plain Sesquilinear Algebraic Norm

$$
\langle\tilde Q\rangle_{*}=\langle\tilde Q,\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}=\lvert Q_t\rvert^{2}+\lvert Q_x\rvert^{2}+\lvert Q_y\rvert^{2}+\lvert Q_z\rvert^{2},
$$

the general plain sesquilinear algebraic norm $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=Q_{1,0}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$. It is real-valued, $\mathbb{R}$-quadratic and positive definite, $\langle\tilde Q\rangle_{*}>0$ for $\tilde Q\neq0$; its Gram matrix is $\mathrm I_4$ and its realification is of signature $(8,0)$. Its vanishing set is the origin alone, and it is the square of the topological norm, $\langle\tilde Q\rangle_{*}=\lVert\tilde Q\rVert_E^{2}$.

The algebraic norm is definite, and it is the one of the four whose square root is the topological norm: $\lVert\tilde Q\rVert_E$ is the unique topological norm of the real vector space $\mathbb{B}\cong\mathbb{R}^{8}$, up to equivalence, and it is the topological norm under which every one of the twelve operations is read in *Topology and Metric for Each of the Twelve Operations*. It is not multiplicative.

### The General Quaternionic Bilinear Algebraic Norm

$$
\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2},
$$

the general quaternionic bilinear algebraic norm $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)=Q_{1,0}Q_{2t}+(\vec Q_1,\vec Q_2)$. It is complex-valued, its Gram matrix is the identity $\mathrm I_4$, and its realification is of signature $(4,4)$. Its vanishing set is the zero-divisor cone $\mathcal N=\{\langle\tilde Q\rangle_{\natural}=0\}$, of real dimension $6$, and the algebraic norm is the reason $\mathbb{B}$ has zero divisors at all.

**Proposition (multiplicativity).** $\langle\cdot\rangle_{\natural}$ is multiplicative:
$$
\boxed{\;
\langle\tilde Q_1\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1\rangle_{\natural}\,\langle\tilde Q_2\rangle_{\natural}
\;}.
$$

*Proof.* Under the matrix representation $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$, $\mathsf{M}_2(\vec e_k)=-i\sigma_k$, the algebraic norm is the determinant, $\langle\tilde Q\rangle_{\natural}=\det\mathsf{M}_2(\tilde Q)$, as the computation of the determinant of $\mathsf{M}_2(\tilde Q)=Q_t\mathrm I-i\sum_kQ_k\sigma_k$ shows. The map $\mathsf{M}_2$ is an algebra homomorphism and the determinant is multiplicative, so $\langle\cdot\rangle_{\natural}$ is.

The algebraic norm is the **reduced norm** of the algebra, it is the only multiplicative one of the four, and it is the biquaternion algebraic norm of *Norm and Invertibility in the General Quaternionic Algebra*: an element is invertible if and only if $\langle\tilde Q\rangle_{\natural}\neq0$, and the unit group is the norm-one group $\{\langle\tilde Q\rangle_{\natural}=1\}$, a non-compact real $6$-manifold homotopy equivalent to $S^{3}$.

### The General Quaternionic Sesquilinear Algebraic Norm

$$
\langle\tilde Q\rangle_{\natural*}=\langle\tilde Q,\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}=\lvert Q_t\rvert^{2}-\lvert Q_x\rvert^{2}-\lvert Q_y\rvert^{2}-\lvert Q_z\rvert^{2},
$$

the general quaternionic sesquilinear algebraic norm $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})=Q_{1,0}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})$; it is the **Krein algebraic norm** of the algebra, the algebraic norm of the Krein form. It is real-valued and indefinite, its Gram matrix is the sign matrix $\mathrm E$, and its realification is of signature $(2,6)$. Its vanishing set is the real cone $\mathcal K=\{\lVert c\rVert_E=\lVert v\rVert_E\}$ of the centre–vector split, and by the identity $\langle\tilde Q\rangle_{\natural*}=\lVert c\rVert_E^{2}-\lVert v\rVert_E^{2}$ it is the null cone of the indefinite metric. It is not multiplicative. The algebraic norm is the one that the **Krein structure** of the algebra produces, the pair of a definite and an indefinite form, and its positive and negative value-one sets are $S^{1}\times\mathbb{R}^{6}$ and $S^{5}\times\mathbb{R}^{2}$.


## The Table of the Four Algebraic Norms

| algebraic norm | bracket of the form | algebraic norm, $\langle\tilde Q\rangle=\langle\tilde Q,\tilde Q\rangle$ | pairing | value | Gram | signature over $\mathbb{R}$ | vanishing set | multiplicative | definite |
|---|---|---|---|---|---|---|---|---|---|
| $\langle\cdot\rangle$ | $\langle\cdot,\cdot\rangle$ | $\langle\tilde Q\rangle=\langle\tilde Q,\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^{2}$ | the general plain bilinear form | $\mathbb{C}$ | $\mathrm E$ | $(4,4)$ | complex cone | no | — |
| $\langle\cdot\rangle_{*}$ | $\langle\cdot,\cdot\rangle_{*}$ | $\langle\tilde Q\rangle_{*}=\langle\tilde Q,\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ | the general plain sesquilinear form, the Hermitian form | $\mathbb{R}$ | $\mathrm I_4$ | $(8,0)$ | $\{0\}$ | no | **yes** |
| $\langle\cdot\rangle_{\natural}$ | $\langle\cdot,\cdot\rangle_{\natural}$ | $\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ | the general quaternionic bilinear form | $\mathbb{C}$ | $\mathrm I_4$ | $(4,4)$ | $\mathcal N$, the zero divisors | **yes** | — |
| $\langle\cdot\rangle_{\natural*}$ | $\langle\cdot,\cdot\rangle_{\natural*}$ | $\langle\tilde Q\rangle_{\natural*}=\langle\tilde Q,\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$ | the general quaternionic sesquilinear form, the Krein form | $\mathbb{R}$ | $\mathrm E$ | $(2,6)$ | $\mathcal K$ | no | no |

The table separates the four by the field of their values, by the Gram matrix and the signature of their pairing, by their vanishing set, and by the two properties that single out one algebraic norm each: definiteness for $\langle\cdot\rangle_{*}$, multiplicativity for $\langle\cdot\rangle_{\natural}$.


## What the Four Algebraic Norms Separate

**Proposition (no algebraic norm is both definite and multiplicative).** No function on $\mathbb{B}$ is both definite and multiplicative.

*Proof.* The algebra has zero divisors, $(e_t+i\vec e_x)(e_t-i\vec e_x)=0$ with $e_t\pm i\vec e_x\neq0$ and $\langle e_t\pm i\vec e_x\rangle_{\natural}=1+i^{2}=0$. A multiplicative function $\varphi$ would give $\varphi(e_t+i\vec e_x)\varphi(e_t-i\vec e_x)=\varphi(0)=0$, so one of the two values is zero, on a nonzero element; a definite function is nonzero off the origin. No function is both.

**Corollary.** $\langle\cdot\rangle_{*}$ is definite and not multiplicative; $\langle\cdot\rangle_{\natural}$ is multiplicative and not definite; and no third algebraic norm of the four repairs the split. The multiplicative one and the definite one are different objects, and that difference is the failure of the biquaternions to be a normed division algebra — the four normed division algebras $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, $\mathbb{O}$ of the Hurwitz theorem are exactly the ones in which the two senses coincide.

**Proposition (only $\langle\cdot\rangle_{\natural}$ is multiplicative).** Of the four algebraic norms, $\langle\cdot\rangle_{\natural}$ alone satisfies $\varphi(\tilde Q_1\tilde Q_2)=\varphi(\tilde Q_1)\varphi(\tilde Q_2)$.

*Proof.* $\langle\cdot\rangle_{\natural}$ is multiplicative by the proposition of its section. The other three are not, each refuted by one substitution. For $\langle\cdot\rangle$: $\langle \vec e_x\vec e_y\rangle=\langle \vec e_z\rangle=-1$ while $\langle \vec e_x\rangle\langle \vec e_y\rangle=(-1)(-1)=1$. For $\langle\cdot\rangle_{*}$: $\langle \vec e_x+i\vec e_y\rangle_{*}=1+1=2$ while $(\vec e_x+i\vec e_y)^{2}=\vec e_x^{2}+(i\vec e_y)^{2}=-e_t+e_t=0$ and $\langle 0\rangle_{*}=0$. For $\langle\cdot\rangle_{\natural*}$: $\langle e_t+\vec e_x\rangle_{\natural*}=1-1=0$ while $(e_t+\vec e_x)^{2}=e_t^{2}+e_t\vec e_x+\vec e_xe_t+\vec e_x^{2}=-e_t+\vec e_x-\vec e_x-e_t=-2e_t$ and $\langle -2e_t\rangle_{\natural*}=4$.

**Remark (the two senses of *norm*).** Two different things carry the name. The **algebraic norm** of this article is a map into the ring — $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural}$ into $\mathbb{C}$, $\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\natural*}$ into $\mathbb{R}$ — and it is algebra: algebraic norms, quadratic forms, polarisations, zero divisors. The **topological norm** is the one selection of positive real values, $\lVert\tilde Q\rVert_E=\bigl(\langle\tilde Q\rangle_{*}\bigr)^{1/2}$, and it is topology: distance, balls, convergence, completeness. Only $\langle\cdot\rangle_{*}$ of the four yields it, because only $\langle\cdot\rangle_{*}$ is real and definite; $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural}$ are complex-valued, and $\langle\cdot\rangle_{\natural*}$ is real but indefinite. The two senses are the two layers of *Introduction to Mathematics*, and no third function holds them together.

**Remark (the four collapse to two on real elements).** For real $\tilde Q_1,\tilde Q_2$ the coefficientwise conjugation is the identity, so $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\langle\tilde Q_1,\tilde Q_2\rangle$ and $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$. On the real part of the space the four algebraic norms are the two, $\langle\cdot\rangle=\langle\cdot\rangle_{\natural*}$ and $\langle\cdot\rangle_{\natural}=\langle\cdot\rangle_{*}$, and the four operations of the two bilinear rows and of the two sesquilinear rows coincide there. This is the real-form caution of *Symmetric and Antisymmetric Decomposition of the Four General Products* read at the two equal arguments: a computation restricted to real elements sees two algebraic norms and hides the other two. On the remarkable real subspaces the four algebraic norms restrict to the two real forms in the same way, and the restrictions, their signatures and the definiteness of each on each are the subject of *Remarkable Subspaces and the Four Algebraic Norms*.


## Summary

The twelve products of *Symmetric and Antisymmetric Decomposition of the Four General Products* carry four forms and no more: the symmetrisation of a family keeps the scalar part and the antisymmetrisation kills it, so the eight operations of the four $\mathrm G/\mathrm S$ rows carry the four forms two by two and the four antisymmetric operations carry the zero form. The four forms are the scalar parts of the four general products, written with the one bracket whose subscript records the pair and named the general plain bilinear, the general plain sesquilinear — the Hermitian —, the general quaternionic bilinear, and the general quaternionic sesquilinear — the Krein — form.

The second slot of the general product decides the symmetry, bilinear or sesquilinear, and so whether the algebraic norm is complex or real; the first slot decides the Gram matrix, the identity or the sign matrix, and so the signature of the algebraic norm and its definiteness on the sectors. The four are indexed by the two-by-two grid of the two slots.

The same two slots read on the groups that preserve the four forms: the second slot decides whether the group is orthogonal or unitary, the first slot which orthogonal or unitary form, so that the four groups are $O_4(\mathbb{C})$, $\mathrm{U}(4)$, $O_4(\mathbb{C})$ and $\mathrm{U}(1,3)$, of real dimensions $12$, $16$, $12$ and $16$, and the natural conjugation lies in all four. The general plain bilinear form carries one further structure, the hyperbolic one: the four elements $h_1=e_t+\vec e_x$, $h_2=\tfrac12(e_t-\vec e_x)$, $h_3=\vec e_y+i\vec e_z$ and $h_4=\tfrac12(i\vec e_z-\vec e_y)$ are isotropic with the only non-zero pairings $\langle h_1,h_2\rangle=\langle h_3,h_4\rangle=1$, so that $\langle\cdot,\cdot\rangle$ is the orthogonal sum of the two hyperbolic planes $\operatorname{span}\{e_t,\vec e_x\}$ and $\operatorname{span}\{\vec e_y,\vec e_z\}$, of index $2$ over $\mathbb{C}$ and $4$ over $\mathbb{R}$.

Read at their two equal arguments, the four forms give the four algebraic norms $\langle\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^{2}$, $\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$, $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ and $\langle\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$, each attained by two operations, the general product and its symmetrisation of the same family, while the four antisymmetrisations carry the vanishing algebraic norm. $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural}$ are complex-valued and $\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\natural*}$ real-valued. $\langle\cdot\rangle_{\natural}$ is the multiplicative one, the reduced norm and the criterion of invertibility; $\langle\cdot\rangle_{*}$ is the definite one, and its square root is the unique topological norm of the space; $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural*}$ are the two indefinite ones of the plain and of the Krein form. Multiplicativity and definiteness are held by no single one of the four, and the zero divisors are the reason.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde Q_1,\tilde Q_2\rangle$ | the general plain bilinear form, $\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, symmetric, Gram $\mathrm E$ |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$ | the general plain sesquilinear form, the Hermitian form, $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$, definite at the two equal arguments |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$, symmetric, Gram $\mathrm I_4$ |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$ | the general quaternionic sesquilinear form, the Krein form, $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})$, indefinite at the two equal arguments |
| $(\mathrm{id},\mathrm{id})$, $(\mathrm{id},{}^{*})$, $({}^{\natural},\mathrm{id})$, $({}^{\natural},{}^{*})$ | the four pairs, the subscript of each bracket |
| $\varepsilon=(1,-1,-1,-1)$ | the sign vector of the natural conjugation, which the first slot applies |
| $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$ | the Gram matrix of $\langle\cdot,\cdot\rangle$ and of $\langle\cdot,\cdot\rangle_{\natural*}$; $\mathrm I_4$ is the Gram matrix of $\langle\cdot,\cdot\rangle_{*}$ and of $\langle\cdot,\cdot\rangle_{\natural}$ |
| $(4,4)$, $(8,0)$, $(4,4)$, $(2,6)$ | the signatures of the realifications of $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{\natural*}$ |
| $O_4(\mathbb{C})$, $\mathrm{U}(4)$, $O_4(\mathbb{C})$, $\mathrm{U}(1,3)$ | the groups preserving the four forms, of real dimensions $12$, $16$, $12$, $16$ |
| $h_1,\dots,h_4$ | the hyperbolic basis of $\langle\cdot,\cdot\rangle$ |
| the complex cone, $\mathcal N$, $\mathcal K$ | the null sets of $\langle\cdot,\cdot\rangle$, of $\langle\cdot,\cdot\rangle_{\natural}$ and of $\langle\cdot,\cdot\rangle_{\natural*}$; that of $\langle\cdot,\cdot\rangle_{*}$ is the origin |
| $\langle\tilde Q\rangle=\langle\tilde Q,\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^{2}$ | the general plain bilinear algebraic norm, the plain norm |
| $\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ | the general plain sesquilinear algebraic norm, the Hermitian norm; definite, $\lVert\tilde Q\rVert_E^{2}$ |
| $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ | the general quaternionic bilinear algebraic norm, the quaternionic norm; multiplicative, the reduced norm |
| $\langle\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$ | the general quaternionic sesquilinear algebraic norm, the Krein norm |
| $\varphi(\tilde Q)=\varphi(\tilde Q,\tilde Q)$ | one bracket, two arities: two arguments give the form, one argument the algebraic norm |
| $\lVert\tilde Q\rVert_E$ | the Euclidean norm, the square root of $\langle\cdot\rangle_{*}$, the unique topological norm |

## Further Reading

- [The Four General Products and Their Relations](the-four-general-products-and-their-relations.html), for the four general products whose scalar parts the four forms are, their relations and their comparison.
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the twelve products, their scalar parts and their two-slot construction, on which the count of four forms rests.
- [Conventions in the Biquaternion Universe](../articles_physics/conventions-in-the-biquaternion-universe.html), for the convention of the four pairings — the one bracket, the four names, the four pairs and the trace forms.
- [The Group of Involutions](the-group-of-involutions.html), for the four conjugations that index the four forms and the group they form.
- [Introduction to the Operators of the Biquaternion Algebra](the-four-general-products-and-operators.html) and [The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples](the-four-adjoints-of-the-two-algebras-and-the-two-sesqualgebras-in-examples.html), for the four adjoints of a left multiplication under the four forms.
- [Bilinear Forms](bilinear-forms.html), [Quadratic Forms and Polarisation](quadratic-forms-and-polarisation.html), [Hermitian Forms and Unitary Geometry](hermitian-forms-and-unitary-geometry.html) and [Matrix Groups and Classical Groups](matrix-groups-and-classical-groups.html), for the general theory of a bilinear or sesquilinear form, its Gram matrix, its hyperbolic decomposition and the classical group that preserves it.
- [Remarkable Subspaces and the Four Forms](remarkable-subspaces-and-the-four-forms.html), for the four forms read on the remarkable subspaces.
- [Remarkable Subspaces and the Four Algebraic Norms](remarkable-subspaces-and-the-four-algebraic-norms.html), for the restriction of the four algebraic norms to the remarkable subspaces.
- [Norm and Invertibility in the General Quaternionic Algebra](norm-and-invertibility-in-the-general-quaternionic-algebra.html), for the multiplicative algebraic norm, the zero divisors and the criterion of invertibility.
- [Topology and Metric for Each of the Twelve Operations](topology-and-metric-for-each-of-the-twelve-operations.html), for the one topology and the one Euclidean norm of the space.
- [The Norm Defined by a Form](the-norm-defined-by-a-form.html), [Hermitian Forms over Algebras and Norms](hermitian-forms-over-algebras-and-norms.html) and [Introduction to Mathematics](introduction-to-mathematics.html), for the distinction between the algebraic norm and the topological norm.
