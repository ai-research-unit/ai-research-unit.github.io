# __Biquaternion Rotations and Lorentz Transformations__

## Introduction

The biquaternion norm fixes what a motion is: the isometries of the form are the transformations that preserve $N$, and they are the rotations, the Lorentz transformations and the reflections. This article reads those motions, together with the double covers that carry them, the sandwich action of the units on the algebra, its kernel and the reflection formula the norm supplies.

The article is the Geometry slot of the Lie-theoretic block: the algebra is *Biquaternion Lie Algebra*, the group and its exponential are *Biquaternion Lie Group and Exponential Structure*, and the topology of the group is *The Biquaternion Unit Group as a Topological Group*. The reflections and the Cartan–Dieudonné theorem are stated generally in *Versors, Rotors and the Sandwich Action* and *The Clifford, Pin and Spin Groups* of Part II, and their biquaternion case is worked here; the Clifford reading of the algebra is *The Clifford Structure of the Biquaternion Algebra*; the transformation group in full is in *Biquaternion Automorphisms and Derivations*.

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The biquaternion norm is $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}=\sum_\mu Q_\mu^2$, and $\tilde{Q}$ is a unit exactly when $N(\tilde{Q})\neq0$ (*Biquaternion Norm and Invertibility*). Throughout, a biquaternion is written $\tilde{Q}=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^3 Q_k e_k$.

---

## The Double Covers and the Lorentz Group

The unit quaternions are the unit sphere $Sp(1)=S^3$, and they carry the motions of the definite form, with the double cover $SU(2)\to SO(3)$; their complexification $\mathbb{B}^\times_1\cong SL(2,\mathbb{C})$ carries the motions of the indefinite one. The center $\{\pm e_0\}$ of $\mathbb{B}^\times_1$ is discrete, so the quotient is a Lie group, and

$$
\mathbb{B}^\times_1/\{\pm e_0\} \cong SO^+(1,3),
$$

the proper orthochronous Lorentz group, of real dimension $6$. Hence $\mathbb{B}^\times_1$ is a two-sheeted cover of $SO^+(1,3)$ and, being simply connected, is its universal cover: it is the spin group of Lorentzian signature,

$$
\mathbb{B}^\times_1 \cong \mathrm{Spin}(1,3), \qquad \mathrm{B}_0 \cong \mathrm{SO}(1,3).
$$

The Lorentz action is rotor conjugation, $\tilde{Q} \mapsto \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^\dagger$ for $\tilde{\Lambda} \in \mathbb{B}^\times_1$, which preserves $\mathbb{M}_-$ and $N(\tilde{Q})$; its compact part is the rotation family and its non-compact part the hyperbolic rotations, with closed forms in *Biquaternion Elementary Functions*, §*The Exponential in the Two Real Directions*.

## The Rotor and the Sandwich Action

A rotation is performed by conjugation, and the conjugating element is read as a **rotor**. A unit quaternion $q\in S^3$ acts on a biquaternion by the sandwich
$$
\tilde{Q}\mapsto q\,\tilde{Q}\,q^{-1},
$$
and on the imaginary part this is the rotation of $\mathbb{R}^3$ through the angle $\theta$ when $q=\cos\tfrac{\theta}{2}+\sin\tfrac{\theta}{2}\,\hat{n}$. Two features are visible in the formula. The angle appears **halved** in the rotor, since the rotation is applied once for the left factor and once for the right, and a full turn of the rotor, $q\mapsto-q$, is the identity rotation: the map $S^3\to SO(3)$ is two-to-one, which is the double cover $SU(2)\to SO(3)$ of the double covers above. The unit quaternions carry the rotations of the definite form, and their complexification carries the motions of the indefinite one; the construction, with the versor and the sandwich action, is that of *Versors, Rotors and the Sandwich Action* of Part II.

## The Dagger Sandwich

The rotor of the previous section conjugates by a real quaternion and an inverse. The action the corpus uses for the Lorentz transformation of the whole algebra replaces the inverse by the Hermitian conjugate and admits any unit:

$$
\mathrm{H}_{\tilde{Q}}:\ \mathbb{B}\longrightarrow\mathbb{B},\qquad \mathrm{H}_{\tilde{Q}}(x)=\tilde{Q}\,x\,\tilde{Q}^{\dagger},
$$

the **dagger sandwich**. Its carrier is the algebra as a real vector space of dimension eight, with basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$; its group is the group of units; and it satisfies $\mathrm{H}_{\tilde{Q}\tilde{R}}=\mathrm{H}_{\tilde{Q}}\circ\mathrm{H}_{\tilde{R}}$ and $\mathrm{H}_{z\tilde{Q}}=\lvert z\rvert^{2}\mathrm{H}_{\tilde{Q}}$ for a central $z$, so that a central phase does not change the operator.

**Why the dagger.** The involution $\dagger$ splits the algebra into the Hermitian sector $\mathbb{M}_+$ and the anti-Hermitian sector $\mathbb{M}_-$. Among the two-sided maps $x\mapsto AxB$ with $A,B$ invertible, those that carry the fixed space of $\dagger$ into itself are exactly those with $B=\lambda A^{\dagger}$ for a real $\lambda$, and the dagger sandwich is the normalised case $\lambda=1$. A sandwich built from the inverse instead carries $\mathbb{M}_+$ into the fixed space of the conjugated involution $\tilde{Q}\,\dagger\,\tilde{Q}^{-1}$, which is a different involution unless $\tilde{Q}$ is unitary. Since the halves and the sectors are the fixed spaces of the involutions, the subspaces a sandwich preserves are the ones its own involution defines.

**Theorem (the two sectors are preserved).** For every unit $\tilde{Q}$, the sandwich maps $\mathbb{M}_+$ to $\mathbb{M}_+$ and $\mathbb{M}_-$ to $\mathbb{M}_-$.

**Proof.** Let $x\in\mathbb{M}_+$, so that $x^{\dagger}=x$. Then

$$
\left(\tilde{Q}x\tilde{Q}^{\dagger}\right)^{\dagger}=\tilde{Q}^{\dagger\dagger}x^{\dagger}\tilde{Q}^{\dagger}=\tilde{Q}x\tilde{Q}^{\dagger},
$$

so the image is Hermitian and lies in $\mathbb{M}_+$; for $x\in\mathbb{M}_-$ one has $x^{\dagger}=-x$, and the image is anti-Hermitian. $\square$

**Theorem (the scaling of the norm).** For every unit $\tilde{Q}$ and every $x$,

$$
N\bigl(\mathrm{H}_{\tilde{Q}}(x)\bigr)=\lvert N(\tilde{Q})\rvert^{2}N(x).
$$

**Proof.** The biquaternion norm is multiplicative and central, $N(ab)=N(a)N(b)$, and $N(\tilde{Q}^{\dagger})=N(\tilde{Q})^{*}$, because $\dagger$ is the composite of quaternion conjugation, which fixes $N$, with complex conjugation, which conjugates it. Hence $N(\tilde{Q}x\tilde{Q}^{\dagger})=N(\tilde{Q})N(x)N(\tilde{Q})^{*}=\lvert N(\tilde{Q})\rvert^{2}N(x)$. $\square$

On the unit-norm slice, where $\lvert N(\tilde{Q})\rvert=1$, the sandwich is an isometry of the biquaternion norm on both sectors: it is the action of $SL(2,\mathbb{C})$ on the Hermitian forms and on the four-vectors, and it is the covering map onto the proper orthochronous Lorentz group. The Lorentz transformation written above as $\tilde{Q}\mapsto\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{\dagger}$ is the sandwich of a norm-one element, and for it no inverse and no rotation part appear.

**The image of the unit.** Applied to $e_0$ the sandwich returns $\mathrm{H}_{\tilde{Q}}(e_0)=\tilde{Q}\tilde{Q}^{\dagger}$, which is Hermitian and, for a general unit, not central: the centre is not preserved. The image of a traceless element need not be traceless, so the vector subspace is not preserved either.

