# __The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra__

## Introduction

The four **forms** are the scalar parts of the four general products, $\varphi(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}\,f(\tilde Q_1,\tilde Q_2)$, and, read at their two equal arguments, they give four **algebraic norms**, $\varphi(\tilde Q)=\varphi(\tilde Q,\tilde Q)$. The twelve products of *Symmetric and Antisymmetric Decomposition of the Four General Products* carry these four and no more: the symmetrisation of a family keeps the scalar part and the antisymmetrisation kills it, so the eight operations of the four $\mathrm G/\mathrm S$ rows carry the four forms two by two and the four antisymmetric operations carry the zero form.

This article defines the four forms, writes them on the coordinates, tabulates them, reads the groups that preserve each, and states what the four separate. It then passes to the four algebraic norms: their definition as the diagonal of a form, the proof that the twelve operations carry exactly four, their coordinates, their table and what they separate — among it the multiplicativity of the quaternionic one, the definiteness of the Hermitian algebraic norm and the impossibility of one function being both. The four carry the letters $P$, $N$, $H$ and $K$, and the article closes with the four qualified notions of a regular and a degenerate biquaternion.

The four forms are the scalar parts of the four general products of *The Four General Products and Their Relations over the Biquaternion Algebra*, which owns the products, their relations and their comparison. The distinction between the algebraic norm, whose value is an element of the ring, and the topological norm, whose value is a positive real, is *The Norm Defined by a Form*; the one topological norm of the space is the square root of the Hermitian algebraic norm.

## Notational Conventions

$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the biquaternion algebra, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, $e_t=1$, $\vec e_k^{2}=-e_t$, and central scalar imaginary $i$, $i^{2}=-1$. A general element is $\tilde Q_2=\sum_{\mu\in\{t,x,y,z\}}Q_{2,\mu} e_\mu$ with $Q_{2,\mu}\in\mathbb{C}$, written in the centre–vector split $\tilde Q_2=c+v$ with $c=Q_{2t}e_t\in\mathbb{C}_{\mathbb{B}}$ and $v=\sum_{k=1}^{3}Q_{2,k}\vec e_k\in\mathrm{Vect}(\mathbb{B})$. The scalar part is $\mathrm{Sc}$, the coefficientwise conjugation is $\bar{\cdot}$, the natural conjugation is ${}^{\natural}$, with $Q^{\natural}_\nu=\varepsilon_\nu Q_{2,\nu}$, and the Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$. The sign vector is $\varepsilon=(1,-1,-1,-1)$, and $\mathbb{B}$ is identified with $\mathbb{C}^{4}$ by $\tilde Q_2\mapsto(Q_{2t},Q_{2x},Q_{2y},Q_{2z})$. The vector parts carry the complex bilinear dot product $(\vec Q_1,\vec Q_2)=\sum_{k=1}^{3}Q_{1,k}Q_{2,k}$ and the cross product $\vec Q_1\times\vec Q_2$. The four forms are $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$; their names, brackets and pairs are the convention of *Conventions in the Biquaternion Universe*, which reads the four on the algebra and on the six remarkable subspaces. Each carries one letter: $P$ the plain, $N$ the quaternionic, $H$ the Hermitian and $K$ the Krein. One letter serves the two arities, $P(\tilde Q_1,\tilde Q_2)$ for the form and $P(\tilde Q)$ for the algebraic norm, and the same holds for the other three. The plain form is written $P$ and not $B$ because $B$ is already the complex modulus of the vector part, $B^{2}=\sum_k Q_k^{2}$, and $B(\tilde Q)$ is the right annihilator $\ker R_{\tilde Q}$ of the plain product. $\langle\cdot,\cdot\rangle_{*}$ is also the Hermitian form and $\langle\cdot,\cdot\rangle_{\natural*}$ the Krein form, and the brackets $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural*}$ are the short names of this article. A form is $\mathbb{C}$-**bilinear** when its second slot is read without the star, so that a scalar pulls out of it, and **sesquilinear** when the second slot is read with the star, so that the scalar pulls out conjugated. The Euclidean norm is $\lVert\tilde Q_2\rVert_E=\bigl(\sum_\mu\lvert Q_{2,\mu}\rvert^{2}\bigr)^{1/2}$, the square root of the algebraic norm of $\langle\cdot\rangle_{*}$.


## The Form of an Operation

**Definition (the form of an operation).** Let $f$ be an operation on $\mathbb{B}$ with scalar part $\varphi(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}\,f(\tilde Q_1,\tilde Q_2)$. The **form of the operation $f$** is $\varphi$. It is bilinear when the second slot of $f$ is read without the star, sesquilinear when it is read with the star. In both cases the value lies in $\mathbb{C}$, the conjugation of the second slot entering the value; a sesquilinear form is conjugate-symmetric, $\varphi(\tilde Q_1,\tilde Q_2)=\overline{\varphi(\tilde Q_2,\tilde Q_1)}$, so that its algebraic norm is real. For an operation whose scalar part vanishes identically the form is the zero form.

The definition is the one of *Introduction to Mathematics*: the form is the degree-two object attached to a product, it is a function of two elements, and the algebraic norm is that form at its two equal arguments, a function of one. The four forms of the biquaternion algebra are then the four functions of the introduction, $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$, read on the third column of the table of the twelve.


## The Four Forms

The four forms are the scalar parts of the four general products, one to each pair of slots:

$$
\boxed{\;
P(\tilde Q_1,\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2),\qquad
N(\tilde Q_1,\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2),\qquad
H(\tilde Q_1,\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*}),\qquad
K(\tilde Q_1,\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})
\;}.
$$

Each is written on the coordinates of a pair, with its Gram matrix and its signature.

### The General Plain Bilinear Form

**The plain form, written $P$.**

$$
P(\tilde Q_1,\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)=Q_{1,0}Q_{2t}-(\vec Q_1,\vec Q_2),
$$

the scalar part of the general plain bilinear product. It is symmetric, $\mathbb{C}$-bilinear and complex-valued, its Gram matrix on the coefficient basis is the sign matrix $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$, and its realification is of signature $(4,4)$. It is non-degenerate. Its null set, the set of $\tilde Q$ with $\langle\tilde Q,\tilde Q\rangle=0$, is the complex cone $\sum_\mu\varepsilon_\mu Q_\mu^{2}=0$, of real dimension six, and it is neither the zero-divisor cone nor the null cone. On the anti-Hermitian subspace its algebraic norm is negative definite, and on the Hermitian subspace positive definite.

### The General Quaternionic Bilinear Form

**The quaternionic form, written $N$.**

$$
N(\tilde Q_1,\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)=Q_{1,0}Q_{2t}+(\vec Q_1,\vec Q_2),
$$

