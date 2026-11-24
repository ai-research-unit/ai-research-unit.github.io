# __Special Element and Peirce Conventions__

## Introduction

A root, an idempotent and a nilpotent are not new kinds of object: each is an element of the algebra, and the glyph records what the element is known to be at the point of use. This article fixes those glyphs, their case rule, their coordinates and their subscripts, and then the Peirce convention, which fixes the words and the glyphs of the decomposition that a complete family of idempotents generates, and finally the three words of a spinor: the spin, the elementary spinor and the Dirac spinor.

The special elements are read after the base because their case rule is the case rule of the elements, and before the representations because the canonical frame of the matrix model is the Peirce frame of the standard pair. The order is: the root, the idempotent, the nilpotent, then the general Peirce convention and its biquaternion reading, and then the spin and the two spinors, which are read on the carriers the convention produces.

The article assumes *Algebra and Element Conventions*, whose §*The Conjugations* fixes the star that the Hermitian idempotent uses, and it is assumed by *Matrix Representations Conventions*, whose §*The 4×4 Regular Representation* writes the canonical frame in the standard pair and its mixed units.

**No contravariant index appears in this article, and none appears anywhere in the series.** The one metric is the unit metric $\delta_{\mu\nu}=(1,1,1,1)$; a metric that is the identity raises nothing, so a raised index would name the same index twice. Every coefficient is written low, every contraction is written as a sum with the weight $\sum_\mu\varepsilon_\mu$, and no letter carries a raised spacetime index, in a display, in a table or in a definition.

## The Special Elements: Root, Idempotent and Nilpotent

**The special glyphs are notational.** A root $\tilde{Ζ}$, an idempotent $\tilde\Pi_{\mathrm{id}}$ or a nilpotent $\tilde\Pi_{\mathrm{nil}}$ is not a different kind of object from a generic $\tilde Q$: the glyph records what the element is known to be, at the point of use.

### The Potent Tag

The idempotent and the nilpotent are the two ends of one Peirce structure, and the tag says which end. The **potent family** is the idempotents and the nilpotents together, and a member carries its kind as the first word of its subscript: $\mathrm{id}$ for the idempotent, $\mathrm{nil}$ for the nilpotent. The case and the accent stay the letter's, as §*The Idempotent Convention* and §*The Nilpotent Convention* fix them: the tilde marks the quaternion and biquaternion layers and nobody else, the capital marks the algebras with a complex or quaternionic factor, and the tilde-free layers write the plain capital.

| layer | idempotent | nilpotent |
|---|---|---|
| $\mathbb{B}$, $\mathbb{B}_{\mathrm{spl}}$ | $\tilde\Pi_{\mathrm{id}}$ | $\tilde\Pi_{\mathrm{nil}}$ |
| $\mathbb{H}$, $\mathbb{H}_{\mathrm{spl}}$ | $\tilde\pi_{\mathrm{id}}$ | $\tilde\pi_{\mathrm{nil}}$ |
| $\mathbb{C}$, $\mathbb{C}_{\mathrm{dln}}$ | $\Pi_{\mathrm{id}}$ | $\Pi_{\mathrm{nil}}$ |
| $\mathbb{C}_{\mathrm{spl}}$, reduced $\mathbb{B}$ | $\Pi_{\mathrm{id},\pm}$ | $\Pi_{\mathrm{nil}}$ |

The tilde is the mark of the quaternion and biquaternion layers and it is written nowhere else. The complex, split-complex and dual layers carry the plain capital in both kinds, $\Pi_{\mathrm{id}}$ and $\Pi_{\mathrm{nil}}$, and the reduced biquaternion layer writes the plain capital with the sign pair, $\Pi_{\mathrm{id},\pm}$ and $\Pi_{\mathrm{nil}}$. The capital separates the nilpotent of those layers from the lower-case nilpotent of the quaternion layers, and the prose names the layer; the tilde never does that work on a tilde-free layer.

The **roots are outside the family** in this pass and keep the glyphs of §*The Root Convention*. A pure member carries the arrow and no tilde, by §*The Centre and the Vector Subspace* of *Algebra and Element Conventions*, so the pure nilpotent is $\vec\Pi_{\mathrm{nil}}$ or $\vec\pi_{\mathrm{nil}}$; an idempotent has no pure form, and no arrowed idempotent exists. The subscript is read sector, kind, sign, index, so a member of a sign pair is $\tilde\Pi_{\mathrm{id},+}$ and a numbered member is $\tilde\Pi_{\mathrm{id},1}$. The **Peirce indices are not kinds**: in a mixed component $A_{ij}$ the idempotent that multiplies on the left is $\tilde\Pi_{\mathrm{id},i}$ and the one on the right is $\tilde\Pi_{\mathrm{id},j}$, and a mixed unit $\tilde\Pi_{\mathrm{nil},ij}$ carries the same pair after its kind.

### The Root Convention

The roots carry a symbol of their own, beside the idempotent $\tilde\Pi_{\mathrm{id}}$ and the nilpotent $\tilde\Pi_{\mathrm{nil}}$, both of §*The Potent Tag*: the **root glyph**, in the two cases. The root is outside the potent family and carries no tag.

A **root of $1$** of the algebra is an element $\tilde{Ζ}$ with $\tilde{Ζ}^2 = 1$. More generally a **root of a central value** $\lambda$ is an element with $\tilde{Ζ}^2 = \lambda e_t$; the roots of the three central values $-1, 0, +1$ are determined in *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*, and the general problem is *The Square Roots of a General Element in the Biquaternion Algebra*.

