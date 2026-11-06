# __Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form__

## Introduction

A mass term is the only term of a field equation that carries no derivative, and that single fact fixes its algebraic shape. Every other term pairs the field with a gradient; a term with no derivative has nothing to differentiate, so it must pair the field with *another field* — and since a free equation is written in terms of one field, that other field must be a **conjugate** of it. The only freedom left is *which* conjugate. That choice is not cosmetic. It is what separates the two kinds of mass, and it is why the words "mass" and "conjugation" belong in the same sentence.

The framework carries several conjugations, and they are easy to conflate because two of them are antilinear and both are called a real structure: the algebra's $\flat$ and the **charge conjugation** $\mathcal{C}$ that acts on the module $\Delta$. This article separates them and settles what each is for. Its claims:

- **Established, and recomputed below.** The biquaternion algebra carries three antilinear involutions — complex conjugation $\bar{\cdot}$, Hermitian conjugation ${}^{*}=\overline{\cdot^{\natural}}$, and the anti-Hermitian conjugation $\flat=-{}^{*}$ — alongside the *linear* quaternion conjugation ${}^{\natural}$. Their fixed spaces are four distinct subspaces, of real dimensions $2, 4, 4$ and $4$, and only the last two of them are the framework's sectors. In particular the one involution that is **linear**, quaternion conjugation, is the one whose fixed space is *not* a sector.
- **Established, and recomputed below.** The **Dirac mass** is linear and couples the two values of the subscript, $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = \lambda_m^{-1}\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = \lambda_m^{-1}\tilde{Ξ}_{\mathrm{sp},R}$; it pairs no field with its own conjugate. The **Majorana mass** is antilinear and pairs a field with its own conjugate, and it is physical: its reality condition has a four-real-dimensional solution space and it preserves the mass shell $p^2 = m^2$.
- **Established, and recomputed below.** The retired single-field equation $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp}} = \lambda_m^{-1}\tilde{Ξ}_{\mathrm{sp}}^{\flat}$ fails, and it fails **on the dispersion**: its central-phase plane waves have nullity $0$ on the timelike shell and nullity $4$ on the spacelike shell, so its solutions lie on the spacelike locus. This is reproduced here on the eight real coordinates, by pure real arithmetic.
- **The distinction the whole article turns on.** The diagnosis of that failure is the *pairing*, not the antilinearity. A Majorana mass is also antilinear and is perfectly physical. What the retired equation did was use the **algebra's** real structure $\flat$ as though it were the mass of a field on the **module** — and the two are different real structures on different spaces.
- **Gap, left visible.** The framework does not derive the values of either mass, and it does not decide which kind a given fermion carries; that is empirical input, as the neutrino companion states. What the framework supplies is the algebraic distinction and the reality structure each kind is built on. Here $\lambda_m=\hbar/(mc)$ is the mass length.

The article is organised as follows. A section fixes what antilinear means in this algebra and tabulates the involutions. A section gives the argument that a mass is a pairing with a conjugate. A section distinguishes the two conjugates and the two masses. A section separates the two real structures, on the algebra and on the module, which is where the retired equation went wrong, and fixes the four levels at which the name "charge conjugation" is used. A section places charge conjugation in its group-theoretic setting, the $\mathrm{Spin}^c$ structure, and reads off which fields can carry the algebra's central $\mathrm{U}(1)$. A section exhibits the dispersion failure in full, for the retired equation and for all four involutions. A section records what the antilinear structure is genuinely for. A closing section, *The Legacy Pauli Gamma Formulation*, is the dictionary: it is the only place in the article where the gammas appear, because they are a frame of the cell algebra and not a separate structure.

## What Antilinear Means Here

The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$, $\vec e_k^2 = -e_t$, and a scalar imaginary $i$ commuting with every unit, $i^2 = -1$. That relation is used all through the article: every sign produced by two imaginary factors is $i^2 = -1$ read once. An element is a sum with complex coefficients,

$$
\tilde{Q} = (a_0 + i b_0)e_t + (a_1 + i b_1)\vec e_x + (a_2 + i b_2)\vec e_y + (a_3 + i b_3)\vec e_z , \qquad a_\mu, b_\mu \in \mathbb{R},
$$

so $\mathbb{B}$ has real dimension $8$ and complex dimension $4$.

Two involutions generate the rest.

**Quaternion conjugation** reverses the vector part and fixes the centre:

$$
\tilde{Q}^{\natural} = (a_0 + ib_0)e_t - (a_1 + ib_1)\vec e_x - (a_2 + ib_2)\vec e_y - (a_3 + ib_3)\vec e_z .
$$

It is $\mathbb{C}$-**linear**, because it fixes $i$, and it is an anti-automorphism, $(\tilde{Q}_2\tilde{Q}_1)^{\natural} = \tilde{Q}_1^{\natural}\,\tilde{Q}_2^{\natural}$.

**Complex conjugation** negates the scalar imaginary and fixes the units:

$$
\bar{\tilde{Q}} = (a_0 - ib_0)e_t + (a_1 - ib_1)\vec e_x + (a_2 - ib_2)\vec e_y + (a_3 - ib_3)\vec e_z .
$$

It is $\mathbb{C}$-**antilinear**, $\overline{\alpha\tilde{Q}} = \bar{\alpha}\,\bar{\tilde{Q}}$ for every $\alpha\in\mathbb{C}$, and it is an automorphism, $\overline{(\tilde{Q}_2\tilde{Q}_1)} = \bar{\tilde{Q}_2}\,\bar{\tilde{Q}_1}$.

Composing them gives the two Hermitian conjugations of the series. Because one factor is linear and the other antilinear, each composite is antilinear:

$$
\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}} = \big(\bar{\tilde{Q}}\big)^{\natural} , \qquad
\tilde{Q}^\flat = -\tilde{Q}^{*} .
$$

Both are anti-automorphisms; the second carries a sign, $(\tilde{Q}_2\tilde{Q}_1)^\flat = -\tilde{Q}_1^\flat\tilde{Q}_2^\flat$, and that sign is its only departure from an ordinary anti-automorphism. The two differ by the central sign alone, and that sign is what moves the fixed space from one sector to the other. On the two central generators the values are read at once: $e_t^{*} = e_t$ and $i^{*} = -i$, hence $e_t^{\flat} = -e_t$ and $i^{\flat} = +i$. The sign of $\flat$ sits on the real unit, not on the imaginary one.

| involution | action on generators | $\mathbb{C}$-linearity | character | fixed space |
|---|---|---|---|---|
| $\tilde{Q}^{\natural}$ | $e_t \mapsto e_t$, $\vec e_k \mapsto -\vec e_k$, $i \mapsto i$ | linear | anti-automorphism | $\mathbb{B}_{C} = \{Q_te_t\}$ (centre), real dim $2$ |
| $\bar{\tilde{Q}}$ | $e_t \mapsto e_t$, $\vec e_k \mapsto \vec e_k$, $i \mapsto -i$ | antilinear | automorphism | $\mathbb{B}_{H}$, real dim $4$ |
| $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$ | $e_t \mapsto e_t$, $\vec e_k \mapsto -\vec e_k$, $i \mapsto -i$ | antilinear | anti-automorphism | $\mathbb{B}_{\Psi}$, real dim $4$ |
| $\tilde{Q}^{\flat} = -\tilde{Q}^{*}$ | $e_t \mapsto -e_t$, $\vec e_k \mapsto \vec e_k$, $i \mapsto i$ | antilinear | anti-automorphism with twist | $\mathbb{B}_{\Phi}$, real dim $4$ |

The last row is the one the rest of the article uses, and its entry on the generators needs reading with care: the minus in $\flat=-{}^{*}$ cancels the signs that ${}^{*}$ puts on the spatial units and on $i$, so on the units $\flat$ does nothing but negate the real one. On an element it negates the real scalar part and the imaginary vector parts, and keeps the real vector part and the imaginary scalar part, so its fixed space is the $a_k\vec e_k + ib_0e_t$ of the material sector — a real spatial vector and an imaginary scalar, the shape of the four-potential.