**The sandwich is not an automorphism.** For general $x,y$,

$$
\mathrm{H}_{\tilde{Q}}(xy)=\tilde{Q}xy\tilde{Q}^{\dagger}\neq\left(\tilde{Q}x\tilde{Q}^{\dagger}\right)\left(\tilde{Q}y\tilde{Q}^{\dagger}\right)=\mathrm{H}_{\tilde{Q}}(x)\mathrm{H}_{\tilde{Q}}(y),
$$

because the insertion required between $x$ and $y$ is $\tilde{Q}^{\dagger}\tilde{Q}$, which is the unit exactly when $\tilde{Q}$ is unitary. The map is a linear action of the group of units on the algebra, and it is an action by automorphisms only on that slice; the automorphisms themselves are in *Biquaternion Automorphisms and Derivations*.

## The Kernel and the Six Subspaces

**Theorem (the kernel is the central circle).** $\mathrm{H}_{\tilde{Q}}=\mathrm{id}$ if and only if $\tilde{Q}=e^{i\theta}e_0$ for some real $\theta$.

**Proof.** If $\mathrm{H}_{\tilde{Q}}(x)=x$ for every $x$, then $x=e_0$ gives $\tilde{Q}\tilde{Q}^{\dagger}=e_0$, so $\tilde{Q}$ is unitary, and an arbitrary $x$ gives $\tilde{Q}x=x\tilde{Q}$, so $\tilde{Q}$ is central; a central unitary is a complex number of modulus one. Conversely such an element acts trivially, its Hermitian conjugate being its inverse. $\square$

The kernel is therefore the circle $U(1)=\{e^{i\theta}e_0\}$ in the centre, of one real dimension: the sandwich is blind to a central phase and to nothing else. On the unit-norm slice it reduces to the two central signs $\{\pm e_0\}$, the intersection of the circle with that slice, and it is this kernel of order two that is the double cover of the Lorentz group by the rotors.

| operator | group | kernel | parameters lost |
|---|---|---|---|
| $\mathrm{H}_{\tilde{Q}}(x)=\tilde{Q}x\tilde{Q}^{\dagger}$ | the units of $\mathbb{B}$ | $U(1)\subset\mathbb{C}_{\mathbb{B}}$ | the circle only |
| $\mathrm{H}_{\tilde{\Lambda}}(x)=\tilde{\Lambda}x\tilde{\Lambda}^{\dagger}$, $N(\tilde{\Lambda})=1$ | the unit-norm slice $SL(2,\mathbb{C})$ | $\{\pm e_0\}$ | the sign |

The action on the six distinguished subspaces is the following. Each entry records whether the image of a general element of the row subspace lies in that same subspace, for a general unit and for a real unit quaternion.

| subspace | $\mathrm{H}_{\tilde{Q}}$, general unit $\tilde{Q}$ | $\mathrm{H}_{\hat{q}}$, real unit quaternion |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ (centre) | no | yes |
| $\mathrm{Vect}(\mathbb{B})$ (vector, $6$-dimensional) | no | yes |
| $\mathbb{H}_{\mathbb{B}}$ (real quaternions) | no | yes |
| $i\mathbb{H}_{\mathbb{B}}$ (antiquaternions) | no | yes |
| $\mathbb{M}_+$ (Hermitian) | yes | yes |
| $\mathbb{M}_-$ (anti-Hermitian) | yes | yes |

The two sectors are preserved for every element; the four subspaces of the scalar–vector and quaternion decompositions are preserved only by the unitary elements, and by them because a real unit quaternion is unitary.

**Theorem (which operators preserve the whole subspace structure).** Let $\tilde{Q}$ be a unit with polar representation $\tilde{Q}=re^{i\alpha}B\hat{q}$, where $r>0$, $\alpha$ is real, $B$ is Hermitian positive of unit norm and $\hat{q}$ is a unit real quaternion. The following are equivalent:

1. the sandwich maps each of the six subspaces to itself;
2. $B=e_0$;
3. $\tilde{Q}=z\hat{q}$ with $z$ central and $\hat{q}$ a unit real quaternion;
4. $\tilde{Q}\tilde{Q}^{\dagger}$ is a positive real multiple of $e_0$.

When they hold, $\mathrm{H}_{\tilde{Q}}=\lvert z\rvert^{2}\mathrm{H}_{\hat{q}}$ is a dilation composed with a rotation of the vector space, and every one of the six subspaces is preserved.

**Proof.** $(3)\Rightarrow(4)$: for $\tilde{Q}=z\hat{q}$ one has $\tilde{Q}\tilde{Q}^{\dagger}=\lvert z\rvert^{2}\hat{q}\hat{q}^{\dagger}=\lvert z\rvert^{2}e_0$, since a real quaternion satisfies $\hat{q}^{\dagger}=\bar{\hat{q}}=\hat{q}^{-1}$. $(4)\Rightarrow(3)$: if $\tilde{Q}\tilde{Q}^{\dagger}=\lambda e_0$ with $\lambda>0$ then $\lvert N(\tilde{Q})\rvert=\lambda$, the element $\tilde{Q}/\rho$, with $\rho$ the principal square root of $N(\tilde{Q})$, has unit norm and Hermitian square $e_0$, hence is $e^{i\alpha}\hat{q}$ with $\hat{q}$ a unit real quaternion, and $\tilde{Q}$ is of the form $(3)$. $(2)\Leftrightarrow(3)$ is immediate from the polar form. $(3)\Rightarrow(1)$: a central factor contributes the dilation, which preserves every subspace, and $\mathrm{H}_{\hat{q}}$ is the rotation of the vector space, which does the same. $(1)\Rightarrow(4)$: if the centre is preserved then $\tilde{Q}\tilde{Q}^{\dagger}$ is central; that element is Hermitian positive of norm $\lvert N(\tilde{Q})\rvert^{2}>0$, and a central Hermitian positive element of the algebra is a positive real multiple of $e_0$. $\square$

The multiplicative criterion and this one meet on the unitary elements: the operators that are multiplicative are exactly those with $\tilde{Q}\tilde{Q}^{\dagger}=e_0$, which are also the elements fixing the time axis, $\mathrm{H}_{\tilde{Q}}(ie_0)=i\tilde{Q}\tilde{Q}^{\dagger}=ie_0$. On the unit-norm slice the operators preserving the subspace structure form

$$
\left\{\mathrm{H}_{\hat{q}}:\hat{q}\hat{q}^{\dagger}=e_0\right\}\cong SU(2)/\{\pm e_0\}\cong SO(3),
$$

of real dimension three; with the dilations admitted they form $\mathbb{R}_{>0}\times SO(3)$, of real dimension four. The rotation group sits inside the six-dimensional operator group as the rotations sit inside the Lorentz group, and the remaining three dimensions are the boosts, which move the centre, the vector subspace and the two halves.

## Orbits, the Invariants and the Infinitesimal Operator

The sandwich preserves the rank of the matrix image $\Phi(x)$ (*Biquaternion 2×2 Matrix Representation*) and scales the biquaternion norm by $\lvert N(\tilde{Q})\rvert^{2}$, the scaling being one on the unit-norm slice. The rank is unchanged because a congruence by an invertible matrix does not change it, and the biquaternion norm is the determinant. The two invariants cut the algebra as follows.

| invariant | value | meaning |
|---|---|---|
| $\operatorname{rank}\Phi(x)=2$ | $N(x)\neq0$ | $x$ is a unit |
| $\operatorname{rank}\Phi(x)=1$ | $N(x)=0$, $x\neq0$ | $x$ is a zero divisor of rank one |
| $\operatorname{rank}\Phi(x)=0$ | $x=0$ | the origin |

