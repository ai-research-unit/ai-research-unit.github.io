# __The Spin Group: Unit Elements, Rotors and the Two-to-One Cover__

## Introduction

**The subject.** The spin group of the biquaternion algebra is the group of unit elements of the algebra: a three-dimensional sphere inside a four-dimensional algebra. The article identifies the group, parametrises its elements by an axis and an angle, computes the exponential, separates the four actions through which the group is seen, and proves that none of those actions marks an axis.

**The order of the article.** The group and its norm come first, because every later count uses the norm. The rotor parametrisation follows, then the four actions with their kernels, then the exponential with its sign. The two commuting copies and the centraliser theorem come next, then the bracket, then the two decompositions of the algebra. The theorem on the absent axis follows, then the worked rotors, the pitfalls and the numerical check.

**It assumes** *Introduction to the Algebra of Biquaternions*, *The Element, the Coordinates and the Conjugations in the Biquaternion Algebra* and *The Clebsch–Gordan Decomposition of the Biquaternion Algebra*. **The row of the operators is** *The Spin Group: the Principal Copy, $\operatorname{Sym}^{3}$ and the Kernel $\{\pm I\}$*, where the same group acts on the sixteen operators instead of on the four elements.

**The result in one line.** The group is $\{\tilde u\in\mathbb{B}:\tilde u\tilde u^{\natural}=e_t\}=S^{3}$; every element is $\pm(\cos\theta\,e_t+\sin\theta\,\vec u)$ with $\vec u$ a unit real axis; the conjugation is two-to-one onto the rotations of the vector part, with kernel $\{\pm e_t\}$; and left multiplication splits the algebra into two copies of the slot while carrying no invariant real line at all.

**Boundaries.** The group of all unitary elements, of real dimension four, is *The Unitary Group of the Biquaternion Algebra*; the rotation that one rotor produces on the vector part is *From the Spin Group to the Spin of a Single Rotor*; the carriers and their closures are *From the Spin to the Carriers and the Closures*; the two-sided action as a Lorentz transformation is *Biquaternion Rotations and Lorentz Transformations*.

## The Group and Its Norm

**Definition (spin group).** The **spin group** is

$$
\mathrm{Spin}=\{\tilde u\in\mathbb{B}:\tilde u\tilde u^{\natural}=e_t\},
$$

the elements of natural norm one, where $\natural$ is the natural conjugation, $x^{\natural}=\mathrm{Sc}(x)-\mathrm{Vec}(x)$, and $\langle x\rangle_{\natural}=xx^{\natural}$ is the natural norm.

**Proposition.** The set is a group, closed under $\natural$ and under inversion, and it is the unit sphere of the real quaternion subalgebra, of real dimension three.

*Proof.* The norm is multiplicative, so a product of two elements of norm one has norm one. For such an element the equation $\tilde u\tilde u^{\natural}=e_t$ gives $\tilde u^{-1}=\tilde u^{\natural}$, so the inverse is the conjugate and the set is closed under $\natural$. In the four real coordinates $q_t,q_x,q_y,q_z$ of the real form the condition is $q_t^{2}+q_x^{2}+q_y^{2}+q_z^{2}=1$, the equation of a sphere of real dimension three.

**Corollary.** The group is connected and simply connected.

*Proof.* It is the sphere $S^{3}$, which is connected and simply connected.

**Corollary.** The group is not the group of unitary elements of the algebra.

*Proof.* Let $G=\{u:uu^{*}=e_t\}$, with $*$ the Hermitian conjugation, and take $u=\lambda e_t$ with $\lambda\in\mathbb{C}$. The Hermitian norm is $\lvert\lambda\rvert^{2}$, so $e^{i\theta}e_t$ lies in $G$ for every real $\theta$; the natural norm is $\lambda^{2}=e^{2i\theta}$, so $e^{i\theta}e_t$ lies in the spin group only at $\theta=0$ and $\theta=\pi$. The circle of phases is therefore a one-dimensional family in $G$ and not in the spin group, and $G$ has real dimension four against the three of the sphere.

**The reading.** The two groups are one dimension apart and are constantly confused. The spin group is the sphere of unit elements for the natural norm; the unitary group is the four-dimensional group defined by the Hermitian norm. The extra dimension is the circle of phases, and every statement of this article is a statement about the sphere.

## The Rotors

**Definition (rotor).** A **rotor** is an element of the form

$$
\tilde u=\cos\theta\,e_t+\sin\theta\,\vec u,
$$

