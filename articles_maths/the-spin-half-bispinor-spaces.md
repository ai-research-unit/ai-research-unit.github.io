# __Introduction to the Spin-Half Bispinors Spaces__

## Introduction

The carrier of spin $\tfrac12$ is a plane, of real dimension $2$, and its closure is not one subspace but a family. This article introduces that family: the plane, the two spinor spaces that contain it, and the bispinor spaces that are their sums.

The family is infinite, and this is the point of the article. There is a plane for every unit real axis, two spinor spaces for every axis, and one bispinor space for every axis up to a sign, so the algebra carries infinitely many spaces of each kind. Nothing singles one of them out. The situation is the one known from the Peirce basis: a basis is a choice, and the algebra has as many bases as it has axes.

**Where the label comes from.** The label $\tfrac12$ is the label of the slot that the Clebsch–Gordan series squares: $\mathbb{B}\cong S\otimes S^{*}$ with $S=V_{1/2}$, and $V_{1/2}\otimes V_{1/2}=V_1\oplus V_0$. The slot is a factor and not a summand, so it is not the image of a projector of the algebra. It is realized by a minimal left ideal, and a minimal left ideal needs an idempotent and an axis. That is why this carrier is a family where the two integer carriers are single subspaces: the axis is the price of realizing a factor inside the algebra, and no projector can pay it.

**The question in one line.** Which real subspaces of $\mathbb{B}$ of dimension $2$, $4$ and $8$ carry the action with weights $\pm\tfrac12$.

**The answer in one line.** The plane $\Sigma(\vec u_{\mathrm r})=\mathbb{C}\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})$, the spinor spaces $S_\pm(\vec u_{\mathrm r})=\mathbb{B}\tilde\Pi_{\mathrm{id},\pm}(\vec u_{\mathrm r})$, and their sum, a bispinor space, which as a set is $\mathbb{B}$.

Nothing below is a statement of physics. The elements are written $X,Y$; the units are $e_t,\vec e_x,\vec e_y,\vec e_z$ with $e_t$ the identity and $\vec e_k^{2}=-e_t$; $*$ is the Hermitian conjugation and ${}^{\natural}$ the natural conjugation; $G=\mathrm{U}(2)$ is the group of unitary elements; and $\vec u_{\mathrm r}$ is a unit real axis, with $\vec u_2,\vec u_3$ an oriented orthonormal pair completing it.

## The Plane

**The idempotent.** For a unit real axis,

$$
\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})=\tfrac12\bigl(e_t+i\vec u_{\mathrm r}\bigr),
\qquad
\tilde\Pi_{\mathrm{id},+}^2=\tilde\Pi_{\mathrm{id},+} .
$$

The element is idempotent because $\vec u_{\mathrm r}^2=-e_t$: the square is $\tfrac14(e_t+2i\vec u_{\mathrm r}-\vec u_{\mathrm r}^2)=\tfrac14(2e_t+2i\vec u_{\mathrm r})=\tilde\Pi_{\mathrm{id},+}$. The verification is one line and needs no array.

**The plane.** The carrier is the complex line spanned by the idempotent, read as a real plane:

$$
\Sigma(\vec u_{\mathrm r})=\mathbb{C}\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})=\mathbb{R}\bigl\{\tilde\Pi_{\mathrm{id},+},\ i\tilde\Pi_{\mathrm{id},+}\bigr\},
$$

of real dimension $2$ and complex dimension $1$.

**The action.** Left multiplication. To an element $X$ of the algebra attach the operator $\varrho_{\mathrm{def}}(X)=L_X$, with $L_X(Y)=XY$. The action is one-sided, and this is what separates the carrier from the other two: the line and the vector part are acted on by a two-sided map, and the plane by a one-sided one.

**The half angle.** The key identity is

$$
\vec u_{\mathrm r}\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})=\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})\vec u_{\mathrm r}=-i\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r}),
$$

which follows in one line from the definition, since $\vec u_{\mathrm r}\tilde\Pi_{\mathrm{id},+}=\tfrac12(\vec u_{\mathrm r}+i\vec u_{\mathrm r}^2)=\tfrac12(\vec u_{\mathrm r}-ie_t)=-i\tilde\Pi_{\mathrm{id},+}$. Then for a rotor of angle $\theta$ about the same axis,

$$
\tilde u_{\mathrm r}\tilde\Pi_{\mathrm{id},+}=\bigl(\cos\tfrac{\theta}{2}-i\sin\tfrac{\theta}{2}\bigr)\tilde\Pi_{\mathrm{id},+}=e^{-i\theta/2}\,\tilde\Pi_{\mathrm{id},+} .
$$

The rotor multiplies the plane by the phase $e^{-i\theta/2}$. The half angle is a consequence of the identity, not an insertion.