Four involutions, four distinct fixed spaces, of real dimensions $2, 4, 4, 4$. The two sectors of the framework are the last two rows, and they are the fixed spaces of *antilinear* maps. The real-quaternion sector $\mathbb{B}_{H}$ is the fixed space of the other antilinear involution, and the centre is the fixed space of the one linear involution. The last two rows are the only pair that is not independent: they differ by the central sign alone, $\flat=-{}^{*}$, and that sign is exactly what moves the fixed space from $\mathbb{B}_{\Psi}$ to $\mathbb{B}_{\Phi}$. The first two rows are different maps, acting differently on the generators. The fixed spaces, not the signs, are what the framework builds on.

On the two sectors $\flat$ acts by a sign, and this is the fact the rest of the article uses:

$$
\tilde{Ξ}_{\mathrm{sp}}^{\flat} = +\tilde{Ξ}_{\mathrm{sp}}\ \ (\tilde{Ξ}_{\mathrm{sp}}\in\mathbb{B}_{\Phi}), \qquad
\tilde{Ξ}_{\mathrm{sp}}^{\flat} = -\tilde{Ξ}_{\mathrm{sp}}\ \ (\tilde{Ξ}_{\mathrm{sp}}\in\mathbb{B}_{\Psi}).
$$

$\mathbb{B}_{\Psi}$ is the Hermitian sector and $\mathbb{B}_{\Phi}$ the anti-Hermitian one, and $\mathbb{B}_{\Phi} = i\,\mathbb{B}_{\Psi}$: multiplication by the central $i$ carries one sector onto the other, because $(i\tilde{Q})^{*} = \bar{i}\,\tilde{Q}^{*} = i^2\tilde{Q}^{*} = -i\tilde{Q}^{*}$. That is a *linear* map between the sectors, and it is not a map of either into itself, since $i\,\mathbb{B}_{\Phi}=\mathbb{B}_{\Psi}$. The antilinear map $\flat$ does not move them: it fixes one and negates the other, and the sign it carries is the same $i^2=-1$, read where the central unit meets the conjugation.

## Why a Mass Is a Pairing with a Conjugate

The argument is short and it is the reason the two topics of this article are one topic.

Write the free equation of a field as

$$
\mathcal{D}\tilde{Ξ}_{\mathrm{sp}} = \text{(mass term)},
$$

where $\mathcal{D}$ is first order and carries the gradient. The mass term is defined as the part of the equation that survives when every derivative is dropped. Being non-derivative, it cannot pair the field with $\partial/\partial R_\mu\tilde{Ξ}_{\mathrm{sp}}$; being bilinear and built from a single field, it must pair $\tilde{Ξ}_{\mathrm{sp}}$ with something constructed from $\tilde{Ξ}_{\mathrm{sp}}$ itself. The only constructions available that do not reintroduce a derivative are the involutions of the previous section.

So a mass term has the shape

$$
\text{mass} \;\sim\; \tilde{Ξ}_{\mathrm{sp}}^{\bullet}\,\tilde{Ξ}_{\mathrm{sp}} \quad\text{or}\quad \tilde{Ξ}_{\mathrm{sp}}\,\tilde{Ξ}_{\mathrm{sp}}^{\bullet},
$$

with $\bullet$ one of ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$, $\flat$. The involutions are not interchangeable — they have different fixed spaces — so **each choice of involution is a different kind of mass**. That is the whole content of the phrase "the two kinds of mass": the kinds are indexed by the conjugation, or by its absence, and not by a numerical value. One qualification matters for the count: $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ are the fixed spaces of two maps that differ only by the central sign, so their pairings are sign variants of one another and admit the same momenta, as the dispersion table below confirms. Up to that sign there are three distinct choices, not four.

Two kinds are realised in physics. One of them is not in the list at all, because it needs no involution; the other is the last entry, the conjugation.

**The pairing of the two values gives the Dirac mass.** It pairs the two values of the subscript rather than a conjugate, $\tilde{Ξ}_{\mathrm{sp},L}$ with $\tilde{Ξ}_{\mathrm{sp},R}$, two independent parts of one field. It is linear, and it is the mass term of the Dirac equation.

**The conjugation choice gives the Majorana mass.** The pairing that uses the field's own conjugate, $\tilde{Ξ}_{\mathrm{sp}}$ with $\tilde{Ξ}_{\mathrm{sp}}^{\bullet}$, requires the field to *equal* its conjugate — a **reality condition** that halves the field's independent components. The map that produces that conjugate is antilinear, and the term it builds is the mass term of a Majorana fermion.

The distinction is visible in the component count before any dynamics is imposed, and the count is decisive. The field is an element of $\mathbb{B}$, of real dimension $8$: four complex components. An antilinear involution of the algebra has a fixed space of real dimension $4$ — half, because multiplication by $i$ exchanges its $+1$ and $-1$ eigenspaces, so the two have equal dimension. So

$$
\boxed{\;\text{Dirac field}: 8 \text{ real components}, \qquad
\text{Majorana field}: 4 \text{ real components}\;},
$$

and the Majorana field is the fixed space of that pairing: a carrier of half the size, singled out by an antilinear structure and not by a linear constraint bolted onto a Dirac field.

The framework's module is $\Delta = S\oplus\bar{S}$, the two parts, of complex dimension $4$ and real dimension $8$. Its charge conjugation is the conjugate-linear map $\mathcal{C}$ satisfying $\mathcal{C}^2 = 1$ that exchanges the two halves; its fixed space is the Majorana space, of real dimension four. The companion on the neutrino and Majorana fermions constructs that map and computes its consequences; the present article is concerned with the algebra-side counterpart, and with keeping the two apart.

## The Two Conjugates and the Two Masses

The two mass terms of a single fermion species, written on the field $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$ of $\mathbb{B}$ and on its charge conjugate $\tilde{Ξ}_{\mathrm{sp}}^c$, are

$$
\mathcal{L}_{\text{Dirac}} = -m_D\,\mathrm{Sc}\big(\tilde{Ξ}_{\mathrm{sp}}^*\,i\,\tilde{Ξ}_{\mathrm{sp}}\,\vec e_x\big) ,
$$

where the unit multiplies on the right: the value of an element is what the subscript $L$ or $R$ reads, and right multiplication by $\vec e_x$ reverses it, because $\vec e_x$ anticommutes with the $\vec e_z$ that defines the value, so the term pairs each part with the other and never a part with itself.

$$
\boxed{\;\mathcal{L}_{\text{Majorana}} = -\tfrac12 m_M\,\mathrm{Sc}\big(\tilde{Ξ}_{\mathrm{sp},L}\,\vec e_x\,\tilde{Ξ}_{\mathrm{sp},L}\big) + \text{h.c.}\;}
$$

The bracket carries no sign of conjugation: the part stands in both slots, and the only structure between them is the unit on the right. That is the transposed realization of the operation, and the multiplier squares to minus the identity, because $\vec e_x^{2}=-e_t$:

$$
\eta(\tilde X)=\tilde X\vec e_x ,
\qquad
\eta^{2}(\tilde X)=\tilde X\vec e_x^{2}=-\tilde X ,
$$

so the multiplier carries the division-ring sign that the companion article records, and the bracket is a transposition pairing rather than a scalar product — which is why the term needs its h.c. to be real. The untransposed realization is the operation on the field that produces the conjugate, and it squares to $+1$:

$$
\mathcal{C}[\tilde{Ξ}_{\mathrm{sp}}]=-\vec e_y\tilde{Ξ}_{\mathrm{sp}}^*\vec e_y ,
\qquad
\mathcal{C}\big(\mathcal{C}[\tilde{Ξ}_{\mathrm{sp}}]\big)=\tilde{Ξ}_{\mathrm{sp}} ,
$$

the second line because $\vec e_y^{*}=-\vec e_y$ and $\vec e_y^{2}=-e_t$, so the two conjugations and the two units cancel in pairs. The section *Two Real Structures, on Two Different Spaces* keeps the operation apart from the algebra's $\flat$.

The first pairs $\tilde{Ξ}_{\mathrm{sp},L}$ with $\tilde{Ξ}_{\mathrm{sp},R}$ and is **linear**; it conserves fermion number and is invariant under the continuous phase $\tilde{Ξ}_{\mathrm{sp}}\mapsto \exp(i\alpha)\tilde{Ξ}_{\mathrm{sp}}$. The second pairs $\tilde{Ξ}_{\mathrm{sp},L}$ with its charge conjugate $\tilde{Ξ}_{\mathrm{sp},L}^c$, a field produced from $\tilde{Ξ}_{\mathrm{sp},L}$ by the antilinear map $\mathcal{C}$; it changes fermion number by two units, and it is not invariant under the continuous phase — which is exactly why it can be written only for a field that is not protected by a conserved charge.

