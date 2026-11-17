# __The Two Actions of One Group: Adjoint and Congruence__

## Introduction

One group acts on one algebra in two different ways, and the two are distinguished by which involution sits on the right of the element. The **adjoint** action uses the inverse and preserves the product. The **congruence** uses the star and preserves the two Hermitian sectors together with the indefinite form. A rotation acts the same way in both. A boost does not, and the difference between the two actions is exactly the difference between a rotation and a boost.

This article separates the two actions, proves what each preserves, computes where they coincide, states the kernel and the scale ambiguity of each, and answers the question a reader of the block will ask: which of the two is a frame change?

The article assumes *The Group of Unit-Norm Biquaternions* for the group and its inverse, *Algebra and Element Conventions* for the star and the quaternion conjugation, *Norm and Pairing Conventions* for the norm, and *Frame and Metric Conventions* for the two Hermitian sectors. It uses *The Rotations, the Boosts and the Groups* for the automorphism question and *The Lorentz Group as Biquaternion Norm Automorphisms* for the norm-automorphism reading.

## The Two Actions

### The Adjoint

For $\tilde U$ in the group of invertibles and $\tilde Q$ any element,

$$
\mathrm{Ad}_{\tilde U}:\ \tilde Q\ \longmapsto\ \tilde U\tilde Q\tilde U^{-1}.
$$

On the unit-norm group the inverse is the quaternion conjugate, so the same formula reads $\tilde U\tilde Q\tilde U^{\natural}$. The map is defined on the group of invertibles and not only on $G$, which is one of the two places where the two actions differ.

### The Congruence

$$
\mathrm{Cg}_{\tilde U}:\ \tilde Q\ \longmapsto\ \tilde U\tilde Q\tilde U^{*},
$$

with ${}^{*}$ the corpus's star, the anti-involution that fixes the Hermitian sector. The map is defined for every $\tilde U$, invertible or not, and it is the map the block calls **rotor conjugation** when $\tilde U$ is of unit norm.

**A warning on the notation.** The survey writes rotor conjugation as $\tilde U\tilde Q\tilde U^{*}$ and the four-vector action of the Lorentz group as the same expression; the two are one map. The adjoint action is written with the inverse. A reader must not read $\tilde U^{*}$ as $\tilde U^{-1}$: they agree only when $\tilde U$ is $*$-unitary.

### The Table

| | adjoint $\tilde U\tilde Q\tilde U^{-1}$ | congruence $\tilde U\tilde Q\tilde U^{*}$ |
|---|---|---|
| preserves the product | yes | no |
| preserves the two Hermitian sectors | no | yes |
| preserves the indefinite form | yes, because it preserves the norm | yes, because $\det(\tilde U\tilde Q\tilde U^{*})=\lvert\det\tilde U\rvert^{2}N(\tilde Q)$ |
| preserves the trace | yes | only for $*$-unitary $\tilde U$ |
| defined on the group of invertibles | yes | yes |
| defined on all elements | no | yes |
| kernel on $G$ | $\{\pm e_t\}$ | $\{\pm e_t\}$ |
| blind to | any nonzero complex factor | a unit-modulus factor only |

Each row is proved below, and the two rows that decide the physics are the first and the second.

## The Adjoint Preserves the Product

### The Proof

$$
\mathrm{Ad}_{\tilde U}(\tilde Q\tilde P)=\tilde U\tilde Q\tilde P\tilde U^{-1}
=(\tilde U\tilde Q\tilde U^{-1})(\tilde U\tilde P\tilde U^{-1})
=\mathrm{Ad}_{\tilde U}(\tilde Q)\,\mathrm{Ad}_{\tilde U}(\tilde P).
$$

One line, and it is the definition of an algebra automorphism. The identity is fixed and inverses are carried to inverses, so $\mathrm{Ad}_{\tilde U}$ is an automorphism of the associative algebra.

### What Follows

Because it is an automorphism of the product, the adjoint preserves everything the product defines:

- the commutator, and therefore the structure constants of the Lie algebra;
- the norm, $\langle \tilde U\tilde Q\tilde U^{-1}\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}$;
- the spectrum, since similar matrices have equal eigenvalues;
- the trace, since $2\,\mathrm{Sc}(\tilde U\tilde Q\tilde U^{-1})=2\,\mathrm{Sc}\tilde Q$.

This is the action under which the algebra has its own symmetry, and it is the action the *automorphism* language of *The Rotations, the Boosts and the Groups* refers to.

