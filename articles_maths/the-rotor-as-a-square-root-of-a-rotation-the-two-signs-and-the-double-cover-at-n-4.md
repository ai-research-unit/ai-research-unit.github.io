# __The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover at $n=4$__

## Introduction

**Every rotation of four-space is the two-sided action $X\mapsto\rho X\rho^{-1}$ of a rotor, the rotors $\rho$ and $-\rho$ give the same rotation, and the map from the rotors to the rotations is a covering of degree two from $\mathrm{Spin}(4)=SU(2)\times SU(2)$ onto $SO(4)$, whose finite shadow is the group of order $32$ of the signed permutations acting on a group of order $64$.**

The article defines the rotor in the biquaternion algebra, proves that the two-sided action is a rotation and that the two signs give the same one, computes the covering and its kernel, exhibits the extraspecial group of order $32$ as the finite shadow of the cover, separates the two components of $O(4)$ from the connected $SO(4)$, and identifies the generator of $\pi_1(SO(4))=\mathbb{Z}_2$ with the belt.

It assumes *Rotors Acting on the Bivector Space: the Adjoint Action at $n=4$* and *The Lie Algebra $\operatorname{Skew}_4\cong\mathfrak{so}(4)$*. The model at order two is *The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover*; the frame that generates the even words is *Rotors Are Even Words in $M_4(\mathbb{C})$: $M_2\oplus M_2$ and $\mathrm{Spin}(4)$*.

## The Rotor and the Two Signs

**Definition.** A **rotor** is an even product $\rho=v_1v_2\cdots v_{2m}$ of unit vectors of the algebra, and a **unit rotor** is one with $\rho\rho^{\natural}=e_t$.

**Proposition.** For a unit rotor the map $\Phi_\rho(X)=\rho X\rho^{\natural}$ preserves the algebra, is real-linear, and preserves the norm $X X^{\natural}$.

**Proof.** $\Phi_\rho(X)\Phi_\rho(X)^{\natural}=\rho X\rho^{\natural}\rho X^{\natural}\rho^{\natural}=\rho X X^{\natural}\rho^{\natural}$, which equals $XX^{\natural}$ when $\rho\rho^{\natural}=e_t$ and the scalar part is central.

**Corollary.** $\Phi_\rho$ is an orthogonal transformation of the four-dimensional real space, and $\Phi_{\rho}\Phi_{\sigma}=\Phi_{\rho\sigma}$.

**Proof.** Preservation of the norm on a real space of dimension four gives orthogonality, and the composition law is associativity.

**Theorem.** $\Phi_\rho=\Phi_{-\rho}$, so the two signs of a rotor give the same rotation.

**Proof.** $(-\rho)X(-\rho)^{\natural}=\rho X\rho^{\natural}$, since the two signs cancel.

**Corollary.** The map from rotors to rotations is at least two to one, and no rotor is its own negative.

**Proof.** The kernel contains $\pm e_t$, which are distinct.

**The square root.** If $\rho^{2}=\sigma$ then $\Phi_\rho^{2}=\Phi_\sigma$, so a rotor is a square root of the rotation it induces only when the induced rotation is the square of another; the useful statement is the other way round, that every rotation has a rotor and the rotor is unique up to sign.

**Proof.** The composition law and the theorem.

## The Two-Sided Action

**Theorem.** Every element of $SO(4)$ is $\Phi_\rho$ for some unit rotor $\rho$, and the rotors form the group $\mathrm{Spin}(4)$.

**Proof.** In the axis-free frame the four left multiplications and the four right multiplications generate a group of signed permutations containing $SO(4)$ in the sense of Lie algebras; at the level of the Lie algebra every antisymmetric matrix is $L_u+R_v$ with $u,v$ imaginary, and exponentiating gives $\Phi_{e^{u}e^{v}}$ with the two one-sided unit quaternions. The rotors form a group because the product of two rotors is a rotor.

**Corollary.** $\mathrm{Spin}(4)\cong SU(2)\times SU(2)$, of real dimension $6$, equal to the dimension of $SO(4)$.

**Proof.** The left unit quaternions form a copy of $SU(2)$ and the right ones another, they commute, and the pair $(-1,-1)$ acts as the identity on the algebra.

