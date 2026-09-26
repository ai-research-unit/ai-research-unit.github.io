# __Biquaternion Operator Representation__

## Introduction

An element of an algebra can be used in two ways. It can be *decomposed*, which is what the polar representation does when it writes $\tilde{Q} = r e^{i\alpha} B \hat{q}$ and presents the four factors of a single element; or it can be made to *act*, which is what a representation does when it presents an element as a linear operator on a vector space. This article is about the second use. Its carrier is the algebra itself, and the action of a unit $\tilde{Q}$ on an element $x$ is the **sandwich**

$$
x \longmapsto \tilde{Q}\, x\, \tilde{Q}^\dagger ,
$$

the conjugation of $x$ by $\tilde{Q}$ with the inverse replaced by the Hermitian conjugate. The dagger is not a convenience of notation. A two-sided sandwich is a map $x \mapsto AxB$ with $A$ and $B$ invertible, and it carries the Hermitian sector into itself exactly when $B$ is a real multiple of $A^\dagger$; a Lorentz transformation must respect the sectors, so a sandwich can be one only in the dagger form. The sandwich is the subject of the article, together with the sense in which it is a representation of a group by linear operators on the eight-dimensional real vector space $\mathbb{B}$. The companion map built from the inverse, which is an automorphism of the algebra rather than a similarity, is recorded for contrast in the last section.

The subject is not the regular representation. Left multiplication, $x \mapsto \tilde{Q}x$, is already a representation of the algebra on itself and has its own article; it is faithful, its matrices are $4 \times 4$ over $\mathbb{C}$, and it carries the whole multiplication table. The sandwich acts on the same carrier by a different rule, and the differences are the whole content of what follows: the sandwich is **not** an automorphism of the algebra, but it is multiplicative exactly on the unitary elements, and away from them it preserves the interval where the product fails; its kernel is the central circle, so it is not faithful; and its action on the six distinguished subspaces of the algebra is decided by the dagger that defines it, with the two sectors invariant and the other four not.

Three results organise the article. The first is that the sandwich is a representation of the group of units — it composes as its elements do — but not by automorphisms: it is multiplicative exactly when the acting element is unitary, and the criterion has a geometric form, because the unitary elements are exactly those that fix the time axis, $\operatorname{H}_{\tilde{Q}}(ie_0) = ie_0$. The second is that it preserves the two four-dimensional sectors and the rank of an element and no other of the six subspaces, and that it scales the norm form by $|N(\tilde{Q})|^2$, which is one on the unit-norm slice: that slice is the Lorentz group and the sandwich is the Lorentz action, the answer to why the series writes the four-vector action with a dagger. The third is that the operators which preserve the whole subspace structure are the class of the central multiples of the real unit quaternions, so the polar representation decides which operators respect the subspaces of the corpus; the multiplicative ones among them are exactly the unitary elements, and the half-angle in the rotor and the double angle in the operator are one fact.

Two conventions are used throughout, and both are those of the corpus. The norm form is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2 = \det\Phi(\tilde{Q})$ with $\Phi(e_0) = I$ and $\Phi(e_k) = -i\sigma_k$; the inverse of a unit is $\tilde{Q}^{-1} = \bar{\tilde{Q}}/N(\tilde{Q})$; and the four involutions are $\bar{\phantom{Q}}$ (quaternion conjugation), ${}^{*}$ (complex conjugation of the coefficients), $\dagger$ (Hermitian conjugation, the composite of the other two) and $\flat = -\dagger$. The six subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion and antiquaternion subspaces $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, and the Hermitian and anti-Hermitian sectors $\mathbb{M}_+$ and $\mathbb{M}_-$. Every numerical statement was recomputed in double precision before it was written; the identities quoted were checked on random elements and the residuals are below $10^{-11}$.

## The Carrier and the Sandwich

### The Carrier Is the Algebra

The carrier of the representation is the algebra $\mathbb{B}$ regarded as a real vector space of dimension eight, with the real basis

$$
e_0,\quad e_1,\quad e_2,\quad e_3,\quad ie_0,\quad ie_1,\quad ie_2,\quad ie_3 .
$$

A representation is a homomorphism from a group to the linear maps of this space, so three pieces of data have to be fixed in each case: the group, the map, and the kernel. For left multiplication the group is the group of units and the map is faithful. For the sandwich the group is again the group of units, but the map is not faithful, and the kernel is the interesting part.

### The Sandwich

The **sandwich**, or **dagger sandwich**, $\operatorname{H}_{\tilde{Q}}$ replaces the inverse by the Hermitian conjugate,

$$
\operatorname{H}_{\tilde{Q}}:\ \mathbb{B} \longrightarrow \mathbb{B} , \qquad \operatorname{H}_{\tilde{Q}}(x) = \tilde{Q}\,x\,\tilde{Q}^\dagger .
$$

It is the map the physics articles call **rotor conjugation** when $\tilde{Q}$ has unit norm form, and it is the form in which the Lorentz action is written there. It is also the map that the corpus's four-vector calculus uses everywhere, and the reason is the dagger: a two-sided sandwich carries the Hermitian sector into itself exactly when it is built from the Hermitian conjugate, and the inverse-based companion of the last section does not have that property unless its element is unitary.

### Comparison with Left Multiplication

| | left multiplication $\tilde{Q}x$ | the sandwich $\operatorname{H}_{\tilde{Q}}(x) = \tilde{Q}x\tilde{Q}^\dagger$ |
|---|---|---|
| type of map | algebra endomorphism | neither, but a representation of the units |
| image of $e_0$ | $\tilde{Q}$ | $\tilde{Q}\tilde{Q}^\dagger$, not central in general |
| kernel, $\tilde{Q}$ of unit norm form | $\{e_0\}$ | $\{\pm e_0\}$ |
| preserves the centre | no | no |
| preserves the norm form | $N(\tilde{Q}x) = N(\tilde{Q})N(x)$ | $N(\operatorname{H}_{\tilde{Q}}x) = \lvert N(\tilde{Q})\rvert^2N(x)$ |

The first column is the regular representation, recorded for comparison only. The last line is the sharpest single difference between the two: left multiplication carries the norm form through the element, and the sandwich scales it by the squared modulus of the norm form of the operator. On the unit-norm slice, where $|N(\tilde{Q})| = 1$, both preserve it; off that slice only the first does.

## The Sandwich

### It Is Not an Automorphism, and Why

The sandwich is not multiplicative. For general $x, y$,

$$
\operatorname{H}_{\tilde{Q}}(xy) = \tilde{Q}\,xy\,\tilde{Q}^\dagger \neq \left(\tilde{Q}x\tilde{Q}^\dagger\right)\left(\tilde{Q}y\tilde{Q}^\dagger\right) = \operatorname{H}_{\tilde{Q}}(x)\operatorname{H}_{\tilde{Q}}(y) ,
$$

because the correct insertion between $x$ and $y$ would be $\tilde{Q}^\dagger\tilde{Q}$, which is the unit exactly when $\tilde{Q}$ is unitary. This is the exact sense in which the physics action is not an algebra action: it is a linear representation of the group of units on the algebra, but not one by algebra automorphisms. The equality for all $x$ and $y$ is therefore a criterion on the element, and it is taken up in the section on the operators that preserve the subspace structure.

### It Preserves the Two Sectors

The sandwich is linear, and it is the map that preserves the two four-dimensional sectors.

**Theorem.** For every unit $\tilde{Q}$, $\operatorname{H}_{\tilde{Q}}$ maps $\mathbb{M}_+$ to $\mathbb{M}_+$ and $\mathbb{M}_-$ to $\mathbb{M}_-$.