with $\vec u$ a unit real vector, so that $\vec u^{2}=-e_t$, and $\theta$ a real angle. The vector $\vec u$ is the **axis** of the rotor and $\theta$ is its **angle**.

**Proposition.** The rotors are exactly the elements of the spin group.

*Proof.* A rotor has natural norm $\cos^{2}\theta+\sin^{2}\theta=1$, so it lies in the group. Conversely let $\tilde u=s e_t+\vec v$ satisfy $\tilde u\tilde u^{\natural}=e_t$, with $s$ the scalar part and $\vec v$ the vector part. The condition is $s^{2}+\lvert\vec v\rvert^{2}=1$ with $s$ real and $\vec v$ real, so writing $s=\cos\theta$ and $\vec v=\sin\theta\,\vec u$ produces the displayed form.

**Proposition (uniqueness).** The pair $(\theta,\vec u)$ is unique once the angle is restricted to $[0,\pi]$, and at the two ends the axis is read up to sign.

*Proof.* The angles $\theta$ and $2\pi-\theta$ have the same scalar part and opposite vector parts, so the restriction to $[0,\pi]$ removes the double count. At $\theta=0$ the element is $e_t$ and at $\theta=\pi$ it is $-e_t$; in both cases the vector part vanishes and no axis is present.

**Corollary.** The conjugate of a rotor is its inverse, $\tilde u^{\natural}=\cos\theta\,e_t-\sin\theta\,\vec u=\tilde u^{-1}$, and the rotors are closed under $\natural$.

*Proof.* The conjugate negates the vector part, and the inverse equals the conjugate because the norm is one.

**The reading.** The axis belongs to the element and not to the group. Every rotor other than $\pm e_t$ has an axis, and the axes of neighbouring rotors are neighbouring. This is the fact that the theorem of *No Preferred Axis* turns into a statement about the whole group.

## The Four Actions

**Definition.** The spin group acts on the algebra in four ways:

$$
L_{\tilde u}(X)=\tilde u X,\qquad
R_{\tilde u}(X)=X\tilde u,\qquad
\operatorname{Ad}_{\tilde u}(X)=\tilde u X\tilde u^{\natural},\qquad
(\tilde u,\tilde v)\cdot X=\tilde u X\tilde v^{\natural}.
$$

The first is left multiplication, the second right multiplication, the third the conjugation, and the fourth the two-sided action of the product of two copies of the group.

**Theorem (kernels, images and dimensions).**

| action | kernel | image | dimension |
|---|---|---|---|
| left multiplication | $\{e_t\}$ | the left copy, faithful | $3$ |
| right multiplication | $\{e_t\}$ | the right copy, faithful | $3$ |
| conjugation | $\{\pm e_t\}$ | the rotations of the vector part | $3$ |
| two-sided | $\{\pm(e_t,e_t)\}$ | the rotations of the whole algebra | $6$ |

*Proof.* Left multiplication kills no rotor but the identity, since $\tilde uX=X$ for every $X$ forces $\tilde u=e_t$ on taking $X=e_t$; the same argument on the right. For the conjugation, $\tilde uX\tilde u^{\natural}=X$ for every $X$ makes $\tilde u$ central; the central elements are the complex scalars, and the only rotors among them are $\pm e_t$. For the two-sided action, $\tilde uX\tilde v^{\natural}=X$ for every $X$ forces $\tilde u=\tilde v=\pm e_t$ with the signs equal. The dimensions are those of the groups, three for one copy and six for the product modulo the diagonal pair.

**Corollary.** The two one-sided actions are faithful, the conjugation and the two-sided action are not, and the two-sided action is not the product of two conjugations.

*Proof.* The kernels are as in the table. The two-sided action is a product of a left and a right multiplication, and each of those is faithful. The product of two conjugations is $\operatorname{Ad}_{\tilde u}\operatorname{Ad}_{\tilde v}=\operatorname{Ad}_{\tilde u\tilde v}$, a single conjugation.

**The reading.** Faithfulness is what separates the four actions. The two one-sided ones carry the sign, since $L_{-\tilde u}=-L_{\tilde u}$ is a nonidentity operator; the two others do not, since $-e_t$ acts as the identity on every element by conjugation. A sentence that names a group without naming its action is incomplete, because the kernel belongs to the action.

## The Exponential and the Sign

**Proposition (the closed form).** For a vector $\vec v$ of the vector part with $\lvert\vec v\rvert=\lambda$,