**Corollary.** The two-sided action is the general rotor action at order four, while at order three the one-sided action suffices; the second quaternion is the new ingredient of the dimension.

**Proof.** $\mathfrak{so}(3)$ has dimension $3$ and is covered by one copy of $SU(2)$; $\mathfrak{so}(4)$ has dimension $6$ and needs two.

**The two factors as the two isoclinic families.** A rotor which is a single left quaternion gives a left-isoclinic rotation, a single right quaternion gives a right-isoclinic one, and a general rotor is the product of the two.

**Proof.** The left action rotates both planes by the same angle, the right action by opposite angles, and the product adds the two contributions.

## The Double Cover

**Theorem.** The map $\pi:\mathrm{Spin}(4)\to SO(4)$, $\rho\mapsto\Phi_\rho$, is a surjective Lie group homomorphism with kernel $\{\pm e_t\}$, hence a covering of degree two.

**Proof.** Surjectivity is the theorem of the previous section; the kernel is the set of rotors acting trivially, which is $\pm e_t$ because the action is faithful up to sign and the representation is faithful; a homomorphism of Lie groups with discrete kernel of two elements is a covering.

**Corollary.** $\pi_1(SO(4))=\mathbb{Z}_2$, and $\mathrm{Spin}(4)$ is simply connected.

**Proof.** The total space of a covering of a connected manifold with simply connected total space computes the fundamental group of the base as the fibre; $SU(2)\times SU(2)$ is simply connected, and the fibre has two points.

**Corollary.** Every rotation has exactly two rotors, and a continuous path of rotations lifts to a path of rotors only if the path is trivial in $\pi_1$; the full turn is not.

**Proof.** The two preimages and the lifting criterion for coverings.

**The two signs are not a convention.** The sign of a rotor is a genuine ambiguity of the square root: there is no continuous choice of a rotor for a continuous family of rotations going once around the nontrivial loop.

**Proof.** A continuous choice would be a section of the covering, which would split the nontrivial double cover.

## The Finite Shadow

**Theorem.** The sixteen matrices $T_{\mu\nu}=L_{\mu}R_{\nu}$ and their negatives form a group of order $32$, isomorphic to $(Q_8\times Q_8)/\{\pm(1,1)\}$, the central product $Q_8\circ Q_8$.

**Proof.** Each $T_{\mu\nu}$ is a signed permutation of determinant one; the products follow $T_{\mu\nu}T_{\rho\sigma}=\pm T_{\mu\rho,\sigma\nu}$, and the sign bookkeeping is that of the two copies of $Q_8$.

**Corollary.** The group of order $32$ is the image under the double cover of the group $Q_8\times Q_8$ of order $64$, and the kernel is again the pair $\pm(1,1)$.

**Proof.** Each $T_{\mu\nu}$ is the image of the pair $(L_\mu,R_\nu)$ of signed permutation quaternions, and the pair $(-1,-1)$ maps to the identity.

**Corollary.** The finite shadow of the double cover is $64\to32$, the same ratio as $SU(2)\times SU(2)\to SO(4)$, and the group of order $32$ lies inside $SO(4)$.

**Proof.** All the $T_{\mu\nu}$ have determinant one, so they are rotations, and the ratio of the orders is two.

**The extraspecial structure.** The group of order $32$ has centre of order two and is extraspecial, so its finite representation theory shadows the covering exactly.

**Proof.** The centre is $\{\pm\mathrm I_4\}$, and the quotient by it is elementary abelian of order $16$.

## The Two Components

**Theorem.** $O(4)$ has two connected components, distinguished by the sign of the determinant; $SO(4)$ is the identity component and is connected.

**Proof.** The determinant is continuous on $O(4)$ and takes the values $\pm1$; the group $SO(4)$ is the image of the connected group $\mathrm{Spin}(4)$ under a continuous map.

**Corollary.** A reflection is not a rotor action, and every element of $O(4)$ is a rotor action composed with a fixed reflection.

**Proof.** A rotor action has determinant one, so a reflection has determinant minus one and is not of that form; the quotient of the two components is of order two.

