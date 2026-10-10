# __The 4 Forms over the Biquaternion $\mathbb{C}$ Space__

## Introduction

The twelve products of *The 12 Products of the Biquaternion Complex Space*, read as the twelve algebraic structures of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, carry four **forms** and no more. The form of a product is its **scalar part**, the degree-two object attached to the product, and it is read off the products themselves, from the table of the twelve. The table is this one, reproduced from *The 12 Products of the Biquaternion Complex Space* with its own columns.

| the product | the operation | scalar part | vector part | scalars | law | unit | image |
|---|---|---|---|---|---|---|---|
| the general plain bilinear product | $\tilde{P}\tilde{Q}$ | $\bigl[P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr]$ | $+P_0\mathbf{Q}+Q_0\mathbf{P}+\mathbf{P}\times\mathbf{Q}$ | $\mathbb{C}$ | associative | $e_0$, both sides | all of $\mathbb{B}$ |
| the symmetric plain bilinear product | $\tfrac12(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P})$ | $\bigl[P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr]$ | $+P_0\mathbf{Q}+Q_0\mathbf{P}$ | $\mathbb{C}$ | commutative, **Jordan** | $e_0$, both sides | all of $\mathbb{B}$ |
| the antisymmetric plain bilinear product | $\tfrac12(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P})$ | $\bigl[0\bigr]$ | $\mathbf{P}\times\mathbf{Q}$ | $\mathbb{C}$ | alternating, **Jacobi** | none | $\mathrm{Vect}(\mathbb{B})$ |
| the general quaternionic bilinear product | $\tilde{P}^{\natural}\tilde{Q}$ | $\bigl[P_0Q_0+(\mathbf{P},\mathbf{Q})\bigr]$ | $+P_0\mathbf{Q}-Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}$ | $\mathbb{C}$ | not associative | $e_0$, left only | all of $\mathbb{B}$ |
| the symmetric quaternionic bilinear product | $\tfrac12(\tilde{P}^{\natural}\tilde{Q}+\tilde{Q}^{\natural}\tilde{P})$ | $\bigl[P_0Q_0+(\mathbf{P},\mathbf{Q})\bigr]$ | $0$ | $\mathbb{C}$ | commutative, no Jordan | none | the centre $\mathbb{C}_{\mathbb{B}}$ |
| the antisymmetric quaternionic bilinear product | $\tfrac12(\tilde{P}^{\natural}\tilde{Q}-\tilde{Q}^{\natural}\tilde{P})$ | $\bigl[0\bigr]$ | $P_0\mathbf{Q}-Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}$ | $\mathbb{C}$ | alternating, no Jacobi | none | $\mathrm{Vect}(\mathbb{B})$ |
| the general plain sesquilinear product | $\tilde{P}\tilde{Q}^{*}$ | $\bigl[P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})\bigr]$ | $-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}$ | $\mathbb{C},\bar{\cdot}$ | not associative | $e_0$, right only | all of $\mathbb{B}$ |
| the symmetric plain sesquilinear product | $\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}+\overline{\tilde{Q}}\tilde{P}^{\natural}\bigr)$ | $\bigl[P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})\bigr]$ | $0$ | $\mathbb{C},\bar{\cdot}$ | conjugate-commutative, no Jordan | none | the centre $\mathbb{C}_{\mathbb{B}}$ |
| the antisymmetric plain sesquilinear product | $\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}-\overline{\tilde{Q}}\tilde{P}^{\natural}\bigr)$ | $\bigl[0\bigr]$ | $-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}$ | $\mathbb{C},\bar{\cdot}$ | conjugate-alternating, no Jacobi | none | $\mathrm{Vect}(\mathbb{B})$ |
| the general quaternionic sesquilinear product | $\tilde{P}^{\natural}\tilde{Q}^{*}$ | $\bigl[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr]$ | $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}+\mathbf{P}\times\overline{\mathbf{Q}}$ | $\mathbb{C},\bar{\cdot}$ | not associative | none | all of $\mathbb{B}$ |
| the symmetric quaternionic sesquilinear product | $\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*}+\tilde{Q}^{*}\tilde{P}^{\natural}\bigr)$ | $\bigl[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr]$ | $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$ | $\mathbb{C},\bar{\cdot}$ | conjugate-commutative, no Jordan | none | no subspace of the remarkable subspaces |
| the antisymmetric quaternionic sesquilinear product | $\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*}-\tilde{Q}^{*}\tilde{P}^{\natural}\bigr)$ | $\bigl[0\bigr]$ | $\mathbf{P}\times\overline{\mathbf{Q}}$ | $\mathbb{C},\bar{\cdot}$ | conjugate-alternating, no Jacobi | none | $\mathrm{Vect}(\mathbb{B})$ |

