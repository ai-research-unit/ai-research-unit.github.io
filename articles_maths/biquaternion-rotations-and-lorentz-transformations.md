# __Biquaternion Rotations and Lorentz Transformations__

## Introduction

The biquaternion norm fixes what a motion is: the isometries of the form are the transformations that preserve $N$, and they are the rotations, the Lorentz transformations and the reflections. This article reads those motions, together with the double covers that carry them, the sandwich action of the units on the algebra, its kernel and the reflection formula the norm supplies. It also reads the group that carries them: the group of units and its representations, the finite-dimensional representations of the Lorentz group, the defining representation with the two Weyl spinors, the tensor products and the Clebsch–Gordan rule, and the unitary representations with the principal series.

The article is the Geometry slot of the Lie-theoretic block: the algebra is *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, the group and its exponential are *Biquaternion Lie Group and Exponential Structure*, and the topology of the group is *The Biquaternion Unit Group as a Topological Group*. The reflections and the Cartan–Dieudonné theorem are stated generally in *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation* and *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* of Part II, and their biquaternion case is worked here; the Clifford reading of the algebra is *The Clifford Algebra Representation*; the transformation group in full is in *Biquaternion Automorphisms and Derivations*; and the finite groups of units, together with the figures they determine, are *Biquaternion Orders and Finite Groups of Units*.

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The biquaternion norm is $N(\tilde{Q})=\tilde{Q}\tilde{Q}^{\natural}=\sum_\mu Q_\mu^2$, and $\tilde{Q}$ is a unit exactly when $N(\tilde{Q})\neq0$ (*Biquaternion Norm and Invertibility*). Throughout, a biquaternion is written $\tilde{Q}=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^3 Q_k e_k$.

---

## The Double Covers and the Lorentz Group

The unit quaternions are the unit sphere $Sp(1)=S^3$, and they carry the motions of the definite form, with the double cover $SU(2)\to SO(3)$; their complexification $\mathbb{B}^\times_1\cong SL(2,\mathbb{C})$ carries the motions of the indefinite one. The center $\{\pm e_0\}$ of $\mathbb{B}^\times_1$ is discrete, so the quotient is a Lie group, and

$$
\mathbb{B}^\times_1/\{\pm e_0\} \cong SO^+(1,3),
$$

the proper orthochronous Lorentz group, of real dimension $6$. Hence $\mathbb{B}^\times_1$ is a two-sheeted cover of $SO^+(1,3)$ and, being simply connected, is its universal cover: it is the spin group of Lorentzian signature,

$$
\mathbb{B}^\times_1 \cong \mathrm{Spin}(1,3), \qquad \mathrm{B}_0 \cong \mathrm{so}(1,3).
$$

The Lorentz action is rotor conjugation, $\tilde{Q} \mapsto \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$ for $\tilde{\Lambda} \in \mathbb{B}^\times_1$, which preserves $\mathbb{M}_-$ and $N(\tilde{Q})$; its compact part is the rotation family and its non-compact part the hyperbolic rotations, with closed forms in *Biquaternion Elementary Functions*, §*The Exponential in the Two Real Directions*.

## The Rotor and the Sandwich Action

A rotation is performed by conjugation, and the conjugating element is read as a **rotor**. A unit quaternion $q\in S^3$ acts on a biquaternion by the sandwich
$$
\tilde{Q}\mapsto q\,\tilde{Q}\,q^{-1},
$$
and on the imaginary part this is the rotation of $\mathbb{R}^3$ through the angle $\theta$ when $q=\cos\tfrac{\theta}{2}+\sin\tfrac{\theta}{2}\,\hat{n}$. Two features are visible in the formula. The angle appears **halved** in the rotor, since the rotation is applied once for the left factor and once for the right, and a full turn of the rotor, $q\mapsto-q$, is the identity rotation: the map $S^3\to SO(3)$ is two-to-one, which is the double cover $SU(2)\to SO(3)$ of the double covers above. The unit quaternions carry the rotations of the definite form, and their complexification carries the motions of the indefinite one; the construction, with the versor and the sandwich action, is that of *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation* of Part II.

## The Dagger Sandwich

The rotor of the previous section conjugates by a real quaternion and an inverse. The action the corpus uses for the Lorentz transformation of the whole algebra replaces the inverse by the Hermitian conjugate and admits any unit:

$$
\mathrm{H}_{\tilde{Q}}:\ \mathbb{B}\longrightarrow\mathbb{B},\qquad \mathrm{H}_{\tilde{Q}}(\tilde T)=\tilde{Q}\,\tilde T\,\tilde{Q}^{*},
$$

the **dagger sandwich**. Its carrier is the algebra as a real vector space of dimension eight, with basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$, and its group is the group of units. Two laws govern it.

**Proposition (composition).** For all $\tilde{Q}$ and $\tilde{R}$,

$$
\mathrm{H}_{\tilde{Q}\tilde{R}}=\mathrm{H}_{\tilde{Q}}\circ\mathrm{H}_{\tilde{R}}.
$$

**Proof.** $\mathrm{H}_{\tilde{Q}}\bigl(\mathrm{H}_{\tilde{R}}(\tilde T)\bigr)=\tilde{Q}\bigl(\tilde{R}\tilde T\tilde{R}^{*}\bigr)\tilde{Q}^{*}=(\tilde{Q}\tilde{R})\tilde T(\tilde{Q}\tilde{R})^{\dagger}=\mathrm{H}_{\tilde{Q}\tilde{R}}(\tilde T)$, using the anti-automorphism property $(\tilde{Q}\tilde{R})^{\dagger}=\tilde{R}^{*}\tilde{Q}^{*}$. Consequently $\tilde{Q}\mapsto\mathrm{H}_{\tilde{Q}}$ is a homomorphism of the group of units into $GL(\mathbb{B})$.

