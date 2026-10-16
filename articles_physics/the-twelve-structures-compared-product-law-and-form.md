# __The Twelve Structures Compared: Product, Law and Form__

## Introduction

The biquaternion complex space carries four general products, and each of the four splits into a symmetric and an antisymmetric part, so that one algebra carries **twelve products** and twelve algebraic structures (*The 12 Products of the Biquaternioid Complex Space*, *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*). Each of the twelve has a band of its own in the menu, and each band article reads its own product and its own physical job. This article is the **crossing reader of the twelve bands for the structures**: it sets the twelve products side by side and compares them on one page. It owns nothing of the products themselves; each product, each identity and each physical job is the matter of its band article and of the mathematics articles named below.

The comparison has three axes, and they are the three questions a reader asks of a multiplication.

- The **product** is what the operation computes, read in the coordinates of the algebra: its scalar part and its vector part, and the subspace its values fill.
- The **law** is the identity the operation is asked for, and whether it holds. A general product is asked for associativity; a symmetric part for (conjugate-)commutativity; an antisymmetric part for (conjugate-)alternation. Over and above those, the two classical identities — the **Jordan** identity of a symmetrisation and the **Jacobi** identity of an antisymmetrisation — single out exactly one structure of each kind, and the comparison is mostly the account of the other six failing.
- The **form** is the scalar form the operation carries, together with the definiteness or the signature that the physics of the band reads. It is the axis on which the twelve are the least alike and the axis that decides which of them can measure.

Two mechanisms generate the twelve, and they are the two sections that follow. The first is the **grid of the four general products**, a product with an involution inserted into a slot, which gives the four general products and their four physical jobs. The second is the **class-preserving split** of each general product into its symmetric and its antisymmetric half, which gives the eight parts. The twelve are the four general products together with the eight parts.

**Boundaries.** The comparison of the four general products with one another is *The Four General Products and Their Physical Readings*, which owns the grid, the two slot rules and the signature table of the four forms on the remarkable subspaces. The operators of the twelve, their adjoints and their brackets, are *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*, which follows this article and reads the same twelve through the maps their elements define. The naming of the twelve, the method of the split, the products in coordinates, the laws, the units and the images are the mathematics articles *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* and *The 12 Products of the Biquaternioid Complex Space*. What is added here is the reading of the twelve structures side by side on the three axes, and the placement of each structure by its form.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, the relations $e_k^{2}=-e_0$ and $e_1e_2=e_3$, and central $i$ with $i^{2}=-1$; a general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu=Q_0e_0+\vec Q$ with complex coefficients $Q_\mu$ and vector part $\vec Q=\sum_{k=1}^{3}Q_ke_k$. The natural conjugation ${}^{\natural}$ fixes $i$ and negates $e_1,e_2,e_3$; the coefficientwise conjugation $\bar{\cdot}$ conjugates the four coefficients; the Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, so that $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ with $\varepsilon=(1,-1,-1,-1)$. The scalar part is $\mathrm{Sc}(\tilde X)=X_0$ and the trace is $\mathrm{Tr}=2\,\mathrm{Sc}$; $(\vec P,\vec Q)$ is the complex bilinear dot product and $\vec P\times\vec Q$ the complex bilinear cross product; $\overline{\vec Q}$ is the coefficientwise conjugate of the vector part. The remarkable subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the sectors $\mathbb{M}_{\pm}$, and the quaternion and antiquaternion subspaces $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$. All conventions are those of *Conventions in the Biquaternion Universe*.

## The Grid of the Four General Products

**Definition (a general product with an involution in a slot).** A general product is written

$$
\tilde P\star\tilde Q=K_1(\tilde P)\,K_2(\tilde Q),
$$

where the first factor is read as it stands or through the natural conjugation ${}^{\natural}$, and the second factor as it stands or through the Hermitian conjugation ${}^{*}$, and the multiplication is the plain product of the algebra. Nothing else varies, and ${}^{*}$ is never put in the first slot nor ${}^{\natural}$ in the second, so the four choices are the **four general products**.

The four general products, their closed forms and their physical jobs are the matter of the grid. Each is $\mathbb{C}$-bilinear or sesquilinear over $(\mathbb{C},\bar{\cdot})$, has its own scalar part, and is the general member of one of the four rows below.

