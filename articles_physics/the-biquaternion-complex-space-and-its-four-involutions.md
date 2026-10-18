# __The Biquaternioid Complex Space and Its Four Involutions__

## Introduction

This article reads the biquaternion complex space and its four involutions in the physical frame. Its scope is the scope of *The Biquaternioid as a Vector Space over $\mathbb{C}$*: the elements, the basis and the complex scalar action, the three coordinate systems, and the four conjugations with the fixed spaces they cut out. It adds one thing to that scope, the physical dictionary of the coordinates and the physical readings the space carries, and it leaves the rest to the articles that own it.

The place of the article is fixed by that scope. It stands just after *The Biquaternion Mathematics Corpus*, as the physics companion of the complex-space article: the same space, the same four formulas, read with the physical names on the eight real parameters. It comes before the band *Focus on Biquaternioid structures*, because the four involutions are the alphabet of that band — every product they read is one multiplication of the algebra with a conjugation inserted into a slot, and every form they read is a scalar part of such a product — and a reader who has the involutions has the vocabulary of everything that follows.

Nothing is owned here. The elements, the basis, the complex scalar action, the three coordinate systems and the four conjugation formulas are *The Biquaternioid as a Vector Space over $\mathbb{C}$*; the real reading and the complex structure are *The Biquaternioid as a Vector Space over $\mathbb{R}$*; the composition of the four conjugations, the Klein group they form and the place of the reversal are *The Group of Involutions*; the six remarkable subspaces, which are their fixed and anti-fixed spaces, are *Introduction to the Remarkable Subspaces*, with their blocks and their lattice in *Comparison of the Remarkable Subspaces*; the physical dictionary and the anti-Hermitian convention are *Conventions in the Biquaternion Universe*; the physical content of the two sectors is *Introduction to the Biquaternion Universe*; and the products, the forms and the norms of the space are the articles of the band that follows, not this one.

## The Complex Space

The **biquaternion algebra** is the complexification of the quaternion algebra,

$$
\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H},
$$

read as a **complex vector space of dimension four** on the basis $e_t, \vec e_x, \vec e_y, \vec e_z$, with the unit and the quaternion relations

$$
e_t = 1, \qquad \vec e_x^2 = \vec e_y^2 = \vec e_z^2 = -e_t, \qquad \vec e_x\vec e_y = -\vec e_y\vec e_x = \vec e_z,
$$

with the cyclic companions $\vec e_y\vec e_z = -\vec e_z\vec e_y = \vec e_x$ and $\vec e_z\vec e_x = -\vec e_x\vec e_z = \vec e_y$. A general element is

$$
\tilde Q = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu = Q_t e_t + \vec Q, \qquad \vec Q = \sum_{k=1}^{3} Q_k \vec e_k, \qquad Q_\mu \in \mathbb{C},
$$

the **scalar part** $Q_te_t$ and the **vector part** $\vec Q$. The tilde marks an element of the algebra, the majuscule a complex coefficient and the boldface a vector part.

**Four complex coordinates, eight real ones.** Every coefficient is a real part plus $i$ times a real part,

$$
Q_\mu = q_\mu + i q'_\mu, \qquad q_\mu, q'_\mu \in \mathbb{R},
$$

so the four complex coordinates are eight real ones: $q_\mu$ is the coefficient of $e_\mu$ and $q'_\mu$ the coefficient of $ie_\mu$, the prime marking the slot that carries the scalar imaginary, the same rule for every $\mu$.

**The central imaginary.** The unit $i$ satisfies $i^2 = -1$ and commutes with the quaternion units, $i e_\mu = e_\mu i$, because it belongs to the $\mathbb{C}$ factor of the tensor product while the units belong to the $\mathbb{H}$ factor. Multiplication by it is the real-linear **complex structure** $J$, with $J^2 = -\mathrm{id}$, of the real reading *The Biquaternioid as a Vector Space over $\mathbb{R}$*. The elements commuting with everything are the multiples of $e_t$, so the **centre** is the complex line $\mathbb{C}e_t$, of real dimension two, spanned by $e_t$ and $ie_t$; its elements of unit modulus, $\exp(i\theta)e_t$, are the **central phase**, and the centre is the algebra's classical or global sector.