**Proposition (the central rule).** For every central $A$ and every $\tilde T$,

$$
\mathrm{H}_{A\tilde{Q}}(\tilde T)=\lvert A\rvert^{2}\mathrm{H}_{\tilde{Q}}(\tilde T),
$$

so that a central phase does not change the operator.

**Why the dagger.** The involution ${}^{*}$ splits the algebra into the Hermitian sector $\mathbb{M}_+$ and the anti-Hermitian sector $\mathbb{M}_-$. Among the two-sided maps $\tilde T\mapsto A\tilde TB$ with $A,B$ invertible, those that carry the fixed space of ${}^{*}$ into itself are exactly those with $B=\lambda A^{\dagger}$ for a real $\lambda$, and the dagger sandwich is the normalised case $\lambda=1$. A sandwich built from the inverse instead carries $\mathbb{M}_+$ into a different fixed space: the automorphism $\tilde T\mapsto\tilde{Q}\tilde T\tilde{Q}^{-1}$ preserves the fixed spaces of the involution ${}^{*}$ conjugated by the image of the identity, $A\mapsto\tilde{Q}\tilde{Q}^{*}\bar{A}(\tilde{Q}\tilde{Q}^{*})^{-1}$, which is a different involution as soon as $\tilde{Q}$ is not unitary. Since the halves and the sectors are the fixed spaces of the involutions, the subspaces a sandwich preserves are the ones its own involution defines.

**Theorem (the two sectors are preserved).** For every unit $\tilde{Q}$, the sandwich maps $\mathbb{M}_+$ to $\mathbb{M}_+$ and $\mathbb{M}_-$ to $\mathbb{M}_-$.

**Proof.** Let $\tilde T\in\mathbb{M}_+$, so that $\tilde{T}^{*}=\tilde T$. Then

$$
\left(\tilde{Q}\tilde T\tilde{Q}^{*}\right)^{*}=\tilde{Q}^{*{}^{*}}\tilde{T}^{*}\tilde{Q}^{*}=\tilde{Q}\tilde T\tilde{Q}^{*},
$$

so the image is Hermitian and lies in $\mathbb{M}_+$; for $\tilde T\in\mathbb{M}_-$ one has $\tilde{T}^{*}=-\tilde T$, and the image is anti-Hermitian.

**Theorem (the scaling of the norm).** For every unit $\tilde{Q}$ and every $\tilde T$,

$$
N\bigl(\mathrm{H}_{\tilde{Q}}(\tilde T)\bigr)=\lvert N(\tilde{Q})\rvert^{2}N(\tilde T).
$$

**Proof.** The biquaternion norm is multiplicative and central, $N(ab)=N(a)N(b)$, and $N(\tilde{Q}^{*})=N(\tilde{Q})^{*}$, because ${}^{*}$ is the composite of quaternion conjugation, which fixes $N$, with complex conjugation, which conjugates it. Hence $N(\tilde{Q}\tilde T\tilde{Q}^{*})=N(\tilde{Q})N(\tilde T)N(\tilde{Q})^{*}=\lvert N(\tilde{Q})\rvert^{2}N(\tilde T)$.

On the unit-norm slice, where $\lvert N(\tilde{Q})\rvert=1$, the sandwich is an isometry of the biquaternion norm on both sectors: it is the action of $SL(2,\mathbb{C})$ on the Hermitian forms and on the four-vectors, and it is the covering map onto the proper orthochronous Lorentz group. The Lorentz transformation written above as $\tilde{Q}\mapsto\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$ is the sandwich of a norm-one element, and for it no inverse and no rotation part appear.

**The image of the unit.** Applied to $e_0$ the sandwich returns $\mathrm{H}_{\tilde{Q}}(e_0)=\tilde{Q}\tilde{Q}^{*}$, which is Hermitian and, for a general unit, not central: the centre is not preserved. The image of a traceless element need not be traceless, so the vector subspace is not preserved either.

**The sandwich is not an automorphism.** For general $\tilde T,\tilde P$,

$$
\mathrm{H}_{\tilde{Q}}(\tilde T\tilde P)=\tilde{Q}\tilde T\tilde P\tilde{Q}^{*}\neq\left(\tilde{Q}\tilde T\tilde{Q}^{*}\right)\left(\tilde{Q}\tilde P\tilde{Q}^{*}\right)=\mathrm{H}_{\tilde{Q}}(\tilde T)\mathrm{H}_{\tilde{Q}}(\tilde P),
$$

because the insertion required between $\tilde T$ and $\tilde P$ is $\tilde{Q}^{*}\tilde{Q}$, which is the unit exactly when $\tilde{Q}$ is unitary. The map is a linear action of the group of units on the algebra, and it is an action by automorphisms only on that slice; the automorphisms themselves are in *Biquaternion Automorphisms and Derivations*.

## The Kernel and the Six Subspaces

**Theorem (the kernel is the central circle).** $\mathrm{H}_{\tilde{Q}}=\mathrm{id}$ if and only if $\tilde{Q}=e^{i\theta}e_0$ for some real $\theta$.

**Proof.** If $\mathrm{H}_{\tilde{Q}}(\tilde T)=\tilde T$ for every $\tilde T$, then $\tilde T=e_0$ gives $\tilde{Q}\tilde{Q}^{*}=e_0$, so $\tilde{Q}$ is unitary, and an arbitrary $\tilde T$ gives $\tilde{Q}\tilde T=\tilde T\tilde{Q}$, so $\tilde{Q}$ is central; a central unitary is a complex number of modulus one. Conversely such an element acts trivially, its Hermitian conjugate being its inverse.

