# __Conventions of the Norms and the Unitary Convention__

## Introduction

The norm is the form at its two equal arguments. This article owns the one-argument reading: the letters of the four norms, the qualified regular and the qualified degenerate, the six layer tables that record the form, the algebraic norm, the realified signature and the role of each bracket, and the unitary convention that fixes what *norm one* means layer by layer.

The norm is not one object across the layers. The complex, split-complex, dual, reduced biquaternion, quaternion and biquaternion layers do not share a norm, and a glyph such as $U$ names no set by itself. The article therefore fixes the condition layer by layer before it fixes the glyph, and the tables are read as one row per bracket that survives on the layer.

The order is: the norm reading of the four letters, the qualified regular and degenerate, the six layer tables, the unitary convention, and the letters $U$ and $u$ outside the layers. The article assumes the products and the forms of *Conventions of the Products and the Forms*, and it is assumed in turn by the calculus of *Conventions of the Operators and the Calculus*.

## The Norm Convention

**One letter, two arities.** The four letters $P$, $N$, $H$ and $K$ fixed in *Conventions of the Products and the Forms* name each form with two arguments and the corresponding algebraic norm with one: $P(\tilde Q)$ is the plain norm, $N(\tilde Q)$ the quaternionic, $H(\tilde Q)$ the Hermitian and $K(\tilde Q)$ the Krein, and the bracket of the same subscript does the same. This article reads that second arity.

**The qualified regular and the qualified degenerate.** In $\mathbb{B}$, for a letter $\Phi$ of the four, a biquaternion is **$\Phi$-regular** when $\Phi(\tilde Q)\neq0$ and **$\Phi$-degenerate** when $\Phi(\tilde Q)=0$. Only $N$ decides invertibility: $\{N=0\}$ is the origin together with the zero divisors, so $\natural$-regular is the unit group and $\natural$-degenerate the non-units. $P$-degenerate and $K$-degenerate contain units, $P(e_t+\vec e_x)=K(e_t+\vec e_x)=0$ with $N(e_t+\vec e_x)=2$, and $H$-degenerate is the origin alone. The unqualified *regular* is the spectral one, $B^{2}\neq0$, of *The Spectrum*, so the letter is never omitted.

### The Six Layer Tables

**The four formulas are written on the biquaternion glyph, whose two marks are independent; when one mark degenerates the brackets collapse two-and-two, and in the reduced biquaternions no mark degenerates and the four remain distinct.** Each table below gives only the brackets that survive on the layer, with the norm they carry.

**One table per layer.** Each table reads the brackets that survive on the layer's own glyph. The **algebraic norm** is the diagonal of the form, the **realified signature** is that of the real quadratic form with the positive directions counted first, and the **role** records what the bracket does: the definite bracket carries the topology and the multiplicative one the invertibility criterion.

**The complex numbers $\mathbb{C}$**, $Q=q+iq'$.

| bracket | form | algebraic norm | realified signature | role |
|---|---|---|---|---|
| $\langle Q_1,Q_2\rangle=Q_1Q_2$ | plain, also quaternionic | $\langle Q\rangle=Q^2\in\mathbb{C}$, $\operatorname{Re}\langle Q\rangle=q^2-q'^2$ | $(1,1)$ | anisotropic; real part indefinite |
| $\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2$ | Hermitian, also Krein | $\langle Q\rangle_{*}=Q\bar Q=q^2+q'^2$ | $(2,0)$ | definite; multiplicative; topology |

In $\mathbb{C}$ the star bracket is definite and multiplicative at once. The plain norm is complex and anisotropic, $\langle Q\rangle=0$ only at $Q=0$; its real part is indefinite. The natural sign being the identity, the quaternionic bracket is the plain one and the Krein bracket the Hermitian one.

**The split-complex numbers $\mathbb{D}$**, $Q=q+jq'$, $j^2=+1$.

