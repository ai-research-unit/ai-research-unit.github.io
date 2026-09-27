# __Biquaternion Lie Algebra and Lie Group Structure__

## Introduction

This article develops the Lie theory of the biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$. The basic algebra article defined $\mathbb{B}$ and its six distinguished subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$; the article on norm and invertibility identified the norm form $N(\tilde{Q})$ with the determinant; and the elementary-functions article computed the exponential, the logarithm and the power functions, with the group law and the kernel of the exponential. Here these are assembled into the standard theory of $\mathbb{B}^\times$ as a Lie group and of its Lie algebra. The closing sections complete the picture with the topology of the group of units: the polar decomposition, the retraction onto the maximal compact subgroup, and the resulting homotopy groups and universal cover.

One point governs everything below. The algebra $\mathbb{B}$ is simultaneously **eight-dimensional over $\mathbb{R}$** and **four-dimensional over $\mathbb{C}$**; each complex dimension counts two real dimensions. Every dimension statement therefore names the field concerned.

Throughout, a biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + \mathbf{Q}, \qquad \mathbf{Q} = \sum_{k=1}^{3} Q_k e_k, \qquad Q_\mu \in \mathbb{C}.
$$

The quaternion units satisfy $e_0 = 1$ and $e_k^2 = -e_0$; the scalar imaginary $i$ satisfies $i^2 = -1$ and commutes with every $e_k$. The quaternion conjugate is $\bar{\tilde{Q}} = Q_0 e_0 - \mathbf{Q}$, and the norm form is

$$
N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2.
$$

For a biquaternion with nonzero vector part we write $B = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}$ for the complex norm of the vector part and $\hat{n} = \mathbf{Q}/B$, so that $\hat{n}^2 = -e_0$ and $\mathbf{Q} = B\hat{n}$.

---

## The Algebra as a Lie Algebra

The trace functional and the norm form are

$$
\mathrm{Tr}(\tilde{Q}) = 2Q_0, \qquad N(\tilde{Q}) = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 .
$$

**Dimension.** As a complex vector space, $\mathbb{B} \cong \mathbb{C}^4$ has complex dimension $4$; as a real vector space it has real dimension $8$. The trace-free part has complex dimension $3$ and real dimension $6$.

The set $\mathbb{B}$ carries the **commutator bracket**

$$
[\tilde{P}, \tilde{Q}] = \tilde{P}\tilde{Q} - \tilde{Q}\tilde{P},
$$

under which it is a complex Lie algebra, written $\mathfrak{g}$, of dimension $4$ over $\mathbb{C}$ and $8$ over $\mathbb{R}$. Its center is the scalar line

$$
\mathfrak{z}(\mathfrak{g}) = \mathbb{C}e_0,
$$

of complex dimension $1$ and real dimension $2$; every scalar multiple of $e_0$ commutes with all of $\mathbb{B}$. Removing the center gives the decomposition

$$
\mathfrak{g} = \mathfrak{B}_0 \oplus \mathbb{C}e_0,
$$

with complex dimensions $4 = 3 + 1$ and real dimensions $8 = 6 + 2$, where

$$
\mathfrak{B}_0 = \{\tilde{Q} \in \mathbb{B} : Q_0 = 0\} = \mathrm{span}_\mathbb{C}\{e_1, e_2, e_3\}
$$

is the **trace-free subalgebra**, the complex pure-vector part.

## The Group of Units

The **group of units** of $\mathbb{B}$ is the set of invertible elements,

$$
\mathbb{B}^\times = \{\tilde{Q} \in \mathbb{B} : N(\tilde{Q}) \neq 0\},
$$

a group under multiplication with identity $e_0$.

**Dimension.** $\mathbb{B}^\times$ has complex dimension $4$ and real dimension $8$; the units are exactly the elements of nonzero norm.

The group $\mathbb{B}^\times$ is open (it is $N^{-1}(\mathbb{C}\setminus\{0\})$) and dense, its complement being the null cone, of real dimension $6$ (*Biquaternion Topology*); it is connected but not compact, and its center is $Z(\mathbb{B}^\times) = \mathbb{C}^\times e_0 \cong \mathbb{C}^\times$, a real Lie group of dimension $2$. Its Lie algebra is $\mathbb{B}$ itself with the commutator bracket, i.e. $\mathfrak{g}$: the tangent space at the identity is the whole algebra because the units are open. The inverse map has differential $-\mathrm{id}$ at the identity, the infinitesimal reason the bracket is antisymmetric.