the scalar part of the general quaternionic bilinear product: the same form as $\langle\cdot,\cdot\rangle$ read through the natural conjugation of the first slot, differing from it by the sign of the vector part alone. It is symmetric, $\mathbb{C}$-bilinear and complex-valued, its Gram matrix is the identity $\mathrm I_4$, and its realification is of signature $(4,4)$. It is non-degenerate. Its null set is the zero-divisor cone $\mathcal N=\{\langle\tilde Q,\tilde Q\rangle_{\natural}=0\}$, of real dimension six, the null cone. Its algebraic norm is the **interval**, the quadratic form $Q_t^{2}+(\vec Q,\vec Q)$, and the pair of the first slot is what gives the square the positive sign on the vector part.

### The General Plain Sesquilinear Form, the Hermitian Form

**The Hermitian form, written $H$.**

$$
H(\tilde Q_1,\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=Q_{1,0}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2}),
$$

the scalar part of the general plain sesquilinear product. It is conjugate-symmetric, $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\overline{\langle\tilde Q_2,\tilde Q_1\rangle_{*}}$, sesquilinear in the second slot, and its algebraic norm is real and positive definite, $\langle\tilde Q_2,\tilde Q_2\rangle_{*}>0$ for $\tilde Q_2\neq0$; its Gram matrix is $\mathrm I_4$ and its realification is of signature $(8,0)$. It is non-degenerate, and its null set is the origin alone, so it has no cone. Its algebraic norm is the square of the unique topological norm of the space, $\lVert\tilde Q_2\rVert_E^{2}$.

### The General Quaternionic Sesquilinear Form, the Krein Form

**The Krein form, written $K$.**

$$
K(\tilde Q_1,\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})=Q_{1,0}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2}),
$$

the scalar part of the general quaternionic sesquilinear product: the same form as $\langle\cdot,\cdot\rangle_{*}$ read through the natural conjugation of the first slot, differing from it by the sign of the vector part alone. It is conjugate-symmetric and sesquilinear, its algebraic norm is real and indefinite, its Gram matrix is the sign matrix $\mathrm E$, and its realification is of signature $(2,6)$. It is non-degenerate, and its null set is the real cone $\mathcal K$, the null cone of the Krein form. It is indefinite, of mixed signature on every subspace.


## The Table of the Four Forms

| Full form name | Reduced name | Letter | Bracket | Expression with $\mathrm{Sc}$ | Coordinates | Gram | Signature over $\mathbb{R}$ | Null set | Algebraic norm lands in |
|---|---|---|---|---|---|---|---|---|---|
| The general plain bilinear form | **Plain Form** | $P$ | $\langle\cdot,\cdot\rangle$ | $\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | $Q_{1,0}Q_{2t}-(\vec Q_1,\vec Q_2)$ | $\mathrm E$ | $(4,4)$ | the complex cone | $\mathbb{C}$ |
| The general quaternionic bilinear form | **Quaternionic Form** | $N$ | $\langle\cdot,\cdot\rangle_{\natural}$ | $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$ | $Q_{1,0}Q_{2t}+(\vec Q_1,\vec Q_2)$ | $\mathrm I_4$ | $(4,4)$ | $\mathcal N$, the $N$-degenerate set, the zero-divisor cone | $\mathbb{C}$ |
| The general plain sesquilinear form | **Hermitian Form** | $H$ | $\langle\cdot,\cdot\rangle_{*}$ | $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ | $Q_{1,0}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$ | $\mathrm I_4$ | $(8,0)$ | $\{0\}$ | $\mathbb{R}$ |
| The general quaternionic sesquilinear form | **Krein Form** | $K$ | $\langle\cdot,\cdot\rangle_{\natural*}$ | $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})$ | $Q_{1,0}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})$ | $\mathrm E$ | $(2,6)$ | $\mathcal K$ | $\mathbb{R}$ |

The table separates the four by their letter, their bracket and the product under $\mathrm{Sc}$, by the Gram matrix and the signature of the realification of their algebraic norm, by their null set, and by the field in which the algebraic norm lands — complex for the two bilinear forms and real for the two sesquilinear ones, the conjugating second slot being what makes a algebraic norm real.


## Why the Other Eight Operations Add No New Form

The four forms are the scalar parts of the four general products, and the eight remaining operations of *Symmetric and Antisymmetric Decomposition of the Four General Products* add none: a symmetric part keeps the scalar part of its general product and an antisymmetric part loses it.

**Lemma.** For a general product $f$ with parts $f^{\mathrm s}$ and $f^{\mathrm a}$, $\mathrm{Sc}\,f^{\mathrm s}=\mathrm{Sc}\,f$ and $\mathrm{Sc}\,f^{\mathrm a}=0$.

*Proof.* For the two bilinear families $\mathrm{Sc}$ is commutative, so the half-sum equals $\mathrm{Sc}\,f$ and the half-difference vanishes. For the two sesquilinear families the exchange is the conjugate transpose, and the value it pairs with $f(\tilde Q_1,\tilde Q_2)$ has the same scalar part, $\mathrm{Sc}\,\overline{f(\tilde Q_2,\tilde Q_1)}=\mathrm{Sc}\,f(\tilde Q_1,\tilde Q_2)$; the half-sum therefore keeps the scalar part and the half-difference kills it.

**Proposition.** The twelve operations carry exactly four non-zero forms, each shared by a general product and its symmetric part: $\langle\cdot,\cdot\rangle$ on $\mathrm{GPA}$ and $\mathrm{SPA}$, $\langle\cdot,\cdot\rangle_{\natural}$ on $\mathrm{GQA}$ and $\mathrm{SQA}$, $\langle\cdot,\cdot\rangle_{*}$ on $\mathrm{GPS}$ and $\mathrm{SPS}$, and $\langle\cdot,\cdot\rangle_{\natural*}$ on $\mathrm{GQS}$ and $\mathrm{SQS}$; the four antisymmetric operations carry the zero form.

*Proof.* The lemma gives the first clause. The four are distinct: at $\tilde Q_1=\vec e_x$ and $\tilde Q_2=\vec e_x+i\vec e_x$ they take the four different values $-(1+i)$, $1+i$, $-(1-i)$ and $1-i$.

**Remark.** The zero form is not counted as a fifth: the four antisymmetric operations have zero scalar part and their values lie in the vector subspace, so the form they carry is the zero form. The alternating parts of the two Hermitian forms are not scalar parts of these operations; they are read in *Remarkable Subspaces and the Four General Products, Forms and Norms*, §*The Alternating Forms on the Whole Space*.

## The Isometry Groups of the Four Forms

