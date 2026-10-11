# __Comparison of the Remarkable Subspaces of the Quaternions__

## Introduction

This is the reference article of the remarkable-subspace group of the chapter. It gathers the two subspaces of $\mathbb{H}$, their intersection and their sum, the sign pattern of the natural sign on each, the axis lines of the inner involutions and the plane each fixes, and the place of the quaternion lattice in the ladder of the real algebras $\mathbb{R}\subset\mathbb{C}\subset\mathbb{H}\subset\mathbb{B}$. The two subspaces themselves, with their bases and dimensions, are *Introduction to the Remarkable Subspaces of the Quaternions*; the involutions are *The Group of Involutions of the Quaternions*; the decompositions are *Decompositions Along the Remarkable Subspaces of the Quaternions*. The counterpart is *Comparison of the Remarkable Subspaces* of the biquaternion chapter, whose six-subspace lattice this article measures against.

## The Two Subspaces

The two remarkable subspaces are
$$
\mathbb{R}_{\mathbb{H}}=\{\tilde q:\tilde q^{\natural}=\tilde q\}=\mathbb{R}e_0 , \qquad
\mathrm{Vect}(\mathbb{H})=\{\tilde q:\tilde q^{\natural}=-\tilde q\}=\mathbb{R}e_1\oplus\mathbb{R}e_2\oplus\mathbb{R}e_3 .
$$

**Proposition.** They are supplementary and their intersection is the origin:
$$
\mathbb{R}_{\mathbb{H}}\cap\mathrm{Vect}(\mathbb{H})=0 , \qquad
\mathbb{R}_{\mathbb{H}}+\mathrm{Vect}(\mathbb{H})=\mathbb{H} , \qquad 1+3=4 .
$$
The first is a subalgebra, indeed the centre, and the second is not closed under the product.

**Proof.** A quaternion fixed by ${}^{\natural}$ has $\mathbf q=0$ and a quaternion anti-fixed has $q_0=0$, so the intersection is $\tilde q=0$; every $\tilde q=q_0+\mathbf q$ is the sum of one of each. The subalgebra and centre statements are *Introduction to the Remarkable Subspaces of the Quaternions*; the failure of closure is the product law $\mathbf p\mathbf q=-\langle\mathbf p,\mathbf q\rangle+\mathbf p\times\mathbf q$ recalled there.

## The Sign Pattern of the Natural Sign

The natural sign acts on the coordinates by the sign vector
$$
{}^{\natural}:\ (q_0,q_1,q_2,q_3)\longmapsto(+q_0,-q_1,-q_2,-q_3),
$$
with multiplicity $+1$ on the scalar line and multiplicity $-1$ on the vector space, that is, $1$ and $3$. Its negative $-\natural$ has the signs exchanged, $-1$ on the scalar line and $+1$ on the vector space, so the two together have the eigenspaces
$$
\mathbb{R}_{\mathbb{H}}=\text{fixed space of }{}^{\natural}=\text{anti-fixed space of }-{}^{\natural} , \qquad
\mathrm{Vect}(\mathbb{H})=\text{anti-fixed space of }{}^{\natural}=\text{fixed space of }-{}^{\natural}.
$$
The pair $\{+1,-1\}$ of signs with multiplicities $(1,3)$ characterizes the decomposition, and it is the quaternion shadow of the biquaternion block table: the same $\natural$ there is $+1$ on the centre $\mathbb{C}_{\mathbb{B}}=\mathbb{R}e_0\oplus\mathbb{R}(ie_0)$ and $-1$ on the vector space $\mathrm{Vect}(\mathbb{B})=\operatorname{span}_{\mathbb{R}}\{e_1,e_2,e_3,ie_1,ie_2,ie_3\}$, that is $+1$ on the two scalar blocks and $-1$ on the two vector blocks; each of the two four-dimensional subspaces $\mathbb{H}_{\mathbb{B}}=\mathbb{R}e_0\oplus\mathbb{R}e_1\oplus\mathbb{R}e_2\oplus\mathbb{R}e_3$ and $i\mathbb{H}_{\mathbb{B}}$ therefore carries a split of its scalar part from its vector part. Over $\mathbb{R}$ the two blocks lying inside $\mathbb{H}$ are the scalar block $\mathbb{R}e_0$, collapsing to the scalar line, and the vector block $\mathbb{R}e_1\oplus\mathbb{R}e_2\oplus\mathbb{R}e_3$, collapsing to the vector space, while $\mathbb{R}(ie_0)$ and $i(\mathbb{R}e_1\oplus\mathbb{R}e_2\oplus\mathbb{R}e_3)$ lie outside $\mathbb{H}$; so the four-block sign pattern $(+,+,-,-)$ of $\mathbb{B}$ becomes the two-block $(+,-)$ of $\mathbb{H}$.

