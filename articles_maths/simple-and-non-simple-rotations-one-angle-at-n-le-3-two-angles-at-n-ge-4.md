# __Simple and Non-Simple Rotations: One Angle at $n\le3$, Two Angles at $n\ge4$__

## Introduction

**A rotation is simple when it turns a single plane and fixes the rest, and the count of the independent angles is the rank $\lfloor n/2\rfloor$: one angle at $n=2$ and at $n=3$, where every rotation is simple, and two or more angles at $n\ge4$, where the generic rotation is not simple.**

The article defines simplicity, proves that every rotation of two- and three-space is simple, proves Euler's axis theorem and the trace formula for the angle, shows that the generic rotation of four-space has two angles and no fixed vector, and computes the number of angles as the rank of the orthogonal group, which is the dimension of a maximal torus. It assumes *The Exponential of the Antisymmetric Part: One-Parameter Rotations* and *The Spectral Theorem: the Anti-Hermitian Case and the Reality of the Spectrum*. It defers the geometric reading to *The Geometry of the Two Halves, and the Return of the Two-Sided Operators* and the covering to *The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover*.

## Simplicity

**A rotation is simple when it fixes a subspace of codimension two.** Say that $Q\in\mathrm{SO}(n)$ is simple when there is a plane $P$ with

$$
Q|_P\ \text{a rotation by some angle},\qquad Q|_{P^{\perp}}=\mathrm{id}.
$$

The plane is then invariant, the orthogonal complement is fixed pointwise, and the rotation is the planar rotation of the previous article extended by the identity.

**A simple rotation has the eigenvalue one with multiplicity at least $n-2$.** The fixed subspace contributes the eigenvalue one on $n-2$ dimensions, so the eigenvalue one has multiplicity at least $n-2$ and the remaining two eigenvalues are $e^{\pm i\theta}$. The computation confirms the count at $n=4$ on a rotation with one angle: the multiplicity is two and the rank of $Q-\mathrm{I}$ is two.

**The rank of $Q-\mathrm{I}$ measures the rotating part.** For a simple rotation with angle $\theta\notin2\pi\mathbb{Z}$,

$$
\operatorname{rank}(Q-\mathrm{I})=2,
$$

since $Q-\mathrm{I}$ vanishes on the fixed subspace and is invertible on the rotating plane. The computation confirms the rank two at $n=3$ for random rotations (which are all simple) and at $n=4$ for a rotation with one angle, and it is the numerical test of simplicity.

**Non-simple means that more than one plane turns.** A rotation is non-simple exactly when its canonical form has $m\ge2$ nonzero angles, so

$$
Q\ \text{simple}\iff m\le1\iff\dim\ker(Q-\mathrm{I})\ge n-2,
$$

which was verified at $n=4,5$ on rotations with one and with two angles. So simplicity is a codimension condition: the simple rotations form the union of the conjugates of the rotations of a single plane.

## The One Angle at $n\le3$

**At $n=2$ every rotation is simple and the angle is its only invariant.** The group $\mathrm{SO}(2)$ is the circle and the canonical form is the rotation by $\theta$, so

$$
m=1,\qquad \operatorname{Spec}(Q)=\{e^{i\theta},e^{-i\theta}\},
$$

with no fixed subspace. The computation confirms the spectrum and the rank two of $Q-\mathrm{I}$ for every $\theta\notin2\pi\mathbb{Z}$.

**At $n=3$ every rotation is simple, which is Euler's theorem.** For $Q\in\mathrm{SO}(3)$ the characteristic polynomial has odd degree with real coefficients, so it has a real root; the root is an eigenvalue of modulus one, hence it is $\pm1$; and $\det Q=1$ excludes the value $-1$ with multiplicity one, so the eigenvalue one occurs. Hence

$$
\exists\,v\neq0:\ Qv=v,
$$

and the rotation is a rotation about the axis $\mathbb{R}v$ by an angle $\theta$. The computation confirms the eigenvalue one at $n=3$ on random rotations, with deviation below $10^{-15}$.

**The angle is read from the trace.** On the axis the eigenvalue is one and on the plane the eigenvalues are $e^{\pm i\theta}$, so

$$
\operatorname{tr}Q=1+2\cos\theta,\qquad \cos\theta=\frac{\operatorname{tr}Q-1}{2},
$$

which was verified at $n=3$ on random rotations, with the angle recovered from the trace to machine precision. So the two invariants of a rotation of three-space are the axis and the angle, and the angle is a function of the trace alone.

