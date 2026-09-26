# __The Operator Representation in Subspaces__

## Introduction

The companion article *The Operator Representation of Biquaternions* makes a single element of the algebra act on the algebra by the sandwich

$$
x \longmapsto \tilde{Q}\,x\,\tilde{Q}^\dagger ,
$$

reads it as a representation of the group of units, and computes its kernel, its invariants and its action on the six distinguished subspaces. This article restricts the **acting element** to one of the six subspaces and records what the restriction does to the operator. It is the operator counterpart of *The Polar Representation in Subspaces*, which restricts the same six subspaces in the other direction: there the question is which of the four polar factors a subspace can carry, here it is which operator an element of a subspace produces.

The question is a physical one, and it has a physical answer. The Lorentz transformation of the corpus is written with a rotor, and for a pure boost that rotor lies in the Hermitian subspace $\mathbb{M}_+$, as *The Lorentz Transformation as a Biquaternionic Rotation* records: the boost biquaternion has a real scalar part and a purely imaginary vector part, so it is Hermitian and its sandwich collapses to $\tilde{\Lambda}\tilde{X}\tilde{\Lambda}$. The rotation lies in $\mathbb{H}_{\mathbb{B}}$, the home of the unit real quaternions; the phase lies in the centre; the four-vectors lie in $\mathbb{M}_-$. Each subspace therefore asks a separate question — what kind of transformation does an element of *this* subspace produce? — and the article answers the six questions and finds that they are four.

Three results organise the answer. The first is a **central invariance**: multiplying the acting element by a central scalar multiplies the sandwich by the squared modulus of that scalar. Because the scalar imaginary $i$ is central, the six subspaces collapse to four **operator classes**: the centre, the vector subspace, the two halves together, and the two sectors together; an antiquaternion acts exactly as its real quaternion, and an element of the material sector acts exactly as the corresponding informational element. The second is that the operator's **type** is decided by the subspace in a sharp way: the centre gives the dilations, the vector subspace gives the similarities, the rotations by $\pi$ among them, the two halves give the rotations, and the two sectors give the Lorentz transformations: the boosts, and the boosts composed with a rotation by $\pi$ on the negative-norm branch. The third is the answer to the question the series puts to the Hermitian subspace: **the Lorentz transformation of the corpus is the sandwich of an element of $\mathbb{M}_+$**, so the informational sector is the home of the boosts, and the material sector reaches the same family through the central imaginary.

The conventions are those of *Conventions in the Biquaternion Universe*, and the notation is that of the companion article: $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2 = \det\Phi(\tilde{Q})$; $\operatorname{H}_{\tilde{Q}}(x) = \tilde{Q}x\tilde{Q}^\dagger$ is the sandwich, which is the map the series calls rotor conjugation when $\tilde{Q}$ has unit norm form; a **rotor** is an element of unit norm form, so that $\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$ and $\tilde{\Lambda}^\dagger = \bar{\tilde{\Lambda}}^{*}$; $\hat{q}$ is a unit real quaternion; and the six subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion and antiquaternion subspaces $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, and the informational and material sectors $\mathbb{M}_+$ and $\mathbb{M}_-$. Every identity quoted below was recomputed in double precision on random elements, and the residuals are below $10^{-10}$.

## The Central Factor Leaves the Operator Alone

### The Rule

**Theorem.** Let $z\in\mathbb{C}^{\times}$ be central, $\tilde{Q}$ an element, and $x$ arbitrary. Then

$$
\operatorname{H}_{z\tilde{Q}}(x) = |z|^2\operatorname{H}_{\tilde{Q}}(x) .
$$

**Proof.** Since $z$ is central, $(z\tilde{Q})x(z\tilde{Q})^\dagger = z\tilde{Q}x\tilde{Q}^\dagger\bar{z} = |z|^2\tilde{Q}x\tilde{Q}^\dagger$. $\square$

Two special cases are worth stating apart. For $z = i$ the scaling factor is $|i|^2 = 1$, so

$$
\operatorname{H}_{i\tilde{Q}} = \operatorname{H}_{\tilde{Q}} ,
$$

the sandwich is completely blind to the scalar imaginary; and for $z = -1$, which is central of modulus one, the operators of $\tilde{Q}$ and $-\tilde{Q}$ coincide, which is the usual two-fold redundancy of a rotor.

### The Six Subspaces Fall into Four Operator Classes

The scalar imaginary multiples act on the subspaces in a fixed way: multiplication by $i$ fixes the centre and the vector subspace, exchanges the quaternion and antiquaternion subspaces, and exchanges the two sectors. The theorem therefore says that a subspace and its image under multiplication by $i$ carry **the same operator element by element**: if $\tilde{Q}' = i\tilde{Q}$ then

