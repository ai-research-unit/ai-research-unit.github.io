# __Conventions of the Products and the Forms__

## Introduction

These are the conventions of the twelve products and of the four forms. They assume the algebra, its basis, its element glyphs and its conjugations as fixed in *Conventions in the Biquaternion Universe*; what is fixed here is the naming and the reading of everything built by multiplying two elements.

The order is the order of the definitions. The four general products come first, one for each choice of the two slots, the first factor read as it stands or through the natural sign and the second as it stands or through the star. Each splits into a symmetric and an antisymmetric part, and the twelve names are these four and their eight parts, written as three-letter codes and read letter by letter. The four maps follow — the identity and the three conjugations — with the four forms they produce, the generic Form and the generic Norm, the sign rule that ties the two lists, one table for each lower layer, and the Hermitian form with its unit, its normalisation and its weight.

The article states conventions only. The properties, the proofs and the namesake theorems belong to *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, and the physical interpretations belong to the articles that own them. The last subsection separates what is forced from what is chosen, and a reader must not turn a choice into a theorem.

## The Twelve Products and Their Names

The algebra carries **four general products** — one to each of the four choices of the two slots, the first factor read as it stands or through ${}^{\natural}$ and the second as it stands or through ${}^{*}$ — and each of the four splits into a **symmetric part** and an **antisymmetric part**, so that the complex space carries **twelve products** in all. The names are these, with the three-letter code the band articles write them by:

| The general product | Its symmetric part | Its antisymmetric part |
|---|---|---|
| The general plain bilinear product ($\mathrm{GPA}$) | The symmetric plain bilinear product ($\mathrm{SPA}$) | The antisymmetric plain bilinear product ($\mathrm{APA}$) |
| The general quaternionic bilinear product ($\mathrm{GQA}$) | The symmetric quaternionic bilinear product ($\mathrm{SQA}$) | The antisymmetric quaternionic bilinear product ($\mathrm{AQA}$) |
| The general plain sesquilinear product ($\mathrm{GPS}$) | The symmetric plain sesquilinear product ($\mathrm{SPS}$) | The antisymmetric plain sesquilinear product ($\mathrm{APS}$) |
| The general quaternionic sesquilinear product ($\mathrm{GQS}$) | The symmetric quaternionic sesquilinear product ($\mathrm{SQS}$) | The antisymmetric quaternionic sesquilinear product ($\mathrm{AQS}$) |

**The code is read letter by letter.** The first letter says which of the three operations of a row — $\mathrm G$ the general product, $\mathrm S$ its symmetric part, $\mathrm A$ its antisymmetric part; the second says which of the two products — $\mathrm P$ the plain one, whose first slot is read as it stands, and $\mathrm Q$ the quaternionic one, whose first slot carries ${}^{\natural}$; and the third says the family — $\mathrm A$ the **algebra** over $\mathbb{C}$, whose three products are $\mathbb{C}$-bilinear, and $\mathrm S$ the **sesqualgebra** over $(\mathbb{C},\bar{\cdot})$, whose three products are sesquilinear. The four general products are the multiplications of the four general structures of the band; the eight parts are the symmetric and antisymmetric products beside them; and the twelve codes together name the twelve algebraic structures of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

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

The products themselves — their coordinates, their laws, their units and their images — are *Symmetric and Antisymmetric Decomposition of the Four General Products*, and the grid of the four general products is *The Four General Products: Composition, Probability, Causality, Gauge*.

**The same code on the reduced biquaternion space.** The construction is not special to $\mathbb{B}$. On the commutative algebra $\mathbb{B}_{\mathrm{r}} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{C} \cong \mathbb{C}\oplus\mathbb{C}$ — the reduced biquaternions, equivalently the tessarines or the double-complex numbers — the same four general products exist, $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{GPS}$ and $\mathrm{GQS}$, and each splits into a symmetric and an antisymmetric part by the two exchanges. Because the algebra is **commutative**, four of the twelve codes name no new operation there: $\mathrm{SPA} = \mathrm{GPA}$ and $\mathrm{SQS} = \mathrm{GQS}$, while $\mathrm{APA} = 0$ and $\mathrm{AQS} = 0$. The space therefore carries **eight distinct algebraic structures** — $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{GPS}$, $\mathrm{GQS}$ and the four live halves $\mathrm{SQA}$, $\mathrm{AQA}$, $\mathrm{SPS}$, $\mathrm{APS}$ — and the twelve slots, the four that collapse and the eight that remain are *The Four Products, Their Forms and Their Algebraic Norms* and *The Specificities of the General Plain Algebra of the Reduced Biquaternions* of the mathematical corpus. The letter $\mathrm Q$ keeps its sense there — the first slot read through ${}_{\mathrm{ts}}$, the tessarine conjugation $j\mapsto-j$ (and $ij\mapsto-ij$) — as in the band above.