## The Coordinates

One element, three scalar systems, all three used in the corpus.

| coordinates | basis | count | scalars |
|---|---|---|---|
| real | $e_t, \vec e_x, \vec e_y, \vec e_z, ie_t, i\vec e_x, i\vec e_y, i\vec e_z$ | $8$ | $\mathbb{R}$ |
| complex | $e_t, \vec e_x, \vec e_y, \vec e_z$ | $4$ | $\mathbb{C}$ |
| quaternionic | $e_t, ie_t$ | $2$ | $\mathbb{H}$ |

The third row gathers the eight real numbers as a real quaternion plus $i$ times another, $\tilde Q = h_1 + i h_2$ with $h_1 = \sum_\mu q_\mu e_\mu$ and $h_2 = \sum_\mu q'_\mu e_\mu$ in $\mathbb{H}$; the first two gather the same numbers as eight real coordinates or as four complex ones. The three rows are one object.

**The physical dictionary.** The eight real parameters are read as physical coordinates by the dictionary, fixed once and for all,

$$
q'_t = c\,t, \qquad (q_x, q_y, q_z) = (x, y, z), \qquad q_t = c\,t', \qquad (q'_x, q'_y, q'_z) = (x', y', z'),
$$

with $x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ the real spatial vector and $x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z$ its informational counterpart. Its two ends are the coordinates of the two sectors,

$$
\tilde R = i c t\, e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z, \qquad \tilde Q = c t'\, e_t + i(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z),
$$

the **material coordinate**, with the temporal direction imaginary and the three spatial directions real, and the **informational coordinate**, with the temporal direction real and the three spatial directions imaginary. Read together with the complex coefficients, each $Q_\mu$ has three guises:

| coefficient | complex | real part | imaginary part | material | informational |
|---|---|---|---|---|---|
| $Q_t$ | $q_t + iq'_t$ | $c t'$ | $c t$ | $i c t$ | $c t'$ |
| $Q_x$ | $q_x + iq'_x$ | $x$ | $x'$ | $x$ | $i x'$ |
| $Q_y$ | $q_y + iq'_y$ | $y$ | $y'$ | $y$ | $i y'$ |
| $Q_z$ | $q_z + iq'_z$ | $z$ | $z'$ | $z$ | $i z'$ |

**The prime falls on the scalar in one sector and on the three vectors in the other.** In the material sector the primed parameter is the time, $q'_t = ct$, so the temporal direction is imaginary and the three spatial directions real. In the informational sector the primed parameters are the three space coordinates, $q'_k = x'_k$, so the temporal direction is real and the three spatial directions imaginary. The two sectors are the same eight coordinates with the place of the prime exchanged, which is the mirror statement of the algebra and not a second convention.

**One element, one point, one label.** The eight parameters split four and four between the sectors, so one element of $\mathbb{B}$ carries a point of the material sector and a point of the informational sector at once. A material element is a spacetime event, $i c t\, e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$, and the four informational parameters it also carries are its internal label; an informational element is a point $c t'\, e_t + i(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)$ of the state side, carrying four material labels. No coefficient is idle, and that is why one element of the algebra serves both as a four-vector and as a state; the physical content is *Introduction to the Biquaternion Universe*.

**Why the temporal coordinate is imaginary.** The material time enters as $i c t$, and the factor $i$ is what the algebra supplies: because $i^2 = -1$, a temporal displacement and a spatial displacement do not count with the same sign, and the reversed sign of the time is carried by the imaginary unit and not added by hand. With $c t$ real in place of $i c t$ the material sector would carry a Euclidean reading and no causal cone. The dictionary and the convention are *Conventions in the Biquaternion Universe*, and the causal structure they produce belongs to the articles on the material sector.