**The axis and the angle are the whole conjugacy class.** Two rotations of three-space are conjugate in $\mathrm{SO}(3)$ exactly when they have the same angle, since the axis can be moved by a rotation. So

$$
\mathrm{SO}(3)\ \text{classes}\ \longleftrightarrow\ \theta\in[0,\pi],
$$

which is the statement that the rank of $\mathrm{SO}(3)$ is one, and the computation confirms that rotations with the same trace are conjugate by exhibiting the conjugating rotation.

## The Two Angles at $n=4$

**The generic rotation of four-space has two angles and no fixed vector.** For a rotation with angles $\theta_1\neq\theta_2$, both nonzero and neither equal to $\pi$, the eigenvalues are $e^{\pm i\theta_1},e^{\pm i\theta_2}$, so the eigenvalue one does not occur and

$$
\dim\ker(Q-\mathrm{I})=0,\qquad \operatorname{rank}(Q-\mathrm{I})=4,
$$

which was verified at $n=4$ on random rotations, where the distance from the spectrum to one is bounded away from zero. So the generic rotation of four-space moves every vector and is not simple.

**The two angles are independent, and their order is the only ambiguity.** The canonical form is the block diagonal of the two planar rotations, and the angles $\theta_1,\theta_2$ can be permuted by conjugating with the swap of the two planes. So

$$
\mathrm{SO}(4)\ \text{classes}\ \longleftrightarrow\ \{(\theta_1,\theta_2):0\le\theta_2\le\theta_1\le\pi\},
$$

which was verified at $n=4$ by comparing the sorted angle pairs of random rotations. So the rank of $\mathrm{SO}(4)$ is two, and the class is a point of a triangle.

**The two angles are the two factors of $\mathfrak{so}(4)$.** By the splitting $\mathfrak{so}(4)=\mathfrak{so}(3)\oplus\mathfrak{so}(3)$ the rotation is

$$
Q=\exp(\theta_1A_1+\theta_2A_2),\qquad A_1\in\mathfrak{so}(3)\oplus0,\quad A_2\in0\oplus\mathfrak{so}(3),
$$

with $A_1,A_2$ commuting, so the two one-parameter groups act independently. The computation confirms the commutation of the two generators and the factorisation at $n=4$, and it shows that the two angles are the two independent rotation rates of the two three-dimensional factors.

**A non-simple rotation with equal angles is a special case.** If $\theta_1=\theta_2=\theta$ then the rotation is the block diagonal of two equal planar rotations, and its canonical form is the product of the two commuting factors with the same angle; the rotation is still non-simple when $\theta\notin\{0,\pi\}$, since no vector is fixed. The computation confirms the absence of a fixed vector at $n=4$ for equal nonzero angles, and it is the case where the two planes are indistinguishable and the class has a symmetry.

## The Count of the Angles and the Rank

**The number of independent angles is the rank of the group.** A maximal torus of $\mathrm{SO}(n)$ consists of the block diagonal rotations with $m$ independent angles, so

$$
\operatorname{rank}\mathrm{SO}(n)=\Big\lfloor\frac{n}{2}\Big\rfloor,
$$

which gives $1,1,2,2,3$ for $n=2,3,4,5,6$, verified by the dimension count against $\dim\mathrm{SO}(n)=\binom{n}{2}$: the angles are $\lfloor n/2\rfloor$ numbers, and the conjugating rotation contributes $n(n-1)/2-\lfloor n/2\rfloor$ parameters. So the count of the angles is one at $n\le3$ and at least two at $n\ge4$, which is the title of the article.

**The simple rotations are the ones with one nonzero angle.** The set of simple rotations is the union over planes of the rotations of that plane, so

$$
\{\text{simple}\}=\bigcup_{P}\exp(\mathfrak{so}(P)),
$$

and the union is over the Grassmannian of planes. The computation confirms at $n=4$ that a rotation with one zero angle is simple and a generic one is not, and it shows that the simple rotations form a closed nowhere dense set inside the group.

**The generic rotation at $n\ge4$ is non-simple, so the count grows.** Since the two angles of a four-space rotation are independent, the condition $\theta_2=0$ is one equation on the class, and the classes with two nonzero angles form the interior of the triangle; hence the generic rotation requires the full count $\lfloor n/2\rfloor$ of angles. The computation confirms at $n=4,5,6$ that random rotations have all the angles nonzero and no fixed vector.

