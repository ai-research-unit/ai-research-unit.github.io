# __Biquaternions as a Vector Space over $\mathbb{C}$__

## Introduction

This article treats the biquaternions as a **complex vector space**: the set of elements, its addition, the scalar action of $\mathbb{C}$ it carries, the real structure beneath it, its coordinates, and the conjugations as linear and antilinear maps. Three further readings are added at the end as alternative views: the same set over the real scalars, then the bimodule over $\mathbb{H}$ and the module over $\mathbb{B}$ itself, the last two with bases that are rings of operators rather than fields of scalars. The goal is to lay out this linear structure precisely and to name the **six** distinguished real subspaces that arise from the conjugations: four of dimension four, together with the two-dimensional centre and the six-dimensional vector subspace. The six are not developed here: they are defined one to a section in *Introduction to the Six Subspaces*, and the three decompositions into pairs of them are *Decompositions Along the Six Subspaces*.

$\mathbb{B}$ carries its product as well, and the product makes it an algebra. That reading, with the product taken as the multiplication, is *Biquaternions as an Algebra over $\mathbb{C}$*; with the real scalars it is *Biquaternions as an Algebra over $\mathbb{R}$*; here the product is used only to say that the scalar actions are compatible with it. The four conjugations and the group they generate are *The Group of Involutions*.

The treatment is elementary and self-contained: every claim is either proved or stated as a definition, and no physics is invoked. The anti-Hermitian subspace is defined algebraically. No form appears in this article; the Hermitian form, the inner product and everything measured with them belong to the Topology group. The product of the algebra — its definition, its two scalar–vector parts, and the dot and cross products they are built from — is *The Four Biquaternion Complex Products*, and it is used here as given.

The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra, together with its basis, its multiplication and its conjugation. No facts about $\mathbb{H}$ are restated here.

## The Vector Space Structure

### Definition

The **biquaternion algebra** is the complexification of the quaternion algebra:

$$
\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H},
$$

read here as a $\mathbb{C}$-vector space: an additive group with a scalar multiplication by the complex numbers. It is therefore **four-dimensional** over $\mathbb{C}$, with complex basis $\{e_0, e_1, e_2, e_3\}$. It also carries its product, the one defined and studied in *The Four Biquaternion Complex Products*; the product is $\mathbb{C}$-bilinear, so the scalars may be moved through it, and it makes $\mathbb{B}$ an algebra over $\mathbb{C}$, a reading developed in *Biquaternions as an Algebra over $\mathbb{C}$*. Its centre is the scalar line $\mathbb{C}e_0$, spanned over $\mathbb{R}$ by $e_0$ and $ie_0$, and it is one of the six distinguished real subspaces of the group. The underlying real space, in which those six are cut out, is **eight-dimensional**, with real basis $\{e_0, e_1, e_2, e_3, ie_0, ie_1, ie_2, ie_3\}$.

The complex dimension four and the real dimension eight are related by

$$
\dim_{\mathbb{R}} \mathbb{B} = 2 \dim_{\mathbb{C}} \mathbb{B},
$$

because each complex coefficient contributes its real and imaginary parts.

### Developed Form

A general biquaternion is written in developed form as

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu \in \mathbb{C},
$$

or, more compactly, as

$$
\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu, \qquad Q_\mu \in \mathbb{C}.
$$

We write

$$
\tilde{Q} = Q_0 + \mathbf{Q}, \qquad \mathbf{Q} = \sum_{k=1}^{3} Q_k e_k,
$$

where $Q_0$ is the **complex scalar part** and $\mathbf{Q}$ is the **complex vector part**. The tilde signals that $\tilde{Q}$ is an element of the algebra $\mathbb{B}$, not a four-vector.

Each complex coefficient is written in terms of its real and imaginary parts:

$$
Q_0 = q_0 + i q'_0, \qquad Q_k = q_k + i q'_k, \qquad q_\mu, q'_\mu \in \mathbb{R}.
$$

The scalar imaginary $i$ satisfies $i^2 = -1$ and commutes with all quaternion units: $i e_k = e_k i$. Multiplication by it is a real-linear map $J$ of $\mathbb{B}$ with $J^2 = -\mathrm{id}$, the complex structure that carries the real reading of $\mathbb{B}$ to the complex one.

In the complex coordinates, $\tilde{Q}$ is the four-tuple $(Q_0, Q_1, Q_2, Q_3)$.

