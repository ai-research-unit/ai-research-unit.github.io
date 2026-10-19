# __The Polar Element Representation and Remarkable Subspaces__

## Introduction

The biquaternion algebra has six subspaces that the corpus calls **remarkable**: the centre, the vector space, the quaternion subspace, the anti-quaternion subspace, the Hermitian subspace and the anti-Hermitian subspace. They are the eigenspaces of the three conjugations and the two real forms, and they carry the physical readings of the algebra: the centre is the complex time, the vector space is the space, the quaternion subspace is the rotor space, and the Hermitian and anti-Hermitian subspaces are the two material sectors.

The polar representation is a product of four factors, and each factor preserves some of the six subspaces and moves the others. The pattern of preservation is the subject of this article. It answers a concrete question: given a polar factor, which subspaces can it see, and which does it mix? The answer is a table, and the table is the content of the article.

The main result is that **only the scale and the rotor preserve all six**. The phase preserves the centre and the vector space but not the quaternion halves; the boost preserves the two material sectors but not the centre or the vector space. The intersection of the subspaces preserved by all four factors is zero. The polar word is therefore not a decomposition adapted to a single subspace: it is a decomposition whose factors are adapted to different subspaces, and the word is the product that reconciles them.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$ and central $i$. The quaternion conjugation is $\natural$, the coefficientwise conjugation is $\bar{\cdot}$, and the Hermitian conjugation is ${}^{*}=\overline{\ \cdot\ }^{\natural}$. The norm is $\langle X\rangle_{\natural}=XX^{\natural}$. The polar word is

$$
\tilde Q=r\exp(i\alpha)B\tilde q,
\qquad
B=\exp(-i\psi\vec u_{\mathrm b}),
\qquad
\tilde q=\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr),
$$

with $r>0$, $\alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$, $\psi\ge0$, and unit axes, in the notation of *The Polar Element Representation of Biquaternions*.

## The Six Subspaces

The six subspaces are defined by the three conjugations.

| subspace | definition | real dimension | physical reading |
|---|---|---|---|
| centre $\mathbb{C}_{\mathbb{B}}$ | $\{a+ib:a,b\in\mathbb{R}\}$ | 2 | complex time, the informational scalar |
| vector space $\mathrm{Vect}(\mathbb{B})$ | $\{\vec v:\vec v\in\mathbb{C}^3\}$ | 6 | complex space |
| quaternion subspace $\mathbb{H}_{\mathbb{B}}$ | fixed by $\bar{\cdot}$ | 4 | real quaternions, rotors |
| anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ | anti-fixed by $\bar{\cdot}$ | 4 | imaginary quaternions |
| Hermitian subspace $\mathbb{M}_+$ | fixed by ${}^{*}$ | 4 | four-velocity, field strength |
| anti-Hermitian subspace $\mathbb{M}_-$ | anti-fixed by ${}^{*}$ | 4 | four-position, four-momentum |

The three conjugations are related by ${}^{*}=\overline{\ \cdot\ }^{\natural}=\bar{\cdot}^{\natural}$, and each has the two eigenspaces in the table. The centre and the vector space are the fixed and anti-fixed spaces of the **vector conjugation** that reverses the vector part; the quaternion and anti-quaternion subspaces are the eigenspaces of the **coefficient conjugation**; the Hermitian and anti-Hermitian subspaces are the eigenspaces of the **Hermitian conjugation**.

The six are not independent. The centre is contained in both $\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_+$; the vector space is contained in neither. The intersections are

$$
\mathbb{C}_{\mathbb{B}}\cap\mathrm{Vect}(\mathbb{B})=0,
\qquad
\mathbb{H}_{\mathbb{B}}\cap i\mathbb{H}_{\mathbb{B}}=0,
\qquad
\mathbb{M}_+\cap\mathbb{M}_-=0,
$$

and the corresponding sums are direct and equal to $\mathbb{B}$:

$$
\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B})
=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}
=\mathbb{M}_+\oplus\mathbb{M}_-.
$$