**Proof.** Let $x \in \mathbb{M}_+$, so that $x^\dagger = x$. Then

$$
\left(\tilde{Q}x\tilde{Q}^\dagger\right)^\dagger = \tilde{Q}^{\dagger\dagger}x^\dagger\tilde{Q}^\dagger = \tilde{Q}x\tilde{Q}^\dagger ,
$$

so the image is Hermitian and lies in $\mathbb{M}_+$. For $x \in \mathbb{M}_-$ one has $x^\dagger = -x$, so the image is anti-Hermitian and lies in $\mathbb{M}_-$. $\square$

**Theorem.** For every unit $\tilde{Q}$, $N\!\left(\operatorname{H}_{\tilde{Q}}(x)\right) = \left|N(\tilde{Q})\right|^2 N(x)$.

**Proof.** The norm form is multiplicative and central, $N(ab) = N(a)N(b)$; and $N(\tilde{Q}^\dagger) = N(\tilde{Q})^{*}$ because $\dagger$ is the composite of $\bar{\phantom{Q}}$, which fixes $N$, and ${}^{*}$, which conjugates it. Hence $N(\tilde{Q}x\tilde{Q}^\dagger) = N(\tilde{Q})N(x)N(\tilde{Q})^{*} = |N(\tilde{Q})|^2N(x)$. $\square$

On the unit-norm slice $N(\tilde{Q}) = 1$ the scaling factor is one, and the sandwich is an isometry of the norm form on both sectors: it is the action of $SL(2,\mathbb{C})$ on the Hermitian forms and on the four-vectors, and it is the covering map onto the proper orthochronous Lorentz group. That is the reason the physics articles use it, and it is the sharpest answer the article gives to the question it started from: **the Lorentz transformation of the corpus is the sandwich of an element of the Hermitian sector**, $\tilde{\Lambda} = \tilde{\Lambda}^\dagger$ of unit norm form, and then no inverse and no rotation part appear.

### It Preserves No Other Subspace

The sandwich is not an automorphism, so no other of the six subspaces survives in general, and the failure is easy to see. Apply it to $e_0$:

$$
\operatorname{H}_{\tilde{Q}}(e_0) = \tilde{Q}\tilde{Q}^\dagger ,
$$

which is Hermitian but not central for a general $\tilde{Q}$. The image of the unit is therefore an element of the informational sector and not of the centre, so the centre is not preserved. The same computation for a general element of the vector subspace shows that the trace is not preserved, so that subspace is not preserved either. The two sectors are the only two of the six that survive, and they survive as a pair, in the sense that the map preserves each one separately and cannot move one into the other.

### The Kernel Is the Central Circle

**Theorem.** $\operatorname{H}_{\tilde{Q}} = \mathrm{id}$ if and only if $\tilde{Q} = e^{i\theta}e_0$ for some real $\theta$.

**Proof.** If $\operatorname{H}_{\tilde{Q}}(x) = x$ for every $x$ then taking $x = e_0$ gives $\tilde{Q}\tilde{Q}^\dagger = e_0$, so $\tilde{Q}$ is unitary; and taking $x$ arbitrary gives $\tilde{Q}x = x\tilde{Q}$, so $\tilde{Q}$ is central. A central unitary is a complex number of modulus one. Conversely such an element acts trivially since its Hermitian conjugate is its inverse. $\square$

The kernel is therefore the central circle $U(1) = \{e^{i\theta}e_0\}$, of one real dimension: the sandwich is blind to a central phase and to nothing else. On the unit-norm slice it reduces to the two central signs $\{\pm e_0\}$, because the intersection of the circle with that slice is the two signs, and that kernel of order two is the double cover of the Lorentz group by the rotors.

The kernel at the two levels the article uses, side by side:

| operator | group | kernel | parameters lost |
|---|---|---|---|
| $\operatorname{H}_{\tilde{Q}}(x)=\tilde{Q}x\tilde{Q}^\dagger$ | units of $\mathbb{B}$ | $U(1)\subset\mathbb{C}_{\mathbb{B}}$ | the circle only |
| $\operatorname{H}_{\tilde{\Lambda}}(x)=\tilde{\Lambda}x\tilde{\Lambda}^\dagger$ | unit-norm $SL(2,\mathbb{C})$ | $\{\pm e_0\}$ | the sign |

## The Action on the Six Subspaces

### The Table

The sandwich separates the six subspaces as follows. Each entry records whether the image of a general element of the row subspace lies in that same subspace, for a general unit $\tilde{Q}$, and for a real unit quaternion $\hat{q}$, where the sandwich is a rotation.

| subspace | $\operatorname{H}_{\tilde{Q}}$, general $\tilde{Q}$ | $\operatorname{H}_{\hat{q}}$, real unit quaternion |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ (centre) | no | yes |
| $\mathrm{Vect}(\mathbb{B})$ (vector, $6$-dimensional) | no | yes |
| $\mathbb{H}_{\mathbb{B}}$ (real quaternions) | no | yes |
| $i\mathbb{H}_{\mathbb{B}}$ (antiquaternions) | no | yes |
| $\mathbb{M}_+$ (Hermitian) | yes | yes |
| $\mathbb{M}_-$ (anti-Hermitian) | yes | yes |

The table is the whole of the case analysis, and two of its features deserve a heading of their own: the two sectors, which are preserved for every element, and the four subspaces that only a unitary element preserves.

### The Centre and the Vector Subspace

The centre and the vector subspace are the two pieces of the scalar–vector decomposition,

$$
\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B}) , \qquad \mathrm{Vect}(\mathbb{B}) = \ker \operatorname{Sc} = [\mathbb{B},\mathbb{B}] ,
$$

and both are defined by relations that respect the multiplication: the centre is the set of elements commuting with every element, and the vector subspace is the kernel of the trace, equivalently the derived subspace. A map that respects the multiplication respects both, and the sandwich does not. Applied to the unit it gives

$$
\operatorname{H}_{\tilde{Q}}(e_0) = \tilde{Q}\tilde{Q}^\dagger ,
$$

which is Hermitian, hence an element of the informational sector, and central only for special elements: the unit leaves the centre, and the centre is carried into a sector. The same computation shows that the vector subspace is not preserved either, since the image of a traceless element need not be traceless. What survives of the scalar–vector decomposition is the rank of the matrix image, which the section on the invariants records.

### The Two Sectors and the Real Structure

The sandwich preserves the two sectors because what it preserves is the involution $\dagger$ itself: the map $x \mapsto \tilde{Q}x\tilde{Q}^\dagger$ is the standard way to make an involution transform, and the computation is the one that gives $x^\dagger = x \Rightarrow \left(\tilde{Q}x\tilde{Q}^\dagger\right)^\dagger = \tilde{Q}^{\dagger\dagger}x^\dagger\tilde{Q}^\dagger = \tilde{Q}x\tilde{Q}^\dagger$.

This is also the sense in which the dagger is forced. A two-sided sandwich is a map $x \mapsto AxB$ with $A$ and $B$ invertible, and the members of the family that carry the fixed space of $\dagger$ into itself are exactly those with $B = \lambda A^\dagger$ for a real $\lambda$, of which the dagger sandwich is the normalised case $\lambda = 1$; the inverse-based companion carries that fixed space into the fixed space of the conjugated real structure $\tilde{Q}\,\dagger\,\tilde{Q}^{-1}$, which is a different involution unless the element is unitary. The halves and the sectors are the fixed spaces of the involutions, so the subspaces a sandwich preserves are exactly the ones its own involution defines.

### The Theorem: Which Operators Preserve the Whole Space Structure

