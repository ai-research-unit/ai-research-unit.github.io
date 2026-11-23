# __The Group of Unit-Norm Biquaternions__

## Introduction

The group of this block is the set of biquaternions of unit norm. It is the spinor group of the restricted Lorentz group, it is the group of $2\times2$ complex matrices of determinant one, and it is the manifold on which the two decompositions of the block are defined. Its elements are the Lorentz rotors. This article states what the set is, proves that it is a group, gives its two descriptions, counts its dimension twice, identifies its compact part, and describes the exponential chart together with the set on which the chart ceases to be one-to-one.

The group is the object the rest of the block acts with. The next two articles take its two actions; the two after that take its Lie algebra; the decompositions take its polar and spectral structure. Everything here is therefore load-bearing, and the article is written to be used rather than admired.

The article assumes *The Isomorphisms and Their Dimensions* for the map and for the dimensions of the algebra, and *Norm and Pairing Conventions* for the norm, the modulus and the quaternion conjugation. The parametrisation of a boost and of a rotation is taken from *The Lorentz Transformation as a Biquaternionic Rotation* and is not re-derived.

## The Group as a Set

### The Defining Condition

$$
G=\{\tilde U\in\mathbb{B}:\langle\tilde U\rangle_{\natural}=e_t\}
=\{\tilde U:\tilde U\tilde U^{\natural}=e_t\},
$$

where $\natural$ is the quaternion conjugation, $\tilde U^{\natural}=U_t-U_x\vec e_x-U_y\vec e_y-U_z\vec e_z$, and $\langle\tilde U\rangle_{\natural}=U_t^{2}+U_x^{2}+U_y^{2}+U_z^{2}$ is the quaternionic norm of *Norm and Pairing Conventions*.

The condition is **complex**: $\langle\tilde U\rangle_{\natural}=1$ is one equation over $\mathbb{C}$, that is two real equations, on eight real coordinates. It is not the condition $\lvert\langle\tilde U\rangle_{\natural}\rvert=1$, which would define a different and larger set. A reader who replaces the norm by its modulus gets the group of biquaternions whose norm is a unit complex number, and that set is not the Lorentz group.

Under the isomorphism the condition is $\det\mathsf{M}_2(\tilde U)=1$, so

$$
G\cong SL(2,\mathbb{C}).
$$

### Closure

Let $\tilde U,\tilde V\in G$. The norm is multiplicative,

$$
\langle\tilde U\tilde V\rangle_{\natural}=\langle\tilde U\rangle_{\natural}\langle\tilde V\rangle_{\natural}=e_t,
$$

so $\tilde U\tilde V\in G$. The multiplicativity is not an accident of this norm: it is the multiplicativity of the determinant of the image under the isomorphism, and it is the single algebraic fact on which the group structure rests.

### The Inverse

$$
\tilde U^{-1}=\tilde U^{\natural},
$$

because the norm is central: $\tilde U\tilde U^{\natural}=\langle\tilde U\rangle_{\natural}=e_t$ and equally $\tilde U^{\natural}\tilde U=e_t$. The quaternion conjugate is therefore the group inverse on $G$, and it is a two-sided inverse rather than a one-sided one for exactly that reason. On a boost, $\tilde U_{\mathrm b}(\vec u_{\mathrm b},\theta_{\mathrm{rpd}})^{-1}=\tilde U_{\mathrm b}(\vec u_{\mathrm b},-\theta_{\mathrm{rpd}})$; on a rotation, $\tilde u_{\mathrm r}(\vec u_{\mathrm r},\theta_{\mathrm{axr}})^{-1}=\tilde u_{\mathrm r}(\vec u_{\mathrm r},-\theta_{\mathrm{axr}})$.

### The Centre

A central element of $G$ is a complex scalar $\lambda$ with $\lambda^{2}=1$, so

$$
Z(G)=\{\pm e_t\}\cong\mathbb{Z}/2\mathbb{Z}.
$$

That group is the kernel of the double cover and the reason every conjugation is blind to the sign of the rotor. *The Two-Sheeted Cover and the Topology of the Group* is the article that reads it physically.

### What the Set Is Not

The unit-norm set is not compact, and it is not the group of invertibles. The group of invertibles is $\mathbb{B}^{\times}=\{\tilde Q:\langle\tilde Q\rangle_{\natural}\neq0\}\cong GL_2(\mathbb{C})$, of real dimension eight, and $G$ is the kernel of the norm inside it. The distinction matters in *The Two Actions of One Group: Adjoint and Congruence*, where one action is defined for all of $\mathbb{B}^{\times}$ and the other is not.

## Two Descriptions of One Element

### The First Description: By the Unit Norm