The three decompositions are three ways to cut the same eight real dimensions into two halves. They are not the same cut, and the polar factors are sensitive to the differences.

## The Preservation Table

A subspace is **preserved** by a factor $A$ if the action of the factor maps it into itself. For the scale, the boost and the rotor the action is the congruence $\Theta_A(X)=AXA^{*}$; for the phase, which is central and whose congruence is the identity, the action is left multiplication $X\mapsto \exp(i\alpha)X$, the action under which the phase is not in the kernel. The following table records the result. The marker **yes** means every element of the subspace is carried into the subspace; **no** means a generic element is carried out; the entries in parentheses are the exceptional parameter values.

| factor | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
|---|---|---|---|---|---|---|
| scale $r$ | yes | yes | yes | yes | yes | yes |
| phase $\exp(i\alpha)$ | yes | yes | no | no | no | no |
| boost $B$ | no | no | no | no | yes | yes |
| rotor $\tilde q$ | yes | yes | yes | yes | yes | yes |

The table is the answer in one view. The scale and the rotor preserve everything under the congruence; the phase preserves the first two under left multiplication; the boost preserves the last two. Under the congruence the phase is the identity and preserves all six, but that is the trivial reading: the phase is central, and the action that carries information about it is the multiplication on the left. No factor except the scale and the rotor preserves more than two of the six, and the two that preserve all six are the two central or real factors.

The degenerate entries are worth spelling out.

- **The phase at $\alpha=0$** is the identity and preserves all six. At $\alpha=\pi/2$ it maps $\mathbb{C}_{\mathbb{B}}$ into itself, $\mathrm{Vect}$ into $i\mathrm{Vect}=\mathrm{Vect}$, $\mathbb{H}_{\mathbb{B}}$ into $i\mathbb{H}_{\mathbb{B}}$, and $\mathbb{M}_+$ onto $\mathbb{M}_-$.
- **The boost at $\psi=0$** is the identity and preserves all six. At $\psi>0$ it preserves exactly $\mathbb{M}_+$ and $\mathbb{M}_-$.
- **The rotor at $\theta=0$ or $2\pi$** is the identity. At $\theta=\pi$ it preserves all six, with the vector part reversed on the perpendicular plane; the rotation by $\pi$ is still a rotation, not a reflection.

The table is the **generic** table. The exceptional values are the boundaries at which a factor degenerates to the identity or to a central scalar, and at those values the preserved set jumps to all six or to a different pair.

## Why the Table Holds

The four rows have four different mechanisms.

**The scale.** The scale is a positive real central element. Its congruence is

$$
X\longmapsto rXr=r^{2}X,
$$

a real dilation. A dilation preserves every real subspace, hence all six. The scale and the boost are not unitary; the scale is the only factor whose action is not an isometry of the interval. It preserves the subspaces because it does not mix the basis at all.

**The phase.** The phase is central and unitary, so its congruence is the identity. The action that sees the phase is left multiplication,

$$
X\longmapsto \exp(i\alpha)X.
$$

Multiplication by a complex scalar preserves the complex subspaces $\mathbb{C}_{\mathbb{B}}$ and $\mathrm{Vect}(\mathbb{B})$: a complex scalar times a complex scalar is a complex scalar, and a complex scalar times a complex vector is a complex vector. It does not preserve the real subspaces $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, because a real quaternion times $i$ is an imaginary quaternion, and it does not preserve $\mathbb{M}_+$ and $\mathbb{M}_-$, because a Hermitian element times $i$ is anti-Hermitian. The phase therefore sees the **complex structure** of the algebra: it preserves the two complex subspaces and rotates the real forms into each other.

**The boost.** The boost is Hermitian and of unit norm, but not unitary: $B^{2}\neq e_t$ for $\psi>0$. Its congruence is

$$
X\longmapsto B X B,
$$

and it preserves $\mathbb{M}_+$ and $\mathbb{M}_-$ because $B$ commutes with the Hermitian conjugation:

$$
(BXB)^{*}=B X^{*} B.
$$