The question the table raises is which operators preserve all six subspaces at once, and the answer is sharp and is decided by the polar representation.

**Theorem.** Let $\tilde{Q}$ be a unit with polar representation $\tilde{Q} = \rho B\hat{q}$, where $\rho = re^{i\alpha}$ is central, $B$ is Hermitian positive of unit norm form and $\hat{q}$ is a unit real quaternion. Then the following are equivalent:

1. $\operatorname{H}_{\tilde{Q}}$ preserves the whole subspace structure, that is, it maps each of the six subspaces to itself;
2. $B = e_0$;
3. $\tilde{Q} = z\hat{q}$ with $z$ central and $\hat{q}$ a unit real quaternion;
4. $\tilde{Q}\tilde{Q}^\dagger$ is a positive real multiple of $e_0$.

When these hold, $\operatorname{H}_{\tilde{Q}} = |z|^2\operatorname{H}_{\hat{q}}$ is a dilation composed with a rotation of the vector space, and each of the six subspaces is preserved.

**Proof.** $(3) \Leftrightarrow (4)$: for $\tilde{Q} = z\hat{q}$ one has $\tilde{Q}\tilde{Q}^\dagger = |z|^2\hat{q}\hat{q}^\dagger = |z|^2e_0$, because a real quaternion has $\hat{q}^\dagger = \bar{\hat{q}} = \hat{q}^{-1}$; conversely if $\tilde{Q}\tilde{Q}^\dagger = \lambda e_0$ with $\lambda > 0$ then $|N(\tilde{Q})| = \lambda$, the element $\hat{U} = \tilde{Q}/\sqrt{N(\tilde{Q})}$ has unit norm form and $\hat{U}\hat{U}^\dagger = \tilde{Q}\tilde{Q}^\dagger/|N(\tilde{Q})| = e_0$, so $\hat{U}$ is unitary, that is, $\hat{U} = e^{i\alpha}\hat{q}$ with $\hat{q}$ a real unit quaternion, and $\tilde{Q} = (\sqrt{N(\tilde{Q})}e^{i\alpha})\hat{q}$ is of the form $(3)$. $(2) \Leftrightarrow (3)$ is immediate from the polar form. $(3) \Rightarrow (1)$: the central factor contributes the dilation by $|z|^2$, which preserves every subspace, and $\operatorname{H}_{\hat{q}}$ is the rotation through twice the half-angle of $\hat{q}$, which preserves all six subspaces, as the manifest symmetry of the basis shows. $(1) \Rightarrow (4)$: if the centre is preserved then $\operatorname{H}_{\tilde{Q}}(e_0) = \tilde{Q}\tilde{Q}^\dagger$ is central; that element is Hermitian positive of norm form $|N(\tilde{Q})|^2 > 0$, and a central Hermitian positive element of the algebra is a positive real multiple of the unit, so $(4)$ holds. $\square$

The multiplicative criterion established earlier and the structure-preserving criterion of this theorem meet on the unitary elements: the operators that are multiplicative are exactly those with $\tilde{Q}\tilde{Q}^\dagger = e_0$, that is the unitary ones, and those are also the elements that fix the time axis, $\operatorname{H}_{\tilde{Q}}(ie_0) = i\tilde{Q}\tilde{Q}^\dagger = ie_0$. A general element of the family $(3)$ preserves the subspaces and has a central scale in its operator, and the scale is what stops it from being multiplicative.

The theorem has a consequence worth spelling out. On the unit-norm slice the operators preserving the subspace structure form the subgroup

$$
\left\{\operatorname{H}_{\hat{q}} : \hat{q}\hat{q}^\dagger = e_0\right\} \cong SU(2)/\{\pm e_0\} \cong SO(3) ,
$$

of real dimension three; with the dilations admitted they form $\mathbb{R}_{>0}\times SO(3)$, of real dimension four. The rotation group sits inside the six-dimensional operator group as the rotations sit inside the Lorentz group; the remaining three dimensions are the boosts, and a boost moves the centre, the vector subspace and the two halves, which is exactly what a boost does not do to the four-vectors but does do to the algebra as a whole.

## The Matrix Picture

### The Congruence of Matrices

The isomorphism $\Phi$ turns the sandwich into a congruence of $2\times2$ complex matrices,

$$
\Phi\!\left(\operatorname{H}_{\tilde{Q}}(x)\right) = \Phi(\tilde{Q})\,\Phi(x)\,\Phi(\tilde{Q})^\dagger ,
$$

read off from the multiplicativity of $\Phi$ and from $\Phi(\tilde{Q}^\dagger) = \Phi(\tilde{Q})^\dagger$. On the unit-norm slice $\Phi(\tilde{Q})$ lies in $SL(2,\mathbb{C})$ and the sandwich is the standard action of that group on the matrix algebra by $*$-congruence, which is the matrix form of the Lorentz action: it preserves the Hermitian matrices as a set, it preserves the determinant up to the modulus factor, and it moves the null cone transitively. The rank of $\Phi(x)$, the modulus of the determinant $|N(x)|$ and the Hermitian signature of the image are the invariants the article uses, and they are read off from this identity.

### The Unitary Subgroup and the Real Form

The subgroup of the operator group that preserves the subspace structure acts by a unitary congruence, and the reason is visible in the matrix picture. A congruence $\Phi(x) \mapsto T\Phi(x)T^\dagger$ preserves the Hermitian matrices exactly when $T$ is unitary up to a scalar, because the condition that $TMT^\dagger$ be Hermitian whenever $M$ is Hermitian is $T^\dagger = \lambda T^{-1}$; the subgroup is the projective unitary group $PU(2) = PSU(2) = SO(3)$, and by the theorem of the previous section it is generated by the real unit quaternions. The two statements — matrix-theoretic and quaternionic — are the same statement, and the identification of $SU(2)$ with the unit real quaternions is what makes them agree.

## The Lie Algebra of the Operator Group

### The Derivative at the Identity

Differentiating the operator action along a one-parameter subgroup gives the infinitesimal operator, and the result identifies the Lie algebra of the operator group with a familiar space.

**Proposition.** Let $X \in \mathbb{B}$ and let $x$ be fixed. Then

$$
\left.\frac{d}{dt}\right|_{t=0}\operatorname{H}_{e_0+tX}(x) = Xx + xX^\dagger .
$$

**Proof.** Since $\operatorname{H}_{\tilde{Q}}(x) = \tilde{Q}x\tilde{Q}^\dagger$, differentiating the product at $\tilde{Q} = e_0$ gives $\dot{\tilde{Q}}x + x\dot{\tilde{Q}}^\dagger = Xx + xX^\dagger$. $\square$

The formula contains both of the algebra's symmetries. Along the anti-Hermitian directions, $X^\dagger = -X$, the infinitesimal operator is the **commutator** $[X,x]$, which is the infinitesimal rotation; along the Hermitian directions, $X^\dagger = X$, it is the **anticommutator** $Xx + xX$, which is the infinitesimal boost. The two appear in one formula because the sandwich is built from the dagger, and the anticommutator is the infinitesimal form of the statement that a boost does not double the half-angle of its element, which the section on the rotor records.

### The Lie Algebra of the Sandwich

**Theorem.** Restricted to the unit-norm slice the operator group is the Lorentz group $SL(2,\mathbb{C})$ acting by the sandwich, and its Lie algebra is $\mathfrak{sl}(2,\mathbb{C})$ regarded over $\mathbb{R}$,

$$
\dim_{\mathbb{R}} = 6 ,
$$

with the anti-Hermitian generators giving the rotations and the Hermitian ones the boosts.