The kernel is therefore the circle $U(1)=\{e^{i\theta}e_0\}$ in the centre, of one real dimension: the sandwich is blind to a central phase and to nothing else. On the unit-norm slice it reduces to the two central signs $\{\pm e_0\}$, the intersection of the circle with that slice, and it is this kernel of order two that is the double cover of the Lorentz group by the rotors.

| operator | group | kernel | parameters lost |
|---|---|---|---|
| $\mathrm{H}_{\tilde{Q}}(\tilde T)=\tilde{Q}\tilde T\tilde{Q}^{*}$ | the units of $\mathbb{B}$ | $U(1)\subset\mathbb{C}_{\mathbb{B}}$ | the circle only |
| $\mathrm{H}_{\tilde{\Lambda}}(\tilde T)=\tilde{\Lambda}\tilde T\tilde{\Lambda}^{*}$, $N(\tilde{\Lambda})=1$ | the unit-norm slice $SL(2,\mathbb{C})$ | $\{\pm e_0\}$ | the sign |

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
3. $\tilde{Q}=A\hat{q}$ with $A$ central and $\hat{q}$ a unit real quaternion;
4. $\tilde{Q}\tilde{Q}^{*}$ is a positive real multiple of $e_0$.

When they hold, $\mathrm{H}_{\tilde{Q}}=\lvert A\rvert^{2}\mathrm{H}_{\hat{q}}$ is a dilation composed with a rotation of the vector space, and every one of the six subspaces is preserved.

**Proof.** $(3)\Rightarrow(4)$: for $\tilde{Q}=A\hat{q}$ one has $\tilde{Q}\tilde{Q}^{*}=\lvert A\rvert^{2}\hat{q}\hat{q}^{\dagger}=\lvert A\rvert^{2}e_0$, since a real quaternion satisfies $\hat{q}^{\dagger}=\hat{q}^{\natural}=\hat{q}^{-1}$. $(4)\Rightarrow(3)$: if $\tilde{Q}\tilde{Q}^{*}=\lambda e_0$ with $\lambda>0$ then $\lvert N(\tilde{Q})\rvert=\lambda$, the element $\tilde{Q}/\rho$, with $\rho$ the principal square root of $N(\tilde{Q})$, has unit norm and Hermitian square $e_0$, hence is $e^{i\alpha}\hat{q}$ with $\hat{q}$ a unit real quaternion, and $\tilde{Q}$ is of the form $(3)$. $(2)\Leftrightarrow(3)$ is immediate from the polar form. $(3)\Rightarrow(1)$: a central factor contributes the dilation, which preserves every subspace, and $\mathrm{H}_{\hat{q}}$ is the rotation of the vector space, which does the same. $(1)\Rightarrow(4)$: if the centre is preserved then $\tilde{Q}\tilde{Q}^{*}$ is central; that element is Hermitian positive of norm $\lvert N(\tilde{Q})\rvert^{2}>0$, and a central Hermitian positive element of the algebra is a positive real multiple of $e_0$.

The multiplicative criterion and this one meet on the unitary elements: the operators that are multiplicative are exactly those with $\tilde{Q}\tilde{Q}^{*}=e_0$, which are also the elements fixing the time axis, $\mathrm{H}_{\tilde{Q}}(ie_0)=i\tilde{Q}\tilde{Q}^{*}=ie_0$. On the unit-norm slice the operators preserving the subspace structure form

$$
\left\{\mathrm{H}_{\hat{q}}:\hat{q}\hat{q}^{\dagger}=e_0\right\}\cong SU(2)/\{\pm e_0\}\cong SO(3),
$$

of real dimension three; with the dilations admitted they form $\mathbb{R}_{>0}\times SO(3)$, of real dimension four. The rotation group sits inside the six-dimensional operator group as the rotations sit inside the Lorentz group, and the remaining three dimensions are the boosts, which move the centre, the vector subspace and the two halves.

## Orbits, the Invariants and the Infinitesimal Operator

The sandwich preserves the rank of the matrix image $\Phi(\tilde T)$ (*Biquaternion 2×2 Matrix Element Representation*) and scales the biquaternion norm by $\lvert N(\tilde{Q})\rvert^{2}$, the scaling being one on the unit-norm slice. The rank is unchanged because a congruence by an invertible matrix does not change it, and the biquaternion norm is the determinant. The two invariants cut the algebra as follows.

| invariant | value | meaning |
|---|---|---|
| $\operatorname{rank}\Phi(\tilde T)=2$ | $N(\tilde T)\neq0$ | $\tilde T$ is a unit |
| $\operatorname{rank}\Phi(\tilde T)=1$ | $N(\tilde T)=0$, $\tilde T\neq0$ | $\tilde T$ is a zero divisor of rank one |
| $\operatorname{rank}\Phi(\tilde T)=0$ | $\tilde T=0$ | the origin |

Off the unit-norm slice every orbit is rescaled by the same positive factor, so it is enough to classify the orbits on the slice. There the two sectors carry the classification the four-vector calculus uses: on $\mathbb{M}_+$ the Hermitian forms are classified by their signature, and on $\mathbb{M}_-$ the four-vectors split into the timelike, the null and the spacelike classes, with the proper orthochronous component, so that the two time directions are not mixed. The non-zero zero divisors are the null cone, and on the slice they form a single orbit, which is the sense in which the light cone is one geometric object rather than a union of the cones of individual four-vectors.

**Proposition (the infinitesimal operator).** Let $\dot{\tilde{Q}}\in\mathbb{B}$ and let $\tilde T$ be fixed. Then