| bracket | form | algebraic norm | realified signature | role |
|---|---|---|---|---|
| $\langle Q_1,Q_2\rangle=Q_1Q_2$ | plain, also quaternionic | $\langle Q\rangle=Q^2\in\mathbb{D}$, $\operatorname{Re}\langle Q\rangle=q^2+q'^2$ | $(2,0)$ | definite; topology; not multiplicative |
| $\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2$ | Hermitian, also Krein | $\langle Q\rangle_{*}=Q\bar Q=q^2-q'^2$ | $(1,1)$ | multiplicative; invertibility; null cone |

The two brackets exchange their signatures with the sign of the square of the coefficient unit: $i^2=-1$ makes the real part of the plain norm indefinite and the star norm definite, while $j^2=+1$ does the reverse. Definite and multiplicative are split across the two brackets, and no single bracket is both, since $(1+j)(1-j)=0$ with $1\pm j\neq0$. The topological norm is therefore $\sqrt{\operatorname{Re}\langle Q\rangle}$, with no modulus sign, and the scale of the polar factor is $\sqrt{\lvert\langle Q\rangle_{*}\rvert}$, which is multiplicative on the units and is not a norm. Over the dual numbers $\mathbb{D}'$ the square of the coefficient unit vanishes and both brackets realify to the rank-one form $q^2$; the algebraic norm is degenerate, and the topology is the Euclidean form $q^2+q'^2$ of the coefficient plane, which is not one of the brackets.

**The modulus of an element is a square root of its algebraic norm**: $\sqrt{\langle Q\rangle_{*}}$ over $\mathbb{C}$ and $\mathbb{D}'$, and $\sqrt{\lvert\langle Q\rangle_{*}\rvert}$ over the indefinite $\mathbb{D}$; the modulus is defined through the algebraic norm.

**Bars around a complex element are the ordinary complex modulus.** For $Q=q+iq'$,

$$
\lvert Q\rvert=\sqrt{Q\bar Q}=\sqrt{q^2+q'^2},
$$

a real and non-negative number. The bars are the modulus and not a bracket of the layer: the algebraic norms keep their bracket, $\langle Q\rangle=Q^2$ and $\langle Q\rangle_{*}=Q\bar Q$. The same bars apply to a complex coefficient of a biquaternion, $\lvert Q_\mu\rvert=\sqrt{q_\mu^2+{q'_\mu}^2}$; over $\mathbb{C}$ the square of the modulus is the Hermitian norm, $\lvert Q\rvert^2=\langle Q\rangle_{*}$.

**The argument of a complex element is written $\arg Q_t$.** For $Q_t\neq0$ it is the angle of the polar form,

$$
Q_t=\lvert Q_t\rvert\,e^{i\arg Q_t},
$$

defined modulo $2\pi$; the branch is stated where the argument is used, and the principal argument in $(-\pi,\pi]$ is written $\operatorname{Arg}Q_t$. The same letter applies to a complex coefficient of a biquaternion, $\arg Q_\mu$, with $\lvert Q_\mu\rvert$ the modulus above.

**The reduced biquaternions $\mathbb{B}_{\mathrm{r}}$**, $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with $Q_{\blacktriangle},Q_{\blacktriangledown}\in\mathbb{C}$; the marks are the bar and the tessarine sign ${}_{\mathrm{ts}}$, and ${}^{*}=\bar{\cdot}\circ{}_{\mathrm{ts}}$.

| bracket | form | algebraic norm | value | role |
|---|---|---|---|---|
| $\langle\breve Q_1,\breve Q_2\rangle=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown}$ | plain | $\langle\breve Q\rangle=Q_{\blacktriangle}^2+Q_{\blacktriangledown}^2$ | complex | — |
| $\langle\breve Q_1,\breve Q_2\rangle_{\mathrm{ts}}=Q_{1\blacktriangle}Q_{2\blacktriangle}-Q_{1\blacktriangledown}Q_{2\blacktriangledown}$ | tessarine | $\langle\breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2$ | complex | multiplicative; invertibility; zero divisors |
| $\langle\breve Q_1,\breve Q_2\rangle_{*}=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}-Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown}$ | Hermitian | $\langle\breve Q\rangle_{*}=\lvert Q_{\blacktriangle}\rvert^2-\lvert Q_{\blacktriangledown}\rvert^2$ | real, $(2,2)$ | indefinite |
| $\langle\breve Q_1,\breve Q_2\rangle_{\mathrm{ts}*}=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}+Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown}$ | tessarine-Hermitian | $\langle\breve Q\rangle_{\mathrm{ts}*}=\lvert Q_{\blacktriangle}\rvert^2+\lvert Q_{\blacktriangledown}\rvert^2$ | real, $(4,0)$ | definite; topology |