| | Dirac mass | Majorana mass |
|---|---|---|
| pairs | $\tilde{Ξ}_{\mathrm{sp},L}$ with $\tilde{Ξ}_{\mathrm{sp},R}$ | $\tilde{Ξ}_{\mathrm{sp}}$ with $\tilde{Ξ}_{\mathrm{sp}}^c$ |
| the map it is built on | the identity, linear | charge conjugation $\mathcal{C}$, antilinear |
| fermion number | conserved | violated by $2$ |
| continuous phase | invariant | not invariant |
| needs a reality condition | no | yes, $\tilde{Ξ}_{\mathrm{sp}}^c=\tilde{Ξ}_{\mathrm{sp}}$ |
| independent real components | $8$ | $4$ |
| framework structure | the two values of the subscript | an antilinear real structure |

Both are masses; neither is a mistake. The two columns of the table are what the phrase "two kinds of mass" names, and the reason they are both called a mass is that both are non-derivative bilinears — the argument of the previous section.

In biquaternionic form the Dirac mass is the linear pair of the parent article. It is **two equations, one per value of the subscript**, and not one equation with two halves:

$$
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = \lambda_m^{-1}\tilde{Ξ}_{\mathrm{sp},L} ,
$$

$$
\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = \lambda_m^{-1}\tilde{Ξ}_{\mathrm{sp},R} .
$$

The first acts on the right-handed half, the second on the left-handed one, and the second is the quaternion conjugate of the first. The massless case is $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp}} = 0$, which is the right-handed member alone; the full massless field is the pair, not either member.

**The two-sided reading.** The pair is also the corpus's two-sided structure. For a scalar mass the siding is invisible — $\lambda_m^{-1}$ is central, so $\lambda_m^{-1}\tilde{Ξ}_{\mathrm{sp},L}=\tilde{Ξ}_{\mathrm{sp},L}\lambda_m^{-1}$ and the mass term may be read as a left or as a right multiplication — but the siding becomes visible as soon as the mass term carries a direction and a conjugation, which is exactly what the dictionary's form of the equation does. With $r'_t$ the imaginary time and $D_3=\sum_k\vec e_k\,\partial/\partial R_k$ the three-dimensional Cauchy–Riemann operator, Kravchenko's form of the equation on $F\in\mathbb{B}$ reads

