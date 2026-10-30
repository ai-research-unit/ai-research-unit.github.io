# __Conventions of the Products and the Forms__

## Introduction

The algebra carries twelve products and four forms. This article fixes their names, their codes and the letters of the forms, and it stops at the form: the norm is the form read at its two equal arguments and is the subject of *Conventions of the Norms and the Unitary Convention*.

The products come first because they are algebraic and need no form. Four general products answer the four choices of conjugation on the two slots, and each splits into a symmetric and an antisymmetric part. The three-letter code names the operation by its first letter and the two slots by the second and the third, and the same code is read on the reduced biquaternion space, where four of the twelve name no new operation.

The form comes second. A form is the scalar part of a product, with a conjugation named on each slot; the corpus writes a generic form $\mathrm{Form}(\tilde Q_1,\tilde Q_2)$, and the four brackets $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ name the four. The letters $P$, $N$, $H$ and $K$ name each form with two arguments and the corresponding norm with one, and the last section fixes how the names are read in a layer.

The article assumes the base of *Conventions in Mathematics*; the norm is read in the companion article, and the calculus that applies the forms to the gradient in *Conventions of the Operators and the Calculus*.

## The Twelve Products and Their Names

The algebra carries **four general products** — one to each of the four choices of the two slots, the first factor read as it stands or through ${}^{\natural}$ and the second as it stands or through ${}^{*}$ — and each of the four splits into a **symmetric part** and an **antisymmetric part**, so that the complex space carries **twelve products** in all. The names are these, with the three-letter code the band articles write them by:

| The general product | Its symmetric part | Its antisymmetric part |
|---|---|---|
| The general plain bilinear product ($\mathrm{GPA}$) | The symmetric plain bilinear product ($\mathrm{SPA}$) | The antisymmetric plain bilinear product ($\mathrm{APA}$) |
| The general quaternionic bilinear product ($\mathrm{GQA}$) | The symmetric quaternionic bilinear product ($\mathrm{SQA}$) | The antisymmetric quaternionic bilinear product ($\mathrm{AQA}$) |
| The general plain sesquilinear product ($\mathrm{GPS}$) | The symmetric plain sesquilinear product ($\mathrm{SPS}$) | The antisymmetric plain sesquilinear product ($\mathrm{APS}$) |
| The general quaternionic sesquilinear product ($\mathrm{GQS}$) | The symmetric quaternionic sesquilinear product ($\mathrm{SQS}$) | The antisymmetric quaternionic sesquilinear product ($\mathrm{AQS}$) |

**The code is read letter by letter.** The first letter says which of the three operations of a row — $\mathrm G$ the general product, $\mathrm S$ its symmetric part, $\mathrm A$ its antisymmetric part; the second says which of the two products — $\mathrm P$ the plain one, whose first slot is read as it stands, and $\mathrm Q$ the one whose first slot carries the intrinsic conjugation, ${}^{\natural}$ in the quaternionic layers and ${}_{\mathrm{ts}}$ in $\mathbb{B}_{\mathrm{r}}$; and the third says the family — $\mathrm A$ the **algebra** over $\mathbb{C}$, whose three products are $\mathbb{C}$-bilinear, and $\mathrm S$ the **sesqualgebra** over $(\mathbb{C},\bar{\cdot})$, whose three products are sesquilinear. The four general products are the multiplications of the four general structures; the eight parts are the symmetric and antisymmetric products beside them; and the twelve codes together name the twelve algebraic structures of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**The same code on the reduced biquaternion space.** The construction is not special to $\mathbb{B}$. On the commutative algebra $\mathbb{B}_{\mathrm{r}} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{C} \cong \mathbb{C}\oplus\mathbb{C}$ — the reduced biquaternions, equivalently the tessarines or the double-complex numbers — the same four general products exist, $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{GPS}$ and $\mathrm{GQS}$, and each splits into a symmetric and an antisymmetric part by the two exchanges. Because the algebra is **commutative**, four of the twelve codes name no new operation there: $\mathrm{SPA} = \mathrm{GPA}$ and $\mathrm{SQS} = \mathrm{GQS}$, while $\mathrm{APA} = 0$ and $\mathrm{AQS} = 0$. The space therefore carries **eight distinct algebraic structures** — $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{GPS}$, $\mathrm{GQS}$ and the four live halves $\mathrm{SQA}$, $\mathrm{AQA}$, $\mathrm{SPS}$, $\mathrm{APS}$ — and the twelve slots, the four that collapse and the eight that remain are *The Four Products, Their Forms and Their Algebraic Norms* and *The Specificities of the Algebra of the Reduced Biquaternions*. The letter $\mathrm Q$ keeps its sense there — the first slot read through ${}_{\mathrm{ts}}$, the tessarine conjugation $j\mapsto-j$ (and $ij\mapsto-ij$) — as in the band above.

