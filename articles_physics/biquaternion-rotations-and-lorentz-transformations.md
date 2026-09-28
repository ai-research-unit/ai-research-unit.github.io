# __Biquaternion Rotations and Lorentz Transformations__

## Introduction

The biquaternion norm fixes what a motion is: the isometries of the form are the transformations that preserve $N$, and they are the rotations, the Lorentz transformations and the reflections. This article reads those motions, together with the double covers that carry them and the reflection formula the norm supplies.

The article is the Geometry slot of the Lie-theoretic block: the algebra is *Biquaternion Lie Algebra*, the group and its exponential are *Biquaternion Lie Group and Exponential Structure*, and the topology of the group is *The Biquaternion Unit Group as a Topological Group*. The reflections and the Cartan–Dieudonné theorem are stated generally in *Versors, Rotors and the Sandwich Action* and *The Clifford, Pin and Spin Groups* of Part II, and their biquaternion case is worked here; the Clifford reading of the algebra is *The Clifford Structure of the Biquaternion Algebra*; the transformation group in full is in *Biquaternion Automorphisms and Derivations*.

Physically the sandwich $\tilde{Q}\mapsto\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{\dagger}$ is the Lorentz transformation of the material sector: the boost is the change of inertial frame and the rotor is the spatial rotation, so that a four-vector of *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* is carried from one frame to another by a biquaternion multiplication. The doubling of the half-angle is the geometric origin of the spinor double cover: the same motion is realised twice in $\mathbb{B}^{\times}_1$, once as $\tilde{\Lambda}$ and once as $-\tilde{\Lambda}$, which is why the carrier of the state of *Biquaternion Quantum Fields* is a spinor and not a vector.

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The biquaternion norm is $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}=\sum_\mu Q_\mu^2$, and $\tilde{Q}$ is a unit exactly when $N(\tilde{Q})\neq0$ (*Biquaternion Norm and Invertibility*). Throughout, a biquaternion is written $\tilde{Q}=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^3 Q_k e_k$.

---

## The Double Covers and the Lorentz Group

The relevant subgroups are: $\mathbb{B}^\times$, the nonzero-norm elements (complex dimension $4$, real dimension $8$); $\mathbb{B}^\times_1$, the unit-norm elements (complex dimension $3$, real dimension $6$); the rotation group $S^3$, the unit-norm real quaternions (real dimension $3$); and the center $\mathbb{C}^\times e_0$ of nonzero scalars (complex dimension $1$, real dimension $2$).

$S^3$ is the maximal compact subgroup of $\mathbb{B}^\times_1$, with Lie algebra the compact rotation subalgebra $\mathrm{K}$ of *Biquaternion Lie Algebra*, §*The Trace-Free Subalgebra*. The center $\{\pm e_0\}$ is discrete, and

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
**Physical reading: the motions of the framework.** The isometries of the norm are the physical motions: $S^3=Sp(1)$ supplies the spatial rotations of the material sector, and $\mathbb{B}^{\times}_1\cong Spin(1,3)$ supplies the Lorentz transformations, the boosts being the hyperbolic directions of the trace-free subalgebra. The two-sided action is the Euclidean reading the informational sector $\mathbb{M}_+$ carries, and its diagonal restriction is the Lorentzian one. Because the rotor acts by conjugation the angle is halved and the map to $SO^+(1,3)$ is two-to-one: the double cover is not an accident of the parametrisation but the statement that a $2\pi$ rotation returns a vector and reverses a spinor, the fact behind the spin-$\tfrac{1}{2}$ behaviour of *Biquaternion Non Relativistic Quantum Theory*.

## Summary

The motions of the biquaternion algebra are the isometries of its biquaternion norm, and they are the rotations and the Lorentz transformations. The unit quaternions $S^3=Sp(1)$ carry the rotations of the definite form by the sandwich $\tilde{Q}\mapsto q\tilde{Q}q^{-1}$, in which the angle is halved and $\pm q$ gives the same rotation: the map $S^3\to SO(3)$ is the double cover $SU(2)\to SO(3)$. Complexifying, the norm-one group $\mathbb{B}^\times_1$ carries the rotations of the indefinite form, and $\mathbb{B}^\times_1/\{\pm e_0\}\cong SO^+(1,3)$ with $\mathbb{B}^\times_1\cong Spin(1,3)$, so that the double cover of the proper orthochronous Lorentz group is realised inside the algebra; the trace-free subalgebra splits into the compact rotation directions and the hyperbolic directions, and it is the boosts generated by the latter that are the isometries of the indefinite form.

The two-sided action $\tilde{Q}\mapsto u\tilde{Q}v$ with independent unit quaternions preserves the Euclidean form and gives $(S^3\times S^3)/\{\pm e_0\}\cong SO(4)$; the one-sided action is its diagonal restriction. The reflections are the maps $\rho_v(x)=-vxv^{-1}=-vx\bar v$ with $N(v)=1$, defined on the Clifford vector subspace $\mathrm{Vect}(\mathbb{B})$ and its real form, where orthogonality and anticommutation coincide; on that subspace every isometry is a product of at most three of them, by Cartan–Dieudonné. The construction is that of *Versors, Rotors and the Sandwich Action* and *The Clifford, Pin and Spin Groups* of Part II, and the full symmetry group of the algebra, wider than its isometries, is in *Biquaternion Automorphisms and Derivations*. Physically these motions are the changes of reference frame and the rotations of the framework: the boost is the change of inertial frame, the rotor the spatial rotation, the two-sided action the Euclidean reading of the informational sector, and the halving of the angle the geometric origin of the spinor double cover.

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

## Further Reading

- John Stillwell, *Naive Lie Theory* (Springer, 2008).
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001).
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997).
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636.