$$
(i\partial/\partial r'_t + D_3)F - mi\,\bar{F}\,\vec e_z = 0 ,
$$

a left multiplication by the derivative, an antilinear coefficient conjugation $\bar{\cdot}$ with no side, and a right multiplication by the spatial unit $\vec e_z$. There the mass term is a right multiplication *followed by* a conjugation, and it is not a single cell. The two readings are related by the dictionary and are not the same equation — their mass terms are of different kinds, a scalar in one and a right multiplication with a conjugation in the other. What they share is the structural reason the second side is needed at all: the Dirac mass is what couples one value to the other, and left multiplication alone preserves the value.

Applying $\tilde{\nabla}$ from the left to the second member and substituting the first, with $\tilde{\nabla}\tilde{\nabla}^{\natural} = \Box$, gives the Klein–Gordon equation for each part,

$$
\Box\tilde{Ξ}_{\mathrm{sp},L} = \lambda_m^{-2}\tilde{Ξ}_{\mathrm{sp},L} ,
$$

and likewise for $\tilde{Ξ}_{\mathrm{sp},R}$ from the first member, so the pair sits on the physical mass shell. The order matters, and it is exactly what *one-sided* means: both gradients act from the left, $\tilde{\nabla}$ and then $\tilde{\nabla}^{\natural}$, so that their product is the scalar $\Box$ and the two members combine. This is the form every article in the series uses, and it is the sense in which the mass is off-diagonal in the value: it is a coupling *between* the two parts, not a conjugation of either.

### Why the Dirac Mass Is Not a Self-Pairing

That the mass must be a pairing with a conjugate does not make it a *self*-pairing, and the algebra forces the difference.

Left multiplication by an element of $\mathbb{B}$ leaves the value of the field alone: a product takes the letter of its right factor, and the left multiplier does not touch it. So no left multiplication, and no sum $a\tilde{Ξ}_{\mathrm{sp},L}+b\tilde{Ξ}_{\mathrm{sp},R}$ of them, carries one value into the other. A mass that couples the two values is therefore not a one-sided operation at all: it is the *pair* of equations displayed above, the derivative on one half and the other half on the right-hand side.

The corpus's two-sided form states the same thing in a single equation, and it shows what "two-sided" means concretely. Three different actions sit in one operator:

- the derivative acts from the **left**, by multiplying on that side;
- the coefficient conjugation $\bar{\cdot}$ acts on the field and has **no side**;
- the mass term ends in a multiplication on the **right** by the spatial unit $\vec e_z$.

Only the first two are needed for a self-pairing. The third is not decoration: in the two-sided form a conjugation does not stand alone, it is accompanied by a right multiplication by a spatial unit, the $\vec e_z$ of the display. A bare conjugation, with no side and no direction, is what the retired equation below attempts, and the attempt is exactly what fails there.

Two consequences follow, and they are the point of this section:

- the **Dirac mass** pairs two different fields, so it needs no involution of a single field and it is linear;
- the **conjugation** in a mass term need not be the algebra's real structure $\flat$. In the two-sided form it is $\bar{\cdot}$, the coefficient conjugation, which is an automorphism and fixes $\mathbb{B}_{H}$, not $\mathbb{B}_{\Phi}$.

So the phrase "the mass is a pairing with a conjugate" asks two questions — *which* conjugate, and *on which side* — and the Dirac and Majorana masses answer them differently. A single equation with a single field and a single mass term can realise the self-pairing. It cannot realise the pair of two values, which needs two independent parts and hence two equations, $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = \lambda_m^{-1}\tilde{Ξ}_{\mathrm{sp},L}$ and $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = \lambda_m^{-1}\tilde{Ξ}_{\mathrm{sp},R}$.

## Two Real Structures, on Two Different Spaces

This is the section on which the retired equation's diagnosis turns, and it separates two objects that the word "conjugation" hides.

The framework calls $\flat$ the algebra's **real structure**. The neutrino companion constructs charge conjugation $\mathcal{C}$ on the module $\Delta$ and calls it a real structure too. Both are antilinear, both are involutions, and both pair an object with its own conjugate. They are nevertheless **different maps on different spaces**, and neither may stand in for the other. The side of an action is carried by position and never by a mark: a two-sided action is written $a\tilde{Ξ}_{\mathrm{sp}} b$, and a field is written with its two parts, $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$. The two maps are then:

| | algebra real structure $\flat$ | module charge conjugation $\mathcal{C}$ |
|---|---|---|
| acts on | the algebra $\mathbb{B}$, real dim $8$ | the module $\Delta$, real dim $8$ |
| defined by | the generators: $e_t\mapsto -e_t$, $\vec e_k\mapsto \vec e_k$, $i\mapsto i$ | the conjugation by $\vec e_y$ composed with the field's star, $\mathcal{C}[\tilde{Ξ}_{\mathrm{sp}}]=-\vec e_y\tilde{Ξ}_{\mathrm{sp}}^*\vec e_y$, with $\mathcal{C}^{2}=+1$ |
| fixed space | $\mathbb{B}_{\Phi}$, the anti-Hermitian sector, real dim $4$ | the Majorana space, real dim $4$ |
| respected by the kinetic operator | **no** | **yes**; the CPT companion verifies on the free equation that $\mathcal{C}$ carries solutions to solutions |
| exchanges the two values | no — it preserves the $\mathbb{B}_{\Psi}/\mathbb{B}_{\Phi}$ split | yes, through the cell under it |
| role | the $\mathbb{B}_{\Psi}/\mathbb{B}_{\Phi}$ split, traces, bilinears | the Majorana reality condition |

The third row and the fourth row are the substance. The fixed spaces have the *same real dimension four*, which is why the two are so easy to identify — and why the identification is wrong. The neutrino companion tests it on the equation and reports the obstruction: **the Dirac operator does not preserve $\mathbb{B}_{\Phi}$.** The reason is one line of the twist in $\flat$. Because $\flat$ is an anti-automorphism with a sign, $(\vec e_k\tilde{Ξ}_{\mathrm{sp}})^\flat=-\tilde{Ξ}_{\mathrm{sp}}^{\flat}\vec e_k$; on the fixed space $\mathbb{B}_{\Phi}$ this is $-\tilde{Ξ}_{\mathrm{sp}}\vec e_k$, which equals $\vec e_k\tilde{Ξ}_{\mathrm{sp}}$ only when $\vec e_k$ anticommutes with $\tilde{Ξ}_{\mathrm{sp}}$. It does not in general: for $\tilde{Ξ}_{\mathrm{sp}}=ie_t$ one gets $\vec e_k\tilde{Ξ}_{\mathrm{sp}}=i\vec e_k$, which is Hermitian, hence in $\mathbb{B}_{\Psi}$. A reality condition that the kinetic operator does not respect cannot be imposed on a field: the constrained field would not stay constrained under time evolution. So $\mathbb{B}_{\Phi}$ is a perfectly good real form *of the algebra* — Lorentz-stable under the rotor action $\tilde{Q}\mapsto\tilde{U}\tilde{Q}\tilde{U}^{*}$ — and simultaneously not the Majorana reality condition *of the module*, despite the matching dimension count.

The moral is the one this article exists to record:

$$
\boxed{\ \text{the algebra's } \flat \text{ and the module's } \mathcal{C} \text{ are different real structures; the dimension count does not identify them.}\ }
$$

The algebras and the modules of this framework have parallel vocabularies — conjugation, real structure, sectors, chirality — and the parallel is not an identity. A statement about $\flat$ is a statement about the algebra; a reality condition on a fermion is a statement about the module. Moving between them requires a construction, not a substitution.

### The Four Levels of the Name

The word "charge conjugation" is used at four levels in the corpus, and the table below fixes which object each level names. The name itself is reserved for **level 3**, the operation on the module. The levels above it are structures of the pairing, and the level-1 map $\flat$ carries the *shape* of the pairing and not the operation.

| level | object | space | what it is |
|---|---|---|---|
| 1, the algebra | $\flat=-{}^{*}$ | $\mathbb{B}$, real dim $8$ | the algebra's real structure, fixed space $\mathbb{B}_{\Phi}$; the **shape** of a charge-conjugation pairing |
| 2, the operators | $F\mapsto\eta_C F^{\dagger}\eta_C^{-1}$ | $\operatorname{End}(\mathbb{B})$ | the charge-conjugation **pseudoautomorphism**: an antiautomorphism of the operator algebra, twisted by the inner conjugation by $\eta_C$; it acts on the slots of an operator and not on a field |
| 3, the field | $\mathcal{C}[\tilde{Ξ}_{\mathrm{sp}}]=-\vec e_y\tilde{Ξ}_{\mathrm{sp}}^*\vec e_y$ | $\Delta$ | **charge conjugation**; the particle–antiparticle operation, $\mathcal{C}^{2}=1$, built on the cell that exchanges the two values |
| 4, the module real structure | $\bar{\cdot}$ | $\Delta\cong S\oplus\bar{S}$ | the fixed-point real structure transported to the module; fixed points $\mathbb{B}_{H}$ |

The squares are where the signs live, and the two signs belong to two *realizations* of one operation. The corpus keeps the name $\eta$ for the transposed realization and $\mathcal{C}$ for the operation, and that is the naming used here. The **transposed** realization is the bilinear $\mathrm{Sc}\big(\tilde{Ξ}_{\mathrm{sp}}\,\vec e_x\,\tilde{Ξ}_{\mathrm{sp}}\big)$, read with the multiplier on the right; its square is read off in one line, using $\vec e_x^{2}=-e_t$:

$$
\eta(\tilde X)=\tilde X\vec e_x ,
\qquad
\eta^{2}(\tilde X)=\tilde X\vec e_x^{2}=-\tilde X .
$$

So the multiplier of the bilinear squares to minus the identity and is not itself an involution — that is the division-ring sign the companion article records. The **untransposed** realization is the operation, $\mathcal{C}[\tilde{Ξ}_{\mathrm{sp}}]=-\vec e_y\tilde{Ξ}_{\mathrm{sp}}^*\vec e_y$, with $\tilde{Ξ}_{\mathrm{sp}}^*$ the Hermitian conjugation read on the field, and its square takes the same relation twice:

$$
\mathcal{C}\big(\mathcal{C}[\tilde{Ξ}_{\mathrm{sp}}]\big)=-\vec e_y\big(-\vec e_y\tilde{Ξ}_{\mathrm{sp}}^*\vec e_y\big)^{*}\vec e_y=\tilde{Ξ}_{\mathrm{sp}} ,
$$

because $\vec e_y^{*}=-\vec e_y$, so the two conjugations cancel the two units and the two signs with them. The two squares differ only in how many times the relation $\vec e_k^{2}=-e_t$ is used: the bilinear uses it once, on its right-hand factor, and carries one minus; the operation uses it on both factors, and the two minuses cancel. What makes the operation exchange the two values is the cell under it: multiplication on the right by $\vec e_y$ anticommutes with multiplication on the right by $\vec e_z$, which is the cell that defines the value, so the cell carries $L$ to $R$ and $R$ to $L$, while a cell that commuted with it would leave the two parts in place. Neither formula may be carried across the change of realization — the multiplier of the bilinear against the star, or the cell of the operation against the transpose — and that is why the two squares appear to disagree.

The levels are the corpus's own statements, each made in the article that owns it: the character interpretation of $\flat$ and the two labelled dictionaries are *Parra's Four Options of the Dirac Equation and the Discrete Symmetries*; the subspace interpretation of $\flat$ is *The Biquaternion Space, the Group of Involutions and the Six Subspaces*; the level-3 passage, with the explicit statement that the conjugation cell is not the coefficient conjugation, is *The Physical Interpretation of the 12 Products*; the pseudoautomorphism and the division-ring sign of $\eta^{2}$ are *Charge Conjugation and the Division Ring: Charged, Neutral and Truly Neutral Particles in Biquaternionic Form*; the level-4 identification is *The Neutrino and Majorana Fermions in Biquaternionic Form*; and the separation of all of them from the real structure on the value space of a scalar field is *The Quantized Scalar Field in Biquaternionic Form*. The $\mathbb{B}_{\Psi}/\mathbb{B}_{\Phi}$ split itself is defined by the algebra-level map, so the level-1 object is also what makes $\mathbb{B}_{\Phi}$ the material sector; the levels are not rivals but a hierarchy, and no level may be substituted for another.

## Charge Conjugation, the $\mathrm{Spin}^c$ Structure and the Neutral Fields

The preceding section separates the algebra's $\flat$ from the module's $\mathcal{C}$ and keeps the two apart. Having separated them, it is worth asking what else acts on the module. Besides the Lorentz action there is an extra central circle, and the group that includes both is $\mathrm{Spin}^c$.

**The group.** The $\mathrm{Spin}^c$ group is defined as

$$
\mathrm{Spin}^c(n) \;=\; \frac{\mathrm{Spin}(n)\times \mathrm{U}(1)}{\{\pm 1\}},
\qquad
\mathrm{Spin}^c(1,3) \;\cong\; \frac{\mathrm{SL}(2,\mathbb{C})\times \mathrm{U}(1)}{\{\pm 1\}},
$$

a double cover of $SO(1,3)\times \mathrm{U}(1)$: the spin group extended by a central circle, of dimension $7$. The quotient is not a direct product, and writing it as one is the common slip: the circle is glued to the spin group along the common $\{\pm 1\}$. It is **not** the complexification of $\mathrm{Spin}(1,3)$ — that is the larger $\mathrm{Spin}(1,3)_{\mathbb{C}}$, of real dimension twelve — and the looser name is sometimes used for it; the definition above is the one used here. $W_3$ is the integral class obstructing its existence, and the group is available exactly when $w_2$ is the mod $2$ reduction of an integral class. The algebra acts on the field by multiplication, faithfully, while the Lorentz group acts on it only **projectively**, a transformation $\Lambda$ being realised by a rotor $\pm\tilde U$; that is why the acting group is the double cover $\mathrm{Spin}(1,3)$, and $\mathrm{Spin}^c$ is the central extension that adds the circle. The extra factor is **central** in $\mathrm{Spin}^c$, and it acts on the field by the same scalar on both parts.

**The framework's central $\mathrm{U}(1)$ is that factor.** The gauge principle article localizes the $*$-unitary part of the centre — the complex scalar subspace $\mathbb{B}_{C}$, of real dimension $2$ — whose $*$-unitary elements are the phases $\lambda = \exp(i\theta)e_t$, and the minimal-coupling article writes the covariant derivative $D = \tilde{\nabla} + (iϙ/\hbar)\tilde{A}$ for exactly that phase. The phase is central in $\mathbb{B}$, so it multiplies every element alike, and it therefore commutes with the chirality cell of the frame, the multiplication on the right by $-i\vec e_z$. The cell is not itself central; it is what separates the two values of the subscript. What matters here is only that the central phase commutes with it, which gives that phase the same factor on the two parts. The framework's $\mathrm{U}(1)$ is **vector-like**, and this is structural rather than an artifact of the representation. It is the electromagnetic $\mathrm{U}(1)$.

**Which fields can carry it.** A field can be rotated by the central phase and remain a field of its own type only when its defining condition survives the rotation. The module imposes no condition, and $\tilde{Ξ}_{\mathrm{sp}}\mapsto \exp(i\alpha)\tilde{Ξ}_{\mathrm{sp}}$ is a symmetry of the free equation, so the Dirac field — with linearly independent parts of the two values — carries the $\mathrm{U}(1)$ and is charged. The Majorana field is the fixed-point set of the module's antilinear real structure, $\tilde{Ξ}_{\mathrm{sp}} = \mathcal{C}[\tilde{Ξ}_{\mathrm{sp}}]$, and $\mathcal{C}$ is conjugate-linear, so

$$
\tilde{Ξ}_{\mathrm{sp}} = \mathcal{C}[\tilde{Ξ}_{\mathrm{sp}}]
\quad\Longrightarrow\quad
\exp(i\alpha)\tilde{Ξ}_{\mathrm{sp}} = \exp(-i\alpha)\,\mathcal{C}[\tilde{Ξ}_{\mathrm{sp}}].
$$

The condition is preserved only for $\exp(2i\alpha) = 1$, that is $\alpha = 0,\pi$: the continuous phase does not act, and the Majorana field is **blind to the central $\mathrm{U}(1)$** — electrically neutral. The **ELKO** field, of Lounesto class $5$, is neutral for the same reason: it is an eigenvector of the same antilinear operator, with eigenvalue $+1$ or $-1$, so the phase acts on it only as a sign at best. The three cases therefore stand as: Dirac charged, Majorana and ELKO neutral.

It matters for the previous section *which* of the article's two real structures does the work. It is the **module's** $\mathcal{C}$ — the fixed-point condition that halves the field — and not the algebra's $\flat$. The distinction between them is thus not bookkeeping; it decides which fields can carry a charge. The minimal-coupling article reaches the same obstruction from the other side, finding that a mass term pairing the field with its conjugate would retain only $\lambda = \pm 1$ of the phase.

**What the identification re-reads.** Three negative results that the series records separately fall under one heading, and their causes come in two parts. The anomaly article finds the central phase vector-like, so that its cubic trace cancels identically; the custodial-symmetry and $W$-and-$Z$ articles find the framework's non-abelian actions — the adjoint on the material sector, and left multiplication on the field — vector-like, so that they cannot give the left- and right-handed fermions inequivalent representations. For the **central** phase the cause is now group-theoretic: it is the central circle of $\mathrm{Spin}^c$, and it is central in $\mathbb{B}$, so it commutes with the chirality cell and acts equally on the two values. For the non-abelian actions the cause is parallel but distinct: they multiply the two parts alike. The two together are why the chiral $\mathrm{U}(1)$ of hypercharge is not a gauge structure of $\mathbb{B}$.

**Gap, left visible.** What the identification does **not** settle is whether $C$ and $P$ become inner operations of the enlarged structure. The CPT companion records their internal factors, the cell that multiplies on both sides by $\vec e_y$ with a minus, and the cell that multiplies on the right by $i\vec e_x$; each anticommutes with the chirality cell, so neither is a multiplication by an element of $\mathbb{B}$, and each is therefore outer as an operation of the algebra; their intrinsic realization is left open. $\mathrm{Spin}^c$ is the central extension of $\mathrm{Spin}(1,3)$ by a circle and is the natural candidate for a structure in which the relevant direction is inner — but charge conjugation in four dimensions is **antilinear**, while the extra $\mathrm{U}(1)$ of $\mathrm{Spin}^c$ is a linear phase. Whether the antilinear $C$ can be realised through a linear group, or is irreducibly external to every such group, is **not decided here** and is stated as a question rather than a result.

## The Retired Equation: The Diagnosis Is the Dispersion

The series previously wrote the massive equation as a single **antilinear** equation in one field,

$$
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp}} = \lambda_m^{-1}\tilde{Ξ}_{\mathrm{sp}}^{\flat} , \qquad \tilde{Ξ}_{\mathrm{sp}}^{\flat} = -\tilde{Ξ}_{\mathrm{sp}}^* ,
$$