**The norm-one group.** Because $N$ is multiplicative and $N(e_0)=1$, the level set

$$
\mathbb{B}^\times_1=\{\tilde{Q}\in\mathbb{B}:N(\tilde{Q})=1\}
$$

is a closed subgroup of $\mathbb{B}^\times$ of real dimension $6$, the **norm-one group**. It is noncompact, and it deformation retracts onto the unit quaternions $S^3$ (§*The Retraction of the Norm-One Group onto Its Maximal Compact Subgroup*); hence it is simply connected, of the homotopy type of $S^3$, with $\pi_3\cong\mathbb{Z}$. Its own subgroups — the rotation subgroup $S^3$, the center $\{\pm e_0\}$, and the Lorentz group $\mathbb{B}^\times_1/\{\pm e_0\}$ — are the subject of §*Subgroups and the Lorentz Group*.

**Two unit spheres.** There are two candidate "unit spheres" in $\mathbb{B}$, and only one of them is a group. The Euclidean sphere $\|\tilde{Q}\|_E=1$ is a genuine sphere $S^7$ but is not a group, since $\|\cdot\|_E$ is not multiplicative and it contains zero divisors (*Biquaternion Topology*, §*The Euclidean unit sphere*). The level set $N(\tilde{Q})=1$ is a group but is neither Euclidean nor compact. The condition that makes a level set of a form on $\mathbb{B}$ a subgroup is $N=1$, not $\|\tilde{Q}\|_E=1$.

## The Unit Quaternions and Their Complexification

The **unit quaternions** are the elements of $\mathbb{H}_{\mathbb{B}}$ of norm form $1$:

$$
S^3 = \{q \in \mathbb{H}_{\mathbb{B}} : N(q) = 1\},
$$

a compact, connected, simply connected real Lie group of real dimension $3$. Every such $q$ is $\cos\theta\, e_0 + \sin\theta\, \hat{n}$ with $\hat{n}$ a real unit vector part, the quaternion exponential.

Complexifying the coefficients turns $N(q) = 1$ into the same equation over $\mathbb{C}$, giving the **unit-norm-form subgroup**

$$
\mathbb{B}^\times_1 = \{\tilde{Q} \in \mathbb{B} : N(\tilde{Q}) = 1\},
$$

whose elements need not be real quaternions.

**Dimension.** The level set $N = 1$ has complex dimension $3$ and real dimension $6$, the norm form being a submersion wherever $N(\tilde{Q}) \neq 0$. The group $\mathbb{B}^\times_1$ is connected, simply connected, and non-compact, and it is the **complexification of the unit quaternions**: the trace-free subalgebra satisfies $\mathfrak{B}_0 = \mathfrak{k} \otimes_{\mathbb{R}} \mathbb{C}$ for the compact rotation subalgebra $\mathfrak{k}$ below, and $\mathbb{B}^\times_1$ complexifies the compact group $S^3$. Its center is

$$
Z(\mathbb{B}^\times_1) = \{\pm e_0\} \cong \mathbb{Z}/2.
$$

## The Trace-Free Subalgebra: Rotations and Hyperbolic Rotations

The Lie algebra of $\mathbb{B}^\times_1$ is the trace-free subalgebra

$$
\mathfrak{B}_0 = \{\tilde{Q} \in \mathbb{B} : Q_0 = 0\} = \mathrm{span}_\mathbb{C}\{e_1, e_2, e_3\},
$$

of complex dimension $3$ and real dimension $6$, closed under the bracket $[e_j,e_k] = 2\sum_l \epsilon_{jkl} e_l$. Over the reals it splits into two three-dimensional real subspaces,

$$
\mathfrak{B}_0 = \mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\} \;\oplus\; \mathrm{span}_\mathbb{R}\{ie_1, ie_2, ie_3\},
$$