## The Involutions and the Four Forms

The algebra carries the identity and three conjugations, four maps in all, and on it there are four forms, each applying one map to each of its two arguments, so the two lists are one list read twice. One rule ties the two lists together, and that rule is what lets the series say which form is the metric and which is the inner product without having to choose.

**The setting.** $\mathbb{B}$ is a $\mathbb{C}$-algebra whose centre is $\mathbb{C}$, so every complex scalar is central, $\lambda\tilde{Q} = \tilde{Q}\lambda$ for all $\lambda \in \mathbb{C}$, which is the property that makes "$\mathbb{C}$-bilinear" well defined on $\mathbb{B}$; the scalar part $\mathrm{Sc}(\tilde{Q}) = Q_t$ is $\mathbb{C}$-linear. The centre is treated in *The Biquaternion Space, the Group of Involutions and the Six Subspaces*, §*The Complex Time Sector $\mathbb{C}_{\mathbb{B}}$*, and the forms of the algebra in *Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group with Hermitian Adjoint* and its mathematical twin *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*, and, on the side of positivity, in *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*.

**The four maps.** The tensor product $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is built from two rings that each carry two involutions, the identity and the conjugation, so it carries $2\times 2 = 4$, together with the derived anti-Hermitian sign:

| Map | Mark | Action | As a ring map | Over $\mathbb{C}$ |
|---|---|---|---|---|
| Identity | — | $\tilde{Q} \mapsto \tilde{Q}$ | Automorphism | $\mathbb{C}$-**linear** |
| Complex conjugation | $\bar{\cdot}$ | $Q_\mu \mapsto \bar{Q}_\mu$ | **Automorphism**: conjugation on the scalars, identity on the quaternion factor | $\mathbb{C}$-**antilinear** |
| Quaternion conjugation | ${}^{\natural}$ | $Q_te_t - Q_x\vec e_x - Q_y\vec e_y - Q_z\vec e_z$ | **Anti-automorphism**: identity on the scalars, conjugation on the quaternion factor | $\mathbb{C}$-**linear** |
| Hermitian conjugation | ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ | $\bar{Q}_te_t - \bar{Q}_x\vec e_x - \bar{Q}_y\vec e_y - \bar{Q}_z\vec e_z$ | **Anti-automorphism** | $\mathbb{C}$-**antilinear** |
| Anti-Hermitian conjugation | ${}^{\flat} = -{}^{*}$ | $-\tilde{Q}^{*}$ | **Neither** | $\mathbb{C}$-**antilinear** |

The fourth column is what the two questions separate. The bar acts on the scalars and on nothing else, so it is an order-two automorphism, $\mathbb{C}$-antilinear and **not** an anti-automorphism. The quaternion conjugation and the Hermitian conjugation are the two genuine **involutions of the ring**, $(\tilde{Q}_1\tilde{Q}_2)^{\natural} = \tilde{Q}_2^{\natural}\tilde{Q}_1^{\natural}$ and $(\tilde{Q}_1\tilde{Q}_2)^{*} = \tilde{Q}_2^{*}\tilde{Q}_1^{*}$, the quaternion conjugation being the one that touches only the quaternion factor. The anti-Hermitian sign is neither: it reverses with a twist, $(\tilde{Q}_1\tilde{Q}_2)^{\flat} = -\tilde{Q}_2^{\flat}\tilde{Q}_1^{\flat}$, so it is an involution of the underlying real vector space and nothing more. It is a derived sign and not a fifth map: it is minus the star, its fixed space is the material sector alone, and a text that counts it as a fifth map will misread the lattice. The four maps, the sign they derive, their fixed and anti-fixed spaces, and the lattice they form are *Comparison of the Remarkable Subspaces*.