The tessarine bracket carries the algebra and the tessarine-Hermitian bracket carries the topology. The norm $\langle\breve Q\rangle_{\mathrm{ts}}$ is the **reduced norm** of the layer: multiplicative, vanishing exactly on the zero divisors and at $0$, so $\breve Q$ is invertible if and only if that norm is non-zero, with $\breve Q^{-1}=\breve Q_{\mathrm{ts}}/\langle\breve Q\rangle_{\mathrm{ts}}$. The fourth bracket is definite, so it is not a Krein form. The plain and the tessarine norms are complex-valued.

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

**The biquaternions $\mathbb{B}$**, $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; the marks $\bar{\cdot}$ and ${}^{\natural}$ are independent, and ${}^{*}=\bar{\cdot}\circ{}^{\natural}$.

| bracket | form | algebraic norm | value | realified signature | role |
|---|---|---|---|---|---|
| $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | plain | $Q_t^2-Q_x^2-Q_y^2-Q_z^2$ | $\mathbb{C}$ | $(4,4)$ | complex cone |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$ | quaternionic | $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ | $\mathbb{C}$ | $(4,4)$ | multiplicative; zero-divisor cone |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ | Hermitian | $\lvert Q_t\rvert^2+\lvert Q_x\rvert^2+\lvert Q_y\rvert^2+\lvert Q_z\rvert^2$ | $\mathbb{R}$ | $(8,0)$ | definite; topology |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})$ | Krein | $\lvert Q_t\rvert^2-\lvert Q_x\rvert^2-\lvert Q_y\rvert^2-\lvert Q_z\rvert^2$ | $\mathbb{R}$ | $(2,6)$ | indefinite |

The quaternionic norm is the determinant in the $2\times2$ image and is the multiplicative one, vanishing exactly on the zero-divisor cone; the Hermitian norm is the definite one and carries the topology; the plain and the Krein norms are the remaining two, complex and indefinite respectively. The signature column is that of the realified form on the eight real parameters; on the material sector the restrictions are those stated above. The split-biquaternion layer $\mathbb{H}_{\mathbb{D}}$ keeps the same four brackets, its coefficients being split-complex instead of complex, so the two bilinear norms take split-complex values and the two sesquilinear ones stay real.

**The one-line rule.** Write the bracket with the intrinsic conjugation of the layer: the star in $\mathbb{C}$, $\mathbb{D}$ and $\mathbb{D}'$, where the natural sign is the identity; the natural sign in $\mathbb{H}$ and $\mathbb{H}_{\mathrm{s}}$, where the bar is the identity; the tessarine sign in $\mathbb{B}_{\mathrm{r}}$; and both marks, all four brackets, in $\mathbb{B}$ and $\mathbb{H}_{\mathbb{D}}$.

### The Unitary Convention

**The convention is the unit-element convention, and the heading keeps its old name because the corpus cites it by that name.** The glyphs $U$, $\tilde u$ and $\tilde U$, in the three cases of the case rule, mark an element of **norm one**. They do not mark a unitary element: the unitary condition is a different condition, stated at the end of the section.

A unit element carries its own glyph, the **$u$** in the two cases, beside the root $\tilde\Xi$, the idempotent $\tilde\Pi$ and the nilpotent $\tilde\nu$: the letter $u$ is reserved for a unit element, and a general element is $\tilde q$ or $\tilde Q$. **The exponential is written $\exp(\cdot)$**, never $e^{\cdot}$, the letter $e$ being the base $e_t,\vec e_x,\vec e_y,\vec e_z$.