A $\mathbb{C}$-linear operator $T$ **preserves** a form $\varphi$ when $\varphi(T\tilde Q_1,T\tilde Q_2)=\varphi(\tilde Q_1,\tilde Q_2)$ for every pair, and the preserving operators form a group, the **isometry group** $\mathrm{Isom}(\varphi)$. The four forms are separated by their four groups, and the four groups are classical.

**Theorem (the four isometry groups).** The $\mathbb{C}$-linear operators preserving the four forms are, in the coefficient basis,

$$
\boxed{\;
\begin{array}{l}
\mathrm{Isom}(\langle\cdot,\cdot\rangle)=\{T:T^{\mathsf T}\mathrm E T=\mathrm E\}=O_4(\mathbb{C}),\qquad
\mathrm{Isom}(\langle\cdot,\cdot\rangle_{\natural})=\{T:T^{\mathsf T}T=\mathrm I_4\}=O_4(\mathbb{C}),\\[2pt]
\mathrm{Isom}(\langle\cdot,\cdot\rangle_{*})=\{T:T^{*}T=\mathrm I_4\}=\mathrm{U}(4),\qquad
\mathrm{Isom}(\langle\cdot,\cdot\rangle_{\natural*})=\{T:T^{*}\mathrm E T=\mathrm E\}=\mathrm{U}(1,3).
\end{array}
\;}
$$

of real dimensions $12$, $12$, $16$ and $16$.

*Proof.* A form with Gram matrix $G$ is preserved by a $\mathbb{C}$-linear $T$ exactly when $T^{\mathsf T}GT=G$ in the bilinear case and $T^{*}GT=G$ in the Hermitian case, $T^{\mathsf T}$ the transpose and $T^{*}$ the conjugate transpose. With $G=\mathrm I_4$ these are the defining equations of the complex orthogonal group $O_4(\mathbb{C})$ and of the unitary group $\mathrm{U}(4)$. With $G=\mathrm E$ the sign matrix is congruent to the identity over $\mathbb{C}$, $\mathrm E=(S^{-1})^{\mathsf T}S^{-1}$ for $S=\operatorname{diag}(1,i,i,i)$, so that $T$ preserves $\langle\cdot,\cdot\rangle$ exactly when $STS^{-1}$ is orthogonal and $T$ preserves $\langle\cdot,\cdot\rangle_{\natural*}$ exactly when $STS^{-1}$ is unitary; the two groups with $\mathrm E$ are conjugates of the two groups with $\mathrm I_4$, and this is why the same name $O_4(\mathbb{C})$ serves both bilinear forms and why the second group is written $\mathrm{U}(1,3)$. The dimensions are the classical ones, $\dim_{\mathbb{R}}O_4(\mathbb{C})=12$ and $\dim_{\mathbb{R}}\mathrm{U}(4)=\dim_{\mathbb{R}}\mathrm{U}(1,3)=16$, and they were recomputed as the dimensions of the four Lie algebras $\{X:X^{\mathsf T}G+GX=0\}$.

**Remark (the two slots read on the groups).** The **second slot** decides whether the group is **orthogonal** or **unitary**, since it decides whether the form is bilinear or Hermitian; the **first slot** decides **which** orthogonal or unitary form, the sign matrix $\mathrm E$ against the identity $\mathrm I_4$ — the same division of labour that §*What the Four Forms Separate* reads on the symmetry and the signature.

**Remark (the natural conjugation lies in all four).** The natural conjugation is the operator $\mathrm E$ in the coefficient basis, and $\mathrm E$ preserves each of the four forms, since $\mathrm E^{\mathsf T}\mathrm E\,\mathrm E=\mathrm E$ and $\mathrm E^{*}\mathrm E\,\mathrm E=\mathrm E$ with $\mathrm E^{2}=\mathrm I_4$; the fundamental symmetry of the algebra therefore sits in all four groups of the theorem.


## The Two Slots

**The mechanism.** A form is obtained from a product by reading the first factor either as it stands or through the natural conjugation ${}^{\natural}$, and the second factor either as it stands or through the star ${}^{*}$; nothing else varies. The four forms are therefore indexed by a two-by-two grid, and the grid is the whole of the subject. The mechanism and the laws are shared with *The Four General Products and Their Relations over the Biquaternion Algebra*, and the signature table of the four on the remarkable subspaces is that of *Remarkable Subspaces and the Four General Products, Forms and Norms*.

**What each slot decides.**

- The **second slot** decides whether the form is a **composition** or a **pairing**. Read without the star the form is bilinear and symmetric and can be iterated; read with the star it is sesquilinear and conjugate-symmetric and can only be evaluated. It is the slot that separates the two bilinear forms from the two sesquilinear ones, and it is what makes the algebraic norm of a sesquilinear form real.
- The **first slot** decides the **Gram matrix** and the **signature**, and through them **definiteness on each subspace**. Read as it stands the form is $\langle\cdot,\cdot\rangle$ or $\langle\cdot,\cdot\rangle_{*}$; read through the natural conjugation it is $\langle\cdot,\cdot\rangle_{\natural}$ or $\langle\cdot,\cdot\rangle_{\natural*}$. Since the natural conjugation multiplies the vector part by $-1$, the first slot toggles the coefficient $\varepsilon$ of the vector part and so turns the sign matrix $\mathrm E$ into the identity $\mathrm I_4$.


## What the Four Forms Separate

**Proposition (no two of the four agree).** No two of the four forms are equal as functions of two elements.

*Proof.* On $\tilde Q_1=\vec e_x$, $\tilde Q_2=\vec e_x+i\vec e_x$ the four values are $-(1+i)$, $1+i$, $-(1-i)$ and $1-i$, four different complex numbers, as in the proposition of §*Why the Other Eight Operations Add No New Form*.

**The second slot gives the symmetry, the first slot the signature.** The four forms fall into two pairs by symmetry, $\{\langle\cdot,\cdot\rangle,\langle\cdot,\cdot\rangle_{\natural}\}$ bilinear and $\{\langle\cdot,\cdot\rangle_{*},\langle\cdot,\cdot\rangle_{\natural*}\}$ sesquilinear, and into two other pairs by Gram matrix, $\{\langle\cdot,\cdot\rangle,\langle\cdot,\cdot\rangle_{\natural*}\}$ of Gram $\mathrm E$ and $\{\langle\cdot,\cdot\rangle_{*},\langle\cdot,\cdot\rangle_{\natural}\}$ of Gram $\mathrm I_4$. The two divisions are independent, and their product is the four: each form is the intersection of one symmetry with one Gram matrix, which is the two-by-two grid of the two slots.

**The four collapse to two on real elements.** For real $\tilde Q_1,\tilde Q_2$ the coefficientwise conjugation is the identity, so $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\langle\tilde Q_1,\tilde Q_2\rangle$ and $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$. On the real part of the space the four forms are the two, and only the two slots together, not the complex structure, separate them.