$$
\left.\frac{d}{dt}\right|_{t=0}\mathrm{H}_{e_0+t\dot{\tilde{Q}}}(\tilde T)=\dot{\tilde{Q}}\tilde T+\tilde T\dot{\tilde{Q}}^{\dagger}.
$$

**Proof.** Since $\mathrm{H}_{\tilde{Q}}(\tilde T)=\tilde{Q}\tilde T\tilde{Q}^{*}$, differentiating the product at $\tilde{Q}=e_0$ gives $\dot{\tilde{Q}}\tilde T+\tilde T\dot{\tilde{Q}}^{\dagger}$.

The formula contains the two symmetries of the algebra in one expression. Along the anti-Hermitian directions, $X^{\dagger}=-X$, the infinitesimal operator is the commutator $[X,\tilde T]$, the infinitesimal rotation; along the Hermitian directions, $X^{\dagger}=X$, it is the anticommutator $X\tilde T+\tilde TX$, the infinitesimal boost. Restricted to the unit-norm slice the operator group is $SL(2,\mathbb{C})$ acting by the sandwich, with Lie algebra $\mathrm{SL}(2,\mathbb{C})$ regarded over $\mathbb{R}$, of real dimension six: the anti-Hermitian generators give the rotations and the Hermitian ones the boosts. The adjoint maps are in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and the exponential in *Biquaternion Lie Group and Exponential Structure*.

## Reflections

The sandwich also realises the **reflections**, on the subspaces where the multiplication is Clifford. Let $v\in\mathbb{B}$ with $N(v)=1$; the reflection in the hyperplane $v^{\perp}$ is the linear map
$$
\rho_v(\tilde T)=-v\,\tilde T\,v^{-1}=-v\,\tilde T\,v^{\natural},
$$
the second equality using $v^{-1}=v^{\natural}/N(v)=v^{\natural}$ for a norm-one element.

**Theorem.** For $v$ with $N(v)=1$ the map $\rho_v$ preserves the biquaternion norm and its polar form, satisfies $\rho_v(v)=-v$, and fixes pointwise every element that anticommutes with $v$; its square is the conjugation $\rho_v^2(\tilde T)=v^2\tilde Tv^{-2}$.

**Proof.** Since $v$ is invertible, $\rho_v$ is a linear automorphism, and $N(\rho_v(\tilde T))=N(v)N(\tilde T)N(v)^{-1}=N(\tilde T)$ by multiplicativity of the norm, whence the polar form is preserved too; the statement $\rho_v(v)=-vvv^{-1}=-v$ is immediate. If $\tilde T$ anticommutes with $v$, then $-v\tilde Tv^{-1}=\tilde Tv\,v^{-1}=\tilde T$, so $\tilde T$ is fixed. The square is $\rho_v(\rho_v(\tilde T))=v(v\tilde Tv^{-1})v^{-1}=v^2\tilde Tv^{-2}$, a conjugation by $v^2$, and it is the identity exactly when $v^2$ is a scalar.

**Remark (which subspaces carry the reflections).** For the formula to be a genuine reflection, orthogonality and anticommutation must coincide on the ambient subspace. This happens when the multiplication is Clifford there: on the vector subspace $\mathrm{Vect}(\mathbb{B})=\mathbb{C}\{e_1,e_2,e_3\}$ and its real form $\mathbb{R}\{e_1,e_2,e_3\}$ one has
$$
v\tilde T+\tilde Tv=-2B(v,\tilde T)\,e_0,
$$
so the hyperplane $v^{\perp}$ is exactly the set of elements anticommuting with $v$, and $\rho_v$ fixes $v^{\perp}$ pointwise, negates $v$, and has complex-linear determinant $-1$. Here $v^2=-\bigl(\sum_k v_k^2\bigr)e_0$ is a scalar, so $\rho_v$ is an involution. On the quaternion and Hermitian subspaces the elements do not anticommute, and a norm-one element acts there by conjugation as a rotation rather than as a reflection. On the algebra as a whole, likewise, $\rho_v$ has determinant $+1$ for every $v$ with $N(v)=1$, so the maps attached to the finite groups of units are rotations and not reflections; and on $\mathbb{H}_{\mathbb{B}}$ the norm-one element $e_0$ is central, so $\rho_{e_0}=-\mathrm{id}$ and nothing is fixed.

**Theorem (Cartan–Dieudonné in the biquaternion algebra).** On the complex three-dimensional vector subspace $\mathrm{Vect}(\mathbb{B})$ and on its real form $\mathbb{R}\{e_1,e_2,e_3\}$, every isometry is a product of at most three reflections $\rho_v$ with $N(v)=1$.

**Proof.** On these subspaces $N(v)=v_1^2+v_2^2+v_3^2$ is a non-degenerate form, and by the theorem above the maps $\rho_v$ with $N(v)=1$ are its reflections in the hyperplanes $v^{\perp}$; the Cartan–Dieudonné theorem, stated for a general vector space in *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, then gives generation by at most $\dim W=3$ reflections.

**Remark.** The reflections of this section are attached to the odd part $\mathrm{Vect}(\mathbb{B})$; the Lorentz reflections are not of the shape $\rho_v$ and live in the Clifford layer, not in $\mathbb{B}$.

## Rotations, Boosts and the Two-Sided Action

Over the reals the trace-free subalgebra splits into the compact rotation directions $\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ and the hyperbolic directions $\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$ (*The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*). A **rotation** is the motion generated by the first, an element of the compact group $S^3$ of the rotation family; a **boost**, or hyperbolic rotation, is the motion generated by the second, an isometry of the indefinite form that fixes a timelike direction and leaves the light cone invariant. Both are boosts or rotations of the form the algebra carries, and together they generate the Lorentz group $SO^+(1,3)$ of the double covers above; the rotations are the isometries of the definite form, the boosts those of the indefinite one, and the closed forms of their exponentials are in *Biquaternion Elementary Functions*.

