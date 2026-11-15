# __The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover__

## Introduction

**Every rotation at order two has exactly two square roots in the rotation group, the rotors $+e^{tJ/2}$ and $-e^{tJ/2}$, so the squaring map of the circle onto itself is a double cover and the rotor is defined only up to sign.**

The article proves that a rotation has two rotation square roots and no more, computes them from the half angle, describes the squaring map as a covering of degree two with the antipodal deck transformation, shows that a full turn of the rotor returns minus the starting rotor, and reads the same two signs inside $\mathrm{SU}(2)$ where the conjugation action covers the rotations of three-space. It assumes *The Exponential of $\operatorname{Skew}_2$: the Single Rotation Plane*, *The Lie Algebra $\operatorname{Skew}_2$: One Dimension, Hence Abelian* and *Normal $2\times2$ Matrices and the Common Spectral Theorem*.

It follows the corpus article *The Polar Decomposition of a Biquaternion* for the rotor read as a biquaternion of unit length.

## Square Roots inside the Circle

**A rotation at order two is a point of the circle, and its square roots are the two points at half the angle and at half the angle plus a half turn.**

**Proposition.** Let $R=e^{tJ}$ be a rotation. Then $A=e^{tJ/2}$ satisfies $A^{2}=R$, and so does $-A$.

**Proof.** The powers add: $e^{tJ/2}e^{tJ/2}=e^{tJ}$ because both factors are polynomials in $J$; and $(-A)^{2}=A^{2}$ because the two signs multiply to one.

**Corollary.** The two square roots are antipodal points of the circle, and their product is $-I$.

**Proof.** The two roots differ by the sign, and $A\cdot(-A)=-A^{2}=-R$; at the level of the circle the sign is the half turn, which is the antipodal map.

**Corollary.** The two roots are rotations, so the square root of a rotation is again a rotation at order two.

**Proof.** Each is $e^{tJ/2}$ or its negative, and both are orthogonal with determinant one.

## The Two Signs

**The sign of the rotor is not an artefact of the formula: it is the ambiguity of the square root.**

**Proposition.** If $A$ is a rotation and $A^{2}=R$, then $A=\pm e^{tJ/2}$.

**Proof.** A rotation $A$ commutes with $R$; when $t$ is not a multiple of $\pi$ the commutant of $R$ is the two-dimensional algebra spanned by $I$ and $J$, so $A=aI+bJ$ with real $a,b$. Then $A^{2}=(a^{2}-b^{2})I+2abJ$ because $J^{2}=-I$, and matching with $R=\cos t\,I+\sin t\,J$ gives $(a+ib)^{2}=e^{it}$, hence $a+ib=\pm e^{it/2}$ and $A=\pm e^{tJ/2}$. When $R=\pm I$ the same computation with the Euler formula gives the two roots $\pm I$ or $\pm J$, so in every case there are exactly two.

**Corollary.** The squaring map on the rotation group is exactly two-to-one, so the two signs are the whole ambiguity.

**Proof.** Every rotation has at least the two roots displayed, and the proposition shows that there are no others.

**Corollary.** The squaring map is smooth and its derivative never vanishes, so it is a local diffeomorphism.

**Proof.** In the angle coordinate the map is $t\mapsto 2t$ modulo $2\pi$, whose derivative is the constant two, so no derivative vanishes.

## The Double Cover

**Theorem.** The squaring map $R\mapsto R^{2}$ from the circle to itself is a covering of degree two, with deck transformation the antipodal map $R\mapsto-R$.

**Proof.** The map is two-to-one by the previous section, it is a local diffeomorphism, and the two points over a rotation are exchanged by the negation, which is a free involution of the circle.

**Corollary.** The circle is the total space of a double cover of itself, and the quotient by the antipodal map is again a circle.

**Proof.** The quotient of a circle by the antipodal involution is a circle, and the projection is the squaring map.

**Corollary.** The fundamental group of the circle has order two, and the double cover corresponds to the subgroup of index two.

**Proof.** The cover is connected and of degree two, so the subgroup is of index two in $\mathbb{Z}$, and the only such subgroup is the even integers.

## The Rotor of an Angle

**Proposition.** The rotor of the rotation by the angle $t$ is $\pm\bigl(\cos\tfrac{t}{2}\,I+\sin\tfrac{t}{2}\,J\bigr)$, and it turns by half the angle of the rotation.

**Proof.** The Euler formula at the half angle gives $e^{(t/2)J}=\cos\tfrac{t}{2}I+\sin\tfrac{t}{2}J$, and its square is the Euler formula at the angle $t$.