$$
\operatorname{H}_{\tilde{Q}'} = \operatorname{H}_{\tilde{Q}} .
$$

The six subspaces of the framework are thus cut into four **operator classes**, and a class is exactly an orbit of the pair of subspaces under multiplication by $i$:

| class | subspaces | the sandwich |
|---|---|---|
| $1$ | $\mathbb{C}_{\mathbb{B}}$ | the dilations by $|z|^2$ |
| $2$ | $\mathrm{Vect}(\mathbb{B})$ | the similarities of the interval, and the rotations by $\pi$ for the real vectors |
| $3$ | $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | the rotations, with a scalar factor off the unit-norm slice |
| $4$ | $\mathbb{M}_+$, $\mathbb{M}_-$ | the Lorentz transformations: the boosts, and the boosts composed with a rotation by $\pi$ for the negative-norm elements |

The four classes must not be confused with the four coordinate blocks of the polar article: the blocks are the intersections of the subspaces and cut them the other way, while the classes are unions of subspaces and are the smallest sets on which the operator is constant.

### The Kernel of the Operator

**Theorem.** For units $\tilde{Q}$ and $\tilde{R}$,

$$
\operatorname{H}_{\tilde{Q}} = \operatorname{H}_{\tilde{R}} \iff \tilde{R}^{-1}\tilde{Q} = e^{i\theta}e_0 .
$$

**Proof.** Put $\tilde{T} = \tilde{R}^{-1}\tilde{Q}$ and note that $\operatorname{H}_{\tilde{R}\tilde{T}} = \operatorname{H}_{\tilde{R}}\circ\operatorname{H}_{\tilde{T}}$; the equality of the two operators is therefore equivalent to $\operatorname{H}_{\tilde{T}} = \mathrm{id}$, whose kernel is the central circle by the companion's theorem. $\square$

The kernel is the central circle $U(1)e_0$, of one real dimension: the sandwich is blind to a central phase and to nothing else. Inside a class the central units are $\mathbb{C}^\times e_0$ on the centre, $\mathbb{R}^\times e_0$ on the two halves and on the informational sector, $i\mathbb{R}^\times e_0$ on the antiquaternion subspace and on the material sector, and none at all on the vector subspace, whose only central element is the zero element. On the unit-norm slice $N = 1$, which is where the rotors live, every class maps to its operators two to one, with fibre $\{\pm e_0\}$: that is the double cover, and it is invisible in the class as a whole, where the sandwich still distinguishes the moduli.

### The Operators Compose as the Elements Do

**Proposition.** For all units $\tilde{Q}, \tilde{R}$,

$$
\operatorname{H}_{\tilde{Q}\tilde{R}} = \operatorname{H}_{\tilde{Q}}\circ\operatorname{H}_{\tilde{R}} .
$$

**Proof.** $\operatorname{H}_{\tilde{Q}\tilde{R}}(x) = \tilde{Q}\tilde{R}x\tilde{R}^\dagger\tilde{Q}^\dagger = \operatorname{H}_{\tilde{Q}}\!\left(\operatorname{H}_{\tilde{R}}(x)\right)$. $\square$

The identity is the statement that the sandwich is a representation of the group of units, not merely a collection of linear maps: the individual maps are not algebra automorphisms, but they compose as their elements do. It is the tool that decomposes an operator whose element is a product, and it is used twice below.

## The Centre: the Operator of a Complex Scalar

### The Element and Its Operator

Let $\tilde{Q} = ze_0$ with $z = re^{i\alpha}\neq 0$; the norm form is $N(\tilde{Q}) = z^2$, of modulus $r^2$. The sandwich of a central element is the dilation

$$
\operatorname{H}_{ze_0}(x) = |z|^2x = r^2x .
$$

The centre therefore contributes to the operator representation nothing but a dilation of the whole algebra by the modulus of the norm form, and on the unit-modulus slice $|z| = 1$ it contributes the identity. In the language of the classes, the centre is a class whose operator is a dilation by the squared modulus of the element, trivial on the unit circle of the class.

### Why This Is the Right Reading

The result is the operator form of a fact about the polar representation: the two factors of a polar element that lie in the centre are the scale $r$ and the phase $e^{i\alpha}$, and a dilation by $r^2$ is the only trace of them that an operator can carry. The sandwich carries the modulus but not the argument, since $|z|^2$ distinguishes $z$ from $\bar{z}$, from $-z$ and from $e^{i\alpha}z$. In the four-factor polar language the centre is the class in which the boost factor and the rotor are both trivial, and the operator statement is that the surviving datum is the modulus, once, squared.

**Example.** Take $z = 3 + 2i$, of modulus $\sqrt{13}$ and norm form $N = (3+2i)^2 = 5 + 12i$ of modulus $13$. Then $\operatorname{H}_{ze_0}(x) = 13x$ on every element, so $N\!\left(\operatorname{H}_{ze_0}(x)\right) = 169N(x) = |N(\tilde{Q})|^2N(x)$, in agreement with the norm-form scaling of the companion article.

## The Vector Subspace: the Similarities

### A Vector Has a Central Square

An element of the vector subspace is $\tilde{Q} = \mathbf{v} = v_1e_1 + v_2e_2 + v_3e_3$ with complex coefficients; equivalently $\operatorname{Sc}\tilde{Q} = 0$. Writing a general element as $\tilde{Q} = ae_0 + \mathbf{v}$ with $a$ complex, its square is

$$
\tilde{Q}^2 = \left(a^2 - \mathbf{v}\cdot\mathbf{v}\right)e_0 + 2a\mathbf{v} ,
$$

where $\mathbf{v}\cdot\mathbf{v} = v_1^2+v_2^2+v_3^2 = N(\mathbf{v})$ is the norm form of the vector part. The square is central exactly when the vector part of the square vanishes, that is when $a\mathbf{v} = 0$.

**Proposition.** $\tilde{Q}^2$ is central if and only if $\tilde{Q}$ lies in the centre or in the vector subspace.

*Proof.* If $a = 0$ or $\mathbf{v} = 0$ the displayed square is central. Conversely if $2a\mathbf{v} = 0$ with $\tilde{Q}$ not central, then $\mathbf{v}\neq 0$ and $a = 0$. $\square$

For an element of the vector subspace the square is therefore central and computable in closed form: the products $e_je_k$ with $j\neq k$ cancel in pairs because they anticommute, so $\mathbf{v}^2 = -N(\mathbf{v})e_0$ and

$$
\mathbf{v}^2 = -N(\mathbf{v})\,e_0 .
$$

### A Real Vector Acts as the Rotation by $\pi$ About Itself

Let $\hat{\mathbf{u}}$ be a real unit vector, so that $\hat{\mathbf{u}}^2 = -e_0$, $N(\hat{\mathbf{u}}) = 1$, and $\hat{\mathbf{u}}^\dagger = -\hat{\mathbf{u}}$. The sandwich of a real unit vector is therefore a sandwich with a sign,

$$
\operatorname{H}_{\hat{\mathbf{u}}}(x) = \hat{\mathbf{u}}\,x\,\hat{\mathbf{u}}^\dagger = -\hat{\mathbf{u}}\,x\,\hat{\mathbf{u}} ,
$$

and the map is the rotation by $\pi$ about $\hat{\mathbf{u}}$: it fixes $e_0$ and $\hat{\mathbf{u}}$, negates the two-dimensional plane orthogonal to $\hat{\mathbf{u}}$, and because $i$ is central it does the same on the imaginary vector part. In particular it preserves each of the six subspaces, and it is an element of the rotation group $SO(3)$ of order two.

**Example.** For $\hat{\mathbf{u}} = e_1$ the operator acts on the basis by

| $x$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ | $ie_0$ | $ie_1$ | $ie_2$ | $ie_3$ |
|---|---|---|---|---|---|---|---|---|
| $\operatorname{H}_{e_1}(x)$ | $e_0$ | $e_1$ | $-e_2$ | $-e_3$ | $ie_0$ | $ie_1$ | $-ie_2$ | $-ie_3$ |

which is the rotation through $\pi$ about $e_1$, as the polar article's reading of the vector subspace — the rotor is a unit vector in the plane of the element — leads one to expect. The real unit vectors therefore realise the rotations by $\pi$ and nothing else, and they are the elements with which the operator representation is most nearly faithful.

### The Sandwich of a Vector Is a Similarity

The sandwich of a vector scales the interval. For $\tilde{Q} = \mathbf{v}$ the norm-form relation of the companion article gives

$$
N\!\left(\operatorname{H}_{\mathbf{v}}(x)\right) = |N(\mathbf{v})|^2N(x) ,
$$

so a vector preserves the causal type of every element and rescales the interval by one positive factor; on the unit-norm vectors the factor is one and the map is an isometry. The Hermitian element that measures the scaling is $\mathbf{v}\mathbf{v}^\dagger$, computable from the cross product of the coefficient vector and its conjugate,

$$
\mathbf{v}\,\mathbf{v}^\dagger = |\mathbf{v}|^2e_0 - \mathbf{v}\times\mathbf{v}^{*} , \qquad |\mathbf{v}|^2 = |v_1|^2+|v_2|^2+|v_3|^2 ,
$$

where $|\mathbf{v}|^2$ is the Euclidean norm squared and $\mathbf{v}\times\mathbf{v}^{*}$ is the cross product of the coefficient triple with its complex conjugate. That cross product is purely imaginary in each coordinate, so $\mathbf{v}\mathbf{v}^\dagger$ is an element of the informational sector; it is central exactly when the three coefficients share a common complex factor, $\mathbf{v} = c\,\mathbf{w}$ with $c\in\mathbb{C}$ and $\mathbf{w}$ real, and then the operator of the complex vector is the operator of the real direction multiplied by the norm form,

$$
\operatorname{H}_{\mathbf{v}} = |\mathbf{v}|^2\operatorname{H}_{\hat{\mathbf{w}}} , \qquad \hat{\mathbf{w}} = \mathbf{w}/|\mathbf{w}| .
$$

### The Unit-Norm Vectors Are Rotors of a Mixed Type

A vector of unit norm form, $N(\mathbf{v}) = 1$, is an element of the Lorentz group, so its sandwich, read on the material sector, lies in $O(1,3)$: it preserves the two sectors and scales the norm form by $|N|^2 = 1$, and the family of unit-norm vectors is connected and contains the real unit vectors, whose operators are the rotations by $\pi$, so the induced map on the material sector lies in the identity component $SO^+(1,3)$. It is not in general a pure boost: a complex vector acts as a boost composed with the rotation by $\pi$ about its own direction, a composition that the section on the sectors returns to. The computation is instructive:

**Example.** Take $\mathbf{v} = a\,e_1 + b\,e_2$ with $a = 0.6 + 0.5i$ and $b = \sqrt{1-a^2} = 0.99079746 - 0.30278640\,i$, so that $N(\mathbf{v}) = 1$. Then

$$
\operatorname{H}_{\mathbf{v}}(ie_0) = 1.683359\,ie_0 + 1.354141\,e_3 , \qquad \operatorname{H}_{\mathbf{v}}(e_1) = -0.463359\,e_1 + 0.886171\,e_2 .
$$

The time axis stays in the cone, the transverse plane stays in the material sector, and the norm form is the unit one: the operator is a Lorentz transformation, with a boost part of rapidity $\operatorname{arcosh}1.683359 = 1.111035$ and a rotation part. The element is a rotor of unit norm form, and its operator is not a pure boost.

### The Imaginary Vectors Give the Same Operators

For $\mathbf{v}$ in the vector subspace the element $i\mathbf{v}$ is again in the vector subspace, and by the central rule the two elements have the same operator. The traceless Hermitian elements $i\mathbf{w}$ with $\mathbf{w}$ a real vector, which are the vector-subspace part of the informational sector, therefore act exactly as the real vectors $\mathbf{w}$, and in particular a unit imaginary vector $i\hat{\mathbf{u}}$ acts as the rotation by $\pi$ about $\hat{\mathbf{u}}$ even though its element is Hermitian. This is the first appearance of a phenomenon that the two sectors will show again: the sector label of an element does not fix the type of its operator.

## The Two Halves: the Rotations

### The Quaternion Subspace

Let $\tilde{R}$ be a real quaternion, $\tilde{R} = a_0e_0 + a_1e_1+a_2e_2+a_3e_3$ with real coefficients. Its Hermitian conjugate is its quaternion conjugate, $\tilde{R}^\dagger = \bar{\tilde{R}} = |\tilde{R}|^2\tilde{R}^{-1}$, with $N(\tilde{R}) = |\tilde{R}|^2$ a positive real, so the central rule gives

$$
\operatorname{H}_{\tilde{R}}(x) = \tilde{R}\,x\,\bar{\tilde{R}} = |\tilde{R}|^2\,\operatorname{H}_{\hat{R}}(x) , \qquad \hat{R} = \tilde{R}/|\tilde{R}| .
$$

A real quaternion therefore acts as the dilation by its squared modulus composed with the rotation of the unit quaternion of the same direction, and on the unit-norm slice it is the familiar rotation. Writing $\tilde{R} = |\tilde{R}|(\cos\theta + \sin\theta\,\hat{\mathbf{u}})$ with $\hat{\mathbf{u}}$ a real unit vector,

$$
\operatorname{H}_{\tilde{R}}(\mathbf{v}) = |\tilde{R}|^2\Bigl(\mathbf{v}\cos2\theta + (\hat{\mathbf{u}}\times\mathbf{v})\sin2\theta + \hat{\mathbf{u}}\,(\hat{\mathbf{u}}\cdot\mathbf{v})(1-\cos2\theta)\Bigr) ,
$$

which is the rotation of the real vector part through $2\theta$ about $\hat{\mathbf{u}}$, scaled by $|\tilde{R}|^2$. The operator preserves all six subspaces, and the kernel on the unit-norm slice is $\{\pm e_0\}$, so the map

$$
\mathrm{Sp}(1)\longrightarrow SO(3) , \qquad \hat{q}\longmapsto\operatorname{H}_{\hat{q}} ,
$$

is the two-fold cover of the rotation group. The doubling of the angle is the same doubling as in the companion article; what the subspace adds is that on $\mathbb{H}_{\mathbb{B}}$ the sandwich acts as a rotation of the whole algebra, leaving the centre, the vector subspace and the two sectors in place.

### The Antiquaternion Subspace Gives the Same Operators

Let $\tilde{Q} = i\tilde{R}$ with $\tilde{R}$ a real quaternion, the general element of the antiquaternion subspace. Since $i$ is central, the operator is that of $\tilde{R}$:

$$
\operatorname{H}_{i\tilde{R}} = \operatorname{H}_{\tilde{R}} .
$$

The antiquaternion subspace therefore contributes no operator that the quaternion subspace does not already contribute, and the two halves are two ways of writing one family of rotations — the operator statement of the polar article's finding that the antiquaternion carries the same rotor with the phase frozen at $\pi/2$. Each half covers the rotation group twice, since the two signs are identified, and the two halves produce the same operators, so the union of the halves covers the rotation group four times over.

### Where the Rotations Sit

The rotations form the three real parameters of the operator group that preserve the whole subspace structure, the subgroup $SU(2)/\{\pm e_0\}\cong SO(3)$ of the companion article; the other three parameters are the boosts, and the sections that follow place them in the two sectors. The half-angle is carried by the element and the full angle by the operator, so the element is a spinor of the operator representation and never the operator itself; the worked examples below exhibit the doubling on $\cos(\pi/6)e_0 + \sin(\pi/6)e_3$, whose operator is the rotation through $\pi/3$.

## The Two Sectors: the Lorentz Transformations

### The Informational Sector: the Lorentz Transformation in $\mathbb{M}_+$

Let $\tilde{Q}$ be a Hermitian element of unit norm form, $\tilde{Q} = \tilde{Q}^\dagger$, $N(\tilde{Q}) = 1$. Its matrix image is Hermitian of determinant one, so its eigenvalues are $\lambda$ and $\lambda^{-1}$ with $\lambda$ real and nonzero; when both are positive the element is the boost rotor

$$
\tilde{\Lambda} = \cosh\frac{\psi}{2}\,e_0 + i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}} , \qquad \tanh\psi = \frac{u}{c} ,
$$