| structure | product | scalar part | second slot | physical job |
|---|---|---|---|---|
| GPA (algebra over $\mathbb{C}$) | $\tilde P\tilde Q$ | $P_0Q_0-(\vec P,\vec Q)$ | identity | composition |
| GPS (sesqualgebra over $(\mathbb{C},\bar{\cdot})$) | $\tilde P\tilde Q^{*}$ | $P_0\overline{Q_0}+(\vec P,\overline{\vec Q})$ | ${}^{*}$ | probability |
| GQA (algebra over $\mathbb{C}$) | $\tilde P^{\natural}\tilde Q$ | $P_0Q_0+(\vec P,\vec Q)$ | identity | causality |
| GQS (sesqualgebra over $(\mathbb{C},\bar{\cdot})$) | $\tilde P^{\natural}\tilde Q^{*}$ | $P_0\overline{Q_0}-(\vec P,\overline{\vec Q})$ | ${}^{*}$ | gauge |

### The Two Slot Rules

The grid is decided by two rules, and they are the reason the four rows are not four unrelated products.

The **second slot** decides whether the operation is a **composition** or a **pairing**. Read without a conjugation it is $\mathbb{C}$-bilinear and can be iterated, which is what makes the two **general algebras** over $\mathbb{C}$; read with the star it is sesquilinear over $(\mathbb{C},\bar{\cdot})$ and can only be evaluated, which is what makes the two **general sesqualgebras**. This is the two-and-two division of the four general products.

The **first slot** decides whether the scalar form is **definite on each sector** or carries a **signature**. The natural conjugation ${}^{\natural}$ in the first slot toggles the coefficient $\varepsilon_\mu$ of the scalar form, so the plain rows carry the form $\sum_\mu P_\mu Q_\mu$ or $\sum_\mu P_\mu\overline{Q_\mu}$ and the quaternionic rows the twisted form $\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ or $\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$. It is the slot that turns a definite form into a signed one, and the slot that decides which of the four carries a metric.

## The Split of Each Product into Two Parts

**Definition (the symmetric and the antisymmetric part).** Each general product $f$ is split into a **symmetric part** $f^{\mathrm{s}}$ and an **antisymmetric part** $f^{\mathrm{a}}$ by an exchange of the two arguments that depends on the family. For the two $\mathbb{C}$-bilinear products the exchange is the **bare interchange** of the arguments,

$$
f^{\mathrm{s}}(\tilde P,\tilde Q)=\tfrac12\bigl(f(\tilde P,\tilde Q)+f(\tilde Q,\tilde P)\bigr),
\qquad
f^{\mathrm{a}}(\tilde P,\tilde Q)=\tfrac12\bigl(f(\tilde P,\tilde Q)-f(\tilde Q,\tilde P)\bigr),
$$

and for the two sesquilinear products it is the **conjugate transpose**, the interchange followed by the coefficientwise conjugation of the value,

$$
f^{\mathrm{s}}(\tilde P,\tilde Q)=\tfrac12\bigl(f(\tilde P,\tilde Q)+\overline{f(\tilde Q,\tilde P)}\bigr),
\qquad
f^{\mathrm{a}}(\tilde P,\tilde Q)=\tfrac12\bigl(f(\tilde P,\tilde Q)-\overline{f(\tilde Q,\tilde P)}\bigr).
$$

The exchange is chosen so that **both parts are operations of the same class as the product they split** — $\mathbb{C}$-bilinear for the two bilinear families and sesquilinear over $(\mathbb{C},\bar{\cdot})$ for the two sesquilinear ones — and this class-preservation is the reason the split is the conjugate transpose and not the bare interchange in the sesquilinear case. Each product reconstructs from its two parts, $f=f^{\mathrm{s}}+f^{\mathrm{a}}$, and the pair is unique.

The eight parts, with the two general products repeated for orientation, have the closed forms of the table. The scalar part of an antisymmetric part is $0$ in every row, and its vector part carries the whole operation.

