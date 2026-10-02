# __Different Ways to Consider Biquaternions__

## Introduction

The biquaternion algebra is a single set of elements, $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, and it carries several structures at once. Someone who asks what the set *is* gets a different and equally correct answer depending on which scalars are admitted. Admit the reals and it is an algebra of dimension eight. Admit the complex numbers and it is an algebra of dimension four. Admit the quaternions and it is a module of rank two. The three answers describe the same elements, the same addition and the same product; the only thing that changes is the scalar system.

This article develops the three answers in turn, from the simplest outward, and then asks the question that ties them together: over which rings is $\mathbb{B}$ an algebra in the strict sense? The answer is that $\mathbb{R}$ and $\mathbb{C}$ qualify and $\mathbb{H}$ does not, and the reason is a single structural fact about the centre, treated once the three views are in place. The conclusion is that **the natural structure of the biquaternion algebra is an algebra over $\mathbb{C}$**.

The general definitions are those of *Algebras: A General Introduction*, where an algebra is defined over a commutative ring, and of *Change of Rings*, for extension and restriction of scalars. The basis, the multiplication, the conjugations and the six subspaces are those of *Biquaternion Algebra* and are not restated.

## The Elements and the Three Coordinate Systems

A general element is written

$$
\tilde{Q} = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3, \qquad Q_\mu \in \mathbb{C},
$$

with unit $e_0$, quaternion units $e_k$ satisfying $e_k^2 = -e_0$, and a central scalar imaginary $i$, $i^2 = -1$, commuting with every $e_k$.

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

The three rows count the same element against three scalar systems. Each supports one structure, and the rest of the article takes them in turn.

## As an Algebra over $\mathbb{R}$

### The Real Algebra Structure

**Definition.** Let $R$ be a ring. An **$R$-algebra** is a ring $A$ together with a ring homomorphism $R \to Z(A)$ into the centre of $A$. The image is required to be central, so that the scalars commute with every element of $A$, and the product is then $R$-bilinear.

**The structure map.** The assignment

$$
\mathbb{R} \longrightarrow Z(\mathbb{B}), \qquad r \longmapsto re_0
$$

is a unital ring homomorphism and its image is central, since $re_0$ commutes with every element of $\mathbb{B}$. It gives the **real scalar multiplication** $r\tilde{Q} = rQ_0e_0 + rQ_1e_1 + rQ_2e_2 + rQ_3e_3$, applied to the four complex coefficients or, equivalently, to the eight real coordinates term by term. Because the image is central,

$$
r(\tilde{P}\tilde{Q}) = (r\tilde{P})\tilde{Q} = \tilde{P}(r\tilde{Q}), \qquad r \in \mathbb{R},
$$

so the product is $\mathbb{R}$-bilinear. The algebra is associative, with unit $e_0$.

### The Real Dimension and the Real Products

Over $\mathbb{R}$ the algebra has **dimension eight**, on the real basis of the first section. Its products are fixed by $e_k^2 = -e_0$, by $i^2 = -e_0$ and by the commutation of $i$ with each $e_k$:

| product | value | reason |
|---|---|---|
| $e_je_k$, $j \neq k$ | $\pm e_l$, the third unit | the quaternion product |
| $e_k^2$ | $-e_0$ | the quaternion units |
| $(ie_0)^2$ | $-e_0$ | $i^2e_0^2 = (-1)(+e_0)$ |
| $(ie_k)^2$, $k = 1,2,3$ | $+e_0$ | $i^2e_k^2 = (-1)(-e_0)$ |
| $ie_k = e_ki$ | the central imaginary | $i$ is central |

The last two rows deserve a remark, and they are the reason the real view is worth having. The four elements $ie_0, ie_1, ie_2, ie_3$ are **not** a second set of quaternion units. The element $ie_0$ is a second imaginary unit, with $(ie_0)^2 = -e_0$; the elements $ie_1, ie_2, ie_3$, by contrast, square to $+e_0$, so each plane $\operatorname{span}_\mathbb{R}\{e_0, ie_k\}$ with $k = 1,2,3$ is a copy of the **split complex numbers** $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$ inside the real algebra. The real view therefore exhibits, side by side, the quaternion subalgebra $\mathbb{H}_{\mathbb{B}} = \operatorname{span}_\mathbb{R}\{e_0,e_1,e_2,e_3\}$ with its units of square $-e_0$, three split-complex planes with generators of square $+e_0$, and the complex plane $\mathbb{C}_{\mathbb{B}} = \operatorname{span}_\mathbb{R}\{e_0, ie_0\}$ generated by an element of square $-e_0$. The sign difference between the two kinds of imaginary direction is stored here and nowhere else.