and when both are negative it is $-\tilde{\Lambda}$ with the same operator. Since $\tilde{\Lambda}$ is Hermitian, its sandwich has the element on both sides of the argument,

$$
\operatorname{H}_{\tilde{\Lambda}}(\tilde{X}) = \tilde{\Lambda}\,\tilde{X}\,\tilde{\Lambda} ,
$$

which is the form in which *The Lorentz Transformation as a Biquaternionic Rotation* writes the boost. This is the sharpest answer the article gives to the question it started from: **the Lorentz transformation of the corpus is the sandwich of an element of the informational sector**, with no rotation part, and the element is Hermitian, so no inverse appears in it. Its action on a four-position is the boost relation, and the kernel on the class is the two central signs, so the boost family is three-dimensional — the hyperbolic three-space of the rapidity vector — and the map from the class to the boosts is two to one.

**Example.** Take $\beta = 0.6$ along $e_3$, that is $\psi = \operatorname{artanh}0.6$, with

$$
\tilde{\Lambda} = 1.060660172\,e_0 + 0.353553391\,i\,e_3 , \qquad N(\tilde{\Lambda}) = \cosh^2\frac{\psi}{2}-\sinh^2\frac{\psi}{2} = 1 ,
$$

and the four-position $\tilde{X} = icte_0 + 0.6ct\,e_3$ of a world line of velocity $0.6c$, at $ct = 1$. Then