| code | product | scalar part | vector part |
|---|---|---|---|
| GPA | $\tilde P\tilde Q$ | $P_0Q_0-(\vec P,\vec Q)$ | $+P_0\vec Q+Q_0\vec P+\vec P\times\vec Q$ |
| GPS | $\tilde P\tilde Q^{*}$ | $P_0\overline{Q_0}+(\vec P,\overline{\vec Q})$ | $-P_0\overline{\vec Q}+\overline{Q_0}\vec P-\vec P\times\overline{\vec Q}$ |
| GQA | $\tilde P^{\natural}\tilde Q$ | $P_0Q_0+(\vec P,\vec Q)$ | $+P_0\vec Q-Q_0\vec P-\vec P\times\vec Q$ |
| GQS | $\tilde P^{\natural}\tilde Q^{*}$ | $P_0\overline{Q_0}-(\vec P,\overline{\vec Q})$ | $-P_0\overline{\vec Q}-\overline{Q_0}\vec P+\vec P\times\overline{\vec Q}$ |
| SPA | $\tfrac12\bigl(\tilde P\tilde Q+\tilde Q\tilde P\bigr)$ | $P_0Q_0-(\vec P,\vec Q)$ | $+P_0\vec Q+Q_0\vec P$ |
| SPS | $\tfrac12\bigl(\tilde P\tilde Q^{*}+\overline{\tilde Q}\tilde P^{\natural}\bigr)$ | $P_0\overline{Q_0}+(\vec P,\overline{\vec Q})$ | $0$ |
| SQA | $\tfrac12\bigl(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P\bigr)$ | $P_0Q_0+(\vec P,\vec Q)$ | $0$ |
| SQS | $\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural}\bigr)$ | $P_0\overline{Q_0}-(\vec P,\overline{\vec Q})$ | $-P_0\overline{\vec Q}-\overline{Q_0}\vec P$ |
| APA | $\tfrac12\bigl(\tilde P\tilde Q-\tilde Q\tilde P\bigr)$ | $0$ | $\vec P\times\vec Q$ |
| APS | $\tfrac12\bigl(\tilde P\tilde Q^{*}-\overline{\tilde Q}\tilde P^{\natural}\bigr)$ | $0$ | $-P_0\overline{\vec Q}+\overline{Q_0}\vec P-\vec P\times\overline{\vec Q}$ |
| AQA | $\tfrac12\bigl(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P\bigr)$ | $0$ | $P_0\vec Q-Q_0\vec P-\vec P\times\vec Q$ |
| AQS | $\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}\bigr)$ | $0$ | $\vec P\times\overline{\vec Q}$ |

Two remarks fix the reading of the table. First, the **symmetrisation keeps the scalar part of the general product unchanged** and the antisymmetrisation keeps the vector part: for each of the four families the general product and its symmetric part share one scalar part, and the general product and its antisymmetric part share one vector part. Second, in the two sesquilinear families the antisymmetric part is the vector part of the **single value** $f(\tilde P,\tilde Q)$, because the conjugate transpose of that value is its natural conjugate; in the quaternionic sesquilinear family the two orders are not conjugate values and the two parts are the half-sum and the half-difference of the two orders, which is why the values of SQS lie in no subspace of the remarkable subspaces.

## The Twelve Together

The twelve structures are collected in one table. The first five columns are the product and its placement; the last three are the law, the form and the physical job, each read in its own section below.