**The local complex structure.** The identification of which direction is the scalar imaginary is not rigid. In a material medium the map from physical time to the imaginary scalar direction carries the local scale $c = 1/\sqrt{\epsilon\mu}$, so the complex structure, and with it the dictionary above, varies from point to point, in the same spirit as the metric of general relativity; the vacuum, $c = c_0$, is the limiting member of the family and the case read here. The owner is *The Local Complex Structure and the Speed of Light*.

**The anti-Hermitian convention.** The material sector is the **anti-Hermitian** subspace, fixed by the reversal of the involution list below, where the more familiar convention takes the Hermitian subspace as the real one. The two differ by the central factor $i$ and there is no mathematical error either way; the corpus fixes the anti-Hermitian one because the material sector is the fixed space of the algebra's real structure and carries the four-positions and the four-vectors. A reader who restores the Hermitian convention will find the whole corpus inverted.

## The Four Involutions

The algebraic content of the article is the four conjugations. The **complex conjugation** $\bar{\cdot}$, the **quaternion conjugation** ${}^{\natural}$, the **Hermitian conjugation** ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ and the **anti-Hermitian conjugation** ${}^{\flat} = -{}^{*}$ act on the coordinates $\tilde Q = \sum_\mu Q_\mu e_\mu$ by the following table. Write $\varepsilon = (1, -1, -1, -1)$ for the **sign vector** that keeps the scalar direction and negates the three vector ones.

| Involution | Symbol | Conjugate Element | Sign-Vector Rule | $\mathbb{C}$-Linear | $\mathbb{C}$-Antilinear | $\mathbb{R}$-Linear |
|---|---|---|---|---|---|---|
| Complex Conjugation | $\bar{\cdot}$ | $\bar{\tilde Q} = \bar Q_t e_t + \bar Q_x \vec e_x + \bar Q_y \vec e_y + \bar Q_z \vec e_z$ | $(\bar{\tilde Q})_\mu = \bar Q_\mu$ | No | Yes | Yes |
| Quaternion Conjugation | ${}^{\natural}$ | $\tilde Q^{\natural} = Q_t e_t - Q_x \vec e_x - Q_y \vec e_y - Q_z \vec e_z$ | $(\tilde Q^{\natural})_\mu = \varepsilon_\mu Q_\mu$ | Yes | No | Yes |
| Hermitian Conjugation | ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ | $\tilde Q^{*} = \bar Q_t e_t - \bar Q_x \vec e_x - \bar Q_y \vec e_y - \bar Q_z \vec e_z$ | $(\tilde Q^{*})_\mu = \varepsilon_\mu \bar Q_\mu$ | No | Yes | Yes |
| Anti-Hermitian Conjugation | ${}^{\flat} = -{}^{*}$ | $\tilde Q^{\flat} = -\bar Q_t e_t + \bar Q_x \vec e_x + \bar Q_y \vec e_y + \bar Q_z \vec e_z$ | $(\tilde Q^{\flat})_\mu = -\varepsilon_\mu \bar Q_\mu$ | No | Yes | Yes |

The three linearity properties are collected in the last columns of the table above: the quaternion conjugation is the only $\mathbb{C}$-**linear** one of the four, the other three are $\mathbb{C}$-**antilinear**, and all four are $\mathbb{R}$-linear, since conjugating a complex coefficient is an $\mathbb{R}$-linear operation.

The natural conjugation keeps the scalar coordinate and negates the three vector ones; the bar conjugates the four complex coefficients and touches no basis element; the star does both; the flat is the negative of the star. In sign-vector form, the natural conjugation and the star carry $+\varepsilon$, the anti-Hermitian conjugation carries $-\varepsilon$, and the bar carries no sign vector at all, since it touches no basis element.

**Each is an involution.** Applying any one of the four twice returns the element, so each cuts the algebra into a fixed space and an anti-fixed space, and each of the two is a real vector subspace.