$$
\exp(\vec v)=\cos\lambda\,e_t+\frac{\sin\lambda}{\lambda}\,\vec v,
$$

so the exponential of the vector part lands in the spin group.

*Proof.* The square of $\vec v$ is $-\lambda^{2}e_t$, so the exponential series separates into its even and its odd part, $\cos\lambda$ times the identity and $(\sin\lambda/\lambda)$ times $\vec v$.

**Corollary.** For every unit axis $\vec u$ the exponential satisfies $\exp(\pi\vec u)=-e_t$ and $\exp(2\pi\vec u)=e_t$.

*Proof.* Evaluate the closed form at $\lambda=\pi$, where $\sin\pi=0$ and $\cos\pi=-1$, and at $\lambda=2\pi$, where $\sin2\pi=0$ and $\cos2\pi=1$.

**Corollary (the fibre).** The exponential from the vector part is onto the group, and the fibre over the identity is the set of vectors $2\pi k\,\vec u$ with $k$ an integer and $\vec u$ a unit axis; the sphere of radius $\pi$ collapses to the single element $-e_t$.

*Proof.* The closed form at $\lambda$ and at $2\pi-\lambda$ agrees, so the map is not injective; it is onto because every rotor is the exponential of its own vector part. The fibre over $e_t$ is given by $\sin\lambda=0$, that is $\lambda=2\pi k$, and at such a radius the closed form is $e_t$ for every axis.

**Proposition (the angle doubling).** Let $\tilde u$ be the rotor of angle $\theta$ about the axis $\vec u$ and let $\vec v$ be perpendicular to $\vec u$. Then

$$
\tilde u\,\vec v\,\tilde u^{\natural}=\cos2\theta\,\vec v+\sin2\theta\,(\vec u\times\vec v),
$$

so the conjugation acts on the vector part as the rotation of angle $2\theta$ about $\vec u$.

*Proof.* Multiply out with $\tilde u=\cos\theta+\sin\theta\vec u$ and $\tilde u^{\natural}=\cos\theta-\sin\theta\vec u$, using $\vec u^{2}=-e_t$, $\vec u\vec v=\vec u\times\vec v$ and $\vec u(\vec v\times\vec u)=-\vec v$ for perpendicular unit-orthogonal vectors. The scalar part cancels, the terms in $\vec u$ combine into $\sin\theta\cos\theta\,(\vec u\times\vec v)$ twice, and the identity $\cos^{2}\theta-\sin^{2}\theta=\cos2\theta$ and $2\sin\theta\cos\theta=\sin2\theta$ give the displayed form.

**Corollary.** Every rotation of the vector part is the image of exactly two rotors, $\tilde u$ and $-\tilde u$, and the rotation of a full turn is the image of the rotor of angle $\pi$, which is $-e_t$.

*Proof.* The angle $2\theta$ and the angle $2\theta+2\pi$ give the same rotation, and the two rotors realising them differ by a half turn, that is by the sign. The kernel of the conjugation is $\{\pm e_t\}$ as in the table.

**The reading.** The factor two of the angle is the whole reason for the double cover, and its residue is the sign. A full turn of the rotation is a half turn of the rotor, so after $2\pi$ in the group the element is $-e_t$ and not $e_t$; that element acts trivially by conjugation, and the kernel $\{\pm e_t\}$ is exactly the record of the factor two.

## The Two Commuting Copies

**Proposition.** Left and right multiplication commute, $L_{\tilde u}R_{\tilde v}=R_{\tilde v}L_{\tilde u}$, and the six operators $L_{\vec e_x},L_{\vec e_y},L_{\vec e_z},R_{\vec e_x},R_{\vec e_y},R_{\vec e_z}$ are linearly independent.

*Proof.* Both sides send $X$ to $\tilde uX\tilde v$, which is associativity. The independence is the statement that the left copy acts on one tensor factor of $\mathbb{B}\cong S\otimes S^{*}$ and the right copy on the other, and the numerical check confirms rank six.

**Corollary.** The two groups meet in $\{\pm e_t\}$, and the two Lie algebras of operators meet only at zero.

*Proof.* An operator that is both a left and a right multiplication acts centrally on one side, so it is a complex scalar, and the rotors among the scalars are $\pm e_t$. At the level of the Lie algebras the intersection consists of the scalar multiples of the identity that lie in both six-dimensional spaces, and that is zero.

**Theorem (the centraliser).** The centraliser of the left copy in the algebra of operators on the algebra is the right copy, of complex dimension four.