with real dimensions $6 = 3 + 3$. The first summand is the compact rotation subalgebra

$$
\mathfrak{k} = \mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\},
$$

the Lie algebra of spatial rotations, on which the bracket is (twice) the cross product; the second, $\mathrm{span}_\mathbb{R}\{ie_1,ie_2,ie_3\}$, consists of the generators of the hyperbolic rotations. The two are non-isomorphic real Lie algebras: one compact, one not.

In the fixed-point subspaces of the basic algebra article the rotation directions are $e_k \in \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$ and the hyperbolic-rotation directions are $ie_k \in \mathbb{M}_+$. This is why pure spatial rotations have rotors in $\mathbb{H}_{\mathbb{B}}$ while pure hyperbolic rotations have rotors in $\mathbb{M}_+$: these are exactly the two real three-dimensional pieces into which $\mathfrak{B}_0$ splits. The central direction $\mathbb{C}e_0$ completes the picture, $\mathfrak{g} = \mathfrak{B}_0 \oplus \mathbb{C}e_0$.

## Subgroups and the Lorentz Group

The relevant subgroups are: $\mathbb{B}^\times$, the nonzero-norm elements (complex dimension $4$, real dimension $8$); $\mathbb{B}^\times_1$, the unit-norm elements (complex dimension $3$, real dimension $6$); the rotation group $S^3$, the unit-norm real quaternions (real dimension $3$); and the center $\mathbb{C}^\times e_0$ of nonzero scalars (complex dimension $1$, real dimension $2$).

$S^3$ is the maximal compact subgroup of $\mathbb{B}^\times_1$, with Lie algebra the compact rotation subalgebra $\mathfrak{k}$ of §*The Trace-Free Subalgebra: Rotations and Hyperbolic Rotations*. The center $\{\pm e_0\}$ is discrete, and

$$
\mathbb{B}^\times_1/\{\pm e_0\} \cong SO^+(1,3),
$$

the proper orthochronous Lorentz group, of real dimension $6$. Hence $\mathbb{B}^\times_1$ is a two-sheeted cover of $SO^+(1,3)$ and, being simply connected, is its universal cover: it is the spin group of Lorentzian signature,

$$
\mathbb{B}^\times_1 \cong \mathrm{Spin}(1,3), \qquad \mathfrak{B}_0 \cong \mathfrak{so}(1,3).
$$

The Lorentz action is rotor conjugation, $\tilde{Q} \mapsto \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^\dagger$ for $\tilde{\Lambda} \in \mathbb{B}^\times_1$, which preserves $\mathbb{M}_-$ and $N(\tilde{Q})$; its compact part is the rotation family and its non-compact part the hyperbolic rotations, with closed forms in *Biquaternion Elementary Functions*, §*The Exponential of a Rotation and of a Hyperbolic Rotation*.

## Surjectivity and Its Failure for the Subgroups

The exponential of the full unit group is surjective (*Biquaternion Elementary Functions*, §*The Logarithm*), but the two distinguished subgroups behave differently.

**Rotations: surjective.** Every unit quaternion is $\cos\theta\, e_0 + \sin\theta\,\hat{n} = \exp(\theta\hat{n})$, so $\exp : \mathfrak{k} \to S^3$ is surjective; this is the general fact that a connected compact Lie group has a surjective exponential map.

**Lorentz group: not surjective.** The exponential $\exp : \mathfrak{B}_0 \to \mathbb{B}^\times_1$ is **not** surjective: $\mathbb{B}^\times_1$ is not exponential. The element of $\mathbb{B}^\times_1$ with scalar part $-1$ and non-semi-simple behaviour, corresponding to the non-diagonalizable norm-one element with the repeated eigenvalue $-1$, is

$$
\tilde{Q} = -e_0 + \frac{i}{2}e_1 - \frac{1}{2}e_2, \qquad N(\tilde{Q}) = 1 + \left(\frac{i}{2}\right)^2 + \left(-\frac{1}{2}\right)^2 = 1.
$$