**The square is read in a named product**, the algebra product unless the statement names another, as for the nilpotents: the class is relative to the product, and the roots of a value are read product by product in *Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**The case rule splits the glyph, as it does for the elements, the idempotents and the nilpotents.** The roots of the biquaternion and split-biquaternion layers carry the upper-case tilde, $\tilde{Ζ}$; those of the quaternion and split-quaternion layers carry the lower-case tilde, $\tilde\zeta$; those of the complex, split-complex and dual layers carry the plain capital, $Ζ$; and those of the reduced biquaternion layer carry the same plain capital, $Ζ$, no tilde being written where there is no quaternionic factor.

**The coordinates carry the letter of the root**: in $\mathbb{B}$ the root is $\tilde{Ζ} = Ζ_te_t + Ζ_x\vec e_x + Ζ_y\vec e_y + Ζ_z\vec e_z$ with $Ζ_\mu = \zeta_\mu + i\zeta'_\mu$, its scalar part $Ζ_t$ and its vector part $\vec{Ζ} = \vec\zeta + i\vec\zeta'$; in $\mathbb{H}$ it is $\tilde\zeta = \zeta_te_t + \zeta_x\vec e_x + \zeta_y\vec e_y + \zeta_z\vec e_z$ with real $\zeta_\mu$.

**It is allowed to add subscripts when several roots are used.** **The subscript of a root is numeric when it counts and a role label when it names.** Where more than one occurs the roots are numbered, $\tilde{Ζ}_1, \tilde{Ζ}_2$, as for the nilpotents and for the idempotent pairs other than the complete sign pair of §*The Idempotent Convention*; where a root plays a named role, it carries the role in upright roman as its subscript. A sign is a subscript where the statement needs one.

The root glyph is therefore **split by the case rule**, and the split is the reason the convention is stated:

| Symbol | Role |
|---|---|
| $Ζ$ | A root of $1$ of the complex, split-complex or dual layer, where no tilde is written |
| $Ζ_\pm$ | A root of $1$ of the reduced biquaternion layer, where no tilde is written |
| $\tilde\zeta$ | A root of $1$ of the quaternion or split-quaternion layer |
| $\tilde{Ζ}$ | A root of $1$ of the biquaternion or split-biquaternion layer |

### The Idempotent Convention

The convention of *The Elements and their Coefficients* fixes the case and the tilde of a generic element. The idempotents carry a symbol of their own, and the corpus uses it throughout.

An **idempotent** of the algebra is an element $\tilde\Pi_{\mathrm{id}}$ with $\tilde\Pi_{\mathrm{id}}^2 = \tilde\Pi_{\mathrm{id}}$. An idempotent fixed by the star, $\tilde\Pi_{\mathrm{id}}^{*} = \tilde\Pi_{\mathrm{id}}$, is a **Hermitian idempotent**, and the rank-one Hermitian idempotents of $\mathbb{B}_{\Psi}$, the Hermitian subspace, are the **pure states**.

**The case rule splits the glyph, as it does for the elements.** The idempotents of the biquaternion and split-biquaternion layers carry the upper-case tilde, $\tilde\Pi_{\mathrm{id}}$; those of the quaternion and split-quaternion layers carry the lower-case tilde, $\tilde\pi_{\mathrm{id}}$; those of the complex and dual layers carry the plain capital, $\Pi_{\mathrm{id}}$, no tilde being written where there is no quaternionic factor. The same splitting of the identity is written $\tilde\pi_{\mathrm{id},1,2}$ in $\mathbb{H}_{\mathrm{spl}}$ (*Split-Quaternion Idempotents and Projections*), while the split-complex layer $\mathbb{C}_{\mathrm{spl}}$ (*Square Roots of One and the Idempotents of the Split-Complex Algebra*) and the reduced biquaternion layer $\mathbb{B}_{\mathrm{red}}$ write the complete pair with the signs, $\Pi_{\mathrm{id},\pm}$, the member attached to $+1$ taking the subscript $+$ and the member attached to $-1$ the subscript $-$; the idempotents of the split-biquaternion layer are the $\tilde\Pi_{\mathrm{id},1,2}$ of *Split-Biquaternion Idempotents and Projections*, and the layer fixes the case while the tag fixes the kind.

The involution here is the star on the elements, as *The Conjugations* fixes it, and *Algebra and Element Conventions* writes the same involution with the same star, $\tilde\Pi_{\mathrm{id}}^{*} = \tilde\Pi_{\mathrm{id}}$: the two corpora agree on the mark, and it is the dagger that is confined to the operators.

**The coordinates carry the letter of the idempotent**: in $\mathbb{B}$ the idempotent is $\tilde\Pi_{\mathrm{id}} = \Pi_{\mathrm{id},t}e_t + \Pi_{\mathrm{id},x}\vec e_x + \Pi_{\mathrm{id},y}\vec e_y + \Pi_{\mathrm{id},z}\vec e_z$ with $\Pi_{\mathrm{id},\mu} = \pi_{\mathrm{id},\mu} + i\pi'_{\mathrm{id},\mu}$, its scalar part $\Pi_{\mathrm{id},t}$ and its vector part $\vec\Pi = \vec\pi + i\vec\pi'$; in $\mathbb{H}$ it is $\tilde\pi_{\mathrm{id}} = \pi_{\mathrm{id},t}e_t + \pi_{\mathrm{id},x}\vec e_x + \pi_{\mathrm{id},y}\vec e_y + \pi_{\mathrm{id},z}\vec e_z$ with real $\pi_{\mathrm{id},\mu}$.