*Proof.* Let $T$ commute with every $L_{\tilde u}$, hence with every $L_{e_\mu}$. Then $T(X)=T(Xe_t)=XT(e_t)$ for every $X$, so $T$ is right multiplication by $T(e_t)$. The right multiplications form a four-dimensional space, and the numerical check gives dimension four and places the centraliser inside their span.

**Corollary.** Left multiplication is irreducible over the real numbers, and over the complex numbers it is the sum of two copies of the slot.

*Proof.* By the centraliser theorem the commutant of the left action is the right copy. Over the real numbers that commutant is the quaternion algebra, a division algebra, and a representation whose commutant is a division algebra is irreducible: a proper invariant subspace would give the projector onto it as a noninvertible element of the commutant. Over the complex numbers the same commutant is the algebra of two-by-two elements, which is not a division algebra, and it acts on a four-dimensional space as two copies of its two-dimensional irreducible.

**The reading.** The centraliser theorem is the structural reason the left copy is a proper subgroup of the rotations of the algebra and not the whole of it. The rotations are six-dimensional, the two copies supply all six, and each centralises the other because the algebra is a tensor square of the slot. The theorem is also the sharpest statement of the distance between the real and the complex readings: the same commutant is a division algebra in one and a full algebra of two-by-two elements in the other.

## The Bracket and Its Normalisation

**Proposition.** The raw generators obey

$$
[\vec e_x,\vec e_y]=2\vec e_z,\qquad[\vec e_y,\vec e_z]=2\vec e_x,\qquad[\vec e_z,\vec e_x]=2\vec e_y,
$$

that is $[\vec e_i,\vec e_j]=2\varepsilon_{ijk}\vec e_k$; after halving, the normalised generators satisfy $[\tfrac12\vec e_i,\tfrac12\vec e_j]=\varepsilon_{ijk}\tfrac12\vec e_k$.

*Proof.* The product $\vec e_x\vec e_y$ is $\vec e_z$ and the product $\vec e_y\vec e_x$ is $-\vec e_z$, so the commutator is twice $\vec e_z$; the other two are cyclic.

**Corollary.** The same factor two appears on the left copy and on the right copy, and it is a property of neither.

*Proof.* Both copies are images of the same bracket of the algebra under multiplicative maps, and a multiplicative map preserves the commutator, so both carry the factor two; halving the generators divides it by two on both sides at once.

**The reading.** It is often said that one copy carries the factor two while the other does not, and the pair is presented as a difference between the two actions. There is no such difference. Both brackets are twice the structure constants, and the familiar form appears after the same halving on both sides.

## The Two Decompositions

**Theorem (left multiplication).** Under left multiplication the algebra is the sum of two copies of the slot,

$$
\mathbb{B}\cong V_{1/2}\oplus V_{1/2},
$$

and the Casimir of the normalised generators is the scalar $-\tfrac34$ on both summands.

*Proof.* The algebra is the tensor square of the slot and left multiplication acts on the first factor alone; that factor is two-dimensional, so the algebra is two copies of it. The sum of the squares of the normalised generators is left multiplication by $\tfrac14\sum_k\vec e_k^{2}=-\tfrac34e_t$, which the numerical check confirms exactly, and $-\tfrac34=-s(s+1)$ at $s=\tfrac12$.

**Theorem (the conjugation).** Under the conjugation the algebra splits by the label,

$$
\mathbb{B}\cong V_1\oplus V_0,
$$

of dimensions $3+1$, and the Casimir of the normalised generators takes the values $-2$ and $0$.

*Proof.* The conjugation fixes the scalars and acts on the vector part by the rotations; the vector part is three-dimensional and irreducible under them, and the scalars are fixed. The Casimir of the normalised generators has the eigenvalues $-2=-k(k+1)$ at $k=1$, with multiplicity three, and $0$ at $k=0$, with multiplicity one.

**Corollary.** Left multiplication carries no invariant line and no invariant hyperplane, and the conjugation isolates exactly one canonical line, the scalar line.

*Proof.* The left action is the sum of two copies of a two-dimensional space, so every invariant subspace is a sum of whole copies and there is no invariant line or hyperplane. Under the conjugation the only invariant line is the scalar line, because the vector part is irreducible of dimension three. Left multiplication moves that line onto the vector part, since $L_{\vec u}(e_t)=\vec u$.

