# __The Sandwich Action in Subspaces__

## Introduction

The Lorentz transformation of the corpus is the sandwich of a rotor, and the boosts live in the informational sector; the remarkable subspaces each produce their own kind of transformation, and this article answers, for each subspace in turn, what operator an element of it produces. The article *Biquaternion Rotations and Lorentz Transformations* makes a single element of the algebra act on the algebra by the sandwich

$$
\tilde S \longmapsto \tilde{Q}\,\tilde S\,\tilde{Q}^{*} ,
$$

reads it as the action of the group of units, and computes its kernel, its invariants and its action on the remarkable subspaces. This article restricts the **acting element** to one of the remarkable subspaces and records what the restriction does to the operator. It is the counterpart of *The Polar Element Representation in Subspaces*, which restricts the same remarkable subspaces in the other direction: there the question is which of the four polar factors a subspace can carry, here it is which operator an element of a subspace produces. The acting element keeps any biquaternion norm: the unit-norm slice, where the sandwich is the Lorentz action of *Biquaternion Rotations and Lorentz Transformations*, is recovered below as the special case in which the operator is an isometry, and off that slice the sandwich of a subspace element is a similarity.

The question is a physical one, and it has a physical answer. The Lorentz transformation of the corpus is written with a rotor, and for a pure boost that rotor lies in the Hermitian subspace $\mathbb{M}_+$, as *The Lorentz Transformation as a Biquaternionic Rotation* records: the boost biquaternion has a real scalar part and a purely imaginary vector part, so it is Hermitian and its sandwich collapses to $\tilde{U}\tilde{Q}\tilde{U}$. That rotor has unit norm, and the unit-norm condition is what makes the map an isometry; the general element of the sector acts by a similarity, which the section on the two sectors separates from the isometric case. The rotation lies in $\mathbb{H}_{\mathbb{B}}$, the home of the unit real quaternions; the phase lies in the centre; the four-vectors lie in $\mathbb{M}_-$. Each subspace therefore asks a separate question — what kind of transformation does an element of *this* subspace produce? — and the six questions are answered below and turn out to be four.

Three results organise the answer. The first is a **central invariance**: multiplying the acting element by a central scalar multiplies the sandwich by the squared modulus of that scalar. Because the scalar imaginary $i$ is central, the remarkable subspaces collapse to four **operator classes**: the centre, the vector subspace, the two halves together, and the two sectors together; an antiquaternion acts exactly as its real quaternion, and an element of the material sector acts exactly as the corresponding informational element. The second is that the operator's **type** is decided by the subspace in a sharp way: the centre gives the dilations, the vector subspace gives the similarities, the rotations by $\pi$ among them, the two halves give the rotations, and the two sectors give the similarities, which on the unit-norm slice are the Lorentz transformations: the boosts, and the boosts composed with a rotation by $\pi$ on the negative-norm branch. The third is the answer to the question the series puts to the Hermitian subspace: **the Lorentz transformation of the corpus is the sandwich of a unit-norm element of $\mathbb{M}_+$**, so the informational sector is the home of the boosts, and the material sector reaches the same family through the central imaginary.

The conventions are those of *Conventions in the Biquaternion Universe*, and the notation is that of *Biquaternion Rotations and Lorentz Transformations*: $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2 = \det\mathsf{M}_2(\tilde{Q})$; $\operatorname{H}_{\tilde{Q}}(\tilde S) = \tilde{Q}\tilde S\tilde{Q}^{*}$ is the sandwich, which is the map the series calls rotor conjugation when $\tilde{Q}$ has unit norm; a **rotor** is an element of unit norm, so that $\tilde{U}\tilde{U}^{\natural} = e_t$ and $\tilde{U}^{*} = \overline{\tilde{U}^{\natural}}$; $\tilde u$ is a unit real quaternion; and the remarkable subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion and antiquaternion subspaces $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, and the informational and material sectors $\mathbb{M}_+$ and $\mathbb{M}_-$.

## The Central Factor Leaves the Operator Alone

### The Rule

**Theorem.** Let $z\in\mathbb{C}^{\times}$ be central, $\tilde{Q}$ an element, and $\tilde S$ arbitrary. Then

$$
\operatorname{H}_{z\tilde{Q}}(\tilde S) = |z|^2\operatorname{H}_{\tilde{Q}}(\tilde S) .
$$

**Proof.** Since $z$ is central, $(z\tilde{Q})\tilde S(z\tilde{Q})^{*} = z\tilde{Q}\tilde S\tilde{Q}^{*}\bar{z} = |z|^2\tilde{Q}\tilde S\tilde{Q}^{*}$.

Two special cases are worth stating apart. For $z = i$ the scaling factor is $|i|^2 = 1$, so

$$
\operatorname{H}_{i\tilde{Q}} = \operatorname{H}_{\tilde{Q}} ,
$$

the sandwich is completely blind to the scalar imaginary; and for $z = -1$, which is central of modulus one, the operators of $\tilde{Q}$ and $-\tilde{Q}$ coincide, which is the usual two-fold redundancy of a rotor.

### Remarkable Subspaces Fall into Four Operator Classes

