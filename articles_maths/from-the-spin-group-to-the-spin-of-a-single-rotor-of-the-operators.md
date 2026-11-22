# __From the Spin Group to the Spin of a Single Rotor: the Sign after $2\pi$ and the Return after $4\pi$__

## Introduction

**The subject.** A rotor is an element of the spin group, a single exponential of a generator, and its action on the module of the operators shows the two-turn phenomenon: after a full rotation the module is multiplied by minus one, and after two full rotations it returns. The article follows one rotor along a curve of the group, computes the holonomy, identifies where the sign lives, and reads the two covers that the group carries.

**The order of the article.** The rotor and its action come first; the sign after a full turn second. The return after two turns follows, then the two covers, and the holonomy closes the article.

**It assumes** *The Spin Group: the Principal Copy, $\operatorname{Sym}^{3}$ and the Kernel $\{\pm\mathrm I\}$*, *The Four Weights of the Module and the Half Angle* and *The One-Sided Operators*. **The row of the elements is** where a rotor turns a vector of space; here it turns an operator, and the operator sees the sign.

**The result in one line.** A rotor $u(\theta)=\exp(\theta\xi/2)$ acts on the module as a rotation of angle $\theta$ in the weight basis, the module changes sign at $\theta=2\pi$ and returns at $\theta=4\pi$, the algebra is unchanged at both, and the sign is a property of the module alone.

**Boundaries.** The weights themselves are *The Four Weights of the Module and the Half Angle*; the kernel is *The Spin Group: the Principal Copy, $\operatorname{Sym}^{3}$ and the Kernel $\{\pm\mathrm I\}$*; the covers of the rotation group are *The Two Pin Groups and the Double Covers of the Orthogonal Group with Inner Conjugation*.

## The Rotor

**Definition.** For a real unit vector $\vec n$ of the vector part, the **rotor** of angle $\theta$ about $\vec n$ is
$$
u(\theta)=\exp\!\left(\tfrac{\theta}{2}\,\xi_{\vec n}\right),\qquad \xi_{\vec n}=\vec n_x\xi_x+\vec n_y\xi_y+\vec n_z\xi_z,
$$
the exponential taken in the operator algebra.

**Theorem.** The rotor is periodic, $u(\theta+4\pi)=u(\theta)$, and $u(\theta+2\pi)=-u(\theta)$. It acts on the module by the diagonal operator with the eigenvalues $e^{i(\theta/2)m}$ on the weight $m$,
$$
u(\theta)\cdot v_m=e^{\,i\theta m/2}\,v_m,\qquad m=\tfrac32,\tfrac12,-\tfrac12,-\tfrac32 .
$$

*Proof.* The generator $\xi_{\vec n}$ has the four weights $2m$ on the module, by the definition of the weights; the exponential multiplies the weight vector $v_m$ by the exponential of $i\theta m$. Periodicity follows because the four values $e^{i\pi m}$ at $\theta=2\pi$ are the four signs of the half-integers, all of which are minus one.

**Corollary.** At $\theta=2\pi$ the module is multiplied by $-1$, and at $\theta=4\pi$ by $+1$.

*Proof.* $e^{2\pi i m}=(-1)^{2m}=-1$ for a half-integer $m$, and $e^{4\pi i m}=1$.

**Corollary.** The algebra, under the conjugation action of the same rotor, is unchanged at $\theta=2\pi$ and at $\theta=4\pi$.

*Proof.* Conjugation by a scalar is the identity, and the two values of the rotor at those angles are central.

**The reading.** One rotor, two behaviours: the module doubles back, the algebra does not. The reason is the half-integer weight, which is the label of the module and not of the algebra.

## The Sign after a Full Turn

**Proposition.** The element $-\mathrm I$ of the group is the rotor of angle $2\pi$, and it acts as minus the identity on the module and as the identity on the algebra.

*Proof.* The rotor of angle $2\pi$ is the exponential of $\pi\xi_{\vec n}$, which equals the central element $-1$ for every unit $\vec n$; its left action is minus the identity, and its conjugation action is trivial.

**Corollary.** The sign after a full turn is independent of the axis, and it is the same for every rotor of angle $2\pi$.

*Proof.* All the rotors of angle $2\pi$ equal the same central element.