**It is allowed to add subscripts when several idempotents are used.** **The subscript of an idempotent is numeric when it counts and a role label when it names, but for the two members of a complete sign pair.** A pair is $\tilde\Pi_{\mathrm{id},1}, \tilde\Pi_{\mathrm{id},2}$; a second pair occurring in the same statement takes the next numbers, $\tilde\Pi_{\mathrm{id},3}, \tilde\Pi_{\mathrm{id},4}$; and a family indexed by a direction is written with its argument, $\tilde\Pi_{\mathrm{id},\pm}(\tilde{Ζ})$. When a pair is **complete**, $\tilde\Pi_{\mathrm{id},+} + \tilde\Pi_{\mathrm{id},-} = e_t$, its two members may be written $\tilde\Pi_{\mathrm{id},+}$ and $\tilde\Pi_{\mathrm{id},-}$, the member attached to $+1$ taking the subscript $+$ and the member attached to $-1$ the subscript $-$. A pair that is not complete may be numbered, labelled or signed as the statement requires. A role label is written in upright roman, as for a unit element. The split-complex and reduced biquaternion layers write their complete pair with the signs throughout, $\Pi_{\mathrm{id},\pm}$. The Peirce indices of the reduced biquaternion layer are the same signs, $\mathbb{B}_{\sigma\tau}=\{\breve Q:\Pi_{\mathrm{id},\sigma} \breve Q\Pi_{\mathrm{id},\tau}=\breve Q\}$ with $\sigma,\tau\in\{+,-\}$, the two signs a pair read on the left and on the right, so that a corner such as $\mathbb{B}_{++}$ is never a coordinate and never a doubled label. The sign is the sign of the member and not a second kind. The coordinates of the element in that pair are the **idempotent coordinates**, written with the sign of the member, $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$ and $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$, so that $\breve Q=Q_{+}\Pi_{\mathrm{id},+}+Q_{-}\Pi_{\mathrm{id},-}$; the sign marks a coordinate of the idempotent pair and the triangle a basis coordinate, so that a numbered element is read the same way, $Q_{1+}$ and $Q_{1-}$ for the idempotent coordinates of $\breve Q_{1}$ and $Q_{1\blacktriangle}$ and $Q_{1\blacktriangledown}$ for its basis coordinates.

A non-zero idempotent $\tilde\Pi_{\mathrm{id}}$ generates the **minimal left ideal** $\mathbb{B}\tilde\Pi_{\mathrm{id}}$; the standard pair, the classification of the idempotents, the polarisation identity, the Peirce decomposition, the matrix units and the projective geometry of the pure states are those of *Idempotents of the General Plain Algebra* and its companions.

The idempotent glyph is therefore **split by the case rule**, and the split is the reason the convention is stated:

| Symbol | Role |
|---|---|
| $\Pi_{\mathrm{id}}$ | An idempotent of the complex, split-complex or dual layer, where no tilde is written |
| $\Pi_{\mathrm{id},\pm}$ | A complete sign pair of idempotents of the split-complex or reduced biquaternion layer, where no tilde is written |
| $\tilde\pi_{\mathrm{id}}$ | An idempotent of the quaternion or split-quaternion layer |
| $\tilde\Pi_{\mathrm{id}}$ | An idempotent or a pure state of the biquaternion or split-biquaternion layer, and the minimal left ideal $\mathbb{B}\tilde\Pi_{\mathrm{id}}$ it generates |

### The Nilpotent Convention

The nilpotents carry a symbol of their own, beside the idempotent $\tilde\Pi_{\mathrm{id}}$ (§*The Idempotent Convention*): the lower-case $\tilde\pi_{\mathrm{nil}}$ of the quaternion and split-quaternion layers and the upper-case $\tilde\Pi_{\mathrm{nil}}$ of the biquaternion and split-biquaternion layers, as the case rule requires. The kind is in the tag and the layer is in the case; the letter is the letter of the idempotent.

A **nilpotent** of the algebra is an element $\tilde\pi_{\mathrm{nil}}$ whose square vanishes,

$$
\tilde\pi_{\mathrm{nil}}^2 = 0 .
$$

**The square is read in a named product**, the algebra product unless the statement names another: the corpus writes nilpotents in the four general products of *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* as well, and the class is relative to the product — an element square-zero in the plain product need not be square-zero in the general plain sesquilinear one, and in the plain antisymmetric block every central element is square-zero, the unit among them. **No nilpotent is a Hermitian idempotent**, a Hermitian nilpotent being zero, so no nilpotent is a pure state; it is nevertheless the partner of the idempotent in a minimal left ideal — for the standard pair $\mathbb{B}\vec\Pi_{\mathrm{nil},2} = \mathbb{B}\tilde\Pi_{\mathrm{id},1}$ — and its products with its star are Hermitian idempotents of that ideal.