The scalar imaginary multiples act on the subspaces in a fixed way: multiplication by $i$ fixes the centre and the vector subspace, exchanges the quaternion and antiquaternion subspaces, and exchanges the two sectors. The theorem therefore says that a subspace and its image under multiplication by $i$ carry **the same operator element by element**: if $\tilde{Q}' = i\tilde{Q}$ then

$$
\operatorname{H}_{\tilde{Q}'} = \operatorname{H}_{\tilde{Q}} .
$$

The remarkable subspaces of the framework are thus cut into four **operator classes**, and a class is exactly an orbit of the pair of subspaces under multiplication by $i$:

| class | subspaces | the sandwich |
|---|---|---|
| $1$ | $\mathbb{C}_{\mathbb{B}}$ | the dilations by $|z|^2$ |
| $2$ | $\mathrm{Vect}(\mathbb{B})$ | the similarities of the interval, and the rotations by $\pi$ for the real vectors |
| $3$ | $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | the rotations, with a scalar factor off the unit-norm slice |
| $4$ | $\mathbb{M}_+$, $\mathbb{M}_-$ | the Lorentz transformations: the boosts, and the boosts composed with a rotation by $\pi$ for the negative-norm elements |

The four classes must not be confused with the four coordinate blocks of the polar article: the blocks are the intersections of the subspaces and cut them the other way, while the classes are unions of subspaces and are the smallest sets on which the operator is constant.

### The Kernel of the Operator

The kernel of the sandwich on the algebra is the central circle $\mathrm{U}(1)e_t$, of one real dimension, computed in *Biquaternion Rotations and Lorentz Transformations*, §*The Kernel on the Whole Algebra* and cited here, not reproved: the sandwich is blind to a central phase and to nothing else. Inside a class the central units are $\mathbb{C}^\times e_t$ on the centre, $\mathbb{R}^\times e_t$ on the two halves and on the informational sector, $i\mathbb{R}^\times e_t$ on the antiquaternion subspace and on the material sector, and none at all on the vector subspace, whose only central element is the zero element. On the unit-norm slice $N = 1$, which is where the rotors live, every class maps to its operators two to one, with fibre $\{\pm e_t\}$: that is the double cover, and it is invisible in the class as a whole, where the sandwich still distinguishes the moduli.

### The Operators Compose as the Elements Do

**Proposition.** For all units $\tilde{Q}, \tilde{R}$,

$$
\operatorname{H}_{\tilde{Q}\tilde{R}} = \operatorname{H}_{\tilde{Q}}\circ\operatorname{H}_{\tilde{R}} .
$$

**Proof.** $\operatorname{H}_{\tilde{Q}\tilde{R}}(\tilde S) = \tilde{Q}\tilde{R}\tilde S\tilde{R}^{*}\tilde{Q}^{*} = \operatorname{H}_{\tilde{Q}}\!\left(\operatorname{H}_{\tilde{R}}(\tilde S)\right)$.

The identity is the statement that the sandwich is an action of the group of units, not merely a collection of linear maps: the individual maps are not algebra automorphisms, but they compose as their elements do. The case of rotors is stated in *Biquaternion Rotations and Lorentz Transformations*, §*Composition of Operators*; the identity holds for every unit, which is what the subspace interpretation needs. It is the tool that decomposes an operator whose element is a product, and it is used twice below.

## The Centre: the Operator of a Complex Scalar

### The Element and Its Operator

Let $\tilde{Q} = ze_0$ with $z = r\exp(i\alpha)\neq 0$; the biquaternion norm is $\langle\tilde{Q}\rangle_{\natural} = z^2$, of modulus $r^2$. The sandwich of a central element is the dilation

$$
\operatorname{H}_{ze_0}(\tilde S) = |z|^2\tilde S = r^2\tilde S .
$$

The centre therefore contributes to the operator nothing but a dilation of the whole algebra by the modulus of the biquaternion norm, and on the unit-modulus slice $|z| = 1$ it contributes the identity. In the language of the classes, the centre is a class whose operator is a dilation by the squared modulus of the element, trivial on the unit circle of the class.

### Why This Is the Right Reading

The result is the operator form of a fact about the polar representation: the two factors of a polar element that lie in the centre are the scale $r$ and the phase $\exp(i\alpha)$, and a dilation by $r^2$ is the only trace of them that an operator can carry. The sandwich carries the modulus but not the argument, since $|z|^2$ distinguishes $z$ from $\bar{z}$, from $-z$ and from $\exp(i\alpha)z$. In the four-factor polar language the centre is the class in which the boost factor and the rotor are both trivial, and the operator statement is that the surviving datum is the modulus, once, squared.

**Example.** Take $z = 3 + 2i$, of modulus $\sqrt{13}$ and biquaternion norm $N = (3+2i)^2 = 5 + 12i$ of modulus $13$. Then $\operatorname{H}_{ze_0}(\tilde S) = 13\tilde S$ on every element, so $N\!\left(\operatorname{H}_{ze_0}(\tilde S)\right) = 169\langle\tilde S\rangle_{\natural} = \langle\tilde S,\tilde S\rangle_{\natural} = |\langle\tilde{Q}\rangle_{\natural}|^2\langle\tilde S\rangle_{\natural}$, in agreement with the scaling of the biquaternion norm.

## The Vector Subspace: the Similarities

### A Vector Has a Central Square

An element of the vector subspace is $\tilde{Q} = \vec v = v_1\vec e_x + v_2\vec e_y + v_3\vec e_z$ with complex coefficients; equivalently $\operatorname{Sc}\tilde{Q} = 0$. Writing a general element as $\tilde{Q} = ae_0 + \vec v$ with $a$ complex, its square is

$$
\tilde{Q}^2 = \left(a^2 - \vec v\cdot\vec v\right)e_t + 2a\vec v ,
$$

where $\vec v\cdot\vec v = v_1^2+v_2^2+v_3^2 = \langle \vec v\rangle_{\natural}$ is the biquaternion norm of the vector part. The square is central exactly when the vector part of the square vanishes, that is when $a\vec v = 0$.

**Proposition.** $\tilde{Q}^2$ is central if and only if $\tilde{Q}$ lies in the centre or in the vector subspace.

*Proof.* If $a = 0$ or $\vec v = 0$ the displayed square is central. Conversely if $2a\vec v = 0$ with $\tilde{Q}$ not central, then $\vec v\neq 0$ and $a = 0$.

For an element of the vector subspace the square is therefore central and computable in closed form: the products $e_je_k$ with $j\neq k$ cancel in pairs because they anticommute, so $\vec v^2 = -\langle \vec v\rangle_{\natural}e_t$ and

$$
\vec v^2 = -\langle \vec v\rangle_{\natural}\,e_t .
$$

### A Real Vector Acts as the Rotation by $\pi$ About Itself

Let $\vec u$ be a real unit vector, so that $\vec u^2 = -e_t$, $\langle \vec u\rangle_{\natural} = 1$, and $\vec u^{*} = -\vec u$. The sandwich of a real unit vector is therefore a sandwich with a sign,

$$
\operatorname{H}_{\vec u}(\tilde S) = \vec u\,\tilde S\,\vec u^{*} = -\vec u\,\tilde S\,\vec u ,
$$

and the map is the rotation by $\pi$ about $\vec u$: it fixes $e_t$ and $\vec u$, negates the two-dimensional plane orthogonal to $\vec u$, and because $i$ is central it does the same on the imaginary vector part. In particular it preserves each of the remarkable subspaces, and it is an element of the rotation group $SO(3)$ of order two.

**Example.** For $\vec u = \vec e_x$ the operator acts on the basis by

| $\tilde S$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ | $ie_0$ | $ie_1$ | $ie_2$ | $ie_3$ |
|---|---|---|---|---|---|---|---|---|
| $\operatorname{H}_{\vec e_x}(\tilde S)$ | $e_t$ | $\vec e_x$ | $-\vec e_y$ | $-\vec e_z$ | $ie_0$ | $ie_1$ | $-ie_2$ | $-ie_3$ |

which is the rotation through $\pi$ about $\vec e_x$, as the polar article's interpretation of the vector subspace — the rotor is a unit vector in the plane of the element — leads one to expect. The real unit vectors therefore realise the rotations by $\pi$ and nothing else, and they are the elements whose operators are the most nearly faithful of the family.

### The Sandwich of a Vector Is a Similarity

The sandwich of a vector scales the interval. For $\tilde{Q} = \vec v$ the biquaternion-norm relation gives

$$
N\!\left(\operatorname{H}_{\vec v}(\tilde S)\right) = |\langle \vec v\rangle_{\natural}|^2\langle\tilde S\rangle_{\natural} ,
$$

so a vector preserves the causal type of every element and rescales the interval by one positive factor; on the unit-norm vectors the factor is one and the map is an isometry. The Hermitian element that measures the scaling is $\vec v\vec v^{*}$, computable from the cross product of the coefficient vector and its conjugate,

$$
\vec v\,\vec v^{*} = |\vec v|^2e_t - \vec v\times\vec v^{*} , \qquad |\vec v|^2 = |v_1|^2+|v_2|^2+|v_3|^2 ,
$$

where $|\vec v|^2$ is the Euclidean norm squared and $\vec v\times\vec v^{*}$ is the cross product of the coefficient triple with its complex conjugate. That cross product is purely imaginary in each coordinate, so $\vec v\vec v^{*}$ is an element of the informational sector; it is central exactly when the three coefficients share a common complex factor, $\vec v = c\,\vec w$ with $c\in\mathbb{C}$ and $\vec w$ real, and then the operator of the complex vector is the operator of the real direction multiplied by the biquaternion norm,

$$
\operatorname{H}_{\vec v} = |\vec v|^2\operatorname{H}_{\vec u_w} , \qquad \vec u_w = \vec w/|\vec w| .
$$

### The Unit-Norm Vectors Are Rotors of a Mixed Type

A vector of unit norm, $\langle \vec v\rangle_{\natural} = 1$, is an element of the Lorentz group, so its sandwich, read on the material sector, lies in $O(1,3)$: it preserves the two sectors and scales the biquaternion norm by $|N|^2 = 1$, and the family of unit-norm vectors is connected and contains the real unit vectors, whose operators are the rotations by $\pi$, so the induced map on the material sector lies in the identity component $SO^+(1,3)$. It is not in general a pure boost: a complex vector acts as a boost composed with the rotation by $\pi$ about its own direction, a composition that the section on the sectors returns to. The computation is instructive:

**Example.** Take $\vec v = a\,\vec e_x + b\,\vec e_y$ with $a = 0.6 + 0.5i$ and $b = \sqrt{1-a^2} = 0.99079746 - 0.30278640\,i$, so that $\langle \vec v\rangle_{\natural} = 1$. Then

$$
\operatorname{H}_{\vec v}(ie_0) = 1.683359\,ie_0 + 1.354141\,\vec e_z , \qquad \operatorname{H}_{\vec v}(\vec e_x) = -0.463359\,\vec e_x + 0.886171\,\vec e_y .
$$

The time axis stays in the cone, the transverse plane stays in the material sector, and the biquaternion norm is the unit one: the operator is a Lorentz transformation, with a boost part of rapidity $\operatorname{arcosh}1.683359 = 1.111035$ and a rotation part. The element is a rotor of unit norm, and its operator is not a pure boost.

### The Imaginary Vectors Give the Same Operators

For $\vec v$ in the vector subspace the element $i\vec v$ is again in the vector subspace, and by the central rule the two elements have the same operator. The traceless Hermitian elements $i\vec w$ with $\vec w$ a real vector, which are the vector-subspace part of the informational sector, therefore act exactly as the real vectors $\vec w$, and in particular a unit imaginary vector $i\vec u$ acts as the rotation by $\pi$ about $\vec u$ even though its element is Hermitian. This is the first appearance of a phenomenon that the two sectors will show again: the sector label of an element does not fix the type of its operator.

## The Two Halves: the Rotations

### The Quaternion Subspace

Let $\tilde{R}$ be a real quaternion, $\tilde{R} = a_0e_t + a_1\vec e_x+a_2\vec e_y+a_3\vec e_z$ with real coefficients. Its Hermitian conjugate is its quaternion conjugate, $\tilde{R}^{*} = \tilde{R}^{\natural} = |\tilde{R}|^2\tilde{R}^{-1}$, with $\langle\tilde{R}\rangle_{\natural} = \langle\tilde{R},\tilde{R}\rangle_{\natural} = |\tilde{R}|^2$ a positive real, so the central rule gives

$$
\operatorname{H}_{\tilde{R}}(\tilde S) = \tilde{R}\,\tilde S\,\tilde{R}^{\natural} = |\tilde{R}|^2\,\operatorname{H}_{\tilde u}(\tilde S) , \qquad \tilde u = \tilde{R}/|\tilde{R}| .
$$

A real quaternion therefore acts as the dilation by its squared modulus composed with the rotation of the unit quaternion of the same direction, and on the unit-norm slice it is the familiar rotation. Writing $\tilde{R} = |\tilde{R}|(\cos\theta + \sin\theta\,\vec u)$ with $\vec u$ a real unit vector,

$$
\operatorname{H}_{\tilde{R}}(\vec v) = |\tilde{R}|^2\Bigl(\vec v\cos2\theta + (\vec u\times\vec v)\sin2\theta + \vec u\,(\vec u\cdot\vec v)(1-\cos2\theta)\Bigr) ,
$$

which is the rotation of the real vector part through $2\theta$ about $\vec u$, scaled by $|\tilde{R}|^2$. The operator preserves all remarkable subspaces, and the kernel on the unit-norm slice is $\{\pm e_t\}$, so the map

$$
\mathrm{Sp}(1)\longrightarrow SO(3) , \qquad \tilde u\longmapsto\operatorname{H}_{\tilde u} ,
$$

is the two-fold cover of the rotation group. The doubling of the angle is the doubling recorded in *Biquaternion Rotations and Lorentz Transformations*; what the subspace adds is that on $\mathbb{H}_{\mathbb{B}}$ the sandwich acts as a rotation of the whole algebra, leaving the centre, the vector subspace and the two sectors in place.

### The Antiquaternion Subspace Gives the Same Operators

Let $\tilde{Q} = i\tilde{R}$ with $\tilde{R}$ a real quaternion, the general element of the antiquaternion subspace. Since $i$ is central, the operator is that of $\tilde{R}$:

$$
\operatorname{H}_{i\tilde{R}} = \operatorname{H}_{\tilde{R}} .
$$

The antiquaternion subspace therefore contributes no operator that the quaternion subspace does not already contribute, and the two halves are two ways of writing one family of rotations — the operator statement of the polar article's finding that the antiquaternion carries the same rotor with the phase frozen at $\pi/2$. Each half covers the rotation group twice, since the two signs are identified, and the two halves produce the same operators, so the union of the halves covers the rotation group four times over.

### Where the Rotations Sit

The rotations form the three real parameters of the operator group that preserve the whole subspace structure, the subgroup $SU(2)/\{\pm e_t\}\cong SO(3)$ of *Biquaternion Rotations and Lorentz Transformations*; the other three parameters are the boosts, and the sections that follow place them in the two sectors. The half-angle is carried by the element and the full angle by the operator, so the element is a spinor and never the operator itself; the worked examples below exhibit the doubling on $\cos(\pi/6)e_t + \sin(\pi/6)\vec e_z$, whose operator is the rotation through $\pi/3$.

## The Two Sectors: Similarities and the Unit-Norm Lorentz Transformation

The two sectors are the fixed spaces of the dagger, so the sandwich of an element of a sector is a similarity of the interval: it preserves the causal type of every element and rescales the biquaternion norm by $|\langle\tilde{Q}\rangle_{\natural}|^2$, which is one exactly on the unit-norm slice. Two families must therefore not be confused here. The **similarities** are what a general Hermitian element produces, and they carry a dilation; the **Lorentz transformations** are the unit-norm slice of that family, and they are the object of the Lorentzian formalism of the corpus. The rest of this section works the unit-norm case, which is the one the series uses, and records the negative-norm branch that reaches the rotations by $\pi$.

### The Informational Sector: the Unit-Norm Boost

Let $\tilde{Q}$ be a Hermitian element of unit norm, $\tilde{Q} = \tilde{Q}^{*}$, $\langle\tilde{Q}\rangle_{\natural} = 1$. Its matrix image is Hermitian of determinant one, so its eigenvalues are $\lambda$ and $\lambda^{-1}$ with $\lambda$ real and nonzero; when both are positive the element is the boost rotor

$$
\tilde{U} = \cosh\frac{\psi}{2}\,e_t + i\sinh\frac{\psi}{2}\,\vec u , \qquad \tanh\psi = \frac{v_b}{c} ,
$$

and when both are negative it is $-\tilde{U}$ with the same operator. Since $\tilde{U}$ is Hermitian, its sandwich has the element on both sides of the argument,

$$
\operatorname{H}_{\tilde{U}}(\tilde{Q}) = \tilde{U}\,\tilde{Q}\,\tilde{U} ,
$$

which is the form in which *The Lorentz Transformation as a Biquaternionic Rotation* writes the boost. This is the sharpest answer to the question the article started from: **the Lorentz transformation of the corpus is the sandwich of a unit-norm element of the informational sector**, with no rotation part, and the element is Hermitian, so no inverse appears in it. The unit-norm condition is what makes the similarity an isometry and the boost a Lorentz transformation. Its action on a four-position is the boost relation, and the kernel on the class is the two central signs, so the boost family is three-dimensional — the hyperbolic three-space of the rapidity vector — and the map from the class to the boosts is two to one.

**Example.** Take $\beta = 0.6$ along $\vec e_z$, that is $\psi = \operatorname{artanh}0.6$, with

$$
\tilde{U} = 1.060660172\,e_t + 0.353553391\,i\,\vec e_z , \qquad \langle\tilde{U}\rangle_{\natural} = \cosh^2\frac{\psi}{2}-\sinh^2\frac{\psi}{2} = 1 ,
$$

and the four-position $\tilde{Q} = icte_0 + 0.6ct\,\vec e_z$ of a world line of velocity $0.6c$, at $ct = 1$. Then

$$
\operatorname{H}_{\tilde{U}}(\tilde{Q}) = \tilde{U}\tilde{Q}\tilde{U} = 0.8\,ie_0 ,
$$

the four-position in the rest frame, with $ct' = 0.8 = \sqrt{1-0.6^2}$ and $z' = 0$. The boost formula of the corpus, $ct' = ct\cosh\psi - z\sinh\psi$ and $z' = z\cosh\psi - ct\sinh\psi$, is the same computation in components, and the element of the informational sector is the operator that performs it.

### The Negative-Norm Branch of the Sector

The unit-modulus Hermitian elements with $\langle\tilde{Q}\rangle_{\natural} = -1$ do not have both eigenvalues positive, and they are not boost rotors; they are nevertheless Lorentz operators, and their structure is worth one computation. Write

$$
\tilde{Q} = \sinh\varphi\,e_t + i\cosh\varphi\,\vec u , \qquad \langle\tilde{Q}\rangle_{\natural} = \sinh^2\varphi - \cosh^2\varphi = -1 ,
$$

with $\vec u$ a real unit vector. Then the product of $\tilde{Q}$ with the boost rotor $\tilde{U} = \cosh\varphi\,e_t + i\sinh\varphi\,\vec u$ and with the unit real vector $\vec u$ is

$$
\tilde{U}\,\vec u = \cosh\varphi\,\vec u + i\sinh\varphi\,\vec u^2 = \cosh\varphi\,\vec u - i\sinh\varphi\,e_t = -i\tilde{Q} ,
\qquad \tilde{Q} = i\,\tilde{U}\,\vec u ,
$$

so by the central rule and the composition lemma

$$
\operatorname{H}_{\tilde{Q}} = \operatorname{H}_{\tilde{U}\vec u} = \operatorname{H}_{\tilde{U}}\circ\operatorname{H}_{\vec u} ,
$$

a boost composed with the rotation by $\pi$ about $\vec u$. At $\varphi = 0$ the element is the traceless $i\vec u$ of the vector subspace and the boost factor is the identity, so the family is connected to the rotations by $\pi$; at every $\varphi$ the operator is orthochronous and proper, and the sign of the biquaternion norm decides whether the rotation by $\pi$ is present.

**Example.** For $\tilde{Q} = \sqrt{3}\,e_t + 2i\,\vec e_z$, which is Hermitian with $\langle\tilde{Q}\rangle_{\natural} = 3-4 = -1$, the same data are $\vec u = \vec e_z$, $\cosh\varphi = 2$, $\sinh\varphi = \sqrt3$, the boost rotor $\tilde{U} = 2e_t + i\sqrt3\,\vec e_z$ of rapidity $\operatorname{arcosh}7 = 2.633915794$, and

$$
\operatorname{H}_{\tilde{Q}}(ie_0) = 7\,ie_0 - 4\sqrt3\,\vec e_z = 7\,ie_0 - 6.928203\,\vec e_z , \qquad \tilde{U}\vec e_z = -i\tilde{Q} ,
$$

so that $\operatorname{H}_{\tilde{Q}} = \operatorname{H}_{\tilde{U}}\circ\operatorname{H}_{\vec e_z}$: the transverse plane is negated and the time axis is carried to the four-velocity of rapidity $\operatorname{arcosh}7$. The example is the exact statement that a Hermitian element of negative biquaternion norm acts as a Lorentz operator with a rotation part, not as a boost.

### The Material Sector Gives the Same Operators

Let $\tilde{Q}$ be an element of the material sector, $\tilde{Q}^{*} = -\tilde{Q}$, so that $\tilde{Q} = ict\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$. By the central rule with $z = i$,

$$
\operatorname{H}_{\tilde{Q}} = \operatorname{H}_{i\tilde{Q}} , \qquad i\tilde{Q}\in\mathbb{M}_+ ,
$$

so the sandwich of a four-vector is the sandwich of the informational element $i\tilde{Q}$, and the material sector adds no operator family: the boosts, the rotations by $\pi$, and their compositions are already all present in the informational sector. The interpretation is the one the corpus uses everywhere: the same Lorentz transformation can be written with a Hermitian form, which is the informational interpretation, and with a four-vector, which is the material interpretation; the traceless Hermitian elements $i\vec u$ correspond exactly to the unit spacelike four-vectors $-\vec u$ and act as the rotations by $\pi$.

**Example.** The element of the previous example, $\tilde{Q} = \sqrt3\,e_t + 2i\,\vec e_z$, has $i\tilde{Q} = \sqrt3\,ie_0 - 2\vec e_z$, a four-vector of biquaternion norm $N = -3+4 = 1$, that is, a unit spacelike four-vector; and $\operatorname{H}_{i\tilde{Q}}(ie_0) = 7ie_0 - 4\sqrt3\vec e_z$ with the same right-hand side, so the two interpretations agree element by element, as the central rule requires.

## The Operator Dictionary

The remarkable subspaces, the operator each produces, and the subspace's own interpretation, in one table. The kernel column records the kernel of the operator inside the class; on the unit-norm slice it reduces to the fibre $\{\pm e_t\}$ in every class.

| subspace | acting element | the sandwich | kernel inside the class | the subspace's role |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $ze_0$ | dilation by $|z|^2$ | $\mathrm{U}(1)e_t$ | the scale and the phase |
| $\mathrm{Vect}(\mathbb{B})$ | $\vec v$, $\vec v^2 = -\langle \vec v\rangle_{\natural}e_t$ | a similarity of the interval; the rotation by $\pi$ for a real unit $\vec v$ | none | the free phase of the polar form |
| $\mathbb{H}_{\mathbb{B}}$ | $\tilde{R}$ real | $|\tilde{R}|^2$ times the rotation through $2\theta$ | $\mathbb{R}^\times e_t$ | the rotor |
| $i\mathbb{H}_{\mathbb{B}}$ | $i\tilde{R}$ | the same rotation | $i\mathbb{R}^\times e_t$ | the same rotor, phase frozen |
| $\mathbb{M}_+$ | Hermitian $\tilde{Q}$ | the boost for $N = 1$ positive definite; boost times rotation by $\pi$ for $N = -1$ | $\mathbb{R}^\times e_t$ | the Lorentz transformation |
| $\mathbb{M}_-$ | $\tilde{Q} = ict\,e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ | the same family as $\mathbb{M}_+$, through $i\tilde{Q}$ | $i\mathbb{R}^\times e_t$ | the four-vectors |

## Comparison with the Polar Representation in Subspaces

The two articles restrict the same remarkable subspaces, and the comparison is a dictionary between the two restrictions. The polar article asks which of the four factors $r$, $\exp(i\alpha)$, $B$ and $\tilde u$ a subspace can carry; this article asks which operator an element of the subspace produces. The answers pair up: the centre is the home of the scale and the phase, and its operator is trivial; the vector subspace is the only one that carries the phase freely together with a nontrivial boost and rotor, and its conjugation operator is the involution; the two halves carry the rotor alone, and their operator is the rotation; the two sectors carry the boost, and their sandwich is the boost on the unit-norm slice and a similarity off it. In each case the factor that a subspace is able to carry is the factor that turns into the operator: the rotor into the rotation, the boost into the boost, and the scale and the phase into nothing at all, since they lie in the centre and the centre is the kernel.

The comparison also explains an asymmetry of this article. The polar representation loses factors when the element is restricted, and the loss is one-sided: a subspace is unable to carry a factor. The operator interpretation loses **operators** when the acting element is restricted, and the loss goes the other way: the remarkable subspaces produce only four operator classes, and inside a class they produce the same operator element by element. The two directions of restriction are the two halves of the same statement about the algebra, and the central circle, which is the kernel of the operator, is what makes them differ.

**The operator factorises through the boost and the rotor, and doubles their parameters.** With the polar word $\tilde{Q} = r\exp(i\alpha)B\tilde u$ and $\tilde{U} = B\tilde u$ of unit norm,

$$
\operatorname{H}_{\tilde{Q}} = r^{2}\,\operatorname{H}_{\tilde{U}},
$$

because the Hermitian conjugates of the four factors are $\tilde u^{*} = \tilde u^{-1}$, $B^{*} = B$, $r^{*} = r$ and $(\exp(i\alpha))^{*} = \exp(-i\alpha)$, so the two central factors cancel against their inverses. A non-central factor occurs once on each side, so its parameter is deposited twice: the rotor of angle $\theta$ acts by the doubled angle, and the boost of rapidity $\psi$ acts by the doubled rapidity, as the diagonal case $\mathsf{M}_2(B) = \operatorname{diag}(\exp(\psi/2),\exp(-\psi/2))$ shows explicitly, the operator storing the half-rapidity and producing the rapidity. The four factors and their range are *The Polar Element Representation of Biquaternions* and *The Polar Element Representation in Subspaces*.

## Worked Examples

### A Central Element

$\tilde{Q} = (3+2i)e_t$: $\operatorname{H}_{\tilde{Q}}(\tilde S) = 13\tilde S$, the dilation by the modulus of the biquaternion norm; the class contributes no other operator.

### A Real Unit Vector

$\vec u = \vec e_x$: the sandwich acts as the rotation by $\pi$ about $\vec e_x$, with $\vec e_y\mapsto-\vec e_y$, $\vec e_z\mapsto-\vec e_z$, $ie_2\mapsto-ie_2$, $ie_3\mapsto-ie_3$, and $e_t$, $\vec e_x$, $ie_0$, $ie_1$ fixed. The operator is an involution and preserves all remarkable subspaces.

### An Imaginary Unit Vector

$i\vec u = ie_1$: the same operator as $\vec e_x$, by the central rule, so a Hermitian element of the informational sector acts as a rotation by $\pi$; the sector label does not fix the type of the operator.

### A Unit Quaternion

$\tilde{R} = \cos\frac{\pi}{6}e_t + \sin\frac{\pi}{6}\vec e_z$: the sandwich gives $\operatorname{H}_{\tilde{R}}(\vec e_x) = \frac12\vec e_x + \frac{\sqrt3}{2}\vec e_y$, the rotation through $\pi/3$ about $\vec e_z$, which is twice the angle $\pi/6$ in the element. The kernel is $\{\pm e_t\}$.

### A Central Real Quaternion

$\tilde{R} = 2e_t$: the element is central, so $\operatorname{H}_{\tilde{R}} = 4\,\mathrm{id}$; the example shows that the scalar of a real quaternion is the dilation $|\tilde{R}|^2$ of its operator, and that it disappears on the unit-norm slice.

### A Boost Rotor

$\beta = 0.6$, $\tilde{U} = 1.060660172e_t + 0.353553391ie_3$: $\operatorname{H}_{\tilde{U}}(ie_0+0.6\vec e_z) = 0.8ie_0$, the rest-frame four-position, and the time axis of the moving world line is carried to the rest frame.

### A Hermitian Element of Negative Biquaternion Norm

$\tilde{Q} = \sqrt3e_t+2ie_3$: $\operatorname{H}_{\tilde{Q}}(ie_0) = 7ie_0 - 4\sqrt3\vec e_z$, and $\operatorname{H}_{\tilde{Q}} = \operatorname{H}_{\tilde{U}}\circ\operatorname{H}_{\vec e_z}$ with $\tilde{U} = 2e_t+i\sqrt3\vec e_z$ of rapidity $\operatorname{arcosh}7 = 2.633915794$; the operator is a boost with a rotation by $\pi$, not a pure boost.

### A Unit Spacelike Four-Vector

$i\tilde{Q} = \sqrt3ie_0 - 2\vec e_z$, of biquaternion norm $1$: the same operators as $\tilde{Q}$, with $\operatorname{H}_{i\tilde{Q}}(ie_0) = 7ie_0-4\sqrt3\vec e_z$, which is the material-sector interpretation of the previous example.

## Physical Readings

The sandwich reads as an isometry of the form of each subspace, and the article's own interpretation is that one map gives one symmetry per subspace. Read on the split, the sandwich is the reason a change of frame cannot mix the material and the informational data: the acting element keeps the grading, so the relativity of the frame and the sharpness of the split are compatible (*The Material-Informational Split as a Superselection Structure in Biquaternionic Form*). Read on the clock, the unit-norm slice of the sandwich is the group that moves the ledger and does not move the phase, which is why the temporal interpretation of the exchange and the transformation theory of the material sector are separate.

## Summary

The sandwich, restricted to the remarkable subspaces, produces four operator classes, because a central factor multiplies the sandwich by the squared modulus of its scalar: the scalar imaginary identifies the two halves and the two sectors, so an antiquaternion acts as its real quaternion and a four-vector acts as the informational element $i$ times it.

The **centre** contributes only the dilations by the squared modulus of the biquaternion norm. The **vector subspace** contributes the similarities of the interval: an element of the vector subspace has a central square, $\vec v^2 = -\langle \vec v\rangle_{\natural}e_t$, and the sandwich preserves the causal type of every element while rescaling the interval by $|\langle \vec v\rangle_{\natural}|^2$; a real unit vector acts as the rotation by $\pi$ about itself and preserves all remarkable subspaces, a general unit-norm vector acts on the four-vectors as a boost composed with that rotation, and the Hermitian factor of the scaling is $\vec v\vec v^{*} = |\vec v|^2e_t - \vec v\times\vec v^{*}$. The **two halves** contribute the rotations: a real quaternion acts as $|\tilde{R}|^2$ times the rotation through twice its half-angle, the two equal on the unit-norm slice, with kernel $\{\pm e_t\}$ and the two-fold cover of $SO(3)$, and the two halves give the same operators. The **two sectors** contribute the similarities, whose unit-norm slice carries the Lorentz transformations: the sandwich of a Hermitian element of unit norm is the boost, written with the element on both sides, and it is the Lorentz transformation of the corpus, while a general element of the sector adds a dilation by $|\langle\tilde{Q}\rangle_{\natural}|^2$; the sandwich of a four-vector is the same family through the central imaginary; and the sign of the biquaternion norm decides whether the operator carries a rotation by $\pi$, since the negative-norm Hermitian elements are $\tilde{Q} = i\tilde{U}\vec u$ and act as a boost composed with the rotation by $\pi$ about $\vec u$.

The type of the operator is therefore decided by the class of the acting element and, inside a class, by the element's biquaternion norm: the centre dilates, the vector subspace and the halves transform isometrically or almost so, and the sectors carry the Lorentz transformations on the unit-norm slice and the similarities off it.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\operatorname{H}_{\tilde{Q}}(\tilde S) = \tilde{Q}\tilde S\tilde{Q}^{*}$ | the sandwich, rotor conjugation for a rotor |
| $\operatorname{H}_{z\tilde{Q}} = |z|^2\operatorname{H}_{\tilde{Q}}$ | the central rule, $z$ central |
| $\operatorname{H}_{\tilde{Q}\tilde{R}} = \operatorname{H}_{\tilde{Q}}\circ\operatorname{H}_{\tilde{R}}$ | the composition law |
| $\mathbb{C}_{\mathbb{B}}$ | the centre, of elements $ze_0$ |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, $\operatorname{Sc}\tilde{Q} = 0$ |
| $\vec v^2 = -\langle \vec v\rangle_{\natural}e_t$ | the central square of a vector |
| $\vec v\vec v^{*} = \|\vec v\|^2e_t - \vec v\times\vec v^{*}$ | the Hermitian element of a vector |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | the quaternion and antiquaternion subspaces |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | the informational and material sectors |
| $\tilde{U} = \cosh\frac{\psi}{2}e_t + i\sinh\frac{\psi}{2}\vec u$ | the boost rotor, Hermitian and of unit norm |
| $\tilde u = \cos\theta+\sin\theta\,\vec u$ | the rotation rotor, a unit real quaternion |
| $\tilde{Q} = \sinh\varphi\,e_t + i\cosh\varphi\,\vec u$, $N = -1$ | the negative-norm branch of the informational sector, $= i\tilde{U}\vec u$ |
| $SO^+(1,3)$, $SO(3)$ | the Lorentz group and the rotation group reached by the sandwich |
| $\langle\tilde{P},\tilde{Q}\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\langle\tilde{Q}\rangle_{\natural}$ |
| $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ |
| $\langle\tilde{P},\tilde{Q}\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{P}\tilde{Q})$ |