**Proof.** The unit-norm slice is the group $SL(2,\mathbb{C})$, and the sandwich is its action on the algebra by the congruence $\Phi(x)\mapsto\Phi(\tilde{Q})\Phi(x)\Phi(\tilde{Q})^\dagger$, which is the defining action of $SL(2,\mathbb{C})$ on $2\times2$ Hermitian matrices; the Lie algebra is $\mathfrak{sl}(2,\mathbb{C})$ over $\mathbb{R}$, and the infinitesimal operators are those of the proposition above, with the commutator directions generating the two $\mathfrak{su}(2)$ rotation subgroups and the anticommutator directions the non-compact boosts. $\square$

The reading of the two halves and the boosts belongs to the physics articles on the Lorentz group, and it is recorded here to fix the two Lie algebras side by side: the automorphism of the last section has for its Lie algebra the derivation algebra of the complex algebra, $\operatorname{Der}(\mathbb{B})\cong\mathfrak{sl}(2,\mathbb{C})$ over $\mathbb{C}$, of three complex dimensions, while the sandwich has the same space over $\mathbb{R}$, of six real dimensions, organised by a real structure; the two are the same six real dimensions with two different real structures, and the dagger is what chooses between them.

## Orbits and Invariants

### The Invariants

The sandwich preserves the rank of the matrix image and scales the norm form by $|N(\tilde{Q})|^2$; the scaling is one on the unit-norm slice, where the norm form is preserved outright. These are the two invariants that organise the orbits: the rank is the invariant of the Jordan type, since $\Phi(\operatorname{H}_{\tilde{Q}}x) = \Phi(\tilde{Q})\Phi(x)\Phi(\tilde{Q})^\dagger$ and a congruence by an invertible matrix does not change the rank, and the norm form is the determinant. Between them they cut the algebra into the pieces that the operator cannot mix.

| invariant | value | meaning |
|---|---|---|
| rank $\Phi(x) = 2$ | $N(x) \neq 0$ | $x$ is a unit |
| rank $\Phi(x) = 1$ | $N(x) = 0$, $x \neq 0$ | $x$ is a zero divisor of rank one |
| rank $\Phi(x) = 0$ | $x = 0$ | the origin |

For a rank-two element the norm form may be any non-zero complex number, and on the unit-norm slice the operator cannot change it at all; off the slice every orbit is rescaled by the same positive factor, $N$ being multiplied by $|N(\tilde{Q})|^2$, so it is enough to classify the orbits on the slice. There the two sectors carry the classification the physics articles use: on $\mathbb{M}_+$ the orbits of the Hermitian forms are classified by the signature, and on $\mathbb{M}_-$ the orbits of the four-vectors are the timelike, the null and the spacelike classes, distinguished by the sign of the real norm form, with the connection component the proper orthochronous one, so the two time directions are not mixed. For a rank-one element the norm form vanishes identically; the non-zero zero divisors are the null cone, and on the unit-norm slice they form a single orbit, which is the fact the physics articles use when they speak of the light cone as a single geometric object rather than as a union of light cones of individual four-vectors.

### The Real Forms

The sandwich, restricted to the two sectors, is exactly the Lorentz action, and its orbits there are the ones the physics articles use: the Hermitian forms classified by the signature on $\mathbb{M}_+$, and the timelike, null and spacelike four-vectors on $\mathbb{M}_-$, with the null class a single orbit. The two sectors are the two real forms of the complex algebra, and the norm form of the algebra restricts to each of them as a real quadratic form whose sign is the invariant; that is why the orbit picture on the sectors is richer than the one on the algebra as a whole, where only the rank and the modulus of the norm form survive.

## The Rotor and the Double Angle

### The Angle Is Doubled

For a real unit quaternion the angle of the operator is twice the angle of the element, and this is the single computation that the whole of the spin representation rests on.

**Theorem.** Let $\hat{q} = \cos\theta + \sin\theta\,\hat{\mathbf{u}}$ with $\hat{\mathbf{u}}$ a unit real vector, and let $\mathbf{v}$ be a real vector, identified with the element $\mathbf{v} = v_1e_1 + v_2e_2 + v_3e_3$. Then

$$
\operatorname{H}_{\hat{q}}(\mathbf{v}) = \mathbf{v}\cos 2\theta + \left(\hat{\mathbf{u}}\times\mathbf{v}\right)\sin 2\theta + \hat{\mathbf{u}}\left(\hat{\mathbf{u}}\cdot\mathbf{v}\right)\left(1 - \cos 2\theta\right) ,
$$

which is the rotation of $\mathbf{v}$ about $\hat{\mathbf{u}}$ through the angle $2\theta$.

**Proof.** The identity $\operatorname{H}_{\hat{q}}(\mathbf{v}) = \hat{q}\mathbf{v}\hat{q}^{\dagger}$ is the standard Rodrigues formula written in quaternion multiplication, since $\hat{q}^\dagger = \hat{q}^{-1}$ for a real quaternion; the computation in components gives the three terms above, and the resulting linear map is orthogonal, fixes $\hat{\mathbf{u}}$, and rotates the plane orthogonal to $\hat{\mathbf{u}}$ by $2\theta$, which identifies it. $\square$

The doubling is not special to the real vector part. Because $i$ is central, $\operatorname{H}_{\hat{q}}(i\mathbf{w}) = i\operatorname{H}_{\hat{q}}(\mathbf{w})$, so the same rotation acts on the imaginary vector part and on the real one; the six-dimensional vector subspace is carried to itself by a single rotation of the underlying three-dimensional space, acting complex-linearly. The Clifford version of the same statement, in which the sandwich acts on vectors and the left multiplication acts on spinors, together with the reason the two differ by the half angle, is the subject of *Versors, Rotors and the Sandwich Action*; the half-angle computation is not repeated here, and what matters for the present article is only that the operator of the rotor is the rotation it squares to.

### Why the Doubling Matters

A map that rotates by $2\theta$ when the element carries the angle $\theta$ cannot be faithful on the rotation group: both $\hat{q}$ and $-\hat{q}$ give the same operator, and the two elements are the two elements of the group lying over one rotation. This is the double cover, and it is the reason a rotation is represented by an element of a group that is twice as large. In the operator language the statement is the kernel computation of this article, $\operatorname{H}_{\hat{q}} = \operatorname{H}_{-\hat{q}}$ together with $\operatorname{H}_{\hat{q}} = \mathrm{id} \Leftrightarrow \hat{q} = \pm e_0$, and no separate theory of spinors is needed to reach it: the half-angle in the element and the full angle in the operator are the same fact.

## The Relation to the Polar Representation

The two subjects meet at the kernel theorem, and the meeting is worth restating in the form of a dictionary.

| polar datum of $\tilde{Q} = re^{i\alpha}B\hat{q}$ | what the sandwich sees |
|---|---|
| scale $r$ | the dilation $\lvert N(\tilde{Q})\rvert^2 = r^4$ of the interval |
| phase $e^{i\alpha}$ | nothing, since it is central: on the unit circle of the phase the operator is unchanged |
| boost $B$ | the boost part of the action |
| rotor $\hat{q}$ | the rotation part of the action |

The sandwich sees all four factors, and the first two only through the central factor as a whole: the operator of $\tilde{Q}$ and the operator of $\tilde{Q}$ multiplied by any unit-modulus central phase are the same operator, and the modulus of the central factor enters only through the single dilation $r^4$. This is the kernel statement of the article in the language of the polar representation, and it is the reason the corpus can use one element for both the decomposition and the action: the two articles are companions, and the theorems of each are the others' unexplained observations.