## The Axis Lines and the Planes They Fix

Each axis line $\mathbb{R}\nu$ of the vector subspace, $\nu$ a unit imaginary quaternion, carries the inner involution $\iota_\nu(\tilde q)=\nu \tilde q\nu^{-1}$ of *The Group of Involutions of the Quaternions*.

| object | value |
|---|---|
| axis line | $\mathbb{R}\nu$, one per pair $\pm\nu$ |
| involution | $\iota_\nu$, an involutive automorphism |
| fixed plane | $\mathbb{C}_\nu=\mathbb{R}e_0\oplus\mathbb{R}\nu$, the commutative subalgebra of the axis |
| negated plane | $\nu^\perp=\{\mathbf q:\nu\cdot\mathbf q=0\}$, its orthogonal complement |
| sign pattern | $+1$ of multiplicity $2$ on $\mathbb{C}_\nu$, $-1$ of multiplicity $2$ on $\nu^\perp$ |
| action on the two subspaces | preserves $\mathbb{R}_{\mathbb{H}}$; on $\mathrm{Vect}(\mathbb{H})$ fixes the line $\mathbb{R}\nu$ and negates the plane $\nu^\perp$ |

The reflection $\rho_\nu=-\iota_\nu$ has the same sign pattern with the labels exchanged and cuts the same two planes. The inner involutions thus produce, for every axis, a decomposition of $\mathbb{H}$ into a two-dimensional commutative subalgebra and a two-dimensional plane, as in *Decompositions Along the Remarkable Subspaces of the Quaternions*; they move the vector subspace among its lines and planes but single out no further invariant subspace of the algebra. In the biquaternion algebra the corresponding family is larger, because the central unit $i$ supplies the second scalar direction and the subspaces $i\mathbb{H}_{\mathbb{B}}$ built on it, which over $\mathbb{R}$ is absent.

## The Two-Subspace Lattice

The remarkable subspaces of an algebra over $\mathbb{R}$ under inclusion form its **lattice of fixed spaces**, the intersections acting as meets and the sums as joins. For $\mathbb{H}$ the lattice is the diamond
$$
0\subsetneq\mathbb{R}_{\mathbb{H}}\subsetneq\mathbb{H} , \qquad 0\subsetneq\mathrm{Vect}(\mathbb{H})\subsetneq\mathbb{H} ,
$$
the two chains meeting only at their ends: the two proper subspaces are incomparable, they meet in $0$ and they join to $\mathbb{H}$. The lattice has exactly the four elements $0,\mathbb{R}_{\mathbb{H}},\mathrm{Vect}(\mathbb{H}),\mathbb{H}$, with no intermediate subspace beyond those.

The three real algebras of the ladder carry lattices of sizes
$$
\mathbb{C}:\ 1 \ \ (\text{the imaginary line }\mathbb{R}i) , \qquad
\mathbb{H}:\ 2 \ \ (\mathbb{R}_{\mathbb{H}},\ \mathrm{Vect}(\mathbb{H})) , \qquad
\mathbb{B}:\ 6 \ \ (\text{the six of the biquaternion comparison}).
$$
The counts are those of the menu, and they measure the number of eigenspaces that the involutions of each algebra single out: one non-trivial conjugation for $\mathbb{C}$, whose anti-fixed space is the imaginary line, one for $\mathbb{H}$, whose two eigenspaces are the scalar line and the vector space, and the four involutions of $\mathbb{B}$ with the central imaginary unit, whose block ladder reaches the six. The biquaternion lattice is not a chain and not closed under sum; the quaternion lattice is a diamond; the complex one is the two-term chain $0\subsetneq\mathbb{R}i\subsetneq\mathbb{C}$ once the real line is identified with the base field. The quaternion algebra is the middle rung of the ladder, where the vector space first appears and the six-fold ladder is not yet available.