Off the unit-norm slice every orbit is rescaled by the same positive factor, so it is enough to classify the orbits on the slice. There the two sectors carry the classification the four-vector calculus uses: on $\mathbb{M}_+$ the Hermitian forms are classified by their signature, and on $\mathbb{M}_-$ the four-vectors split into the timelike, the null and the spacelike classes, with the proper orthochronous component, so that the two time directions are not mixed. The non-zero zero divisors are the null cone, and on the slice they form a single orbit, which is the sense in which the light cone is one geometric object rather than a union of the cones of individual four-vectors.

**Proposition (the infinitesimal operator).** Let $X\in\mathbb{B}$ and let $x$ be fixed. Then

$$
\left.\frac{d}{dt}\right|_{t=0}\mathrm{H}_{e_0+tX}(x)=Xx+xX^{\dagger}.
$$

**Proof.** Since $\mathrm{H}_{\tilde{Q}}(x)=\tilde{Q}x\tilde{Q}^{\dagger}$, differentiating the product at $\tilde{Q}=e_0$ gives $\dot{\tilde{Q}}x+x\dot{\tilde{Q}}^{\dagger}=Xx+xX^{\dagger}$. $\square$

The formula contains the two symmetries of the algebra in one expression. Along the anti-Hermitian directions, $X^{\dagger}=-X$, the infinitesimal operator is the commutator $[X,x]$, the infinitesimal rotation; along the Hermitian directions, $X^{\dagger}=X$, it is the anticommutator $Xx+xX$, the infinitesimal boost. Restricted to the unit-norm slice the operator group is $SL(2,\mathbb{C})$ acting by the sandwich, with Lie algebra $\mathrm{SL}(2,\mathbb{C})$ regarded over $\mathbb{R}$, of real dimension six: the anti-Hermitian generators give the rotations and the Hermitian ones the boosts. The adjoint maps are in *Biquaternion Lie Algebra* and the exponential in *Biquaternion Lie Group and Exponential Structure*.

## Reflections

The sandwich also realises the **reflections**, on the subspaces where the multiplication is Clifford. Let $v\in\mathbb{B}$ with $N(v)=1$; the reflection in the hyperplane $v^{\perp}$ is the linear map
$$
\rho_v(x)=-v\,x\,v^{-1}=-v\,x\,\bar{v},
$$
the second equality using $v^{-1}=\bar{v}/N(v)=\bar{v}$ for a norm-one element.

**Theorem.** For $v$ with $N(v)=1$ the map $\rho_v$ preserves the biquaternion norm and its polar form, satisfies $\rho_v(v)=-v$, and fixes pointwise every element that anticommutes with $v$; its square is the conjugation $\rho_v^2(x)=v^2xv^{-2}$.

**Proof.** Since $v$ is invertible, $\rho_v$ is a linear automorphism, and $N(\rho_v(x))=N(v)N(x)N(v)^{-1}=N(x)$ by multiplicativity of the norm, whence the polar form is preserved too; the statement $\rho_v(v)=-vvv^{-1}=-v$ is immediate. If $x$ anticommutes with $v$, then $-vxv^{-1}=xv\,v^{-1}=x$, so $x$ is fixed. The square is $\rho_v(\rho_v(x))=v(vxv^{-1})v^{-1}=v^2xv^{-2}$, a conjugation by $v^2$, and it is the identity exactly when $v^2$ is a scalar. $\square$

**Remark (which subspaces carry the reflections).** For the formula to be a genuine reflection, orthogonality and anticommutation must coincide on the ambient subspace. This happens when the multiplication is Clifford there: on the vector subspace $\mathrm{Vect}(\mathbb{B})=\mathbb{C}\{e_1,e_2,e_3\}$ and its real form $\mathbb{R}\{e_1,e_2,e_3\}$ one has
$$
vx+xv=-2B(v,x)\,e_0,
$$
so the hyperplane $v^{\perp}$ is exactly the set of elements anticommuting with $v$, and $\rho_v$ fixes $v^{\perp}$ pointwise, negates $v$, and has complex-linear determinant $-1$. Here $v^2=-\bigl(\sum_k v_k^2\bigr)e_0$ is a scalar, so $\rho_v$ is an involution. On the quaternion and Hermitian subspaces the elements do not anticommute, and a norm-one element acts there by conjugation as a rotation rather than as a reflection. On the algebra as a whole, likewise, $\rho_v$ has determinant $+1$ for every $v$ with $N(v)=1$, so the maps attached to the finite groups of units are rotations and not reflections; and on $\mathbb{H}_{\mathbb{B}}$ the norm-one element $e_0$ is central, so $\rho_{e_0}=-\mathrm{id}$ and nothing is fixed.