Two further comparisons are immediate and are recorded for completeness. The operator is unchanged by the central phase, so the four factors of the polar representation collapse to the two geometric ones as far as the operator is concerned, and the phase should not be expected to appear in it; and the operator depends on the product $B\hat{q}$ through the order of composition, so the decomposition into a boost operator and a rotation operator is a decomposition of the *operator*, with the factors in the order of composition, and it is not a property of the element independent of that order.

## The Relation to the Spin Representation

The sandwich, restricted to the real quaternions, is the algebraic origin of the spin representations of the corpus, and the connection is exact rather than analogical.

**Theorem.** The group of unit real quaternions, embedded in the algebra, acts on the three-dimensional space of imaginary quaternions by the sandwich, and

$$
\mathrm{Sp}(1) = SU(2) \longrightarrow SO(3) , \qquad \hat{q} \longmapsto \operatorname{H}_{\hat{q}} ,
$$

is a surjective group homomorphism with kernel $\{\pm e_0\}$, hence a double cover.

**Proof.** The unit real quaternions form a group under multiplication, isomorphic to $SU(2) \cong S^3$; the map is a homomorphism because it is the restriction of the sandwich representation; its kernel is $\{\pm e_0\}$ by the kernel theorem; and it is surjective because every rotation is a rotation about some axis through some angle, and $\cos\theta + \sin\theta\hat{\mathbf{u}}$ is a unit real quaternion for every $\theta$ and every unit $\hat{\mathbf{u}}$. $\square$

Two consequences complete the link with the spinor module. First, the action is irreducible on the imaginary quaternions and is not faithful, so $SO(3)$ has no genuine action there that extends the module structure; the faithful object is the element $\hat{q}$, and an object that transforms by $\hat{q}$ and takes the sign $-\hat{q}$ for the same rotation is exactly a spinor. Second, the same construction with the unit-norm biquaternions in place of the unit real quaternions gives the double cover of the Lorentz group, $SL(2,\mathbb{C}) \to SO^+(1,3)$, with the same kernel $\{\pm e_0\}$ by the same kernel theorem; the only difference between the two cases is the real slice on which the element is taken. The two double covers of the corpus are therefore two readings of one computation, and the dictionary between them is the dictionary between the two sections above.

## Worked Examples

### A Real Unit Quaternion of Order Two

Take $\hat{q} = e_1$, a real unit quaternion of unit norm form. The operator acts on the basis of the imaginary quaternions by

| $x$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ | $ie_1$ | $ie_2$ |
|---|---|---|---|---|---|---|
| $\operatorname{H}_{e_1}(x)$ | $e_0$ | $e_1$ | $-e_2$ | $-e_3$ | $ie_1$ | $-ie_2$ |

The operator fixes $e_0$ and $e_1$ and negates the plane spanned by $e_2$ and $e_3$, which is the rotation through $\pi$ about $e_1$; the angle is $2\theta$ with $\theta = \pi/2$ as it must be for $\hat{q} = e_1$. The two entries in the imaginary-vector columns confirm that the same rotation acts on the imaginary half of the vector subspace. The operator is an involution of the algebra, $\operatorname{H}_{e_1}^2 = \mathrm{id}$, as the square of a rotation by $\pi$ must be, and it is multiplicative because a real unit quaternion is unitary.

### A Central Element

Take $\tilde{Q} = (3 + 2i)e_0$, of norm form $N = 9 - 4 + 12i = 5 + 12i$, with $|N| = 13$ and $|\tilde{Q}|^2 = 13$. The operator multiplies every element by the positive factor $\tilde{Q}\tilde{Q}^\dagger = 13e_0$, so $\operatorname{H}_{\tilde{Q}}(x) = 13x$, which is the scaling statement $N(\operatorname{H}_{\tilde{Q}}x) = |N(\tilde{Q})|^2N(x) = 169N(x)$ in the case of a central element. The element is a unit and its operator is not the identity, in agreement with the kernel theorem: the kernel is the circle of unit modulus, and a central element of modulus $\sqrt{13}$ is not in it. The operator preserves the six subspaces, as the structure theorem requires of a central multiple of the unit, and it is not multiplicative, because $\tilde{Q}\tilde{Q}^\dagger = 13e_0$ is not the unit.

### A Central Phase Times a Rotor

Take $\tilde{Q} = (1+i)\left(\cos\frac{\pi}{6}e_0 + \sin\frac{\pi}{6}e_3\right)$. The element is a central multiple of a real unit quaternion, so the structure theorem applies: $\tilde{Q}\tilde{Q}^\dagger = 2e_0$ is a positive real multiple of the unit, the polar boost factor is the unit, and $\operatorname{H}_{\tilde{Q}} = 2\operatorname{H}_{\hat{q}}$ with $\hat{q} = \cos(\pi/6)e_0 + \sin(\pi/6)e_3$. On $e_1$ the operator gives

$$
\operatorname{H}_{\tilde{Q}}(e_1) = e_1 + \sqrt3\,e_2 = 2\cos\frac{\pi}{3}\,e_1 + 2\sin\frac{\pi}{3}\,e_2 ,
$$

which is the rotation through $\pi/3$ about $e_3$, twice the angle $\pi/6$ of the element, scaled by the modulus $|1+i|^2 = 2$. The phase $1+i$ has left no trace except through its modulus, and the operator is not multiplicative, because the central scale is not of modulus one.

### A General Unit-Norm Element

Take $\tilde{G} = e_0 + ie_1 + e_2$, whose norm form is $N = 1 + i^2 + 1 = 1$, so the element lies on the unit-norm slice. Its polar representation has a nontrivial boost factor,

$$
B = \sqrt{2}\,e_0 + \frac{\sqrt2}{2}ie_1 - \frac{\sqrt2}{2}ie_3 ,
$$

which is not the unit, so by the structure theorem the element is not one of those whose operator preserves the subspace structure. The sandwich on the Hermitian element $ie_0$ gives

$$
\operatorname{H}_{\tilde{G}}(ie_0) = 3ie_0 - 2e_1 + 2e_3 ,
$$

which is Hermitian, as the sector theorem requires, and whose norm form is $N = (3i)^2 + 4 + 4 = -9 + 8 = -1$, equal to the norm form of $ie_0$ because $|N(\tilde{G})| = 1$. The operator is therefore a Lorentz transformation of the algebra and not a rotation, and the nontrivial boost factor is exactly what makes it so.

### Rank and the Null Cone

Take the two elements $e_0 + e_1$ and $e_0 + ie_1$. Their norm forms are $N = 1 + 1 = 2$ and $N = 1 - 1 = 0$, so the first is a unit and the second is a zero divisor. The matrix images are

$$
\Phi(e_0 + e_1) = \begin{pmatrix} 1 & -i \\ -i & 1 \end{pmatrix} , \qquad \Phi(e_0 + ie_1) = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} ,
$$

of ranks two and one respectively, and the second matrix visibly has a one-dimensional image. The sandwich cannot move one into the other, because it preserves the rank of the matrix image; it moves each within its own class; and the class of the second is the non-zero rank-one stratum, the null cone of the material sector, which the Lorentz action moves transitively. The example is the smallest one that shows the rank as an invariant independent of the norm form, since the null cone is exactly the rank-one stratum and the norm form alone would not distinguish a rank-one element from the origin.

## For Contrast: the Automorphism

The other two-sided sandwich of the algebra is built from the inverse rather than from the Hermitian conjugate,

$$
x \longmapsto \tilde{Q}\,x\,\tilde{Q}^{-1} ,
$$