using the algebra's real structure. The equation is well formed; what disqualifies it is not its shape but its solutions.

Take the central-phase plane-wave ansatz of the parent article, with $\tilde{Ξ}_{\mathrm{sp}} = \tilde{Ξ}_{\mathrm{sp},0}\exp(i\,\mathrm{Sc}(\tilde{P}\tilde{Q}^{\natural})) = \tilde{Ξ}_{\mathrm{sp},0}\exp(i\theta)$ and $\tilde{P} = ik_0e_t + \vec e_xk_1 + \vec e_yk_2 + \vec e_zk_3$, $k_0 = \omega/c$. The computation is one of elements: the field is an element of $\mathbb{B}$, the gradient acts by left multiplication, and on the plane wave that multiplication is by $i\tilde{P}$. A single phase cannot satisfy the equation: the gradient multiplies the phase by $i\tilde{P}$, while $\flat$ conjugates it, so the two sides carry $\exp(+i\theta)$ and $\exp(-i\theta)$ and cannot match. The equation's solutions are therefore necessarily **two-frequency** superpositions,

$$
\tilde{Ξ}_{\mathrm{sp}} = \tilde{Ξ}_{\mathrm{sp},0}\,\exp(i\theta) + \tilde{Ξ}_{\mathrm{sp},1}\,\exp(-i\theta),
$$

and the equation becomes a linear system for the pair $(\tilde{Ξ}_{\mathrm{sp},0},\tilde{Ξ}_{\mathrm{sp},1})$. Its solvability depends on $\tilde{P}$, and the dependence is the whole story.

Since $\flat$ is antilinear, it conjugates the phase: $(\tilde{Ξ}_{\mathrm{sp},0}e^{i\theta})^\flat=\tilde{Ξ}_{\mathrm{sp},0}^{\flat} e^{-i\theta}$. The value of $i^\flat$ is not what does the work here — $\flat$ fixes $i$, and what conjugates the exponential is the antilinearity, $(\lambda\tilde{Ξ}_{\mathrm{sp}})^\flat=\bar{\lambda}\tilde{Ξ}_{\mathrm{sp}}^{\flat}$ for $\lambda\in\mathbb{C}$. With $\tilde{Ξ}_{\mathrm{sp},0}^{\flat}=-\tilde{Ξ}_{\mathrm{sp},0}^*$ the two modes act as

$$
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp}} = i\tilde{P}\tilde{Ξ}_{\mathrm{sp},0}\exp(i\theta) - i\tilde{P}\tilde{Ξ}_{\mathrm{sp},1}\exp(-i\theta), \qquad
\tilde{Ξ}_{\mathrm{sp}}^{\flat} = -\tilde{Ξ}_{\mathrm{sp},0}^* \exp(-i\theta) - \tilde{Ξ}_{\mathrm{sp},1}^* \exp(i\theta) ,
$$

and matching exponentials gives the two equations of elements

$$
i\tilde{P}\tilde{Ξ}_{\mathrm{sp},0} + m\tilde{Ξ}_{\mathrm{sp},1}^* = 0, \qquad
i\tilde{P}\tilde{Ξ}_{\mathrm{sp},1} - m\tilde{Ξ}_{\mathrm{sp},0}^* = 0 .
$$