**The definitions.** Write the two elements $\tilde Q_1=Q_{1t}e_t+\vec Q_1$ and $\tilde Q_2=Q_{2t}e_t+\vec Q_2$, with $\vec Q_1=(Q_{1x},Q_{1y},Q_{1z})$ and $\vec Q_2=(Q_{2x},Q_{2y},Q_{2z})$; $(\vec Q_1,\vec Q_2)$ is the Euclidean inner product, $\vec Q_1\times\vec Q_2$ the cross product in the units $\vec e_x,\vec e_y,\vec e_z$, and $\overline{\vec Q_2}$ the coefficientwise conjugation. Every product is the sum of a scalar part, a multiple of $e_t$, and a vector part.

**The four general products**, one to each choice of the two slots.

**The general plain bilinear product**, the multiplication of the algebra, associative, with $e_t$ a unit on both sides:

$$
\tilde Q_1\tilde Q_2=\bigl[Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)\bigr]+Q_{1t}\vec Q_2+Q_{2t}\vec Q_1+\vec Q_1\times\vec Q_2 .
$$

**The general plain sesquilinear product**, the second factor read through ${}^{*}$, not associative, with $e_t$ a unit on the right only:

$$
\tilde Q_1\tilde Q_2^{*}=\bigl[Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})\bigr]-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2} .
$$

**The general quaternionic bilinear product**, the first factor read through ${}^{\natural}$, not associative, with $e_t$ a unit on the left only:

$$
\tilde Q_1^{\natural}\tilde Q_2=\bigl[Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)\bigr]+Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2 .
$$

**The general quaternionic sesquilinear product**, both slots read through a conjugation, not associative, with a unit on neither side:

$$
\tilde Q_1^{\natural}\tilde Q_2^{*}=\bigl[Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})\bigr]-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1+\vec Q_1\times\overline{\vec Q_2} .
$$

**The four symmetric parts**, written with the **full dot** $\bullet$, the four half-sums under the exchange that keeps the class of the product — the interchange for the two bilinear products, the conjugate transpose for the two sesquilinear ones. The subscript names the slots as it does for the forms: none for the plain bilinear product, ${}_{\natural}$ for the quaternionic bilinear, ${}_{*}$ for the plain sesquilinear and ${}_{\natural*}$ for the quaternionic sesquilinear.

**The symmetric plain bilinear product**, the half-sum of the two orders, the **Jordan product** $\tilde Q_1\bullet\tilde Q_2$, written $\star$ in the symmetric-plain band of the physics corpus:

$$
\tilde Q_1\bullet\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1\bigr)=\bigl[Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)\bigr]+Q_{1t}\vec Q_2+Q_{2t}\vec Q_1 .
$$

**The symmetric plain sesquilinear product**, the half-sum under the conjugate transpose, the **Hermitian form** $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$, central-valued:

$$
\tilde Q_1\bullet_{*}\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}+(\tilde Q_1\tilde Q_2^{*})^{\natural}\bigr)=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\bigl[Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})\bigr] .
$$

**The symmetric quaternionic bilinear product**, the half-sum of the two orders, the **quaternion form** $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$, central-valued:

$$
\tilde Q_1\bullet_{\natural}\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2+\tilde Q_2^{\natural}\tilde Q_1\bigr)=\bigl[Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)\bigr] .
$$

**The symmetric quaternionic sesquilinear product**, the half-sum under the conjugate transpose:

$$
\tilde Q_1\bullet_{\natural*}\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}+\tilde Q_2^{*}\tilde Q_1^{\natural}\bigr)=\bigl[Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})\bigr]-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1 .
$$

**The four antisymmetric parts**, written with the **wedge** $\wedge$, the four half-differences under the same exchange; all four have zero scalar part and lie in the vector subspace.

**The antisymmetric plain bilinear product**, the half-difference of the two orders, the **outer product** $\tilde Q_1\wedge\tilde Q_2$:

$$
\tilde Q_1\wedge\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1\bigr)=\vec Q_1\times\vec Q_2 .
$$

**The antisymmetric plain sesquilinear product**, the half-difference under the conjugate transpose, the vector part $\mathrm{Vect}(\tilde Q_1\tilde Q_2^{*})$:

$$
\tilde Q_1\wedge_{*}\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}-(\tilde Q_1\tilde Q_2^{*})^{\natural}\bigr)=\mathrm{Vect}(\tilde Q_1\tilde Q_2^{*})=-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2} .
$$

**The antisymmetric quaternionic bilinear product**, the half-difference of the two orders:

$$
\tilde Q_1\wedge_{\natural}\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1\bigr)=Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2 .
$$

**The antisymmetric quaternionic sesquilinear product**, the half-difference under the conjugate transpose, the cross product $\vec Q_1\times\overline{\vec Q_2}$:

$$
\tilde Q_1\wedge_{\natural*}\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}-\tilde Q_2^{*}\tilde Q_1^{\natural}\bigr)=\vec Q_1\times\overline{\vec Q_2} .
$$

**The reconstruction.** The dot and the wedge rebuild the four general products, so the eight parts carry the whole content of the twelve, one identity to a slot:

$$
\tilde Q_1\tilde Q_2=\tilde Q_1\bullet\tilde Q_2+\tilde Q_1\wedge\tilde Q_2,\qquad
\tilde Q_1\tilde Q_2^{*}=\tilde Q_1\bullet_{*}\tilde Q_2+\tilde Q_1\wedge_{*}\tilde Q_2,\qquad
\tilde Q_1^{\natural}\tilde Q_2=\tilde Q_1\bullet_{\natural}\tilde Q_2+\tilde Q_1\wedge_{\natural}\tilde Q_2,\qquad
\tilde Q_1^{\natural}\tilde Q_2^{*}=\tilde Q_1\bullet_{\natural*}\tilde Q_2+\tilde Q_1\wedge_{\natural*}\tilde Q_2 .
$$

**The two antisymmetrisations are not one.** The eight parts above come from the exchange that keeps the class of the product; the **bare interchange** of the two arguments gives a second antisymmetrisation and different objects — the symmetrised sesquilinear product and the **sesquilinear commutator**,

$$
[\tilde Q_1,\tilde Q_2]_\varsigma=\tilde Q_1\tilde Q_2^{*}-\tilde Q_2\tilde Q_1^{*},
$$

whose values lie in the skew-Hermitian part. **The full dot $\bullet$ and the wedge $\wedge$ are reserved for the exchange that keeps the class of the product, so neither names the objects of this paragraph.** The two are not the same operation (*Symmetric and Antisymmetric Decomposition of the Four General Products*; *The Sesquilinear Commutator and the Symmetrised Product on the Biquaternion*), and the current of a scalar field is the commutator, $\tilde J=i[\tilde\Phi^{*}(\tilde\nabla\tilde\Phi)-(\tilde\nabla\tilde\Phi^{*})\tilde\Phi]$.

The products themselves — their coordinates, their laws, their units and their images — are *Symmetric and Antisymmetric Decomposition of the Four General Products*, and the grid of the four general products is *The Four General Products and Their Relations over the Biquaternion Algebra*.

## The Form Convention

**The order is product, then form, then norm.** A form is the scalar part of a product, with a conjugation named on each slot; the norm is that form at its two equal arguments, and it is read in *Conventions of the Norms and the Unitary Convention*. The product comes first and needs no form: the four general products are algebraic, and only their scalar parts are forms.