| code | product | unit | law of its kind | identity of its kind | image | form | physical job |
|---|---|---|---|---|---|---|---|
| GPA | $\tilde P\tilde Q$ | $e_0$, both sides | associative | — | all of $\mathbb{B}$ | $\langle\tilde P,\tilde Q\rangle$ | composition |
| GPS | $\tilde P\tilde Q^{*}$ | $e_0$, right only | not associative | — | all of $\mathbb{B}$ | $\langle\tilde P,\tilde Q\rangle_{*}$ | probability |
| GQA | $\tilde P^{\natural}\tilde Q$ | $e_0$, left only | not associative | — | all of $\mathbb{B}$ | $\langle\tilde P,\tilde Q\rangle_{\natural}$ | causality |
| GQS | $\tilde P^{\natural}\tilde Q^{*}$ | none | not associative | — | all of $\mathbb{B}$ | $\langle\tilde P,\tilde Q\rangle_{\natural*}$ | gauge |
| SPA | $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ | $e_0$, both sides | commutative | **Jordan holds** | all of $\mathbb{B}$ | $\langle\tilde P,\tilde Q\rangle$ | commutativity |
| SPS | $\tfrac12(\tilde P\tilde Q^{*}+\overline{\tilde Q}\tilde P^{\natural})$ | none | conjugate-commutative | Jordan fails, $7$ of $8$ | the centre | $\langle\tilde P,\tilde Q\rangle_{*}$ | positivity |
| SQA | $\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$ | none | commutative | Jordan fails, $6$ of $8$ | the centre | $\langle\tilde P,\tilde Q\rangle_{\natural}$ | coupling |
| SQS | $\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$ | none | conjugate-commutative | Jordan fails, $4$ of $8$ | no subspace | $\langle\tilde P,\tilde Q\rangle_{\natural*}$ | metric |
| APA | $\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)$ | none | alternating | **Jacobi holds** | $\mathrm{Vect}(\mathbb{B})$ | none | rotation |
| APS | $\tfrac12(\tilde P\tilde Q^{*}-\overline{\tilde Q}\tilde P^{\natural})$ | none | conjugate-alternating | Jacobi fails, $252$ of $512$ | $\mathrm{Vect}(\mathbb{B})$ | none | phase |
| AQA | $\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$ | none | alternating | Jacobi fails, $144$ of $512$ | $\mathrm{Vect}(\mathbb{B})$ | none | obstruction |
| AQS | $\tfrac12(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural})$ | none | conjugate-alternating | Jacobi fails, $72$ of $512$ | $\mathrm{Vect}(\mathbb{B})$ | none | polarisation |

Read as a whole, the table has three patterns, and the three comparison sections below take them one at a time. The **units** are carried by four structures and by no others: the two-sided unit $e_0$ by the two plain bilinear structures and by no other pair, the right unit by the general plain sesquilinear product, and the left unit by the general quaternionic product. The **images** fall into four classes — the whole space for the five structures with a scalar or a vector part in both, the centre for the two central-valued symmetric parts, the vector subspace for the four antisymmetric parts, and no remarkable subspace for SQS. The **forms** are carried by eight of the twelve and by no antisymmetric part.

## Compared by Law: Which Identity Survives

**Definition (the law and the identity of a structure).** Each of the twelve is asked for the law of its kind: associativity for a general product, (conjugate-)commutativity for a symmetric part, (conjugate-)alternation for an antisymmetric part. In addition, a symmetrisation is a **Jordan** product exactly when it satisfies the Jordan identity $\tilde X^{2}\bullet(\tilde Y\bullet\tilde X)=(\tilde X^{2}\bullet\tilde Y)\bullet\tilde X$ with $\tilde X^{2}=\tilde X\bullet\tilde X$, and an antisymmetrisation is a **Lie** product exactly when it satisfies the Jacobi identity in the cyclic form of the conventions of *The 12 Products of the Biquaternioid Complex Space*.

### The Two Classical Products

Of the twelve, exactly two are the product of a classical nonassociative algebra, and both belong to the plain family.

- **SPA** is commutative and satisfies the Jordan identity, so it is a **Jordan** product. It is the special Jordan algebra of degree two, and its Hermitian subspace is the Hermitian Jordan algebra $J(\mathbb{B})$.
- **APA** is alternating and satisfies the Jacobi identity, so it is a **Lie** product. It is the Lie algebra of *The Unitary Lie Algebra*, with the vector subspace a Lie subalgebra isomorphic to $\mathfrak{sl}(2,\mathbb{C})$ and the anti-Hermitian subspace $\mathfrak{u}(2)$.

That the two are the plain ones and not the quaternionic ones is the comparison content of the law axis: the two slot rules that generate the twelve do not touch the plain row's identities, and the natural conjugation in the first slot is what breaks them. The general products are neither symmetrisations nor antisymmetrisations, so neither identity is put to them; among the twelve only GPA is associative.

### The Six Failures

The other six parts fail the identity of their kind, each on a named witness, and the counts over the eight-element basis of the corpus record the shape of the failure.

