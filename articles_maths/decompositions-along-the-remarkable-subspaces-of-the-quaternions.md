# __Decompositions Along the Remarkable Subspaces of the Quaternions__

## Introduction

The involutions of the quaternion algebra cut $\mathbb{H}$ into three additive decompositions, and the product adds a fourth, multiplicative one. This article states all four: the scalar–vector decomposition $\mathbb{H}=\mathbb{R}_{\mathbb{H}}\oplus\mathrm{Vect}(\mathbb{H})$ of dimensions $1+3$, cut by the natural sign; the axis decomposition $\mathbb{H}=\mathbb{C}_\nu\oplus\nu^\perp$ of dimensions $2+2$ along a unit imaginary quaternion $\nu$, cut by the inner involution; the twist decomposition $\mathbb{H}=(\mathbb{R}_{\mathbb{H}}\oplus\nu^\perp)\oplus\mathbb{R}\nu$ of dimensions $3+1$, its companion on the same axis, cut by the twist ${}^{\natural}\iota_\nu$; and the polar decomposition $\tilde q=|\tilde q|\,u$ of a nonzero quaternion into a positive real modulus and a unit quaternion. It then proves that the list is complete. The element and the basis are those of *Quaternion Algebra*; the two subspaces are *Introduction to the Remarkable Subspaces of the Quaternions*; the involutions that cut them are *Quaternion Involutions and Projections*.

The article is an offer of the group: the scalar–vector decomposition is developed in *Introduction to the Remarkable Subspaces of the Quaternions*, the axis and the twist decompositions in the two articles just named, and the polar element is *Quaternion Polar Element Representation*, below this article in this category.

## The Scalar–Vector Decomposition

The natural sign ${}^{\natural}$ is an involution whose $\pm1$ eigenspaces are the scalar line and the vector space, so the additive decomposition
$$
\mathbb{H}=\mathbb{R}_{\mathbb{H}}\oplus\mathrm{Vect}(\mathbb{H}), \qquad 1+3=4,
$$
is the eigenspace decomposition of ${}^{\natural}$. The two projections are
$$
\tilde q\longmapsto \mathrm{Sc}(\tilde q)=\tfrac12(\tilde q+\tilde q^{\natural}), \qquad \tilde q\longmapsto \vec q=\tfrac12(\tilde q-\tilde q^{\natural}),
$$
they are idempotent, $\mathrm{Sc}+\mathrm{vec}=\operatorname{id}$, and they cut every element uniquely as $\tilde q=\mathrm{Sc}(\tilde q)+\vec q$. The decomposition is characteristic: the two summands are the fixed space of ${}^{\natural}$ and its anti-fixed space, and they are and remain distinguished by the algebra, the scalar line being its centre. The word **scalar** names the coordinates on $\mathbb{R}_{\mathbb{H}}$ and the word **pure** the elements of $\mathrm{Vect}(\mathbb{H})$.

## The Axis Decomposition

Let $\nu$ be a unit imaginary quaternion and let $\iota_\nu(\tilde q)=\nu \tilde q\nu^{-1}$ be the inner involution of *Quaternion Involutions and Projections*. Its fixed space is the plane
$$
\mathbb{C}_\nu=\mathbb{R}e_t\oplus\mathbb{R}\nu=\{a+b\nu:a,b\in\mathbb{R}\},
$$
a commutative two-dimensional subalgebra, and its anti-fixed space is the orthogonal complement $\nu^\perp=\{\vec q\in\mathrm{Vect}(\mathbb{H}):\nu\cdot\vec q=0\}$, a plane. The eigenspace decomposition is therefore
$$
\mathbb{H}=\mathbb{C}_\nu\oplus\nu^\perp, \qquad 2+2=4,
$$
with the projections $\tilde q\mapsto\tfrac12(\tilde q+\iota_\nu \tilde q)$ onto $\mathbb{C}_\nu$ and $\tilde q\mapsto\tfrac12(\tilde q-\iota_\nu \tilde q)$ onto $\nu^\perp$. The reflection $\rho_\nu=-\iota_\nu$ has the same two eigenspaces with the labels exchanged, so it cuts the same decomposition.