**The reading.** The two decompositions cut one four-dimensional space in two ways, $2+2$ and $3+1$, and the difference is the difference between the actions. The labels come from the Clebsch–Gordan series of the tensor square, $\tfrac12\otimes\tfrac12=1\oplus0$, and not from the parametrisation of the group: the pair $(\theta,\vec u)$ carries no label, and a parametrisation that carried one would be a coincidence and not a property of the group.

## The Four Carriers of the Operator Space

**The setting.** Everything so far decomposes the algebra, of complex dimension four. The operators on the algebra are a different space, of complex dimension sixteen, and they carry a longer tower. This section names the four carriers of that space, because the four subsections that follow take them one at a time.

**The carrier of the operators.** The operators on a four-dimensional carrier form its tensor square. The four-dimensional carrier here is the symmetric cube of the slot,

$$
V_{3/2}=\operatorname{Sym}^{3}S,\qquad \dim V_{3/2}=2\cdot\tfrac32+1=4,
$$

and the Clebsch–Gordan rule for its tensor square is

$$
\tfrac32\otimes\tfrac32=\bigoplus_{k=0}^{3}V_k=V_3\oplus V_2\oplus V_1\oplus V_0,
\qquad 7+5+3+1=16.
$$

Each of the four occurs exactly once. The algebra itself stops at the two even ones, $\mathbb{B}\cong V_1\oplus V_0$; the two odd carriers and the two higher ones live on the operators.

**Theorem (the four summands).** The four carriers, their dimensions and their Casimir values are

| carrier | spin | dimension | Casimir $k(k+1)$ | where it lives |
|---|---|---|---|---|
| $V_0$ | $0$ | $1$ | $0$ | the scalars, the centre |
| $V_1$ | $1$ | $3$ | $2$ | the vector part |
| $V_2$ | $2$ | $5$ | $6$ | the operators only |
| $V_3$ | $3$ | $7$ | $12$ | the operators only |

and no carrier of intermediate dimension occurs between them.

*Proof (weights).* The weights of $V_{3/2}$ are $-\tfrac32,-\tfrac12,\tfrac12,\tfrac32$, so the weights of the tensor square are the sums $m+n$ of two of them. Counting them gives the multiset

$$
\{-3:1,\;-2:2,\;-1:3,\;0:4,\;1:3,\;2:2,\;3:1\}.
$$

The highest weight is $3$, so $V_3$ occurs, of dimension seven, and removing its weight string $\{3,2,1,0,-1,-2,-3\}$ leaves $\{-2:1,-1:2,0:3,1:2,2:1\}$. The highest weight is now $2$, so $V_2$ occurs, of dimension five, and removing its string leaves $\{-1:1,0:2,1:1\}$. The highest weight is now $1$, so $V_1$ occurs, of dimension three, and removing its string leaves $\{0:1\}$, which is $V_0$. The four dimensions sum to $7+5+3+1=16$, so nothing is left over, and each carrier occurs once because at every step the highest weight present is stripped once and the remainder is again a sum of full strings.

**Corollary.** The Casimir takes the four values $0,2,6,12$ on the operator space, with multiplicities $1,3,5,7$.

*Proof.* The Casimir of $V_k$ is $k(k+1)$, and $k=0,1,2,3$ gives $0,2,6,12$; the multiplicities are the dimensions, since each carrier occurs once.

**Corollary.** The four projectors onto the carriers have traces $1,3,5,7$, and their sum is the identity of the operator space.

*Proof.* The trace of a projector is the dimension of its image, and the images are the four carriers, which span the space.

**The half-integers.** The two half-integer carriers are not summands of the algebra either. The slot $V_{1/2}$ of dimension two is realised by a minimal left ideal, and $V_{3/2}$ of dimension four is realised by its symmetric cube; the algebra contains $V_{1/2}\otimes V_{1/2}=V_1\oplus V_0$ and not the odd carriers themselves. That is why the tower runs $1,2,3,4,5,7$ in dimensions and skips six: the dimensions are $2k+1$ at integer $k$ and $2$ or $4$ at half-integer $k$, and no carrier of dimension six arises from a tensor square of slots.

**The reading.** The four carriers are the four rows of the operator section, and the split $1+3+5+7$ is the operator analogue of the algebra's $3+1$. The first two are already present on the algebra; the last two exist only once one passes to the operators, which is the reason the operator section is longer than the section on the algebra. The Carrier articles take $V_0$, $V_{1/2}$, $V_1$ and $V_{3/2}$ in turn, and $V_2$ and $V_3$ follow in the later subsections.