**The generic form.** The series writes a **generic form** $\mathrm{Form}(\tilde{Q}_1,\tilde{Q}_2)$, the form of the statement at hand, of which the four below are the instances; the matching generic norm is stated with the norms in *Conventions of the Norms and the Pairings*, §*The Four Algebraic Norms and the $*$-Unitary Convention*.

**The four forms, written out.** Each conjugation applied to the first argument and each to the second gives one form. The four are written with the single bracket $\langle\cdot,\cdot\rangle$, whose subscript records the pair of conjugations — nothing when the identity sits in both, ${}^{\natural}$ when the quaternion conjugation sits in the first, ${}^{*}$ when the Hermitian conjugation sits in the second, and $\natural*$ when both sit.

The **plain form** applies the identity to both arguments:

$$
\langle\tilde{Q}_1,\tilde{Q}_2\rangle = \mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2) = Q_{1t}Q_{2t} - Q_{1x}Q_{2x} - Q_{1y}Q_{2y} - Q_{1z}Q_{2z},
$$

$\mathbb{C}$-**bilinear** in both arguments; on $\mathbb{M}_-$ it is $-c^2{t'}^2-x^2-y^2-z^2$, signature $(0,4)$.

The **quaternionic form** applies the quaternion conjugation to the first argument and the identity to the second:

$$
\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural} = \mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2) = Q_{1t}Q_{2t} + Q_{1x}Q_{2x} + Q_{1y}Q_{2y} + Q_{1z}Q_{2z},
$$

$\mathbb{C}$-**bilinear** in both arguments; on $\mathbb{M}_-$ it is $-c^2{t'}^2+x^2+y^2+z^2$, signature $(3,1)$.

The **Hermitian form** applies the identity to the first argument and the Hermitian conjugation to the second:

$$
\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*} = \mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*}) = Q_{1t}\bar{Q}_{2t} + Q_{1x}\bar{Q}_{2x} + Q_{1y}\bar{Q}_{2y} + Q_{1z}\bar{Q}_{2z},
$$

$\mathbb{C}$-**sesquilinear**, linear in the first argument and antilinear in the second; on $\mathbb{M}_-$ it is $c^2{t'}^2+x^2+y^2+z^2$, signature $(4,0)$.

The **Krein form** applies the quaternion conjugation to the first argument and the Hermitian conjugation to the second:

$$
\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural*} = \mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2^{*}) = Q_{1t}\bar{Q}_{2t} - Q_{1x}\bar{Q}_{2x} - Q_{1y}\bar{Q}_{2y} - Q_{1z}\bar{Q}_{2z},
$$