**The coordinates carry the letter of the nilpotent**: in $\mathbb{B}$ the nilpotent is $\tilde\Pi_{\mathrm{nil}} = \Pi_{\mathrm{nil},t}e_t + \Pi_{\mathrm{nil},x}\vec e_x + \Pi_{\mathrm{nil},y}\vec e_y + \Pi_{\mathrm{nil},z}\vec e_z$ with $\Pi_{\mathrm{nil},\mu} = \pi_{\mathrm{nil},\mu} + i\pi'_{\mathrm{nil},\mu}$, its scalar part $\Pi_{\mathrm{nil},t}$ and its vector part $\vec\Pi_{\mathrm{nil}}$; in $\mathbb{H}$ it is $\tilde\pi_{\mathrm{nil}} = \pi_{\mathrm{nil},t}e_t + \pi_{\mathrm{nil},x}\vec e_x + \pi_{\mathrm{nil},y}\vec e_y + \pi_{\mathrm{nil},z}\vec e_z$ with real $\pi_{\mathrm{nil},\mu}$.

**It is allowed to add subscripts when several nilpotents are used.** **The subscript of a nilpotent is numeric when it counts and a role label when it names**, as for the idempotents apart from their complete sign pair: where more than one occurs a pair is $\tilde\pi_{\mathrm{nil},1}, \tilde\pi_{\mathrm{nil},2}$, a second pair in the same statement takes the next numbers, and where a nilpotent plays a named role it carries the role in upright roman as its subscript. A sign is a subscript where the statement needs one.

The nilpotents have no classification of the idempotent kind. The square-zero set is not one family, and which set it is depends on the product: the elements of zero norm under the general quaternionic product, the pure isotropic vectors under the associative one. The standard units and the instances are those of *Nilpotents of the General Quaternionic Algebra*, *Idempotents of the General Plain Algebra* and *Peirce Decompositions of the Biquaternion Algebra*. The standard pair of nilpotents is the two off-diagonal Peirce units of the last of these, $\vec\Pi_{\mathrm{nil},1}$ and $\vec\Pi_{\mathrm{nil},2}$, exchanged by the star.

The nilpotent glyph is one letter in two cases, the capital $\Pi$ and the lower-case $\pi$, with the tilde where the layer carries one and the kind in the subscript:

| Symbol | Role |
|---|---|
| $\tilde\Pi_{\mathrm{nil}}$ | A nilpotent of the biquaternion or split-biquaternion layer, and the minimal left ideal $\mathbb{B}\tilde\Pi_{\mathrm{nil}}$ it generates; where it spans a mixed Peirce component it is written $\tilde\Pi_{\mathrm{nil},ij}$ (§*The Peirce Convention*) |
| $\Pi_{\mathrm{nil}}$ | A nilpotent of the complex, split-complex or dual layer, with the plain capital and no tilde; a mixed Peirce component is written $\Pi_{\mathrm{nil},ij}$ |
| $\tilde\pi_{\mathrm{nil}}$ | A nilpotent of the quaternion or split-quaternion layer |
| $\vec\Pi_{\mathrm{nil}}$, $\vec\pi_{\mathrm{nil}}$ | A pure nilpotent, written with the arrow and without the tilde by the priority rule of *Algebra and Element Conventions*, §*The Centre and the Vector Subspace* |

**The standard pair carries the arrow, not the tilde.** The two off-diagonal Peirce units are pure, $\vec\Pi_{\mathrm{nil},1} = \tfrac12(i\vec e_x - \vec e_y)$ and $\vec\Pi_{\mathrm{nil},2} = \tfrac12(i\vec e_x + \vec e_y)$, with no scalar part, so by *Algebra and Element Conventions*, §*The Centre and the Vector Subspace* the arrow takes priority over the tilde and the tilde is dropped; the pair is written $\vec\Pi_{\mathrm{nil},1}, \vec\Pi_{\mathrm{nil},2}$ and never $\tilde\Pi_{\mathrm{nil},1}, \tilde\Pi_{\mathrm{nil},2}$. The tilde is kept for the general nilpotent $\tilde\Pi_{\mathrm{nil}}$, which may carry a scalar part and is not pure.

## The Peirce Convention

### The General Peirce Convention

**Introduction.** A Peirce decomposition writes an algebra as a direct sum of Peirce components, one for each ordered pair of members of a complete family of orthogonal idempotents. This convention fixes the words and the glyphs for those components; the articles state the properties.

**Scope.** $A$ is an associative algebra with unit $1$ over a field. Indices are 1-based. Every Peirce article uses the four levels below and no others.

**The family.** A family $\Pi_{\mathrm{id},1},\dots,\Pi_{\mathrm{id},n}$ is **complete, orthogonal and idempotent** when

$$
\Pi_{\mathrm{id},i}^2=\Pi_{\mathrm{id},i},\qquad \Pi_{\mathrm{id},i}\Pi_{\mathrm{id},j}=0\ (i\ne j),\qquad \sum_{i=1}^{n}\Pi_{\mathrm{id},i}=1 .
$$

The subscripts are numeric, 1-based, and the family is unordered. A family that does not sum to $1$ is not a Peirce family; adjoining the complement is a construction of the articles, not part of this convention. The sign pair $\Pi_{\mathrm{id},+},\Pi_{\mathrm{id},-}$ belongs to §*The Idempotent Convention* and is not repeated here.

**The decomposition.** The Peirce decomposition relative to the family is

$$
A=\bigoplus_{i,j=1}^{n}A_{ij},\qquad A_{ij}=\Pi_{\mathrm{id},i}A\Pi_{\mathrm{id},j} .
$$

The left index is written first. The summands are **Peirce components**, and the array of them is the **Peirce table**. The components multiply by the rule: the second index of the first factor must equal the first index of the second, otherwise the product is zero. So $A_{ij}A_{jq}\subseteq A_{iq}$, and $A_{ij}A_{pq}=0$ when $j\ne p$.