## Why the List of the Two Is the Whole List

**Theorem.** The remarkable real subspaces of $\mathbb{H}$ are exactly $\mathbb{R}_{\mathbb{H}}$ and $\mathrm{Vect}(\mathbb{H})$.

**Proof.** A remarkable subspace, in the sense of this group, is a fixed or an anti-fixed space of a distinguished conjugation of the algebra. Over $\mathbb{R}$ the coefficientwise bar is the identity and the star is ${}^{\natural}$, so the distinguished conjugations are ${}^{\natural}$ and its negative, whose eigenspaces are the scalar line and the vector space. The inner automorphisms $\iota_\nu$ are not distinguished conjugations but automorphisms of the inner class; their fixed and anti-fixed spaces are the plane $\mathbb{C}_\nu$ and the plane $\nu^\perp$, and these are not singled out by the algebra — a different axis $\nu'$ gives different planes, and the group generated by the $\iota_\nu$ moves any axis to any other — so they are not remarkable subspaces of $\mathbb{H}$ but objects of the family of one axis. The remaining involutions of the group, the twists $\alpha_\nu$, are anti-automorphisms whose fixed and anti-fixed spaces are the three-dimensional plane $\mathbb{R}e_0\oplus\nu^\perp$ and the axis line $\mathbb{R}\nu$, so they single out no new remarkable subspace either — the scalar line is their only summand that is one. Hence the list is the two.

This is the same argument as *Introduction to the Remarkable Subspaces of the Quaternions*, stated here in the lattice language; the two articles agree by construction, the introduction owning the definition and the comparison owning the count.

## Summary

The quaternion algebra has two remarkable real subspaces, the scalar line and the vector space, supplementary and with zero intersection. The natural sign has sign vector $(+,-,-,-)$ with multiplicities $1$ and $3$, and its negative exchanges the two; the pair characterizes the decomposition, and it is the collapse of the biquaternion four-block pattern $(+,+,-,-)$ to two blocks. Each axis line of the vector space carries an inner involution, with fixed plane the commutative subalgebra of the axis and negated plane the orthogonal complement. The lattice is the diamond over the two subspaces, against the six-subspace lattice of the biquaternion algebra and the single imaginary line of the complex numbers; and the two are the whole list because ${}^{\natural}$ is the only coordinate conjugation and the inner involutions single out no invariant subspace.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{R}_{\mathbb{H}}$ | the scalar line, the fixed space of ${}^{\natural}$, dimension one |
| $\mathrm{Vect}(\mathbb{H})$ | the vector space, the anti-fixed space of ${}^{\natural}$, dimension three |
| sign vector of ${}^{\natural}$ | $(+,-,-,-)$, multiplicities $(1,3)$ |
| $\mathbb{C}_\nu,\nu^\perp$ | the fixed and anti-fixed planes of the inner involution $\iota_\nu$ |
| lattice of fixed spaces | the remarkable subspaces under inclusion, meets and joins |

## Further Reading

- *Introduction to the Remarkable Subspaces of the Quaternions* (`articles_maths/introduction-to-the-remarkable-subspaces-of-the-quaternions.md`), for the definition, basis and role of the two subspaces.
- *Decompositions Along the Remarkable Subspaces of the Quaternions* (`articles_maths/decompositions-along-the-remarkable-subspaces-of-the-quaternions.md`), for the three additive decompositions and the polar one.
- *The Group of Involutions of the Quaternions* (`articles_maths/the-group-of-involutions-of-the-quaternions.md`), for the natural sign and the inner involutions of the axis lines.
- *Comparison of the Remarkable Subspaces* (`articles_maths/comparison-of-the-remarkable-subspaces.md`), for the six-subspace lattice and the four-block table the quaternion one collapses from.