### The Coordinate Systems

The same element is written in three coordinate systems, and all three are used below.

**Real coordinates.** Splitting each complex coefficient as $Q_\mu = q_\mu + iq'_\mu$ with $q_\mu, q'_\mu \in \mathbb{R}$ gives a list of eight real numbers on the real basis:

$$
\tilde{Q} = q_0e_0 + q_1e_1 + q_2e_2 + q_3e_3 + q'_0(ie_0) + q'_1(ie_1) + q'_2(ie_2) + q'_3(ie_3).
$$

**Complex coordinates.** Collecting the eight real numbers into four complex ones gives the developed form, four complex coordinates $(Q_0, Q_1, Q_2, Q_3)$ on the complex basis $\{e_0, e_1, e_2, e_3\}$.

**Quaternionic coordinates.** Collecting them by the scalar imaginary instead gives

$$
\tilde{Q} = h_1 + ih_2, \qquad h_1 = \sum_{\mu=0}^{3} q_\mu e_\mu \in \mathbb{H}, \qquad h_2 = \sum_{\mu=0}^{3} q'_\mu e_\mu \in \mathbb{H},
$$

a real quaternion plus $i$ times another real quaternion. The decomposition is unique, so in this view an element is a **pair of quaternions**.

| coordinates | basis | count | scalars |
|---|---|---|---|
| real | $e_0, e_1, e_2, e_3, ie_0, ie_1, ie_2, ie_3$ | $8$ | $\mathbb{R}$ |
| complex | $e_0, e_1, e_2, e_3$ | $4$ | $\mathbb{C}$ |
| quaternionic | $e_0, ie_0$ | $2$ | $\mathbb{H}$ |

The three rows count the same element against three scalar systems, and all three are used below.

### Conjugations

There are **four** natural conjugations on $\mathbb{B}$. The first three are obtained from the quaternion conjugation ${}^{\natural}$ and the complex conjugation $\bar{\cdot}$; the fourth is defined as the negative of Hermitian conjugation:

**Quaternion conjugation** $\tilde{Q}^{\natural}$:

$$
\tilde{Q}^{\natural} = Q_0 e_0 - Q_1 e_1 - Q_2 e_2 - Q_3 e_3.
$$

**Complex conjugation** $\bar{\tilde{Q}}$:

$$
\bar{\tilde{Q}} = \bar{Q_0} e_0 + \bar{Q_1} e_1 + \bar{Q_2} e_2 + \bar{Q_3} e_3.
$$

**Hermitian conjugation** $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$:

$$
\tilde{Q}^{*} = \bar{Q_0} e_0 - \bar{Q_1} e_1 - \bar{Q_2} e_2 - \bar{Q_3} e_3.
$$

**Anti-Hermitian conjugation** $\tilde{Q}^\flat = -\tilde{Q}^{*}$:

$$
\tilde{Q}^\flat = -\bar{Q_0} e_0 + \bar{Q_1} e_1 + \bar{Q_2} e_2 + \bar{Q_3} e_3.
$$

Each conjugation is an involution: applying it twice returns the original biquaternion. Each therefore splits $\mathbb{B}$ into a fixed space and an anti-fixed space, and each of the two is a real vector subspace of $\mathbb{B}$. These spaces are the **six distinguished subspaces** of $\mathbb{B}$, defined one to a section in *Introduction to the Six Subspaces* and tabulated in *Comparison of the Six Subspaces*.

The two anti-automorphisms ${}^{\natural}$ and ${}^{*}$, the Klein four-group they generate with the identity and their composite $\bar{\cdot}$, and the place of the reversal outside it are *The Group of Involutions*; the composition table that includes the reversal and the lattice of fixed spaces are *Biquaternion Involution Lattice*. Neither the group nor the six subspaces are repeated here: this article keeps the four formulas above, and the three decompositions the conjugations cut out are *Decompositions Along the Six Subspaces*.

## Alternative View: Biquaternions as a Vector Space over $\mathbb{R}$

### The Real Scalars

**Definition.** The **real reading** of $\mathbb{B}$ is the same additive group over the subfield $\mathbb{R}$ of $\mathbb{C}$, obtained by restriction of scalars: the elements are unchanged and the scalar domain is cut from $\mathbb{C}$ down to the subfield $\mathbb{R}$. The general element is written in the eight real coordinates of §*The Coordinate Systems*, on the real basis