**One is linear, three are antilinear.** The natural conjugation is $\mathbb{C}$-**linear**, the natural conjugate of $\lambda\tilde Q$ being $\lambda\tilde Q^{\natural}$ for every complex scalar $\lambda$; the bar, the star and the flat are $\mathbb{C}$-**antilinear**. Which factor of the tensor product a map touches decides it: the natural conjugation touches the quaternion factor and leaves the complex scalars alone, the bar touches the scalars and leaves the units alone, and the star touches both. The linearity or antilinearity of each is what the real reading *The Biquaternioid as a Vector Space over $\mathbb{R}$* records, and the two classes are used throughout the corpus.

**The group.** The identity, the natural, the bar and the star close into a group of order four,

$$
{}^{*} = \bar{\cdot} \circ {}^{\natural} = {}^{\natural} \circ \bar{\cdot}, \qquad \{\mathrm{id}, {}^{\natural}, \bar{\cdot}, {}^{*}\} \cong V_4,
$$

the **Klein four-group**, in which the composition of two non-identity elements is the third. The flat is the star times the central sign, $\flat = -{}^{*}$, and it lies **outside** the group: it is the fourth character and not a fifth conjugation of the algebra. The Cayley table, the composition with the reversal included and the anti-automorphism property of the natural and the star with respect to the product are *The Group of Involutions*, and no product is read here.

**What each one does.** The **bar** conjugates the scalar imaginary, so on the central phase it acts as $\theta \mapsto -\theta$; the **natural conjugation** reflects the three quaternion directions, fixing the scalar direction and the central unit; the **star** does both at once, and it is the conjugation under which the states and the observables of the informational sector are self-adjoint; the **reversal** is the star with the global sign, and its shape is that of a charge-conjugation pairing, which is why it is the algebra's **real structure** and why the physical sector of the corpus is the anti-Hermitian one. None of the four moves an element between the two sectors.

**Fixed spaces and the remarkable subspaces.** The fixed and anti-fixed spaces met above are the six **remarkable subspaces** of the corpus. The natural conjugation fixes the **centre** $\mathbb{C}_{\mathbb{B}}$ and anti-fixes the **vector subspace** $\mathrm{Vect}(\mathbb{B})$, which are complementary, of real dimensions two and six. The bar fixes the **quaternion subspace** $\mathbb{H}_{\mathbb{B}}$ and anti-fixes the **antiquaternion subspace** $i\mathbb{H}_{\mathbb{B}}$, again complementary, of dimensions four and four. The star fixes the **Hermitian subspace** $\mathbb{M}_+$ and anti-fixes the **anti-Hermitian subspace** $\mathbb{M}_-$, and the reversal reproduces exactly these two spaces with the signs exchanged, so it adds no new subspace. The four involutions therefore produce six remarkable subspaces and not eight. They are not defined here: they are defined one to a section in *Introduction to the Remarkable Subspaces*, with their coordinate blocks and their lattice in *Comparison of the Remarkable Subspaces*.

## The Two Sectors

Two of the six subspaces are the physical backbone of the corpus, and their definition belongs to the involutions just listed.

The **sector split** is

$$
\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+, \qquad \mathbb{M}_- = \{\tilde Q : \tilde Q^{*} = -\tilde Q\}, \qquad \mathbb{M}_+ = \{\tilde Q : \tilde Q^{*} = +\tilde Q\},
$$

the eigenspace split of the Hermitian conjugation, and it is also the split into the fixed and anti-fixed spaces of the reversal, which is the star with the central sign. The **material sector** $\mathbb{M}_-$ is the anti-Hermitian one, where the scalar coefficient is imaginary and the three vector coefficients are real; it carries the four-position $i c t\, e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ and the four-vectors, and it is the fixed space of the algebra's real structure. The **informational sector** $\mathbb{M}_+$ is the Hermitian one, where the scalar coefficient is real and the three vector coefficients are imaginary; it carries the states and the observables, and it is the fixed space of the star. Every one of the four involutions preserves both sectors, which is why the two can carry two different physical readings without a cross-term; the maps that do cross between them are built from the central unit and are *Cross-Sector Coupling in the Biquaternion Framework: A Catalogue of the Maps Between the Sectors*.