$$
\operatorname{H}_{\tilde{\Lambda}}(\tilde{X}) = \tilde{\Lambda}\tilde{X}\tilde{\Lambda} = 0.8\,ie_0 ,
$$

the four-position in the rest frame, with $ct' = 0.8 = \sqrt{1-0.6^2}$ and $z' = 0$. The boost formula of the corpus, $ct' = ct\cosh\psi - z\sinh\psi$ and $z' = z\cosh\psi - ct\sinh\psi$, is the same computation in components, and the element of the informational sector is the operator that performs it.

### The Negative-Norm Branch of the Sector

The unit-modulus Hermitian elements with $N(\tilde{Q}) = -1$ do not have both eigenvalues positive, and they are not boost rotors; they are nevertheless Lorentz operators, and their structure is worth one computation. Write

$$
\tilde{Q} = \sinh\varphi\,e_0 + i\cosh\varphi\,\hat{\mathbf{u}} , \qquad N(\tilde{Q}) = \sinh^2\varphi - \cosh^2\varphi = -1 ,
$$

with $\hat{\mathbf{u}}$ a real unit vector. Then the product of $\tilde{Q}$ with the boost rotor $\tilde{\Lambda} = \cosh\varphi\,e_0 + i\sinh\varphi\,\hat{\mathbf{u}}$ and with the unit real vector $\hat{\mathbf{u}}$ is