Its scalar part is $Q_0 = -1$ and its vector part has $B = 0$, so the element is non-semi-simple with the repeated eigenvalue $-1$. If $\tilde{Q} = \exp(\tilde{R})$ with $\tilde{R} \in \mathfrak{B}_0$, then $R_0 = 0$, and $\tilde{R} = \mu e_0 + \tilde{N}$ with $\tilde{N}$ nilpotent and $e^\mu = -1$, hence $\mu \in i\pi(2\mathbb{Z}+1)$ and $\mathrm{Tr}(\tilde{R}) = 2\mu \neq 0$, a contradiction. The same obstruction makes $\exp$ non-surjective on the real group $SL(2,\mathbb{R})$.

**Generation versus surjectivity.** Failure of surjectivity does not mean the exponentials fail to generate: since $\mathbb{B}^\times_1$ is connected and $\exp$ is a local diffeomorphism at $0$, the image $\exp(\mathfrak{B}_0)$ contains a neighbourhood of the identity and generates the group, while remaining a proper subset. Nor does simple connectivity force surjectivity: $\mathbb{B}^\times_1$ is simply connected, yet $\exp$ is not onto. The classical criteria (connected compact, connected nilpotent, or $GL(n,\mathbb{C})$) are sufficient, not necessary.

---

The group of units is an open subset of $\mathbb{B}$, hence a smooth real manifold of dimension $8$, but its topology is far from that of a general open set in $\mathbb{R}^8$: it has the homotopy type of a compact group. The polar decomposition exhibits the maximal compact subgroup as a strong deformation retract, and with it determines the homotopy groups and the universal cover. Everything in this part is a statement about $\mathbb{B}^\times$ as a topological group; the topology of the ambient space and of the null cone is in *Biquaternion Topology*.

## The Retraction of $\mathbb{B}^\times$ onto Its Maximal Compact Subgroup

Every $\tilde{A} \in \mathbb{B}^\times$ has a unique polar decomposition $\tilde{A} = \tilde{U}\tilde{P}$, where $\tilde{U}$ is unitary ($\tilde{U}^\dagger\tilde{U} = e_0$) and $\tilde{P} = (\tilde{A}^\dagger\tilde{A})^{1/2}$ is Hermitian positive definite. For $t\in[0,1]$ put $\tilde{P}_t=(1-t)\tilde{P}+t e_0$ and

$$
\tilde{H}(t,\tilde{A})=\tilde{U}\tilde{P}_t.
$$

The eigenvalues of $\tilde{P}_t$ are $(1-t)\lambda+t$ with $\lambda>0$, hence positive, so $\tilde{P}_t$ is positive definite and $\tilde{H}(t,\tilde{A})\in \mathbb{B}^\times$; the map $\tilde{H}$ is continuous because the positive-definite square root depends continuously on $\tilde{A}$. Moreover

$$
\tilde{H}(0,\tilde{A})=\tilde{A},\qquad \tilde{H}(1,\tilde{A})=\tilde{U},\qquad \tilde{H}(t,\tilde{U})=\tilde{U}\ \text{ for unitary } \tilde{U}.
$$

So the unitary biquaternions form a strong deformation retract of $\mathbb{B}^\times$, and the two are homotopy equivalent, whence $\pi_n(\mathbb{B}^\times)\cong\pi_n(\mathrm{U}(\mathbb{B}))$ for all $n$, writing $\mathrm{U}(\mathbb{B})$ for the group of unitary biquaternions. Every $\tilde{A}$ is joined to a unitary element, and $\mathrm{U}(\mathbb{B})$ is connected (§*The Structure of the Maximal Compact Subgroup*), so $\mathbb{B}^\times$ is connected, in agreement with *Biquaternion Norm and Invertibility*. (The statement that there are two components distinguished by the sign of the determinant concerns the real algebra, not the complex one.) The retraction takes $\mathbb{B}^\times$ onto its maximal compact subgroup, the **unitary biquaternions**

$$
\mathrm{U}(\mathbb{B}) = \{\tilde{Q}\in\mathbb{B}:\tilde{Q}^\dagger\tilde{Q}=e_0\}.
$$

## The Retraction of the Norm-One Group onto Its Maximal Compact Subgroup

