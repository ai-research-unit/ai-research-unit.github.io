# __The Vector Parts of the Products over the Biquaternion Algebra__

## Introduction

The twelve products of *Symmetric and Antisymmetric Decomposition of the Four General Products* split every value into a scalar part and a vector part. The scalar parts are the four forms of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, and they are studied as forms. The vector parts are the other half, and this article treats them as what they are: vector-valued maps, one to a product, with a table, a diagonal, an image, a symmetry and a behaviour on the remarkable subspaces.

The vector part is not a scalar form. It is a map into the three-dimensional complex vector subspace $\mathrm{Vect}(\mathbb{B})$, and the scalar theory applies to its three contractions with the basis vectors. The article states this distinction first, then reads the twelve vector parts one by one, then develops the properties that are common to them. The two results that organise the table are the **two-bit rule** for the four general products and the **loss of distinctions**: the twelve products carry nine distinct vector parts on the complex space, not twelve, because the two central symmetric products have zero vector part and because the quaternionic bilinear and the plain sesquilinear products share their vector part with their antisymmetric parts.

The article assumes the four general products of *The Four General Products and Their Relations over the Biquaternion Algebra*, the twelve products and their codes of *Symmetric and Antisymmetric Decomposition of the Four General Products*, and the four forms of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*. The element, the basis and the three conjugations are those of *The Biquaternion Algebra*; the remarkable subspaces are those of *The Six Subspaces*; the two switches are those of *Introduction to the Operators of the Biquaternion Algebra*. The diagonal of the plain product is also computed in *The Square of an Element*, the diagonal of the general quaternionic sesquilinear product in *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*, and the diagonal of the block in *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*.

Throughout, $\tilde Q_1=Q_{1t}e_t+\vec Q_1$ and $\tilde Q_2=Q_{2t}e_t+\vec Q_2$, with $Q_{1t},Q_{2t}\in\mathbb{C}$ and $\vec Q_1,\vec Q_2\in\mathrm{Vect}(\mathbb{B})$. The coefficientwise conjugation is $\overline{\cdot}$, the natural conjugation is ${}^{\natural}$, the Hermitian conjugation is ${}^{*}=\overline{\cdot}\circ{}^{\natural}$, the complex bilinear dot product is $(\vec Q_1,\vec Q_2)=\sum_kQ_{1k}Q_{2k}$, and the complex bilinear cross product is $\vec Q_1\times\vec Q_2$. The vector subspace is $\mathrm{Vect}(\mathbb{B})$, the centre is $\mathbb{C}_{\mathbb{B}}$, the real quaternion subspace is $\mathbb{H}_{\mathbb{B}}$, and the Hermitian and anti-Hermitian subspaces are $\mathbb{M}_+$ and $\mathbb{M}_-$. The codes are those of the decomposition article: $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{GPS}$, $\mathrm{GQS}$ for the four general products, $\mathrm{SPA}$, $\mathrm{SQA}$, $\mathrm{SPS}$, $\mathrm{SQS}$ for their symmetric parts, and $\mathrm{APA}$, $\mathrm{AQA}$, $\mathrm{APS}$, $\mathrm{AQS}$ for their antisymmetric parts.

## The Vector Part of a Product

**Definition (the vector part).** For a biquaternion $\tilde Q=Q_te_t+\vec Q$, the **scalar part** and the **vector part** are

$$
\mathrm{Sc}(\tilde Q)=Q_t,\qquad \mathrm{Vec}(\tilde Q)=\vec Q ,
$$

so that $\tilde Q=\mathrm{Sc}(\tilde Q)e_t+\mathrm{Vec}(\tilde Q)$. They are the two projections of the scalar–vector split, and both are $\mathbb{C}$-linear:

$$
\mathrm{Sc}(\tilde Q)=\tfrac12\bigl(\tilde Q+\tilde Q^{\natural}\bigr),\qquad
\mathrm{Vec}(\tilde Q)=\tfrac12\bigl(\tilde Q-\tilde Q^{\natural}\bigr).
$$

**Definition (the vector part of a product).** For a product $f$ of the twelve, the **vector part of $f$** is the map

$$
V_f(\tilde Q_1,\tilde Q_2)=\mathrm{Vec}\bigl(f(\tilde Q_1,\tilde Q_2)\bigr).
$$

The product is reconstructed from its two parts,

$$
f(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}\bigl(f(\tilde Q_1,\tilde Q_2)\bigr)e_t+V_f(\tilde Q_1,\tilde Q_2),
$$

and the scalar part is one of the four forms, while $V_f$ is the new object. The map $V_f$ is $\mathbb{C}$-bilinear when $f$ is one of the six products of the two bilinear families, and sesquilinear over $(\mathbb{C},\bar{\cdot})$ when $f$ is one of the six products of the two sesquilinear families. Its values lie in $\mathrm{Vect}(\mathbb{B})$.

**The vector part is not a form.** A form of the corpus is scalar-valued: it is the scalar part of a product read in two arguments, bilinear or sesquilinear by its second slot. The vector part is vector-valued, so it has no scalar Gram matrix and no signature of its own. What replaces the scalar form is a family of three scalar forms, one to a vector of the subspace: for $w\in\mathrm{Vect}(\mathbb{B})$ put

$$
\varphi_{f,w}(\tilde Q_1,\tilde Q_2)=\bigl(w,V_f(\tilde Q_1,\tilde Q_2)\bigr).
$$

For $f$ bilinear, $\varphi_{f,w}$ is a complex bilinear form; for $f$ sesquilinear, it is sesquilinear over $(\mathbb{C},\bar{\cdot})$. The three coordinate forms with $w=\vec e_x,\vec e_y,\vec e_z$ determine $V_f$, and $V_f$ determines them. This is the precise sense in which a vector part is a package of three scalar forms. The four forms of the corpus are the scalar parts; they are not a fifth member of the package of three.

**The natural quadratic invariants.** The scalar forms of $V_f$ are not the only scalars it carries. The complex bilinear square $(V_f,V_f)$ and the real square $(V_f,\overline{V_f})$ are the two natural scalar quantities attached to the vector part; the second is the Euclidean square of the vector. They are quartic in the arguments for a general product, and they are the natural invariants when no vector $w$ is chosen.

## The Rule for the Four General Products

The four general products obey one rule. Put $\varepsilon=0$ for the two products whose second slot is plain, $\mathrm{GPA}$ and $\mathrm{GQA}$, and $\varepsilon=1$ for the two whose second slot is the Hermitian conjugation, $\mathrm{GPS}$ and $\mathrm{GQS}$. Write

$$
\vec Q_2^{\varepsilon}=
\begin{cases}
\vec Q_2, & \varepsilon=0,\\
\overline{\vec Q_2}, & \varepsilon=1,
\end{cases}
\qquad
Q_{2t}^{\varepsilon}=
\begin{cases}
Q_{2t}, & \varepsilon=0,\\
\overline{Q_{2t}}, & \varepsilon=1.
\end{cases}
$$