**The null sets are four.** The null set of $\langle\cdot,\cdot\rangle$ is the complex cone, that of $\langle\cdot,\cdot\rangle_{\natural}$ the zero-divisor cone $\mathcal N$ — the null cone —, that of $\langle\cdot,\cdot\rangle_{*}$ the origin alone, and that of $\langle\cdot,\cdot\rangle_{\natural*}$ the real cone $\mathcal K$. Three of the four are cones: the complex cone and the zero-divisor cone, of real dimension six, and the Krein cone, of real dimension seven. The two of dimension six do not agree, so the complex cone of $\langle\cdot,\cdot\rangle$ is not the null cone of $\langle\cdot,\cdot\rangle_{\natural}$; the fourth null set is the origin, so the algebraic norm of $\langle\cdot\rangle_{*}$ is definite and has no cone.


## The Algebraic Norm of an Operation

**Definition (algebraic norm).** Let $f$ be an operation on $\mathbb{B}$ with scalar-part form $\varphi(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}\,f(\tilde Q_1,\tilde Q_2)$. The **algebraic norm of the operation $f$** is the algebraic norm

$$
\varphi(\tilde Q)=\varphi(\tilde Q,\tilde Q),
$$

a function of one element taking its value in $\mathbb{C}$ when $f$ is $\mathbb{C}$-bilinear and in $\mathbb{R}$ when $f$ is Hermitian. For an operation whose scalar part vanishes identically the algebraic norm is the zero function.

The definition is the one of *Introduction to Mathematics*: the algebraic norm is the quadratic form $\mathfrak{Q}(x)=\langle x,x\rangle$ read at the two equal arguments of a form, valued in the ring. It records the size of an element only in the sense of the ring; it is not a distance, and it becomes a distance only when it is selected to take positive real values.

The four algebraic norms of the biquaternion algebra are then the four functions of the introduction, $\langle\cdot\rangle$, $\langle\cdot\rangle_{\natural}$, $\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\natural*}$: the four algebraic norms of the four forms of this article.


## From the Four Forms to the Four Algebraic Norms

The count of the four is taken, one step, in §*Why the Other Eight Operations Add No New Form*, above: the symmetrisation of a family keeps the scalar part and the antisymmetrisation kills it, so the eight operations of the four $\mathrm G/\mathrm S$ rows carry the four forms two by two and the four antisymmetric operations carry the zero form. The twelve products are named in the three-letter code defined in *Symmetric and Antisymmetric Decomposition of the Four General Products* — the general, symmetric and antisymmetric operation of each family, the plain and quaternionic family lettered $\mathrm P$ and $\mathrm Q$ and the algebra and sesqualgebra lettered $\mathrm A$ and $\mathrm S$, so that the twelve are $\mathrm{GPA}$, $\mathrm{GPS}$, $\mathrm{GQA}$, $\mathrm{GQS}$ the four general, $\mathrm{SPA}$, $\mathrm{SPS}$, $\mathrm{SQA}$, $\mathrm{SQS}$ the four symmetric and $\mathrm{APA}$, $\mathrm{APS}$, $\mathrm{AQA}$, $\mathrm{AQS}$ the four antisymmetric.

**Proposition (the twelve operations carry four algebraic norms).** The twelve operations have exactly four distinct non-zero algebraic norms, the four algebraic norms above, each attained by two operations, and four operations have the zero algebraic norm.

*Proof.* The algebraic norm is the form at the two equal arguments, so the count of the four algebraic norms is the count of the four forms, which is the proposition of §*Why the Other Eight Operations Add No New Form*, above; the symmetrisation of a family therefore carries the same algebraic norm as the general product and the antisymmetrisation the zero one. Hence the algebraic norms of the twelve are those of the four general products, each on the two operations $\mathrm G$ and $\mathrm S$ of its family: $\langle\cdot\rangle$ on $\mathrm{GPA}$ and $\mathrm{SPA}$, $\langle\cdot\rangle_{\natural}$ on $\mathrm{GQA}$ and $\mathrm{SQA}$, $\langle\cdot\rangle_{*}$ on $\mathrm{GPS}$ and $\mathrm{SPS}$, $\langle\cdot\rangle_{\natural*}$ on $\mathrm{GQS}$ and $\mathrm{SQS}$; and $0$ on $\mathrm{APA}$, $\mathrm{APS}$, $\mathrm{AQA}$ and $\mathrm{AQS}$. The four are distinct as functions of one element: on $\vec e_x$ and on $ie_t$ their value pairs are

$$
(-1,-1),\qquad(1,-1),\qquad(1,1),\qquad(-1,1),
$$

which are four different pairs.

**Remark (a vanishing form carries no algebraic norm).** The four antisymmetric operations have the zero algebraic norm because their scalar part is identically zero and every value lies in the vector subspace. A vanishing quadratic form is not an algebraic norm, and its vanishing set is the whole space, so the four operations are counted with no algebraic norm rather than with a zero one.


## The Four Algebraic Norms

Each algebraic norm is the diagonal of its form:

$$
\boxed{\;
P(\tilde Q)=\langle\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^{2},\qquad
N(\tilde Q)=\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2},\qquad
H(\tilde Q)=\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2},\qquad
K(\tilde Q)=\langle\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}
\;}.
$$

Each is written on the coordinates of one element, with its value ring, its Gram matrix and its signature.

### The General Plain Bilinear Algebraic Norm

**The plain norm, written $P$.**

$$
P(\tilde Q)=\langle\tilde Q\rangle=\langle\tilde Q,\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^{2}=Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2},
$$

the general plain bilinear algebraic norm $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)=Q_{1,0}Q_{2t}-(\vec Q_1,\vec Q_2)$. It is complex-valued and $\mathbb{C}$-quadratic, its Gram matrix on the coefficient basis is the sign matrix $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$, and its realification is of signature $(4,4)$. Its vanishing set is the complex cone $\langle\tilde Q\rangle=0$, already the complex quadric of §*The Four Forms*, above. It is not multiplicative. The algebraic norm is that of the **plain product**, the multiplication of the algebra, and it is the one algebraic norm the plain product carries.

### The General Quaternionic Bilinear Algebraic Norm

**The quaternionic norm, written $N$.**

$$
N(\tilde Q)=\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2},
$$

the general quaternionic bilinear algebraic norm $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)=Q_{1,0}Q_{2t}+(\vec Q_1,\vec Q_2)$. It is complex-valued, its Gram matrix is the identity $\mathrm I_4$, and its realification is of signature $(4,4)$. Its vanishing set is the zero-divisor cone $\mathcal N=\{\langle\tilde Q\rangle_{\natural}=0\}$, of real dimension $6$, and the algebraic norm is the reason $\mathbb{B}$ has zero divisors at all.