| structure | identity | witness | value on the witness | count on the eight-element basis |
|---|---|---|---|---|
| SPS | Jordan | $\tilde X=e_1$ | the sides are $0$ and $e_0$ | $7$ of $8$ |
| SQA | Jordan | $\tilde X=e_1$ | the sides are $0$ and $e_0$ | $6$ of $8$ elements |
| SQS | Jordan | $\tilde X=e_1$ | the sides are $-e_0$ and $e_0$ | $4$ of $8$ |
| APS | Jacobi | $(e_0,e_1,e_2)$ | $e_3$ | $252$ of $512$ |
| AQA | Jacobi | $(e_0,e_1,e_2)$ | $-e_3$ | $144$ of $512$ triples |
| AQS | Jacobi | $(e_1,e_1,ie_2)$ | $-2ie_2$ | $72$ of $512$ |

The three Jacobi failures have three different reasons. For APS and AQS the reason is the **obstruction of the sesquilinear antisymmetrisation**, which is a Lie bracket only after the collapse of the two involutions that a genuine sesqualgebra forbids (*Lie Algebras of Sesqualgebras*); for AQA it is the **non-associativity** of the general quaternionic product it comes from. The three Jordan failures are witnessed on the same element and are of two shapes: the outright vanishing of SPS and SQA, whose symmetric square on $e_1$ is $e_0$, and the central shift of SQS, whose symmetric square on $e_1$ is $-e_0$, differing by $2e_0$ rather than by $e_0$.

**Caution on the counts.** The counts are counts on a chosen basis and are not invariants of the operation; they are given as the **shape** of each failure and they change with the basis. What is invariant is the existence of the failure and its witness. The one structural distinction the counts carry is that the Jacobi failure of AQS is the sparsest and the only one whose witness needs a complex element off the real basis, so it is the failure invisible on the real forms; the failure of APS is the densest, failing on half the triples.

## Compared by Form: What Each Structure Measures

The form axis is where the twelve are the least alike, and it is decided by one principle and one slot rule.

**Principle (the scalar part fixes the form).** For the two bilinear rows the scalar part of the product is **symmetric**, $\mathrm{Sc}(\tilde P\tilde Q)=\mathrm{Sc}(\tilde Q\tilde P)$ and $\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=\mathrm{Sc}(\tilde Q^{\natural}\tilde P)$; for the two sesquilinear rows it is **Hermitian**, $\mathrm{Sc}(\tilde P\tilde Q^{*})=\overline{\mathrm{Sc}(\tilde Q\tilde P^{*})}$ and $\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\overline{\mathrm{Sc}(\tilde Q^{\natural}\tilde P^{*})}$. The antisymmetric part of a product has scalar part $0$ by construction, so it carries no form at all; the symmetric part keeps the scalar part of the general product unchanged, so it carries the same form as the general product. Hence **exactly four scalar forms are carried**, each by the general and the symmetric member of its family, and the four antisymmetric parts carry none.

The four forms are one bilinear form read through the two involutions,

$$
\langle\tilde P,\tilde Q\rangle_{*}=\langle\tilde P,\tilde Q^{*}\rangle,
\qquad
\langle\tilde P,\tilde Q\rangle_{\natural}=\langle\tilde P^{\natural},\tilde Q\rangle,
\qquad
\langle\tilde P,\tilde Q\rangle_{\natural*}=\langle\tilde P^{\natural},\tilde Q^{*}\rangle,
$$

so that the dial ${}^{\natural}$ is what produces a metric and the star is what produces a pairing, the two operations commuting. Written out, the four are $B=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$, $H=\sum_\mu P_\mu\overline{Q_\mu}$, $N=\sum_\mu P_\mu Q_\mu$ and $K=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$.

| form | row | type | definiteness and signature |
|---|---|---|---|
| $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)$ | GPA, SPA | symmetric $\mathbb{C}$-bilinear | $+\mathrm{I}_4$ on $\mathbb{M}_+$, $-\mathrm{I}_4$ on $\mathbb{M}_-$; signature $(4,4)$ on $\mathbb{B}$ |
| $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$ | GPS, SPS | Hermitian | positive definite, of signature $(8,0)$; the Born pairing |
| $\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$ | GQA, SQA | symmetric $\mathbb{C}$-bilinear | the interval; indefinite, of signature $(3,1)$ on $\mathbb{M}_-$; null set the light cone |
| $\langle\tilde P,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})$ | GQS, SQS | Hermitian | indefinite; inertia $(1,3)$ over the complex coefficients, $(2,6)$ over the real parameters |