The **axis decomposition** of the vector subspace is the refinement of the previous line,
$$
\mathrm{Vect}(\mathbb{H})=\mathbb{R}\nu\oplus\nu^\perp, \qquad 1+2=3,
$$
the component of a pure element along the axis and its part orthogonal to the axis;
$$
\vec q=(\nu\cdot\vec q)\,\nu+\bigl(\vec q-(\nu\cdot\vec q)\nu\bigr).
$$
Combining with the scalar–vector decomposition gives the three-term splitting $\mathbb{H}=\mathbb{R}_{\mathbb{H}}\oplus\mathbb{R}\nu\oplus\nu^\perp$ of dimensions $1+1+2$. The decomposition depends on the axis $\mathbb{R}\nu$, not on the unit chosen to name it, since $\nu$ and $-\nu$ give the same axis and the same $\mathbb{C}_\nu$. Of the two summands $\mathbb{C}_\nu$ is a commutative subalgebra and $\nu^\perp$ is only a subspace, not closed under the product: $\nu^\perp\subseteq\mathrm{Vect}(\mathbb{H})$ and the square of a nonzero element of $\nu^\perp$ is a nonzero scalar.

## The Twist Decomposition

The axis supplies a second involution beside the inner one, the **twist**
$$
\alpha_\nu={}^{\natural}\circ\iota_\nu=\iota_\nu\circ{}^{\natural}, \qquad \alpha_\nu(\tilde q)=\nu \tilde q^{\natural}\nu^{-1},
$$
of *Quaternion Involutions and Projections*. It is an involutive anti-automorphism: $\alpha_\nu^2=\operatorname{id}$ on the elements and $\alpha_\nu(\tilde q_1\tilde q_2)=\alpha_\nu(\tilde q_2)\alpha_\nu(\tilde q_1)$ on the product, and it fixes every element of the plane
$$
\mathbb{R}_{\mathbb{H}}\oplus\nu^\perp=\{a+\vec q:a\in\mathbb{R},\ \vec q\in\nu^\perp\},
$$
scalar part plus the plane orthogonal to the axis, while reversing the axis line $\mathbb{R}\nu$ alone. Its eigenspace decomposition is therefore
$$
\mathbb{H}=(\mathbb{R}_{\mathbb{H}}\oplus\nu^\perp)\oplus\mathbb{R}\nu, \qquad 3+1=4,
$$
with the projections $\tilde q\mapsto\tfrac12(\tilde q+\alpha_\nu\tilde q)$ onto the plane and $\tilde q\mapsto\tfrac12(\tilde q-\alpha_\nu\tilde q)$ onto the axis line. The twist is the companion of the inner involution on the same axis: $\iota_\nu$ isolates the negated plane $\nu^\perp$ against the axis plane $\mathbb{C}_\nu$, and $\alpha_\nu$ isolates the axis line against the scalar line and that plane. The three involutions ${}^{\natural}$, $\iota_\nu$ and $\alpha_\nu$ thus cut the orthogonal splitting $\mathbb{H}=\mathbb{R}_{\mathbb{H}}\oplus\mathbb{R}\nu\oplus\nu^\perp$ into its three two-sided groupings, and the twist decomposition is the one in which the axis line stands alone.

The plane $\mathbb{R}_{\mathbb{H}}\oplus\nu^\perp$ is not a subalgebra: for $\nu=\vec e_x$ the units $\vec e_y$ and $\vec e_z$ of the plane multiply to $\vec e_x$, outside it. The decomposition depends on the axis $\mathbb{R}\nu$ and not on the unit chosen to name it, and the negative twist $-\alpha_\nu$ cuts the same two eigenspaces with the labels exchanged, as the reflection does for the inner involution.

## The Polar Decomposition

The quaternion norm $\langle\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}$ is real and non-negative on $\mathbb{H}$, by *Norm and Invertibility in the Quaternion Algebra*, below this article in this category, and it vanishes only at zero, by *Norm and Invertibility in the Quaternion Algebra*, below this article in this category. For $\tilde q\neq0$ the number
$$
|\tilde q|=\sqrt{\langle\tilde q\rangle_{\natural}}\in\mathbb{R}_{>0}
$$
is the **modulus** of $\tilde q$, and
$$
\tilde q=|\tilde q|\cdot u, \qquad u=\frac{\tilde q}{|\tilde q|}, \qquad \langle u\rangle_{\natural}=\frac{\langle\tilde q\rangle_{\natural}}{|\tilde q|^2}=1.
$$
The element $u$ is a **unit quaternion** (a **rotor**), and $\tilde q=|\tilde q|u$ is the **polar decomposition** of $\tilde q$. The decomposition is unique: the modulus is the non-negative root of the norm and the rotor is then forced. It multiplies two factors of different nature — a positive scalar and an element of the unit sphere — and it is not additive. The polar element, its argument and its axis are *Quaternion Polar Element Representation*, below this article in this category; the unit sphere $N=1$ is the group of rotors, whose topology is *The Quaternion Unit Group as a Topological Group*, below this article in this category.