These are $16$ real linear equations in the $16$ real unknowns $(\tilde{Ξ}_{\mathrm{sp},0},\tilde{Ξ}_{\mathrm{sp},1})$. Their nullity, computed by exact elimination over the integers and independent of the momentum within each row, is

| locus | shell condition | nullity |
|---|---|---|
| timelike | $k_0^2 = \vec k^2 + m^2$ | $0$ |
| spacelike | $\vec k^2 = k_0^2 + m^2$ | $4$ |
| elsewhere | — | $0$ |

The nullity vanishes on the physical shell and jumps to four on the spacelike locus. The equation has no timelike solutions and a four-real-dimensional family of spacelike ones — so its propagating modes are spacelike, at any $m\neq 0$. An equation whose central-phase plane waves are spacelike is not the Dirac equation, and it contradicts the four-momentum kinematics the rest of the series uses. That is why the equation was retired, and reproducing the two nullities by hand is a matter of pure real arithmetic.

### What the Failure Does and Does Not Show

The nullity table is easy to misread in two opposite ways, and both errors are worth naming.

**It does not say that antilinear equations are unphysical.** A Majorana mass is antilinear and physical. Its equation is nevertheless not a single-field self-pairing: the Majorana field is the Dirac field subject to the reality condition $\tilde{Ξ}_{\mathrm{sp}}=\mathcal{C}[\tilde{Ξ}_{\mathrm{sp}}]$, and since $\mathcal{C}$ carries solutions of the pair to solutions, the condition is imposed on a space the kinetic operator preserves. It halves the eight real components to four and leaves the frequency untouched, so the solutions sit on the ordinary shell $k_0^2=\vec k^2+m^2$. What differs between the two cases is not the linearity but the **space the conjugate lives on**:

- a **Majorana mass** pairs the field with a conjugate defined *on the same space as the field*, and its reality condition reduces the field to a real form on which the kinetic operator acts consistently; its mass shell is the ordinary $p^2 = m^2$, and its solution space is the four-real-dimensional Majorana space of the previous sections.
- the **retired equation** paired a field with the *algebra's* conjugate $\flat$, an involution of $\mathbb{B}$ that the field's own kinetic operator does not respect — left multiplication by a spatial generator carries $\mathbb{B}_{\Phi}$ out of itself. The mismatch between the space of the pairing and the space of the dynamics is what the spacelike dispersion is measuring.

**It does not say that the retired equation was a notation error.** The two real structures genuinely resemble one another — both antilinear, both fixed spaces of real dimension four — so the conflation was natural, and the spacelike locus is the price of it. Separating them, as the previous section does, removes the puzzle without removing any structure.

So the correct statement is narrower than "the antilinear equation was wrong", and sharper than "the antilinear equation was a slip". The framework had **two** real structures and used one where the other was meant; the dispersion is the physical signature of the substitution.

### The Four Involutions and the Mass Shell

The retired equation is one of four. For each involution $J$ of the algebra the single-field equation

$$
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp}} = m\,J(\tilde{Ξ}_{\mathrm{sp}})
$$

is formed with the same gradient and the same mass. The three antilinear involutions conjugate the phase, so as in the equation above the minimal ansatz is the two-frequency superposition, a system of $16$ real unknowns; the linear involution leaves the phase alone, a single frequency suffices there, and the count is that of an $8$-unknown system. The table gives the dimension of the solution space in each case, at a representative momentum of each locus. The three antilinear rows are constant there, as the elimination shows at every momentum tested; the control row is not, and its exceptions are listed below.

| involution | type | fixed space | timelike $k_0^2 = \vec k^2 + m^2$ | spacelike $\vec k^2 = k_0^2 + m^2$ |
|---|---|---|---|---|
| quaternion conjugation ${}^{\natural}$ | linear | $\mathbb{B}_{C}$, real dim $2$ | $2$ | $0$ |
| complex conjugation $\bar{\cdot}$ | antilinear | $\mathbb{B}_{H}$, real dim $4$ | $0$ | $8$ |
| Hermitian conjugation ${}^{*}$ | antilinear | $\mathbb{B}_{\Psi}$, real dim $4$ | $0$ | $4$ |
| anti-Hermitian conjugation $\flat=-{}^{*}$ | antilinear | $\mathbb{B}_{\Phi}$, real dim $4$ | $0$ | $4$ |

The fourth row is the retired equation, and its $0$ and $4$ reproduce the table of the previous section. The third row is the same system with $m$ replaced by $-m$, because $\flat=-{}^{*}$, so the two sector fixed spaces share their nullities: a Hermitian self-pairing and an anti-Hermitian one fail in the same way, with the same four-real-dimensional spacelike family. The second row is worse still, with a spacelike family of eight. The first row is the one linear involution of the four, and it is not a candidate mass: as the first point of the summary records, it is the one whose fixed space is not a sector, and it supplies no reality condition. It is listed as a **control**, since it is the only transformation in the table that is *not* antilinear, and it is the only row with a solution on the timelike shell. Its row is also the one row that is not constant: $2$ on the timelike shell away from rest and $6$ at the rest point $k_0=m$, $\vec k=0$, where $i\tilde P=-m$ is central and the equation reduces to $\tilde{Ξ}_{\mathrm{sp}}=-\tilde{Ξ}_{\mathrm{sp}}^{\natural}$, solved by the six-dimensional space of elements with no scalar part; $2$ at $k_0=0$, $|\vec k|=m$ and $0$ elsewhere on the spacelike shell; and $2$ on the cones $k_0=m\pm|\vec k|$, which lie on neither shell. These exceptions belong to the control and not to the diagnosis: what the three antilinear rows share, and what the control fails to share, is the vanishing on the timelike shell.

The four rows are the reason the diagnosis can be stated exactly. The failure is **not** a property of $\flat$ alone, nor of the choice among the three antilinear involutions: it is a property of **every antilinear self-pairing of the algebra**, which is why the retired equation could be rewritten with ${}^{*}$ or with $\bar{\cdot}$ and fail identically. And the failure is **not** forced by the *form* of a self-pairing either: the lone linear involution is the only one of the four with a solution on the timelike shell, so linearity alone does not save a self-pairing. The discriminator is therefore neither the linearity of the pair nor the particular involution; it is the one the article has isolated all along: **the space on which the pairing is defined**. A pairing built on the algebra's own involutions, antilinear or not, is a pairing on $\mathbb{B}$; the physical antilinear mass is built on the *module*'s real structure $\mathcal{C}$, and its mass shell is the ordinary one. The spacelike locus is the signature of an algebra-level pairing, and reading the table with that in mind turns the retired equation from a mistake into the fourth line of a classification.

## What the Antilinear Structure Is For

The algebra's real structure is retained, and the companion articles use the antilinear structure in four ways, none of which is a Dirac mass.

**The $\mathbb{B}_{\Psi}/\mathbb{B}_{\Phi}$ split itself.** The material and informational sectors are the fixed spaces of $\flat$ and ${}^{*}$, and the framework's identification of $\mathbb{B}_{\Phi}$ with material space is the statement that the field is anti-Hermitian. The sign convention by which $\flat$ acts as $+$ on $\mathbb{B}_{\Phi}$ and $-$ on $\mathbb{B}_{\Psi}$ *is* the convention that makes $\mathbb{B}_{\Phi}$ the material sector; the two are one convention seen twice.

**Bilinear pairings and the trace.** The invariant pairings of the series are built on $\flat$, and the reason is a one-line computation with the real part of the scalar part $\mathrm{Sc}$ — the coefficient of $e_t$, whose real part is what the form takes. For $\tilde{Q}=\sum_\mu(a_\mu+ib_\mu)e_\mu$ and $\tilde{P}=\sum_\mu(a'_\mu+ib'_\mu)e_\mu$,

$$
\mathrm{Re}\,\mathrm{Sc}\big(\tilde{Q}^{*}\tilde{P}\big)=\sum_\mu\big(a_\mu a'_\mu+b_\mu b'_\mu\big),
\qquad
\mathrm{Re}\,\mathrm{Sc}\big(\tilde{Q}^{\flat}\tilde{P}\big)=-\mathrm{Re}\,\mathrm{Sc}\big(\tilde{Q}^{*}\tilde{P}\big)=-\sum_\mu\big(a_\mu a'_\mu+b_\mu b'_\mu\big),
$$