One complex equation, as above. Its advantage is that it uses nothing but the algebra: no axis, no frame, no decomposition. Its disadvantage is that it says nothing about what the element does.

### The Second Description: By a Hermitian Pair of Factors

Every element of $G$ is a product of a Hermitian factor and a unitary one,

$$
\tilde U=\tilde H\tilde\Upsilon,\qquad
\tilde H=\tilde H^{*},\quad \operatorname{Tr}\mathsf{M}_2(\tilde H)>0,\quad \det\mathsf{M}_2(\tilde H)=1,
\qquad \tilde\Upsilon^{*}\tilde\Upsilon=e_t,
$$

and the pair is unique. The Hermitian factor is a positive Hermitian matrix of determinant one; the unitary factor is a $*$-unitary biquaternion of determinant one, which is to say a unitary $2\times2$ matrix of determinant one.

Three facts about this description are needed later, and each is proved in *The Cartan Decomposition: Every Lorentz Transformation as a Boost and a Rotation*.

- The Hermitian factor is a pure boost: it is $\tilde U_{\mathrm b}=\exp(i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b})$.
- The unitary factor is a pure rotation: it is $\tilde u_{\mathrm r}=\exp(\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r})$.
- Positivity is what makes the pair unique, and positivity of a Hermitian matrix of determinant one is an open condition, so the pair varies smoothly.

So the second description of an element of the group is **a boost and a rotation**, and the second description of the group is the product of the two sets. The product is not a direct product of groups: $P$ is a submanifold and not a subgroup, and the two sets meet in $e_t$ alone, which is why the word is written $P\cdot K$ and not $P\times K$.

### The Two Columns as a Spinor Pair

A third description is worth recording because it is the one *The Spinor Module in Biquaternionic Form and Its Lorentz Action* uses. The image of an element is a matrix of determinant one,

$$
\mathsf{M}_2(\tilde U)=\bigl(\xi\ \ \eta\bigr),
$$

whose columns $\xi,\eta$ are two spinors. The determinant condition becomes

$$
\det\bigl(\xi\ \ \eta\bigr)=1,
$$

which is the statement that the two spinors are paired to one by the antisymmetric Hermitian form of the module. An element of the group is therefore also a **Hermitian pair of spinors**, and the group is the set of such pairs. This description is the one that makes the one-sided action on spinors and the two-sided action on four-vectors different actions of the same object.

### Why the Descriptions Agree

The three descriptions are one element read three ways:

| description | the data | what it shows |
|---|---|---|
| unit norm | one complex equation on eight real coordinates | the set, with no frame |
| Hermitian pair of factors | a positive Hermitian factor and a unitary factor | the boost and the rotation, and the Cartan word |
| Hermitian pair of spinors | two columns with pairing one | the module and its two chiral halves |

## The Dimension Count

### Six Real Dimensions

$G$ has real dimension six and complex dimension three.

The count from the defining condition: eight real coordinates, two real equations, so $8-2=6$. The count from the isomorphism: $SL(2,\mathbb{C})$ is the determinant-one locus in $M_2(\mathbb{C})$, which has four complex entries and one complex equation, so complex dimension three and real dimension six.

### Three Plus Three

The count from the second description: the boosts contribute three parameters, the rapidity vector $\theta_{\mathrm{rpd}}\vec u_{\mathrm b}$, and the rotations contribute three, the axis-angle vector $\theta_{\mathrm{axr}}\vec u_{\mathrm r}$. The sum is six, and it is a genuine sum and not a product of independent sets, because the pair is unique once positivity is imposed.

The two parametrisations are therefore coordinates and not just labels. Every element of the group is a boost of some rapidity along some direction followed by a rotation of some angle about some axis, and no information is thrown away in saying so.

### Why the Algebra Has Eight and the Group Six

This is the one count that readers get wrong, and the two answers are different for two different reasons.

- The **associative algebra** $\mathbb{B}$ has real dimension eight. The group is cut out of it by the norm condition, which is one complex equation, so the group has six. The two directions lost are the scale $r$ and the central phase $\theta_{\mathrm{pha}}$: a unit-norm element has neither, and every element of the group of invertibles is a positive scale times a central phase times an element of $G$.
- The **Lie algebra** of $G$ has real dimension six, and it is the traceless part. It is *not* the associative algebra under the commutator, which has eight; the two extra directions are the centre, and the centre exponentiates to the scale and to the phase, neither of which lies in $G$.

So "the group is six-dimensional while the algebra is eight" is true of the associative algebra and false of the Lie algebra, and a sentence that does not say which is meant cannot be checked.

## The Compact Subgroup and the Non-Compact Direction

### The Compact Subgroup