The decomposition is **canonical**: it depends on the family and on nothing else. A component is called a **line** when it is one-dimensional. The word **fine** is used only for a maximal family, when every component is a line. The word **complete** refers only to $\sum_i\Pi_{\mathrm{id},i}=1$. The word **full** is not used.

**The basis and the gauge.** A **Peirce basis** is a choice of one nonzero element in each line, with

$$
E_{ij}E_{jq}=E_{iq},\qquad E_{ii}=\Pi_{\mathrm{id},i} .
$$

It exists only when the components are lines, it is not canonical, and every statement using it says so: "in a Peirce basis", "in the basis adapted to the family".

The **Peirce gauge** is the replacement

$$
E_{ij}\longmapsto t_it_j^{-1}E_{ij},\qquad t_i\ne0,
$$

which leaves the family, the components and the products fixed. With a star, $\lvert t_i\rvert=1$ and the gauge is a torus of phases.

A **Peirce frame** is a Peirce basis together with the data that selects it.

**Coordinates and spinors.** The **Peirce coordinates** of an element $Q\in A$ are the numbers $Q_{ij}$ in $Q=\sum_{i,j}Q_{ij}E_{ij}$. The coordinates carry the glyph of the element, by the case rule of the layer: $q_{ij}$ for a real element, $Q_{ij}$ for a complex one, $\tilde q_{ij}$ or $\tilde Q_{ij}$ for a quaternion, split-quaternion, biquaternion or split-biquaternion one. No separate letter is used for a coordinate.

A **spinor** is the tuple of $n$ coordinates of one row of the table, at fixed left index,

$$
\psi=(\psi_1,\dots,\psi_n),\qquad \psi_j=Q_{ij}\ \text{for fixed } i .
$$

When a spinor is treated as an object of its own, its entries are written $\psi_j$; they are the coordinates $Q_{ij}$ of one row. The gauge acts on a spinor by $\psi_j\mapsto t_j\psi_j$, up to the common factor $t_i$, which is its overall phase. The word at this level names the tuple and never an element of $A$; the carrier element is the elementary spinor of §*The Spinor Convention*, and the tuple is its coordinate form.

**Glyphs of the invertibles.**

| Unit | Glyph |
|---|---|
| Diagonal unit | The idempotent, $\Pi_{\mathrm{id},i}$ |
| Off-diagonal unit, abstract algebra | The nilpotent glyph, $\tilde\Pi_{\mathrm{nil},ij}$ in the quaternionic layers and $\Pi_{\mathrm{nil},ij}$ in the tilde-free ones, with the arrow instead of the tilde when pure |
| Off-diagonal unit, in $M_n$ | The matrix unit, $E_{ij}$, 1-based |
| Several units in one component | Counting subscript, $\tilde\Pi_{\mathrm{nil},ij,1},\dots,\tilde\Pi_{\mathrm{nil},ij,m}$ |

$E_{ij}$ is written only when the objects are matrices. In an abstract algebra the generic letter $E$ is not used.

**What is not a Peirce notion.** A root of unity, an eigenvalue, a grading, a weight, a Cartan subalgebra. A root may produce a family, through its Lagrange idempotents; the family is then a Peirce family like any other, and the root adds nothing to the Peirce vocabulary. Nor is a chirality a Peirce notion: the chirality of an operator is the side on which it multiplies (*Operator Family Conventions*, §*The Slot Label, Which Is the Chirality*); the Peirce sign of the third axis, $iR_{\vec e_z}$, is minus the chirality operator of the frame, a coincidence of arrays at that one root and not an identity of notions (*Operator Chirality on the Biquaternion Algebra*, §*What Operator Chirality Is Not*). Neither is an ordered or nested reading of the family: an order on the indices, a sequence of cuts, a cumulative sum of the members. When an article reads the family step by step, it says so there, and the reading is called there what it is.

**Excluded vocabulary.** Left ideal, right ideal, minimal left ideal, carrier, module and representation are not used at the levels of the family and of the decomposition, and are not used to define a spinor here; the one place where a spinor is defined through an ideal is §*The Spinor Convention*, and it says so. A sum $\bigoplus_jA_{ij}$ or $\bigoplus_iA_{ij}$ is a **row** or a **column** of the Peirce table, never a component and never a carrier. If another article needs an ideal, it names it there, under its own name, with an explicit pointer.

**Symbols.**

| Symbol | Meaning |
|---|---|
| $\Pi_{\mathrm{id},i}$ | A member of the complete orthogonal family |
| $A_{ij}$ | A Peirce component, left index first |
| $\tilde\Pi_{\mathrm{nil},ij}$, $\Pi_{\mathrm{nil},ij}$ | An off-diagonal Peirce unit, a nilpotent; the tilde in the quaternionic layers, the plain capital in the tilde-free ones |
| $E_{ij}$ | A matrix unit, only in $M_n$ |
| $Q_{ij}$, $\psi_j$ | A Peirce coordinate, and the entry of a spinor |
| $Ζ$ | A root of unity, by the case rule |

**The summary sentence.** The family gives the components, the decomposition is canonical, the basis is chosen, the gauge is its freedom, and the spinor is a tuple of coordinates in that basis.

### The Biquaternion Peirce Convention