**Reading the third column.** The twelve products have twelve scalar parts, and these take **four values and no more**. The scalar part $P_0Q_0-(\mathbf P,\mathbf Q)$ is shared by the general plain bilinear product and by its symmetrisation; the scalar part $P_0Q_0+(\mathbf P,\mathbf Q)$ by the general quaternionic bilinear product and by its symmetrisation; the scalar part $P_0\overline{Q_0}+(\mathbf P,\overline{\mathbf Q})$ by the general plain sesquilinear product and by its symmetrisation; the scalar part $P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q})$ by the general quaternionic sesquilinear product and by its symmetrisation. The remaining four products, the four antisymmetrisations, have the scalar part $0$. Four values, each carried by the general product of a family and by its symmetrisation; and no value is carried by products of two different families.

**Definition (the four forms).** The **form** of a product $f$ is its scalar part, $\varphi(\tilde P,\tilde Q)=\mathrm{Sc}\,f(\tilde P,\tilde Q)$, a function of two elements. The four distinct scalar parts therefore give **four forms**, the scalar parts of the four general products. They are written with the one bracket of *Conventions in the Biquaternion Universe*, whose subscript records the pair $(a,b)$, the natural conjugation ${}^{\natural}$ for a non-identity first slot and the star ${}^{*}$ for a non-identity second slot:

$$
B(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)=P_0Q_0-(\mathbf P,\mathbf Q),
\qquad
N(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q),
$$
$$
H(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})=P_0\overline{Q_0}+(\mathbf P,\overline{\mathbf Q}),
\qquad
K(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q}),
$$

for the four pairs $(\mathrm{id},\mathrm{id})$, $({}^{\natural},\mathrm{id})$, $(\mathrm{id},{}^{*})$, $({}^{\natural},{}^{*})$ read in that order, the four pairs and no others: the **general plain bilinear form**, the **general quaternionic bilinear form**, the **general plain sesquilinear form**, also called the **Hermitian form**, and the **general quaternionic sesquilinear form**, also called the **Krein form**. The symmetrisation of a family keeps the scalar part of the general product, so it keeps the form; the antisymmetrisation kills the scalar part, so it has no form. That is the whole of the count, and §*From Twelve Operations to Four Forms* proves it.

The four forms are the four pairings of *The Four Pairings of the Biquaternion Algebra*, read as the scalar parts of the four general products. The general theory of the pairings — the group of the four involutions, the Gram matrices, the groups that preserve each form, the null sets and the value-one sets — is owned by that article and by *Conventions in the Biquaternion Universe*, and only the count and the notation are recalled here. Each form is the trace form of its own pair, up to the factor of the trace convention,

$$
2h_{a,b}(\tilde P,\tilde Q)=\mathrm{Tr}(\tilde P^{a}\tilde Q^{b}),
$$

for the same four pairs in the same order.

The **diagonal** of a form is the form with its two arguments equated, $\varphi(\tilde Q)=\varphi(\tilde Q,\tilde Q)$, a function of one element. The four diagonals of the four forms are the four **algebraic norms** of *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*: that article starts from the four forms defined here, and it owns the further structure of the four — the multiplicativity of $N$, the definiteness of the diagonal of $H$, the failure of any function to be both, the two senses of the word *norm* and the one topological norm of the space. The chain is therefore the table of the twelve, then the four forms of this article, then the four algebraic norms of the companion.