$$
\tilde{\Lambda}\,\hat{\mathbf{u}} = \cosh\varphi\,\hat{\mathbf{u}} + i\sinh\varphi\,\hat{\mathbf{u}}^2 = \cosh\varphi\,\hat{\mathbf{u}} - i\sinh\varphi\,e_0 = -i\tilde{Q} ,
\qquad \tilde{Q} = i\,\tilde{\Lambda}\,\hat{\mathbf{u}} ,
$$

so by the central rule and the composition lemma

$$
\operatorname{H}_{\tilde{Q}} = \operatorname{H}_{\tilde{\Lambda}\hat{\mathbf{u}}} = \operatorname{H}_{\tilde{\Lambda}}\circ\operatorname{H}_{\hat{\mathbf{u}}} ,
$$

a boost composed with the rotation by $\pi$ about $\hat{\mathbf{u}}$. At $\varphi = 0$ the element is the traceless $i\hat{\mathbf{u}}$ of the vector subspace and the boost factor is the identity, so the family is connected to the rotations by $\pi$; at every $\varphi$ the operator is orthochronous and proper, and the sign of the norm form decides whether the rotation by $\pi$ is present.

**Example.** For $\tilde{Q} = \sqrt{3}\,e_0 + 2i\,e_3$, which is Hermitian with $N(\tilde{Q}) = 3-4 = -1$, the same data are $\hat{\mathbf{u}} = e_3$, $\cosh\varphi = 2$, $\sinh\varphi = \sqrt3$, the boost rotor $\tilde{\Lambda} = 2e_0 + i\sqrt3\,e_3$ of rapidity $\operatorname{arcosh}7 = 2.633915794$, and