$$
e_0, e_1, e_2, e_3, ie_0, ie_1, ie_2, ie_3 .
$$

Every element is a unique real combination of those eight, so the real dimension is the complex dimension doubled, $\dim_\mathbb{R}\mathbb{B} = 2\dim_\mathbb{C}\mathbb{B} = 8$, as recorded in §*The Vector Space Structure*.

**Remark.** No complex number is used as a scalar in this reading: the scalars are real, and the complex reading is the stronger structure rather than a different set. Every statement made over $\mathbb{R}$ holds over $\mathbb{C}$, since a complex scalar is a pair of real ones, and the real reading keeps the additive group, the basis and the product while dropping the complex scalars alone.

### The Complex Structure

The difference between the two readings is carried by one operator. Multiplication by the central imaginary,

$$
J : \tilde{Q} \mapsto i\tilde{Q}, \qquad J^2 = -\mathrm{id},
$$

is real-linear, and it is the **complex structure** of the real space, already named in §*Developed Form*. It carries the whole gap between the readings: for $\lambda = a + bi$, the centrality of the scalars gives

$$
\lambda\tilde{Q} = a\tilde{Q} + bJ(\tilde{Q}),
$$

so the complex action is the real action together with $J$, and the real space together with $J$ is the complex space.

**Proposition (linearity is the commutator with $J$).** A real-linear map $T$ of $\mathbb{B}$ is $\mathbb{C}$-linear exactly when it commutes with $J$, and antilinear exactly when it anticommutes with it:

$$
T(\lambda\tilde{Q}) = \lambda T(\tilde{Q}) \text{ for all } \lambda \iff TJ = JT, \qquad T(\lambda\tilde{Q}) = \bar{\lambda} T(\tilde{Q}) \text{ for all } \lambda \iff TJ = -JT .
$$

**Proof.** Let $T$ be real-linear. Then $T(J\tilde{Q}) = T(i\tilde{Q})$ and $J(T\tilde{Q}) = iT(\tilde{Q})$, so the identity $T(i\tilde{Q}) = iT(\tilde{Q})$ is exactly $TJ = JT$; real-linearity then gives $T(\lambda\tilde{Q}) = T(a\tilde{Q} + bJ\tilde{Q}) = aT(\tilde{Q}) + bJT(\tilde{Q}) = \lambda T(\tilde{Q})$ for every $\lambda = a + bi$, and conversely $TJ = JT$ gives $T(i\tilde{Q}) = iT(\tilde{Q})$ and hence the same identity. The antilinear case is the same computation with the sign reversed, $T(i\tilde{Q}) = -iT(\tilde{Q})$, which is $TJ = -JT$. $\square$

### Linear and Antilinear Maps

The four conjugations of §*Conjugations* are all real-linear, and the proposition separates them into two classes: ${}^{\natural}$ commutes with $J$ and is $\mathbb{C}$-linear, while $\bar{\cdot}$, ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ and $\flat = -{}^{*}$ anticommute with $J$ and are antilinear. The line between the two kinds of map is thus the commutation with one operator.

The real reading sees more linear maps than the complex one:

$$
\operatorname{End}_\mathbb{R}(\mathbb{B}) \cong M_8(\mathbb{R}), \qquad \operatorname{End}_\mathbb{C}(\mathbb{B}) \cong M_4(\mathbb{C}),
$$

of real dimensions $64$ and $32$. The $\mathbb{C}$-linear maps are the real-linear ones commuting with $J$, a subspace of half the dimension; a real-linear map that anticommutes with $J$ is antilinear, an ordinary linear map of the real space that is not a complex-linear operator. The conjugations are the natural examples.

### The Real Form

A real subspace of $\mathbb{B}$ of real dimension four need not be closed under $J$; when it meets its image under $J$ only at zero, the two together fill $\mathbb{B}$ and the subspace is a **real form**.

**Proposition.** Let $V$ be a real subspace of $\mathbb{B}$ of real dimension four. Then $V \cap JV = 0$ if and only if $\mathbb{B} = V \oplus JV$, and in that case the complex reading is recovered from $V$ by extension of scalars, $\mathbb{C}\otimes_\mathbb{R}V\cong\mathbb{B}$.