## No Preferred Axis

**Theorem.** Let $\vec u$ be a unit real axis and let $L_{\vec u}$ be left multiplication by it. Then $L_{\vec u}$ has no invariant real line in the algebra, and its eigenvalues are $\pm i$.

*Proof.* The square $L_{\vec u}^{2}$ is left multiplication by $\vec u^{2}=-e_t$, so $L_{\vec u}^{2}=-\mathrm{id}$ and every eigenvalue $\lambda$ satisfies $\lambda^{2}=-1$. An eigenvector with a real eigenvalue therefore does not exist, and no real line is carried to itself.

**Theorem (the invariant complex lines).** The invariant complex lines of $L_{\vec u}$ are the minimal left ideals built from the idempotents of the axis, $\mathbb{B}\tilde\Pi_{\pm}(\vec u)$, and they are indexed by the pair $\pm\vec u$.

*Proof.* Over the complex numbers the equation $L_{\vec u}^{2}=-\mathrm{id}$ gives the two eigenspaces of the eigenvalues $\pm i$, and each is a two-dimensional space spanned by the elements annihilated by the projectors $\tilde\Pi_{\mp}(\vec u)$ of the axis; the lines inside an eigenspace are the minimal left ideals of that axis. A different axis gives a different pair of idempotents and hence a different pair of eigenspaces.

**Corollary.** No action of the group marks an axis, and a decomposition of the algebra into two invariant complex subspaces is a choice of a point of the sphere of axes.

*Proof.* Every rotor other than $\pm e_t$ has an axis, and conjugation carries the axis of $\tilde u$ to the axis of $\tilde v\tilde u\tilde v^{\natural}$, which runs over the whole sphere of axes as $\tilde v$ runs over the group; no axis is fixed. The invariant complex subspaces are the eigenspaces above, indexed by the axis, so choosing them is choosing the axis.

**Corollary (all three axes at once).** The natural conjugation negates the three axes simultaneously, and no rotor conjugation negates a single axis while fixing the other two.

*Proof.* The natural conjugation sends $\vec e_k$ to $-\vec e_k$ for the three $k$ at once. A rotor conjugation acts on the vector part as a rotation, which preserves the orientation, so the map that reverses one axis and fixes the other two, of determinant $-1$, is not available.

**The reading.** The absence of an invariant real line is the exact form of the statement that no axis is preferred. A reader who wants the algebra cut into two invariant two-dimensional complex pieces must pay for it with a choice, and the price is a point of the sphere of axes: the piece written first is the minimal left ideal of that point. Different choices give pictures related by a rotor, and the group cannot tell them apart.

## Worked Rotors

**The quarter turn.** The rotor of angle $\tfrac{\pi}{2}$ about the axis $\vec e_z$ is $\tfrac{1}{\sqrt2}(e_t+\vec e_z)$, its conjugate is $\tfrac{1}{\sqrt2}(e_t-\vec e_z)=$ its inverse, and the product of the two is $e_t$.

**Corollary.** The quarter turn acts on the vector part as the rotation of angle $\tfrac{\pi}{2}$, sending $\vec e_x$ to $\vec e_y$; the half turn, which is the rotor $\vec e_z$ of angle $\pi$, sends both $\vec e_x$ and $\vec e_y$ to their negatives and fixes $\vec e_z$.

*Proof.* The angle doubling, at $\theta=\tfrac{\pi}{2}$ and at $\theta=\pi$; at $\theta=\pi$ the two-sided product is $\vec e_z\vec v\vec e_z^{\natural}=-\vec e_z\vec v\vec e_z$, and for $\vec v$ in the plane of the axis the two sign changes cancel, while for $\vec v$ along the axis they add.

**The sign after a full turn.** The rotor of angle $2\pi$ is $-e_t$. It is a distinct element of the group, the second element of the kernel of the conjugation, and it acts on the algebra as the identity by conjugation and as minus the identity by left multiplication.

**Corollary.** Two rotors about the same axis compose to the rotor of the sum of their angles, and a full turn returns $-e_t$ and not $e_t$.

*Proof.* The rotors about one axis form the circle $\{e^{i\theta}\}$ read inside the algebra, and the additivity of angles is the multiplicativity of that circle.

**The two-sided product.** For one rotor the two-sided action is the conjugation, $X\mapsto\tilde uX\tilde u^{\natural}$; for two independent rotors it is $X\mapsto\tilde uX\tilde v^{\natural}$, which is the six-dimensional rotation of the algebra, with the two factors acting on the two tensor slots.