On the physical dictionary the sectors read as the two ends of the table above: the material sector has three real spatial directions and one imaginary temporal one, $\mathbb{M}_-\ni i c t\, e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$, and the informational sector three imaginary spatial directions and one real temporal one, $\mathbb{M}_+\ni c t'\, e_t + i(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)$. The physics of the material sector is *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, the physics of the informational sector *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, and the sector split in the framework *Introduction to the Biquaternion Universe*. The informational sector is written in quantum physics with the letter of an operator, $\mathbb{M}_+ \ni \tilde{H} = h_0e_t + ih_1\vec e_x + ih_2\vec e_y + ih_3\vec e_z$ with real $h_\mu$: the same element as $ct'\,e_t + i(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)$, under coefficient names that record its role as a Hermitian operator, and the Pauli expansion $h_0I_2 + h_1\sigma_1 + h_2\sigma_2 + h_3\sigma_3$ under the module dictionary of *The Native Qubit and the Defining Module of the Biquaternion Algebra*.

## Physical Readings

Two readings of the space and of the involutions belong to this article: the sector split is the eigenspace split of one involution, and the four involutions are the algebra's own discrete structure.

**The sectors are the eigenspaces of the star.** The split $\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+$ is exactly the split into the eigenspaces of the Hermitian conjugation for the eigenvalues $-1$ and $+1$, so the corpus's two sectors are the two halves of one involution and not two spaces placed side by side. The material sector is at the same time the fixed space of the reversal, the star with the central sign, which is the algebra's real structure; that is the algebra's reason for carrying the four-positions and the four-vectors, and it is why the corpus's convention is the anti-Hermitian one and not the Hermitian one.

**The involutions preserve the sectors.** Each of the four conjugations maps each sector into itself, because the star acts by a sign on $\mathbb{M}_\pm$ and the natural conjugation acts by a sign on the vector directions. No conjugation carries an element from the material sector to the informational one, and this is why the two sectors can carry two different physical readings without a cross-term.

**The complex structure is local.** The physical dictionary of the coordinates is fixed by the identification of the scalar imaginary, and that identification is not rigid: the dictionary varies from point to point through the local scale $c = 1/\sqrt{\epsilon\mu}$ of a material medium, so the complex structure itself is a field and not a constant. This is the algebra's way of carrying the same freedom the metric carries in general relativity, and the corpus's `ict` is the vacuum value of the family.

**The discrete structure of the algebra.** Read physically, the four involutions are what the discrete symmetries of the corpus are built on: the bar conjugates the phase carried by $i$, the natural conjugation reflects the three vector directions, the star does both at once, and the reversal is the real structure. The four sign characters act on the four coordinate blocks, and the labels the corpus reads are parity, time reversal and charge conjugation for three of them; the owner is *The Centre of the Biquaternion Algebra as the Classical Sector*.

## Summary

The biquaternion complex space is $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ read as a complex vector space of dimension four on the basis $e_t, \vec e_x, \vec e_y, \vec e_z$, with $\vec e_k^2 = -e_t$ and $\vec e_x\vec e_y = \vec e_z$ cyclic. A general element is $\tilde Q = \sum_\mu Q_\mu e_\mu$ with complex coefficients $Q_\mu = q_\mu + iq'_\mu$, so it has four complex coordinates, eight real ones and a reading as a pair of real quaternions; the central imaginary $i$ commutes with the units, its multiples form the centre $\mathbb{C}e_t$, and its unit-modulus elements $\exp(i\theta)e_t$ are the central phase.

The eight real parameters are read as physical coordinates, $q'_t = ct$, $(q_x,q_y,q_z) = (x,y,z)$, $q_t = ct'$ and $(q'_x,q'_y,q'_z) = (x',y',z')$. The material coordinate is $ict\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ and the informational coordinate is $ct'\,e_t + i(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)$; the prime falls on the scalar in the first and on the three vectors in the second, so the two sectors are mirror images, with three real spatial directions and one imaginary temporal one against three imaginary spatial directions and one real temporal one. The temporal coordinate is imaginary because the algebra's central unit supplies the reversed sign of a timelike displacement, and the identification of that unit is local, carrying the scale $c = 1/\sqrt{\epsilon\mu}$.