**Proof.** If $\mathbb{B} = V \oplus JV$, then $V \cap JV = 0$ by the directness of the sum. Conversely let $V \cap JV = 0$. If $v + Jw = 0$ with $v, w \in V$, then $v = -Jw$ lies in $V \cap JV$, so $v = 0$ and then $Jw = 0$; the map $V \oplus JV \to \mathbb{B}$, $(v, w)\mapsto v + w$, is therefore injective, and since both sides have real dimension eight it is an isomorphism, $\mathbb{B} = V \oplus JV$. The map $\mathbb{C}\otimes_\mathbb{R}V \to \mathbb{B}$, $z \otimes v \mapsto zv$, is then $\mathbb{C}$-linear and surjective, because its image contains $V$ and $JV$, hence all of $\mathbb{B}$, and both spaces have complex dimension four, so it is an isomorphism. $\square$

**Example.** The elements with real coefficients, spanned by $e_0, e_1, e_2, e_3$, form a real form; its image under $J$ is the subspace of elements with purely imaginary coefficients, the two meet at zero and their sum is $\mathbb{B}$. Real forms are not unique, and the choice of one is data beyond the real reading.

**Remark (the two real spaces, of dimensions eight and four).** The two dimensions must not be confused. The restriction of scalars of the complex reading is the eight-dimensional space above, whose extension of scalars back to $\mathbb{C}$ has complex dimension eight; the extension of scalars of a real form is the four-dimensional complex space $\mathbb{B}$ itself. What returns the complex reading from the eight-dimensional space is the operator $J$, not a scalar extension. The version of this caution for the algebra and its base rings, where $\mathbb{C}\otimes_\mathbb{R}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$, is *Biquaternions as an Algebra over $\mathbb{R}$*.

**Remark (the six subspaces in the real reading).** The six distinguished subspaces are real subspaces, and the complex structure sorts them: the centre and the vector subspace are carried to themselves by $J$ and are the only two that are complex subspaces, of complex dimensions one and three, while the other four are real forms, exchanged in two pairs by $J$. The six are defined in *Introduction to the Six Subspaces*, and the action of the central imaginary unit upon them is *Comparison of the Six Subspaces*.

### What the View Adds

The real reading sees more subspaces than the complex one, since every complex subspace is a real subspace and the converse fails, and it makes the antilinear maps visible as ordinary linear maps. It costs the complex structure, which leaves the scalars and must be carried by $J$ whenever the complex action is meant. The product stays $\mathbb{R}$-bilinear, so the four products of *The Four Biquaternion Complex Products* and the ring-based views that follow are read over $\mathbb{R}$ unchanged.

## Alternative View: Biquaternions as a Bimodule over $\mathbb{H}$

### The Two Actions

**Definition.** The **left and right $\mathbb{H}$-actions** on $\mathbb{B} = \mathbb{C} \otimes_\mathbb{R} \mathbb{H}$ are