Let $\tilde{A}\in \mathbb{B}^\times_1$ have polar decomposition $\tilde{A}=\tilde{U}\tilde{P}$. Then $1=N(\tilde{A})=N(\tilde{U})N(\tilde{P})$, with $N(\tilde{U})$ of modulus $1$ and $N(\tilde{P})$ a positive real, so $N(\tilde{U})=N(\tilde{P})=1$, that is $\tilde{U}$ lies in $S^3$. For $t\in[0,1]$ define

$$
\tilde{P}_t=\frac{(1-t)\tilde{P}+t e_0}{N\big((1-t)\tilde{P}+t e_0\big)^{1/2}}.
$$

The denominator is a positive real number, so $\tilde{P}_t$ is Hermitian positive definite of norm $1$. The map $\tilde{H}(t,\tilde{A})=\tilde{U}\tilde{P}_t$ is continuous, lies in $\mathbb{B}^\times_1$ since $N(\tilde{U}\tilde{P}_t)=1$, and satisfies $\tilde{H}(0,\tilde{A})=\tilde{A}$, $\tilde{H}(1,\tilde{A})=\tilde{U}\in S^3$, and $\tilde{H}(t,\tilde{U})=\tilde{U}$ for unitary $\tilde{U}$. Hence $S^3$ is a strong deformation retract of $\mathbb{B}^\times_1$.

Thus $\mathbb{B}^\times_1\simeq S^3$: it is connected and simply connected with $\pi_3\cong\mathbb{Z}$ and the homotopy type of $S^3$, but is not homeomorphic to $S^3$, being a noncompact real $6$-manifold. The norm-one group $\mathbb{B}^\times_1$ of §*The Group of Units* is therefore simply connected, of homotopy type $S^3$.

## The Structure of the Maximal Compact Subgroup

The unit quaternions form $S^3$; $S^3$ is compact, connected and simply connected, the double cover of the rotation group $SO(3)$.

Every unitary biquaternion $\tilde{U}$ is a scalar multiple of a unit quaternion: if $N(\tilde{U})=z\in S^1$ and $\zeta^2=z$, then $\tilde{A}=\zeta^{-1}\tilde{U}$ has $N(\tilde{A})=1$ and $\tilde{U}=\zeta\tilde{A}$. Hence

$$
\mathrm{U}(\mathbb{B})=S^1\cdot S^3,\qquad S^1\cap S^3=\{\pm e_0\},
$$

and the multiplication map $S^1\times S^3\to \mathrm{U}(\mathbb{B})$ is a surjective homomorphism with kernel $\{(e_0,e_0),(-e_0,-e_0)\}\cong\mathbb{Z}/2$, so by the first isomorphism theorem for Lie groups

$$
\mathrm{U}(\mathbb{B})\cong(S^1\times S^3)/\{\pm e_0\},
$$

with $\{\pm e_0\}$ acting diagonally. The norm form $N:\mathrm{U}(\mathbb{B})\to S^1$ is a principal $S^3$-bundle, each fibre being a coset of $S^3$, and it admits a section, so

$$
\mathrm{U}(\mathbb{B})\cong S^1\times S^3
$$

as spaces. This is a homeomorphism, not an isomorphism of Lie groups: the map above is two-to-one, while the centre of $\mathrm{U}(\mathbb{B})$ is connected but that of $S^1\times S^3$ is not.

The central scalars form a maximal torus $T^2\cong S^1\times S^1\subset \mathrm{U}(\mathbb{B})$. It is **not** true that $\mathrm{U}(\mathbb{B})$ deformation retracts onto $T^2$: that would give $\pi_1(\mathrm{U}(\mathbb{B}))\cong\pi_1(T^2)$, but these are $\mathbb{Z}$ and $\mathbb{Z}^2$. Every element of $\mathrm{U}(\mathbb{B})$ does lie in some maximal torus, and the quotient is the complete flag variety

$$
\mathrm{U}(\mathbb{B})/T^2\cong P^1\cong S^2,
$$

so $\mathrm{U}(\mathbb{B})$ is a fibre bundle over $S^2$ with fibre $T^2$; and $\mathrm{U}(\mathbb{B})$ is not homotopy equivalent to $T^2$, being homeomorphic to $S^1\times S^3$.

## Homotopy Groups and Generators