The four forms are separated by their symmetry and by their Gram matrix, and no two of them share both. The **symmetry** is that of the second slot of the general product: symmetric for the two bilinear forms, conjugate-symmetric for the two sesquilinear ones. The **Gram matrix**, the identity $\mathrm I_4$ for $N$ and $H$ and the sign matrix $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$ for $B$ and $K$, is that of the first slot, which enters through the natural conjugation and the sign vector $\varepsilon=(1,-1,-1,-1)$. It fixes the **signature** of the realification of each, and it is the first slot alone that decides whether a form is definite or indefinite where the other is not.

## Notational Conventions

$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the biquaternion algebra, with basis $e_0,e_1,e_2,e_3$, $e_0=1$, $e_k^{2}=-e_0$, and central scalar imaginary $i$, $i^{2}=-1$. A general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$, written in the centre–vector split $\tilde Q=c+v$ with $c=Q_0e_0\in\mathbb{C}_{\mathbb{B}}$ and $v=\sum_{k=1}^{3}Q_ke_k\in\mathrm{Vect}(\mathbb{B})$. The scalar part is $\mathrm{Sc}$, the coefficientwise conjugation is $\bar{\cdot}$, the natural conjugation is ${}^{\natural}$, with $Q^{\natural}_\nu=\varepsilon_\nu Q_\nu$, and the Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$. The sign vector is $\varepsilon=(1,-1,-1,-1)$, and $\mathbb{B}$ is identified with $\mathbb{C}^{4}$ by $\tilde Q\mapsto(Q_0,Q_1,Q_2,Q_3)$. The vector parts carry the complex bilinear dot product $(\mathbf P,\mathbf Q)=\sum_{k=1}^{3}P_kQ_k$ and the cross product $\mathbf P\times\mathbf Q$. The four forms are $B$, $N$, $H$ and $K$; their names, brackets and pairs are the convention of *Conventions in the Biquaternion Universe*, which reads the four on the algebra and on the material sector. $H$ is also the Hermitian form and $K$ the Krein form, and the letters $B$, $N$, $H$, $K$ are the short names of this article. A form is $\mathbb{C}$-**bilinear** when its second slot is read without the star, so that a scalar pulls out of it, and **sesquilinear** when the second slot is read with the star, so that the scalar pulls out conjugated. The Euclidean norm is $\lVert\tilde Q\rVert_E=\bigl(\sum_\mu\lvert Q_\mu\rvert^{2}\bigr)^{1/2}$, the square root of the diagonal of $H$.

## The Form of an Operation

**Definition (the form of an operation).** Let $f$ be an operation on $\mathbb{B}$ with scalar part $\varphi(\tilde P,\tilde Q)=\mathrm{Sc}\,f(\tilde P,\tilde Q)$. The **form of the operation $f$** is $\varphi$. It is bilinear when the second slot of $f$ is read without the star, sesquilinear when it is read with the star. In both cases the value lies in $\mathbb{C}$, the conjugation of the second slot entering the value; a sesquilinear form is conjugate-symmetric, $\varphi(\tilde P,\tilde Q)=\overline{\varphi(\tilde Q,\tilde P)}$, so that its diagonal is real. For an operation whose scalar part vanishes identically the form is the zero form.

The definition is the one of *Introduction to Mathematics*: the form is the degree-two object attached to a product, it is a function of two elements, and the algebraic norm is its diagonal, a function of one. The four forms of the biquaternion algebra are then the four functions of the introduction, $B$, $N$, $H$ and $K$, read on the third column of the table of the twelve.

## From Twelve Operations to Four Forms

The reduction from twelve to four is in two steps: the symmetrisation of a family keeps the scalar part, and the antisymmetrisation kills it. The twelve products are named in the three-letter code of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* — the general, symmetric and antisymmetric operation of each family, the plain and quaternionic family lettered $\mathrm P$ and $\mathrm Q$ and the algebra and sesqualgebra lettered $\mathrm A$ and $\mathrm S$, so that the twelve are $\mathrm{GPA},\mathrm{SPA},\mathrm{APA}$ in the plain algebra, $\mathrm{GQA},\mathrm{SQA},\mathrm{AQA}$ in the quaternionic algebra, and $\mathrm{GPS},\mathrm{SPS},\mathrm{APS}$, $\mathrm{GQS},\mathrm{SQS},\mathrm{AQS}$ in the two sesqualgebras.

