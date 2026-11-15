# __Where the Rotor Leaves $M_2$: the Even Subalgebra and $Cl(2)$__

## Introduction

**The rotor of a plane rotation lives in the copy of $\mathbb{C}$ spanned by $I$ and $J$ inside $M_2(\mathbb{R})$, which is the even part of the Clifford algebra $Cl(2)$, while the rotor of a three-dimensional rotation is a quaternion and the quaternions form a real form of $M_2(\mathbb{C})$ that is not closed under multiplication by $i$.**

The article identifies the Clifford algebra of the plane with $M_2(\mathbb{R})$, its even part with the complex numbers inside, the Clifford algebra of three-space with $M_2(\mathbb{C})$, and its even part with the quaternions. It proves that the quaternion algebra sits inside $M_2(\mathbb{C})$ as a real subspace closed under multiplication but not under the complex structure, and it explains what survives at order two. It assumes *The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover*, *Rotors Acting on the Bivector Space at $n=2$: the Adjoint Action* and *The Two Base Fields: $M_2(\mathbb{R})$ inside $M_2(\mathbb{C})$*.

It follows the biquaternion side of the corpus, where the same eight real dimensions are written as *The Biquaternion Algebra*.

## The Clifford Algebra of the Plane

**The Clifford algebra of the plane with the positive definite form is $M_2(\mathbb{R})$, and its even part is the plane of the complex numbers spanned by $I$ and $J$.**

**Definition.** Let $Cl(2)$ be the real algebra with generators $e_{1},e_{2}$ and relations $e_{1}^{2}=e_{2}^{2}=1$, $e_{1}e_{2}+e_{2}e_{1}=0$.

**Proposition.** The algebra $Cl(2)$ is four-dimensional and is isomorphic to $M_2(\mathbb{R})$.

**Proof.** The four products $1,e_{1},e_{2},e_{1}e_{2}$ span it and are independent, so it has dimension four, the same as $M_2(\mathbb{R})$; the assignment $e_{1}\mapsto\sigma_{1}$, $e_{2}\mapsto\sigma_{3}$ respects the relations because $\sigma_{1}^{2}=\sigma_{3}^{2}=I$ and the two anticommute, so it extends to a homomorphism of algebras of the same dimension, which is an isomorphism.

**Corollary.** The even part of $Cl(2)$ is spanned by $1$ and $e_{1}e_{2}$, and it is isomorphic to $\mathbb{C}$.

**Proof.** The even products are $1$ and $e_{1}e_{2}$, and $(e_{1}e_{2})^{2}=-e_{1}^{2}e_{2}^{2}=-1$; the span is therefore a two-dimensional real algebra with an element of square minus one, which is $\mathbb{C}$.

**Corollary.** The rotor of a plane rotation is the even element $e^{tJ/2}$, which is the unit complex number of the half angle.

**Proof.** The element $J$ is the product $e_{1}e_{2}$ up to the identification of the isomorphism, and the exponential stays in the even part because the even part is a subalgebra.

## The Rotor inside $M_2(\mathbb{R})$

**Proposition.** The centraliser of $J$ in $M_2(\mathbb{R})$ is the span of $I$ and $J$, and it is the copy of $\mathbb{C}$ that carries the rotors.

**Proof.** Solving $XJ=JX$ for a real two-by-two matrix forces the two diagonal entries to be equal and the two off-diagonal entries to be opposite, which is the span of $I$ and $J$.

**Corollary.** The rotors of the plane form the circle $a^{2}+b^{2}=1$ inside that copy of $\mathbb{C}$, and the circle is the group of unit complex numbers.

**Proof.** The rotor is $aI+bJ$ with $a^{2}+b^{2}=1$ by the Euler formula, and the multiplication rule of $J$ is the multiplication rule of $i$.

**Corollary.** The rotation group of the plane is the quotient of the rotor circle by the two signs, which is again a circle.

**Proof.** The squaring map of the rotor circle is two-to-one onto the rotation circle.

## The Clifford Algebra of Three-Space

**Theorem.** The Clifford algebra $Cl(3)$ of three-space with the positive definite form is isomorphic to $M_2(\mathbb{C})$.

**Proof.** The generators $e_{1},e_{2},e_{3}$ map to the Pauli matrices, which satisfy the same relations $\sigma_{j}^{2}=I$ and $\sigma_{j}\sigma_{k}+\sigma_{k}\sigma_{j}=0$ for distinct indices; the eight products span $Cl(3)$, which has dimension eight, and the eight Pauli products including the identity are independent; a homomorphism between real algebras of the same dimension with a spanning image is an isomorphism.

**Corollary.** The eight real dimensions of $Cl(3)$ are the eight real dimensions of $M_2(\mathbb{C})$, and the identification is the Pauli representation of the corpus.

**Proof.** The dimension count and the generating set give the identification, and the same assignment of the Pauli matrices to the generators is used in the biquaternion matrix model.

**Corollary.** The rotor of a three-dimensional rotation is an even element of $Cl(3)$, so it lives in a four-dimensional real subspace of $M_2(\mathbb{C})$.

**Proof.** The even elements are the products of an even number of generators, which are spanned by the identity and the three products $e_{2}e_{3}$, $e_{3}e_{1}$, $e_{1}e_{2}$.

## The Even Part Is the Quaternions

**Theorem.** The even part of $Cl(3)$ is isomorphic to the quaternion algebra $\mathbb{H}$.