The form axis is the sharpest structural division of the twelve, and it is the form and not the product that carries the physics of the band. Two structures of the table carry a **definite** form on each sector and so can measure a length; these are the plain bilinear $\langle\tilde P,\tilde Q\rangle$ and the plain sesquilinear $\langle\tilde P,\tilde Q\rangle_{*}$, and they are the two structures the framework reads as composition and as probability. Two carry an **indefinite** form and so carry a metric with a light cone or a Krein signature; these are the quaternionic $\langle\tilde P,\tilde Q\rangle_{\natural}$ and $\langle\tilde P,\tilde Q\rangle_{\natural*}$, read as causality and as gauge. The four antisymmetric parts carry no form and so measure nothing: they are the structures of order, of rotation and of phase, and their scalar part is identically zero.

## Compared by Image and Unit

Two further columns of the master table separate the twelve as cleanly as the law and the form.

### The Image

The image of a product is the subspace its values fill, and it falls into three classes.

- The **whole space** $\mathbb{B}$ is the image of the five structures whose value has both a scalar and a vector part in general: the four general products, where no term is forced to vanish, and the symmetric plain bilinear product SPA, whose cross term drops but which still reaches every direction through $P_0\vec Q+Q_0\vec P$.
- The **centre** $\mathbb{C}_{\mathbb{B}}$ is the image of the two central-valued symmetric parts SPS and SQA, whose closed forms are scalar multiples of $e_0$. A central-valued product is a **measurement** and not a composition: its value is a number, not an element that can be fed back into the product.
- The **vector subspace** $\mathrm{Vect}(\mathbb{B})$ is the image of the four antisymmetric parts, whose scalar part vanishes identically.

The one structure whose image is in no remarkable subspace is **SQS**: its value is the sum of a central scalar and a mixed vector term that is a multiple of neither the centre nor a fixed direction, so no subspace of the remarkable subspaces contains all its values.

### The Unit

$e_0$ is a unit of a structure exactly when the structure is the plain product read symmetrically enough. The two-sided unit is carried by exactly two structures, GPA and SPA, and it is the same fact: the symmetrisation drops the cross term, which is the term that stops a plain product from being commutative, and it leaves $e_0$ a unit. The general plain sesquilinear product GPS has $e_0$ as a **right** unit only, because the star conjugates the second factor; the general quaternionic product GQA has $e_0$ as a **left** unit only, because the natural conjugation of the second factor reads the parameter, not the argument. No other structure has a unit, and in particular no antisymmetric part has one and the fourth general product GQS has none on either side.

## The Twelve on the Real Forms: Twelve to Ten

The twelve structures are pairwise distinct on the complex space, but on the **real part** — the real span of $e_0,e_1,e_2,e_3$, where the coefficientwise conjugation fixes every element — two pairs coincide, and the twelve fall to ten. The two coincidences are

$$
\mathrm{SPS}=\mathrm{SQA}
\qquad\text{and}\qquad
\mathrm{APA}=\mathrm{AQS}
\qquad\text{on the real part,}
$$

because on a real vector the coefficientwise conjugation is the identity, so the symmetric plain sesquilinear product collapses to the quaternionic scalar form of SQA, and the antisymmetric quaternionic sesquilinear product $\vec P\times\overline{\vec Q}$ becomes the plain cross product $\vec P\times\vec Q$ of APA. A third distinction also disappears: the Jacobi failure of AQS, whose witness is $(e_1,e_1,ie_2)$ and needs a complex element, is **invisible on the real forms**, so the parity of APA and AQS, which the Jacobi identity separates on the complex space, is not separated on the real one.

The real-form collapse is the reason the corpus says the twelve are twelve on the complex space and ten on the real part, and it is the one place where the complex dimension of the coefficient field, and not the algebra alone, decides a comparison. The three failures of the Jacobi kind are one on the real forms and two proper to the complex ones, and the one proper to AQS is the one whose witness carries the central imaginary.

## The Ledger