**Proposition (multiplicativity).** $\langle\cdot\rangle_{\natural}$ is multiplicative:
$$
\boxed{\;
\langle\tilde Q_1\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1\rangle_{\natural}\,\langle\tilde Q_2\rangle_{\natural}
\;}.
$$

*Proof.* Under the matrix representation $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$, $\mathsf{M}_2(\vec e_k)=-i\sigma_k$, the algebraic norm is the determinant, $\langle\tilde Q\rangle_{\natural}=\det\mathsf{M}_2(\tilde Q)$, as the computation of the determinant of $\mathsf{M}_2(\tilde Q)=Q_t\mathrm I-i\sum_kQ_k\sigma_k$ shows. The map $\mathsf{M}_2$ is an algebra homomorphism and the determinant is multiplicative, so $\langle\cdot\rangle_{\natural}$ is.

The algebraic norm is the **reduced norm** of the algebra, it is the only multiplicative one of the four, and it is the biquaternion algebraic norm of *Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra*: an element is invertible if and only if $\langle\tilde Q\rangle_{\natural}\neq0$, and the unit group is the norm-one group $\{\langle\tilde Q\rangle_{\natural}=1\}$, a non-compact real $6$-manifold homotopy equivalent to $S^{3}$.

### The General Plain Sesquilinear Algebraic Norm

**The Hermitian norm, written $H$.**

$$
H(\tilde Q)=\langle\tilde Q\rangle_{*}=\langle\tilde Q,\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}=\lvert Q_t\rvert^{2}+\lvert Q_x\rvert^{2}+\lvert Q_y\rvert^{2}+\lvert Q_z\rvert^{2},
$$

the general plain sesquilinear algebraic norm $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=Q_{1,0}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$. It is real-valued, $\mathbb{R}$-quadratic and positive definite, $\langle\tilde Q\rangle_{*}>0$ for $\tilde Q\neq0$; its Gram matrix is $\mathrm I_4$ and its realification is of signature $(8,0)$. Its vanishing set is the origin alone, and it is the square of the topological norm, $\langle\tilde Q\rangle_{*}=\lVert\tilde Q\rVert_E^{2}$.

The algebraic norm is definite, and it is the one of the four whose square root is the topological norm: $\lVert\tilde Q\rVert_E$ is the unique topological norm of the real vector space $\mathbb{B}\cong\mathbb{R}^{8}$, up to equivalence, and it is the topological norm of *Topology in the Space of Biquaternions*. It is not multiplicative.

### The General Quaternionic Sesquilinear Algebraic Norm

**The Krein norm, written $K$.**

$$
K(\tilde Q)=\langle\tilde Q\rangle_{\natural*}=\langle\tilde Q,\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}=\lvert Q_t\rvert^{2}-\lvert Q_x\rvert^{2}-\lvert Q_y\rvert^{2}-\lvert Q_z\rvert^{2},
$$

the general quaternionic sesquilinear algebraic norm $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})=Q_{1,0}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})$; it is the **Krein algebraic norm** of the algebra, the algebraic norm of the Krein form. It is real-valued and indefinite, its Gram matrix is the sign matrix $\mathrm E$, and its realification is of signature $(2,6)$. Its vanishing set is the real cone $\mathcal K=\{\lVert c\rVert_E=\lVert v\rVert_E\}$ of the centre–vector split, and by the identity $\langle\tilde Q\rangle_{\natural*}=\lVert c\rVert_E^{2}-\lVert v\rVert_E^{2}$ it is the null cone of the indefinite metric. It is not multiplicative. The algebraic norm is the one that the **Krein structure** of the algebra produces, the pair of a definite and an indefinite form, and its positive and negative value-one sets are $S^{1}\times\mathbb{R}^{6}$ and $S^{5}\times\mathbb{R}^{2}$.


## The Table of the Four Algebraic Norms

| Algebraic norm | Full norm name | Reduced name | Letter | Multiplicative | Definite | Use | Value | Gram | Signature over $\mathbb{R}$ | Vanishing set |
|---|---|---|---|---|---|---|---|---|---|---|
| $\langle\tilde Q\rangle=\langle\tilde Q,\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^{2}$ | The general plain bilinear algebraic norm | **Plain Norm** | $P$ | no | — | product and its square | $\mathbb{C}$ | $\mathrm E$ | $(4,4)$ | complex cone |
| $\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ | The general quaternionic bilinear algebraic norm | **Quaternionic Norm** | $N$ | **yes** | — | interval, invertibility, the reduced norm | $\mathbb{C}$ | $\mathrm I_4$ | $(4,4)$ | $\mathcal N$, the $N$-degenerate set, the zero-divisor cone |
| $\langle\tilde Q\rangle_{*}=\langle\tilde Q,\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ | The general plain sesquilinear algebraic norm | **Hermitian Norm** | $H$ | no | **yes** | topology, $\lVert\tilde Q\rVert_E^{2}$ | $\mathbb{R}$ | $\mathrm I_4$ | $(8,0)$ | $\{0\}$ |
| $\langle\tilde Q\rangle_{\natural*}=\langle\tilde Q,\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$ | The general quaternionic sesquilinear algebraic norm | **Krein Norm** | $K$ | no | no | indefinite geometry | $\mathbb{R}$ | $\mathrm E$ | $(2,6)$ | $\mathcal K$ |

The table separates the four by their letter, by the field of their values, by the Gram matrix and the signature, by their vanishing set, by the two properties that single out one algebraic norm each — multiplicativity for $\langle\cdot\rangle_{\natural}$, definiteness for $\langle\cdot\rangle_{*}$ — and by their use. Two of the four are the working norms: the quaternionic one answers *when is $\tilde Q$ invertible*, the Hermitian one answers *what is the distance*. The plain and the Krein are the two indefinite remainders, one complex and one real, and each is the sign-flipped twin of a working norm: the plain is the quaternionic with the sign of the vector part reversed, the Krein is the Hermitian with the sign of the vector part reversed.

**The plain norm: no job of its own.** $P(\tilde Q)=\langle\tilde Q\rangle=\mathrm{Sc}(\tilde Q^{2})$ is the scalar part of the ordinary square, the quadratic form of the plain product. It is neither definite nor multiplicative, and it decides no invertibility: the unit $e_t+\vec e_x$ has $P(e_t+\vec e_x)=0$, while the zero divisor $e_t+i\vec e_x$ has $P(e_t+i\vec e_x)=2$. It is the value of the product read on the diagonal and carries no job of its own: the square, its idempotents, its Peirce decompositions, its roots and its cone are properties of the product, which comes before the form.