**Proof.** The three products $e_{2}e_{3}$, $e_{3}e_{1}$, $e_{1}e_{2}$ square to $-1$ and anticommute in pairs, which is the presentation of $\mathbb{H}$ by three imaginary units.

**Corollary.** The quaternions sit inside $M_2(\mathbb{C})$ as the matrices $\begin{pmatrix}\alpha&\beta\\-\bar\beta&\bar\alpha\end{pmatrix}$ with $\alpha,\beta\in\mathbb{C}$, a real subspace of dimension four.

**Proof.** The three imaginary units correspond to $i\sigma_{1}$, $i\sigma_{2}$, $i\sigma_{3}$, whose real span together with the identity is exactly the displayed set; the multiplication is preserved because the Pauli relations are the quaternion relations.

**Corollary.** The determinant of such a matrix is the squared norm of the quaternion, and the trace is twice its real part.

**Proof.** The determinant is $|\alpha|^{2}+|\beta|^{2}$, which is the sum of the four squares, and the trace is $\alpha+\bar\alpha=2\operatorname{Re}\alpha$.

## Why the Quaternion Rotor Leaves $M_2(\mathbb{R})$

**Proposition.** The quaternion algebra is not a subalgebra of $M_2(\mathbb{R})$, while it is a real subspace of $M_2(\mathbb{C})$ closed under multiplication.

**Proof.** A four-dimensional real subalgebra of $M_2(\mathbb{R})$ is all of $M_2(\mathbb{R})$, because the algebra has real dimension four; and $M_2(\mathbb{R})$ has zero divisors, so it is not a division algebra. The quaternions are a division algebra, so they cannot appear as such a subalgebra. Inside $M_2(\mathbb{C})$ the displayed matrices are closed under multiplication and have no zero divisors except zero.

**Corollary.** The rotor of a three-dimensional rotation cannot be a real $2\times2$ matrix, and it needs the complex entries of $M_2(\mathbb{C})$.

**Proof.** The rotor is a unit quaternion, and the quaternions have no real two-by-two model.

**Corollary.** The complexification of the quaternions is $M_2(\mathbb{C})$, so the passage to complex entries is exactly the passage from the rotor of three-space to the full matrix algebra.

**Proof.** Tensoring the quaternion algebra with $\mathbb{C}$ gives a complex algebra of dimension four with no nontrivial two-sided ideals, which is $M_2(\mathbb{C})$.

## The Two Real Forms

**Proposition.** The quaternions and $M_2(\mathbb{R})$ are the two real forms of $M_2(\mathbb{C})$, and they are not isomorphic over $\mathbb{R}$.

**Proof.** The two are real subalgebras of dimension four whose complexification is $M_2(\mathbb{C})$; the first has no zero divisors and the second has many, so they cannot be isomorphic.

**Corollary.** The biquaternion algebra, which is $M_2(\mathbb{C})$ over $\mathbb{C}$ and eight-dimensional over $\mathbb{R}$, contains both real forms, and the choice of a real form is the choice of a real structure on it.

**Proof.** A real structure is a conjugate-linear involution of the algebra, and the fixed points of the two standard involutions are the two real forms.

**Corollary.** The rotor of the plane lives in the real form $M_2(\mathbb{R})$, and the rotor of three-space lives in the real form $\mathbb{H}$, so the two rotors belong to different real forms of the same complex algebra.

**Proof.** The plane rotor is a real two-by-two matrix and the three-space rotor is a quaternion, and the two algebras are the two real forms.

## Summary

The Clifford algebra of the plane is $M_2(\mathbb{R})$, and its even part is the copy of $\mathbb{C}$ spanned by $I$ and $J$, which carries the rotors of plane rotations as unit complex numbers. The Clifford algebra of three-space is $M_2(\mathbb{C})$, and its even part is the quaternion algebra, whose four real dimensions sit inside $M_2(\mathbb{C})$ as the matrices $\begin{pmatrix}\alpha&\beta\\-\bar\beta&\bar\alpha\end{pmatrix}$.

The quaternion algebra is a real form of $M_2(\mathbb{C})$ and has no real two-by-two model, so the rotor of a three-dimensional rotation leaves $M_2(\mathbb{R})$ and needs complex entries. The plane rotor and the three-space rotor therefore live in the two different real forms $M_2(\mathbb{R})$ and $\mathbb{H}$ of the same complex algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Cl(2)$ | the Clifford algebra of the plane, isomorphic to $M_2(\mathbb{R})$ |
| $Cl(3)$ | the Clifford algebra of three-space, isomorphic to $M_2(\mathbb{C})$ |
| $\mathbb{H}$ | the quaternions, the even part of $Cl(3)$ |
| $J$ | the generator of the even part of $Cl(2)$ |
| $\alpha,\beta$ | the complex entries of a quaternion matrix |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the low-dimensional Clifford algebras and their even parts.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the identification of $Cl(3)$ with $M_2(\mathbb{C})$.
- [The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover](the-rotor-as-a-square-root-of-a-rotation-the-two-signs-and-the-double-cover.html), for the rotor in the plane.
- [Rotors Acting on the Bivector Space at $n=2$: the Adjoint Action](rotors-acting-on-the-bivector-space-at-n-2-the-adjoint-action.html), for the action that the rotor produces.
- [The Two Base Fields: $M_2(\mathbb{R})$ inside $M_2(\mathbb{C})$](the-two-base-fields-m2r-inside-m2c.html), for the two real forms at order two.