so the $\flat$ pairing is the negative of the Euclidean inner product of $\mathbb{R}^8$ and the ${}^{*}$ pairing is the inner product itself. The plus sign in the first line is $i^2=-1$ read once: it is the scalar part of $(-i)(i)=+1$ in $\tilde Q{}^{*}\tilde P$, the one place where the two imaginary factors meet, and $\flat$ reverses it in the second line. So $-\mathrm{Re}\,\mathrm{Sc}\big(\tilde{Q}^{\flat}\tilde{P}\big)$ is a positive-definite inner product on the algebra, and the choice between $\flat$ and ${}^{*}$ is the choice of which sign is called positive — that is, of which sector is the material one. The linear involution gives no form at all: $\mathrm{Re}\,\mathrm{Sc}\big(\tilde{Q}^{\natural}\tilde{Q}\big)$ is not proportional to $|\tilde{Q}|^2$.

**Kramers degeneracy and antiunitary symmetry.** An antiunitary operator that commutes with the Hamiltonian and squares to $-1$ forces every level to be at least doubly degenerate. The theorem is available to the antilinear maps alone — no linear involution yields the conclusion, whatever its spectrum. The framework carries the $-1$ the theorem needs, but in an internal factor and not in the square of an operation. The internal factor of time reversal is the multiplication on the left by the real element $-\vec e_y$, so $\eta_T(\tilde X)=-\vec e_y\tilde X$ and $\eta_T^{2}=-\tilde X$, because $\vec e_y^{2}=-e_t$: a complex structure on the module. The operation itself, $T=\eta_T\circ{}^{*}$, squares to an inner automorphism instead, because the conjugation turns the left multiplication into a right one, $T^{2}(\tilde X)=\vec e_y\tilde X\vec e_y^{-1}$; that is the rotation by $\pi$ about the second axis, it satisfies $(T^{2})^{2}=\mathrm{id}$ without being $\pm\mathrm{id}$, and it is what the CPT companion calls the operation being of order two up to the free phase. The algebra's real structure is of neither kind: it is an involution, $\flat^{2}=+1$, with no complex structure anywhere in it, and that contrast — an antiunitary operation whose internal factor squares to $-1$ against an involution that squares to $+1$ — is the sharpest reason the distinction between an antilinear symmetry and a linear one has content.

**The discrete symmetries.** Charge conjugation and time reversal are antilinear, and the CPT companion establishes that the antilinearity is forced — a *linear* time reversal is not a symmetry of the Dirac equation. The internal factors of the three operations are cells of the frame, and whether a factor anticommutes with the chirality cell decides which value it carries to: the factors of charge conjugation and of parity anticommute with it and exchange the two values, the factor of time reversal commutes with it and preserves them, and so does the factor of $CPT$. The commutation governs the value; the linearity governs the spacetime parity, since an antilinear map multiplies the induced determinant by $-1$ — the point recorded in *The Reflection and the Rotation in Biquaternionic Form*.

In every one of these uses the coupling pairs the field with its conjugate, and in every one of them the pairing is a **constraint or a symmetry**, not the mass of the Dirac equation. That is the pattern the retired equation violated, and stating it positively is the content of this article: an antilinear pairing is not thereby a mass, and a mass is not thereby antilinear.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, $\gamma_0^2=I_4$ and $\gamma_k^2=-I_4$. The frame belongs to the coordinate, not to the array.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}_{\mathrm{sp}}=a\tilde{Ξ}_{\mathrm{sp}}$ and $R_b\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}} b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\begin{aligned}
\gamma_0 &= iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x}, &\gamma_1 &= iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\\[2pt]
\gamma_2 &= iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y}, &\gamma_3 &= iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\\[2pt]
\gamma_5 &= -iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z}.
\end{aligned}
$$

The same in the axis-free display:

$$
\begin{aligned}
\gamma_0 &= iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x}, &\gamma_1 &= iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\\[2pt]
\gamma_2 &= iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}, &\gamma_3 &= iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\\[2pt]
\gamma_5 &= -iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z}.
\end{aligned}
$$

A single product $L_{a}R_{b}$ is a pure tensor; the pure tensors form the seven-dimensional cone of rank at most one in $M_4(\mathbb{C})$, and a general element is a sum of at most four of them, and of no fewer than $\operatorname{rank}c(M)$, since the tensor rank of a matrix is at least its rank.

Every generator is $i$ times a real cell, so $i^2 = -1$ fixes the signs: $(iL_{a}R_{b})^{2} = -L_{a^{2}}R_{b^{2}}$, and the square of an imaginary cell is minus the square of the real one. That one line gives both signs of the frame,

$$
\gamma_0^{2} = -L_{\mathrm{pau},e_t^{2}}R_{\mathrm{pau},\vec e_x^{2}} = -L_{\mathrm{pau},e_t}R_{\mathrm{pau},-e_t} = +I_4,
\qquad
\gamma_k^{2} = -L_{\mathrm{pau},\vec e_k^{2}}R_{\mathrm{pau},\vec e_y^{2}} = -L_{\mathrm{pau},-e_t}R_{\mathrm{pau},-e_t} = -I_4.
$$

In the axis-free display:

$$
\gamma_0^{2} = -L_{\mathrm{axf},e_t^{2}}R_{\mathrm{axf},\vec e_x^{2}} = -L_{\mathrm{axf},e_t}R_{\mathrm{axf},-e_t} = +I_4,
\qquad
\gamma_k^{2} = -L_{\mathrm{axf},\vec e_k^{2}}R_{\mathrm{axf},\vec e_y^{2}} = -L_{\mathrm{axf},-e_t}R_{\mathrm{axf},-e_t} = -I_4.
$$

$\gamma_5$ is the reference-frame cell of the chirality; the central grading is a different object. It is $\chi=i\tilde{Ζ}_{\mathrm{ad}}$, with $\tilde{Ζ}_{\mathrm{ad}}$ the central root of $-e_t$, so that $\chi^2=e_t$ and $e_\pm=\tfrac12(e_t\pm\xi)$ are the two central idempotents; on the Dirac module it is represented by $\gamma_5$.

**The two conjugation cells in the frame.** The cells of the previous sections are two of these products, and reading them off settles the signs:

$$
\eta=L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x}=-i\gamma_0 ,
\qquad
\eta_C=-L_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y}=i\gamma_2 .
$$

The same identities in the axis-free display:

$$
\eta=L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x}=-i\gamma_0 ,
\qquad
\eta_C=-L_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}=i\gamma_2 .
$$

Their squares are then the frame signs at once: $(-i\gamma_0)^{2}=-\gamma_0^{2}=-I_4$, and $(i\gamma_2)^{2}=-\gamma_2^{2}=+I_4$. So the division-ring sign of the bilinear, $\eta^{2}=-I_4$, and the cancellation that makes $\mathcal{C}[\tilde{Ξ}_{\mathrm{sp}}]$ an involution, $\eta_C^{2}=+I_4$, are one line of the frame: the timelike generator squares to $+I_4$ and the spatial one to $-I_4$, and each square is read with the extra minus of $i^2=-1$.

The dictionary is complex-linear; over $\mathbb{R}$ the gammas span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$, while the real cells $L_aR_b$ span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities used in the body.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$ and every trace taken on the module $\Delta$, of complex dimension four,

$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,\qquad
\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3,
\qquad \varepsilon=(1,-1,-1,-1),$$

$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d-\varepsilon_a\delta_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$

The contraction sums are frame statements, because their signs are the signs of the cells' squares. The four are

$$
\sum_\mu\gamma_\mu\gamma_\mu,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\mu,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\mu,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\delta\gamma_\mu .
$$

With the summed index raised, $\gamma^\mu=-\varepsilon_\mu\gamma_\mu$, they are $-4I_4$, $+2\gamma_\alpha$, $-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $-2\gamma_\alpha\gamma_\beta\gamma_\delta$. With every index low only the first keeps a closed form, $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$; the other three are index-dependent and are computed, not transcribed.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{\mathrm{axf},e_\mu}=C_{\Pi}L_{\mathrm{pau},e_\mu}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

