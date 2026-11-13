# __The Carrier of the Dirac Field__

## Introduction

The Dirac field is the one field of the corpus whose carrier is the whole algebra. That is not a failure of economy. It follows from the equation: the Dirac operator acts by **left multiplication**, and the subspaces of an algebra that survive left multiplication by every element are its left ideals. The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is simple, so all of its left ideals are sums of copies of one minimal left ideal, of complex dimension two. Two copies are needed, and the sum of two is the whole algebra.

So the Dirac field is carried by $\mathbb{B}$, and the splitting of $\mathbb{B}$ into two minimal left ideals is the splitting of the field into its two values. **Each value is carried by a two-dimensional complex carrier, and the field is the pair.**

This article states the carrier, proves the closure, and shows why the material sector cannot replace it. The last point is a theorem and not an opinion: no non-zero subspace of $\mathbb{B}_\Phi$ is a left ideal, so no field carried by the material sector can obey an equation of left multiplication without an extra condition.

## The Operator Acts on One Side

The equation of the companion article is one element multiplying another on the left,

$$
\tilde\nabla_\Phi\tilde\Xi_R=k_m\tilde\Xi_L,
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_L=k_m\tilde\Xi_R ,
$$

with $\tilde\nabla_\Phi$ the gradient of the corpus and $k_m=mc/\hbar$. Every term is a left multiplication: the gradient, its conjugate, and the central coefficient $k_m$. Nothing multiplies on the right, and no term moves an element between subspaces by any other route.

**The carrier condition is therefore one line.** A subspace $V\subseteq\mathbb{B}$ carries a solution of this equation if

$$
\tilde a\,V\subseteq V
\qquad\text{for every }\tilde a\in\mathbb{B},
$$

because the equation must hold for whatever the field is, with no restriction on the coefficients. A subspace with that property is a **left ideal**. The condition is necessary and it is sufficient: if $V$ is a left ideal, both sides of each line lie in $V$ whenever the field does.

## The Minimal Left Ideals

A left ideal of $\mathbb{B}$ is minimal when it contains no smaller non-zero one. Since $\mathbb{B}\cong M_2(\mathbb{C})$ is simple, all minimal left ideals are isomorphic to the defining module $S\cong\mathbb{C}^{2}$, and each is of complex dimension two.

**A concrete form.** With the frame's third unit $\vec e_z$, the two elements

$$
\tilde\Pi_\pm=\tfrac12\bigl(e_t\pm i\vec e_z\bigr)
$$

are idempotents, $\tilde\Pi_\pm^{2}=\tilde\Pi_\pm$, orthogonal, $\tilde\Pi_+\tilde\Pi_-=0$, and they sum to the unit, $\tilde\Pi_++\tilde\Pi_-=e_t$. The two subspaces

$$
S_+=\mathbb{B}\tilde\Pi_+,
\qquad
S_-=\mathbb{B}\tilde\Pi_-,
$$

are minimal left ideals. They are of real dimension four each, they meet only at zero, and together they span the algebra:

$$
\dim_\mathbb{R}S_+=\dim_\mathbb{R}S_-=4,
\qquad
S_+\cap S_-=\{0\},
\qquad
S_++S_-=\mathbb{B}.
$$

**The idempotents are derived and not chosen.** The datum is the frame's third unit, which the companion article already declares in order to read the value of an element. The idempotent is a polynomial in that unit, $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$, so the carrier costs the frame and nothing further.

## The Two Values Are the Two Ideals

The value test of the companion article is right multiplication by $\vec e_z$,

$$
\tilde X\vec e_z=-i\tilde X\ \Longrightarrow\ \text{value }L,
\qquad
\tilde X\vec e_z=+i\tilde X\ \Longrightarrow\ \text{value }R .
$$

The two values are exactly the two ideals. The test and the projection agree:

$$
\tilde X\tilde\Pi_+=\tilde X_L\in S_+,
\qquad
\tilde X\tilde\Pi_-=\tilde X_R\in S_-,
$$

and the agreement was checked on fifty random elements of the algebra with no exception. Read as a containment, the statement is that the part of value $L$ lies in $S_+$ and the part of value $R$ lies in $S_-$. Read as a projection, it is that right multiplication by $\tilde\Pi_\pm$ returns the part.

**The field is the pair and not one member.** A single element of $S_+$ is a two-component object, which is a Weyl field. The massive field needs both ideals, because the mass is the coefficient that relates the two components and neither line of the pair is satisfied by a field confined to one ideal. So the carrier of the Dirac field is $S_++S_-=\mathbb{B}$, and the statement "the field lives in a minimal left ideal" is true of each value and false of the field.