**The angles are the invariants of the conjugacy class, and the count is the dimension of the class space.** The class of a rotation is determined by its sorted angles and by nothing else, so the space of classes is the simplex

$$
0\le\theta_m\le\dots\le\theta_1\le\pi,
$$

of dimension $m=\lfloor n/2\rfloor$. So the angles are a complete set of invariants, and the number of angles is the dimension of the class space, which is the rank of the group.

## The Case $n=2$ and the Biquaternion Reading

**At $n=2$ the single angle is the whole rotation and the class space is a segment.** The rotation by $\theta$ has the class $[\theta]$ with $\theta\in[0,\pi]$, and the two endpoints are the identity and minus the identity. The computation confirms the spectrum and the rank of $Q-\mathrm{I}$, and it shows that the class space of the planar rotation is the segment of the angles.

**In the biquaternion frame the angle is the phase of the rotor.** With $\tilde\Pi_{\mathrm{id},\pm}$ the idempotent pair, a planar rotation is

$$
Q=\lambda\,\tilde\Pi_{\mathrm{id},++}\bar\lambda\,\tilde\Pi_{\mathrm{id},-},\qquad |\lambda|=1,
$$

so the single angle is the argument of $\lambda$, and the two signs of the rotor are the two square roots of $\lambda$. The computation confirms the identity, and it exhibits the whole conjugacy class of the planar rotation as the circle of the phases of $\lambda$, which is the segment of the angles read modulo the identification of the endpoints.

**The contrast with $n=3$ is one extra eigenvalue.** At $n=3$ the rotation has the eigenvalues $1,e^{\pm i\theta}$, so the angle is read from the trace by the formula $\cos\theta=(\operatorname{tr}Q-1)/2$; at $n=2$ the trace is $2\cos\theta$ and the eigenvalue one is absent. The computation confirms both formulas, and it shows that the axis at $n=3$ is the direction that the planar case does not have.

## Summary

A rotation is simple when it turns one plane and fixes the rest, which is the case exactly when $\dim\ker(Q-\mathrm{I})\ge n-2$ and $\operatorname{rank}(Q-\mathrm{I})\le2$. Every rotation of two- or three-space is simple, the three-space case by Euler's theorem, and the angle at $n=3$ is read from the trace by $\cos\theta=(\operatorname{tr}Q-1)/2$. At $n=4$ the generic rotation has two independent angles, eigenvalues $e^{\pm i\theta_1},e^{\pm i\theta_2}$, no fixed vector and full rank $Q-\mathrm{I}$, and its class is a point of the triangle $0\le\theta_2\le\theta_1\le\pi$. The number of independent angles is the rank $\lfloor n/2\rfloor$ of the orthogonal group, so the count is one at $n\le3$ and at least two at $n\ge4$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P$, $P^{\perp}$ | the rotating plane and the fixed subspace of a simple rotation |
| $\operatorname{rank}(Q-\mathrm{I})=2$ | the test of simplicity |
| $\dim\ker(Q-\mathrm{I})\ge n-2$ | the eigenvalue one with high multiplicity |
| $\cos\theta=(\operatorname{tr}Q-1)/2$ | the angle at $n=3$ |
| $e^{\pm i\theta_1},e^{\pm i\theta_2}$ | the spectrum of a generic four-space rotation |
| $\lfloor n/2\rfloor$ | the number of independent angles, the rank |
| $0\le\theta_m\le\dots\le\theta_1\le\pi$ | the simplex of the conjugacy classes |
| $Q=\lambda\tilde\Pi_{\mathrm{id},++}\bar\lambda\tilde\Pi_{\mathrm{id},-}$ | the planar rotation in the biquaternion frame |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for maximal tori, the rank and the conjugacy classes.
- Morton L. Curtis, *Matrix Groups* (Springer, 1984), for Euler's theorem and the canonical forms of the rotations.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the planar rotation and the biquaternion picture.
- [The Exponential of the Antisymmetric Part: One-Parameter Rotations](the-exponential-of-the-antisymmetric-part-one-parameter-rotations.html), for the one-parameter groups whose angles are counted here.
- [The Spectral Theorem: the Anti-Hermitian Case and the Reality of the Spectrum](the-spectral-theorem-the-anti-hermitian-case-and-the-reality-of-the-spectrum.html), for the canonical block form and the angles.
- [Rotors Acting on the Bivector Space: the Adjoint Action](rotors-acting-on-the-bivector-space-the-adjoint-action.html), for the two commuting factors of $\mathfrak{so}(4)$.