The corpus writes a **generic form** and a **generic norm**, the norm being the form read at its two equal arguments:

$$
\mathrm{Form}(\tilde Q_1,\tilde Q_2) , \qquad \mathrm{Norm}(\tilde Q) = \mathrm{Form}(\tilde Q,\tilde Q) .
$$

**One bracket, two arities.** A **bracket** names a **form** when it carries two arguments and its **algebraic norm** when it carries one, the single argument standing for the two equal ones. Each form is built from its own conjugation in the first argument and its own in the second, and the bracket's subscript records the two. Written out, the **plain form** is

$$
\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2) , \qquad \langle\tilde Q\rangle=\langle\tilde Q,\tilde Q\rangle ,
$$

the **quaternionic form** is

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2) , \qquad \langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural} ,
$$

the **Hermitian form** is

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*}) , \qquad \langle\tilde Q\rangle_{*}=\langle\tilde Q,\tilde Q\rangle_{*} ,
$$

and the **Krein form** is

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*}) , \qquad \langle\tilde Q\rangle_{\natural*}=\langle\tilde Q,\tilde Q\rangle_{\natural*} .
$$

**One letter, two arities.** The four also carry one letter each, $P$ for the plain, $N$ for the quaternionic, $H$ for the Hermitian and $K$ for the Krein, the letter naming the form with two arguments and the algebraic norm with one: $P(\tilde Q_1,\tilde Q_2)$ is the plain form and $P(\tilde Q)$ the plain norm, and the same holds for the other three. The plain norm is written $P$ and not $B$, because $B$ is the complex modulus of the vector part, $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$, and $B(\tilde Q)$ is the right annihilator of the plain product. **$P$ is the scalar part of the plain product**, with no conjugation on either slot: it is not the plain product, and it is not a reading of $N$. The letters and the four qualified notions of a regular and a degenerate biquaternion are those of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, §*Regular and Degenerate Biquaternions*.

**The bracket carries the mark that is not the identity in the layer**, and the four brackets collapse two-and-two wherever one mark degenerates. The cases are worked layer by layer in *Conventions of the Norms and the Unitary Convention*, §*The Six Layer Tables*.

The distinction is one of **notation, not of substance**: the pair is the form and the norm of the statement at hand. The two definitions — the form of an operation as its scalar part read in two arguments, bilinear or sesquilinear by its second slot, and the algebraic norm as that form at its two equal arguments — and the four brackets, $\langle\cdot,\cdot\rangle$ the plain, $\langle\cdot,\cdot\rangle_{*}$ the Hermitian, $\langle\cdot,\cdot\rangle_{\natural}$ the quaternionic and $\langle\cdot,\cdot\rangle_{\natural*}$ the Krein, are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*.

**The four names stand on the four scalar parts.** One name runs over the three levels of the product, the form and the norm: the form is the scalar part of the product in the named slots, and the norm is the form at two equal arguments. The **plain** bracket is the scalar part of the plain bilinear product, the **quaternionic** bracket that of the quaternionic bilinear product, the **Hermitian** bracket that of the plain sesquilinear product, and the **Krein** bracket that of the quaternionic sesquilinear product. Read on one argument the four are the **plain norm**, the **Hermitian norm**, the **quaternionic norm** and the **Krein norm**. The four products, their forms and their norms go together, one to a row:

| Product | Form | Letter | Norm |
|---|---|---|---|
| the general plain bilinear | $\langle\tilde Q_1,\tilde Q_2\rangle$ | $P$ | the plain norm $\langle\tilde Q\rangle$ |
| the general quaternionic bilinear | $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$ | $N$ | the quaternionic norm $\langle\tilde Q\rangle_{\natural}$ |
| the general plain sesquilinear | $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$ | $H$ | the Hermitian norm $\langle\tilde Q\rangle_{*}$ |
| the general quaternionic sesquilinear | $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$ | $K$ | the Krein norm $\langle\tilde Q\rangle_{\natural*}$ |

**The names are read in the layer where the map they mark exists.** In $\mathbb{B}_{\mathrm{r}}$ the **quaternionic** name becomes the **tessarine** and the **Krein** name the **tessarine-Hermitian**, their brackets carrying ${}_{\mathrm{ts}}$ and ${}_{\mathrm{ts}*}$; the plain and the Hermitian keep their names.