**Theorem (Cartan–Dieudonné in the biquaternion algebra).** On the complex three-dimensional vector subspace $\mathrm{Vect}(\mathbb{B})$ and on its real form $\mathbb{R}\{e_1,e_2,e_3\}$, every isometry is a product of at most three reflections $\rho_v$ with $N(v)=1$.

**Proof.** On these subspaces $N(v)=v_1^2+v_2^2+v_3^2$ is a non-degenerate form, and by the theorem above the maps $\rho_v$ with $N(v)=1$ are its reflections in the hyperplanes $v^{\perp}$; the Cartan–Dieudonné theorem, stated for a general vector space in *The Clifford, Pin and Spin Groups*, then gives generation by at most $\dim W=3$ reflections. $\square$

**Remark.** The reflections of this section are attached to the odd part $\mathrm{Vect}(\mathbb{B})$; the Lorentz reflections are not of the shape $\rho_v$ and live in the Clifford layer, not in $\mathbb{B}$.

## Rotations, Boosts and the Two-Sided Action

Over the reals the trace-free subalgebra splits into the compact rotation directions $\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ and the hyperbolic directions $\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$ (*Biquaternion Lie Algebra*). A **rotation** is the motion generated by the first, an element of the compact group $S^3$ of the rotation family; a **boost**, or hyperbolic rotation, is the motion generated by the second, an isometry of the indefinite form that fixes a timelike direction and leaves the light cone invariant. Both are boosts or rotations of the form the algebra carries, and together they generate the Lorentz group $SO^+(1,3)$ of the double covers above; the rotations are the isometries of the definite form, the boosts those of the indefinite one, and the closed forms of their exponentials are in *Biquaternion Elementary Functions*.

A **two-sided** action, $\tilde{Q}\mapsto u\,\tilde{Q}\,v$ with $u,v\in S^3$ independent, is a four-dimensional rotation: the pair $(u,v)$ acts on $\mathbb{B}\cong\mathbb{R}^8$ preserving the Euclidean form, with kernel $\{\pm(e_0,e_0)\}$, so the two-sided action realises
$$
(S^3\times S^3)/\{\pm e_0\}\cong SO(4)
$$
on the algebra. The one-sided action is its diagonal restriction, and the Lorentzian motions are obtained from the complexification instead.

## Summary

The motions of the biquaternion algebra are the isometries of its biquaternion norm, and they are the rotations and the Lorentz transformations. The unit quaternions $S^3=Sp(1)$ carry the rotations of the definite form by the sandwich $\tilde{Q}\mapsto q\tilde{Q}q^{-1}$, in which the angle is halved and $\pm q$ gives the same rotation: the map $S^3\to SO(3)$ is the double cover $SU(2)\to SO(3)$. Complexifying, the norm-one group $\mathbb{B}^\times_1$ carries the rotations of the indefinite form, and $\mathbb{B}^\times_1/\{\pm e_0\}\cong SO^+(1,3)$ with $\mathbb{B}^\times_1\cong Spin(1,3)$, so that the double cover of the proper orthochronous Lorentz group is realised inside the algebra; the trace-free subalgebra splits into the compact rotation directions and the hyperbolic directions, and it is the boosts generated by the latter that are the isometries of the indefinite form.