and it is recorded here, in the last section, because the article's subject is the dagger sandwich while the contrast between the two maps is short and sharp. The inverse sandwich is an **automorphism** of the algebra: it is multiplicative, it preserves the norm form of every element exactly, and it is the concrete realisation of the inner automorphism group. It is *not* the sector-preserving form — the dagger sandwiches are the only two-sided sandwiches that preserve the two sectors, which is the reason the physics articles write the four-vector action with a dagger — and its relation to the dagger sandwich is the factorisation recorded below.

### The Inverse Sandwich

Let $\tilde{Q}$ be a unit of $\mathbb{B}$, that is, an element with $N(\tilde{Q}) \neq 0$, equivalently an element whose matrix image is invertible. The **inverse sandwich**, or conjugation, or inner action, is

$$
\operatorname{Int}_{\tilde{Q}}:\ \mathbb{B} \longrightarrow \mathbb{B} , \qquad \operatorname{Int}_{\tilde{Q}}(x) = \tilde{Q}\,x\,\tilde{Q}^{-1} = \frac{\tilde{Q}\,x\,\bar{\tilde{Q}}}{N(\tilde{Q})} .
$$

The second expression uses $\tilde{Q}^{-1} = \bar{\tilde{Q}}/N(\tilde{Q})$ and makes the central denominator explicit. Because $N(\tilde{Q})$ is central it may be placed anywhere in the product, and the two forms of the definition agree.

### It Is an Automorphism

**Theorem.** For every unit $\tilde{Q}$, the map $\operatorname{Int}_{\tilde{Q}}$ is an algebra automorphism of $\mathbb{B}$, and the assignment $\tilde{Q} \mapsto \operatorname{Int}_{\tilde{Q}}$ is a homomorphism from the group of units to the automorphism group of $\mathbb{B}$.

**Proof.** The map is $\mathbb{C}$-linear, because multiplication by a fixed element and by its fixed inverse are $\mathbb{C}$-linear on $\mathbb{B}$ regarded as a complex vector space. It is multiplicative, since

$$
\operatorname{Int}_{\tilde{Q}}(xy) = \tilde{Q}xy\tilde{Q}^{-1} = \left(\tilde{Q}x\tilde{Q}^{-1}\right)\left(\tilde{Q}y\tilde{Q}^{-1}\right) = \operatorname{Int}_{\tilde{Q}}(x)\operatorname{Int}_{\tilde{Q}}(y) ,
$$

the middle equality inserting $\tilde{Q}^{-1}\tilde{Q} = e_0$ between $x$ and $y$. It is injective, because $\operatorname{Int}_{\tilde{Q}}(x) = 0$ gives $x = 0$, and surjective, because $y = \operatorname{Int}_{\tilde{Q}}(\tilde{Q}^{-1}y\tilde{Q})$. Hence it is an automorphism. For the homomorphism property, $\operatorname{Int}_{\tilde{Q}}\operatorname{Int}_{\tilde{R}}(x) = \tilde{Q}\tilde{R}x\tilde{R}^{-1}\tilde{Q}^{-1} = \operatorname{Int}_{\tilde{Q}\tilde{R}}(x)$. $\square$

Because it is an automorphism, $\operatorname{Int}_{\tilde{Q}}$ carries every algebraically defined subset of $\mathbb{B}$ to a subset of the same kind: it maps the centre to the centre, the set of zero divisors to itself, the set of idempotents to itself, the derived subspace $[\mathbb{B},\mathbb{B}]$ to itself, and it preserves the rank of the matrix image. The preservation of the rank is worth isolating, because the rank is the invariant that classifies the elements of $\mathbb{B}$ as a matrix algebra and it is not a polynomial in the coefficients of a degree that the norm form sees:

$$
\operatorname{rank}\Phi\!\left(\operatorname{Int}_{\tilde{Q}}x\right) = \operatorname{rank}\Phi(x) ,
$$

since $\Phi(\operatorname{Int}_{\tilde{Q}}x) = \Phi(\tilde{Q})\Phi(x)\Phi(\tilde{Q})^{-1}$ and conjugation by an invertible matrix does not change the rank.

### The Kernel Is the Centre

**Theorem.** $\operatorname{Int}_{\tilde{Q}}$ is the identity map if and only if $\tilde{Q}$ lies in the centre, $\tilde{Q} = z e_0$ with $z \in \mathbb{C}^{\times}$. More generally $\operatorname{Int}_{\tilde{Q}} = \operatorname{Int}_{\tilde{R}}$ if and only if $\tilde{Q}\tilde{R}^{-1}$ lies in the centre.

**Proof.** If $\tilde{Q} = ze_0$ then $\operatorname{Int}_{\tilde{Q}}(x) = zxz^{-1} = x$ for every $x$. Conversely suppose $\operatorname{Int}_{\tilde{Q}}(x) = x$ for every $x$; then $\tilde{Q}x = x\tilde{Q}$ for every $x$, which is the definition of the centre, and the centre of $\mathbb{B}$ is $\mathbb{C}_{\mathbb{B}}$. For the second statement, $\operatorname{Int}_{\tilde{Q}} = \operatorname{Int}_{\tilde{R}}$ is equivalent to $\operatorname{Int}_{\tilde{Q}\tilde{R}^{-1}} = \mathrm{id}$, hence to $\tilde{Q}\tilde{R}^{-1}$ central. $\square$

The kernel is therefore the multiplicative group of the centre, $\mathbb{C}_{\mathbb{B}}^{\times} = \mathbb{C}^{\times}e_0$, of two real dimensions, and the operator loses exactly the two real parameters of the central phase. The loss is the reason the action is not faithful, and it has an exact physical reading: the operator of an element and the operator of that element multiplied by any non-zero complex scalar are the same operator, so no operator can detect the central phase.

### The Action Sees Only the Class of $\tilde{Q}$

The theorem has a corollary that connects the operator representation to the polar representation, and it is worth stating separately because it is the bridge between the two subjects.

**Corollary.** Let $\tilde{Q} = r e^{i\alpha} B\hat{q}$ be the polar representation of a unit, with $r$ the scale, $e^{i\alpha}$ the central phase, $B$ the boost and $\hat{q}$ the rotor. Then

$$
\operatorname{Int}_{\tilde{Q}} = \operatorname{Int}_{B\hat{q}} = \operatorname{Int}_{B}\circ \operatorname{Int}_{\hat{q}} .
$$

**Proof.** The scale and the phase form the central factor $\rho = re^{i\alpha} = \sqrt{N(\tilde{Q})}$, so $\tilde{Q} = \rho(B\hat{q})$ with $\rho$ central, and the first equality is the second statement of the previous theorem. The second equality is the homomorphism property. $\square$

The operator therefore depends on the centre-free part $B\hat{q}$ alone — three real parameters of the boost and three of the rotor, six in all, matching the real dimension of the inner automorphism group computed in the next section — and not on the scale or on the phase. A photometric reading is available and useful: the operator factors as a boost operator followed by a rotor operator, and the order in the factorisation is the order of the composition, exactly as in the polar representation itself. The two factors do not commute, so the order matters and cannot be reversed.

### The Image Is the Inner Automorphism Group

Every automorphism produced by the construction is inner, and conversely every inner automorphism of $\mathbb{B}$ is produced by it: for $\mathbb{B} \cong M_2(\mathbb{C})$, the Skolem–Noether theorem states that every $\mathbb{C}$-algebra automorphism is of the form $x \mapsto TxT^{-1}$ with $T \in GL_2(\mathbb{C})$, unique up to scalars. The image is therefore the group of inner automorphisms,