$$
h \cdot (A \otimes h') = A \otimes hh', \qquad (A \otimes h') \cdot h = A \otimes h'h .
$$

The left action is left multiplication by $1 \otimes h$, the right action is right multiplication by the same element, and both are $\mathbb{R}$-bilinear. They **commute**,

$$
(h \cdot \tilde Q) \cdot h' = A \otimes hh'h' = h \cdot (\tilde Q \cdot h'),
$$

by associativity of the product, so $\mathbb{B}$ is an $\mathbb{H}$-**bimodule**.

### Free of Rank Two

In the quaternionic coordinates an element is $\tilde Q = h_1 + ih_2$ with $h_1, h_2 \in \mathbb{H}$, and the two actions are

$$
h \cdot \tilde Q = (hh_1) + i(hh_2), \qquad \tilde Q \cdot h = (h_1h) + i(h_2h),
$$

using the centrality of $i$. The decomposition $\tilde Q = h_1 + ih_2$ is unique, so $\{e_0, ie_0\}$ is a basis on the right and on the left at once:

$$
\mathbb{B} = \mathbb{H}e_0 \oplus \mathbb{H}(ie_0) \cong \mathbb{H}^2 \quad \text{on each side},
$$

and $\mathbb{B}$ is **free of rank two** over $\mathbb{H}$. It is worth noticing which elements serve as the generators: $e_0$ and $ie_0$ span the plane $\mathbb{C}_{\mathbb{B}}$ of the centre. The two free generators over $\mathbb{H}$ are a real basis of the centre of $\mathbb{B}$.

### The Endomorphisms

Because $\mathbb{B}$ is free of rank two as a right $\mathbb{H}$-module, its $\mathbb{H}$-linear endomorphisms are the two-by-two matrices over $\mathbb{H}$:

$$
\operatorname{End}_\mathbb{H}(\mathbb{B}) \cong M_2(\mathbb{H}).
$$

This is the standard description of the endomorphism ring of a free module of rank two over a ring, and it holds over a non-commutative base without change.

### A Bimodule Is Not a Scalar Structure

The two actions give the quaternions a reach over $\mathbb{B}$ that is **not** the reach of a scalar field. Multiplication is left $\mathbb{H}$-linear in the first argument and right $\mathbb{H}$-linear in the second,

$$
(h \cdot \tilde Q) \cdot \tilde P = h \cdot (\tilde Q \cdot \tilde P), \qquad \tilde Q \cdot (\tilde P \cdot h) = (\tilde Q \cdot \tilde P) \cdot h,
$$

but it is **not** fully $\mathbb{H}$-bilinear, since for non-central $h$

$$
\tilde Q \cdot (h \cdot \tilde P) - h \cdot (\tilde Q \cdot \tilde P) = (\tilde Qh - h\tilde Q)\tilde P = [\tilde Q,h]\tilde P,
$$

which does not vanish in general. A ring with exactly these properties is an **$\mathbb{H}$-ring**, and the failure is measured by the commutator. The quaternions are not central in $\mathbb{B}$, which is why $\mathbb{H}$ is a ring of operators here and not a second field of scalars; the base-ring question is decided in *Biquaternions as an Algebra over $\mathbb{R}$*.

## Alternative View: Biquaternions as a Module over Itself

One more structure sits apart from the scalar question. The algebra acts on its own additive group by its multiplication, and the module so obtained is the **regular module**; its base is the algebra itself, not one of the three scalar rings, so it neither competes with the scalar views nor refines them: it is the general construction by which every ring is a module over itself, applied to $\mathbb{B}$.

Read on the left, the action $\tilde Q\cdot\tilde R=\tilde Q\tilde R$ makes $\mathbb{B}$ the **left regular module** ${}_{\mathbb{B}}\mathbb{B}$; read on the right, $\tilde R\cdot\tilde Q=\tilde R\tilde Q$ makes it the **right regular module** $\mathbb{B}_{\mathbb{B}}$; read on both sides, the two commuting actions make it the **regular bimodule** ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$. What the view adds is a second dictionary alongside the endomorphism ring $\operatorname{End}_{\mathbb{H}}(\mathbb{B})\cong M_2(\mathbb{H})$ of the quaternionic bimodule. The submodules of the regular module are the **ideals** — left, right and two-sided — so the ideal theory of $\mathbb{B}$ is the module theory of ${}_{\mathbb{B}}\mathbb{B}$; the module is free of rank one on $e_0$, cyclic and faithful, a generator, and the identity of the tensor product, $M\otimes_{\mathbb{B}}{}_{\mathbb{B}}\mathbb{B}\cong M$; and its endomorphism rings are

$$
\operatorname{End}_{\mathbb{B}}(\mathbb{B}_{\mathbb{B}})\cong\mathbb{B},\qquad \operatorname{End}_{\mathbb{B}}({}_{\mathbb{B}}\mathbb{B})\cong\mathbb{B}^{\mathrm{op}},\qquad \operatorname{End}_{\mathbb{B}\text{-}\mathbb{B}}(\mathbb{B})\cong Z(\mathbb{B})=\mathbb{C}.
$$

The last of these is the centre reappearing as an endomorphism ring, the statement that the only linear operators commuting with both actions are the scalars. The view is the subject of *The Regular Module and the Regular Bimodule over the Biquaternion Algebra*, and its operator reading is *Biquaternion 4×4 Regular Matrix Element Representation*.

## Summary

The biquaternion algebra is the set $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, a complex vector space of dimension four on the basis $e_0 = 1, e_1, e_2, e_3$, with $e_k^2 = -e_0$, and a real vector space of dimension eight on the basis $e_0, e_1, e_2, e_3, ie_0, ie_1, ie_2, ie_3$, the two dimensions related by $\dim_\mathbb{R}\mathbb{B} = 2\dim_\mathbb{C}\mathbb{B}$. The central element $i$ is a complex structure $J$, $J^2 = -\mathrm{id}$.

The space carries two scalar actions. Over $\mathbb{C}$ the scalars are the centre; over $\mathbb{R}$ they are the subfield, the same set with the scalars cut down to $\mathbb{R}$, of dimension eight. The real reading is the restriction of scalars of the complex one, and the complex structure $J$, the multiplication by $i$, is what returns one from the other: the real-linear maps commuting with $J$ are the $\mathbb{C}$-linear ones and those anticommuting with it are the antilinear ones, and a real form, a real subspace of dimension four meeting its image under $J$ only at zero, recovers the complex reading by extension of scalars.

It carries four natural conjugations, ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ and $\flat = -{}^{*}$, of which the first three are commuting involutions; the group they form is *The Group of Involutions*. They define the six distinguished real subspaces of $\mathbb{B}$, defined one to a section in *Introduction to the Six Subspaces*, and the three direct-sum decompositions they cut out are *Decompositions Along the Six Subspaces*; the coordinate blocks, the intersections, the sums and the action of the conjugations upon the six are *Comparison of the Six Subspaces*.

Beyond the scalar fields it carries two structures whose base is not a field. Over $\mathbb{H}$ it is a bimodule with commuting left and right actions, free of rank two on each side on the generators $e_0$ and $ie_0$, with endomorphism ring $\operatorname{End}_\mathbb{H}(\mathbb{B})\cong M_2(\mathbb{H})$, and its product is not fully $\mathbb{H}$-bilinear. Over itself it is the regular module, in the three readings ${}_{\mathbb{B}}\mathbb{B}$, $\mathbb{B}_{\mathbb{B}}$ and ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$.

The product read as the multiplication of an algebra is *Biquaternions as an Algebra over $\mathbb{C}$*, and with the real scalars it is *Biquaternions as an Algebra over $\mathbb{R}$*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra |
| $\mathbb{B}$ | Biquaternion algebra, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $e_0 = 1$ | Identity |
| $e_1, e_2, e_3$ | Quaternion units, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$, commutes with $e_k$ |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | General biquaternion |
| $Q_\mu = q_\mu + i q'_\mu$ | Complex coefficient, with $q_\mu, q'_\mu \in \mathbb{R}$ |
| $Q_0$ | Complex scalar part |
| $\mathbf{Q}$ | Complex vector part |
| $J : \tilde{Q} \mapsto i\tilde{Q}$ | the real-linear complex structure, $J^2 = -\mathrm{id}$ |
| $\operatorname{Res}_{\mathbb{C}/\mathbb{R}}\mathbb{B}$ | the real reading: same additive group and same elements over the scalars $\mathbb{R}$, dimension $8$ |
| real form of $\mathbb{B}$ | a real subspace $V$ of real dimension $4$ with $\mathbb{B} = V \oplus JV$, e.g. the elements with real coefficients |
| $h \cdot \tilde Q = A \otimes hh'$, $\tilde Q \cdot h = A \otimes h'h$ | the left and right $\mathbb{H}$-actions |
| $\mathbb{B} \cong \mathbb{H}^2$ | free $\mathbb{H}$-module of rank two on each side, generators $e_0, ie_0$ |
| $\operatorname{End}_\mathbb{H}(\mathbb{B}) \cong M_2(\mathbb{H})$ | the $\mathbb{H}$-linear endomorphisms |
| $\mathbb{H}$-ring | bimodule over $\mathbb{H}$ with multiplication left linear in the first argument and right linear in the second |
| ${}_{\mathbb{B}}\mathbb{B}$, $\mathbb{B}_{\mathbb{B}}$, ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$ | left regular module, right regular module, regular bimodule |
| $\tilde{Q}^{\natural} = Q_0 e_0 - \mathbf{Q}$ | Quaternion conjugate |
| $\bar{\tilde{Q}} = \bar{Q_0} e_0 + \mathbf{Q}^*$ | Complex conjugate |
| $\tilde{Q}^{*} = \bar{Q_0} e_0 - \mathbf{Q}^*$ | Hermitian conjugate |
| $\tilde{Q}^\flat = -\overline{\tilde{Q}^{\natural}} = -\tilde{Q}^{*}$ | Anti-Hermitian conjugate |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Nicolas Bourbaki, *Algebra I* (Springer, 1998), for vector spaces, modules, bimodules and the tensor product.
- Tsit Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for the regular module, ideals as its submodules, and the endomorphism rings of a free module.