**"Norm one" is fixed layer by layer.** The glyphs name no set by themselves, and the layers do not share a norm. The table gives the norm of each layer and the set it cuts out at one.

| Layer | Glyph | The norm | The condition | The norm-one elements |
|---|---|---|---|---|
| $\mathbb{R}$ | — | $\langle q\rangle=q^{2}$ | $q=\pm1$ | $\{\pm1\}=O(1)$ |
| $\mathbb{C}$ | $U$ | $\lvert Q\rvert=(Q\bar Q)^{1/2}$, the modulus | $\lvert Q\rvert=1$ | $\mathrm{U}(1)=S^{1}$ |
| $\mathbb{D}$, split-complex | $U$ | $Q\bar Q=q^{2}-q'^{2}$, the split norm | $Q\bar Q=1$ | the unit hyperbola, two branches |
| $\mathbb{D}'$, dual | $U$ | $\langle Q\rangle=q^{2}$ | $q=\pm1$, $q'$ free | the two lines $\pm1+\mathrm{M}$; the identity component is the shear group |
| $\mathbb{B}_{\mathrm{r}}$, reduced biquaternion | $U$ | $\langle\breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$ | $\langle\breve Q\rangle_{\mathrm{ts}}=1$ | the reduced-norm quadric |
| $\mathbb{H}$, quaternion | $\tilde u$ | $\langle\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}$ | $\langle\tilde q\rangle_{\natural}=1$ | $Sp(1)=S^{3}=\mathrm{SU}(2)$ |
| $\mathbb{H}_{\mathrm{s}}$, split-quaternion | $\tilde u$ | $\langle\tilde q\rangle_{\natural}$ | $\langle\tilde q\rangle_{\natural}=1$ | $\mathrm{SL}_{2}(\mathbb{R})$, non-compact |
| $\mathbb{B}$, biquaternion | $\tilde U$ | $\langle\tilde Q\rangle_{\natural}$ and no other | $\langle\tilde Q\rangle_{\natural}=e_t$ | $\mathbb{B}^{\times}_{1}\cong\mathrm{SL}(2,\mathbb{C})$ |
| $\mathbb{H}_{\mathbb{D}}$, split-biquaternion | $\tilde U$ | $\langle\tilde Q\rangle_{\natural}$ | $\langle\tilde Q\rangle_{\natural}=e_t$ | $S^{3}\times S^{3}$ |

**Where the norm is indefinite, the sign is not part of the glyph.** In $\mathbb{D}$ the level set $Q\bar Q=1$ is the two-branched hyperbola; the polar decomposition of *Modulus–Unit Polar Decomposition of Split-Complex Numbers* takes its unit factor on $\lvert Q\bar Q\rvert=1$, four branches, because the sign of the norm is a regime carried by that factor. In $\mathbb{B}_{\mathrm{r}}$ the reduced norm cuts the quadric of the table, while *Modulus–Unit Polar Decomposition of Reduced Biquaternions* puts its unit factor on the bar-unitary torus and states that the torus is not a norm-one set. The glyph follows the level set $\mathrm{Norm}=1$; a modulus-one factor of an indefinite layer is not a second meaning of the glyph.

**The biquaternion layer uses $N$ and only $N$.** The glyph $\tilde U$ is the $N$-norm-one element,

$$
\mathbb{B}^{\times}_{1}=\{\tilde Q:\langle\tilde Q\rangle_{\natural}=e_t\}\cong\mathrm{SL}(2,\mathbb{C}),
$$

and the other three norms of the layer are not unit-element conditions. Their level sets are named for completeness and carry no glyph:

| Letter | Norm | The level set | What it is | Defines $\tilde U$ |
|---|---|---|---|---|
| $P$ | $\langle\tilde Q\rangle$ | $Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2}=e_t$ | the complex hyperboloid of the plain norm | no |
| $N$ | $\langle\tilde Q\rangle_{\natural}$ | $Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}=e_t$ | $\mathbb{B}^{\times}_{1}$, the norm-one units | **yes** |
| $H$ | $\langle\tilde Q\rangle_{*}$ | $\lvert Q_t\rvert^{2}+\lvert Q_x\rvert^{2}+\lvert Q_y\rvert^{2}+\lvert Q_z\rvert^{2}=1$ | the unit sphere of the Hermitian norm | no |
| $K$ | $\langle\tilde Q\rangle_{\natural*}$ | $\lvert Q_t\rvert^{2}-\lvert Q_x\rvert^{2}-\lvert Q_y\rvert^{2}-\lvert Q_z\rvert^{2}=1$ | the indefinite level set of the Krein norm | no |