### The Homomorphism

$$
\mathrm{Ad}_{\tilde U\tilde V}=\mathrm{Ad}_{\tilde U}\circ\mathrm{Ad}_{\tilde V},
$$

so the adjoint is a representation of the group of invertibles, of real dimension eight on the eight-dimensional algebra. That representation is not irreducible: it is the six-dimensional adjoint of the Lorentz algebra plus two trivial central directions, as *The Isomorphisms and Their Dimensions* states.

## The Congruence Preserves the Sectors and the Form

### The Two Sectors

The star is an anti-involution, $(XY)^{*}=Y^{*}X^{*}$. Hence

$$
(\tilde U\tilde Q\tilde U^{*})^{*}=\tilde U\tilde Q^{*}\tilde U^{*},
$$

so if $\tilde Q$ is Hermitian the image is Hermitian, and if $\tilde Q$ is anti-Hermitian the image is anti-Hermitian. The congruence therefore preserves each of the two sectors

$$
\mathbb{B}_{\Psi}=\{\tilde Q:\tilde Q^{*}=\tilde Q\},\qquad
\mathbb{B}_{\Phi}=\{\tilde Q:\tilde Q^{*}=-\tilde Q\},
$$

separately, and it does so for every $\tilde U$, invertible or not. The adjoint does neither: for a boost the adjoint of an anti-Hermitian element leaves the sector, which is the subject of a later section.

### The Indefinite Form

Take $\tilde Q\in\mathbb{B}_\Psi$ and write it as the image of a real four-vector, $\tilde Q=q_t+\sum_\eta iq_\eta\vec e_\eta$, with $q_t$ and the $q_\eta$ real. Then

$$
\det\mathsf{M}_2(\tilde U\tilde Q\tilde U^{*})=\det\mathsf{M}_2(\tilde U)\det\mathsf{M}_2(\tilde Q)\overline{\det\mathsf{M}_2(\tilde U)}
=\lvert N(\tilde U)\rvert^{2}\bigl(q_t^{2}-\lvert\vec q\rvert^{2}\bigr),
$$

so on the group of invertibles the congruence preserves the interval exactly, with the factor $\lvert N\rvert^{2}=1$. The indefinite form is

$$
q_t^{2}-\lvert\vec q\rvert^{2}=\det\mathsf{M}_2(\tilde Q)
$$

on the Hermitian slice, and the congruence is its isometry group. That is the statement that the congruence *is* the Lorentz action, and it is the reason the physical reading of this block runs through it.

### What the Congruence Does Not Preserve

$$
\mathrm{Cg}_{\tilde U}(\tilde Q\tilde P)=(\tilde U\tilde Q\tilde U^{*})(\tilde U\tilde P\tilde U^{*})
=\tilde U\tilde Q(\tilde U^{*}\tilde U)\tilde P\tilde U^{*}
\neq\tilde U\tilde Q\tilde P\tilde U^{*}
$$

unless $\tilde U^{*}\tilde U=e_t$. So the congruence is an isometry of the form and not an automorphism of the algebra, and the two properties are different properties. A boost is an isometry of the interval and not an automorphism of the biquaternion product; this single sentence is the algebraic content of the distinction between a rotation and a boost.

## The Coincidence on the Compact Slice

### The Statement

If $\tilde U$ is $*$-unitary, $\tilde U^{*}=\tilde U^{-1}$, and then

$$
\mathrm{Ad}_{\tilde U}=\mathrm{Cg}_{\tilde U}.
$$

The $*$-unitary elements of the group of unit norm are the rotations, $SU(2)$, which is why the article calls this the coincidence on the compact slice.

### Why It Is Only There

Two reasons, and the second is the useful one.

- **Algebraically**, the identity $\tilde U^{*}=\tilde U^{-1}$ is the definition of $*$-unitarity, and it holds on $SU(2)$ and nowhere else in $G$.
- **Geometrically**, a rotation is an automorphism of the algebra and an isometry of the interval at once, while a boost is only the second. The intersection of the automorphism group and the isometry group of the form is the rotation group.

The coincidence is what makes the rotation subgroup unproblematic. On rotations there is no choice of action to make, and every formula of the block that involves rotations only may be written with either. Every formula that involves a boost may not.

### A Check

On a quarter turn about $\vec e_z$ and a random element, the two images agree to $10^{-16}$. On a boost of rapidity $0.8$ and the same element, they differ in the second decimal place and the difference is not small. A computation that accidentally uses the adjoint where the congruence is meant will therefore pass every rotation test and fail every boost test, which is the worst possible failure mode and the reason this section exists.