$$
\operatorname{H}_{\tilde{Q}}(ie_0) = 7\,ie_0 - 4\sqrt3\,e_3 = 7\,ie_0 - 6.928203\,e_3 , \qquad \tilde{\Lambda}e_3 = -i\tilde{Q} ,
$$

so that $\operatorname{H}_{\tilde{Q}} = \operatorname{H}_{\tilde{\Lambda}}\circ\operatorname{H}_{e_3}$: the transverse plane is negated and the time axis is carried to the four-velocity of rapidity $\operatorname{arcosh}7$. The example is the exact statement that a Hermitian element of negative norm form acts as a Lorentz operator with a rotation part, not as a boost.

### The Material Sector Gives the Same Operators

Let $\tilde{Q}$ be an element of the material sector, $\tilde{Q}^\dagger = -\tilde{Q}$, so that $\tilde{Q} = ict\,e_0 + \mathbf{x}$. By the central rule with $z = i$,

$$
\operatorname{H}_{\tilde{Q}} = \operatorname{H}_{i\tilde{Q}} , \qquad i\tilde{Q}\in\mathbb{M}_+ ,
$$

so the sandwich of a four-vector is the sandwich of the informational element $i\tilde{Q}$, and the material sector adds no operator family: the boosts, the rotations by $\pi$, and their compositions are already all present in the informational sector. The reading is the one the corpus uses everywhere: the same Lorentz transformation can be written with a Hermitian form, which is the informational reading, and with a four-vector, which is the material reading; the traceless Hermitian elements $i\hat{\mathbf{u}}$ correspond exactly to the unit spacelike four-vectors $-\hat{\mathbf{u}}$ and act as the rotations by $\pi$.

**Example.** The element of the previous example, $\tilde{Q} = \sqrt3\,e_0 + 2i\,e_3$, has $i\tilde{Q} = \sqrt3\,ie_0 - 2e_3$, a four-vector of norm form $N = -3+4 = 1$, that is, a unit spacelike four-vector; and $\operatorname{H}_{i\tilde{Q}}(ie_0) = 7ie_0 - 4\sqrt3e_3$ with the same right-hand side, so the two readings agree element by element, as the central rule requires.

## The Operator Dictionary

The six subspaces, the operator each produces, and the subspace's own reading, in one table. The kernel column records the kernel of the operator inside the class; on the unit-norm slice it reduces to the fibre $\{\pm e_0\}$ in every class.

| subspace | acting element | the sandwich | kernel inside the class | the subspace's role |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $ze_0$ | dilation by $|z|^2$ | $U(1)e_0$ | the scale and the phase |
| $\mathrm{Vect}(\mathbb{B})$ | $\mathbf{v}$, $\mathbf{v}^2 = -N(\mathbf{v})e_0$ | a similarity of the interval; the rotation by $\pi$ for a real unit $\mathbf{v}$ | none | the free phase of the polar form |
| $\mathbb{H}_{\mathbb{B}}$ | $\tilde{R}$ real | $|\tilde{R}|^2$ times the rotation through $2\theta$ | $\mathbb{R}^\times e_0$ | the rotor |
| $i\mathbb{H}_{\mathbb{B}}$ | $i\tilde{R}$ | the same rotation | $i\mathbb{R}^\times e_0$ | the same rotor, phase frozen |
| $\mathbb{M}_+$ | Hermitian $\tilde{Q}$ | the boost for $N = 1$ positive definite; boost times rotation by $\pi$ for $N = -1$ | $\mathbb{R}^\times e_0$ | the Lorentz transformation |
| $\mathbb{M}_-$ | $\tilde{Q} = ict\,e_0+\mathbf{x}$ | the same family as $\mathbb{M}_+$, through $i\tilde{Q}$ | $i\mathbb{R}^\times e_0$ | the four-vectors |

## Comparison with the Polar Representation in Subspaces

The two articles restrict the same six subspaces, and the comparison is a dictionary between the two restrictions. The polar article asks which of the four factors $r$, $e^{i\alpha}$, $B$ and $\hat{q}$ a subspace can carry; this article asks which operator an element of the subspace produces. The answers pair up: the centre is the home of the scale and the phase, and its operator is trivial; the vector subspace is the only one that carries the phase freely together with a nontrivial boost and rotor, and its conjugation operator is the involution; the two halves carry the rotor alone, and their operator is the rotation; the two sectors carry the boost, and their sandwich is the boost. In each case the factor that a subspace is able to carry is the factor that turns into the operator: the rotor into the rotation, the boost into the boost, and the scale and the phase into nothing at all, since they lie in the centre and the centre is the kernel.