**Introduction.** The general Peirce convention read in the biquaternion algebra $\mathbb{B}$. It adds nothing to the family and fixes nothing about it; it fixes only the glyphs and the case rule of the layer.

**Scope.** $A=\mathbb{B}$, with unit $e_t$. The upper-case tilde is written in this layer, and a pure element carries the arrow and no tilde. Indices are numeric, 1-based. The four levels of §*The General Peirce Convention* are used, and no others.

**The family.** A complete, orthogonal and idempotent family $\tilde\Pi_{\mathrm{id},1},\tilde\Pi_{\mathrm{id},2}$ in $\mathbb{B}$. The family is arbitrary: this convention fixes no pair, and no pair is preferred. The canonical frame of the matrix model is written in the standard pair and its mixed units, $\tilde\Pi_{\mathrm{id},\pm}=\tfrac12(e_t\pm i\vec e_z)$ and $\vec\Pi_{\mathrm{nil},\pm}=\tfrac12(i\vec e_x\pm\vec e_y)$; that is a choice of frame, owned by *Matrix Representations Conventions*, §*The Matrix Models*, and it fixes nothing here. The glyph is governed by §*The Idempotent Convention*.

**The decomposition.**

$$
\mathbb{B}=A_{11}\oplus A_{12}\oplus A_{21}\oplus A_{22},\qquad A_{ij}=\tilde\Pi_{\mathrm{id},i}\mathbb{B}\tilde\Pi_{\mathrm{id},j} .
$$

The left index is written first. The summands are Peirce components and the array is the Peirce table. The components multiply by the rule: the second index of the first factor must equal the first index of the second, otherwise the product is zero. So $A_{ij}A_{jq}\subseteq A_{iq}$, and $A_{ij}A_{pq}=0$ when $j\ne p$. The decomposition is canonical: it depends on the family and on nothing else.

**The basis and the gauge.** The diagonal units are the idempotents themselves,

$$
\tilde\Pi_{\mathrm{id},1}\in A_{11},\qquad \tilde\Pi_{\mathrm{id},2}\in A_{22},
$$

and the mixed units carry the nilpotent glyph, with the arrow where the element is pure,

$$
\tilde\Pi_{\mathrm{nil},12}\in A_{12},\qquad \tilde\Pi_{\mathrm{nil},21}\in A_{21}.
$$

A Peirce basis is a choice of these two units, and every statement using it says so. The gauge is

$$
\tilde\Pi_{\mathrm{nil},ij}\longmapsto t_it_j^{-1}\tilde\Pi_{\mathrm{nil},ij},\qquad t_1,t_2\ne0,
$$

which leaves the family, the components and the products fixed. With a star, $\lvert t_i\rvert=1$ and the gauge is a torus of phases.

**Coordinates and spinors.** An element is

$$
\tilde Q=\tilde Q_{11}\tilde\Pi_{\mathrm{id},1+}\tilde Q_{12}\tilde\Pi_{\mathrm{nil},12}+\tilde Q_{21}\tilde\Pi_{\mathrm{nil},21}+\tilde Q_{22}\tilde\Pi_{\mathrm{id},2},
$$

and the four complex numbers $\tilde Q_{ij}$ are its Peirce coordinates, carrying the glyph of the element, indexed by the left index first. A spinor is a pair of coordinates in one row:

$$
\psi_1=(\tilde Q_{11},\tilde Q_{12}),\qquad \psi_2=(\tilde Q_{21},\tilde Q_{22}).
$$

The gauge acts on a spinor by $\psi_j\mapsto t_j\psi_j$, up to the common factor $t_i$ of the row, which is its overall phase. The word spinor belongs to this level only.

**Glyphs of the invertibles.**

| Unit | Glyph |
|---|---|
| Diagonal, $A_{11}$, $A_{22}$ | $\tilde\Pi_{\mathrm{id},1}$, $\tilde\Pi_{\mathrm{id},2}$ |
| Mixed, $A_{12}$, $A_{21}$ | $\tilde\Pi_{\mathrm{nil},12}$, $\tilde\Pi_{\mathrm{nil},21}$, with the arrow where pure |
| Several units in one line | Counting subscript, $\tilde\Pi_{\mathrm{nil},12,1},\dots$ |
| Quaternion or split-quaternion layer | $\tilde\pi_{\mathrm{id},1},\tilde\pi_{\mathrm{id},2}$ and $\tilde\pi_{\mathrm{nil},12},\tilde\pi_{\mathrm{nil},21}$ |
| Complex, split-complex or dual layer | $\Pi_{\mathrm{id},1},\Pi_{\mathrm{id},2}$ and $\Pi_{\mathrm{nil},12},\Pi_{\mathrm{nil},21}$, with no tilde |
| Matrix model of $\mathbb{B}$ | $E_{ij}$, 1-based, only there |

No generic $E$ is written outside the matrix model, and no tilde on a pure element.

**Symbols.**

| Symbol | Meaning |
|---|---|
| $\tilde\Pi_{\mathrm{id},1}$, $\tilde\Pi_{\mathrm{id},2}$ | The complete orthogonal pair |
| $A_{ij}$ | A Peirce component, left index first |
| $\tilde\Pi_{\mathrm{nil},12}$, $\tilde\Pi_{\mathrm{nil},21}$ | The mixed Peirce units, nilpotents |
| $E_{ij}$ | A matrix unit, only in the matrix model |
| $\tilde Q_{ij}$, $\psi_j$ | A Peirce coordinate, and the entry of a spinor |
| $t_1$, $t_2$ | The gauge parameters |