## Kernel and Scale

### The Kernel on the Group

For $\tilde U\in G$,

$$
\mathrm{Ad}_{\tilde U}=\mathrm{id}\iff \tilde U\ \text{is central}\iff \tilde U=\pm e_t,
$$

and the same for the congruence, since $\tilde U\tilde Q\tilde U^{*}=\tilde Q$ for all $\tilde Q$ forces $\tilde U$ central. So both actions have kernel $\{\pm e_t\}$, and both factor through the Lorentz group:

$$
G/\{\pm e_t\}\cong SO^{+}(1,3).
$$

This is the two-to-one cover of *The Two-Sheeted Cover and the Topology of Boosts in Biquaternionic Form*, read as a statement about kernels.

### The Scale on the Group of Invertibles

The two actions differ in what they are blind to when the group of invertibles is used.

- **The adjoint** is blind to any nonzero complex factor: $\mathrm{Ad}_{\lambda\tilde U}=\mathrm{Ad}_{\tilde U}$ for $\lambda\in\mathbb{C}^{\times}$, because the factor cancels against its inverse. Its true kernel on $\mathbb{B}^{\times}$ is the whole centre $\mathbb{C}^{\times}e_t$, of real dimension two.
- **The congruence** is blind to a unit-modulus factor only: $\mathrm{Cg}_{\lambda\tilde U}=\lvert\lambda\rvert^{2}\mathrm{Cg}_{\tilde U}$. A phase cancels, a real scale does not.

So a scale $r$ is invisible to the adjoint and is a genuine dilatation of the congruence: the congruence sees the modulus and the adjoint does not. This is the algebraic form of the statement that the interval's isometry group contains the scale only through its modulus, and of the further statement that the congruence by a non-invertible element is a conformal map, which *The Conformal Group in Biquaternionic Form* takes up.

### The Phase

For a central phase $\tilde U=e^{i\theta_{\mathrm{pha}}}e_t$ the congruence is the identity on four-vectors, since $\lvert\lambda\rvert^{2}=1$. The phase is therefore invisible to the whole of the geometry of this block, exactly as the menu's dictionary says: it is a factor outside $SL(2,\mathbb{C})$ and it is irrelevant to a frame change.

## Why a Boost Is Invisible to the Adjoint and Visible to the Congruence

### The Time Axis Under the Adjoint

Take a boost of rapidity $\theta_{\mathrm{rpd}}$ along $\vec u_{\mathrm b}$ and the timelike element $ie_t$. Then

$$
\mathrm{Ad}_{\tilde U_{\mathrm b}}(ie_t)=\tilde U_{\mathrm b}\,ie_t\,\tilde U_{\mathrm b}^{-1}=ie_t,
$$

because $ie_t$ is central. The adjoint of a boost fixes the time axis **exactly**, and it fixes the boost axis as well, because a boost lies in the Cartan direction of its own axis and the adjoint of a Cartan element fixes the Cartan. Verified numerically: the adjoint of $ie_t$ by a boost of rapidity $0.8$ returns $ie_t$ to machine precision, and the adjoint of $\vec e_x$ by the same boost returns $\vec e_x$.

This is the precise sense of *invisible*. A boost is an inner automorphism that moves almost nothing that a four-vector reading cares about; it moves the null directions of its own plane, and it fixes the axis and the time direction.

### The Time Axis Under the Congruence

The same element under the congruence gives

$$
\mathrm{Cg}_{\tilde U_{\mathrm b}}(ie_t)=ie_t\tilde U_{\mathrm b}\tilde U_{\mathrm b}^{*}
=i\cosh\theta_{\mathrm{rpd}}\,e_t-\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b},
$$

which is the four-velocity of a frame moving with speed $c\tanh\theta_{\mathrm{rpd}}$ along $-\vec u_{\mathrm b}$. The sign is the passive reading: the frame is boosted along $+\vec u_{\mathrm b}$ and the coordinate velocity of the original rest frame is reversed.

So the congruence moves the time axis, and it moves it by exactly the Lorentz transformation. Verified numerically at rapidity $0.8$: the image is $1.337435\,i e_t-0.888106\,\vec u_{\mathrm b}$ against $\cosh 0.8=1.337435$ and $\sinh 0.8=0.888106$.

### The Sector Argument