**Only $N$ decides invertibility**, which is the reason it is the norm of the glyph: $\{N=0\}$ is the origin together with the zero divisors, while the other three degenerate sets contain units. The phrase "the norm in view" belongs to the polar decompositions, where the author names the norm in the text and takes its level set; it is not a licence to read one glyph under four norms.

**Unitary is not norm one.** The unitary group is

$$
\mathrm{U}(\mathbb{B})=\{\tilde Q:\tilde Q^{*}\tilde Q=e_t\}\cong\mathrm{U}(2)=S^{1}\cdot S^{3},
$$

of real dimension four, written upright because it is a group. Its elements are **unitary elements**, not unit elements, and the two conditions are independent:

- neither set contains the other: $\mathrm{U}(2)\cap\mathrm{SL}(2,\mathbb{C})=\mathrm{SU}(2)=S^{3}$, the unit quaternions;
- the Hermitian level set $\{H=1\}$ contains $\mathrm{U}(2)$ strictly, since it is the unit sphere of $\mathbb{R}^{8}$ of dimension seven and $\mathrm{U}(2)$ has dimension four;
- the $N$-norm-one set $\mathbb{B}^{\times}_{1}$ does not contain $\mathrm{U}(2)$, because $\mathrm{U}(2)\not\subset\mathrm{SL}(2,\mathbb{C})$.

A boost is a unit element and is not unitary. A unitary element whose determinant is not one is unitary and is not a unit element. The glyph asserts the first and never the second; an article that needs a unitary element states $\tilde Q^{*}\tilde Q=e_t$ on it.

**The norm and the group condition exist only where their involution does**: the bar alone over $\mathbb{C}$ and the split-complex numbers, the natural sign alone over $\mathbb{H}$ and the split-quaternions, the bar, the tessarine sign and the star over $\mathbb{B}_{\mathrm{r}}$, and all four marks over $\mathbb{B}$ and the split-biquaternions.

**The case rule splits the glyph**, as for the elements: $\tilde U$ in the biquaternion and split-biquaternion layers, $\tilde u$ in the quaternion and split-quaternion ones, $U$ in the complex, split-complex, dual and reduced biquaternion ones. The pure case carries the arrow, $\vec u$ and $\vec U$.

**The coordinates carry the letter of the unit element**: in $\mathbb{B}$ it is $\tilde U = U_te_t + U_x\vec e_x + U_y\vec e_y + U_z\vec e_z$ with $U_\mu = u_\mu + iu'_\mu$ and vector part $\vec U = \vec u + i\vec u'$; in $\mathbb{H}$ it is $\tilde u = u_te_t + u_x\vec e_x + u_y\vec e_y + u_z\vec e_z$ with real $u_\mu$. **A coordinate carries the label of its direction**, as the base does: the scalar coordinate is $U_t$ and the vector coordinates are $U_x, U_y, U_z$, and likewise $u_t, u_x, u_y, u_z$ for the quaternion-layer element $\tilde u$; a role label is written in the upright roman where the statement names a role. **It is allowed to add subscripts when several unit elements are used**, $\tilde U_1, \tilde U_2$.

### The Letters $U$ and $u$ Outside the Layers

The reservation above is **local to the layers of the biquaternion family** — the complex, split-complex, dual and reduced biquaternion layers, the quaternion, split-quaternion, biquaternion and split-biquaternion layers, and the operator articles built on them. Inside them the glyphs $u$, $\tilde u$, $\vec u$, $U$, $\tilde U$ and $\vec U$ name unit elements and nothing else.