**Corollary.** No element of the algebra distinguishes the rotor of angle $2\pi$ from the identity, while every element of the module does.

*Proof.* The conjugation action is trivial on the algebra; the left action is minus the identity on the module.

**The reading.** The sign is not a defect of the construction: it is the difference between the two readings. An observer inside the algebra cannot detect the full turn; an observer inside the module sees a change of sign of the whole state.

## The Return after Two Turns

**Theorem.** The map $\theta\mapsto u(\theta)$ from the circle of angle to the group is a double cover of the circle of rotations, and the module is a faithful module of the covering circle but not of the base.

*Proof.* The angle $\theta$ and the angle $\theta+2\pi$ give opposite elements of the group, and the two are the same rotation because conjugation by $-1$ is trivial; the module distinguishes the two, so it is faithful on the cover and not on the quotient.

**Corollary.** A closed curve of rotations lifts to a path of the group that closes only after two turns, and the holonomy of the lift is the sign.

*Proof.* The lift of the closed curve of rotations ends at the element $-1$ after one turn and at the identity after two.

**Corollary.** The module has no continuous choice of sign along a closed curve of rotations, and the ambiguity is measured by the first Stiefel–Whitney class of the projective quotient.

*Proof.* The two lifts differ by the sign, and the sign is the non-trivial class of the double cover.

**The reading.** The return after two turns is the statement that the group is a double cover and that the module is the space on which the cover acts faithfully. The two turns are not a curiosity of one example: they are forced by the half-integer label.

## The Two Covers

**Proposition.** The group carries two quotients: the rotation group of the vector part, by the kernel $\{\pm\mathrm I\}$, and the projective quotient of the module, by the scalars.

*Proof.* The kernel of the module action is $\{\pm\mathrm I\}$, and the kernel of the action on the projective module is the full centre.

**Corollary.** The projection to the linear group of the module is a quotient by the scalars, and it is not the same quotient as the projection to the rotations.

*Proof.* The two kernels are different: one of order two, the other the circle of scalars intersected with the group.

**Corollary.** A single rotor is an element of the group, and its projective class is what the module of states remembers.

*Proof.* The module is defined up to scalars in the projective reading, and the rotor acts on the classes.

**The reading.** Two covers, one kernel each. The rotation group is the base of the first, the projective linear group the base of the second, and a rotor sits in the group above both. The sign after a full turn is the statement that the first cover is non-trivial; the return after two turns is the statement that its total space is connected.

## The Holonomy

**Definition.** For a curve $\gamma$ in the rotation group with a chosen base point, the **holonomy** is the element of the group that the lift of $\gamma$ produces at the end.

**Proposition.** The holonomy of a closed curve of rotations is $\pm1$, and it is $-1$ exactly when the curve is the projection of a path joining the two lifts of one point.

*Proof.* The lift is unique once a starting point is chosen, and the two possible ends differ by the sign; the sign is $-1$ exactly when the lift does not close.

**Corollary.** The holonomy depends only on the homotopy class of the curve, and it defines a homomorphism from the fundamental group of the rotation group to $\{\pm1\}$.

*Proof.* The lift depends only on the homotopy class, and the endpoint is a sign.

**Corollary.** The non-trivial loop of the rotation group has holonomy $-1$, and it is the loop that a rotor of angle $2\pi$ projects to.

*Proof.* The rotor of angle $2\pi$ is the lift of the trivial loop based at the identity, ending at $-1$.

**The reading.** The holonomy is the group-theoretic form of the sign: a closed path in the base, a sign in the fibre. The algebra sees the base, the module sees the fibre, and the two readings are the two ends of one covering.

## Further Reading

- [The Spin Group: the Principal Copy, $\operatorname{Sym}^{3}$ and the Kernel $\{\pm\mathrm I\}$](the-spin-group-the-principal-copy-and-the-kernel.html), for the group and its kernel.
- [The Four Weights of the Module and the Half Angle](the-four-weights-of-the-module-and-the-half-angle.html), for the half angle and the weights.
- [The Two Pin Groups and the Double Covers of the Orthogonal Group with Inner Conjugation](the-two-pin-groups-and-the-double-covers-of-the-orthogonal-group-with-inner-conjugation.html), for the covering groups in general.
- [The One-Sided Operators](the-one-sided-operators-of-the-biquaternion-algebra.html), for the left action of the group.