Let $\alpha$ be the sign of the vector part of the second factor and $\beta$ the sign of the vector part of the first factor:

| product | first slot | second slot | $\varepsilon$ | $\alpha$ | $\beta$ | $\alpha\beta$ |
|---|---|---|---|---|---|---|
| $\mathrm{GPA}$ | plain | plain | $0$ | $+$ | $+$ | $+$ |
| $\mathrm{GQA}$ | natural | plain | $0$ | $+$ | $-$ | $-$ |
| $\mathrm{GPS}$ | plain | star | $1$ | $-$ | $+$ | $-$ |
| $\mathrm{GQS}$ | natural | star | $1$ | $-$ | $-$ | $+$ |

**Theorem (the vector part of a general product).** For the four general products,

$$
\boxed{\;V_f(\tilde Q_1,\tilde Q_2)=\alpha\,Q_{1t}\vec Q_2^{\varepsilon}+\beta\,Q_{2t}^{\varepsilon}\vec Q_1+\alpha\beta\,\vec Q_1\times\vec Q_2^{\varepsilon}\;}
$$

and the scalar part is

$$
\mathrm{Sc}\bigl(f(\tilde Q_1,\tilde Q_2)\bigr)=Q_{1t}Q_{2t}^{\varepsilon}-\alpha\beta\,\bigl(\vec Q_1,\vec Q_2^{\varepsilon}\bigr).
$$

*Proof.* The first factor is $\tilde Q_1^{\natural}$ for $\beta=-1$ and $\tilde Q_1$ for $\beta=+1$, so it is $Q_{1t}+\beta\vec Q_1$. The second factor is $\tilde Q_2$ for $\varepsilon=0$ and $\tilde Q_2^{*}=Q_{2t}^{\varepsilon}-\vec Q_2^{\varepsilon}$ for $\varepsilon=1$; in both cases it is $Q_{2t}^{\varepsilon}+\alpha\vec Q_2^{\varepsilon}$ with $\alpha=+1$ for $\varepsilon=0$ and $\alpha=-1$ for $\varepsilon=1$. The quaternion product of $Q_{1t}+\beta\vec Q_1$ and $Q_{2t}^{\varepsilon}+\alpha\vec Q_2^{\varepsilon}$ has scalar part $Q_{1t}Q_{2t}^{\varepsilon}-\alpha\beta(\vec Q_1,\vec Q_2^{\varepsilon})$ and vector part $\alpha Q_{1t}\vec Q_2^{\varepsilon}+\beta Q_{2t}^{\varepsilon}\vec Q_1+\alpha\beta\,\vec Q_1\times\vec Q_2^{\varepsilon}$, which is the display.

**Remark (the two bits).** The sign $\alpha$ is read on the **second** slot: it is $+$ for the plain and $-$ for the star. The sign $\beta$ is read on the **first** slot: it is $+$ for the plain and $-$ for the natural conjugation. The cross term carries the product $\alpha\beta$. The first mixed term carries $\alpha$, the second carries $\beta$, and the two are the two switches of *Introduction to the Operators of the Biquaternion Algebra* read on the vector part rather than on the scalar form. The four general vector parts are therefore the four sign choices of two independent bits, not a list of four unrelated formulas.

## The Table of the Twelve Vector Parts

The table lists the twelve products with their codes, their vector parts, their diagonals, their symmetries and their images. The diagonal is $V_f(\tilde Q,\tilde Q)$ at the single element $\tilde Q=Q_te_t+\vec Q$; the symmetry is the relation between $V_f(\tilde Q_1,\tilde Q_2)$ and $V_f(\tilde Q_2,\tilde Q_1)$, read with the coefficientwise conjugation in the sesquilinear families.

| product | code | vector part | diagonal | symmetry | image |
|---|---|---|---|---|---|
| the general plain bilinear product | $\mathrm{GPA}$ | $Q_{1t}\vec Q_2+Q_{2t}\vec Q_1+\vec Q_1\times\vec Q_2$ | $2Q_t\vec Q$ | neither | $\mathrm{Vect}(\mathbb{B})$ |
| the general quaternionic bilinear product | $\mathrm{GQA}$ | $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$ | $0$ | alternating | $\mathrm{Vect}(\mathbb{B})$ |
| the general plain sesquilinear product | $\mathrm{GPS}$ | $-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}$ | $-Q_t\overline{\vec Q}+\overline{Q_t}\vec Q-\vec Q\times\overline{\vec Q}$ | conjugate-alternating | $\mathrm{Vect}(\mathbb{B})$ |
| the general quaternionic sesquilinear product | $\mathrm{GQS}$ | $-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1+\vec Q_1\times\overline{\vec Q_2}$ | $-Q_t\overline{\vec Q}-\overline{Q_t}\vec Q+\vec Q\times\overline{\vec Q}$ | neither | $\mathrm{Vect}(\mathbb{B})$ |
| the symmetric plain bilinear product | $\mathrm{SPA}$ | $Q_{1t}\vec Q_2+Q_{2t}\vec Q_1$ | $2Q_t\vec Q$ | symmetric | $\mathrm{Vect}(\mathbb{B})$ |
| the symmetric quaternionic bilinear product | $\mathrm{SQA}$ | $0$ | $0$ | zero | $\{0\}$ |
| the symmetric plain sesquilinear product | $\mathrm{SPS}$ | $0$ | $0$ | zero | $\{0\}$ |
| the symmetric quaternionic sesquilinear product | $\mathrm{SQS}$ | $-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1$ | $-Q_t\overline{\vec Q}-\overline{Q_t}\vec Q$ | conjugate-symmetric | $\mathrm{Vect}(\mathbb{B})$ |
| the antisymmetric plain bilinear product | $\mathrm{APA}$ | $\vec Q_1\times\vec Q_2$ | $0$ | alternating | $\mathrm{Vect}(\mathbb{B})$ |
| the antisymmetric quaternionic bilinear product | $\mathrm{AQA}$ | $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$ | $0$ | alternating | $\mathrm{Vect}(\mathbb{B})$ |
| the antisymmetric plain sesquilinear product | $\mathrm{APS}$ | $-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}$ | $-Q_t\overline{\vec Q}+\overline{Q_t}\vec Q-\vec Q\times\overline{\vec Q}$ | conjugate-alternating | $\mathrm{Vect}(\mathbb{B})$ |
| the antisymmetric quaternionic sesquilinear product | $\mathrm{AQS}$ | $\vec Q_1\times\overline{\vec Q_2}$ | $\vec Q\times\overline{\vec Q}$ | conjugate-alternating | $\mathrm{Vect}(\mathbb{B})$ |

The **vector part** column is $V_f$; the **diagonal** column is $V_f$ at the two equal arguments; the **symmetry** column is the class of the map under the exchange of the arguments, with the coefficientwise conjugation in the sesquilinear families; and the **image** column is the image of $V_f$ on the whole space. Ten rows fill the vector subspace and two rows, $\mathrm{SQA}$ and $\mathrm{SPS}$, are the zero map. The table has repetitions: the rows $\mathrm{GQA}$ and $\mathrm{AQA}$ are identical, the rows $\mathrm{GPS}$ and $\mathrm{APS}$ are identical, and the two zero rows are identical. The next section proves that these are the only repetitions on the complex space.