The space carries four involutions, ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ and $\flat = -{}^{*}$. The natural conjugation is $\mathbb{C}$-linear and the other three are $\mathbb{C}$-antilinear; the identity, the natural, the bar and the star form the Klein four-group, and the flat is the fourth character outside it. Each involution cuts the algebra into a fixed and an anti-fixed space, giving the six remarkable subspaces, of which the corpus develops the two sectors; the sector split $\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+$ is the eigenspace split of the star, reproduced by the reversal, and every involution preserves both sectors. The products, the forms and the norms of the space are the subject of the band that follows, not of this article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | the biquaternion algebra |
| $e_t, \vec e_x, \vec e_y, \vec e_z$ | the basis, $e_t = 1$, $\vec e_k^2 = -e_t$ |
| $i$ | the central scalar imaginary, $i^2 = -1$ |
| $\tilde Q = \sum_\mu Q_\mu e_\mu$ | a general element |
| $Q_\mu = q_\mu + i q'_\mu$ | a complex coefficient, $q_\mu, q'_\mu \in \mathbb{R}$ |
| $Q_t$, $\vec Q$ | the scalar part and the vector part |
| $q'_t = c t$, $(q_x,q_y,q_z) = (x,y,z)$ | the material dictionary |
| $q_t = c t'$, $(q'_x,q'_y,q'_z) = (x',y',z')$ | the informational dictionary |
| $i c t\, e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ | the material coordinate, in $\mathbb{M}_-$ |
| $c t'\, e_t + i(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)$ | the informational coordinate, in $\mathbb{M}_+$ |
| $J : \tilde Q \mapsto i\tilde Q$ | the real-linear complex structure, $J^2 = -\mathrm{id}$ |
| ${}^{\natural}$ | quaternion conjugation, the $\mathbb{C}$-linear involution |
| $\bar{\cdot}$ | complex conjugation, the $\mathbb{C}$-antilinear involution |
| ${}^{*} = \bar{\cdot} \circ {}^{\natural}$ | Hermitian conjugation, the $\mathbb{C}$-antilinear involution |
| $\flat = -{}^{*}$ | anti-Hermitian conjugation, outside the Klein group |
| $\varepsilon = (1, -1, -1, -1)$ | the sign vector of the natural conjugation |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ | the six remarkable subspaces |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | the material sector and the informational sector |

## Further Reading

- *The Biquaternioid as a Vector Space over $\mathbb{C}$* (`articles_maths/the-biquaternioid-vector-space-over-c.md`), for the elements, the basis, the three coordinate systems and the four conjugation formulas.
- *The Biquaternioid as a Vector Space over $\mathbb{R}$* (`articles_maths/the-biquaternioid-vector-space-over-r.md`), for the realification and the complex structure $J$.
- *The Group of Involutions* (`articles_maths/the-group-of-involutions.md`), for the Klein four-group, its Cayley table and the place of the reversal outside it.
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`) and *Comparison of the Remarkable Subspaces* (`articles_maths/comparison-of-the-remarkable-subspaces.md`), for the six subspaces, their blocks and their lattice.
- *The Biquaternion Mathematics Corpus* (`articles_physics/the-biquaternion-mathematics-corpus.md`), the article this one follows and the index of the mathematics corpus it cites.
- *Conventions in the Biquaternion Universe* (`articles_physics/conventions-in-the-biquaternion-universe.md`), for the physical dictionary, the anti-Hermitian convention and the mathematical conventions of the corpus.
- *Introduction to the Biquaternion Universe* (`articles_physics/introduction-to-the-biquaternion-universe.md`), for the physical content of the two sectors.
- *The Local Complex Structure and the Speed of Light* (`articles_physics/the-local-complex-structure-and-the-speed-of-light.md`), for the local reading of the scalar imaginary.