**Lemma (the symmetrisation keeps the scalar part, the antisymmetrisation kills it).** For each of the four general products $f$, with symmetric part $f^{\mathrm s}$ and antisymmetric part $f^{\mathrm a}$,

$$
\mathrm{Sc}\,f^{\mathrm s}(\tilde P,\tilde Q)=\mathrm{Sc}\,f(\tilde P,\tilde Q),
\qquad
\mathrm{Sc}\,f^{\mathrm a}(\tilde P,\tilde Q)=0 .
$$

*Proof.* For the two bilinear families the scalar part is commutative, $\mathrm{Sc}(\tilde P\tilde Q)=\mathrm{Sc}(\tilde Q\tilde P)$, so $\mathrm{Sc}\,f^{\mathrm s}=\tfrac12\bigl(\mathrm{Sc}\,f(\tilde P,\tilde Q)+\mathrm{Sc}\,f(\tilde Q,\tilde P)\bigr)=\mathrm{Sc}\,f(\tilde P,\tilde Q)$ and $\mathrm{Sc}\,f^{\mathrm a}=\tfrac12\bigl(\mathrm{Sc}\,f(\tilde P,\tilde Q)-\mathrm{Sc}\,f(\tilde Q,\tilde P)\bigr)=0$. For the two sesquilinear families the exchange carries the conjugation of the value and the forms are Hermitian, $\mathrm{Sc}\,f(\tilde P,\tilde Q)=\overline{\mathrm{Sc}\,f(\tilde Q,\tilde P)}$, so $\mathrm{Sc}\,f^{\mathrm s}=\tfrac12\bigl(\mathrm{Sc}\,f(\tilde P,\tilde Q)+\overline{\mathrm{Sc}\,f(\tilde Q,\tilde P)}\bigr)=\mathrm{Sc}\,f(\tilde P,\tilde Q)$ and $\mathrm{Sc}\,f^{\mathrm a}=0$. $\square$

**Proposition (the twelve operations carry four forms).** The twelve operations have exactly four distinct non-zero forms, the four above, each attained by two operations, and four operations have the zero form.

*Proof.* By the lemma, the symmetric part of a general product has the same scalar part as the general product and the antisymmetric part the zero scalar part. Hence the forms of the twelve are those of the four general products, each on the two operations $\mathrm G$ and $\mathrm S$ of its family: the form $B$ on $\mathrm{GPA}$ and $\mathrm{SPA}$, $N$ on $\mathrm{GQA}$ and $\mathrm{SQA}$, $H$ on $\mathrm{GPS}$ and $\mathrm{SPS}$, $K$ on $\mathrm{GQS}$ and $\mathrm{SQS}$; and the zero form on $\mathrm{APA}$, $\mathrm{AQA}$, $\mathrm{APS}$ and $\mathrm{AQS}$. The four are distinct as functions of two elements: on the pair $\tilde P=e_1$, $\tilde Q=e_1+ie_1$ their values are

$$
B=-(1+i),\qquad N=1+i,\qquad H=1-i,\qquad K=-(1-i),
$$

four different complex numbers, and no two of the four agree. $\square$

**Remark (the zero form is not a form of the count).** The four antisymmetric operations have the zero scalar part because their scalar part vanishes identically — $\mathbf P\times\mathbf Q$ for $\mathrm{APA}$ and $\mathrm{AQA}$, and the alternating forms of the two Hermitian forms for $\mathrm{APS}$ and $\mathrm{AQS}$. A vanishing scalar part is counted as no form rather than as a fifth form, so the twelve operations are counted four ways and no more.

## The Four Forms

### The General Plain Bilinear Form $B$

$$
B(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)=P_0Q_0-(\mathbf P,\mathbf Q),
$$

the scalar part of the general plain bilinear product. It is symmetric, $\mathbb{C}$-bilinear and complex-valued, its Gram matrix on the coefficient basis is the sign matrix $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$, and its realification is of signature $(4,4)$. It is non-degenerate. Its null set, the set of $\tilde Q$ with $B(\tilde Q,\tilde Q)=0$, is the complex cone $\sum_\mu\varepsilon_\mu Q_\mu^{2}=0$, of real dimension six, and it is neither the zero-divisor cone nor the light cone. In the physics of the corpus this is the form of **composition**: it pairs two material operations, and its diagonal carries the sector sign, negative on the anti-Hermitian sector and positive on the Hermitian one.