$$
\operatorname{Int}\!\left(\mathbb{B}^{\times}\right) = \operatorname{Inn}(\mathbb{B}) \cong \mathbb{B}^{\times}/\mathbb{C}_{\mathbb{B}}^{\times} \cong PGL_2(\mathbb{C}) \cong PSL_2(\mathbb{C}) ,
$$

the last isomorphism because every class in $PGL_2(\mathbb{C})$ has a representative of determinant one after scaling. The scalar ambiguity in Skolem–Noether is exactly the kernel computed above, and this is the sense in which the operator representation is the concrete realisation of the automorphism group of the algebra. It is the same group that appears as the entry $\operatorname{Aut}_{\mathbb{C}}(\mathbb{B}) = PSL_2(\mathbb{C})$ of the ladder of operator spaces in *The Operators on an Algebra*, reached there in the abstract and here through the inverse sandwich.

The real dimensions agree and the count is worth making explicit. The group of units of $\mathbb{B}$ has real dimension eight; the kernel has real dimension two; the image, being $PGL_2(\mathbb{C})$, has real dimension six, which is also the dimension of $SO(1,3)$ and of $\mathfrak{sl}(2,\mathbb{C})$ regarded over $\mathbb{R}$. The three numbers $8 = 2 + 6$ are the whole content of the action, and the six is the number of parameters of the operator.

### The Automorphisms That Are Not Inner

One automorphism of $\mathbb{B}$ is not inner and must be kept apart from the action: the map ${}^{*}$ that conjugates the coefficients. It is an algebra automorphism over $\mathbb{R}$ but not over $\mathbb{C}$, since it sends $i$ to $-i$, while every inner automorphism is $\mathbb{C}$-linear because $\tilde{Q}$ and $\tilde{Q}^{-1}$ commute with $i$. Hence the automorphism group of $\mathbb{B}$ as a real algebra is larger than the image of the operator action,

$$
\operatorname{Aut}_{\mathbb{R}\text{-alg}}(\mathbb{B}) \cong PGL_2(\mathbb{C}) \rtimes \mathbb{Z}/2 ,
$$

and the inverse sandwich produces only the identity component. The consequence for the subspace structure is direct and is used below: no operator of the form $\operatorname{Int}_{\tilde{Q}}$ can reproduce the map ${}^{*}$, and a general operator need not even preserve the halves, because $\operatorname{Int}_{\tilde{Q}}$ need not commute with ${}^{*}$. What it does instead is to carry $\mathbb{H}_{\mathbb{B}}$ to the fixed space of the *conjugated* real structure $\operatorname{Int}_{\tilde{Q}}\circ{}^{*}\circ\operatorname{Int}_{\tilde{Q}}^{-1}$, which is a new real form, generally neither $\mathbb{H}_{\mathbb{B}}$ nor $i\mathbb{H}_{\mathbb{B}}$; the example below exhibits an element of $\mathbb{H}_{\mathbb{B}}$ whose image has both real and imaginary coefficients.

### It Is an Automorphism Followed by a Right Multiplication

The defect is nevertheless of a completely explicit kind, and the factorisation isolates it.

**Proposition.** With $\tilde{Q}$ a unit, $S = \tilde{Q}\tilde{Q}^\dagger$ the Hermitian positive element it determines, and $R_S$ the right multiplication by $S$,

$$
\operatorname{H}_{\tilde{Q}} = R_{S}\circ \operatorname{Int}_{\tilde{Q}} , \qquad \operatorname{H}_{\tilde{Q}}(x) = \operatorname{Int}_{\tilde{Q}}(x)\,S .
$$

**Proof.** $\operatorname{Int}_{\tilde{Q}}(x)\,S = \tilde{Q}x\tilde{Q}^{-1}\tilde{Q}\tilde{Q}^\dagger = \tilde{Q}x\tilde{Q}^\dagger$. $\square$

The whole failure of multiplicativity is carried by the single right multiplication, and it disappears exactly when $S$ is central. This is the algebraic reason for the equivalence proved in the main text: the inverse sandwich and the dagger sandwich coincide exactly when $\tilde{Q}\tilde{Q}^\dagger = e_0$, that is, when $\tilde{Q}$ is **unitary**, and the unitary elements are precisely the unit-modulus central phases times the real unit quaternions.

The factorisation also displays where the dagger sandwich gets its invariance of the interval. The norm form is multiplicative, so $N\!\left(\operatorname{H}_{\tilde{Q}}(x)\right) = N\!\left(\operatorname{Int}_{\tilde{Q}}(x)\right)N(S) = N(x)\,|N(\tilde{Q})|^2$: the right multiplication by $S$ is exactly the factor that rescales the interval, and it is the unit only when $\tilde{Q}$ is unitary, which is the case in which the two maps coincide. On the unit-norm slice this factor is one, and there the two maps agree whenever they agree at all.

### Conjugation of Matrices

The isomorphism $\Phi$ turns the inverse sandwich into conjugation of $2 \times 2$ complex matrices,

$$
\Phi\!\left(\operatorname{Int}_{\tilde{Q}}(x)\right) = \Phi(\tilde{Q})\,\Phi(x)\,\Phi(\tilde{Q})^{-1} ,
$$

which is read off from the multiplicativity of $\Phi$ and makes the statements of this section properties of $M_2(\mathbb{C})$: the inverse sandwich is the action of $GL_2(\mathbb{C})$ on the full matrix algebra by similarity, its orbits are the conjugacy classes, classified by the Jordan form, so two elements of $\mathbb{B}$ are in the same orbit exactly when their matrix images have the same Jordan form. Its dagger counterpart, the congruence of the main text, is the map that preserves the Hermitian forms instead of the conjugacy classes. A similarity cannot change the trace or the determinant either, so its orbits refine the level sets of the norm form, which is the determinant.

### The Automorphism Moves the Halves

The difference between the two maps is visible on the antiquaternions. For the unit-norm element $\tilde{G} = e_0 + ie_1 + e_2$ of the worked example of the main text, whose polar boost factor is not the unit, the automorphism gives

$$
\operatorname{Int}_{\tilde{G}}(e_2) = 2ie_1 + 3e_2 + 2ie_3 ,
$$

which has both real and imaginary coefficients: an element of the quaternion subspace is taken out of it, and a rotation would have preserved it. The comparison is the content of the subspaces table of the main text, where the dagger sandwich preserves the two sectors for every element while the automorphism preserves the two halves only for a unitary element.

### An Inner Derivation

Take $X = e_1$ and compute the infinitesimal operator of the inverse sandwich on the other units:

$$
[e_1, e_2] = e_1e_2 - e_2e_1 = e_3 + e_3 = 2e_3 , \qquad [e_1, e_3] = e_1e_3 - e_3e_1 = -e_2 - e_2 = -2e_2 , \qquad [e_1, e_1] = 0 .
$$

The infinitesimal operator reproduces the rotation generated by $e_1$, up to the factor two that the doubling produces: the finite operator is a rotation through $2\theta$ and the infinitesimal one generates a rotation through $\theta$ for the parametrisation $\hat{q} = \cos\theta + \sin\theta e_1$. The factor two here and the doubling of the previous section are the same factor.

Finally, the two kernels side by side, which is the exact statement of what each map loses:

| action | group | kernel | parameters lost |
|---|---|---|---|
| $\operatorname{Int}_{\tilde{Q}}(x)=\tilde{Q}x\tilde{Q}^{-1}$ | units of $\mathbb{B}$ | $\mathbb{C}_{\mathbb{B}}^{\times}$ | the scale and the phase |
| $\operatorname{H}_{\tilde{Q}}(x)=\tilde{Q}x\tilde{Q}^\dagger$ | units of $\mathbb{B}$ | $U(1)\subset\mathbb{C}_{\mathbb{B}}$ | the circle only |
| $\operatorname{H}_{\tilde{\Lambda}}(x)=\tilde{\Lambda}x\tilde{\Lambda}^\dagger$ | unit-norm $SL(2,\mathbb{C})$ | $\{\pm e_0\}$ | the sign |