**Corollary.** A rotation by a full turn has the rotors $\pm I$, and a rotation by a half turn has the rotors $\pm J$.

**Proof.** At $t=2\pi$ the half angle is $\pi$ and the rotor is $-I$ or $I$; at $t=\pi$ the half angle is $\pi/2$ and the rotor is $J$ or $-J$.

**Corollary.** The trace of the rotor is $2\cos\tfrac{t}{2}$, so the rotor distinguishes the angle $t$ from $t+2\pi$ by a sign.

**Proof.** The trace is twice the cosine of the half angle, and adding a full turn to $t$ changes the half angle by $\pi$, which changes the cosine to its negative.

## A Full Turn of the Rotor

**Theorem.** Continuous rotation of the rotor through a full turn returns minus the rotor, and only a turn of two full turns returns the rotor itself.

**Proof.** The path $s\mapsto e^{sJ/2}$ for $s$ from $0$ to $2\pi$ starts at $I$ and ends at $-I$, and it is a lift of a full turn of the rotation; a further full turn returns to $I$.

**Corollary.** The rotor is not a function of the rotation alone, and a physical rotation through $360$ degrees changes the sign of the rotor.

**Proof.** The two ends of the path are different matrices with the same square, so the assignment of a rotor to a rotation is not a continuous single-valued choice along the whole circle.

**Corollary.** A continuous choice of a rotor is possible on any interval of angles of length less than a full turn, and not on the whole circle.

**Proof.** On such an interval the half angle varies over an interval of length less than $\pi$, so the rotor stays away from the antipodal point and the choice is continuous; on the whole circle the two ends disagree.

## The Same Signs in $\mathrm{SU}(2)$

**Proposition.** The matrices $\pm e^{i\theta(\vec n\cdot\vec\sigma)/2}$ are unitary with determinant one, and they are the two elements of $\mathrm{SU}(2)$ with the same conjugation action.

**Proof.** The matrix $i\theta(\vec n\cdot\vec\sigma)/2$ is skew-Hermitian and traceless, so its exponential is unitary with determinant one; and the sign does not change the conjugation, since $(-q)X(-q)^{*}=qXq^{*}$.

**Corollary.** The conjugation action of $\mathrm{SU}(2)$ on the traceless Hermitian matrices depends only on the class of the rotor up to sign.

**Proof.** The action is invariant under the replacement of $q$ by $-q$, and $\pm q$ are the two elements with the same action.

**Corollary.** A rotation of the traceless Hermitian space by the angle $2\theta$ is produced by the rotor of the angle $\theta$, so the rotor turns by half the angle in this picture as well.

**Proof.** For $q=e^{i\theta(\vec n\cdot\vec\sigma)/2}$ the conjugated matrix $qXq^{*}$ is the rotation of $X$ about the axis $\vec n$ by the angle $2\theta$, which is the statement that the rotor angle is half the rotation angle.

## Summary

Every rotation at order two has exactly two square roots in the rotation group, namely $e^{tJ/2}$ and its negative, and there are no others. The squaring map of the circle onto itself is therefore a covering of degree two, with the antipodal map as its deck transformation, and the angle of the rotor is half the angle of the rotation.

The ambiguity is not removable: a continuous choice of a rotor is possible only on an arc shorter than a full turn, and a full turn of the rotor returns minus the rotor. The same two signs appear in $\mathrm{SU}(2)$, where $\pm q$ act in the same way on the traceless Hermitian matrices.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R=e^{tJ}$ | a rotation of the plane |
| $e^{tJ/2}$ | the rotor, a square root of $R$ |
| $J$ | the right-angle rotation |
| $\pm q$ | the two rotors in $\mathrm{SU}(2)$ |
| $\vec n\cdot\vec\sigma$ | the traceless Hermitian direction |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for rotors and the double cover in low dimensions.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for covering maps of matrix groups.
- [The Exponential of $\operatorname{Skew}_2$: the Single Rotation Plane](the-exponential-of-skew-2-the-single-rotation-plane.html), for the Euler formula that produces the rotors.
- [Normal $2\times2$ Matrices and the Common Spectral Theorem](normal-2x2-matrices-and-the-common-spectral-theorem.html), for the unitary diagonalisation used in the uniqueness proof.
- [The Spectral Theorem: the Hermitian Case and the Sphere of Idempotents](the-spectral-theorem-the-hermitian-case-and-the-sphere-of-idempotents.html), for the traceless Hermitian space on which the rotor acts.