**Proved.** The twelve products, their closed forms, their scalar and vector parts, their units, their laws and their images are the mathematics of *The 12 Products of the Biquaternioid Complex Space*, recomputed here on the eight-element basis: the four general products are the four insertions of an involution into a slot; the eight parts are the class-preserving symmetrisation and antisymmetrisation of the four; exactly one general product is associative, exactly one symmetric part satisfies the Jordan identity and exactly one antisymmetric part satisfies the Jacobi identity, the two being the plain ones SPA and APA; the six other parts fail, with the witnesses and counts of the table; exactly four scalar forms are carried, by the general and the symmetric member of each family, and the antisymmetric parts carry none; the four forms are one bilinear form read through the two involutions, $H=\langle\tilde P,\tilde Q^{*}\rangle$, $N=\langle\tilde P^{\natural},\tilde Q\rangle$, $K=\langle\tilde P^{\natural},\tilde Q^{*}\rangle$; the units are carried by GPA, GPS, GQA and SPA alone; the images are the whole space, the centre or the vector subspace; and on the real part the twelve fall to ten through $\mathrm{SPS}=\mathrm{SQA}$ and $\mathrm{APA}=\mathrm{AQS}$.

**Interpretations.** That the four general products are the four jobs a relativistic quantum theory needs — composition, probability, causality and gauge — and that the symmetric and antisymmetric parts of each carry the two halves of the job's word; that a central-valued symmetric part is a **measurement** and not a composition; that the definite forms are the ones that measure and the indefinite ones the ones that carry a metric; and that the complex dimension is what keeps the twelve distinct, the real part merging two pairs and hiding one failure. Each is the framework's naming of a proved algebraic fact and is labelled as such in the band articles and in *The Four General Products and Their Physical Readings*.

## Physical Interpretation

The twelve structures are one algebra read in twelve products, and the comparison reads the physical content as the placement of each structure on the three axes.

The **product** axis carries the four jobs and their halves. The general product of a row is the operation the band is named for — composition, probability, causality, gauge — and the symmetric part is the half that measures or couples, the antisymmetric part the half that orders, rotates or phases. The **law** axis carries the two classical structures: the plain commutativity SPA, which is the Jordan algebra of the observables, and the plain rotation APA, which is the Lie algebra of the frame, are the only two of the twelve that are the product of a classical nonassociative algebra, and they are the two the menu names commutativity and rotation. The **form** axis carries the division between the structures that measure and the structures that only act: the plain bilinear and plain sesquilinear forms are definite on each sector and carry the two definite readings, the sector sign $\langle\tilde P,\tilde Q\rangle$ and the Born weight $\langle\tilde P,\tilde Q\rangle_{*}$, while the quaternionic forms are indefinite and carry the two metric readings, the interval $\langle\cdot\rangle_{\natural}$ and the Krein metric $\langle\tilde P,\tilde Q\rangle_{\natural*}$.

Read the three axes together, and the twelve fall into four columns of three. Each column is one family, and within it the general product is the operation, the symmetric part is the quantity, and the antisymmetric part is the order or the phase. The four columns are the four jobs; the three rows are the operation, the measurable half and the ordered half; and the two classical structures — the Jordan product SPA and the Lie product APA, the only two of the twelve that are the product of a classical nonassociative algebra — are the observables and the rotations the physics of the frame asks for. The comparison adds no product and no theorem; it is the map on which the twelve band articles and the mathematics articles meet.

## Summary