**The use of the quaternionic norm: invertibility.** $N(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ is the determinant of the $2\times2$ image, hence multiplicative. Its vanishing set is exactly the zero-divisor cone, so $\tilde Q$ is invertible if and only if the value is non-zero, and the unit group is the level set $1$. The value is the interval, the quadratic form of the quaternionic layer. It answers *when is the element invertible*, a yes-or-no question and not a how-big one, and the price of multiplicativity is that it is complex and vanishes off the origin.

**The use of the Hermitian norm: topology.** $H(\tilde Q)=\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ is real and positive definite, and its square root is the Euclidean norm $\lVert\tilde Q\rVert_E$, the unique topological norm of the space. It gives the distance, the balls, the Cauchy–Schwarz inequality, the bounded operators and the completion. It is the pairing of the positive cone. It answers *what is the distance*, and the price of definiteness is that it is not multiplicative.

**The use of the Krein norm: indefinite geometry.** $K(\tilde Q)=\langle\tilde Q\rangle_{\natural*}=\lvert Q_t\rvert^{2}-\lvert\vec Q\rvert^{2}$ is real of signature $(2,6)$, indefinite and not multiplicative. Its use is the indefinite geometry: the inertia, the fundamental symmetry, the Krein orthogonality, the classification of the subspaces, the isotropic elements, the Witt index and the Krein cone, and its group is $\mathrm{U}(1,3)$. It answers *which directions are positive, negative or null*, and what its isometry group preserves.

**Why the four uses do not overlap.** The four are four different questions and not four competing answers, and the cell *definite and multiplicative* is empty: no function on $\mathbb{B}$ is both, the zero divisors forbidding it, as the proposition of the next section proves. The quaternionic norm takes multiplicativity, the Hermitian norm takes definiteness, and the plain and the Krein norms take the two indefinite remainders.


## What the Four Algebraic Norms Separate

**Proposition (no algebraic norm is both definite and multiplicative).** No function on $\mathbb{B}$ is both definite and multiplicative.

*Proof.* The algebra has zero divisors, $(e_t+i\vec e_x)(e_t-i\vec e_x)=0$ with $e_t\pm i\vec e_x\neq0$ and $\langle e_t\pm i\vec e_x\rangle_{\natural}=1+i^{2}=0$. A multiplicative function $\varphi$ would give $\varphi(e_t+i\vec e_x)\varphi(e_t-i\vec e_x)=\varphi(0)=0$, so one of the two values is zero, on a nonzero element; a definite function is nonzero off the origin. No function is both.

**Corollary.** $\langle\cdot\rangle_{*}$ is definite and not multiplicative; $\langle\cdot\rangle_{\natural}$ is multiplicative and not definite; and no third algebraic norm of the four repairs the split. The multiplicative one and the definite one are different objects, and that difference is the failure of the biquaternions to be a normed division algebra — the four normed division algebras $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, $\mathbb{O}$ of the Hurwitz theorem are exactly the ones in which the two senses coincide.

**Proposition (only $\langle\cdot\rangle_{\natural}$ is multiplicative).** Of the four algebraic norms, $\langle\cdot\rangle_{\natural}$ alone satisfies $\varphi(\tilde Q_1\tilde Q_2)=\varphi(\tilde Q_1)\varphi(\tilde Q_2)$.

*Proof.* $\langle\cdot\rangle_{\natural}$ is multiplicative by the proposition of its section. The other three are not, each refuted by one substitution. For $\langle\cdot\rangle$: $\langle \vec e_x\vec e_y\rangle=\langle \vec e_z\rangle=-1$ while $\langle \vec e_x\rangle\langle \vec e_y\rangle=(-1)(-1)=1$. For $\langle\cdot\rangle_{*}$: $\langle \vec e_x+i\vec e_y\rangle_{*}=1+1=2$ while $(\vec e_x+i\vec e_y)^{2}=\vec e_x^{2}+(i\vec e_y)^{2}=-e_t+e_t=0$ and $\langle 0\rangle_{*}=0$. For $\langle\cdot\rangle_{\natural*}$: $\langle e_t+\vec e_x\rangle_{\natural*}=1-1=0$ while $(e_t+\vec e_x)^{2}=e_t^{2}+e_t\vec e_x+\vec e_xe_t+\vec e_x^{2}=e_t+\vec e_x+\vec e_x-e_t=2\vec e_x$ and $\langle 2\vec e_x\rangle_{\natural*}=-4$.

**Remark (the two senses of *norm*).** Two different things carry the name. The **algebraic norm** of this article is a map into the ring — $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural}$ into $\mathbb{C}$, $\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\natural*}$ into $\mathbb{R}$ — and it is algebra: algebraic norms, quadratic forms, polarisations, zero divisors. The **topological norm** is the one selection of positive real values, $\lVert\tilde Q\rVert_E=\bigl(\langle\tilde Q\rangle_{*}\bigr)^{1/2}$, and it is topology: distance, balls, convergence, completeness. Only $\langle\cdot\rangle_{*}$ of the four yields it, because only $\langle\cdot\rangle_{*}$ is real and definite; $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural}$ are complex-valued, and $\langle\cdot\rangle_{\natural*}$ is real but indefinite. The two senses are the two layers of *Introduction to Mathematics*, and no third function holds them together.

**Remark (the four collapse to two on real elements).** For real $\tilde Q_1,\tilde Q_2$ the coefficientwise conjugation is the identity, so $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\langle\tilde Q_1,\tilde Q_2\rangle$ and $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$. On the real part of the space the four algebraic norms are the two, $\langle\cdot\rangle=\langle\cdot\rangle_{\natural*}$ and $\langle\cdot\rangle_{\natural}=\langle\cdot\rangle_{*}$, and the four operations of the two bilinear rows and of the two sesquilinear rows coincide there. This is the real-form caution of *Symmetric and Antisymmetric Decomposition of the Four General Products* read at the two equal arguments: a computation restricted to real elements sees two algebraic norms and hides the other two. On the remarkable real subspaces the four algebraic norms restrict to the two real forms in the same way, and the restrictions, their signatures and the definiteness of each on each are the subject of *Remarkable Subspaces and the Four General Products, Forms and Norms*.


## Regular and Degenerate Biquaternions

**Definition (the qualified regular and the qualified degenerate).** Let $\Phi$ be one of the four letters $P$, $N$, $H$, $K$. A biquaternion is **$\Phi$-regular** when $\Phi(\tilde Q)\neq0$, and **$\Phi$-degenerate** when $\Phi(\tilde Q)=0$. In full, an **$N$-regular biquaternion** has $N(\tilde Q)\neq0$, an **$N$-degenerate biquaternion** has $N(\tilde Q)=0$, and the same definition holds for $P$, $H$ and $K$.