The comparison also explains an asymmetry of this article. The polar representation loses factors when the element is restricted, and the loss is one-sided: a subspace is unable to carry a factor. The operator representation loses **operators** when the acting element is restricted, and the loss goes the other way: the six subspaces produce only four operator classes, and inside a class they produce the same operator element by element. The two directions of restriction are the two halves of the same statement about the algebra, and the central circle, which is the kernel of the operator, is what makes them differ.

## Worked Examples

### A Central Element

$\tilde{Q} = (3+2i)e_0$: $\operatorname{H}_{\tilde{Q}}(x) = 13x$, the dilation by the modulus of the norm form; the class contributes no other operator.

### A Real Unit Vector

$\hat{\mathbf{u}} = e_1$: the sandwich acts as the rotation by $\pi$ about $e_1$, with $e_2\mapsto-e_2$, $e_3\mapsto-e_3$, $ie_2\mapsto-ie_2$, $ie_3\mapsto-ie_3$, and $e_0$, $e_1$, $ie_0$, $ie_1$ fixed. The operator is an involution and preserves all six subspaces.

### An Imaginary Unit Vector

$i\hat{\mathbf{u}} = ie_1$: the same operator as $e_1$, by the central rule, so a Hermitian element of the informational sector acts as a rotation by $\pi$; the sector label does not fix the type of the operator.

### A Unit Quaternion

$\tilde{R} = \cos\frac{\pi}{6}e_0 + \sin\frac{\pi}{6}e_3$: the sandwich gives $\operatorname{H}_{\tilde{R}}(e_1) = \frac12e_1 + \frac{\sqrt3}{2}e_2$, the rotation through $\pi/3$ about $e_3$, which is twice the angle $\pi/6$ in the element. The kernel is $\{\pm e_0\}$.

### A Central Real Quaternion

$\tilde{R} = 2e_0$: the element is central, so $\operatorname{H}_{\tilde{R}} = 4\,\mathrm{id}$; the example shows that the scalar of a real quaternion is the dilation $|\tilde{R}|^2$ of its operator, and that it disappears on the unit-norm slice.

### A Boost Rotor

$\beta = 0.6$, $\tilde{\Lambda} = 1.060660172e_0 + 0.353553391ie_3$: $\operatorname{H}_{\tilde{\Lambda}}(ie_0+0.6e_3) = 0.8ie_0$, the rest-frame four-position, and the time axis of the moving world line is carried to the rest frame.

### A Hermitian Element of Negative Norm Form

$\tilde{Q} = \sqrt3e_0+2ie_3$: $\operatorname{H}_{\tilde{Q}}(ie_0) = 7ie_0 - 4\sqrt3e_3$, and $\operatorname{H}_{\tilde{Q}} = \operatorname{H}_{\tilde{\Lambda}}\circ\operatorname{H}_{e_3}$ with $\tilde{\Lambda} = 2e_0+i\sqrt3e_3$ of rapidity $\operatorname{arcosh}7 = 2.633915794$; the operator is a boost with a rotation by $\pi$, not a pure boost.

### A Unit Spacelike Four-Vector

$i\tilde{Q} = \sqrt3ie_0 - 2e_3$, of norm form $1$: the same operators as $\tilde{Q}$, with $\operatorname{H}_{i\tilde{Q}}(ie_0) = 7ie_0-4\sqrt3e_3$, which is the material-sector reading of the previous example.

## Summary

The sandwich of the operator representation, restricted to the six distinguished subspaces, produces four operator classes, because a central factor multiplies the sandwich by the squared modulus of its scalar: the scalar imaginary identifies the two halves and the two sectors, so an antiquaternion acts as its real quaternion and a four-vector acts as the informational element $i$ times it.

The **centre** contributes only the dilations by the squared modulus of the norm form. The **vector subspace** contributes the similarities of the interval: an element of the vector subspace has a central square, $\mathbf{v}^2 = -N(\mathbf{v})e_0$, and the sandwich preserves the causal type of every element while rescaling the interval by $|N(\mathbf{v})|^2$; a real unit vector acts as the rotation by $\pi$ about itself and preserves all six subspaces, a general unit-norm vector acts on the four-vectors as a boost composed with that rotation, and the Hermitian factor of the scaling is $\mathbf{v}\mathbf{v}^\dagger = |\mathbf{v}|^2e_0 - \mathbf{v}\times\mathbf{v}^{*}$. The **two halves** contribute the rotations: a real quaternion acts as $|\tilde{R}|^2$ times the rotation through twice its half-angle, the two equal on the unit-norm slice, with kernel $\{\pm e_0\}$ and the two-fold cover of $SO(3)$, and the two halves give the same operators. The **two sectors** contribute the Lorentz transformations: the sandwich of a Hermitian element of unit norm form is the boost, written with the element on both sides, and it is the Lorentz transformation of the corpus; the sandwich of a four-vector is the same family through the central imaginary; and the sign of the norm form decides whether the operator carries a rotation by $\pi$, since the negative-norm Hermitian elements are $\tilde{Q} = i\tilde{\Lambda}\hat{\mathbf{u}}$ and act as a boost composed with the rotation by $\pi$ about $\hat{\mathbf{u}}$.