The $*$-unitary elements of $G$ form the maximal compact subgroup,

$$
K=\{\tilde\Upsilon\in G:\tilde\Upsilon^{*}\tilde\Upsilon=e_t\}\cong SU(2),
$$

of real dimension three. Because the elements of $K$ have real quaternion coefficients, $K=SL(2,\mathbb{C})\cap\mathbb{B}_{H}$: the compact part of the group is the group of unit real quaternions, which is the rotation group's double cover. On $K$ the norm condition and the $*$-unitarity condition coincide, which is why rotations are both unit-norm and unitary.

### The Non-Compact Direction

The complement of $K$ in the group is where the boosts live. The set of positive Hermitian elements of unit norm,

$$
P=\{\tilde H\in G:\tilde H^{*}=\tilde H,\ \operatorname{Tr}\mathsf{M}_2(\tilde H)>0\},
$$

is a closed submanifold of dimension three, diffeomorphic to $\mathbb{R}^{3}$ through the rapidity vector, and it is not a subgroup: the product of two of its elements is generally not Hermitian. It is the symmetric space $G/K$, and the identification is the polar decomposition.

### The Shape of the Group

Three consequences, each of which is used later.

- **It retracts onto $SU(2)$.** Every element is uniquely a positive Hermitian factor times a unitary one, so the group is homeomorphic to $\mathbb{R}^{3}\times SU(2)$ and deformation-retracts onto $SU(2)\cong S^{3}$. It is therefore connected and simply connected, and its fundamental group is trivial. That triviality is what makes the double cover of the Lorentz group a cover of a simply connected group.
- **It is not compact.** The rapidity is unbounded. A compact group has a finite invariant measure of finite total mass, and this one does not: the measure on the boosts grows like $\sinh^{2}\theta_{\mathrm{rpd}}$. *The Invariant Measure on the Mass Shell* is the article that uses the growth.
- **Its two ends.** Because the boosts are a vector space, the group has one end, and the Lorentz group obtained by quotienting by $\{\pm e_t\}$ has one end as well. This is the topological reason a boost cannot be continuously undone by rotations alone.

## The Exponential Chart

### The Chart

$$
\exp:\mathfrak{sl}(2,\mathbb{C})\longrightarrow G,\qquad
\exp(\tilde X)=\sum_{n\ge0}\frac{\tilde X^{n}}{n!},
$$

with $\mathfrak{sl}(2,\mathbb{C})$ the scalar-free part, of real dimension six. The chart is **not** onto the group: it misses one conjugacy class, the class of $-e_t+\tilde N$ with $\tilde N$ a nonzero nilpotent, and *The Exponential Map from Algebra to Group* proves both the exclusion and the fact that every element of the group is a product of two exponentials. This article records what the chart is, and the other states what it covers.

For a pure generator the series closes, because every traceless element satisfies a quadratic,

$$
\exp(a\vec u)=\cos a+\sin a\,\vec u\quad(\vec u^{2}=-e_t),
\qquad
\exp(ia\vec u)=\cosh a+i\sinh a\,\vec u\quad(\vec u^{2}=-e_t),
$$

and these two lines are the rotation and the boost of the block in exponential form. With the half-angle convention, a rotation of angle $\theta_{\mathrm{axr}}$ is $\exp(\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r})$ and a boost of rapidity $\theta_{\mathrm{rpd}}$ is $\exp(i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b})$.

### Where It Stops Being One-to-One

The chart is a local diffeomorphism away from its cut and it covers the group except for one conjugacy class, but it is not injective, and the failure has a shape.

- **The axes meet at the far point.** With a fixed axis, the rotation family is $\tilde u_{\mathrm r}(\theta_{\mathrm{axr}})=\cos\tfrac{\theta_{\mathrm{axr}}}{2}+\sin\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}$, so $\theta_{\mathrm{axr}}$ and $\theta_{\mathrm{axr}}+4\pi$ give the same element and $\theta_{\mathrm{axr}}+2\pi$ gives its negative. The chart is one-to-one on $0\le\theta_{\mathrm{axr}}<4\pi$ along each fixed axis, and the two ends coincide.
- **One element, every axis.** At $\theta_{\mathrm{axr}}=2\pi$ every axis gives the same element, $-e_t$. The sphere of radius $\pi$ in the rotation part of the algebra therefore collapses to a point of the group, and the chart is not injective on any neighbourhood of that sphere.
- **The identity is not isolated in the fibre.** $\exp(2\pi k\,\vec u)=e_t$ and $\exp((2k+1)\pi\,\vec u)=-e_t$ for every integer $k$ and every invertible $\vec u$, so the fibre over each of the two central elements contains a whole family of spheres.
- **The rapidity is injective but unbounded.** Along a fixed boost axis the map $\theta_{\mathrm{rpd}}\mapsto\exp(i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b})$ is injective on $\mathbb{R}$, since $\cosh$ and $\sinh$ are injective on the pair. The non-injectivity of the chart is entirely the compact direction's.