## The Pitfalls

**Eight sentences that must not be written as they stand.**

1. **"The spin group is the group of unitary elements."** It is not: the unitary group has real dimension four and contains the circle of phases; the spin group is the three-dimensional sphere of unit elements for the natural norm.
2. **"The spin group is the group of rotations."** It is not: the conjugation is two-to-one onto the rotations of the vector part, with kernel $\{\pm e_t\}$, and the rotation group is an image.
3. **"The spin group has a preferred axis."** It has not: an element has an axis, and the group carries the sphere of axes onto itself by all of its rotations.
4. **"Left multiplication fixes the scalars."** It does not: it is the sum of two copies of the slot, and $L_{\vec u}(e_t)=\vec u$. It is the conjugation that fixes the scalars.
5. **"The two-sided action is the product of two conjugations."** It is not: it is a product of a left and a right multiplication, its kernel is the pair of diagonal signs, and the product of two conjugations is one conjugation.
6. **"Left multiplication splits as $1\oplus3$."** Over the real numbers it does not split at all; over the complex numbers it splits as two copies of the slot, and never as a line and a three-dimensional space. The split $3+1$ belongs to the conjugation.
7. **"The two copies carry different brackets."** They do not: both are twice the structure constants, and the familiar form appears after the same halving on both sides.
8. **"The labels $\tfrac12$ and $1$ come from the parametrisation."** They do not: they come from the Clebsch–Gordan series of the tensor square, and the parametrisation by axis and angle carries no label.

## Verification

**How the numbers were obtained.** The four units were multiplied by the structure rules $\vec e_k^{2}=-e_t$, $\vec e_t\vec e_\nu=\vec e_\nu$ and $\vec e_x\vec e_y=\vec e_z$ cyclic. The operators $L$ and $R$ were built from that table alone, and each claim was computed in double precision on random rotors and random unit axes.

| claim | what was computed | largest residual |
|---|---|---|
| the bracket | $[\vec e_x,\vec e_y]-2\vec e_z$, cyclic | $0$ |
| the two copies commute | $L_{\vec u}R_{\vec v}-R_{\vec v}L_{\vec u}$ | $0$ |
| the six generators are independent | the rank of the six | $6$ |
| the centraliser is the right copy | its dimension, and its distance from the span of the four right multiplications | $4$, and $2.2\cdot10^{-16}$ |
| the left Casimir | $\sum_k\bigl(\tfrac12L_{\vec e_k}\bigr)^{2}+\tfrac34$ | $0$ |
| the conjugation Casimir | the eigenvalues on the algebra | $-2$ three times, $0$ once |
| no invariant real line | the eigenvalues of $L_{\vec u}$ over $300$ axes | $\pm i$, minimal imaginary part $1$ |
| the eigenvector is complex | the rank of $({\rm Re}\,v\mid{\rm Im}\,v)$ | $2$ always |
| the norm of a rotor | $\tilde u\tilde u^{\natural}-e_t$ | $0$ |
| the inverse is the conjugate | $\tilde u^{\natural}\tilde u-e_t$ | $0$ |
| the exponential against its series | forty terms against the closed form, $200$ vectors | $1.1\cdot10^{-15}$ |
| the collapse at $\pi$ | $\exp(\pi\vec u)+e_t$ | $3.6\cdot10^{-16}$ |
| the return at $2\pi$ | $\exp(2\pi\vec u)-e_t$ | $1.4\cdot10^{-14}$ |
| the angle doubling | the two-sided product against the rotation by $2\theta$, $200$ axes | $1.3\cdot10^{-15}$ |
| the conjugation kernel | the rotors acting trivially | the pair $\pm e_t$ |
| the two-sided kernel | the pairs acting trivially | the pair $\pm(e_t,e_t)$ |
| the four carriers | the weight multiset of $\tfrac32\otimes\tfrac32$, stripped | $V_3,V_2,V_1,V_0$, dimensions $7,5,3,1$, total $16$ |
| their Casimirs | $k(k+1)$ at $k=0,1,2,3$ | $0,2,6,12$, multiplicities $1,3,5,7$ |

**One check that is not numerical.** The theorems on irreducibility, on the centraliser and on the absent axis are statements about every element, and no sample confirms them. They are proved above, and the numbers confirm only the instances computed: that the six generators are independent, that the centraliser has dimension four and lies inside the right copy, that the eigenvalues of the sampled left multiplications are $\pm i$ with no real one, and that the eigenvector directions are genuinely complex.