$\mathbb{C}$-**sesquilinear**, linear in the first argument and antilinear in the second; on $\mathbb{M}_-$ it is $c^2{t'}^2-x^2-y^2-z^2$, signature $(1,3)$.

Each form is the scalar part of its own product. The Hermitian form is the pairing that carries probability; the plain form is its restriction to $\mathbb{M}_+$ and the primary computational form on the sector; the other two are read by choosing the conjugation of a slot, and the trace is a reading of the Hermitian form in the $2\times2$ image.

**The four formulas are written on the biquaternion glyph, whose two marks are independent; when one mark degenerates the brackets collapse two-and-two, and in the reduced biquaternions no mark degenerates and the four remain distinct.** Each table below gives only the brackets that survive on the layer, with the norm they carry.

**One table per lower layer.** Each table reads the brackets that survive on the layer's own glyph. The **algebraic norm** is the diagonal of the form, the **signature** is that of the real quadratic form with the positive directions counted first, and the **role** records what the bracket does: the definite bracket carries the topology and the multiplicative one the invertibility criterion.

**The complex numbers $\mathbb{C}$**, $Q=q+iq'$.

| bracket | form | algebraic norm | signature | role |
|---|---|---|---|---|
| $\langle Q_1,Q_2\rangle=Q_1Q_2$ | plain, also quaternionic | $\langle Q\rangle=Q^2\in\mathbb{C}$, $\operatorname{Re}\langle Q\rangle=q^2-q'^2$ | $(1,1)$ | anisotropic; real part indefinite |
| $\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2$ | Hermitian, also Krein | $\langle Q\rangle_{*}=Q\bar Q=q^2+q'^2$ | $(2,0)$ | definite; multiplicative; topology |

In $\mathbb{C}$ the star bracket is definite and multiplicative at once. The plain norm is complex and anisotropic; its real part is indefinite. The modulus is $\sqrt{\langle Q\rangle_{*}}$. The natural sign being the identity, the quaternionic bracket is the plain one and the Krein bracket the Hermitian one.

**The split-complex numbers $\mathbb{D}$**, $Q=q+jq'$, $j^2=+1$.

| bracket | form | algebraic norm | signature | role |
|---|---|---|---|---|
| $\langle Q_1,Q_2\rangle=Q_1Q_2$ | plain, also quaternionic | $\langle Q\rangle=Q^2\in\mathbb{D}$, $\operatorname{Re}\langle Q\rangle=q^2+q'^2$ | $(2,0)$ | definite; topology; not multiplicative |
| $\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2$ | Hermitian, also Krein | $\langle Q\rangle_{*}=Q\bar Q=q^2-q'^2$ | $(1,1)$ | multiplicative; invertibility; null cone |

The two brackets exchange their signatures with the sign of the square of the coefficient unit: $i^2=-1$ makes the real part of the plain norm indefinite and the star norm definite, while $j^2=+1$ does the reverse. Definite and multiplicative are split across the two brackets, and no single bracket is both, since $(1+j)(1-j)=0$ with $1\pm j\neq0$. The topological norm is $\sqrt{\operatorname{Re}\langle Q\rangle}$, with no modulus sign; the scale of the polar factor is $\sqrt{\lvert\langle Q\rangle_{*}\rvert}$ and is not a norm. Over the dual numbers $\mathbb{D}'$ both brackets realify to the rank-one form $q^2$; the algebraic norm is degenerate, and the topology is the Euclidean form $q^2+q'^2$ of the coefficient plane, which is not one of the brackets.

**The reduced biquaternions $\mathbb{B}_{\mathrm{r}}$**, $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with complex $Q_{\blacktriangle},Q_{\blacktriangledown}$; the marks are the bar and the tessarine sign ${}_{\mathrm{ts}}$, and ${}^{*}=\bar{\cdot}\circ{}_{\mathrm{ts}}$.

| bracket | form | algebraic norm | value | role |
|---|---|---|---|---|
| $\langle\breve Q_1,\breve Q_2\rangle=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown}$ | plain | $\langle\breve Q\rangle=Q_{\blacktriangle}^2+Q_{\blacktriangledown}^2$ | complex | — |
| $\langle\breve Q_1,\breve Q_2\rangle_{\mathrm{ts}}=Q_{1\blacktriangle}Q_{2\blacktriangle}-Q_{1\blacktriangledown}Q_{2\blacktriangledown}$ | tessarine | $\langle\breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2$ | complex | multiplicative; invertibility; zero divisors |
| $\langle\breve Q_1,\breve Q_2\rangle_{*}=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}-Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown}$ | Hermitian | $\langle\breve Q\rangle_{*}=\lvert Q_{\blacktriangle}\rvert^2-\lvert Q_{\blacktriangledown}\rvert^2$ | real, $(2,2)$ | indefinite |
| $\langle\breve Q_1,\breve Q_2\rangle_{\mathrm{ts}*}=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}+Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown}$ | tessarine-Hermitian | $\langle\breve Q\rangle_{\mathrm{ts}*}=\lvert Q_{\blacktriangle}\rvert^2+\lvert Q_{\blacktriangledown}\rvert^2$ | real, $(4,0)$ | definite; topology |

The tessarine bracket carries the algebra and the tessarine-Hermitian bracket carries the topology. The tessarine norm is the **reduced norm**, multiplicative and vanishing exactly on the zero divisors, so it decides invertibility. The fourth bracket is definite, so it is not a Krein form.

**The quaternions $\mathbb{H}$**, $\tilde q=q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ with real coefficients and $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$.

| bracket | form | algebraic norm | signature | role |
|---|---|---|---|---|
| $\langle\tilde q_1,\tilde q_2\rangle=\mathrm{Sc}(\tilde q_1\tilde q_2)$ | plain, also Krein | $q_t^2-q_x^2-q_y^2-q_z^2$ | $(1,3)$ | indefinite; not multiplicative |
| $\langle\tilde q_1,\tilde q_2\rangle_{\natural}=\mathrm{Sc}(\tilde q_1^{\natural}\tilde q_2)$ | quaternionic, also Hermitian | $q_t^2+q_x^2+q_y^2+q_z^2$ | $(4,0)$ | definite; multiplicative; topology |