It does not preserve $\mathbb{C}_{\mathbb{B}}$ or $\mathrm{Vect}(\mathbb{B})$, because $B$ has a scalar part and an imaginary vector part, and the product $BXB$ mixes the two. It does not preserve $\mathbb{H}_{\mathbb{B}}$ or $i\mathbb{H}_{\mathbb{B}}$ either, because the imaginary vector part of $B$ turns a real element into one with an imaginary part. The boost therefore sees the **material split** and nothing else.

**The rotor.** The rotor is a real unit quaternion. Its congruence is a conjugation by a real element,

$$
X\longmapsto \tilde q X\tilde q^{-1},
$$

which commutes with all three conjugations. A real quaternion conjugation is an automorphism of the algebra as a real algebra with the three involutions; it carries each eigenspace into itself. The rotor therefore preserves all six. It is the only non-central factor that does, and the reason is that it lives in the real quaternion subspace and acts by an automorphism.

The four mechanisms are the four ways a factor can act: a dilation, a complex multiplication, a Hermitian congruence and a real automorphism. The table is the list of their fixed subspaces.

## The Common Subspace

The subspaces preserved by all four factors are the intersection of the four rows. The scale and the rotor preserve all six; the phase preserves $\mathbb{C}_{\mathbb{B}}$ and $\mathrm{Vect}$; the boost preserves $\mathbb{M}_+$ and $\mathbb{M}_-$. The intersection is

$$
\mathbb{C}_{\mathbb{B}}\cap\mathrm{Vect}(\mathbb{B})\cap\mathbb{M}_+\cap\mathbb{M}_-
=0,
$$

because the centre and the vector space are complementary, and the two material sectors are complementary. The only subspace preserved by every factor is the zero subspace.

The result is not a defect. It says that the polar word is **irreducible** with respect to the six subspaces: no proper nonzero subspace is invariant under all four factors. The word is a product of four actions, each adapted to a different subspace, and the product is what makes the algebra's structure visible. A decomposition adapted to a single subspace would be a decomposition of a smaller algebra; the biquaternion polar word is adapted to the whole algebra.

The exception is the degenerate word. If $\alpha=0$ and $\psi=0$, the word is $r\tilde q$, and the phase and boost are trivial; the preserved set is all six. If only $\alpha=0$, the boost still preserves only $\mathbb{M}_\pm$. If only $\psi=0$, the phase still preserves only $\mathbb{C}_{\mathbb{B}}$ and $\mathrm{Vect}$. The generic word has the zero intersection; the degenerate words have larger ones.

## The Orbits of the Factors

Each factor has an orbit through the identity, and the orbits are the one-parameter subgroups of the factor.

**The scale** has the orbit $\{r e_t:r>0\}=\mathbb{R}_{>0}e_t$, a half-line in the centre. Its tangent at the identity is $e_t$, the dilation generator.

**The phase** has the orbit $\{\exp(i\alpha):\alpha\in\mathbb{R}\}=\mathrm{U}(1)$, the unit circle in the centre. Its tangent is $i$, the complex structure.

**The boost** has the orbit $\{B(\psi,\vec u_{\mathrm b})\}=\{\cosh\psi e_t-i\sinh\psi\vec u_{\mathrm b}\}$, a hyperbola in $\mathbb{M}_+$ for each axis. Its tangent at the identity is $i\vec u_{\mathrm b}$, the boost generator. The orbit is the set of four-velocities of unit norm, the hyperboloid $H^3$.

**The rotor** has the orbit $\{\tilde q(\theta,\vec u_{\mathrm r})\}=\{\cos(\theta/2)e_t+\sin(\theta/2)\vec u_{\mathrm r}\}$, the sphere $S^3=Sp(1)$ in $\mathbb{H}_{\mathbb{B}}$. Its tangent at the identity is $\vec u_{\mathrm r}$, the rotation generator.

The four orbits are the four model spaces of the factors: a line, a circle, a hyperbola and a sphere. The polar word is a point of the product of the four, and the product has dimension $1+1+3+3=8$. The dimension count is the real dimension of the algebra, and the four orbits are the four directions in which an element can move away from the identity.