## Summary

The spin group is the group of unit elements of the algebra, a sphere of real dimension three inside the real form, and every element is a rotor $\pm(\cos\theta\,e_t+\sin\theta\,\vec u)$. The exponential of the vector part is $\cos\lambda\,e_t+\lambda^{-1}\sin\lambda\,\vec v$; it covers the group, it satisfies $\exp(\pi\vec u)=-e_t$ and $\exp(2\pi\vec u)=e_t$, and its fibre over the identity is the set of vectors $2\pi k\vec u$.

The group acts in four ways and the kernels separate them: the two one-sided actions are faithful, the conjugation has kernel $\{\pm e_t\}$ and is two-to-one onto the rotations of the vector part, and the two-sided action has kernel $\{\pm(e_t,e_t)\}$ and is six-dimensional. The two one-sided copies commute, their generators are six independent operators, and the centraliser of the left copy is the right copy, of dimension four. Over the real numbers that commutant is a division algebra, so left multiplication is irreducible; over the complex numbers it is two copies of the slot, with Casimir $-\tfrac34$.

The conjugation cuts the algebra as $V_1\oplus V_0$, of dimensions $3+1$, with Casimir $-2$ and $0$, and it is the action that isolates the scalar line. On the operators the tower is longer: the operator space is the tensor square of the four-dimensional carrier $V_{3/2}=\operatorname{Sym}^{3}S$, and $\tfrac32\otimes\tfrac32=V_3\oplus V_2\oplus V_1\oplus V_0$, of dimensions $7+5+3+1=16$, each carrier once, with Casimirs $12,6,2,0$. The labels come from the series of the tensor square and not from the group. No action of the group marks an axis: an element has an axis, the group does not, the sphere of axes is carried onto itself by all of its rotations, the eigenvalues of a left multiplication are $\pm i$ so no real line is invariant, and the natural conjugation negates all three axes at once and never one alone.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, of complex dimension four |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the units, with $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ cyclic |
| $\natural$, $\langle x\rangle_{\natural}$ | the natural conjugation and the norm |
| $*$ | the Hermitian conjugation |
| $\mathrm{Spin}$, $Sp(1)$ | the spin group, the rotors, $S^{3}$ |
| $G$ | the unitary group of the algebra, real dimension four |
| $\tilde u,\theta,\vec u$ | a rotor, its angle and its axis |
| $\mathfrak{k}$ | the vector part, the real span of the three pure units |
| $L_{\tilde u},R_{\tilde u}$ | left and right multiplication, the two commuting copies |
| $\operatorname{Ad}_{\tilde u}$ | the conjugation by a rotor |
| $V_{1/2},V_1,V_0$ | the carriers, of dimensions $2,3,1$ |
| $V_{3/2},V_2,V_3$ | $\operatorname{Sym}^{3}S$ and the two higher carriers, of dimensions $4,5,7$ |
| $\tilde\Pi_{\pm}(\vec u)$ | the idempotents of the axis, whose minimal left ideals are the invariant lines |

## Further Reading

- [The Clebsch–Gordan Decomposition of the Biquaternion Algebra](the-clebsch-gordan-decomposition-of-the-biquaternion-algebra.html), for the series $\tfrac12\otimes\tfrac12=1\oplus0$ from which the labels come.
- [From the Spin Group to the Spin of a Single Rotor](from-the-spin-group-to-the-spin-of-a-single-rotor.html), for the rotation one rotor produces and for the sign after $2\pi$.
- [From the Spin to the Carriers and the Closures](the-carriers-the-representation-the-spin-and-the-closure.html), for the carriers and their closures.
- [The Unitary Group of the Biquaternion Algebra](the-unitary-group-of-the-biquaternion-algebra.html), for the four-dimensional group that contains the rotors.
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), for the two-sided action and the Lorentz group.
- [The Minimal Left Ideals of the Biquaternion Algebra](the-minimal-left-ideals-of-the-biquaternion-algebra.html), for the invariant lines of a left multiplication and the idempotents of an axis.
- [The Euclidean Topology of the Biquaternion Algebra](the-euclidean-topology-of-the-biquaternion-algebra.html), for the sphere, its fundamental group and the covering.
- [Quaternion Rotations and Reflections](quaternion-rotations-and-reflections.html), for the same group in the language of rotations.