### The Conjugations Are Real-Linear

All four conjugations ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ and $\flat$ either fix or negate real scalars, so all four are $\mathbb{R}$-**linear** maps of the real algebra. Two of them change character when the scalars are enlarged: the bar and the star conjugate the complex coefficients and become $\mathbb{C}$-antilinear in the next section. Over $\mathbb{R}$ there is no such distinction to draw, and this is the view in which the four maps are simplest.

### The Central Imaginary as a Complex Structure

The central element $i$ defines a real-linear map

$$
J : \mathbb{B} \to \mathbb{B}, \qquad J(\tilde{Q}) = i\tilde{Q}, \qquad J^2 = -\mathrm{id},
$$

because $i^2 = -e_0$. A real algebra carrying a central element of square $-1$ carries a complex structure, and that is exactly how the complex view of the next section is obtained from this one.

## As an Algebra over $\mathbb{C}$

### The Complex Algebra Structure

**The structure map.** The assignment

$$
\varphi : \mathbb{C} \longrightarrow Z(\mathbb{B}), \qquad \varphi(z) = ze_0
$$

is a unital ring homomorphism with central image, and it gives the **complex scalar multiplication** $z\tilde{Q} = zQ_0e_0 + zQ_1e_1 + zQ_2e_2 + zQ_3e_3$, applied to the four complex coefficients. Because the image is central,

$$
z(\tilde{P}\tilde{Q}) = (z\tilde{P})\tilde{Q} = \tilde{P}(z\tilde{Q}), \qquad z \in \mathbb{C},
$$

so the product is $\mathbb{C}$-bilinear and $\mathbb{B}$ is a **$\mathbb{C}$-algebra**. This structure is finer than the real one. The field $\mathbb{R}$ sits inside $\mathbb{C}$, the two structure maps compose, every $\mathbb{C}$-linear map is $\mathbb{R}$-linear and not conversely, and the dimensions are related by

$$
\dim_\mathbb{R}\mathbb{B} = 2 \dim_\mathbb{C}\mathbb{B} = 8.
$$

**The gate, in elementary terms.** Giving a $\mathbb{C}$-algebra structure on a real algebra, compatible with its real structure, is the same thing as giving a **central element $j$ with $j^2 = -1$**, the scalar action being $(a + ib)x = ax + bjx$. Centrality is needed exactly at the product: with $j$ not central, the two expressions $(a+bj)(c+dj)$ and $(ac-bd) + (ad+bc)j$ differ by $bjc - bcj$. For $\mathbb{B}$ the element is $j = i$.

### The Complex Multiplication and Its Table

Over $\mathbb{C}$ the basis is $\{e_0, e_1, e_2, e_3\}$, the complex dimension is four, and the product is generated by

$$
e_0e_k = e_k, \qquad e_k^2 = -e_0, \qquad e_1e_2 = e_3, \quad e_2e_3 = e_1, \quad e_3e_1 = e_2, \qquad e_je_k = -e_ke_j \ (j \neq k).
$$

Compared with the real table, the relations $(ie_k)^2 = +e_0$ have vanished, because $i$ is no longer an element of the algebra but the scalar of the base ring: the square $ie_k \cdot ie_k$ is now computed as $i^2e_k^2 = e_0$ by pulling the scalars out of the product. The complex view is smaller for that same reason: half the generators of the real basis have been promoted to scalars.

### What the Complex View Buys

- **A field of scalars.** $\mathbb{C}$ is a field, so every module is free, every dimension is well defined, and left and right scalar multiplication coincide.
- **The two antilinear conjugations.** The bar and the star are $\mathbb{C}$-antilinear, which is what makes a sesquilinear form available alongside the bilinear one.
- **The centre is exactly the scalars.** No scalar is lost and no non-scalar is admitted. The next section puts that fact under scrutiny, because it is also the reason the quaternions cannot play the same role.

## As a Bimodule over $\mathbb{H}$

### The Two Actions