### The General Quaternionic Bilinear Form $N$

$$
N(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q),
$$

the scalar part of the general quaternionic bilinear product: the same form as $B$ read through the natural conjugation of the first slot, differing from it by the sign of the vector part alone. It is symmetric, $\mathbb{C}$-bilinear and complex-valued, its Gram matrix is the identity $\mathrm I_4$, and its realification is of signature $(4,4)$. It is non-degenerate. Its null set is the zero-divisor cone $\mathcal N=\{N(\tilde Q,\tilde Q)=0\}$, of real dimension six, which is the light cone of the physics corpus. This is the form of **causality**: its diagonal is the interval, and the pair of the first slot is what makes the square of a material element land on the interval rather than on the negative Euclidean square.

### The General Plain Sesquilinear Form $H$, the Hermitian Form

$$
H(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})=P_0\overline{Q_0}+(\mathbf P,\overline{\mathbf Q}),
$$

the scalar part of the general plain sesquilinear product. It is conjugate-symmetric, $H(\tilde P,\tilde Q)=\overline{H(\tilde Q,\tilde P)}$, sesquilinear in the second slot, and its diagonal is real and positive definite, $H(\tilde Q,\tilde Q)>0$ for $\tilde Q\neq0$; its Gram matrix is $\mathrm I_4$ and its realification is of signature $(8,0)$. It is non-degenerate, and its null set is the origin alone, so it has no cone. This is the form of **probability**: it is the Born pairing, definite, and its diagonal is the square of the unique topological norm of the space, $\lVert\tilde Q\rVert_E^{2}$.

### The General Quaternionic Sesquilinear Form $K$, the Krein Form

$$
K(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q}),
$$

the scalar part of the general quaternionic sesquilinear product: the same form as $H$ read through the natural conjugation of the first slot, differing from it by the sign of the vector part alone. It is conjugate-symmetric and sesquilinear, its diagonal is real and indefinite, its Gram matrix is the sign matrix $\mathrm E$, and its realification is of signature $(2,6)$. It is non-degenerate, and its null set is the real cone $\mathcal K$, the null cone of the Krein form. This is the form of **gauge**: indefinite, of mixed signature on every sector, and the form of a constraint rather than of a state space.

## The Table of the Four Forms

| form | bracket | pair | coordinates | symmetry | Gram | signature over $\mathbb{R}$ | null set | diagonal lands in |
|---|---|---|---|---|---|---|---|---|
| $B$ | $\langle\cdot,\cdot\rangle$ | $(\mathrm{id},\mathrm{id})$ | $P_0Q_0-(\mathbf P,\mathbf Q)$ | symmetric | $\mathrm E$ | $(4,4)$ | the complex cone | $\mathbb{C}$ |
| $N$ | $\langle\cdot,\cdot\rangle_{\natural}$ | $({}^{\natural},\mathrm{id})$ | $P_0Q_0+(\mathbf P,\mathbf Q)$ | symmetric | $\mathrm I_4$ | $(4,4)$ | $\mathcal N$, the zero divisors | $\mathbb{C}$ |
| $H$ | $\langle\cdot,\cdot\rangle_{*}$ | $(\mathrm{id},{}^{*})$ | $P_0\overline{Q_0}+(\mathbf P,\overline{\mathbf Q})$ | conjugate-symmetric | $\mathrm I_4$ | $(8,0)$ | $\{0\}$ | $\mathbb{R}$ |
| $K$ | $\langle\cdot,\cdot\rangle_{\natural*}$ | $({}^{\natural},{}^{*})$ | $P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q})$ | conjugate-symmetric | $\mathrm E$ | $(2,6)$ | $\mathcal K$ | $\mathbb{R}$ |

The table separates the four by their bracket and pair, by their symmetry, by the Gram matrix and the signature of the realification of their diagonal, by their null set, and by the field in which the diagonal lands — complex for the two bilinear forms and real for the two sesquilinear ones, the conjugating second slot being what makes a diagonal real.

## The Two Slots