The type of the operator is therefore decided by the class of the acting element and, inside a class, by the element's norm form: the centre dilates, the vector subspace and the halves transform isometrically or almost so, and the sectors are where the Lorentz transformations of the series live.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\operatorname{H}_{\tilde{Q}}(x) = \tilde{Q}x\tilde{Q}^\dagger$ | the sandwich, rotor conjugation for a rotor |
| $\operatorname{H}_{z\tilde{Q}} = |z|^2\operatorname{H}_{\tilde{Q}}$ | the central rule, $z$ central |
| $\operatorname{H}_{\tilde{Q}\tilde{R}} = \operatorname{H}_{\tilde{Q}}\circ\operatorname{H}_{\tilde{R}}$ | the composition law |
| $\mathbb{C}_{\mathbb{B}}$ | the centre, of elements $ze_0$ |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, $\operatorname{Sc}\tilde{Q} = 0$ |
| $\mathbf{v}^2 = -N(\mathbf{v})e_0$ | the central square of a vector |
| $\mathbf{v}\mathbf{v}^\dagger = \|\mathbf{v}\|^2e_0 - \mathbf{v}\times\mathbf{v}^{*}$ | the Hermitian element of a vector |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | the quaternion and antiquaternion subspaces |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | the informational and material sectors |
| $\tilde{\Lambda} = \cosh\frac{\psi}{2}e_0 + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ | the boost rotor, Hermitian and of unit norm form |
| $\hat{q} = \cos\theta+\sin\theta\,\hat{\mathbf{u}}$ | the rotation rotor, a unit real quaternion |
| $\tilde{Q} = \sinh\varphi\,e_0 + i\cosh\varphi\,\hat{\mathbf{u}}$, $N = -1$ | the negative-norm branch of the informational sector, $= i\tilde{\Lambda}\hat{\mathbf{u}}$ |
| $SO^+(1,3)$, $SO(3)$ | the Lorentz group and the rotation group reached by the sandwich |

## Further Reading

- *The Operator Representation of Biquaternions* (`articles_physics/the-operator-representation-of-biquaternions.md`), immediately before the present article in the menu, for the sandwich unrestricted, its kernel, its action on the six subspaces and its composition law
- *The Polar Representation in Subspaces* (`articles_physics/the-polar-representation-in-subspaces.md`), for the same six subspaces restricted in the other direction, to the four factors of one element
- *Relations Between Subspaces* (`articles_physics/relations-between-subspaces.md`), for the six subspaces, their definitions, their intersections and the four coordinate blocks
- *The Lorentz Transformation as a Biquaternionic Rotation* (`articles_physics/the-lorentz-transformation-as-a-biquaternionic-rotation.md`), for the boost biquaternion in the informational sector and the sandwich with the element on both sides
- *The Lorentz Group as Biquaternion Norm-Form Automorphisms* (`articles_physics/the-lorentz-group-as-biquaternion-norm-form-automorphisms.md`), for the unit-norm rotors, the homomorphism onto the Lorentz group and its kernel
- *The Lorentz Group in Biquaternionic Form — Structure and Representations* (`articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.md`), for the boosts, the rotations and the Thomas–Wigner rotation the composition lemma produces
- *The Center Subspace C_B as the Complex Time Sector* (`articles_physics/the-center-subspace-c-b-as-the-complex-time-sector.md`), for the centre on its own terms
- *The Vector Subspace Vect(B) as the Complex Space Sector* (`articles_physics/the-vector-subspace-vect-b-as-the-complex-space-sector.md`), for the vector subspace, its norm form and its polar phase
- *The Quaternion Subspace H_B as the Real Sector* (`articles_physics/the-quaternion-subspace-hb-as-the-real-sector.md`), for the real quaternions and the rotations
- *The Anti-Quaternion Subspace iH_B as the Imaginary Sector* (`articles_physics/the-anti-quaternion-subspace-ihb-as-the-imaginary-sector.md`), for the antiquaternions and the frozen phase
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* (`articles_physics/the-hermitian-subspace-m-plus-as-the-informational-sector.md`), for the sector that carries the boosts and the Hermitian forms
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* (`articles_physics/the-anti-hermitian-subspace-m-as-the-material-sector.md`), for the sector that carries the four-vectors
- *The 2×2 Matrix Representation of Biquaternions* (`articles_physics/the-2x2-matrix-representation-of-biquaternions.md`), for the matrix image of the sandwich as a similarity
- *Conventions in the Biquaternion Universe* (`articles_physics/conventions-in-the-biquaternion-universe.md`), for the conventions used throughout
- *Introduction to the Biquaternion Universe* (`articles_physics/introduction-to-the-biquaternion-universe.md`), for the map of the series
- *Biquaternion Operator Representation* (`articles_maths/biquaternion-operator-representation.md`), the maths companion, for the same sandwich treated algebraically