The retractions give $S^3$ for the unit quaternions, $\mathrm{U}(\mathbb{B})\cong S^1\times S^3$, $\mathbb{B}^\times_1\simeq S^3$, and $\mathbb{B}^\times\simeq \mathrm{U}(\mathbb{B})\simeq S^1\times S^3$. Hence

$$
\pi_1(S^3)=\pi_2(S^3)=0,\qquad\pi_3(S^3)\cong\mathbb{Z},
$$

$$
\pi_1(\mathrm{U}(\mathbb{B}))\cong\mathbb{Z},\qquad\pi_2(\mathrm{U}(\mathbb{B}))=0,\qquad\pi_3(\mathrm{U}(\mathbb{B}))\cong\mathbb{Z},
$$

and likewise $\pi_1(\mathbb{B}^\times_1)=0$, $\pi_1(\mathbb{B}^\times)\cong\mathbb{Z}$, with $\pi_2=0$ and $\pi_3\cong\mathbb{Z}$ for both.

**Generators.** The group $\pi_3(S^3)\cong\mathbb{Z}$ is generated by the class $[\operatorname{id}_{S^3}]$ of the identity map under $S^3=\{\text{unit quaternions}\}$, and $\pi_3(\mathrm{U}(\mathbb{B}))\cong\mathbb{Z}$ by the image of that class under the inclusion $S^3\hookrightarrow \mathrm{U}(\mathbb{B})$, which induces an isomorphism on $\pi_3$. The group $\pi_1(\mathrm{U}(\mathbb{B}))\cong\mathbb{Z}$ is generated by the central loop $\gamma(t)=e^{2\pi i t}e_0$, $t\in[0,1]$, and $N_*:\pi_1(\mathrm{U}(\mathbb{B}))\to\pi_1(S^1)\cong\mathbb{Z}$ is an isomorphism, so a generator is a loop whose norm winds once. The universal covers are

$$
\widetilde{\mathrm{U}(\mathbb{B})}\cong\widetilde{\mathbb{B}^\times}\cong\mathbb{R}\times S^3,
$$

while $S^3$ and $\mathbb{B}^\times_1$ are their own universal covers. By Hurewicz, $H_1(\mathrm{U}(\mathbb{B}))\cong H_1(\mathbb{B}^\times)\cong\mathbb{Z}$ and $H_1(S^3)=H_1(\mathbb{B}^\times_1)=0$; and $\pi_n(\mathrm{U}(\mathbb{B}))\cong\pi_n(S^3)$ for $n\geq2$.

## Summary

The algebra $\mathbb{B}$ is simultaneously eight-dimensional over $\mathbb{R}$ and four-dimensional over $\mathbb{C}$, and every dimension statement names its field. As a complex Lie algebra it is $\mathfrak{g}$ with the commutator bracket, the Lie algebra of the group of units $\mathbb{B}^{\times}$; the exponential map, its closed form, its group law, its kernel and the logarithm belong to *Biquaternion Elementary Functions*, and only their group-theoretic consequences are used here.

The trace-free subalgebra $\mathfrak{B}_0 = \mathrm{span}_{\mathbb{C}}\{e_1,e_2,e_3\}$ has complex dimension $3$ and real dimension $6$, splitting over $\mathbb{R}$ into the compact rotation subalgebra $\mathfrak{k} = \mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ of the rotations and the non-compact $\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$ of the hyperbolic rotations; these sit in $\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$ and in $\mathbb{M}_+$ respectively, and the central direction completes $\mathfrak{g} = \mathfrak{B}_0 \oplus \mathbb{C}e_0$.

The subgroups are the units, the unit-norm elements $\mathbb{B}^\times_1$, the rotation group $S^3$ (the maximal compact subgroup, the unit-norm real quaternions), and the center $\mathbb{C}^{\times}e_0$. Since $\mathbb{B}^\times_1/\{\pm e_0\} \cong SO^{+}(1,3)$, the unit-norm group is the spin group $\mathrm{Spin}(1,3)$ and the universal cover of the proper orthochronous Lorentz group, acting by rotor conjugation $\tilde{Q} \mapsto \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{\dagger}$, which preserves $\mathbb{M}_-$ and the norm form.