Outside them the letter keeps a single shape for a single meaning, and the font carries the distinctions the layers do not need. The **unitary group** and the **universal enveloping algebra** are upright roman, $\mathrm{U}(n)$, $\mathrm{U}(H)$, $\mathrm{U}(\mathbb B)$, $\mathrm{U}(\mathfrak g)$; the **group of units** of a ring is the sans-serif $\mathsf{U}(R)$, which the corpus more usually writes $R^{\times}$; a **family of sets** — an open cover, a filter, a uniformity — is the script $\mathcal U$; and the **up quark** and the **atomic mass unit** are the upright roman $\mathrm u$. The italic letters $U$ and $u$ are reserved: outside the layers they never name an open set, a flow or evolution operator, a horocycle, a Jordan quadratic representation, a dual element, an internal energy or an unknown function.

## Summary

The four letters $P$, $N$, $H$ and $K$ name the four algebraic norms with one argument, beside the four forms with two. A biquaternion is **$\Phi$-regular** when $\Phi(\tilde Q)\neq0$ and **$\Phi$-degenerate** when $\Phi(\tilde Q)=0$; only $N$ decides invertibility, so the $N$-regular elements are the units and the $N$-degenerate ones the non-units, while the other three pairs are not a partition into invertible and singular.

The six layer tables give, for each layer, only the brackets that survive on its glyph. The **algebraic norm** is the diagonal of the form, the **realified signature** is that of the real quadratic form with the positive directions counted first, and the **role** records whether the bracket carries the topology or the invertibility criterion. In $\mathbb{C}$ the star bracket is definite and multiplicative at once; in the split-complex numbers the two exchange their signatures and no bracket is both; in the quaternion and biquaternion layers the Hermitian bracket is the definite one and the quaternionic norm the multiplicative one; in the reduced biquaternions no mark degenerates and the four remain distinct.

**Norm one** is fixed layer by layer: $\{\pm1\}$ over the reals, the unit circle over the complex numbers, the unit hyperbola over the split-complex numbers, the two lines $\pm1+\mathrm{M}$ over the dual numbers, the unit group of the layer over the quaternion and biquaternion algebras. The glyphs $u$, $\tilde u$, $U$ and $\tilde U$ mark a unit element, not a unitary one: the unitary condition is a different condition, stated in §*The Unitary Convention*, and the heading keeps its old name because the corpus cites it by that name.

The reservation of $U$ and $u$ is local to the layers of the biquaternion family and to the operator articles built on them. Outside them the unitary group and the universal enveloping algebra are upright roman, $\mathrm{U}(n)$ and $\mathrm{U}(\mathfrak g)$, and the group of units of a ring is the sans-serif $\mathsf{U}(R)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P(\tilde Q)$, $N(\tilde Q)$, $H(\tilde Q)$, $K(\tilde Q)$ | The plain, quaternionic, Hermitian and Krein algebraic norms, the forms with one argument |
| $\Phi$-regular, $\Phi$-degenerate | $\Phi(\tilde Q)\neq0$ and $\Phi(\tilde Q)=0$ for $\Phi\in\{P,N,H,K\}$ |
| $\operatorname{Re}\langle Q\rangle$ | The realified form, whose signature is tabulated layer by layer |
| $U$, $\tilde U$, $\tilde u$, $\vec u$ | A unit element of a layer, and its pure case; not a unitary element |
| $\mathrm{U}(n)$ | The unitary group, upright roman, outside the layers |
| $\mathsf{U}(R)$ | The group of units of a ring, sans-serif |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998). Algebras with involution, the first and the second kind, and the classification of their involutions.
- Soo-Chang Pei, Ja-Han Chang and Jian-Jiun Ding, "Commutative reduced biquaternions and their Fourier transform for signal and image processing applications", *IEEE Transactions on Signal Processing* **52** (2004) 2012–2022. The reduced biquaternion algebra of the engineering literature, its idempotent decomposition, its ring-valued norm and its transform.
- Nicolas Bourbaki, *Éléments de mathématique* (Hermann, then Springer). The model for a notation fixed once and used without variation.