The action that carries these motions on the whole algebra is the dagger sandwich $\mathrm{H}_{\tilde{Q}}(x)=\tilde{Q}x\tilde{Q}^{\dagger}$. It preserves the two Hermitian sectors and no other pair of the six subspaces, it scales the biquaternion norm by $\lvert N(\tilde{Q})\rvert^{2}$ and preserves it on the unit-norm slice, and its kernel is the central circle $U(1)$, which reduces to $\{\pm e_0\}$ on the slice and is the double cover. It is multiplicative exactly on the unitary elements, its infinitesimal form is $Xx+xX^{\dagger}$, the commutator along the anti-Hermitian directions and the anticommutator along the Hermitian ones, and the operators preserving the whole subspace structure are exactly the central multiples of the real unit quaternions, giving $SO(3)$ on the slice and $\mathbb{R}_{>0}\times SO(3)$ with the dilations admitted.

The two-sided action $\tilde{Q}\mapsto u\tilde{Q}v$ with independent unit quaternions preserves the Euclidean form and gives $(S^3\times S^3)/\{\pm e_0\}\cong SO(4)$; the one-sided action is its diagonal restriction. The reflections are the maps $\rho_v(x)=-vxv^{-1}=-vx\bar v$ with $N(v)=1$, defined on the Clifford vector subspace $\mathrm{Vect}(\mathbb{B})$ and its real form, where orthogonality and anticommutation coincide; on that subspace every isometry is a product of at most three of them, by Cartan–Dieudonné. The construction is that of *Versors, Rotors and the Sandwich Action* and *The Clifford, Pin and Spin Groups* of Part II, and the full symmetry group of the algebra, wider than its isometries, is in *Biquaternion Automorphisms and Derivations*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $N(\tilde{Q})$ | Biquaternion norm; the invariant of the motions |
| $S^3=Sp(1)$ | Unit quaternions; rotors of the definite form |
| $q\tilde{Q}q^{-1}$ | Sandwich action; rotor conjugation |
| $\rho_v(x)=-vxv^{-1}=-vx\bar v$ | Reflection in $v^{\perp}$ on $\mathrm{Vect}(\mathbb{B})$, $N(v)=1$ |
| $vx+xv=-2B(v,x)e_0$ | Anticommutation as orthogonality on $\mathrm{Vect}(\mathbb{B})$; then $v^{\perp}=\{x:xv=-vx\}$ |
| Cartan–Dieudonné | Every isometry of $\mathrm{Vect}(\mathbb{B})$ is at most three reflections $\rho_v$ |
| $S^3\to SO(3)$ | Double cover $SU(2)\to SO(3)$; $\pm q$ give the same rotation |
| $\mathbb{B}^\times_1\cong Spin(1,3)$ | Norm-one group as the spin group; double cover of $SO^+(1,3)$ |
| $\mathbb{B}^\times_1/\{\pm e_0\}\cong SO^+(1,3)$ | Proper orthochronous Lorentz group |
| $\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ | Rotation directions; compact |
| $\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$ | Hyperbolic (boost) directions |
| $u\tilde{Q}v$ | Two-sided action; preserves the Euclidean form |
| $(S^3\times S^3)/\{\pm e_0\}\cong SO(4)$ | Two-sided action as four-dimensional rotations |
| $\mathrm{H}_{\tilde{Q}}(x)=\tilde{Q}x\tilde{Q}^{\dagger}$ | The dagger sandwich; the action of a unit on the algebra |
| $\mathrm{H}_{z\tilde{Q}}=\lvert z\rvert^{2}\mathrm{H}_{\tilde{Q}}$ | Central phase invisible; modulus as the dilation |
| $N(\mathrm{H}_{\tilde{Q}}(x))=\lvert N(\tilde{Q})\rvert^{2}N(x)$ | Scaling of the norm; an isometry on the unit-norm slice |
| $U(1)=\{e^{i\theta}e_0\}$ | Kernel of the sandwich; $\{\pm e_0\}$ on the unit-norm slice |
| structure theorem | Operators preserving all six subspaces: the central multiples of the real unit quaternions |
| $Xx+xX^{\dagger}$ | Infinitesimal operator; commutator on $\mathbb{M}_-$, anticommutator on $\mathbb{M}_+$ |

## Further Reading

- John Stillwell, *Naive Lie Theory* (Springer, 2008).
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001).
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997).
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636.