## Summary

A unit $\tilde{Q}$ of $\mathbb{B}$ acts on the algebra by the **sandwich**

$$
\operatorname{H}_{\tilde{Q}}(x) = \tilde{Q}\,x\,\tilde{Q}^\dagger ,
$$

and the sandwich is the Lorentz action of the series written on the whole algebra, so it is the subject of the article. Among the two-sided sandwiches it is the only form that preserves the two sectors, and on the unit-norm slice it is the form that leaves the interval invariant.

The sandwich **preserves the two sectors and no other of the six subspaces**, it preserves the rank of the matrix image, and it scales the norm form by $|N(\tilde{Q})|^2$, which is one on the unit-norm slice. Its kernel is the central circle $U(1)$, so it is blind to a central phase and to nothing else; on the unit-norm slice the kernel is $\{\pm e_0\}$, which is the double cover of the Lorentz group by the rotors. The multiplicative criterion and the structure-preserving criterion agree, since the sandwich is multiplicative exactly when the acting element is unitary, which is exactly when it fixes the time axis, and the operators preserving the whole subspace structure are exactly those whose element is a central multiple of a real unit quaternion.

The dagger is what makes the sandwich an operator of the interval rather than an operator of the algebra. Its infinitesimal form is $Xx + xX^\dagger$, the commutator along the anti-Hermitian directions and the anticommutator along the Hermitian ones, so the rotations and the boosts appear in one formula with two different symmetries; and the same dagger gives the two double covers of the corpus, the rotation group by the unit real quaternions and the Lorentz group by the unit-norm biquaternions. The half-angle in the rotor and the double angle in the operator are one fact, and the four-factor polar representation is the object that decides which operators respect the corpus's six subspaces.

The automorphism $x \mapsto \tilde{Q}x\tilde{Q}^{-1}$ of the last section is the operator that respects the multiplication and the norm form exactly, and it is not the interval-conserving map; that is the sense in which the dagger, and not the inverse, is the sandwich of the corpus.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, $8$-dimensional over $\mathbb{R}$ |
| $\tilde{Q}$ | a general element; a unit when $N(\tilde{Q}) \neq 0$ |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2 = \det\Phi(\tilde{Q})$ | the norm form |
| $\tilde{Q}^{-1} = \bar{\tilde{Q}}/N(\tilde{Q})$ | the inverse of a unit |
| $\operatorname{H}_{\tilde{Q}}(x) = \tilde{Q}x\tilde{Q}^\dagger$ | the sandwich, or dagger sandwich; the physics rotor conjugation for a rotor |
| $\operatorname{H}_{z\tilde{Q}} = \lvert z\rvert^2\operatorname{H}_{\tilde{Q}}$ | the central rule, $z$ central |
| $\operatorname{H}_{\tilde{Q}\tilde{R}} = \operatorname{H}_{\tilde{Q}}\circ\operatorname{H}_{\tilde{R}}$ | the composition law |
| $Xx + xX^\dagger$ | the infinitesimal operator, $[X,x]$ on the anti-Hermitian directions |
| $\operatorname{Int}_{\tilde{Q}}(x) = \tilde{Q}x\tilde{Q}^{-1}$ | the inverse sandwich, or inner action (contrast section) |
| $\operatorname{ad}_X(x) = [X,x]$ | the inner derivation, the derivative of the inverse sandwich |
| $\operatorname{Inn}(\mathbb{B}) \cong PGL_2(\mathbb{C}) \cong PSL_2(\mathbb{C})$ | the image of the inverse sandwich |
| $SO(3) \cong SU(2)/\{\pm e_0\}$ | the operators that preserve the six subspaces of the unit-norm slice |
| $\mathbb{C}_{\mathbb{B}}^{\times} = \mathbb{C}^{\times}e_0$ | the kernel of the inverse sandwich |
| $U(1) = \{e^{i\theta}e_0\}$ | the kernel of the sandwich |
| $R_S$ | right multiplication by $S$, $R_S(x) = xS$, in the factorisation of the contrast section |
| $\tilde{Q} = re^{i\alpha}B\hat{q}$ | the polar representation of a unit |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | the Hermitian and anti-Hermitian sectors |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | the quaternion and antiquaternion subspaces |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$ | the centre and the vector subspace |

## Further Reading

- *Biquaternion Polar Representation* (`articles_maths/biquaternion-polar-representation.md`), for the four factors of a single element and the theorem that they exist and are unique
- *Biquaternion Partial Polar Representations* (`articles_maths/biquaternion-partial-polar-representations.md`), for the three pairings of the four factors, immediately before the present article in the menu
- *Biquaternion Representation Theory* (`articles_maths/biquaternion-representation-theory.md`), for the automorphisms, the derivations and the Skolem–Noether theorem in their own right
- *Biquaternion Algebraic Representations* (`articles_maths/biquaternion-algebraic-representations.md`), for the four-vector, matrix, spinor and Clifford representations of the algebra
- *Biquaternion 4×4 Regular Matrix Representation* (`articles_maths/biquaternion-4x4-regular-matrix-representation.md`), for left multiplication, the operator of this article's comparison column
- *Biquaternion Zero Divisors* (`articles_maths/biquaternion-zero-divisors.md`), for the rank-one stratum and the null cone as orbits
- *Biquaternion Roots of Minus One* (`articles_maths/biquaternion-roots-of-minus-one.md`), for the elements of square minus the unit, the generators of the operators of order two
- *Spinors and the Biquaternion Spinor Module* (`articles_maths/spinors-and-the-biquaternion-spinor-module.md`), for the double cover and the spinor module
- *Spin Representations and Clifford Modules* (`articles_maths/spin-representations-and-clifford-modules.md`), for the spin representations in general
- *The Clifford, Pin and Spin Groups* (`articles_maths/the-clifford-pin-and-spin-groups.md`), for the twisted adjoint action, which is the sandwich in a general Clifford algebra
- *The Biquaternion Algebra as a Clifford Algebra* (`articles_maths/the-biquaternion-algebra-as-a-clifford-algebra.md`), for the Clifford reading of the same algebra
- *The Operators on an Algebra* (`articles_maths/the-operators-on-an-algebra.md`), for the ambient space of all linear operators on an algebra, the ladder of subspaces and groups inside it, and the abstract statement $\operatorname{Aut}_{\mathbb{C}}(\mathbb{B}) = PSL_2(\mathbb{C})$
- *Versors, Rotors and the Sandwich Action* (`articles_maths/versors-rotors-and-the-sandwich-action.md`), for the sandwich action in the Clifford setting and the half angle that separates the action on vectors from the action on spinors
- *The Rotation and Reflection Groups in the Biquaternion Algebra* (`articles_maths/the-rotation-and-reflection-groups-in-the-biquaternion-algebra.md`), for the finite and continuous subgroups the operators generate
- *Worked Examples in the Biquaternion Algebra* (`articles_maths/worked-examples-in-the-biquaternion-algebra.md`), for the basis products used in the worked examples above
- *Relations Between Subspaces* (`articles_physics/relations-between-subspaces.md`), for the six subspaces and their intersections, in the physics menu
- *The Operator Representation of Biquaternions* (`articles_physics/the-operator-representation-of-biquaternions.md`), the companion article, for the same sandwich read as the action of boosts and rotations