## Summary

The algebra carries four general products, one to each choice of the conjugation on the two slots: the general plain bilinear, the general quaternionic bilinear, the general plain sesquilinear and the general quaternionic sesquilinear. Each splits into a symmetric and an antisymmetric part, so that the twelve names are the four general products, their four symmetric parts and their four antisymmetric parts. The code is read letter by letter: $\mathrm G$, $\mathrm S$ or $\mathrm A$ for the operation, $\mathrm P$ or $\mathrm Q$ for the first slot, $\mathrm A$ or $\mathrm S$ for the second. On the reduced biquaternion space the algebra is commutative and four of the twelve collapse, leaving eight distinct structures.

A form is the scalar part of a product, with a conjugation named on each slot, and the generic form is $\mathrm{Form}(\tilde Q_1,\tilde Q_2)$; the generic norm is that form at its two equal arguments. A bracket names the form with two arguments and the algebraic norm with one, its subscript recording the pair of slots. The plain bracket is $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, the quaternionic $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$, the Hermitian $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ and the Krein $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})$.

The four letters are $P$ for the plain, $N$ for the quaternionic, $H$ for the Hermitian and $K$ for the Krein, each naming the form with two arguments and the norm with one. The bracket carries the mark that is not the identity in the layer, and the four collapse two-and-two wherever a mark degenerates. In the reduced biquaternions the quaternionic name becomes the tessarine and the Krein name the tessarine-Hermitian, their brackets carrying ${}_{\mathrm{ts}}$ and ${}_{\mathrm{ts}*}$.

The distinction between the form and the norm is one of **notation, not of substance**: the pair is the form and the norm of the statement at hand. The norm reading of the four letters, the qualified regular and degenerate, and the layer-by-layer tables are the subject of *Conventions of the Norms and the Unitary Convention*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{GPS}$, $\mathrm{GQS}$ | The four general products: plain bilinear, quaternionic bilinear, plain sesquilinear, quaternionic sesquilinear |
| $\mathrm{SPA}$, $\mathrm{SQA}$, $\mathrm{SPS}$, $\mathrm{SQS}$ | Their four symmetric parts |
| $\mathrm{APA}$, $\mathrm{AQA}$, $\mathrm{APS}$, $\mathrm{AQS}$ | Their four antisymmetric parts |
| $\mathrm{Form}(\tilde Q_1,\tilde Q_2)$ | The generic form, the form of the statement at hand |
| $\mathrm{Norm}(\tilde Q)=\mathrm{Form}(\tilde Q,\tilde Q)$ | The generic norm, the form at its two equal arguments |
| $\langle\tilde Q_1,\tilde Q_2\rangle$ | The plain form; $\langle\tilde Q\rangle$ the plain norm |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$ | The quaternionic form; $\langle\tilde Q\rangle_{\natural}$ the quaternionic norm |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$ | The Hermitian form; $\langle\tilde Q\rangle_{*}$ the Hermitian norm |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$ | The Krein form; $\langle\tilde Q\rangle_{\natural*}$ the Krein norm |
| $P$, $N$, $H$, $K$ | The letters of the four, each the form with two arguments and the norm with one |
| ${}_{\mathrm{ts}}$, ${}_{\mathrm{ts}*}$ | The tessarine and tessarine-Hermitian brackets of the reduced biquaternions |
| $\bullet$, $\wedge$ | The symmetrised and antisymmetrised product, on the exchange that keeps the class of the product |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998). Algebras with involution, the first and the second kind, and the classification of their involutions.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636. The biquaternion conjugations and the conventions of the complexified algebra in the applied literature.
- Soo-Chang Pei, Ja-Han Chang and Jian-Jiun Ding, "Commutative reduced biquaternions and their Fourier transform for signal and image processing applications", *IEEE Transactions on Signal Processing* **52** (2004) 2012–2022. The reduced biquaternion algebra of the engineering literature, its idempotent decomposition, its ring-valued norm and its transform.