The biquaternion complex space carries twelve products, and this article compares them on three axes: the **product** each computes, the **law** each obeys, and the **form** each carries. The twelve are generated by the grid of the four general products — the four insertions of an involution into a slot — together with the class-preserving split of each general product into a symmetric and an antisymmetric part. Of the twelve, exactly one general product is associative (GPA); exactly two structures are the product of a classical nonassociative algebra, the Jordan product SPA and the Lie product APA, both plain; the six other parts fail the identity of their kind, with the witnesses and counts of the table, and the failure of AQS is invisible on the real forms. Exactly four scalar forms are carried, each by the general and the symmetric member of its family, and they are one bilinear form read through the two involutions, the sector sign $\langle\tilde P,\tilde Q\rangle$, the positive Born form $\langle\tilde P,\tilde Q\rangle_{*}$, the interval $\langle\cdot\rangle_{\natural}$ and the indefinite Krein form $\langle\tilde P,\tilde Q\rangle_{\natural*}$; the four antisymmetric parts carry no form and measure nothing. The units are carried by GPA and SPA on both sides, by GQA on the left, by GPS on the right and by no other structure; the images are the whole space for the four general products and SPA, the centre for SPS and SQA, the vector subspace for the four antisymmetric parts, and no remarkable subspace for SQS. On the real part the twelve fall to ten, through $\mathrm{SPS}=\mathrm{SQA}$ and $\mathrm{APA}=\mathrm{AQS}$. The comparison is the map on which the twelve band articles and the mathematics articles meet; it adds no product and no theorem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm G$, $\mathrm S$, $\mathrm A$ (first letter) | the general product, its symmetric part, its antisymmetric part |
| $\mathrm P$, $\mathrm Q$ (second letter) | the plain first slot, the quaternionic first slot |
| $\mathrm A$, $\mathrm S$ (third letter) | the family: the algebra over $\mathbb{C}$, the sesqualgebra over $\mathbb{C}$ |
| $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{SPA}$, $\mathrm{SQA}$, $\mathrm{APA}$, $\mathrm{AQA}$ | the six structures of the two algebras over $\mathbb{C}$ |
| $\mathrm{GPS}$, $\mathrm{GQS}$, $\mathrm{SPS}$, $\mathrm{SQS}$, $\mathrm{APS}$, $\mathrm{AQS}$ | the six structures of the two sesqualgebras over $\mathbb{C}$ |
| $B=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ | the general plain bilinear form, the scalar part of GPA and SPA |
| $H=\sum_\mu P_\mu\overline{Q_\mu}$ | the general plain sesquilinear form, the scalar part of GPS and SPS; the Born pairing |
| $N=\sum_\mu P_\mu Q_\mu$ | the general quaternionic bilinear form, the scalar part of GQA and SQA; the interval |
| $K=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | the general quaternionic sesquilinear form, the scalar part of GQS and SQS; the Krein form |
| Jordan, Jacobi | the two identities that single out SPA and APA |
| $(\vec P,\vec Q)$, $\vec P\times\vec Q$, $\overline{\vec Q}$ | the bilinear dot product, the bilinear cross product and the conjugate of the vector part |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{M}_{\pm}$ | the centre, the vector subspace and the two sectors |

## Further Reading

- Mathematics article *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the naming of the twelve, the three letters of each code, and the two identities that single out SPA and APA.
- Mathematics article *The 12 Products of the Biquaternioid Complex Space* (`articles_maths/the-12-products-of-the-biquaternioid-complex-space.md`), for the products and their parts in coordinates, the method of the decomposition, the table of the twelve with their laws, units and images, and the counts of the failures.
- Mathematics article *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the property table of the four general products and the short computation that decides each entry.
- Mathematics article *The Symmetric and Antisymmetric Parts of an Algebra Product* and *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, for the two definitions of the split and the class-preserving exchange.
- Mathematics article *Lie Algebras of Sesqualgebras*, for the obstruction that fails the Jacobi identity of the two sesquilinear antisymmetrisations, and *The Unitary Lie Algebra* and *The Hermitian Jordan Algebra* for the two structures that pass.
- Companion article *The Four General Products and Their Physical Readings*, for the grid, the two slot rules and the signature table of the four forms on the remarkable subspaces.
- Companion article *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*, for the same twelve read through the maps their elements define.
- Companion article *The Bilinear Product on the Biquaternion Space*, for the sector sign $\langle\tilde P,\tilde Q\rangle$ and the composition reading of the plain product, and *The Biquaternioid General Quaternionic Algebra (GQA) over $\mathbb{C}$*, for the interval $\langle\cdot\rangle_{\natural}$ read as the square of a product.
- Companion article *The Biquaternioid General Plain Sesqualgebra (GPS) over $\mathbb{C}$*, for the positivity of $\langle\tilde P,\tilde Q\rangle_{*}$ and the Born pairing, and *The Biquaternioid General Quaternionic Sesqualgebra (GQS) over $\mathbb{C}$*, for the indefiniteness of the Krein form $\langle\tilde P,\tilde Q\rangle_{\natural*}$.
- Companion article *Conventions in the Biquaternion Universe*, for the conventions of the algebra, its conjugations and its subspaces.