**The weights.** The generator along the axis is $A(\vec u_{\mathrm r})=\tfrac12\vec u_{\mathrm r}$, and by the identity above it acts on the plane as the complex scalar $-\tfrac i2$. On the two real dimensions the eigenvalues are the scalar and its conjugate, so the spectrum is

$$
\{+\tfrac12,-\tfrac12\},
$$

and the spin is the largest weight, $s=\tfrac12$. The identity reads $2s+1=2=\dim_\mathbb{R}\Sigma$.

**The full turn.** At $\theta=2\pi$ the phase is $e^{-i\pi}=-1$, so the operator of a full turn is $-\mathrm{id}$ on the plane. The sign is $(-1)^{2s}=-1$, and here it is visible as a half turn of a real plane: a full rotation of space turns the plane by half a turn.

## The Plane Is Not a Carrier for the Whole Group

**The failure.** The plane is invariant under the rotations about its own axis and under no others. Left multiplication by the transverse axis sends $\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})$ out of the plane:

$$
\vec u_2\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})\notin\Sigma(\vec u_{\mathrm r}).
$$

The product has a component along $\vec u_3\tilde\Pi_{\mathrm{id},+}$, and that component is not a complex multiple of the idempotent.

**What this means.** Read strictly, the plane is a carrier for the circle of rotations about its axis, and not for the group. The defect is repaired by the closure, and the repair is the content of the next two sections. This is the one place among the three carriers where the carrier and the group do not match, and it is why the spin-half case has two closures while the other two have one.

## The First Closure: The Spinor Spaces

**The step.** The smallest real subspace containing the plane and invariant under the whole group is

$$
S_+(\vec u_{\mathrm r})=\mathbb{B}\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})
=\mathbb{C}\bigl\{\tilde\Pi_{\mathrm{id},+},\ \vec u_2\tilde\Pi_{\mathrm{id},+}\bigr\},
$$

of real dimension $4$ and complex dimension $2$. The plane is one complex line of the ideal; the transverse direction gives the second, and the two together are the ideal.

**What the step adds.** The step does not add the complex structure: the plane is a complex line already, and multiplication by $i$ acts inside it. The step adds the transverse direction, which is two real dimensions. The statement is worth the care, because the natural guess is the wrong one.

**The minimality.** $S_+$ is a minimal left ideal: no nonzero left subspace of it is invariant under left multiplication by the whole algebra. The dimension $4$ over $\mathbb{R}$ and $2$ over $\mathbb{C}$ is the smallest that supports the action, and the plane sits inside it as one of its two complex lines.

**The second spinor space.** The complementary idempotent

$$
\tilde\Pi_{\mathrm{id},-}(\vec u_{\mathrm r})=\tfrac12\bigl(e_t-i\vec u_{\mathrm r}\bigr)=e_t-\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})
$$

gives a second left ideal $S_-(\vec u_{\mathrm r})=\mathbb{B}\tilde\Pi_{\mathrm{id},-}(\vec u_{\mathrm r})$, also of real dimension $4$. The two idempotents satisfy $\tilde\Pi_{\mathrm{id},+}\tilde\Pi_{\mathrm{id},-}=0$, so the sum is direct:

$$
S_+(\vec u_{\mathrm r})\cap S_-(\vec u_{\mathrm r})=\{0\},
\qquad
\mathbb{B}=S_+(\vec u_{\mathrm r})\oplus S_-(\vec u_{\mathrm r}).
$$

Both spaces carry the same weights, $\pm\tfrac12$, and the same spin.

## The Second Closure: The Bispinor Spaces

**The space.** The sum of the two spinor spaces is a **bispinor space**, and it is the whole algebra. A bispinor space is therefore the algebra together with a Peirce basis: the pair of idempotents and the two spinor spaces they cut out.

**The two closures are two steps.** The first step goes from the plane, of real dimension $2$, to a spinor space, of real dimension $4$, and it adds the transverse direction. The second goes from the spinor space to the bispinor space, of real dimension $8$, and it adds the second idempotent. The two steps are different in kind and the article keeps them apart: the first repairs an invariance, the second completes a pair.

**Why the plural.** There is one bispinor space per Peirce basis, and there is one Peirce basis per unit real axis. Two axes that differ by a sign give the same unordered pair, since

$$
\tilde\Pi_{\mathrm{id},+}\bigl(-\vec u_{\mathrm r}\bigr)=\tilde\Pi_{\mathrm{id},-}\bigl(\vec u_{\mathrm r}\bigr),
$$

so the family is indexed by the real projective plane and it is infinite.

**As sets they coincide.** Each bispinor space is $\mathbb{B}$, so as sets the family has one member. What varies is the splitting: the pairs of spinor spaces differ from axis to axis, since each contains its own idempotent. A bispinor space is not a proper subspace of the algebra; it is the algebra together with a decomposition. The spinor spaces, by contrast, are proper subspaces, and they genuinely differ from axis to axis.