## A Table of Examples

The following table applies each factor to a few elements and records the result. The examples are chosen to show the preservation and the failure of preservation.

| element | $r$ | $\exp(i\alpha)$ | $B$ | $\tilde q$ |
|---|---|---|---|---|
| $e_t$ | $r^{2}e_t$ | $e^{i\alpha}e_t$ | $B^{2}$ | $e_t$ |
| $i e_t$ | $ir^{2}e_t$ | $ie^{i\alpha}e_t$ | $iB^{2}$ | $i e_t$ |
| $\vec e_x$ | $r^{2}\vec e_x$ | $e^{i\alpha}\vec e_x$ | $B\vec e_x B$ | $\tilde q\vec e_x\tilde q^{-1}$ |
| $e_t+i\vec e_x$ | $r^{2}(e_t+i\vec e_x)$ | $e^{i\alpha}(e_t+i\vec e_x)$ | $B(e_t+i\vec e_x)B$ | $e_t+i\tilde q\vec e_x\tilde q^{-1}$ |
| $i e_t+\vec e_x$ | $r^{2}(i e_t+\vec e_x)$ | $ie^{i\alpha}(e_t-i\vec e_x)$ | $B(i e_t+\vec e_x)B$ | $i e_t+\tilde q\vec e_x\tilde q^{-1}$ |

The rows show the pattern. The scale multiplies every coefficient by $r^{2}$; the phase multiplies by $e^{i\alpha}$ and turns a real element into a complex one; the boost mixes the scalar and the parallel vector; the rotor rotates the vector part and leaves the scalar part.

**The boost on $\vec e_x$.** For a boost along $\vec e_x$,

$$
B\vec e_x B=+\sinh2\psi\,i e_t+\cosh2\psi\,\vec e_x.
$$

The result has an imaginary scalar part and a real vector part: it is in $\mathbb{M}_-$, not in $\mathrm{Vect}(\mathbb{B})$. The boost has carried a vector out of the vector space and into the anti-Hermitian sector. This is the concrete failure of the vector-space preservation.

**The phase on $\mathbb{M}_+$.** For $X=e_t+i\vec e_x$,

$$
\exp(i\alpha)X=e^{i\alpha}e_t+ie^{i\alpha}\vec e_x
=\cos\alpha\,e_t-\sin\alpha\,\vec e_x+i(\sin\alpha\,e_t+\cos\alpha\,\vec e_x).
$$

The result has a real and an imaginary part; it is neither Hermitian nor anti-Hermitian unless $\alpha=0$ or $\pi/2$. The phase has carried the Hermitian element out of $\mathbb{M}_+$ and into the whole algebra.

These two computations are the mechanism of the table. The abstract statement "the boost preserves $\mathbb{M}_\pm$" and "the phase preserves $\mathbb{C}_{\mathbb{B}}$ and $\mathrm{Vect}$" is the statement that the corresponding products do not produce the forbidden components; the examples show the products that do.

## The Element and the Factors

The table is about the factors, not about the element. The element $\tilde Q$ itself does not preserve the six subspaces; its left multiplication mixes them. The polar word separates the element into factors that are adapted to the subspaces one at a time.

The distinction is visible in the matrix picture. The matrix of $\tilde Q$ is a general element of $GL(2,\mathbb{C})$, and it has no nonzero invariant subspace of the six in general. The polar decomposition writes it as

$$
\mathsf M_2(\tilde Q)
=r\exp(i\alpha)\mathsf M_2(B)\mathsf M_2(\tilde q),
$$

and the three matrices on the right are a dilation, a positive Hermitian matrix and a unitary matrix. The positive Hermitian matrix preserves the two material sectors; the unitary matrix preserves the complex structure; the dilation preserves everything. The element is the product, and the product mixes what the factors preserve.

The physical reading is the same statement. A general Lorentz transformation is a boost and a rotation; the boost preserves the light cone and the two material sectors, the rotation preserves the spatial sphere and the quaternion subspaces, and the product is a general transformation that preserves neither separately. The polar word is the decomposition that makes the two preserving factors explicit.