**The mechanism.** A form is obtained from a product by reading the first factor either as it stands or through the natural conjugation ${}^{\natural}$, and the second factor either as it stands or through the star ${}^{*}$; nothing else varies. The four forms are therefore indexed by a two-by-two grid, and the grid is the whole of the subject. The mechanism, the laws and the readings are shared with *The Four General Products of the Biquaternion $\mathbb{C}$ Space* and with the physics companion *The Four General Products and Their Physical Readings*, which carries the signature table of the four on the remarkable subspaces.

**What each slot decides.**

- The **second slot** decides whether the form is a **composition** or a **pairing**. Read without the star the form is bilinear and symmetric and can be iterated; read with the star it is sesquilinear and conjugate-symmetric and can only be evaluated. It is the slot that separates the two bilinear forms from the two sesquilinear ones, and it is what makes the diagonal of a sesquilinear form real.
- The **first slot** decides the **Gram matrix** and the **signature**, and through them **definiteness on each sector**. Read as it stands the form is $B$ or $H$; read through the natural conjugation it is $N$ or $K$. Since the natural conjugation multiplies the vector part by $-1$, the first slot toggles the coefficient $\varepsilon$ of the vector part and so turns the sign matrix $\mathrm E$ into the identity $\mathrm I_4$.

**The physical reading, and it is a reading and not a theorem.** The four forms are the four jobs a relativistic quantum theory needs: the general plain bilinear form is **composition**, the general quaternionic bilinear form is **causality**, the general plain sesquilinear form is **probability** and the general quaternionic sesquilinear form is **gauge**. The reading is the one of *Conventions in the Biquaternion Universe* and of the physics companion; it is stated here and not proved, since what is proved here is the count of the four and their table.

## What the Four Forms Separate

**Proposition (no two of the four agree).** No two of the four forms are equal as functions of two elements.

*Proof.* On $\tilde P=e_1$, $\tilde Q=e_1+ie_1$ the four values are $-(1+i)$, $1+i$, $1-i$ and $-(1-i)$, four different complex numbers, as in the proposition of §*From Twelve Operations to Four Forms*. $\square$

**The second slot gives the symmetry, the first slot the signature.** The four forms fall into two pairs by symmetry, $\{B,N\}$ bilinear and $\{H,K\}$ sesquilinear, and into two other pairs by Gram matrix, $\{B,K\}$ of Gram $\mathrm E$ and $\{N,H\}$ of Gram $\mathrm I_4$. The two divisions are independent, and their product is the four: each form is the intersection of one symmetry with one Gram matrix, which is the two-by-two grid of the two slots.

**The four collapse to two on real elements.** For real $\tilde P,\tilde Q$ the coefficientwise conjugation is the identity, so $K(\tilde P,\tilde Q)=B(\tilde P,\tilde Q)$ and $H(\tilde P,\tilde Q)=N(\tilde P,\tilde Q)$. On the real part of the space the four forms are the two, and only the two slots together, not the complex structure, separate them.

**The null sets are four.** The null set of $B$ is the complex cone, that of $N$ the zero-divisor cone $\mathcal N$ — the light cone —, that of $H$ the origin alone and that of $K$ the real cone $\mathcal K$. Three of the four are cones: the complex cone and the zero-divisor cone, of real dimension six, and the Krein cone, of real dimension seven. The two of dimension six do not agree, so the complex cone of $B$ is not the light cone of $N$; the fourth null set is the origin, so the diagonal of $H$ is definite and has no cone. The three cones and the origin are what the physics reads as the two light cones and the two definite structures.

## Summary

The twelve products of *The 12 Products of the Biquaternion Complex Space* carry four forms and no more: the symmetrisation of a family keeps the scalar part and the antisymmetrisation kills it, so the eight operations of the four $\mathrm G/\mathrm S$ rows carry the four forms two by two and the four antisymmetric operations carry the zero form. The four forms are the scalar parts of the four general products, written with the one bracket whose subscript records the pair and named the general plain bilinear, the general quaternionic bilinear, the general plain sesquilinear — the Hermitian — and the general quaternionic sesquilinear — the Krein — form.