## Closure Is Exact, and It Survives Every Coupling

The left-ideal property is stronger than the closure the other two fields enjoy, and the difference shows the moment a potential is added.

For a member $\tilde X$ of $S_+$ and an **arbitrary** element $\tilde G$ of the algebra, the product $\tilde G\tilde X$ lies in $S_+$:

$$
\tilde G(\tilde X\tilde\Pi_+)=(\tilde G\tilde X)\tilde\Pi_+\in S_+,
$$

with no hypothesis on $\tilde G$ at all. The residue outside $S_+$ was checked over two hundred random pairs and is zero to machine precision.

**This is what a coupling is.** The covariant derivative of the companion articles is a general element multiplying on the left. For the scalar carrier and for the vector carrier, a general left multiplier leaves the carrier. For a minimal left ideal, it does not: any left multiplier is absorbed. So the Dirac field is the only one of the three whose carrier survives an arbitrary coupling, and that is a structural property of being an ideal rather than a subspace.

| carrier | closed under left multiplication by |
| --- | --- |
| $\mathbb{B}_C$ | central elements only |
| $S_\pm$ | **every** element of $\mathbb{B}$ |
| $\mathbb{B}_\Phi$ | no general element |

## Why the Material Sector Cannot Carry It

The tempting proposal is to put the Dirac field in the material sector, on the ground that the gradient is material. The proposal fails, and it fails for a reason that needs no computation.

**The theorem.** No non-zero subspace of $\mathbb{B}_\Phi$ is a left ideal.

**The proof.** Suppose $V\subseteq\mathbb{B}_\Phi$ is a non-zero left ideal. The central $i$ lies in $\mathbb{B}$, so $iV\subseteq V$. But $i$ is central and $i\mathbb{B}_\Phi=\mathbb{B}_\Psi$, so $iV\subseteq\mathbb{B}_\Psi$. Hence $iV\subseteq\mathbb{B}_\Phi\cap\mathbb{B}_\Psi=\{0\}$, which forces $V=\{0\}$, against the hypothesis.

**The same fact as a dimension.** A left ideal of $\mathbb{B}$ has complex dimension at least one, and the intersection of the smallest one with the material sector is

$$
\dim_\mathbb{R}\bigl(S_+\cap\mathbb{B}_\Phi\bigr)=1,
$$

spanned by $i\tilde\Pi_+$. One real dimension of four. The other three dimensions of the spinor carrier are informational, and no choice of frame changes the count, because the count is a dimension of an intersection of two subspaces fixed by the algebra.

**What the material restriction would cost.** A field confined to $\mathbb{B}_\Phi$ and obeying a left-multiplication equation would have to satisfy the extra condition $\{\tilde\nabla_\Phi,\tilde\Xi\}=0$, since $(\tilde\nabla_\Phi\tilde\Xi)^{*}=-\tilde\nabla_\Phi\tilde\Xi$ is equivalent to $\tilde\Xi\tilde\nabla_\Phi=-\tilde\nabla_\Phi\tilde\Xi$. That is a differential constraint on the field which the Dirac equation does not impose, and it removes solutions rather than selecting them.

## The Idempotent Is Derived, Not Chosen

**The objection that used to stand against this carrier has been retired, and the way it was retired is the argument for the carrier.** *The Dirac Equation in Biquaternionic Form* once listed the minimal left ideal among the constructions a Dirac equation does not need, on the ground that an ideal is chosen by an idempotent, that is by a point of a projective line, and a choice the equation does not make has to be justified from outside. The premise is true of a **free** idempotent and false of the one the article uses.

**The idempotent is derived, from a datum the companion already pays.** The value test of the companion declares the frame and reads the value by right multiplication by the frame's third unit $\vec e_z$. The idempotent is a polynomial in that unit, $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$, so naming it adds no datum and no point of a projective line. A free idempotent would indeed be a choice; this one is a function of the frame. The companion now carries the same statement in §*The Approaches the Equation Does Not Need*, where the ideal is kept and the free idempotent is rejected, and the retired rejection is not repeated anywhere in it.

**The value is not merely labelled by the ideal, it is the ideal.** The test $\tilde X\vec e_z=-i\tilde X$ and the projection $\tilde X\tilde\Pi_+=\tilde X$ return the same answer on every element, checked on fifty random elements. So $S_+$ is the value $L$ written as a subspace, and a reader who rejects the ideal has to reject the value test with it.