## The Nine Vector Parts

**Theorem (the vector part loses the central symmetric parts).** The twelve vector parts satisfy

$$
\boxed{\;V_{\mathrm{GQA}}=V_{\mathrm{AQA}},\qquad V_{\mathrm{GPS}}=V_{\mathrm{APS}},\qquad V_{\mathrm{SQA}}=V_{\mathrm{SPS}}=0\;}
$$

and these three identities are the only coincidences among the twelve on the complex space. The twelve products therefore carry **nine distinct vector parts**.

*Proof.* The symmetric part of the general quaternionic bilinear product is the quaternion form read as a product, $\mathrm{SQA}(\tilde Q_1,\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$, which is central; its vector part is zero. Hence $V_{\mathrm{GQA}}=V_{\mathrm{SQA}}+V_{\mathrm{AQA}}=V_{\mathrm{AQA}}$. The symmetric part of the general plain sesquilinear product is the Hermitian form read as a product, $\mathrm{SPS}(\tilde Q_1,\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{*}e_t$, which is central; hence $V_{\mathrm{GPS}}=V_{\mathrm{APS}}$. The two central products themselves have zero vector part. The nine remaining classes are separated by the three pairs in the next table.

**Theorem (the separation).** The nine classes are pairwise distinct, and the three pairs $(\vec e_t,\vec e_x)$, $(\vec e_x,\vec e_y)$ and $(\vec e_x,i\vec e_y)$ separate them.

| class | $(\vec e_t,\vec e_x)$ | $(\vec e_x,\vec e_y)$ | $(\vec e_x,i\vec e_y)$ |
|---|---|---|---|
| $\mathrm{GPA}$ | $\vec e_x$ | $\vec e_z$ | $i\vec e_z$ |
| $\mathrm{GQA}=\mathrm{AQA}$ | $\vec e_x$ | $-\vec e_z$ | $-i\vec e_z$ |
| $\mathrm{GPS}=\mathrm{APS}$ | $-\vec e_x$ | $-\vec e_z$ | $i\vec e_z$ |
| $\mathrm{GQS}$ | $-\vec e_x$ | $\vec e_z$ | $-i\vec e_z$ |
| $\mathrm{SPA}$ | $\vec e_x$ | $0$ | $0$ |
| $\mathrm{SQS}$ | $-\vec e_x$ | $0$ | $0$ |
| $\mathrm{APA}$ | $0$ | $\vec e_z$ | $i\vec e_z$ |
| $\mathrm{AQS}$ | $0$ | $\vec e_z$ | $-i\vec e_z$ |
| $0$ | $0$ | $0$ | $0$ |

Each row is different from every other, so the nine classes are distinct. The table also shows where the coincidences come from: $\mathrm{GPA}$ and $\mathrm{GQA}$ differ only in the sign of the cross term and of the second mixed term; $\mathrm{GPS}$ and $\mathrm{GQS}$ differ in the sign of the second mixed term and of the cross term; $\mathrm{SPA}$ and $\mathrm{SQS}$ differ in the sign and in the coefficientwise conjugation of the two mixed terms; and $\mathrm{APA}$ and $\mathrm{AQS}$ differ only at the complex pair.

**Corollary (the vector part does not determine the product).** The map $f\mapsto V_f$ has fibres $\{\mathrm{GQA},\mathrm{AQA}\}$, $\{\mathrm{GPS},\mathrm{APS}\}$ and $\{\mathrm{SQA},\mathrm{SPS}\}$. In each fibre the two products have different scalar parts — the quaternionic form against zero, the Hermitian form against zero, and the quaternionic form against the Hermitian form — so the pair $(\mathrm{Sc}\circ f,V_f)$ determines $f$, while $V_f$ alone does not. The vector part is one half of the product; the scalar part is the other, and the two are needed together.

## The Four General Vector Parts

### The General Plain Bilinear Product (GPA)

The vector part is

$$
V_{\mathrm{GPA}}=Q_{1t}\vec Q_2+Q_{2t}\vec Q_1+\vec Q_1\times\vec Q_2.
$$

It is $\mathbb{C}$-bilinear and neither symmetric nor alternating: its symmetric part is $V_{\mathrm{SPA}}=Q_{1t}\vec Q_2+Q_{2t}\vec Q_1$ and its alternating part is $V_{\mathrm{APA}}=\vec Q_1\times\vec Q_2$, so $V_{\mathrm{GPA}}=V_{\mathrm{SPA}}+V_{\mathrm{APA}}$. Its diagonal is $2Q_t\vec Q$, which vanishes exactly on the centre and on the vector subspace; it is the vector part of the square computed in *The Square of an Element*. Its image is all of $\mathrm{Vect}(\mathbb{B})$, since at $\tilde Q_1=\vec e_t$ and $\tilde Q_2=\vec w$ it is $\vec w$. On pure vectors it is the cross product $\vec Q_1\times\vec Q_2$. Its scalar part is the plain form $P$. When one argument is central, only the mixed term of the other survives, and the vector part is a complex multiple of the other vector part.

### The General Quaternionic Bilinear Product (GQA)

The vector part is

$$
V_{\mathrm{GQA}}=Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2.
$$

It is $\mathbb{C}$-bilinear and **alternating**, $V_{\mathrm{GQA}}(\tilde Q_2,\tilde Q_1)=-V_{\mathrm{GQA}}(\tilde Q_1,\tilde Q_2)$, and its diagonal is zero. It equals $V_{\mathrm{AQA}}$ because the symmetric part $\mathrm{SQA}$ is central. Its image is all of $\mathrm{Vect}(\mathbb{B})$. On pure vectors it is $-\vec Q_1\times\vec Q_2$. It is the reflection of the plain vector part in $Q_{1t}\vec Q_2$,

$$
V_{\mathrm{GQA}}=2Q_{1t}\vec Q_2-V_{\mathrm{GPA}},\qquad
V_{\mathrm{GPA}}+V_{\mathrm{GQA}}=2Q_{1t}\vec Q_2,
$$

which is the vector form of the splitting identity of *The Four General Products and Their Relations over the Biquaternion Algebra*. Its scalar part is the quaternionic form $N$. The square of the product is central, $N(\tilde Q)e_t$, and the vanishing of the diagonal is that statement. It is the only general product whose vector part is alternating.

### The General Plain Sesquilinear Product (GPS)

The vector part is

$$
V_{\mathrm{GPS}}=-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}.
$$

It is sesquilinear over $(\mathbb{C},\bar{\cdot})$ and **conjugate-alternating**,

$$
V_{\mathrm{GPS}}(\tilde Q_1,\tilde Q_2)=-\overline{V_{\mathrm{GPS}}(\tilde Q_2,\tilde Q_1)}.
$$

Its diagonal is the vector part of the Hermitian square $\tilde Q\tilde Q^{*}$, hence a purely imaginary vector; it vanishes exactly when $\tilde Q\tilde Q^{*}$ is central, that is, when the Hermitian square has no vector part. It equals $V_{\mathrm{APS}}$ because $\mathrm{SPS}$ is central. Its image is all of $\mathrm{Vect}(\mathbb{B})$. On pure vectors it is $-\vec Q_1\times\overline{\vec Q_2}$. It is the plain vector part read on $(\tilde Q_1,\tilde Q_2^{*})$,

$$
V_{\mathrm{GPS}}(\tilde Q_1,\tilde Q_2)=V_{\mathrm{GPA}}(\tilde Q_1,\tilde Q_2^{*}),
$$

which is the vector form of the slot identity. Its scalar part is the Hermitian form $H$.

### The General Quaternionic Sesquilinear Product (GQS)

The vector part is

$$
V_{\mathrm{GQS}}=-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1+\vec Q_1\times\overline{\vec Q_2}.
$$

It is sesquilinear and neither conjugate-symmetric nor conjugate-alternating. It splits into its conjugate-symmetric and conjugate-alternating halves,

$$
V_{\mathrm{GQS}}=V_{\mathrm{SQS}}+V_{\mathrm{AQS}},
\qquad
V_{\mathrm{SQS}}=-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1,
\qquad
V_{\mathrm{AQS}}=\vec Q_1\times\overline{\vec Q_2}.
$$

Its diagonal is $-Q_t\overline{\vec Q}-\overline{Q_t}\vec Q+\vec Q\times\overline{\vec Q}$; its real part is the real vector $-2(a\vec p+b\vec q)$ and its imaginary part is $-2i\,\vec p\times\vec q$ for $Q_t=a+ib$ and $\vec Q=\vec p+i\vec q$, so the two parts are orthogonal. Its image is all of $\mathrm{Vect}(\mathbb{B})$. On pure vectors it is $\vec Q_1\times\overline{\vec Q_2}$. It is the quaternionic vector part read on $(\tilde Q_1,\tilde Q_2^{*})$,

$$
V_{\mathrm{GQS}}(\tilde Q_1,\tilde Q_2)=V_{\mathrm{GQA}}(\tilde Q_1,\tilde Q_2^{*}),
$$

and it satisfies $V_{\mathrm{GPS}}+V_{\mathrm{GQS}}=-2Q_{1t}\overline{\vec Q_2}$. Its scalar part is the Krein form $K$. It is the only general product whose vector part has both a conjugate-symmetric and a conjugate-alternating piece.

## The Four Symmetric Vector Parts

### The Symmetric Plain Bilinear Product (SPA)

The vector part is

$$
V_{\mathrm{SPA}}=Q_{1t}\vec Q_2+Q_{2t}\vec Q_1.
$$

It is symmetric, $V_{\mathrm{SPA}}(\tilde Q_1,\tilde Q_2)=V_{\mathrm{SPA}}(\tilde Q_2,\tilde Q_1)$, and it is the symmetrisation of the plain vector part,

$$
V_{\mathrm{SPA}}=\tfrac12\bigl(V_{\mathrm{GPA}}(\tilde Q_1,\tilde Q_2)+V_{\mathrm{GPA}}(\tilde Q_2,\tilde Q_1)\bigr).
$$

Its diagonal is $2Q_t\vec Q$, the same as that of $\mathrm{GPA}$; it vanishes on the centre and on the vector subspace. Its image is all of $\mathrm{Vect}(\mathbb{B})$. On pure vectors it vanishes identically. Its scalar part is the plain form $P$. The zero set is $Q_{1t}\vec Q_2=-Q_{2t}\vec Q_1$; off the centre and the vector subspace it forces the two vector parts to be proportional.

### The Symmetric Quaternionic Bilinear Product (SQA)

The vector part is zero:

$$
V_{\mathrm{SQA}}=0.
$$

The product is central-valued, $\mathrm{SQA}(\tilde Q_1,\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$, the quaternion form read as a product. The vector part has zero diagonal, zero image and zero values on pure vectors. It is one of the two products of the twelve whose vector part vanishes identically.

### The Symmetric Plain Sesquilinear Product (SPS)

The vector part is zero:

$$
V_{\mathrm{SPS}}=0.
$$

The product is central-valued, $\mathrm{SPS}(\tilde Q_1,\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{*}e_t$, the Hermitian form read as a product. The vector part has zero diagonal, zero image and zero values on pure vectors. It is the second of the two products whose vector part vanishes identically.

### The Symmetric Quaternionic Sesquilinear Product (SQS)

The vector part is

$$
V_{\mathrm{SQS}}=-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1.
$$

It is conjugate-symmetric,

$$
V_{\mathrm{SQS}}(\tilde Q_1,\tilde Q_2)=\overline{V_{\mathrm{SQS}}(\tilde Q_2,\tilde Q_1)},
$$

and it is the conjugate-symmetric half of the general quaternionic sesquilinear vector part,

$$
V_{\mathrm{SQS}}=\tfrac12\bigl(V_{\mathrm{GQS}}(\tilde Q_1,\tilde Q_2)+\overline{V_{\mathrm{GQS}}(\tilde Q_2,\tilde Q_1)}\bigr).
$$

Its diagonal is $-Q_t\overline{\vec Q}-\overline{Q_t}\vec Q$, a real vector. It vanishes exactly when $Q_t=0$ or $\vec Q=iQ_t\vec r$ with $\vec r$ a real vector. Its image is all of $\mathrm{Vect}(\mathbb{B})$, and its diagonal image is the real vector subspace $\mathrm{Vect}_{\mathbb{R}}(\mathbb{B})$. On pure vectors it vanishes. Its scalar part is the Krein form $K$; the values of the product itself lie in no remarkable subspace of *The Six Subspaces*.

## The Four Antisymmetric Vector Parts

### The Antisymmetric Plain Bilinear Product (APA)

The vector part is

$$
V_{\mathrm{APA}}=\vec Q_1\times\vec Q_2.
$$

It is alternating and satisfies the Jacobi identity; it is the Lie bracket of the vector subspace, which is isomorphic to $\mathfrak{sl}(2,\mathbb{C})$, and the article that develops it is *The Lie Algebra of the Antisymmetric Plain Algebra*. Its diagonal is zero, its image is all of $\mathrm{Vect}(\mathbb{B})$, and on pure vectors it is the cross product. Its scalar part is zero. Its quadratic invariant is the Lagrange identity

$$
\bigl(\vec Q_1\times\vec Q_2,\vec Q_1\times\vec Q_2\bigr)
=\bigl(\vec Q_1,\vec Q_1\bigr)\bigl(\vec Q_2,\vec Q_2\bigr)-\bigl(\vec Q_1,\vec Q_2\bigr)^2,
$$

and it vanishes exactly when the two vector parts are linearly dependent.

### The Antisymmetric Quaternionic Bilinear Product (AQA)

The vector part is

$$
V_{\mathrm{AQA}}=Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2.
$$

It is alternating, and it equals $V_{\mathrm{GQA}}$ because the symmetric part $\mathrm{SQA}$ is central. Its diagonal is zero, its image is all of $\mathrm{Vect}(\mathbb{B})$, and on pure vectors it is $-\vec Q_1\times\vec Q_2$. Its scalar part is zero. It fails the Jacobi identity at $(\vec e_t,\vec e_x,\vec e_y)$ with cyclic sum $-\vec e_z$, as *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra* records. It is the antisymmetric part of the quaternionic bilinear product.

### The Antisymmetric Plain Sesquilinear Product (APS)

The vector part is

$$
V_{\mathrm{APS}}=-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}.
$$

It is conjugate-alternating, and it equals $V_{\mathrm{GPS}}$ because the symmetric part $\mathrm{SPS}$ is central. Its diagonal is the vector part of $\tilde Q\tilde Q^{*}$, a purely imaginary vector; its image is all of $\mathrm{Vect}(\mathbb{B})$; on pure vectors it is $-\vec Q_1\times\overline{\vec Q_2}$. Its scalar part is zero. It fails the Jacobi identity at $(\vec e_t,\vec e_x,\vec e_y)$ with cyclic sum $\vec e_z$ and at $(\vec e_x,\vec e_x,i\vec e_y)$ with $-2i\vec e_y$, as *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra* records. It is the antisymmetric part of the general plain sesquilinear product.

### The Antisymmetric Quaternionic Sesquilinear Product (AQS)

The vector part is

$$
V_{\mathrm{AQS}}=\vec Q_1\times\overline{\vec Q_2}.
$$

It is conjugate-alternating. Its diagonal is

$$
\vec Q\times\overline{\vec Q}=-2i\,\vec p\times\vec q,
\qquad \vec Q=\vec p+i\vec q,
$$

a purely imaginary vector, and it vanishes exactly when $\vec Q$ is a complex multiple of a real vector. Its image is all of $\mathrm{Vect}(\mathbb{B})$, and on pure vectors it is $\vec Q_1\times\overline{\vec Q_2}$. Its scalar part is zero. It fails the Jacobi identity at $(\vec e_x,\vec e_x,i\vec e_y)$ with $-2i\vec e_y$, as *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra* records. On the real subspace it equals $V_{\mathrm{APA}}$. It is the antisymmetric part of the general quaternionic sesquilinear product.

## The Diagonal and the Square

**Definition.** The **diagonal** of a vector part is

$$
D_f(\tilde Q)=V_f(\tilde Q,\tilde Q)=\mathrm{Vec}\bigl(f(\tilde Q,\tilde Q)\bigr).
$$

It is the vector part of the square of the element. The table groups the twelve diagonals by their value.

| products | diagonal | image |
|---|---|---|
| $\mathrm{GPA}$, $\mathrm{SPA}$ | $2Q_t\vec Q$ | $\mathrm{Vect}(\mathbb{B})$ |
| $\mathrm{GQA}$, $\mathrm{SQA}$, $\mathrm{SPS}$, $\mathrm{APA}$, $\mathrm{AQA}$ | $0$ | $\{0\}$ |
| $\mathrm{GPS}$, $\mathrm{APS}$ | $-Q_t\overline{\vec Q}+\overline{Q_t}\vec Q-\vec Q\times\overline{\vec Q}$ | $i\,\mathrm{Vect}_{\mathbb{R}}(\mathbb{B})$ |
| $\mathrm{GQS}$ | $-Q_t\overline{\vec Q}-\overline{Q_t}\vec Q+\vec Q\times\overline{\vec Q}$ | $\{r+is:\ r,s\in\mathrm{Vect}_{\mathbb{R}}(\mathbb{B}),\ r\cdot s=0\}$ |
| $\mathrm{SQS}$ | $-Q_t\overline{\vec Q}-\overline{Q_t}\vec Q$ | $\mathrm{Vect}_{\mathbb{R}}(\mathbb{B})$ |
| $\mathrm{AQS}$ | $\vec Q\times\overline{\vec Q}$ | $i\,\mathrm{Vect}_{\mathbb{R}}(\mathbb{B})$ |

**Proposition (homogeneity).** The diagonal of a $\mathbb{C}$-bilinear product is homogeneous of degree two over $\mathbb{C}$, $D_f(\lambda\tilde Q)=\lambda^2D_f(\tilde Q)$, and the diagonal of a sesquilinear product is homogeneous of degree two in the real sense, $D_f(\lambda\tilde Q)=\lvert\lambda\rvert^2D_f(\tilde Q)$.

*Proof.* For a bilinear product, $f(\lambda\tilde Q,\lambda\tilde Q)=\lambda^2f(\tilde Q,\tilde Q)$; for a sesquilinear product, $f(\lambda\tilde Q,\lambda\tilde Q)=\lambda\overline{\lambda}f(\tilde Q,\tilde Q)=\lvert\lambda\rvert^2f(\tilde Q,\tilde Q)$. The vector part carries the scalar.

**Proposition (the GQS diagonal and orthogonality).** Write $Q_t=a+ib$ and $\vec Q=\vec p+i\vec q$ with $a,b\in\mathbb{R}$ and $\vec p,\vec q\in\mathrm{Vect}_{\mathbb{R}}(\mathbb{B})$. Then

$$
D_{\mathrm{GQS}}(\tilde Q)=-2(a\vec p+b\vec q)-2i\,\vec p\times\vec q,
$$

and its real and imaginary parts are orthogonal. Conversely, every pair of orthogonal real vectors is the real and imaginary parts of a value of $D_{\mathrm{GQS}}$.

*Proof.* The mixed terms give $-Q_t\overline{\vec Q}-\overline{Q_t}\vec Q=-2(a\vec p+b\vec q)$, which is real, and the cross term gives $\vec Q\times\overline{\vec Q}=-2i\,\vec p\times\vec q$, which is purely imaginary. The real part lies in the plane spanned by $\vec p,\vec q$, while the imaginary part is perpendicular to that plane, so the two are orthogonal. For the converse, let $r,s$ be orthogonal real vectors; take $\vec p=r/\lvert r\rvert$, $\vec q=-(\lvert s\rvert/2)(\hat s\times\hat p)$, $a=-\lvert r\rvert/2$ and $b=0$, and the display returns $r+is$; the degenerate cases follow by continuity and by the zero vector.

**The zero sets of the diagonals.** The diagonal of $\mathrm{GPA}$ or $\mathrm{SPA}$ vanishes exactly on the centre and on the vector subspace, $Q_t=0$ or $\vec Q=0$. The diagonals of $\mathrm{GQA}$, $\mathrm{SQA}$, $\mathrm{SPS}$, $\mathrm{APA}$ and $\mathrm{AQA}$ vanish identically. The diagonal of $\mathrm{SQS}$ vanishes exactly when $Q_t=0$ or $\vec Q=iQ_t\vec r$ with $\vec r$ real. The diagonal of $\mathrm{AQS}$ vanishes exactly when $\vec Q$ is a complex multiple of a real vector. The diagonal of $\mathrm{GPS}$ or $\mathrm{APS}$ vanishes exactly when $\tilde Q\tilde Q^{*}$ is central, that is, when the Hermitian square has no vector part. The diagonal of $\mathrm{GQS}$ vanishes exactly when the two equations $a\vec p+b\vec q=0$ and $\vec p\times\vec q=0$ hold.

**Remark (the diagonal is not a form).** The diagonal is a quadratic map, not a bilinear or sesquilinear form. This is the same distinction as for the vector part itself, read at the two equal arguments. The diagonal of $\mathrm{GPS}$ is the object studied in *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*, and the diagonal of $\mathrm{GQS}$ is the vector part of the square studied in *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*.

## The Behaviour on the Subspaces

**The centre.** If both arguments are central, all twelve vector parts vanish. More generally, if one argument is central, every vector part collapses to a scalar multiple of the other vector part, and the multiplier is $Q_{1t}$ or $\overline{Q_{1t}}$ for the first argument and $Q_{2t}$ or $\overline{Q_{2t}}$ for the second, with the sign of the slot:

| central argument | the surviving vector parts |
|---|---|
| $\tilde Q_1\in\mathbb{C}_{\mathbb{B}}$ | $V_{\mathrm{GPA}}=V_{\mathrm{GQA}}=V_{\mathrm{SPA}}=V_{\mathrm{AQA}}=Q_{1t}\vec Q_2$; $V_{\mathrm{GPS}}=V_{\mathrm{GQS}}=V_{\mathrm{SQS}}=V_{\mathrm{APS}}=-Q_{1t}\overline{\vec Q_2}$; the other four vanish |
| $\tilde Q_2\in\mathbb{C}_{\mathbb{B}}$ | $V_{\mathrm{GPA}}=V_{\mathrm{SPA}}=Q_{2t}\vec Q_1$; $V_{\mathrm{GQA}}=V_{\mathrm{AQA}}=-Q_{2t}\vec Q_1$; $V_{\mathrm{GPS}}=V_{\mathrm{APS}}=\overline{Q_{2t}}\vec Q_1$; $V_{\mathrm{GQS}}=V_{\mathrm{SQS}}=-\overline{Q_{2t}}\vec Q_1$; the other four vanish |

**The vector subspace.** On pure vectors, $\tilde Q_1=\vec Q_1$ and $\tilde Q_2=\vec Q_2$, the mixed terms drop and only the cross term survives. The twelve vector parts fall to five:

| products | vector part on $\mathrm{Vect}(\mathbb{B})$ |
|---|---|
| $\mathrm{GPA}$, $\mathrm{APA}$ | $\vec Q_1\times\vec Q_2$ |
| $\mathrm{GQA}$, $\mathrm{AQA}$ | $-\vec Q_1\times\vec Q_2$ |
| $\mathrm{GPS}$, $\mathrm{APS}$ | $-\vec Q_1\times\overline{\vec Q_2}$ |
| $\mathrm{GQS}$, $\mathrm{AQS}$ | $\vec Q_1\times\overline{\vec Q_2}$ |
| $\mathrm{SPA}$, $\mathrm{SQA}$, $\mathrm{SPS}$, $\mathrm{SQS}$ | $0$ |

Each general vector part coincides with its antisymmetric part on the vector subspace, and each symmetric part vanishes there. On the vector subspace the vector part is therefore the cross product alone.

**The real subspace.** On the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the coefficientwise conjugation is the identity and the twelve vector parts fall to eight. The collisions are

$$
V_{\mathrm{GQA}}=V_{\mathrm{AQA}},\qquad
V_{\mathrm{GPS}}=V_{\mathrm{APS}},\qquad
V_{\mathrm{APA}}=V_{\mathrm{AQS}},\qquad
V_{\mathrm{SQA}}=V_{\mathrm{SPS}}=0,
$$

and the eight representatives are

| product | vector part on $\mathbb{H}_{\mathbb{B}}$ |
|---|---|
| $\mathrm{GPA}$ | $Q_{1t}\vec Q_2+Q_{2t}\vec Q_1+\vec Q_1\times\vec Q_2$ |
| $\mathrm{GQA}$ | $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$ |
| $\mathrm{GPS}$ | $-Q_{1t}\vec Q_2+Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$ |
| $\mathrm{GQS}$ | $-Q_{1t}\vec Q_2-Q_{2t}\vec Q_1+\vec Q_1\times\vec Q_2$ |
| $\mathrm{SPA}$ | $Q_{1t}\vec Q_2+Q_{2t}\vec Q_1$ |
| $\mathrm{SQS}$ | $-Q_{1t}\vec Q_2-Q_{2t}\vec Q_1$ |
| $\mathrm{APA}$ | $\vec Q_1\times\vec Q_2$ |
| $0$ | $0$ |

**The Hermitian subspace.** On $\mathbb{M}_+$, write $\tilde Q_1=a+i\vec p$ and $\tilde Q_2=b+i\vec q$ with $a,b\in\mathbb{R}$ and $\vec p,\vec q\in\mathrm{Vect}_{\mathbb{R}}(\mathbb{B})$. The twelve vector parts fall to seven:

| class | vector part on $\mathbb{M}_+$ |
|---|---|
| $\mathrm{GPA}=\mathrm{GPS}=\mathrm{APS}$ | $-\vec p\times\vec q+i(a\vec q+b\vec p)$ |
| $\mathrm{GQA}=\mathrm{GQS}=\mathrm{AQA}$ | $\vec p\times\vec q+i(a\vec q-b\vec p)$ |
| $\mathrm{SPA}$ | $i(a\vec q+b\vec p)$ |
| $\mathrm{SQS}$ | $i(a\vec q-b\vec p)$ |
| $\mathrm{APA}$ | $-\vec p\times\vec q$ |
| $\mathrm{AQS}$ | $\vec p\times\vec q$ |
| $\mathrm{SQA}=\mathrm{SPS}$ | $0$ |

The identities behind the table are $V_{\mathrm{GPS}}=V_{\mathrm{GPA}}$ and $V_{\mathrm{GQS}}=V_{\mathrm{GQA}}$ on $\mathbb{M}_+$, because $\tilde Q^{*}=\tilde Q$ there, together with $V_{\mathrm{SPS}}=V_{\mathrm{GPS}}-V_{\mathrm{APS}}=0$. On the anti-Hermitian subspace $\mathbb{M}_-$ the same argument with $\tilde Q^{*}=-\tilde Q$ gives $V_{\mathrm{GPS}}=-V_{\mathrm{GPA}}$ and $V_{\mathrm{GQS}}=-V_{\mathrm{GQA}}$.

## The Symmetries of the Vector Parts

The exchange of the two arguments classifies the vector parts by the same four symmetries that classify the parts of the products. The following table gives the class, the identity and the products.

| class | identity | products |
|---|---|---|
| symmetric | $V(\tilde Q_1,\tilde Q_2)=V(\tilde Q_2,\tilde Q_1)$ | $\mathrm{SPA}$ |
| alternating | $V(\tilde Q_1,\tilde Q_2)=-V(\tilde Q_2,\tilde Q_1)$ | $\mathrm{GQA}$, $\mathrm{APA}$, $\mathrm{AQA}$ |
| conjugate-symmetric | $V(\tilde Q_1,\tilde Q_2)=\overline{V(\tilde Q_2,\tilde Q_1)}$ | $\mathrm{SQS}$ |
| conjugate-alternating | $V(\tilde Q_1,\tilde Q_2)=-\overline{V(\tilde Q_2,\tilde Q_1)}$ | $\mathrm{GPS}$, $\mathrm{APS}$, $\mathrm{AQS}$ |
| neither | — | $\mathrm{GPA}$, $\mathrm{GQS}$ |
| zero | $V=0$ | $\mathrm{SQA}$, $\mathrm{SPS}$ |

**Theorem (the class of the vector part).** The vector part of a product has the symmetry of the part of the product: it is symmetric for the symmetric part of a bilinear product, alternating for the antisymmetric part of a bilinear product, conjugate-symmetric for the symmetric part of a sesquilinear product, and conjugate-alternating for the antisymmetric part of a sesquilinear product. The vector parts of the four general products are not all of one class: the plain bilinear is neither, the quaternionic bilinear is alternating, the plain sesquilinear is conjugate-alternating, and the quaternionic sesquilinear is neither.

*Proof.* The four definitions of the parts give the four identities term by term. For the bilinear pair, the exchange is the swap and the vector part of the swapped value is the swapped vector part; for the sesquilinear pair, the exchange is the swap followed by the coefficientwise conjugation, and the vector part of the conjugated value is the conjugated vector part because the conjugation is real-linear on the vector subspace. The general rows follow from the decompositions $V_{\mathrm{GPA}}=V_{\mathrm{SPA}}+V_{\mathrm{APA}}$ and $V_{\mathrm{GQS}}=V_{\mathrm{SQS}}+V_{\mathrm{AQS}}$.

**Remark (the vector part can be more symmetric than the product).** The general quaternionic bilinear product is not alternating — its scalar part is symmetric — but its vector part is alternating. The general plain sesquilinear product is not conjugate-alternating as a product — its scalar part is conjugate-symmetric — but its vector part is. The symmetry of the vector part is the symmetry of the vector half, not of the whole value; the scalar half carries the other symmetry, and the two halves together are neither.

## The Component Forms

**Definition (the component forms).** For $f$ of the twelve and $w\in\mathrm{Vect}(\mathbb{B})$, the **component form** is

$$
\varphi_{f,w}(\tilde Q_1,\tilde Q_2)=\bigl(w,V_f(\tilde Q_1,\tilde Q_2)\bigr).
$$

For $f$ bilinear it is a complex bilinear form, with Gram matrix $G_{ij}=\varphi_{f,w}(e_i,e_j)$ in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ and $\varphi(\sum c_ie_i,\sum d_je_j)=\sum c_iG_{ij}d_j$. For $f$ sesquilinear it is sesquilinear over $(\mathbb{C},\bar{\cdot})$, with the same entries and $\varphi(\sum c_ie_i,\sum d_je_j)=\sum c_iG_{ij}\overline{d_j}$.

**Theorem (the component forms of the twelve).** The three coordinate forms of each vector part have the following classes, Gram matrices and ranks.

| products | class of $\varphi$ | Gram matrix | rank |
|---|---|---|---|
| $\mathrm{GPA}$ | bilinear | neither; symmetric part the $\mathrm{SPA}$ form, alternating part the $\mathrm{APA}$ form | $4$ |
| $\mathrm{GQA}$ | bilinear | alternating | $4$ |
| $\mathrm{SPA}$ | bilinear | symmetric | $2$ |
| $\mathrm{SQA}$ | zero | zero | $0$ |
| $\mathrm{APA}$ | bilinear | alternating | $2$ |
| $\mathrm{GPS}$, $\mathrm{APS}$ | sesquilinear | conjugate-alternating; skew-Hermitian | $4$ |
| $\mathrm{SPS}$ | zero | zero | $0$ |
| $\mathrm{SQS}$ | sesquilinear | conjugate-symmetric; Hermitian | $2$ |
| $\mathrm{AQS}$ | sesquilinear | conjugate-alternating; skew-Hermitian | $2$ |
| $\mathrm{GQS}$ | sesquilinear | sum of a Hermitian rank $2$ and a skew-Hermitian rank $2$ | $4$ |

*Proof.* The ranks and the symmetry types are read from the matrices. For $\mathrm{GPA}$ and $w=\vec e_x$ the matrix is

$$
G_x=
\begin{pmatrix}
0&1&0&0\\
1&0&0&0\\
0&0&0&1\\
0&0&-1&0
\end{pmatrix},
$$

of rank $4$; its symmetric part has rank $2$ and its alternating part rank $2$, and they are the matrices of $V_{\mathrm{SPA}}$ and $V_{\mathrm{APA}}$. The matrices for $w=\vec e_y$ and $w=\vec e_z$ are the cyclic permutations of $G_x$. For $\mathrm{GQA}$ and $w=\vec e_x$ the matrix is

$$
N_x=
\begin{pmatrix}
0&1&0&0\\
-1&0&0&0\\
0&0&0&-1\\
0&0&1&0
\end{pmatrix},
$$

skew of rank $4$; the other two are its cyclic permutations. The zero rows are immediate. For the sesquilinear rows, the Gram matrix of a conjugate-symmetric form is Hermitian and that of a conjugate-alternating form is skew-Hermitian, by the two definitions read in the entries; the ranks are computed from the same matrices. The row of $\mathrm{GQS}$ is the sum of the rows of $\mathrm{SQS}$ and $\mathrm{AQS}$; its Hermitian part is the $\mathrm{SQS}$ matrix, its skew-Hermitian part is the $\mathrm{AQS}$ matrix, and its rank is $4$.

**Remark (the diagonal of a component form).** At the two equal arguments,

$$
\varphi_{f,w}(\tilde Q,\tilde Q)=\bigl(w,D_f(\tilde Q)\bigr).
$$

For a conjugate-symmetric component form this is real, and for a conjugate-alternating one it is purely imaginary; this is the scalar-form reading of the real and imaginary characters of the diagonals of $\mathrm{SQS}$ and of $\mathrm{AQS}$.

## The Relations among the Twelve

The twelve vector parts are linked by the following identities, in which $\tau$ is the swap of the two arguments and the bar is the coefficientwise conjugation.

| identity | content |
|---|---|
| $V_{\mathrm{GQA}}=V_{\mathrm{AQA}}$, $V_{\mathrm{GPS}}=V_{\mathrm{APS}}$, $V_{\mathrm{SQA}}=V_{\mathrm{SPS}}=0$ | the three coincidences |
| $V_{\mathrm{GPA}}=V_{\mathrm{SPA}}+V_{\mathrm{APA}}$, $V_{\mathrm{GQS}}=V_{\mathrm{SQS}}+V_{\mathrm{AQS}}$ | the two reconstructions |
| $V_{\mathrm{GPA}}+V_{\mathrm{GQA}}=2Q_{1t}\vec Q_2$, $V_{\mathrm{GPS}}+V_{\mathrm{GQS}}=-2Q_{1t}\overline{\vec Q_2}$ | the two sums |
| $V_{\mathrm{GQA}}=2Q_{1t}\vec Q_2-V_{\mathrm{GPA}}$, $V_{\mathrm{GQS}}=-2Q_{1t}\overline{\vec Q_2}-V_{\mathrm{GPS}}$ | the two reflections |
| $V_{\mathrm{GPS}}(\tilde Q_1,\tilde Q_2)=V_{\mathrm{GPA}}(\tilde Q_1,\tilde Q_2^{*})$, $V_{\mathrm{GQS}}(\tilde Q_1,\tilde Q_2)=V_{\mathrm{GQA}}(\tilde Q_1,\tilde Q_2^{*})$ | the two slot identities |
| $V_{\mathrm{SPA}}=\tfrac12(V_{\mathrm{GPA}}+V_{\mathrm{GPA}}\circ\tau)$, $V_{\mathrm{APA}}=\tfrac12(V_{\mathrm{GPA}}-V_{\mathrm{GPA}}\circ\tau)$ | the two bilinear halves |
| $V_{\mathrm{SQS}}=\tfrac12(V_{\mathrm{GQS}}+\overline{V_{\mathrm{GQS}}\circ\tau})$, $V_{\mathrm{AQS}}=\tfrac12(V_{\mathrm{GQS}}-\overline{V_{\mathrm{GQS}}\circ\tau})$ | the two sesquilinear halves |

The first row collects the coincidences, the second and third the reconstructions and the two sums, and the rest the reflections, the slot identities and the two half formulas. The scalar parts obey the companion identities of *The Four General Products and Their Relations over the Biquaternion Algebra*, and the two sets together reconstruct the twelve products.

## Summary

The vector parts of the twelve products are vector-valued maps into the complex vector subspace, not scalar forms. The four general products obey one two-bit rule: the first slot fixes the sign of the second mixed term, the second slot fixes the sign of the first mixed term, and the cross term carries the product of the two signs. The twelve vector parts take nine distinct values on the complex space: the two central symmetric products have zero vector part, and the quaternionic bilinear and the plain sesquilinear products share their vector part with their antisymmetric parts. The nine are separated by three pairs of basis elements, and the vector part alone therefore does not determine the product; the pair of the scalar part and the vector part does.

Each product was read with its own properties: its diagonal, its image, its value on pure vectors, its symmetry and its role in the algebra. The diagonals give the vector parts of the squares: $2Q_t\vec Q$ for the plain bilinear pair; zero for the quaternionic bilinear product, the two central symmetric products and the two bilinear antisymmetric products; the Hermitian square $\mathrm{Vec}(\tilde Q\tilde Q^{*})$ for the plain sesquilinear pair; a real vector for $\mathrm{SQS}$; a purely imaginary vector for $\mathrm{AQS}$; and a real-plus-imaginary pair with orthogonal parts for $\mathrm{GQS}$. On the centre all vector parts vanish; on the vector subspace only the cross term survives and the twelve fall to five; on the real subspace they fall to eight; on the Hermitian subspace they fall to seven. The component forms are three scalar forms to a vector part: rank $4$ with a rank-$2$ symmetric and a rank-$2$ alternating part for the plain bilinear product, alternating rank $4$ for the quaternionic bilinear product, Hermitian or skew-Hermitian of rank $2$ or $4$ in the sesquilinear families.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Vec}(\tilde Q)=\vec Q$ | the vector part of an element |
| $\mathrm{Vect}(\mathbb{B})$ | the complex vector subspace, the image of the vector parts |
| $\mathrm{Vect}_{\mathbb{R}}(\mathbb{B})$ | the real vector subspace, the real vectors |
| $V_f(\tilde Q_1,\tilde Q_2)=\mathrm{Vec}(f(\tilde Q_1,\tilde Q_2))$ | the vector part of the product $f$ |
| $D_f(\tilde Q)=V_f(\tilde Q,\tilde Q)$ | the diagonal, the vector part of the square |
| $\varphi_{f,w}(\tilde Q_1,\tilde Q_2)=(w,V_f(\tilde Q_1,\tilde Q_2))$ | the component form in the direction $w$ |
| $\varepsilon$, $\alpha$, $\beta$ | the second-slot bit, the second-slot sign and the first-slot sign of the general rule |
| $\vec Q_2^{\varepsilon}$, $Q_{2t}^{\varepsilon}$ | the second vector part and scalar read with or without the coefficientwise conjugation |
| $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{GPS}$, $\mathrm{GQS}$ | the four general products |
| $\mathrm{SPA}$, $\mathrm{SQA}$, $\mathrm{SPS}$, $\mathrm{SQS}$ | the four symmetric parts |
| $\mathrm{APA}$, $\mathrm{AQA}$, $\mathrm{APS}$, $\mathrm{AQS}$ | the four antisymmetric parts |
| $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ | the centre, the real quaternion subspace and the Hermitian and anti-Hermitian subspaces |

## Further Reading

- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the twelve products, their codes and their scalar and vector parts.
- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the four general products and the splitting identities used here.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the scalar parts and the four degenerate sets.
- [The Biquaternion Algebra](the-biquaternion-algebra.html) and [The Six Subspaces](the-six-subspaces.html), for the basis, the conjugations and the remarkable subspaces.
- [Introduction to the Operators of the Biquaternion Algebra](introduction-to-the-operators-of-the-biquaternion-algebra.html), for the two switches behind the two-bit rule.
- [The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra](the-vector-part-of-the-square-and-the-jacobi-failure-of-the-antisymmetric-plain-sesqualgebra.html), [The Square of an Element](the-square-of-an-element.html) and [The Square of the General Quaternionic Sesquilinear Product and the Two Halves](the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.html), for the diagonals.
- [The Lie Algebra of the Antisymmetric Plain Algebra](the-lie-algebra-of-the-antisymmetric-plain-algebra.html), [The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra](the-jacobi-failure-and-the-associator-defect-of-the-antisymmetric-quaternionic-algebra.html) and [The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra](the-conjugate-cross-product-and-the-jacobi-failure-of-the-antisymmetric-quaternionic-sesqualgebra.html), for the three antisymmetric vector parts and their failures.
- [The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](the-algebraic-structures-over-the-biquaternion-c-space.html), for the names and the laws of the twelve.