The second slot of the general product decides the symmetry, bilinear or sesquilinear, and so whether the diagonal is complex or real; the first slot decides the Gram matrix, the identity or the sign matrix, and so the signature of the diagonal and its definiteness on the sectors. The four are indexed by the two-by-two grid of the two slots, and their diagonals are the four algebraic norms of *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $B(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle$ | the general plain bilinear form, $\mathrm{Sc}(\tilde P\tilde Q)$, symmetric, Gram $\mathrm E$ |
| $N(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$, symmetric, Gram $\mathrm I_4$; its diagonal is the interval |
| $H(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{*}$ | the general plain sesquilinear form, the Hermitian form, $\mathrm{Sc}(\tilde P\tilde Q^{*})$, positive definite on the diagonal |
| $K(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{\natural*}$ | the general quaternionic sesquilinear form, the Krein form, $\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})$, indefinite on the diagonal |
| $(\mathrm{id},\mathrm{id})$, $({}^{\natural},\mathrm{id})$, $(\mathrm{id},{}^{*})$, $({}^{\natural},{}^{*})$ | the four pairs, the subscript of each bracket |
| $\varepsilon=(1,-1,-1,-1)$ | the sign vector of the natural conjugation, which the first slot applies |
| $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$ | the Gram matrix of $B$ and of $K$; $\mathrm I_4$ is the Gram matrix of $N$ and of $H$ |
| $(4,4)$, $(4,4)$, $(8,0)$, $(2,6)$ | the signatures of the realifications of $B$, $N$, $H$, $K$ |
| the complex cone, $\mathcal N$, $\mathcal K$ | the null sets of $B$, of $N$ and of $K$; that of $H$ is the origin |
| $\varphi(\tilde Q)=\varphi(\tilde Q,\tilde Q)$ | the diagonal of a form, the passage to an algebraic norm |

## Further Reading

- *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-algebraic-norms-over-the-biquaternion-c-space.md`), the companion that starts from the four forms of this article, for the four algebraic norms as their diagonals, the multiplicativity of $N$, the definiteness of the diagonal of $H$, the failure of any function to be both, and the two senses of the word *norm*.
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the twelve products, their scalar parts and their two-slot construction, on which the count of four forms rests.
- *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the twelve names $\mathrm{GPA},\dots,\mathrm{AQS}$ and the reading of the third column of the table.
- *Conventions in the Biquaternion Universe* (`articles_physics/conventions-in-the-biquaternion-universe.md`), for the convention of the four pairings — the one bracket $\langle\cdot,\cdot\rangle$ with the subscript that records the pair, the four names, the four pairs, the trace form $2h_{a,b}=\mathrm{Tr}(\tilde P^{a}\tilde Q^{b})$ and the readings of the four on the algebra and on the material sector.
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the general theory of the four pairings: the group of the involutions, the Gram matrices, the groups that preserve each form, the null sets and the value-one sets.
- *The Four General Products of the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternion-c-space.md`), *Relations Between the Four General Products* (`articles_maths/relations-between-the-four-general-products.md`) and *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the four general products whose scalar parts the four forms are, and for the comparison of the four.
- *The Four General Products and Their Physical Readings* (`articles_physics/the-four-general-products-and-their-physical-readings.md`), for the signature table of the four forms on the remarkable subspaces and for the four readings, composition, causality, probability and gauge.
- *Remarkable Subspaces and the Four Forms* (`articles_maths/remarkable-subspaces-and-the-four-forms.md`), for the same four forms read on the remarkable subspaces, with the real and imaginary parts of each, the collapse patterns and the alternating companion of the two sesquilinear forms.
- *Remarkable Subspaces and the Four General Products* (`articles_maths/remarkable-subspaces-and-the-four-general-products.md`), for the four general products — the operations whose scalar parts the four forms are — read on the remarkable subspaces.
- *Introduction to Mathematics* (`articles_maths/introduction-to-mathematics.md`), *Hermitian Forms over Algebras and Norms* (`articles_maths/hermitian-forms-over-algebras-and-norms.md`) and *The Norm Defined by a Form* (`articles_maths/the-norm-defined-by-a-form.md`), for the degree-two object attached to a product, its diagonal and the passage from the algebraic norm to the topological one.