**What is added is a closure statement, not a subspace.** The value rule says which part is which. The carrier says what happens to a part under an arbitrary left multiplication, and that statement cannot be made without the subspace: it is the left-ideal property, and it is what the gauging argument of §*Closure Is Exact* and the theorem of §*Why the Material Sector Cannot Carry It* both use.

**What the objection correctly forbids.** The field is not confined to a chosen ideal. A field in one ideal is a two-component Weyl field, and the massive field is the pair. The carrier of the field is $\mathbb{B}$; the carriers of its two values are $S_+$ and $S_-$. Both statements are in the companion's spirit, and the second is the one that carries the structure.

## Two Dimensions Is the Whole Content

The carrier of the spinor is two complex dimensional, and the number is not an accident of the construction. The algebra is simple, so it has a single isomorphism class of simple modules; that module has complex dimension two; every carrier of a spin-half field is a copy of it. The scalar carrier of the companion article is complex dimension one, the vector carrier is a real form rather than a complex space — four real dimensions for the potential, three for the spin after the constraint — and the module dimension is what names the spin.

**The two ideals are exchanged by nothing in the equation.** Both are minimal, both are isomorphic, and no element of the algebra maps one onto the other by left multiplication — a left multiplier preserves each value, which is the value rule of the companion article. The pair is therefore not a symmetric object with an internal symmetry; it is two copies related by the mass.

## What Was Checked

The idempotents satisfy $\tilde\Pi_\pm^{2}=\tilde\Pi_\pm$, $\tilde\Pi_+\tilde\Pi_-=0$ and $\tilde\Pi_++\tilde\Pi_-=e_t$, exactly. The two ideals have real dimension four each, meet at zero and span the algebra. The value test and the projection agree on fifty random elements. A product of an arbitrary element with a member of $S_+$ stays in $S_+$ over two hundred trials, with residue below $10^{-15}$. The intersection $S_+\cap\mathbb{B}_\Phi$ is one real dimensional and is spanned by $i\tilde\Pi_+$.

## Summary

The Dirac operator multiplies on the left, so its carrier must be a left ideal. The algebra's left ideals are sums of copies of one minimal left ideal of complex dimension two, and the Dirac field uses two of them: the field is the sum $S_++S_-=\mathbb{B}$, and each value of the field is one summand.

The two ideals are $\mathbb{B}\tilde\Pi_\pm$ with $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$, and the idempotents are derived from the frame's third unit rather than chosen. The value test by right multiplication by $\vec e_z$ returns exactly the two ideals.

Closure under left multiplication is exact for **every** left multiplier, so the Dirac carrier is the only one of the three that survives an arbitrary coupling. The material sector cannot serve: no non-zero subspace of $\mathbb{B}_\Phi$ is a left ideal, because $i$ is central and exchanges the sectors, and the material part of the spinor carrier is one real dimension of four. A field confined to the material sector would satisfy a differential constraint that the Dirac equation does not impose.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | The biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\eta^{2}=-e_t$ |
| $i$ | Central scalar imaginary |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ | The Peirce idempotents, derived from the frame's third unit |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | The two minimal left ideals, real dimension four |
| $\mathbb{B}_\Phi$, $\mathbb{B}_\Psi$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| ${}^{*}$, ${}^{\natural}$ | Hermitian conjugation, quaternion conjugation |
| $L$, $R$ | The values, read by right multiplication by $\vec e_z$ |
| $\tilde\nabla_\Phi$ | The gradient, acting by left multiplication |
| $k_m=mc/\hbar$ | Mass wave number |

## Further Reading

- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), for the equation, the value rule and the argument that the letters are not defined by idempotents.
- [The Carrier of the Klein–Gordon Field](the-carrier-of-the-klein-gordon-field.html), for the carrier of complex dimension one.
- [The Carrier of the Proca Field](the-carrier-of-the-proca-field.html), for the carrier that is a sector.
- [Spin and the Three Elementary Carriers](spin-and-the-three-elementary-carriers.html), for the classification of the carriers by the action that preserves them.
- [Higher Spin from Tensor Products: The Three Carriers and the Absence of a Fourth](higher-spin-from-tensor-products-the-three-carriers-and-the-absence-of-a-fourth.html), for the module category and the dimension of the defining module.
- [Angular Momentum and Spin in Biquaternionic Form](angular-momentum-and-spin-in-biquaternionic-form.html), for the spin operators as elements of the informational sector.
- [Algebra and Element Conventions](algebra-and-element-conventions.html), for the algebra, the units and the conjugations.