A **two-sided** action, $\tilde{Q}\mapsto u\,\tilde{Q}\,v$ with $u,v\in S^3$ independent, is a four-dimensional rotation: the pair $(u,v)$ acts on $\mathbb{B}\cong\mathbb{R}^8$ preserving the Euclidean form, with kernel $\{\pm(e_0,e_0)\}$, so the two-sided action realises
$$
(S^3\times S^3)/\{\pm e_0\}\cong SO(4)
$$
on the algebra. The one-sided action is its diagonal restriction, and the Lorentzian motions are obtained from the complexification instead.

## The Group of Units and Its Representations

The group of units is $\mathbb{B}^{\times} = \{\tilde{Q} : N(\tilde{Q}) \neq 0\}$, which under the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ is the group of invertible matrices, since the biquaternion norm is the determinant (*Biquaternion 2×2 Matrix Element Representation*):

$$
\mathbb{B}^{\times} \cong GL_2(\mathbb{C}),
$$

a connected non-compact complex Lie group of complex dimension $4$ and real dimension $8$, with centre $\mathbb{C}^{\times}$. The unit-norm subgroup is $\mathbb{B}^{\times}_1 \cong SL(2,\mathbb{C})$, of complex dimension $3$ and real dimension $6$, the double cover of the Lorentz group of the preceding section. The unitary biquaternions $\tilde{Q}^{*}\tilde{Q} = e_0$ form $U(2)$, the maximal compact subgroup of $\mathbb{B}^{\times}$, and the unit quaternions form $SU(2) = \mathbb{B}^{\times}_1 \cap U(2)$, the maximal compact subgroup of $SL(2,\mathbb{C})$ and the double cover of $SO(3)$.

**Representations of the unit group.** As a reductive group, $GL_2(\mathbb{C})$ has finite-dimensional algebraic (rational) representations parameterised by highest weights $(\lambda_1, \lambda_2) \in \mathbb{Z}^2$ with $\lambda_1 \geq \lambda_2$; the irreducible one is $\operatorname{Sym}^{\lambda_1 - \lambda_2}(\mathbb{C}^2) \otimes (\det)^{\lambda_2}$, of dimension $\lambda_1 - \lambda_2 + 1$, with central character $A \mapsto A^{\lambda_1 + \lambda_2}$. Restriction to $SL(2,\mathbb{C})$ forgets the determinant twist, leaving the highest weight $2j = \lambda_1 - \lambda_2 \geq 0$, that is, the irreducible $V_j$ below with spin $j \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$.

## Finite-Dimensional Representations of the Lorentz Group

Let $G = SL(2,\mathbb{C})$, with real Lie algebra the traceless $2\times2$ complex matrices (*The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*). Its complexification is a sum of two copies of the special linear algebra, the complexified Lorentz algebra:

$$
\mathrm{so}(1,3)\otimes_{\mathbb{R}}\mathbb{C} \cong \mathrm{sl}(2,\mathbb{C}) \oplus \mathrm{sl}(2,\mathbb{C}),
$$

the two summands corresponding to the self-dual and anti-self-dual parts. Every finite-dimensional smooth complex representation of $G$ is completely reducible, and its irreducible summands are the outer tensor products $(m,n) = V_m \boxtimes V_n$ with $m, n \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$, where $V_j$ denotes the irreducible $\mathrm{SU}(2)$-module of dimension $2j+1$, equivalently the $\mathrm{SL}(2,\mathbb{C})$-module $\operatorname{Sym}^{2j}(\mathbb{C}^2)$ of highest weight $2j$; thus $\dim_{\mathbb{C}}(m,n) = (2m+1)(2n+1)$. The defining representation is $(\tfrac{1}{2}, 0)$ and its complex conjugate is $(0, \tfrac{1}{2})$.

**Polynomial representations.** Relative to a Cartan subalgebra spanned by $h = \operatorname{diag}(1,-1)$, the irreducible $SL(2,\mathbb{C})$-modules are the symmetric powers $V_j \cong \operatorname{Sym}^{2j}(\mathbb{C}^2)$, with spin $j \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$, highest weight $2j$ and dimension $2j+1$. These are exactly the **polynomial** (equivalently holomorphic, equivalently algebraic) finite-dimensional representations of the complex group $G$: their matrix entries are polynomial functions of the entries of $g \in G$, and every finite-dimensional holomorphic representation of $G$ is a direct sum of the $V_j$, hence is parameterised by its highest weight $2j$, that is, by its spin $j \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$. Not every continuous finite-dimensional representation is polynomial: the complex conjugates of the $V_j$ are antiholomorphic and belong to the $(0, j)$ family.

**The unitary trick.** Restriction to the maximal compact subgroup $SU(2)$ is an equivalence of categories

$$
\left\{\text{f.d. polynomial representations of } SL(2,\mathbb{C})\right\} \simeq \left\{\text{f.d. unitary representations of } SU(2)\right\},
$$

so the finite-dimensional polynomial representations of $SL(2,\mathbb{C})$ are obtained from those of $SU(2)$ by complexifying the Lie algebra and exponentiating, and both are parameterised by the same highest weights $2j$, $j \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$. What complexification does not preserve is unitarity, a point taken up in §*Unitary Representations*.

## The Defining Representation and the Weyl Spinors