The hidden premise of the previous two subsections is that $ie_t$ is a four-vector and must stay one. The adjoint does not keep it: it keeps it only because $ie_t$ is central. On a spatial vector the adjoint of a boost does not even preserve the sector,

$$
\tilde U_{\mathrm b}\,\vec e_y\,\tilde U_{\mathrm b}^{-1}\notin\mathbb{B}_{\Phi}\quad(\vec u_{\mathrm b}=\vec e_x),
$$

because the image is neither Hermitian nor anti-Hermitian. A map that takes four-vectors out of the four-vector sector cannot be the action of a frame change, whatever it does to the time axis.

## Which Action a Frame Change Uses

### The Requirement

A frame change must do three things. It must carry four-vectors to four-vectors, so it must preserve the sector. It must preserve the interval, so it must be an isometry of the indefinite form. It must compose, so it must be a homomorphism.

### The Answer

The congruence satisfies all three. The adjoint satisfies the third and fails the first two on boosts.

$$
\text{a frame change is }\mathrm{Cg}_{\tilde U}:\ \tilde Q\longmapsto\tilde U\tilde Q\tilde U^{*},\qquad \tilde U\in G .
$$

This is the formula the whole block uses, and it is the formula *The Lorentz Transformation as a Biquaternionic Rotation* derives from the component transformation.

### What the Other Action Is For

The adjoint is not idle. It is the action on the algebra's own structure: it is the map under which the multiplication table, the structure constants and the spectrum are invariant, and it is the map that gives the eight-dimensional representation of the group of invertibles. When the block asks what a frame change does to an *algebra element*, it uses the congruence. When it asks how the algebra's own symmetries act, it uses the adjoint. The two questions are different and the answers are different maps.

A short table makes the division of labour explicit:

| question | action |
|---|---|
| what does a boost do to a four-velocity? | congruence |
| what does a boost do to the structure constants? | nothing: the adjoint, which fixes them |
| what does a rotation do? | either; they coincide |
| what does a dilatation do? | congruence, scaled; invisible to the adjoint |

## Summary

The adjoint $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{-1}$ is an algebra automorphism: it preserves the product, the commutator, the norm, the trace and the spectrum. The congruence $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$ is an isometry of the indefinite form: it preserves each Hermitian sector separately and it preserves the interval on the group of invertibles up to $\lvert N\rvert^{2}$. The two coincide exactly on the $*$-unitary elements, that is on the rotations. Both have kernel $\{\pm e_t\}$ on the group of invertibles and both factor through the Lorentz group. On the group of invertibles the adjoint is blind to any complex factor and the congruence to a unit-modulus factor only, so the scale is a genuine dilatation of the congruence and the phase is invisible to both. A boost fixes the time axis and the boost axis under the adjoint and moves the time axis under the congruence, and it does not even preserve the four-vector sector under the adjoint. A frame change is therefore the congruence, and the adjoint is reserved for the algebra's own automorphisms.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathrm{Ad}_{\tilde U}$ | the adjoint action $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{-1}$ |
| $\mathrm{Cg}_{\tilde U}$ | the congruence $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$ |
| ${}^{*}$ | the star, an anti-involution fixing $\mathbb{B}_{\Psi}$ |
| $\natural$ | the quaternion conjugation, the inverse on $G$ |
| $\mathbb{B}_{\Psi}$ | the Hermitian sector |
| $\mathbb{B}_{\Phi}$ | the anti-Hermitian sector, the four-vectors |
| $N$ | the biquaternion norm |
| $G$ | the unit-norm group |

## Further Reading

- S. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, Academic Press, 1978 — inner automorphisms, the adjoint representation of a Lie group and the isometry group of an indefinite form.
- R. A. Horn and C. R. Johnson, *Matrix Analysis*, 2nd ed., Cambridge University Press, 2012 — similarity and congruence transformations, what each preserves, and the inertia theorem for Hermitian forms.
- P. Lounesto, *Clifford Algebras and Spinors*, 2nd ed., Cambridge University Press, 2001 — the distinction between the automorphism group and the Clifford (twisted-adjoint) action in a Clifford algebra, which is the same distinction in another language.
- *The Rotations, the Boosts and the Groups* — the corpus's treatment of the automorphisms and the derivations, of which this article's first action is the group version.
- *The Lorentz Group as Biquaternion Norm Automorphisms* — the same group read as the automorphisms of the norm, with the real slice taken.
- *The Lorentz Transformation as a Biquaternionic Rotation* and *Paravectors and the Geometry of Spacetime* — the congruence in its component form and its paravector form.