The group of units has the homotopy type of its maximal compact subgroup: $\mathrm{U}(\mathbb{B})\cong S^1\times S^3$ is a strong deformation retract of $\mathbb{B}^\times$, and $S^3$ is a strong deformation retract of $\mathbb{B}^\times_1$. Hence $\mathbb{B}^\times\simeq S^1\times S^3$ and $\mathbb{B}^\times_1\simeq S^3$, so
$$
\pi_1(\mathbb{B}^\times)\cong\mathbb{Z},\qquad \pi_2(\mathbb{B}^\times)=0,\qquad \pi_3(\mathbb{B}^\times)\cong\mathbb{Z},
$$
with universal cover $\widetilde{\mathbb{B}^\times}\cong\mathbb{R}\times S^3$, while $\mathbb{B}^\times_1$ and $S^3$ are their own universal covers.

Surjectivity of the exponential is not uniform over these groups. It is surjective onto $S^3$, a connected compact group, but it is **not** surjective onto $\mathbb{B}^\times_1$: the Lorentz group is not exponential, the obstruction being a non-semi-simple element with the repeated eigenvalue $-1$, and the same obstruction applies to $SL(2,\mathbb{R})$. Failure of surjectivity does not prevent generation — the image contains a neighbourhood of the identity and generates the connected group — and simple connectivity does not force surjectivity, since $\mathbb{B}^\times_1$ is simply connected while $\exp$ is not onto.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | Biquaternion algebra; a complex Lie algebra under the commutator |
| $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$ | Biquaternion; $\mathbf{Q} = \sum_k Q_k e_k$ |
| $B = \sqrt{Q_1^2+Q_2^2+Q_3^2}$, $\hat{n} = \mathbf{Q}/B$ | Complex norm and axis of the vector part, $\hat{n}^2 = -e_0$ |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form; $\tilde{Q}$ is a unit iff $N(\tilde{Q}) \neq 0$ |
| $\mathbb{B}^{\times}$ | Group of units; complex dimension $4$, real dimension $8$ |
| $\mathbb{B}^{\times}_1 = \{N = 1\}$ | Norm-one group; closed subgroup of real dimension $6$ |
| $\mathrm{U}(\mathbb{B}) = \{\tilde{Q}^\dagger\tilde{Q}=e_0\}$ | Unitary biquaternions; maximal compact subgroup of $\mathbb{B}^{\times}$ |
| $\mathbb{B}^{\times} \simeq \mathrm{U}(\mathbb{B}) \simeq S^1 \times S^3$ | Homotopy type of the group of units; $\pi_1 \cong \mathbb{Z}$, $\pi_2 = 0$, $\pi_3 \cong \mathbb{Z}$ |
| $S^3 = \{q \in \mathbb{H}_{\mathbb{B}} : N(q) = 1\}$ | Unit quaternions; maximal compact subgroup of $\mathbb{B}^{\times}_1$, real dimension $3$ |
| $\mathbb{C}^{\times}e_0$ | Center of the group of units; nonzero complex scalars |
| $\mathfrak{g} = \mathbb{B}$ (commutator) | Lie algebra of the group of units; complex dimension $4$ |
| $\mathfrak{B}_0 = \{Q_0 = 0\} = \mathrm{span}_{\mathbb{C}}\{e_1,e_2,e_3\}$ | Trace-free subalgebra, complex pure-vector part |
| $\mathfrak{k} = \mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ | Compact rotation subalgebra |
| $\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$ | Non-compact part of $\mathfrak{B}_0$, the hyperbolic-rotation directions |
| $\exp$ | Exponential map of $\mathbb{B}^{\times}$ and of its subgroups; closed form in *Biquaternion Elementary Functions* |
| $\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{\dagger}$ | Lorentz action by rotor conjugation |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, 2nd ed. 2015), for the exponential map, its surjectivity on $GL(n,\mathbb{C})$, and the matrix logarithm.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for an elementary treatment of the unit quaternions $S^3$ and the double cover of the rotation group.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the exponential, polar forms, and norms of biquaternions.
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the biquaternion exponential and polar forms.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras and the spin groups.