## Further Reading

- *Biquaternion Rotations and Lorentz Transformations* (`articles_physics/biquaternion-rotations-and-lorentz-transformations.md`), immediately before the present article in the menu, for the sandwich unrestricted, its kernel, its action on the remarkable subspaces and its composition law
- *The Polar Element Representation in Subspaces* (`articles_physics/the-polar-element-representation-in-subspaces.md`), for the same remarkable subspaces restricted in the other direction, to the four factors of one element
- *Relations Between Subspaces* (`articles_physics/relations-between-subspaces.md`), for the remarkable subspaces, their definitions, their intersections and the four coordinate blocks
- *The Lorentz Transformation as a Biquaternionic Rotation* (`articles_physics/the-lorentz-transformation-as-a-biquaternionic-rotation.md`), for the boost biquaternion in the informational sector and the sandwich with the element on both sides
- *The Lorentz Group as Biquaternion Norm Automorphisms* (`articles_physics/the-lorentz-group-as-biquaternion-norm-automorphisms.md`), for the unit-norm rotors, the homomorphism onto the Lorentz group and its kernel
- *The Lorentz Group in Biquaternionic Form — Structure and Representations* (`articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.md`), for the boosts, the rotations and the Thomas–Wigner rotation the composition lemma produces
- *Other Remarkable Subspaces* (`articles_physics/other-remarkable-subspaces.md`), for the centre, the vector subspace, the quaternion and the anti-quaternion subspace: their dimensions over the reals and over the complex numbers and the coordinates each carries
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* (`articles_physics/the-hermitian-subspace-m-plus-as-the-informational-sector.md`), for the sector that carries the boosts and the Hermitian forms
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* (`articles_physics/the-anti-hermitian-subspace-m-as-the-material-sector.md`), for the sector that carries the four-vectors
- *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_physics/the-2x2-matrix-element-representation-m2c-of-biquaternions.md`), for the matrix image of the sandwich as a similarity
- *Conventions in the Biquaternion Universe* (`articles_physics/conventions-in-the-biquaternion-universe.md`), for the conventions used throughout
- *Introduction to the Biquaternion Universe* (`articles_physics/introduction-to-the-biquaternion-universe.md`), for the map of the series