The four conditions are polynomial equations on the eight real coordinates, homogeneous of degree two: two real equations for the complex-valued $P$ and $N$, one for the real-valued $H$ and $K$, and each defines a cone with apex the origin. Written out,

$$
P(\tilde Q)=Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2}=0,\qquad
N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}=0,
$$
$$
H(\tilde Q)=\lvert Q_t\rvert^{2}+\lvert Q_x\rvert^{2}+\lvert Q_y\rvert^{2}+\lvert Q_z\rvert^{2}=0,\qquad
K(\tilde Q)=\lvert Q_t\rvert^{2}-\lvert Q_x\rvert^{2}-\lvert Q_y\rvert^{2}-\lvert Q_z\rvert^{2}=0.
$$

**The four degenerate sets.** The $P$-degenerate set is the complex cone $\{P=0\}$, of real dimension $6$. The $N$-degenerate set is the zero-divisor cone $\mathcal N$, of real dimension $6$. The $K$-degenerate set is the real cone $\mathcal K$, of real dimension $7$. The $H$-degenerate set is the origin alone: $H$ is a sum of four non-negative terms, so it vanishes only where every coefficient vanishes.

| Letter | $\Phi$-degenerate set | $\dim_{\mathbb R}$ | Contains a unit | Equals the non-units |
|---|---|---|---|---|
| $P$ | the complex cone $\{P=0\}$ | $6$ | yes | no |
| $N$ | $\mathcal N$, the origin together with the zero divisors | $6$ | no | **yes** |
| $H$ | $\{0\}$ | $0$ | no | no |
| $K$ | $\mathcal K$, the real cone $\{K=0\}$ | $7$ | yes | no |

**Proposition (only the $N$-degenerate set is the non-unit set).** The $N$-degenerate biquaternions are the origin and the zero divisors, $\{N=0\}=\{0\}\cup\mathcal Z$, and they alone are the non-units. The $P$-degenerate set and the $K$-degenerate set contain units, and the $H$-degenerate set contains the origin alone; none of the three is the non-unit set.

*Proof.* The identity $N(\tilde Q)=\det\mathsf M_2(\tilde Q)$ identifies $\{N=0\}$ with the singular matrices of $M_2(\mathbb{C})$, which are the zero matrix and the zero divisors. The unit $e_t+\vec e_x$ has $P(e_t+\vec e_x)=K(e_t+\vec e_x)=1-1=0$ and $N(e_t+\vec e_x)=1+1=2$, so the $P$ and $K$ sets contain a unit. The $H$ case is the sum of four non-negative terms.

**Remark (the four sets are distinct).** The unit $e_t+\vec e_x$ is $P$-degenerate and $K$-degenerate, not $N$-degenerate; the zero divisor $e_t+i\vec e_x$ is $N$-degenerate and $K$-degenerate, with $P(e_t+i\vec e_x)=1-i^{2}=2$; the zero divisor $\vec e_x+i\vec e_y$ is $P$-degenerate and $N$-degenerate, with $K(\vec e_x+i\vec e_y)=-(1+1)=-2$; and $\sqrt2 e_t+\vec e_x+i\vec e_y$ is $K$-degenerate, with $P=N=2$. The $H$-degenerate set is the origin alone. The four sets are therefore pairwise distinct.

**Remark (the zero element).** The origin is $\Phi$-degenerate for all four letters, and it is neither a unit nor a zero divisor. A degenerate biquaternion is therefore not the same object as a zero divisor for any letter; the $N$ case is the closest, its set being the origin together with the zero divisors.

**Remark (the existing names).** $N$-regular and $N$-degenerate are the qualified pair of *Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra* read at $\Phi=N$, the two halves of its partition of $\mathbb{B}$ into the unit group and the null cone. $K$-regular and $K$-degenerate are the **Krein-regular** and **Krein-degenerate** of *Krein Norm Regularity and Degeneracy in the Biquaternion Algebra*, whose halves are *The K-Regular Sector* and *The K-Degenerate Sector*. The $P$ and $H$ qualifiers are the same construction on the other two letters, named here to close the four; neither decides invertibility.

**Remark (the unqualified words).** **Regular** without a letter is **spectrally regular**, $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}\neq0$, of *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, and **degenerate** without a letter is **spectrally degenerate**, $B^{2}=0$. The letter is therefore never omitted when the four algebraic norms are meant.

**The four regular sets.** The $P$-regular set is the complement of the complex cone, open and dense of real dimension $8$; it is not a group, since $(e_t+i\vec e_x)(e_t-i\vec e_x)=0$ with both factors $P$-regular of value $2$. The $N$-regular set is the unit group $\mathbb{B}^{\times}$, open and dense and a group. The $H$-regular set is $\mathbb{B}\setminus\{0\}$, open and dense, and not a group, since it contains the zero divisors. The $K$-regular set is the complement of $\mathcal K$, open and dense with exactly two connected components, the positive and the negative regions, and it is not a group; it is the regular set of *The K-Regular Sector*.


## Summary

The twelve products of *Symmetric and Antisymmetric Decomposition of the Four General Products* carry four forms and no more: the symmetrisation of a family keeps the scalar part and the antisymmetrisation kills it, so the eight operations of the four $\mathrm G/\mathrm S$ rows carry the four forms two by two and the four antisymmetric operations carry the zero form. The four forms are the scalar parts of the four general products, written with the one bracket whose subscript records the pair and named the general plain bilinear, the general quaternionic bilinear, the general plain sesquilinear — the Hermitian —, and the general quaternionic sesquilinear — the Krein — form. They carry the letters $P$, $N$, $H$ and $K$.

The second slot of the general product decides the symmetry, bilinear or sesquilinear, and so whether the algebraic norm is complex or real; the first slot decides the Gram matrix, the identity or the sign matrix, and so the signature of the algebraic norm and its definiteness on the subspaces. The four are indexed by the two-by-two grid of the two slots.

The same two slots read on the groups that preserve the four forms: the second slot decides whether the group is orthogonal or unitary, the first slot which orthogonal or unitary form, so that the four groups are $O_4(\mathbb{C})$, $O_4(\mathbb{C})$, $\mathrm{U}(4)$ and $\mathrm{U}(1,3)$, of real dimensions $12$, $12$, $16$ and $16$, and the natural conjugation lies in all four. The hyperbolic basis of the plain product, which belongs to the algebra and its vector space rather than to the forms, is *The Biquaternion Algebra and Its Vector Spaces*, §*The Hyperbolic Basis of the Plain Product*.