The coefficients are real and the only non-trivial involution is the natural sign, so the Hermitian form is the quaternionic one and the Krein form the plain one. The quaternionic form is definite and its norm is multiplicative, the usual quaternion norm $q_t^2+q_x^2+q_y^2+q_z^2$; the plain form is indefinite and its norm is not multiplicative.

**The split-quaternions $\mathbb{H}_{\mathrm{s}}$**, the same glyph over the units $\vec e_x^2=-e_t$ and $\vec e_y^2=\vec e_z^2=+e_t$.

| bracket | form | algebraic norm | signature | role |
|---|---|---|---|---|
| $\langle\tilde q_1,\tilde q_2\rangle=\mathrm{Sc}(\tilde q_1\tilde q_2)$ | plain, also Krein | $q_t^2-q_x^2+q_y^2+q_z^2$ | $(3,1)$ | indefinite; not multiplicative |
| $\langle\tilde q_1,\tilde q_2\rangle_{\natural}=\mathrm{Sc}(\tilde q_1^{\natural}\tilde q_2)$ | quaternionic, also Hermitian | $q_t^2+q_x^2-q_y^2-q_z^2$ | $(2,2)$ | multiplicative; indefinite; zero divisors |

The collapse of the names is the same. The quaternionic norm is the split-quaternion norm $\langle\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}=q_t^2+q_x^2-q_y^2-q_z^2$: multiplicative, indefinite, and vanishing exactly on the zero divisors, so it decides invertibility. The plain form is $\mathrm{Sc}(\tilde q^2)$ and is indefinite as well, so neither form is definite. No positive-definite form can be multiplicative here: $1+\vec e_y$ and $1-\vec e_y$ are non-zero and their product is $1-\vec e_y^2=0$, so a multiplicative form vanishes on one of them. The topology is therefore the Euclidean form of the coefficient space, $q_t^2+q_x^2+q_y^2+q_z^2$, which is positive definite but not multiplicative.

**The biquaternion layer.** The four brackets and their norms on $\mathbb{B}$ are the table of *Conventions of the Norms and the Pairings*, §*The Four Algebraic Norms and the $*$-Unitary Convention*.

**The Hermitian form, its norm, the unit, the normalisation and the weight.** The order is fixed once for the series. The form is

$$
\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*} = \mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*}) = \sum_\mu Q_{1\mu}\bar Q_{2\mu},
$$

its diagonal is the Hermitian norm,

$$
\langle\tilde{Q}\rangle_{*} = \langle\tilde{Q},\tilde{Q}\rangle_{*} = \sum_\mu\lvert Q_\mu\rvert^{2},
$$

and the unit is normalised by it, $\langle e_t\rangle_{*} = 1$. The form is positive definite on the whole algebra. Its restriction to $\mathbb{M}_+$ is the plain form,
$$
\langle\tilde{H}_1,\tilde{H}_2\rangle = \mathrm{Sc}(\tilde{H}_1\tilde{H}_2),
$$
of signature $(4,0)$ there, and its restriction to $\mathbb{M}_-$ is minus the plain form, of signature $(0,4)$. A state is normalised by the form against the unit,

$$
\langle\tilde{Ϛ},e_t\rangle_{*} = \tfrac12\langle e_t\rangle_{*},
\qquad \langle e_t\rangle_{*}=1 .
$$

and the Born weight of an observable is the normalised Hermitian form,

$$
p=\frac{\langle\tilde{Ϛ},\tilde H\rangle_{*}}{\langle\tilde{Ϛ},e_t\rangle_{*}}
 =\frac{\mathrm{Sc}(\tilde{Ϛ}\tilde H^{*})}{\mathrm{Sc}(\tilde{Ϛ})}
 =h_t+\vec r\cdot\vec h .
$$