### Why the Fibre Matters Physically

An exponential coordinate is a set of six numbers that a laboratory could in principle dial: three rapidities and three rotation angles. The fibre is the statement that the dials do not determine the element uniquely, and it is the same statement as the two-to-one cover seen at the level of coordinates. A rotation by $2\pi$ returns $-e_t$ and not $e_t$; a rotation by $4\pi$ returns $e_t$. The physical interferometric mark of that sign is the subject of *The Two-Sheeted Cover and the Topology of the Group*.

The practical rule for this block: an exponential coordinate is used where a *path* is what is meant — a continuous motion of a frame — and never where an element alone is meant.

### The Reconstruction Check

The chart is used numerically throughout the block, and the check that it is being used correctly is the round trip. On four elements — a rotation by $0.7$, a boost of rapidity $0.9$, their product, and a random unit-norm element — computing a traceless logarithm and exponentiating again returns the element to $2\times10^{-16}$. The two central elements $\pm e_t$ are on the cut locus and need the analytic values $\exp(0)=e_t$ and $\exp(\operatorname{diag}(i\pi,-i\pi))=-e_t$; a naive numerical logarithm fails there, and that failure is the visible face of the excluded conjugacy class. The branches and the cut are the subject of *The Exponential Map from Algebra to Group*; the point here is that a numerical reader can trust the chart away from the cut.

## Summary

The group of unit-norm biquaternions is the set of elements whose quaternionic norm is exactly $1$, a complex condition, and it is $SL(2,\mathbb{C})$. It is closed under multiplication because the norm is multiplicative, its inverse is the quaternion conjugate, and its centre is $\{\pm e_t\}$. It has two descriptions: one complex equation, or a unique pair of a positive Hermitian factor and a unitary factor, which is the pair of a boost and a rotation. Its real dimension is six, three plus three; the associative algebra has eight because the group is cut out by two real conditions, and the Lie algebra has six because it is the traceless part. Its compact subgroup is $SU(2)$, the rotations; the boosts form the non-compact symmetric space $G/K\cong\mathbb{R}^{3}$; the group retracts onto $S^{3}$ and is simply connected. The exponential chart is locally one-to-one, covers the group except for one conjugacy class, and fails to be one-to-one exactly along the compact direction, where a $2\pi$ turn returns the negative of the identity and every axis meets at one point.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde U$ | an element of $G$, a unit-norm biquaternion |
| $\natural$ | the quaternion conjugation, $\tilde U^{\natural}=U_t-U_x\vec e_x-U_y\vec e_y-U_z\vec e_z$ |
| $\langle\tilde U\rangle_{\natural}$ | the quaternionic norm, $U_t^{2}+U_x^{2}+U_y^{2}+U_z^{2}$ |
| $G$ | the unit-norm group, $\cong SL(2,\mathbb{C})$ |
| $K$ | the maximal compact subgroup, $\cong SU(2)$, the rotations |
| $P$ | the positive Hermitian elements of unit norm, the boosts |
| $\tilde H\tilde\Upsilon$ | the polar pair, boost times rotation |
| $\theta_{\mathrm{rpd}}$, $\vec u_{\mathrm b}$ | rapidity and boost axis |
| $\theta_{\mathrm{axr}}$, $\vec u_{\mathrm r}$ | rotation angle and axis |

## Further Reading

- S. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, Academic Press, 1978 — $SL(2,\mathbb{C})$, its maximal compact subgroup, the Cartan decomposition and the symmetric space $G/K$.
- B. C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer, 2015 — the matrix exponential, its surjectivity on $SL(2,\mathbb{C})$ and the structure of its fibres.
- S. Lang, *$SL_2(\mathbb{R})$*, Addison-Wesley, 1975 — the same group and its decompositions treated as a working object, with the topology done explicitly.
- P. Lounesto, *Clifford Algebras and Spinors*, 2nd ed., Cambridge University Press, 2001 — the unit-norm biquaternions as a Clifford group and the identification with $SL(2,\mathbb{C})$.
- *The Lorentz Group in Biquaternionic Form — Structure and Representations*, §*The Group of Unit-Norm Biquaternions* — the survey's own statement of the closure, the inverse and the dimension.
- *The Two-Sheeted Cover and the Topology of the Group*, *The Exponential Map from Algebra to Group*, *The Cartan Decomposition: Every Lorentz Transformation as a Boost and a Rotation* — the three articles that take this group apart.