**Definition.** The **left and right $\mathbb{H}$-actions** on $\mathbb{B} = \mathbb{C} \otimes_\mathbb{R} \mathbb{H}$ are

$$
h \cdot (z \otimes h') = z \otimes hh', \qquad (z \otimes h') \cdot h = z \otimes h'h .
$$

The left action is left multiplication by $1 \otimes h$, the right action is right multiplication by the same element, and both are $\mathbb{R}$-bilinear. They **commute**,

$$
(h \cdot x) \cdot h' = z \otimes hh'h' = h \cdot (x \cdot h'),
$$

by associativity of the product, so $\mathbb{B}$ is an $\mathbb{H}$-**bimodule**.

### Free of Rank Two

In the quaternionic coordinates an element is $x = h_1 + ih_2$ with $h_1, h_2 \in \mathbb{H}$, and the two actions are

$$
h \cdot x = (hh_1) + i(hh_2), \qquad x \cdot h = (h_1h) + i(h_2h),
$$

using the centrality of $i$. The decomposition $x = h_1 + ih_2$ is unique, so $\{e_0, ie_0\}$ is a basis on the right and on the left at once:

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

### A Bimodule Is Not an Algebra over $\mathbb{H}$

The two actions give the quaternions a reach over $\mathbb{B}$ that is **not** the reach of a scalar field. Multiplication is left $\mathbb{H}$-linear in the first argument and right $\mathbb{H}$-linear in the second,

$$
(h \cdot x) \cdot y = h \cdot (x \cdot y), \qquad x \cdot (y \cdot h) = (x \cdot y) \cdot h,
$$

but it is **not** fully $\mathbb{H}$-bilinear, since for non-central $h$

$$
x \cdot (h \cdot y) - h \cdot (x \cdot y) = (xh - hx)y = [x,h]y,
$$

which does not vanish in general. A ring with exactly these properties is an **$\mathbb{H}$-ring**. The failure is measured by the commutator, and the quaternions are not central in $\mathbb{B}$; the next section is about why that matters.

## The Centre, and Which Base Rings Are Legitimate

The three views are not on the same footing. Two of them are **algebra** structures, over commutative rings; the third is a module structure. The criterion that separates them is the centrality of the structure map.

### The Centrality Condition

An $R$-algebra structure on a ring $A$ is a unital ring homomorphism $R \to Z(A)$, and two things are required of it: the map must exist, and its image must be central. The second requirement is not a technicality, since it is what makes the scalar multiplication $R$-bilinear, exactly as the elementary gate of the complex section demanded a *central* element of square $-1$. A non-commutative ring can serve as a base ring only if the map kills its non-commutativity, so only if it factors through the quotient by the two-sided ideal generated by the commutators. When the ring is simple, the way $\mathbb{H}$ and $\mathbb{B}$ are, that ideal is either $0$ or the whole ring, because a unital homomorphism out of a simple ring is injective and an image inside a commutative ring is commutative.

### The Centre Is $\mathbb{C}$

**Proposition.** The centre of $\mathbb{B}$ is $\mathbb{C}$, the complex line spanned by $e_0$ and $ie_0$:

$$
Z(\mathbb{B}) = \mathbb{C} \otimes_{\mathbb{R}} Z(\mathbb{H}) = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{R} = \mathbb{C} = \mathbb{C}_{\mathbb{B}}.
$$

**Proof.** The centre of a tensor product of algebras over a field is the tensor product of their centres, and $Z(\mathbb{C}) = \mathbb{C}$ while $Z(\mathbb{H}) = \mathbb{R}$. In coordinates, $[\tilde{Q}, e_1] = 2Q_3e_2 - 2Q_2e_3$ vanishes exactly when $Q_2 = Q_3 = 0$, and $[\tilde{Q}, e_2]$ vanishes exactly when $Q_1 = Q_3 = 0$, so centrality forces $Q_1 = Q_2 = Q_3 = 0$; conversely every $Q_0e_0$ is central because $i$ commutes with the units.

The centre is therefore the **same** $\mathbb{C}$ as the base ring of the complex view. The structure map $\varphi$ has image exactly the centre, and the scalars cannot be enlarged further, because there is no room in the centre for more.

### The Quaternion Factor Is Not Central

The canonical embedding

$$
\psi : \mathbb{H} \longrightarrow \mathbb{B}, \qquad \psi(h) = 1 \otimes h
$$

is an injective unital ring homomorphism, with image the quaternion subspace $\mathbb{H}_{\mathbb{B}}$. It is a homomorphism into the algebra but not into its centre: $\psi(e_2) = e_2$ fails to commute with $e_1$, since $e_1e_2 = -e_2e_1$. No other map can repair this, because no unital homomorphism $\mathbb{H} \to \mathbb{C}$ exists at all: such a map would be injective by simplicity, and $\mathbb{C}$ cannot contain a copy of the non-commutative ring $\mathbb{H}$. There is no map $\mathbb{H} \to Z(\mathbb{B})$ to serve as a structure map.

The same argument applies with $\mathbb{B}$ in place of $\mathbb{H}$: the identity map has image all of $\mathbb{B}$, which is not central.

### The Table

| base ring | is $\mathbb{B}$ an algebra over it? | reason |
|---|---|---|
| $\mathbb{R}$ | yes | $\mathbb{R} \subset \mathbb{C} = Z(\mathbb{B})$, so the image is central |
| $\mathbb{C}$ | yes | $z \mapsto ze_0$ lands on $Z(\mathbb{B}) = \mathbb{C}$ |
| $\mathbb{H}$ | no | $\mathbb{H}$ is non-commutative and simple, so no unital homomorphism $\mathbb{H} \to \mathbb{C}$ |
| $\mathbb{B}$ | no | the same obstruction, with the identity map in place of $\psi$ |

## Why the Base Ring Matters for the Forms

Bilinearity is meaningful only relative to a base ring, and the base ring fixes which conjugation may twist a form.

The **natural sign** ${}^{\natural}$ fixes the complex coefficients and negates the vector units, so it is $\mathbb{C}$-**linear**. A pairing built on it, such as the polarisation $B(\tilde{P}, \tilde{Q}) = \operatorname{Sc}(\tilde{P}\tilde{Q}^{\natural})$ of *Biquaternion Norm and Invertibility*, is therefore $\mathbb{C}$-**bilinear**, and its scalars may be moved out of either argument. The **star** ${}^{*} = \bar{\cdot} \circ {}^{\natural}$ conjugates the coefficients, so it is $\mathbb{C}$-**antilinear**; it is the involution with respect to which the trace form is Hermitian, which is what makes the inner product $\langle\tilde{P}, \tilde{Q}\rangle = \sum_\mu \bar{P}_\mu Q_\mu$ sesquilinear rather than bilinear, both forms being defined in *Biquaternion Algebra*.

Over $\mathbb{H}$ neither construction is available. The natural sign does not commute with the $\mathbb{H}$-action, the scalars cannot be pulled out of either argument, and the failure is the commutator identity of the bimodule section. To call a form "$\mathbb{H}$-bilinear" would be to require the $\mathbb{H}$-scalars to be central, so the phrase has no content for $\mathbb{B}$.

## The Other Structures Carried by the Same Set

| view of $\mathbb{B}$ | base | what is added | article |
|---|---|---|---|
| real algebra | $\mathbb{R}$ | eight real dimensions, the four real-linear conjugations | *Biquaternion Algebra* |
| complex algebra | $\mathbb{C}$ | four complex dimensions, the centre as scalars | *Biquaternion Algebra* |
| quaternionic bimodule | $\mathbb{H}$ | free of rank two on each side, no centrality | this article |
| six subspaces | $\mathbb{R}$ | the fixed and anti-fixed spaces of the conjugations | *Biquaternion Relations Between Subspaces* |

## Summary

The biquaternion algebra is one set of elements with three basic structures, taken in the order of the scalars they admit.

As an **$\mathbb{R}$-algebra** it has dimension eight, on the basis $e_0, e_1, e_2, e_3, ie_0, ie_1, ie_2, ie_3$, with $e_k^2 = -e_0$, with $(ie_0)^2 = -e_0$ and $(ie_k)^2 = +e_0$ for $k = 1,2,3$, and with central $i$. Its four conjugations are all real-linear, and the central element $i$ is a complex structure, $J^2 = -\mathrm{id}$.

As a **$\mathbb{C}$-algebra** it has dimension four, on the basis $e_0, e_1, e_2, e_3$, with $\mathbb{C}$-bilinear product. Its centre is $\mathbb{C}$, the scalars are exactly the centre, and the bar and the star are its antilinear conjugations.

As a **bimodule over $\mathbb{H}$** it is free of rank two on each side, on the generators $e_0$ and $ie_0$, with commuting left and right actions, with $\operatorname{End}_\mathbb{H}(\mathbb{B}) \cong M_2(\mathbb{H})$, and with an $\mathbb{H}$-ring multiplication that is left linear in the first argument and right linear in the second but not fully bilinear.

For $\mathbb{C}$ to be the base ring and $\mathbb{H}$ not to be, one fact is responsible, and it is the centre:

$$
Z(\mathbb{B}) = \mathbb{C} \otimes_{\mathbb{R}} Z(\mathbb{H}) = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{R} = \mathbb{C} = \mathbb{C}_{\mathbb{B}},
$$

the complex line spanned by $e_0$ and $ie_0$. The base ring must map into the centre, so $\mathbb{R}$ and $\mathbb{C}$ qualify and $\mathbb{H}$ does not, since no unital homomorphism $\mathbb{H} \to \mathbb{C}$ exists. The forms follow: the natural sign is $\mathbb{C}$-linear and gives the $\mathbb{C}$-bilinear polarisation, the star is $\mathbb{C}$-antilinear and gives the Hermitian inner product, and neither has an $\mathbb{H}$-analogue.

$$
\boxed{\ \text{The natural structure of the biquaternion algebra is an algebra over } \mathbb{C}.\ }
$$

The quaternions are present as a bimodule action and not as scalars, and the real algebra is the same object read with the larger scalar field restricted, not a different algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | biquaternion algebra |
| $e_0, e_1, e_2, e_3$ | complex basis; $e_0$ the unit, $e_k$ the quaternion units |
| $i$ | central scalar imaginary, $i^2 = -1$ |
| $q_\mu, q'_\mu$ | real coordinates, $Q_\mu = q_\mu + iq'_\mu$ |
| $h_1, h_2$ | quaternionic coordinates, $\tilde{Q} = h_1 + ih_2$ |
| $Z(A)$ | centre of the ring $A$, the elements commuting with every element of $A$ |
| $\mathbb{C}_{\mathbb{B}} = \mathbb{R}e_0 \oplus \mathbb{R}(ie_0)$ | centre of $\mathbb{B}$, the complex line, $= Z(\mathbb{B})$ |
| $\mathbb{H}_{\mathbb{B}} = \mathbb{R}e_0 + \cdots + \mathbb{R}e_3$ | quaternion subspace, the image of $\psi$ |
| $\varphi : \mathbb{C} \to \mathbb{B}$, $z \mapsto ze_0$ | the $\mathbb{C}$-algebra structure map, onto the centre |
| $\psi : \mathbb{H} \to \mathbb{B}$, $h \mapsto 1 \otimes h$ | the embedding of the quaternion factor, image not central |
| $J = L_i$ | the real-linear complex structure, $J^2 = -\mathrm{id}$ |
| $h \cdot x = z \otimes hh'$, $x \cdot h = z \otimes h'h$ | the left and right $\mathbb{H}$-actions |
| $\mathbb{B} \cong \mathbb{H}^2$ | free $\mathbb{H}$-module of rank two on each side, generators $e_0, ie_0$ |
| $\operatorname{End}_\mathbb{H}(\mathbb{B}) \cong M_2(\mathbb{H})$ | the $\mathbb{H}$-linear endomorphisms |
| $\mathbb{H}$-ring | bimodule over $\mathbb{H}$ with multiplication left linear in the first argument and right linear in the second |
| $x \cdot (h \cdot y) - h \cdot (x \cdot y) = [x,h]y$ | the failure of full $\mathbb{H}$-bilinearity |
| ${}^{\natural}$ | natural sign; $\mathbb{C}$-linear, the twist of the $\mathbb{C}$-bilinear polarisation |
| ${}^{*} = \bar{\cdot} \circ {}^{\natural}$ | star; $\mathbb{C}$-antilinear, the twist of the Hermitian inner product |

## Further Reading

- Nicolas Bourbaki, *Algebra I* (Springer, 1998), for the definition of an algebra over a ring and the centrality of the base ring.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for base change, the tensor product of algebras and the bimodule structure of an extension.
- Tsit Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for the centre of a tensor product, the simplicity of a division ring, and the impossibility of a unital homomorphism from a simple non-commutative ring into a commutative one.