The defining representation of $SL(2,\mathbb{C})$ is $V_{1/2} = \mathbb{C}^2$, the polynomial representation of highest weight $1$. It is the same space that appears in *Modules over the General Plain Algebra of Biquaternions* as the unique simple module of the algebra $\mathbb{B}$, and the isomorphism $\mathbb{B} \cong \operatorname{End}_{\mathbb{C}}(V_{1/2})$ is the content of the matrix realization (*Biquaternion 2×2 Matrix Element Representation*): choosing a basis of $V_{1/2}$ writes each element of the algebra as a $2 \times 2$ matrix, and the choice of basis is the only freedom in doing so. Under the Lorentz group the defining representation and its conjugate are the two **Weyl spinors**: $V_{1/2} = (\tfrac{1}{2}, 0)$ is the left-handed one and $\overline{V_{1/2}} = (0, \tfrac{1}{2})$ is the right-handed one; they are not isomorphic as complex representations, and parity exchanges them. Their direct sum is the **Dirac spinor**

$$
\Delta = V_{1/2} \oplus \overline{V_{1/2}} = (\tfrac{1}{2},0) \oplus (0,\tfrac{1}{2}), \qquad \dim_{\mathbb{C}} \Delta = 4,
$$

and their tensor product is the **vector representation** $(\tfrac{1}{2}, \tfrac{1}{2}) = V_{1/2} \otimes \overline{V_{1/2}}$, of complex dimension $4$, whose real form is the Lorentz action on the four-dimensional vector space (*Biquaternion Four-Vector Element Representation*). The adjoint representation of the Lorentz algebra is $(1,0) \oplus (0,1)$, of dimension $3 + 3$.

Two dualities must be distinguished. The defining module is **self-dual** as a representation of $SL(2,\mathbb{C})$: since $\det = 1$, the alternating form $\varepsilon(u,v) = u_1 v_2 - u_2 v_1$ is invariant and identifies $V_{1/2}^{*}$ with $V_{1/2}$, so $V_{1/2}^{*} \cong V_{1/2}$. The **conjugate** $\overline{V_{1/2}}$, by contrast, is not isomorphic to $V_{1/2}$; it is the other chirality. Finally, since $-e_0$ acts as $-1$ on $V_{1/2}$, the defining representation, and every $(m,n)$ with $m+n$ half-integral, does not descend to $SO^+(1,3)$.

## Tensor Products and the Clebsch–Gordan Rule

Group representations tensor with the diagonal action $g \cdot (v \otimes w) = (gv) \otimes (gw)$. For the polynomial representations of $SL(2,\mathbb{C})$ the Clebsch–Gordan rule is

$$
V_j \otimes V_k \cong \bigoplus_{l=|j-k|}^{j+k} V_l, \qquad j, k \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}.
$$

The tensor square of the spinor is the simplest nontrivial case:

$$
V_{1/2} \otimes V_{1/2} \cong \operatorname{Sym}^2 V_{1/2} \oplus \Lambda^2 V_{1/2} \cong V_1 \oplus V_0, \qquad \dim_{\mathbb{C}} V_1 = 3, \quad \dim_{\mathbb{C}} V_0 = 1.
$$

The summand $V_1$ is the symmetric square and is the adjoint representation of the special linear algebra, that is, the complexification of the adjoint representation of the compact algebra $\mathrm{su}(2) \cong \mathrm{so}(3)$; the summand $V_0 = \Lambda^2 V_{1/2} \cong \mathbb{C}$ is the **scalar**, spanned by the invariant alternating form $\varepsilon$. Thus the tensor square of the spinor splits as the complexified adjoint representation plus a scalar. This is the three-dimensional rotation algebra; the adjoint representation of the six-dimensional Lorentz algebra is instead $(1,0) \oplus (0,1)$.

For the two-parameter family the rule applies to each factor:

$$
(m,n) \otimes (m',n') \cong \bigoplus_{k=0}^{\min(m,m')} \bigoplus_{k'=0}^{\min(n,n')} (m+m'-2k,\ n+n'-2k').
$$

For example, $(\tfrac{1}{2},\tfrac{1}{2}) \otimes (\tfrac{1}{2},\tfrac{1}{2}) \cong (0,0) \oplus (1,0) \oplus (0,1) \oplus (1,1)$, of dimension $1 + 3 + 3 + 9 = 16 = 4 \times 4$.

**Tensor powers of the defining representation.** Iterating the rule gives the complete decomposition of the $N$-fold tensor power of the spinor,

$$
V_{1/2}^{\otimes N} \cong \bigoplus_{k=0}^{\lfloor N/2 \rfloor} \left[ \binom{N}{k} - \binom{N}{k-1} \right] V_{N/2-k}, \qquad \binom{N}{-1} = 0,
$$

the multiplicity of $V_{N/2-k}$ being the ballot (Catalan-triangle) number $\binom{N}{k} - \binom{N}{k-1}$. For example $V_{1/2}^{\otimes 2} \cong V_1 \oplus V_0$ and $V_{1/2}^{\otimes 3} \cong V_{3/2} \oplus 2V_{1/2}$. Since every finite-dimensional polynomial representation is completely reducible, the composition factors of a tensor power are exactly its direct summands, with these multiplicities.

## Unitary Representations

A representation $\rho$ on $W$ is **unitary** if $W$ carries an invariant positive-definite Hermitian form $\langle \cdot, \cdot \rangle$. On $V_{1/2} = \mathbb{C}^2$ the standard form $\langle u,v \rangle = u_1^{*}v_1 + u_2^{*}v_2$ is invariant under $SU(2)$, so $V_{1/2}$ is unitary for the compact form $SU(2)$. It is **not** unitary for $SL(2,\mathbb{C})$: the non-compact one-parameter subgroups of hyperbolic rotations do not preserve it. More generally a non-compact simple Lie group has no nontrivial finite-dimensional unitary representation, since the image would lie in a compact group; hence only the trivial representation is finite-dimensional and unitary for $SL(2,\mathbb{C})$, and the defining representation is not unitarisable for the complex group. Unitarity of the compact form $SU(2)$, not of $SL(2,\mathbb{C})$, is what complexification preserves.

**The principal series.** The infinite-dimensional unitary representations are built by induction (*Induced Representations of Locally Compact Groups*). Let $P$ be the Borel subgroup of upper triangular matrices, with $P = MAN$,

$$
M = \{\operatorname{diag}(u,u^{-1}) : |u| = 1\} \cong U(1), \qquad A = \{\operatorname{diag}(e^{t/2}, e^{-t/2}) : t \in \mathbb{R}\},
$$

and $N$ the upper unitriangular matrices. For $m \in \mathbb{Z}$ and $\nu \in \mathbb{R}$ define a unitary character of $P$ by $\chi_{m,\nu}(man) = u^{m} e^{i\nu t}$; the **principal series** representation is the unitarily induced representation

$$
\pi_{m,\nu} = \operatorname{Ind}_{P}^{G}(\chi_{m,\nu}),
$$

realised on $L^2(G/P) = L^2(S^2)$ in the case $m = 0$, where $G/P \cong SU(2)/U(1) \cong S^2$, and on the sections of the associated line bundle in general. Each $\pi_{m,\nu}$ is unitary by construction; it is irreducible for generic parameters, and for $\nu \in \mathbb{R}$ it is tempered. The parameter $m$ is discrete and $\nu$ is continuous. The principal series is not the whole unitary dual: there are also the **complementary series**, for which the continuous parameter is purely imaginary and bounded rather than real, and the trivial representation. The finite-dimensional polynomial representations are not unitary for $SL(2,\mathbb{C})$, except for the trivial representation $V_0$; only their restrictions to $SU(2)$ are unitary.

**Complexification of the unitary dual.** The unitary dual of the maximal compact subgroup $SU(2)$ is discrete, the family $\{V_j\}_{j \in \frac{1}{2}\mathbb{Z}_{\geq 0}}$. Passing to the complexification $SL(2,\mathbb{C})$ replaces the discrete highest-weight parameter by a continuous complex parameter; the representations that remain unitary form the principal series, with parameter on the unitary axis, together with the complementary series on a bounded interval of the imaginary axis. In this sense the unitary dual of $SL(2,\mathbb{C})$ is the complexification of the unitary dual of $SU(2)$. The polynomial representations correspond to the dominant integral highest weights, the discrete points that were unitary for $SU(2)$; under complexification those points cease to be unitary except for the trivial representation.

## Summary

The motions of the biquaternion algebra are the isometries of its biquaternion norm, and they are the rotations and the Lorentz transformations. The unit quaternions $S^3=Sp(1)$ carry the rotations of the definite form by the sandwich $\tilde{Q}\mapsto q\tilde{Q}q^{-1}$, in which the angle is halved and $\pm q$ gives the same rotation: the map $S^3\to SO(3)$ is the double cover $SU(2)\to SO(3)$. Complexifying, the norm-one group $\mathbb{B}^\times_1$ carries the rotations of the indefinite form, and $\mathbb{B}^\times_1/\{\pm e_0\}\cong SO^+(1,3)$ with $\mathbb{B}^\times_1\cong Spin(1,3)$, so that the double cover of the proper orthochronous Lorentz group is realised inside the algebra; the trace-free subalgebra splits into the compact rotation directions and the hyperbolic directions, and it is the boosts generated by the latter that are the isometries of the indefinite form.

The action that carries these motions on the whole algebra is the dagger sandwich $\mathrm{H}_{\tilde{Q}}(\tilde T)=\tilde{Q}\tilde T\tilde{Q}^{*}$. It preserves the two Hermitian sectors and no other pair of the six subspaces, it scales the biquaternion norm by $\lvert N(\tilde{Q})\rvert^{2}$ and preserves it on the unit-norm slice, and its kernel is the central circle $U(1)$, which reduces to $\{\pm e_0\}$ on the slice and is the double cover. It is multiplicative exactly on the unitary elements, its infinitesimal form is $X\tilde T+\tilde TX^{\dagger}$, the commutator along the anti-Hermitian directions and the anticommutator along the Hermitian ones, and the operators preserving the whole subspace structure are exactly the central multiples of the real unit quaternions, giving $SO(3)$ on the slice and $\mathbb{R}_{>0}\times SO(3)$ with the dilations admitted.

The two-sided action $\tilde{Q}\mapsto u\tilde{Q}v$ with independent unit quaternions preserves the Euclidean form and gives $(S^3\times S^3)/\{\pm e_0\}\cong SO(4)$; the one-sided action is its diagonal restriction. The reflections are the maps $\rho_v(\tilde T)=-v\tilde Tv^{-1}=-v\tilde Tv^{\natural}$ with $N(v)=1$, defined on the Clifford vector subspace $\mathrm{Vect}(\mathbb{B})$ and its real form, where orthogonality and anticommutation coincide; on that subspace every isometry is a product of at most three of them, by Cartan–Dieudonné. The construction is that of *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation* and *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* of Part II, and the full symmetry group of the algebra, wider than its isometries, is in *Biquaternion Automorphisms and Derivations*.

The groups that carry the motions have their own representation theory. The group of units is $\mathbb{B}^{\times}\cong GL_2(\mathbb{C})$, of real dimension $8$, with the unit-norm subgroup $\mathbb{B}^{\times}_1\cong SL(2,\mathbb{C})$, the maximal compact subgroups $U(2)$ and $SU(2)$, and the finite-dimensional algebraic representations of $GL_2(\mathbb{C})$ parameterised by the highest weights $(\lambda_1,\lambda_2)$. The finite-dimensional representations of the Lorentz group are the outer products $(m,n)=V_m\boxtimes V_n$ of dimension $(2m+1)(2n+1)$, the polynomial ones being the symmetric powers $V_j$, which the unitary trick recovers from those of $SU(2)$ by complexifying the Lie algebra; the defining representation $V_{1/2}=\mathbb{C}^2$ is the unique simple module of the algebra $M_2(\mathbb{C})$. The defining representation and its conjugate are the two Weyl spinors $(\tfrac12,0)$ and $(0,\tfrac12)$, whose sum is the Dirac spinor and whose tensor product is the four-vector representation $(\tfrac12,\tfrac12)$; the adjoint representation of the Lorentz algebra is $(1,0)\oplus(0,1)$. Tensor products obey the Clebsch–Gordan rule, with the ballot numbers counting the composition factors of the tensor powers of the spinor. Unitarity is preserved by complexification only for the compact form $SU(2)$: the only finite-dimensional unitary representation of $SL(2,\mathbb{C})$ is the trivial one, and the infinite-dimensional unitary representations are the principal series, induced from characters of the Borel subgroup, together with the complementary series.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $N(\tilde{Q})$ | Biquaternion norm; the invariant of the motions |
| $S^3=Sp(1)$ | Unit quaternions; rotors of the definite form |
| $q\tilde{Q}q^{-1}$ | Sandwich action; rotor conjugation |
| $\rho_v(\tilde T)=-v\tilde Tv^{-1}=-v\tilde Tv^{\natural}$ | Reflection in $v^{\perp}$ on $\mathrm{Vect}(\mathbb{B})$, $N(v)=1$ |
| $v\tilde T+\tilde Tv=-2B(v,\tilde T)e_0$ | Anticommutation as orthogonality on $\mathrm{Vect}(\mathbb{B})$; then $v^{\perp}=\{\tilde T:\tilde Tv=-v\tilde T\}$ |
| Cartan–Dieudonné | Every isometry of $\mathrm{Vect}(\mathbb{B})$ is at most three reflections $\rho_v$ |
| $S^3\to SO(3)$ | Double cover $SU(2)\to SO(3)$; $\pm q$ give the same rotation |
| $\mathbb{B}^\times_1\cong Spin(1,3)$ | Norm-one group as the spin group; double cover of $SO^+(1,3)$ |
| $\mathbb{B}^\times_1/\{\pm e_0\}\cong SO^+(1,3)$ | Proper orthochronous Lorentz group |
| $\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ | Rotation directions; compact |
| $\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$ | Hyperbolic (boost) directions |
| $u\tilde{Q}v$ | Two-sided action; preserves the Euclidean form |
| $(S^3\times S^3)/\{\pm e_0\}\cong SO(4)$ | Two-sided action as four-dimensional rotations |
| $\mathrm{H}_{\tilde{Q}}(\tilde T)=\tilde{Q}\tilde T\tilde{Q}^{*}$ | The dagger sandwich; the action of a unit on the algebra |
| $\mathrm{H}_{A\tilde{Q}}=\lvert A\rvert^{2}\mathrm{H}_{\tilde{Q}}$ | Central phase invisible; modulus as the dilation |
| $N(\mathrm{H}_{\tilde{Q}}(\tilde T))=\lvert N(\tilde{Q})\rvert^{2}N(\tilde T)$ | Scaling of the norm; an isometry on the unit-norm slice |
| $U(1)=\{e^{i\theta}e_0\}$ | Kernel of the sandwich; $\{\pm e_0\}$ on the unit-norm slice |
| structure theorem | Operators preserving all six subspaces: the central multiples of the real unit quaternions |
| $X\tilde T+\tilde TX^{\dagger}$ | Infinitesimal operator; commutator on $\mathbb{M}_-$, anticommutator on $\mathbb{M}_+$ |
| $\mathbb{B}^{\times}\cong GL_2(\mathbb{C})$ | Group of units; real dimension $8$ |
| $U(2)$ | Unitary biquaternions; maximal compact subgroup of $\mathbb{B}^{\times}$ |
| $(\lambda_1,\lambda_2)$ | Highest weight of an algebraic representation of $GL_2(\mathbb{C})$ |
| $V_j$ | Irreducible representation of spin $j$, highest weight $2j$, dimension $2j+1$ |
| $(m,n)=V_m\boxtimes V_n$ | Finite-dimensional irreducible representation of the Lorentz group |
| $(\tfrac12,0)$, $(0,\tfrac12)$ | Left- and right-handed Weyl spinors |
| $(\tfrac12,\tfrac12)$ | Four-vector representation, $V_{1/2}\otimes\overline{V_{1/2}}$ |
| $V_{1/2}^{\otimes N}$ | Ballot-number decomposition of the tensor powers of the spinor |
| $\operatorname{Ind}_P^G(\chi_{m,\nu})$ | Principal series of $SL(2,\mathbb{C})$; $P=MAN$ the Borel subgroup |

## Further Reading

- John Stillwell, *Naive Lie Theory* (Springer, 2008).
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001).
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997).
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the finite-dimensional representations of $SL(2,\mathbb{C})$, the highest weights, and the Clebsch–Gordan rule.
- Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples* (Princeton University Press, 1986), for the principal and complementary series and the unitary dual of $SL(2,\mathbb{C})$.