**Corollary.** The two components are the two cosets of $SO(4)$ in $O(4)$, and each is a copy of $SO(4)$ as a manifold.

**Proof.** The cosets of the identity component in a Lie group are the components, and the action by a reflection is a diffeomorphism.

**The dimension count.** $\dim SO(4)=6$, $\dim O(4)=6$, and the two components are each of dimension six.

**Proof.** The dimension of a Lie group is that of its Lie algebra, and the two components are diffeomorphic.

## The Loop and the Belt

**Theorem.** The loop $t\mapsto e^{tJ}$ for $t\in[0,2\pi]$, with $J$ a complex structure, is the nontrivial element of $\pi_1(SO(4))$, and its double is contractible.

**Proof.** The loop lifts to $t\mapsto e^{tJ/2}$ in $\mathrm{Spin}(4)$, which returns to $-e_t$ at $t=2\pi$; the lift of the double loop returns to $e_t$, and $SU(2)\times SU(2)$ is simply connected, so the double loop is null-homotopic.

**Corollary.** A full turn of a rigid body does not return its rotor, and two full turns do; the belt is the physical picture of the same statement.

**Proof.** The lift computation and the connectedness of the path space.

**Corollary.** The two signs of the rotor are the two lifts of the same rotation, and only a closed loop that is twice a generator returns to the starting sign.

**Proof.** The kernel of the covering and the computation above.

**The higher groups.** At order four the same argument applies with $\mathrm{Spin}(4)$ replaced by $\mathrm{Spin}(4)$ itself, and the conclusion $\pi_1(SO(4))=\mathbb{Z}_2$ is the same for every order at least three.

**Proof.** The covering $\mathrm{Spin}(n)\to SO(n)$ has kernel of order two and $\mathrm{Spin}(n)$ is simply connected for $n\ge3$.

## Summary

A unit rotor $\rho$ acts by $X\mapsto\rho X\rho^{-1}$, the rotors $\rho$ and $-\rho$ give the same rotation, and every rotation of four-space arises this way: the action is onto with kernel $\{\pm e_t\}$, so $\mathrm{Spin}(4)=SU(2)\times SU(2)$ covers $SO(4)$ with degree two.

At order four the rotor needs two one-sided unit quaternions, one for each factor of $\mathfrak{so}(4)=\mathfrak{sl}_2\oplus\mathfrak{sl}_2$, and the isoclinic rotations are those with one factor real. The finite shadow is the group of order $32$ of the signed permutations, the image of $Q_8\times Q_8$ of order $64$.

$SO(4)$ is connected and $O(4)$ has two components, separated by the sign of the determinant. The generator of $\pi_1(SO(4))=\mathbb{Z}_2$ is the full turn, whose lift changes the sign of the rotor and whose double returns: the belt trick.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho$ | a unit rotor in the biquaternion algebra |
| $\Phi_\rho(X)=\rho X\rho^{\natural}$ | the rotation induced by the rotor |
| $\mathrm{Spin}(4)=SU(2)\times SU(2)$ | the group of rotors |
| $T_{\mu\nu}$ | the sixteen signed permutations and their negatives |
| $Q_8\circ Q_8$ | the central product of order $32$ |
| $\pi_1(SO(4))=\mathbb{Z}_2$ | the fundamental group of the rotations |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for rotors, the two signs and the double cover.
- [Rotors Acting on the Bivector Space: the Adjoint Action at $n=4$](rotors-acting-on-the-bivector-space-at-n-4-the-adjoint-action.html), for the action on the six-dimensional bivector space.
- [Rotors Are Even Words in $M_4(\mathbb{C})$: $M_2\oplus M_2$ and $\mathrm{Spin}(4)$](rotors-are-even-words-in-m4c.html), for the even subalgebra and the frame.
- [Simple and Non-Simple Rotations: One Angle at $n\le3$, Two Angles at $n\ge4$](simple-and-non-simple-rotations-one-angle-at-n-le-3-two-angles-at-n-ge-4.html), for the two angles and the isoclinic families.
- [The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover](the-rotor-as-a-square-root-of-a-rotation-the-two-signs-and-the-double-cover.html), for the case at order two.