On the two remarkable subspaces the polar decomposition specialises. A nonzero scalar is already positive or negative and its rotor is $\pm e_t$; a pure element $\vec q$ has square $\vec q^2=-\langle \vec q\rangle_{\natural}$ and rotor $\vec q/|\vec q|$, an element of the sphere of roots of $-1$ of *Introduction to the Remarkable Subspaces of the Quaternions*.

## There Are Exactly These

**Theorem.** The additive decompositions of $\mathbb{H}$ cut out by its involutions, and the multiplicative decomposition cut out by the norm, are exactly these four: the scalar–vector decomposition of dimensions $1+3$, the axis decomposition of dimensions $2+2$ along a unit imaginary, the twist decomposition of dimensions $3+1$ along the same axis, and the polar decomposition.

**Proof.** The involutions available on the elements of $\mathbb{H}$, up to sign, are of three kinds, by *Quaternion Involutions and Projections*. The coordinate involution is ${}^{\natural}$ and its negative, with the two eigenspaces $\mathbb{R}_{\mathbb{H}}$ and $\mathrm{Vect}(\mathbb{H})$, giving the scalar–vector decomposition; the inner involutions are the $\iota_\nu$, one per axis line, and their negatives $\rho_\nu$, with the two eigenspaces $\mathbb{C}_\nu$ and $\nu^\perp$, giving the axis decomposition; and the twists are the $\alpha_\nu={}^{\natural}\iota_\nu$, one per axis line, and their negatives, with the two eigenspaces $\mathbb{R}_{\mathbb{H}}\oplus\nu^\perp$ and $\mathbb{R}\nu$, giving the twist decomposition. No other involution is available, and the eigenspace decomposition of an involution is determined by it, so the additive list is complete. For the multiplicative one, the norm is the only quadratic form on the element with $\langle\tilde q_1\tilde q_2\rangle_{\natural}=\langle\tilde q_1\rangle_{\natural}\langle\tilde q_2\rangle_{\natural}$ and positive values, its positive square root is the modulus, and normalising by it gives the rotor; there is no second multiplicative decomposition, the modulus being one-dimensional.

## Summary

The quaternion algebra decomposes four ways. Additively by the natural sign into the scalar line and the vector space, of dimensions $1+3$, with the projections $\tfrac12(\tilde q\pm \tilde q^{\natural})$. Additively along a unit imaginary $\nu$, by the inner involution, into the plane $\mathbb{C}_\nu$ and the orthogonal plane $\nu^\perp$, of dimensions $2+2$, refining the vector part as $\mathbb{R}\nu\oplus\nu^\perp$; and, on the same axis, by the twist ${}^{\natural}\iota_\nu$, into the plane $\mathbb{R}_{\mathbb{H}}\oplus\nu^\perp$ and the axis line $\mathbb{R}\nu$ alone, of dimensions $3+1$, with the axis line isolated. Multiplicatively, by the positive square root of the norm, into a modulus and a unit rotor, $\tilde q=|\tilde q|u$. These four are all the decompositions the involutions and the norm provide.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{H}=\mathbb{R}_{\mathbb{H}}\oplus\mathrm{Vect}(\mathbb{H})$ | the scalar–vector decomposition, dimensions $1+3$ |
| $\mathbb{C}_\nu=\mathbb{R}e_t\oplus\mathbb{R}\nu$ | the plane of the inner involution $\iota_\nu$, a commutative subalgebra |
| $\nu^\perp$ | the orthogonal plane, the anti-fixed space of $\iota_\nu$ |
| $\mathbb{H}=\mathbb{C}_\nu\oplus\nu^\perp$ | the axis decomposition, dimensions $2+2$ |
| $\alpha_\nu={}^{\natural}\iota_\nu$ | the twist, the involutive anti-automorphism of the axis |
| $\mathbb{R}_{\mathbb{H}}\oplus\nu^\perp$ | the fixed plane of the twist, scalar part plus the orthogonal plane |
| $\mathbb{H}=(\mathbb{R}_{\mathbb{H}}\oplus\nu^\perp)\oplus\mathbb{R}\nu$ | the twist decomposition, dimensions $3+1$ |
| $\lvert \tilde q\rvert=\sqrt{\langle\tilde q\rangle_{\natural}}$ | the modulus of a nonzero quaternion, positive real |
| $u=\tilde q/\lvert \tilde q\rvert$ | the unit rotor, $\langle u\rangle_{\natural}=1$ |

## Further Reading

- *Introduction to the Remarkable Subspaces of the Quaternions* (`articles_maths/introduction-to-the-remarkable-subspaces-of-the-quaternions.md`), for the scalar–vector decomposition and the two subspaces.
- *Quaternion Polar Element Representation* (`articles_maths/quaternion-polar-element-representation.md`), below this article in this category, for the argument and the axis of the polar element.