The star is the Hermitian conjugation, and it is what makes the pairing positive definite on the whole algebra. On $\mathbb{M}_+$ it is inert, since both arguments are Hermitian, and the weight is positive there by the sector's own definiteness. The weight is written with the star on $\mathbb{M}_+$ and on $\mathbb{B}$ alike. On $\mathbb{M}_+$ both arguments are Hermitian, so $\tilde H^{*}=\tilde H$ and the star acts as the identity on them, but it is not omitted: it names the form that is positive definite everywhere. The same weight is therefore also $\mathrm{Sc}(\tilde{Ϛ}\tilde H)/\mathrm{Sc}(\tilde{Ϛ})$, the plain scalar. The plain form is the restriction of the Hermitian form to the sector, not a second definition of the weight. The Hermitian norm is the only one of the four that is positive definite on the whole algebra; the plain form is definite only on a sector, with opposite signs on the two. For a state $\tilde{Ϛ}\ge0$ and an effect $0\le\tilde H\le e_t$ the weight lies in $[0,1]$, manifestly non-negative because the form is positive definite on the whole algebra. The trace is the final reading, at normalisation: the unstarred trace is real, because $(AB)^{\dagger}=BA$ for Hermitian $A,B$ gives $\overline{\mathrm{tr}(AB)}=\mathrm{tr}(AB)$; it is non-negative here because $\mathrm{tr}(AB)=\mathrm{tr}(A^{1/2}BA^{1/2})\ge0$ for the positive state and effect. The weight is therefore also $p=\operatorname{Tr}(\tilde{Ϛ}\tilde H)/\operatorname{Tr}(\tilde{Ϛ})\in[0,1]$.

The scalar part is then a reading of the form against the unit, $\mathrm{Sc}(\tilde Q)=\langle\tilde Q,e_t\rangle_{*}$, and the trace is the reading in the $2\times2$ image, once and last,

$$
2\langle\tilde Q_1,\tilde Q_2\rangle_{*}=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\operatorname{Tr}(\tilde Q_1\tilde Q_2^{*}),
\qquad 2\,\mathrm{Sc}(\tilde Q)=\operatorname{Tr}(\tilde Q).
$$

The factor $2$ is the dimension of that image, not a property of the form. The order of the readings is fixed once for the series — form with star, scalar with star, plain scalar on $\mathbb{M}_+$, trace at normalisation last — and is explained in *The Born Rule from the Hermitian Form — Derivation and Comparison*. The Hermitian norm is not the normalising functional: on a state it reads $\langle\tilde{Ϛ}\rangle_{*}=\tfrac14(1+|\vec r|^2)$, which varies from $\tfrac14$ to $\tfrac12$ across the Bloch ball.

**In the $2\times2$ image.** The four forms are the traces of their products up to that factor,

$$
2\langle\tilde{Q}_1,\tilde{Q}_2\rangle = \operatorname{Tr}(\tilde{Q}_1\tilde{Q}_2), \qquad 2\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural} = \operatorname{Tr}(\tilde{Q}_1^{\natural}\tilde{Q}_2),
$$

$$
2\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*} = \operatorname{Tr}(\tilde{Q}_1\tilde{Q}_2^{*}), \qquad 2\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural*} = \operatorname{Tr}(\tilde{Q}_1^{\natural}\tilde{Q}_2^{*}).
$$

**The type is decided by the second argument.** The scalars are central and $\mathrm{Sc}$ is $\mathbb{C}$-linear, so a conjugation that is $\mathbb{C}$-linear passes a complex scalar out of its argument unchanged, while a conjugation that is $\mathbb{C}$-antilinear conjugates it. The identity and the quaternion conjugation are $\mathbb{C}$-linear and the Hermitian conjugation is $\mathbb{C}$-antilinear, so a scalar leaving the second argument comes out barred in exactly the two sesquilinear forms:

$$
\langle\tilde{Q}_1,\lambda\tilde{Q}_2\rangle = \lambda\langle\tilde{Q}_1,\tilde{Q}_2\rangle, \qquad \langle\tilde{Q}_1,\lambda\tilde{Q}_2\rangle_{\natural} = \lambda\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural},
$$

$$
\langle\tilde{Q}_1,\lambda\tilde{Q}_2\rangle_{*} = \bar\lambda\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}, \qquad \langle\tilde{Q}_1,\lambda\tilde{Q}_2\rangle_{\natural*} = \bar\lambda\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural*} .
$$