**The summary sentence.** The family gives the four components, the decomposition is canonical, the two mixed units are chosen, the gauge is their freedom, and the spinor is a pair of coordinates in one row.

## The Spin and Spinor Convention

**Three words.** A **spin** is a scalar label of a carrier; an **elementary spinor** is an element of a carrier; a **Dirac spinor** is an element of $\mathbb{B}$ read as a pair of elementary spinors. The three words are fixed here, as names with their glyphs. The theorems that produce the carriers, that fix the weights and the dimension, and that separate the two parts are *From the Spin to the Carriers and the Closures* and *Spinors and Dirac Spinors in the Biquaternion Algebra*.

### The Spin Convention

**The definition.** Let $(W,\rho)$ be an irreducible unitary carrier of the rotation algebra generated by $\tilde S_k=\tfrac12 i\vec e_k$. For an invertible element $\vec u$ the operator $\rho(\vec u\cdot\vec S)$ is self-adjoint and its spectrum does not depend on $\vec u$. The **spin** of the carrier is its largest eigenvalue,
$$
s=\max\operatorname{spec}\bigl(\rho(\vec u\cdot\vec S)\bigr)\in\tfrac12\mathbb{Z}_{\ge0},
$$
a scalar label and not a vector. The generator is $\tilde S_k$, the label $s$, the projection $s_z$; a total of several parts carries the role subscript $s_{\mathrm{tot}}$ (*Index and Notation Conventions*, §*The Subscripts*).

**The group.** The rotation algebra is the Lie algebra of the **rotor group** $S^3=\mathrm{Spin}(3)$, the unit quaternions under quaternion multiplication. Its elements are the rotors. A rotor acts on space by the two-sided product $v\mapsto RvR^{-1}$, which is the spatial rotation, and on a carrier by the one-sided product $\psi\mapsto R\psi$, which is the spin action; the two actions use one rotor and are not the same representation. As groups $S^3=\mathrm{Spin}(3)\cong SU(2)$, and $SU(2)$ is the name of the standard $2\times2$ complex display, which is a choice of display and not a second group. **Every spin of the biquaternion layer is the label of a carrier of this group**: spin is the rotor action read on a carrier, and the rotor action is the quaternion product. The general case, where the rotor group of $\mathbb{R}^n$ is the larger $\mathrm{Spin}(n)$, is *Spin Geometry* of the Geometry part; the quaternion name and the $SU(2)$ name belong to $n=3$.

**The two carriers of $\mathbb{B}$.** The minimal left ideals are
$$
S_\pm(\vec u)=\mathbb{B}\tilde\Pi_{\mathrm{id},\pm}(\vec u),\qquad \tilde\Pi_{\mathrm{id},\pm}(\vec u)=\tfrac12\bigl(e_t\pm i\vec u\bigr),
$$
for a unit real vector $\vec u$; each is a complex two-dimensional space on which the left multiplications act irreducibly, and $\vec u\mapsto S_+(\vec u)$ is a bijection from the unit sphere onto the minimal left ideals. Each carries spin $\tfrac12$, Casimir $\tfrac34$ and dimension $2s+1=2$. The idempotents are the sign pair $\tilde\Pi_{\mathrm{id},\pm}$ of §*The Idempotent Convention* at the declared axis.

### The Spinor Convention

**Definition (elementary spinor).** An **elementary spinor** is an element of a complex two-dimensional space on which the left multiplications act irreducibly with weights $+\tfrac12$ and $-\tfrac12$, so that a rotation through $\theta$ about $\vec u$ multiplies it by $e^{-i\theta\vec u\cdot\vec S}$. In $\mathbb{B}$ such a space is a minimal left ideal $S_+(\vec u)$ or $S_-(\vec u)$, and the axis $\vec u$ is part of the datum.

**The coordinates.** An element of $S_+(\vec u)$ is $d_0\tilde\Pi_{\mathrm{id},+}(\vec u)+d_1\vec\pi_{\mathrm{nil}}(\vec u)$ with $d_0,d_1\in\mathbb{C}$ and $\vec\pi_{\mathrm{nil}}$ the companion nilpotent, so an elementary spinor is a pair $(d_0;d_1)$. A column of two components is that pair written in a chosen carrier and is not a second definition; the tuple of Peirce coordinates is its form at the array level, §*The General Peirce Convention*.

**Definition (Dirac spinor).** A **Dirac spinor** is an element $\tilde\Psi=\tilde\Psi_L+\tilde\Psi_R$ of $\mathbb{B}$, the two parts being its two components in the decomposition of $\mathbb{B}$ into minimal left ideals,
$$
\mathbb{B}=S_+(\vec u)\oplus S_-(\vec u),\qquad \tilde\Pi_{\mathrm{id},\pm}(\vec u)=\tfrac12\bigl(e_t\pm i\vec u\bigr),
$$
for a declared unit imaginary direction $\vec u$, and each part is an elementary spinor of complex dimension two.