Read at their two equal arguments, the four forms give the four algebraic norms $\langle\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^{2}$, $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$, $\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ and $\langle\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$, each attained by two operations, the general product and its symmetrisation of the same family, while the four antisymmetrisations carry the vanishing algebraic norm. $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural}$ are complex-valued and $\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\natural*}$ real-valued. $\langle\cdot\rangle_{\natural}$ is the multiplicative one, the reduced norm and the criterion of invertibility; $\langle\cdot\rangle_{*}$ is the definite one, and its square root is the unique topological norm of the space; $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural*}$ are the two indefinite ones of the plain and of the Krein form. Multiplicativity and definiteness are held by no single one of the four, and the zero divisors are the reason.

The four carry the letters $P$, $N$, $H$ and $K$, and each letter gives a qualified pair: a $\Phi$-regular biquaternion is one with $\Phi(\tilde Q)\neq0$ and a $\Phi$-degenerate one has $\Phi(\tilde Q)=0$. Only the $N$ pair is the unit partition — $N$-regular is the unit group, $N$-degenerate the origin together with the zero divisors — while $P$ and $K$ vanish on units and $H$ vanishes only at the origin.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde Q_1,\tilde Q_2\rangle$ | the general plain bilinear form, $\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, symmetric, Gram $\mathrm E$ |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$, symmetric, Gram $\mathrm I_4$ |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$ | the general plain sesquilinear form, the Hermitian form, $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$, definite at the two equal arguments |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$ | the general quaternionic sesquilinear form, the Krein form, $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})$, indefinite at the two equal arguments |
| $(\mathrm{id},\mathrm{id})$, $({}^{\natural},\mathrm{id})$, $(\mathrm{id},{}^{*})$, $({}^{\natural},{}^{*})$ | the four pairs, the subscript of each bracket |
| $\varepsilon=(1,-1,-1,-1)$ | the sign vector of the natural conjugation, which the first slot applies |
| $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$ | the Gram matrix of $\langle\cdot,\cdot\rangle$ and of $\langle\cdot,\cdot\rangle_{\natural*}$; $\mathrm I_4$ is the Gram matrix of $\langle\cdot,\cdot\rangle_{*}$ and of $\langle\cdot,\cdot\rangle_{\natural}$ |
| $(4,4)$, $(4,4)$, $(8,0)$, $(2,6)$ | the signatures of the realifications of $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural*}$ |
| $O_4(\mathbb{C})$, $O_4(\mathbb{C})$, $\mathrm{U}(4)$, $\mathrm{U}(1,3)$ | the groups preserving the four forms, of real dimensions $12$, $12$, $16$, $16$ |
| the complex cone, $\mathcal N$, $\mathcal K$ | the null sets of $\langle\cdot,\cdot\rangle$, of $\langle\cdot,\cdot\rangle_{\natural}$ and of $\langle\cdot,\cdot\rangle_{\natural*}$; that of $\langle\cdot,\cdot\rangle_{*}$ is the origin |
| $\langle\tilde Q\rangle=\langle\tilde Q,\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^{2}$ | the general plain bilinear algebraic norm, the Plain Norm |
| $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ | the general quaternionic bilinear algebraic norm, the Quaternionic Norm; multiplicative, the reduced norm |
| $\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ | the general plain sesquilinear algebraic norm, the Hermitian Norm; definite, $\lVert\tilde Q\rVert_E^{2}$ |
| $\langle\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$ | the general quaternionic sesquilinear algebraic norm, the Krein Norm |
| $P$, $N$, $H$, $K$ | the letters of the plain, the quaternionic, the Hermitian and the Krein form and norm; one letter, two arities |
| $P(\tilde Q)$, $N(\tilde Q)$, $H(\tilde Q)$, $K(\tilde Q)$ | the four algebraic norms, the diagonals of the four forms |
| $\Phi$-regular, $\Phi$-degenerate | $\Phi(\tilde Q)\neq0$ and $\Phi(\tilde Q)=0$ for $\Phi\in\{P,N,H,K\}$; the $N$ pair alone is the partition into units and non-units |
| $\varphi(\tilde Q)=\varphi(\tilde Q,\tilde Q)$ | one bracket, two arities: two arguments give the form, one argument the algebraic norm |
| $\lVert\tilde Q\rVert_E$ | the Euclidean norm, the square root of $\langle\cdot\rangle_{*}$, the unique topological norm |

## Further Reading

- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the four general products whose scalar parts the four forms are, their relations and their comparison.
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the twelve products, their scalar parts and their two-slot construction, on which the count of four forms rests.
- [Conventions in the Biquaternion Universe](../articles_physics/conventions-in-the-biquaternion-universe.html), for the convention of the four pairings — the one bracket, the four names, the four pairs and the trace forms.
- [Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra](quaternionic-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the norm-regular and norm-degenerate partition, the $N$ pair of the last section.
- [Krein Norm Regularity and Degeneracy in the Biquaternion Algebra](krein-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the Krein-regular and Krein-degenerate partition, the $K$ pair of the last section.
- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the unqualified *regular* and *degenerate*, which the letters qualify.
- [The Group of Involutions](the-group-of-involutions.html), for the four conjugations that index the four forms and the group they form.
- [Introduction to the Operators of the Biquaternion Algebra](the-four-general-products-and-operators.html) and [The Four Adjoints of the Biquaternion Algebra in Examples](the-four-adjoints-of-the-biquaternion-algebra-in-examples.html), for the four adjoints of a left multiplication under the four forms.
- [Bilinear Forms](bilinear-forms.html), [Quadratic Forms and Polarisation](quadratic-forms-and-polarisation.html), [Hermitian Forms and Unitary Geometry](hermitian-forms-and-unitary-geometry.html) and [Matrix Groups and Classical Groups](matrix-groups-and-classical-groups.html), for the general theory of a bilinear or sesquilinear form, its Gram matrix and the classical group that preserves it.
- [Remarkable Subspaces and the Four General Products, Forms and Norms](remarkable-subspaces-and-the-four-general-products-forms-and-norms.html), for the four forms read on the remarkable subspaces and the restriction of the four algebraic norms to them.
- [Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra](quaternionic-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the multiplicative algebraic norm, the zero divisors and the criterion of invertibility.
- [Topology in the Space of Biquaternions](topology-in-the-space-of-biquaternions.html), for the one topology of the space, and [The Euclidean Topology of the Biquaternion Algebra](the-euclidean-topology-of-the-biquaternion-algebra.html), for the Euclidean norm.
- [The Norm Defined by a Form](the-norm-defined-by-a-form.html), [Hermitian Forms over Algebras and Norms](hermitian-forms-over-algebras-and-norms.html) and [Introduction to Mathematics](introduction-to-mathematics.html), for the distinction between the algebraic norm and the topological norm.