**The corners.** Inside a bispinor space the four Peirce corners $\tilde\Pi_{\mathrm{id},\epsilon}\mathbb{B}\tilde\Pi_{\mathrm{id},\delta}$, with $\epsilon,\delta\in\{+,-\}$, have real dimension $2$ each, and the two spinor spaces are their grouping two by two. The corner count and the spinor count therefore agree in number and not in kind: four corners of dimension $2$, two spinor spaces of dimension $4$.

## What the Family Teaches

**The infinity is not an accident.** The two other carriers also depend on the axis, but their closures do not: the centre and the anti-Hermitian space are the same space at every axis. Only the spin-half closure moves, because only it is built from an idempotent, and an idempotent is a choice.

**There is no canonical member.** Nothing in the algebra singles out an axis, so nothing singles out a plane, a spinor space, or a bispinor space. A statement about one of them is a statement about all of them, and the article writes the axis as a parameter for that reason.

**The count of spaces exceeds the count of carriers.** The algebra has three carriers and infinitely many spinor spaces, because a carrier is a module and a module can be realised in many subspaces. The realisation is not part of the carrier.

**The limits.** This article treats the plane, its two spinor spaces and their sum. It does not treat products of spinor spaces, it does not treat the action of the general invertible elements, and it does not prove that the two ideals are the only minimal left ideals up to the choice of axis.

## Summary

The spin-half carrier is the plane $\Sigma(\vec u_{\mathrm r})=\mathbb{C}\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})$, of real dimension $2$, with weights $\pm\tfrac12$, spin $\tfrac12$, and a full turn acting as $-1$. The plane is invariant only under the rotations about its own axis. Its first closure is the spinor space $S_+=\mathbb{B}\tilde\Pi_{\mathrm{id},+}$, of real dimension $4$, and the second is the bispinor space $\mathbb{B}=S_+\oplus S_-$, of real dimension $8$. Both closures depend on the axis, so the family is infinite and indexed by the real projective plane. As sets the bispinor spaces coincide; as decompositions they differ.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, real, of dimension $8$ |
| $\vec u_{\mathrm r}$ | a unit real axis, the parameter of the family |
| $\vec u_2,\vec u_3$ | an oriented orthonormal pair completing the axis |
| $\theta$ | the rotation angle, twice the rotor angle |
| $\tilde\Pi_{\mathrm{id},\pm}(\vec u_{\mathrm r})=\tfrac12(e_t\pm i\vec u_{\mathrm r})$ | the two idempotents of the axis, a Peirce basis |
| $\Sigma(\vec u_{\mathrm r})=\mathbb{C}\tilde\Pi_{\mathrm{id},+}(\vec u_{\mathrm r})$ | the spinor plane, $\dim_\mathbb{R}=2$ |
| $S_\pm(\vec u_{\mathrm r})=\mathbb{B}\tilde\Pi_{\mathrm{id},\pm}(\vec u_{\mathrm r})$ | the spinor spaces, $\dim_\mathbb{R}=4$ |
| $S_+\oplus S_-=\mathbb{B}$ | a bispinor space, $\dim_\mathbb{R}=8$ |
| $L_X$, $R_X$ | left and right multiplication by $X$ |
| $\varrho$ | the representation of the action on the carrier |
| ${}^{\natural}$ | the natural conjugation, exchanging the two idempotents |

## Further Reading

- [The Clebsch–Gordan Decomposition of the Biquaternion Algebra](the-clebsch-gordan-decomposition-of-the-biquaternion-algebra.html), for the series $\mathbb{B}\cong V_1\oplus V_0$, the two projectors and the label of the slot
- [The Spin-Half Bispinors and N Norm Regularity](the-spin-half-bispinors-and-n-norm-regularity.html), for the nullity of the plane and of the ideals, and the pairing of the two halves
- [The Spin-Half Bispinors and Spectral Regularity](the-spin-half-bispinors-and-spectral-regularity.html), for the spectrum $\{0,\lambda\}$ of the plane and the degenerate plane inside a spinor space
- [From the Spin to the Carriers and the Closures](the-carriers-the-representation-the-spin-and-the-closure.html), for the three carriers, the spin table and the four closures
- [The Minimal Left Ideals of the Biquaternion Algebra](the-minimal-left-ideals-of-the-biquaternion-algebra.html), for the idempotents, the minimality and the splitting of the algebra
- [The Peirce Basis of the Biquaternion Algebra](the-peirce-basis-of-the-biquaternion-algebra.html), for the basis that parametrises the family
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the four corners and their dimensions
- [The One-Sided Action and the Spin Representation](the-one-sided-action-and-the-spin-representation.html), for the left multiplication as a representation