1. **Four involutions, four fixed spaces.** The algebra carries quaternion conjugation (linear) and complex, Hermitian and anti-Hermitian conjugation (all antilinear), with fixed spaces of real dimensions $2, 4, 4, 4$. The two sectors are the fixed spaces of the last two, and the one that is the fixed space of the *linear* involution is not a sector at all.

2. **A mass is a pairing with a conjugate.** The mass is the non-derivative part of the equation; it has nothing to differentiate, so it must pair the field with a second field, and in a single-field equation that second field is a conjugate of the first. Which conjugation is chosen — or whether a chiral partner stands in its place — is the definition of which kind of mass.

3. **The two kinds are the pairing of two values and the self-pairing.** The Dirac mass is linear and couples the two values of the subscript; the Majorana mass is antilinear and pairs the field with its own conjugate. In biquaternionic form the Dirac mass is two equations, one per value; the two-sided form carries the same coupling in a single equation, with the derivative entering from the left and the mass from the right, and the two readings differ in the shape of the mass term and not in the coupling. The counts differ before any dynamics is imposed: $8$ real components against $4$.

4. **The algebra's $\flat$ and the module's $\mathcal{C}$ are different real structures.** Both antilinear, both with a four-real-dimensional fixed space, but on different spaces. The Dirac operator preserves the module's real form and does not preserve $\mathbb{B}_{\Phi}$; the matching dimension count does not identify them.

5. **The $\mathrm{Spin}^c$ structure organises charge conjugation, and it decides who is charged.** $\mathrm{Spin}^c(1,3) = \bigl(\mathrm{Spin}(1,3)\times \mathrm{U}(1)\bigr)/\{\pm 1\}$ is the spin group extended by a central circle, and the framework's central $\mathrm{U}(1)$ — the phase that minimal coupling localizes — is that circle. Being central it commutes with the chirality cell and is therefore **vector-like**: the electromagnetic $\mathrm{U}(1)$, not a chiral one. A Dirac field carries it; a Majorana or ELKO field is fixed by an antilinear condition and is blind to it, hence neutral. It is the module's $\mathcal{C}$, not the algebra's $\flat$, that enforces the neutrality.

6. **The retired equation failed on its dispersion.** Its central-phase plane waves have nullity $0$ on the timelike shell and $4$ on the spacelike one, so its modes are spacelike. It is one of four: every antilinear self-pairing of the algebra shares the spacelike locus — nullity $4$ on the two sector fixed spaces and $8$ on the real-quaternion one — while the single linear involution is the only one with a solution on the timelike shell.

7. **The failure was the pairing, not the antilinearity.** A Majorana mass is antilinear and physical. The retired equation paired a field with the algebra's conjugate, on a space where its kinetic operator does not respect it.

8. **The antilinear structure is retained and used.** The sector split, the bilinear pairings, Kramers degeneracy, and the discrete symmetries $C$ and $T$ are all built on it — as constraints and symmetries, never as the Dirac mass.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra; real dim $8$, complex dim $4$ |
| $\tilde{Q}^{\natural}$, $\bar{\tilde{Q}}$, $\tilde{Q}^{*}$, $\tilde{Q}^{\flat}$ | Quaternion, complex, Hermitian, anti-Hermitian conjugations |
| $\tilde{Q}^\flat = -\tilde{Q}^{*}$; $e_t^\flat = -e_t$, $\vec e_k^\flat = \vec e_k$, $i^\flat = +i$ | The algebra's real structure; the antilinear involution that negates the real unit and fixes the three spatial units and $i$ |
| $\mathbb{B}_{\Phi} = \{\tilde{Q} : \tilde{Q}^\flat = \tilde{Q}\}$ | Anti-Hermitian (material) sector, real dim $4$ |
| $\mathbb{B}_{\Psi} = \{\tilde{Q} : \tilde{Q}^{*} = \tilde{Q}\}$ | Hermitian (informational) sector, real dim $4$ |
| $\mathbb{B}_{H} = \{\tilde{Q} : \bar{\tilde{Q}} = \tilde{Q}\}$ | Real-quaternion sector, real dim $4$ |
| $\mathbb{B}_{C} = \{\tilde{Q} : \tilde{Q}^{\natural} = \tilde{Q}\}$ | Centre, real dim $2$ |
| $\mathrm{Sc}\,\tilde{Q}$ | Scalar part, the coefficient of $e_t$; $\mathrm{Sc}\big(\tilde{Q}^\flat\tilde{Q}\big) = -\lvert\tilde{Q}\rvert^2$, $\mathrm{Sc}\big(\tilde{Q}^{*}\tilde{Q}\big) = +\lvert\tilde{Q}\rvert^2$ |
| $\tilde{\nabla}$, $\tilde{\nabla}^{\natural}$ | Biquaternionic gradient and its conjugate; $\tilde{\nabla}\tilde{\nabla}^{\natural} = \Box$ |
| $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = \lambda_m^{-1}\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = \lambda_m^{-1}\tilde{Ξ}_{\mathrm{sp},R}$ | The Dirac mass: linear, off-diagonal in the value of the subscript |
| $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp}} = \lambda_m^{-1}\tilde{Ξ}_{\mathrm{sp}}^{\flat}$ | The retired equation; spacelike dispersion, not a mass term |
| $\mathcal{C}[\tilde{Ξ}_{\mathrm{sp}}]=-\vec e_y\tilde{Ξ}_{\mathrm{sp}}^*\vec e_y$, $\mathcal{C}^{2}=1$ | Charge conjugation on the module; the Majorana reality condition. Its transposed realization is the bilinear $\mathrm{Sc}\big(\tilde{Ξ}_{\mathrm{sp}}\,\vec e_x\,\tilde{Ξ}_{\mathrm{sp}}\big)$, whose multiplier satisfies $\eta(\tilde X)=\tilde X\vec e_x$, $\eta^{2}=-I$ |
| $\mathrm{Spin}^c(1,3) = \bigl(\mathrm{Spin}(1,3)\times \mathrm{U}(1)\bigr)/\{\pm 1\}$ | Central extension of the spin group by a circle; its central factor is the framework's central phase, and a charged field is one on which that factor acts non-trivially |
| $\Delta = S\oplus\bar{S}$ | Dirac module, real dim $8$; $\mathcal{C}$ exchanges the halves |
| $a\tilde{Ξ}_{\mathrm{sp}} b$ | The two-sided action; the side is carried by position and never by a mark |
| $D_3=\sum_k\vec e_k\,\partial/\partial R_k$; $r'_t$ | Three-dimensional Cauchy–Riemann operator; imaginary time, in the two-sided form only |
| $m_D$, $m_M$ | Dirac and Majorana masses |
| $\flat$ acts $+$ on $\mathbb{B}_{\Phi}$, $-$ on $\mathbb{B}_{\Psi}$ | The sector sign; the same convention as the material identification |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- Foundational articles: [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html); [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html); [Conventions in the Biquaternion Universe](algebra-and-element-conventions.html) (the mass-term convention, the real structure $\flat$, and the dispersion failure this article expands).
- The Dirac mass in biquaternionic form: [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) (the linear chiral pair and the massless limit $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp}} = 0$); [The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit](the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html).
- The Majorana side: [The Neutrino and Majorana Fermions in Biquaternionic Form](the-neutrino-and-majorana-fermions-in-biquaternionic-form.html) (charge conjugation on the module, the Majorana condition, and the obstruction by which $\mathbb{B}_{\Phi}$ fails to be a reality condition); [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html) (why a chiral fermion cannot carry a bare Dirac mass).
- The antilinear discrete symmetries: [The CPT Theorem in Biquaternionic Form](the-cpt-theorem-in-biquaternionic-form.html) ($C$ and $T$ antilinear, and why a linear $T$ is not a symmetry).
- On the reflection parity that antilinearity shifts: [The Reflection and the Rotation in Biquaternionic Form](the-reflection-and-the-rotation-in-biquaternionic-form.html).
- The Clifford structures: [Conventions of the Matrix Models](matrix-representations-conventions.html), §*The Clifford Structure and the Frame*; *Spinors*.
- The $\mathrm{Spin}^c$ structure and its obstruction: the definition of $\mathrm{Spin}^c$, of $W_3$, and of $w_2$ as the mod $2$ reduction of an integral class; [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html) (the localized central phase and the $\lambda = \pm 1$ obstruction).