**The two parts carry the chirality letters.** The decomposition is a decomposition into the two values of the chirality: the basis operator $-iR_{\vec u}$ is $-1$ on $S_+(\vec u)$ and $+1$ on $S_-(\vec u)$, so $\tilde\Psi_L\in S_+(\vec u)$ is the $L$ part and $\tilde\Psi_R\in S_-(\vec u)$ the $R$ part, in the letters of §*The Slot Label, Which Is the Chirality* of *Operator Family Conventions*. At $\vec u=\vec e_z$ the basis operator is $\mathsf{V}_{\mathrm{vol}}$. Exchanging the two letters is the substitution $\vec u\mapsto-\vec u$, because $\tilde\Pi_{\mathrm{id},+}(\vec u)=\tilde\Pi_{\mathrm{id},-}(-\vec u)$; the pair is unordered and the definition orders it only to name the parts.

**What the three words do not name.** No Clifford relation, no gamma basis operator, no Pauli array, no volume element and no second rotation triple. The elementary spinor names the axis that selects its carrier, the Dirac spinor names one axis and nothing else, and a change of axis changes the decomposition and nothing beside it.
## Summary

A **root** is an element with $\tilde{Ζ}^2=1$, or $\tilde{Ζ}^2=\lambda e_t$ for a central value $\lambda$, the square read in a named product. An **idempotent** is an element with $\tilde\Pi_{\mathrm{id}}^2=\tilde\Pi_{\mathrm{id}}$, and the rank-one Hermitian ones of $\mathbb{B}_{\Psi}$ are the **pure states**. A **nilpotent** is an element whose square vanishes. Each glyph is split by the case rule, layer by layer, and the subscript counts when it distinguishes and names when it is a role. The **Peirce convention** fixes four levels — family, components, multiplication rule and array — the left index first, $A_{ij}A_{jq}\subseteq A_{iq}$. A **spin** is a scalar in $\tfrac12\mathbb{Z}_{\ge0}$, the carriers of $\mathbb{B}$ are the minimal left ideals $S_\pm(\vec u)$ of spin $\tfrac12$, and an element of one is an **elementary spinor**.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Ζ$, $\tilde\zeta$, $\tilde{Ζ}$ | A root of $1$ in the tilde-free, quaternion and biquaternion layers |
| $Ζ_\pm$ | A root of $1$ of the reduced biquaternion layer, the two signs |
| $\Pi_{\mathrm{id}}$, $\tilde\pi_{\mathrm{id}}$, $\tilde\Pi_{\mathrm{id}}$ | An idempotent in the tilde-free, quaternion and biquaternion layers; $\tilde\Pi_{\mathrm{id}}$ also the pure state and the left ideal $\mathbb{B}\tilde\Pi_{\mathrm{id}}$ |
| $\Pi_{\mathrm{id},\pm}$ | The two members of a complete sign pair of idempotents |
| $\Pi_{\mathrm{nil}}$, $\tilde\Pi_{\mathrm{nil}}$, $\tilde\pi_{\mathrm{nil}}$ | A nilpotent of the tilde-free layers with the plain capital, of the biquaternion and split-biquaternion layers with the tilde, and of the quaternion layers in the lower case |
| $\vec{Ζ}$, $\vec\pi_{\mathrm{nil}}$, $\vec\Pi_{\mathrm{nil}}$ | A pure root and a pure nilpotent |
| $\tilde\Pi_{\mathrm{id},1},\dots,\tilde\Pi_{\mathrm{id},n}$ | A complete, orthogonal and idempotent family |
| $A_{ij}=\tilde\Pi_{\mathrm{id},i}\mathbb{B}\tilde\Pi_{\mathrm{id},j}$ | A Peirce component; the left index first |
| $A_{ij}A_{jq}\subseteq A_{iq}$ | The multiplication rule of the components |
| $\tilde S_k=\tfrac12 i\vec e_k$ | The generator of the rotation algebra |
| $\vec S$ | The generator read as one vector, $\vec u\cdot\vec S=u_k\tilde S_k$; pure, so arrowed and without the tilde |
| $s$, $s_z$, $s_{\mathrm{tot}}$ | The spin, its projection and the total of several parts |
| $S_\pm(\vec u)=\mathbb{B}\tilde\Pi_{\mathrm{id},\pm}(\vec u)$ | The two carriers, minimal left ideals of complex dimension two |
| $\tilde\Pi_{\mathrm{id},\pm}(\vec u)=\tfrac12(e_t\pm i\vec u)$ | The idempotents of the two carriers, at the declared axis $\vec u$ |
| $\tilde\Psi$, $\tilde\Psi_L$, $\tilde\Psi_R$ | A Dirac spinor and its two parts, the $L$ part in $S_+$ and the $R$ part in $S_-$ |

## Further Reading

- Benjamin Peirce, "Linear Associative Algebra", *American Journal of Mathematics* **4** (1881) 97–229. The original Peirce decomposition, from which the components and the multiplication rule of §*The General Peirce Convention* take their name.
- Soo-Chang Pei, Ja-Han Chang and Jian-Jiun Ding, "Commutative reduced biquaternions and their Fourier transform for signal and image processing applications", *IEEE Transactions on Signal Processing* **52** (2004) 2012–2022. The reduced biquaternion algebra of the engineering literature, its idempotent decomposition, its ring-valued norm and its transform.
- [From the Spin to the Carriers and the Closures](the-carriers-the-representation-the-spin-and-the-closure.html). The rotation algebra, the criterion, the quadratic element, the definition of spin and the classification of the carriers.
- [Spinors and Dirac Spinors in the Biquaternion Algebra](spinors-and-dirac-spinors-in-the-biquaternion-algebra.html). The two definitions, the weights, the dimension and the multiplicity of the two parts.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998). Algebras with involution, the first and the second kind, and the classification of their involutions.