## The Physical Reading of the Six

The six subspaces carry the six physical objects of the framework.

- **The centre $\mathbb{C}_{\mathbb{B}}$** is the complex time: the real part is the time coordinate and the imaginary part is the $ict$ of the material sector. The phase acts on it by multiplication, and the scale dilates it.
- **The vector space $\mathrm{Vect}(\mathbb{B})$** is the complex space: the three complex components of the vector part. The rotor acts on it by rotation, and the boost mixes it with the centre.
- **The quaternion subspace $\mathbb{H}_{\mathbb{B}}$** is the rotor space: the real quaternions, the home of the unit sphere $Sp(1)=SU(2)$. The rotor lives in it and acts on it by conjugation.
- **The anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$** is the imaginary quaternion space: the home of the imaginary vector part that the boost uses. The phase rotates it into the quaternion subspace.
- **The Hermitian subspace $\mathbb{M}_+$** is the four-velocity and field-strength sector: real scalar plus imaginary vector. The boost preserves it.
- **The anti-Hermitian subspace $\mathbb{M}_-$** is the four-position and four-momentum sector: imaginary scalar plus real vector. The boost preserves it.

The polar word is the unique decomposition that separates the four actions: the scale sees the norm, the phase sees the complex structure, the boost sees the material split, and the rotor sees the real quaternion structure. The table of preservation is the precise statement of which action sees which subspace, and the zero intersection is the statement that no single subspace is enough.

## Summary

The six remarkable subspaces are the centre, the vector space, the quaternion and anti-quaternion subspaces, and the Hermitian and anti-Hermitian subspaces. The polar factors preserve them as follows: the scale and the rotor preserve all six; the phase, under left multiplication, preserves the centre and the vector space; the boost preserves the two material sectors. The intersection of the preserved subspaces is zero, so the polar word is irreducible with respect to the six. The factor orbits are a line, a circle, a hyperbola and a sphere, of dimensions $1+1+3+3=8$. The element itself mixes the subspaces; the factors are the pieces that do not.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | the centre, complex scalars |
| $\mathrm{Vect}(\mathbb{B})$ | the vector space, complex vectors |
| $\mathbb{H}_{\mathbb{B}}$ | the real quaternion subspace |
| $i\mathbb{H}_{\mathbb{B}}$ | the imaginary quaternion subspace |
| $\mathbb{M}_+$ | the Hermitian subspace |
| $\mathbb{M}_-$ | the anti-Hermitian subspace |
| $\Theta_A(X)=AXA^{*}$ | the congruence |
| $r,\alpha,\psi,\theta$ | the scale, phase, frame rapidity and rotor angle |
| $B$ | the positive Hermitian boost factor |
| $\tilde q$ | the rotor |

## Further Reading

- *The Polar Element Representation of Biquaternions* (`articles_physics/the-polar-element-representation-of-biquaternions.md`), the word and the factors.
- *The Action of the Polar Element Representation on the Hermitian and Anti-Hermitian Subspaces* (`articles_physics/the-action-of-the-polar-element-representation-on-the-hermitian-and-anti-hermitian-subspaces.md`), the action formulas.
- *The Polar Element Representation in Subspaces* (`articles_physics/the-polar-element-representation-in-subspaces.md`), the restrictions to the subspaces.
- *Other Remarkable Subspaces* (`articles_physics/other-remarkable-subspaces.md`), the catalogue of the six.
- *Relations Between Subspaces* (`articles_physics/relations-between-subspaces.md`), the inclusions and the intersections.
- *The Cartan Hermitian Pairing of the Polar Element Representation of Biquaternions* (`articles_physics/the-cartan-hermitian-pairing-of-the-polar-element-representation-of-biquaternions.md`), the positive-unitary reading.
- *The Quaternion Pairing of the Polar Element Representation of Biquaternions* (`articles_physics/the-quaternion-pairing-of-the-polar-element-representation-of-biquaternions.md`), the real-quaternion reading.