In the first argument no scalar is conjugated, every first-slot conjugation being $\mathbb{C}$-linear:

$$
\langle\lambda\tilde{Q}_1,\tilde{Q}_2\rangle = \lambda\langle\tilde{Q}_1,\tilde{Q}_2\rangle, \qquad \langle\lambda\tilde{Q}_1,\tilde{Q}_2\rangle_{*} = \lambda\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*} .
$$

Throughout the series a signature is written $(n,m)$ with the **positive** directions counted first, so that $(-,-,-,-)$ is $(0,4)$.

**Where the four are proved and named.** The classification of the four, their Gram matrices, their signatures, their isometry groups, their Witt classes, and their reading as Hermitian forms over the algebra with respect to their own involutions are *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*, with its twin *Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group with Hermitian Adjoint*.

**What is forced and what is chosen.** The two bilinear forms are $\mathbb{C}$-bilinear in both slots and the two sesquilinear forms are linear in the first slot and sesquilinear in the second. That is not a choice but a consequence of the $\mathbb{C}$-linearity of the natural sign together with the centrality of $\mathbb{C}$ in $\mathbb{B}$; its verification is *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*. Multiplication by $i$ reverses the sign of the two bilinear forms and leaves the two sesquilinear forms unchanged, since the centrality of $i$ puts either a factor $i^2 = -1$ on both slots or on neither.

## Summary

The twelve products are one construction. Two slots, each read plain or through its conjugation, give four general products; the exchange of the two arguments within the class of the product gives a symmetric and an antisymmetric part to each. The codes GPA, GQA, GPS and GQS name the general products, SPA, SQA, SPS and SQS their symmetric parts, and APA, AQA, APS and AQS their antisymmetric parts. The symmetric product is the bullet and the antisymmetric the wedge, and the general product is their sum. The bare interchange of the two arguments is not the class-preserving exchange, so the two antisymmetrisations are not one operation; on the reduced biquaternion space four of the twelve codes name no new operation.

The four forms are the four maps read on two arguments. The identity gives the plain bilinear form $B$, the natural sign the quaternionic form $N$, the star the Hermitian form $H$ and the flat sign the Krein form $K$, with the signature convention and the pairwise sign rule that make the table consistent. Each lower layer has its own table, and where a mark degenerates the brackets collapse two and two rather than becoming a different convention.

The Hermitian form is the one that carries probability: $\langle e_t,e_t\rangle_*=1$, a normalised state has $\langle\tilde{Ϛ},e_t\rangle_*=\tfrac12$, and the Born weight is a ratio of pairings. Its type is decided by the second argument. The article closes by separating the conventions that are chosen from the assignments that are forced by the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| GPA, GQA, GPS, GQS | The four general products: plain bilinear, quaternionic bilinear, plain sesquilinear, quaternionic sesquilinear |
| SPA, SQA, SPS, SQS | Their symmetric parts |
| APA, AQA, APS, AQS | Their antisymmetric parts |
| $\tilde Q_1\bullet\tilde Q_2$ | The symmetric product, the half-sum of the two orders |
| $\tilde Q_1\wedge\tilde Q_2$ | The antisymmetric product, the half-difference; on differential forms the same glyph is the exterior product |
| $B$, $N$, $H$, $K$ | The four forms: plain, quaternionic, Hermitian, Krein |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$ | The Hermitian form, $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ |
| $\natural$, ${}^{*}$, $\flat=-{}^{*}$ | The natural, star and flat conjugations |
| $\mathrm{Form}$, $\mathrm{Norm}$ | The generic form of the statement and the form at its two equal arguments |

## Further Reading

- [Conventions in the Biquaternion Universe](conventions-in-the-biquaternion-universe.html), for the algebra, the basis, the element glyphs and the conjugations these conventions assume.
- [Conventions of the Norms and the Pairings](conventions-of-the-norms-and-the-pairings.html), for the norms read on the diagonal of these forms and for the unitary convention.
- [Conventions of the Operators and the Calculus](conventions-of-the-operators-and-the-calculus.html), for the same products read on the gradient.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), companion article, for the proofs, the signature convention and the pairwise sign rule.
- [Conventions in Mathematics](../articles_maths/conventions-in-mathematics.html), for the same forms on the lower layers.
