# __From the Spin to the Carriers and the Closures__

## Introduction

**The question.** What spins does the biquaternion algebra carry, and which subspaces of it carry them? The question is about the algebra itself. The spins are read from the actions the algebra has on itself, not from a matrix group imposed on it from outside.

**The one decomposition.** The algebra is the endomorphism algebra of one slot, so it is the square of that slot, and the Clebsch–Gordan series for a square of the half-integer slot is

$$
V_{1/2}\otimes V_{1/2}=V_{1}\oplus V_{0},\qquad 3+1=4 .
$$

Everything else in the article is a reading of that line: the two summands, the label of the slot that is squared, the subspace that carries each label, and the closure of each subspace. The split is realized by two operators built from the conjugation alone,

$$
P_{0}=\tfrac12\bigl(\mathrm{id}+\natural\bigr),\qquad P_{1}=\tfrac12\bigl(\mathrm{id}-\natural\bigr),
$$

with no axis and no basis in either of them.

**The answer, one line per carrier.**

$$
\text{the summand }V_{0}\ \longmapsto\ s=0\ \longmapsto\ \dim_\mathbb{R}=1\ \longmapsto\ \text{fixed line }\mathbb{R}e_t\ \longmapsto\ \text{centre},
$$

$$
\text{the factor }V_{1/2}\ \longmapsto\ s=\tfrac12\ \longmapsto\ \dim_\mathbb{R}=2\ \longmapsto\ \text{spinor plane }\Sigma\ \longmapsto\ \text{spinor space, then bispinor space},
$$

$$
\text{the summand }V_{1}\ \longmapsto\ s=1\ \longmapsto\ \dim_\mathbb{R}=3\ \longmapsto\ \text{vector part }\mathfrak{k}\ \longmapsto\ \text{anti-Hermitian space}.
$$

The first and the third lines are the two summands of the series, and the second is the slot that the series squares. The three dimensions are $1,2,3$, the three spins are $0,\tfrac12,1$, and the identity $2s+1=\dim_\mathbb{R}$ compares two counts of the same nature.

**The route.** *The Clebsch–Gordan Decomposition* states the series, builds the two projectors from the conjugation and reads the two summands with their weights, so that the labels $0$ and $1$ are placed on subspaces and not on a list. *The Slot* identifies the remaining label, $\tfrac12$, from the Casimir of the left-regular generators: it is the label of the factor that the series squares. *The Product* confirms the labels $0$ and $1$ on a second carrier, the tensor square of two slots, and on the total Casimir of a pair acting on two sides. *The Criterion* turns irreducibility into a reading of the spectrum, which is what lets a summand of the right dimension be called a carrier. *The Carriers* then names, for each spin, the subspace of real dimension $2s+1$ that carries it, and the assignment is forced by the dimension and by the natural action of the algebra on itself. *The Summands and the Factor* separates the two kinds of carrier, which is why the three are not a direct sum. *Three and No More* proves that no fourth carrier exists. *The Closure of a Carrier* places each carrier in a subspace of $\mathbb{B}$, and *The Quadratic Element* reads the same three numbers from one central element of the algebra.

**The order, and what it buys.** The decomposition comes first, with its two canonical summands; the label of the slot comes second; the carriers come third; the closures come last. Nothing in the list is found by inspection and justified afterwards, and the Casimir computations of *The Slot* and *The Product* change job: they identify the label of a factor and confirm the labels of the summands, instead of producing a list that the reader has no reason to expect.

The article works on real spaces, and the reason is the question itself and not a preference of notation. A spatial rotation acts on a real space, a subspace that a rotation leaves alone is a real subspace, and the question asks for those subspaces. The decomposition above is stated over the complex numbers, where the series lives; the carriers are its real forms, of real dimensions $1$, $2$ and $3$, and every spectrum below is read on them. The complex structure $i$ is an element of the algebra and not a scalar of the ground field, so a complex line of the algebra is also a real plane, and the passages between the two readings are named where they occur. It is one of the operators, on the same footing as $\vec e_x,\vec e_y,\vec e_z$, and the fact that it is available is what the closure steps use.

Three things are not claimed. The article does not read the label $s$ as anything but a spectral quantity: it is the largest weight of a carrier, and no physical vocabulary is attached to it. It does not present the closures as a decomposition, because they are not one: the four closure dimensions sum to $18$, and the algebra has real dimension $8$. And the plane of real dimension $2$ is not a group of arrays returning under another name. It is the smallest faithful carrier of the double cover, and it is realized inside $\mathbb{B}$ by the algebra's own $i$; what can be read into it is a choice of display, not a structure of the algebra.

No argument array is printed anywhere below, at any point, and this is deliberate. An array carries a frame, the frame singles out a direction, and the direction is not part of the algebra: a display that fixes one axis absorbs whatever depends on that axis, and the page then stops showing it. Every statement here is made at a general axis $\vec u_{\mathrm r}$ and proved from two identities that hold at that axis. The rule and its reasons are those of *Matrix Representations Conventions*.

Nothing below is a statement of physics, and no physical vocabulary is used. This article opens the subsection *Spin Geometry* of *Geometry*, in *Biquaternions*.

## Preliminaries

**The algebra.** The biquaternion algebra $\mathbb{B}$ is the real algebra with basis

$$
e_t,\ \vec e_x,\ \vec e_y,\ \vec e_z,\ ie_t,\ i\vec e_x,\ i\vec e_y,\ i\vec e_z,
$$

of real dimension $8$, where $i$ is an element commuting with the four units and $i^2=-e_t$. The four real units multiply as

$$
e_t\tilde Q=\tilde Qe_t=\tilde Q,\qquad
\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t,\qquad
\vec e_x\vec e_y=\vec e_z,\quad \vec e_y\vec e_z=\vec e_x,\quad \vec e_z\vec e_x=\vec e_y,
$$

with the last line read cyclically. An element is written

$$
\tilde Q=q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z+i\bigl(q'_te_t+q'_x\vec e_x+q'_y\vec e_y+q'_z\vec e_z\bigr),
$$

with real coefficients $q_\mu$ and $q'_\mu$, or briefly $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu=q_\mu+iq'_\mu$. The vector part $\vec Q$ is a pure element, and the **pure part** is the real span

$$
\mathfrak{k}=\mathbb{R}\vec e_x\oplus\mathbb{R}\vec e_y\oplus\mathbb{R}\vec e_z,
$$

of real dimension $3$. The **centre** is $\mathbb{B}_C=\mathbb{C}e_t=\mathbb{R}e_t\oplus\mathbb{R}(ie_t)$, of real dimension $2$.

**The two conjugations.** The **natural conjugation** ${}^{\natural}$ fixes $e_t$ and $i$ and negates the vectors:

$$
(Q_te_t+\vec Q)^{\natural}=Q_te_t-\vec Q,\qquad (XY)^{\natural}=Y^{\natural}X^{\natural}.
$$

Where the map is read as an operator it is written $\natural\tilde X$ for $\tilde X^{\natural}$. It is complex-linear and involutive, $\natural^{2}=\mathrm{id}$, so it is the operator that splits the algebra in *The Clebsch–Gordan Decomposition*.

The **star** is the natural conjugation followed by the conjugation of $i$, and it is the Hermitian conjugation of the algebra:

$$
(Q_te_t+\vec Q)^{*}=\bar Q_te_t-\bar{\vec Q},\qquad (XY)^{*}=Y^{*}X^{*}.
$$

An element is **Hermitian** when $X^{*}=X$ and **anti-Hermitian** when $X^{*}=-X$.

**The norm and the invertibles.** The **norm** is

$$
N(\tilde Q)=Q_t^2+Q_x^2+Q_y^2+Q_z^2,
$$

multiplicative, and vanishing exactly on the elements without an inverse. An element is **invertible** when $N(\tilde Q)\ne0$. An element is of norm one, or a **unit**, when $XX^{*}=e_t$; the units form the group $G=\mathrm U(2)$, of real dimension $4$, and every unit is invertible, since $X^{-1}=X^{*}$. The converse fails: the invertible group is $\mathbb{B}^{\times}\cong GL_2(\mathbb{C})$, of real dimension $8$, and $2e_t$ is invertible without being a unit.

**The rotor.** A **unit real axis** is a real pure element $\vec u_{\mathrm r}$ with $(\vec u_{\mathrm r},\vec u_{\mathrm r})=1$ for the positive definite form on $\mathfrak{k}$. For a real angle $\theta_{\mathrm{axr}}$ the **rotor** is

$$
\tilde u_{\mathrm r}=\cos\frac{\theta_{\mathrm{axr}}}{2}\,e_t+\sin\frac{\theta_{\mathrm{axr}}}{2}\,\vec u_{\mathrm r},
$$

with real coefficients and $\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}=e_t$. The rotors form $Sp(1)$, the unit sphere of the quaternion layer, of real dimension $3$.

**The operators.** For an element $X$ the four operators used below are

$$
L_X(Y)=XY,\qquad R_X(Y)=YX,\qquad \operatorname{ad}_X(Y)=XY-YX,\qquad \operatorname{Ad}_u(Y)=uYu^{*},
$$

the last one for $uu^{*}=e_t$. The first two are left and right multiplication, the third is the commutator, the fourth is the conjugation by an invertible element.

## The Clebsch–Gordan Decomposition

The decomposition comes first. It is one line of representation theory, and everything the article reads afterwards is a reading of it: two summands of the algebra, one factor of it, three subspaces of it.

**The square of the slot.** The algebra acts on itself on two sides, $L_{\tilde Q}(\tilde X)=\tilde Q\tilde X$ and $R_{\tilde Q}(\tilde X)=\tilde X\tilde Q$. The first is a homomorphism of algebras, $L_{\tilde Q}L_{\tilde P}=L_{\tilde Q\tilde P}$, and the second is an anti-homomorphism, $R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q}$. A slot on which an algebra acts on the left is a module; a slot on which it acts on the right with the order reversed is the transpose action on the dual. So the right slot is the dual slot and the algebra is the product of a slot with its dual,

$$
\mathbb{B}\cong S\otimes S^{*},\qquad \dim_\mathbb{C}S=2,\qquad 2\cdot 2=4 .
$$

**The series.** The irreducible carriers of the rotor group are labelled by $j\in\tfrac12\mathbb{Z}_{\ge0}$, the carrier of label $j$ has complex dimension $2j+1$ and Casimir $j(j+1)$, and for two labels

$$
j_{1}\otimes j_{2}=\bigoplus_{j=\lvert j_{1}-j_{2}\rvert}^{j_{1}+j_{2}}j,
$$

each summand occurring once. The slot of the algebra is the defining carrier $V_{1/2}$ — its label is computed in *The Slot* below, and the computation is the Casimir of a single factor — and the slot is self-dual, because the rotor group preserves a nondegenerate antisymmetric form on it. So the algebra is a square of one carrier, and the series gives

$$
V_{1/2}\otimes V_{1/2}=V_{1}\oplus V_{0},\qquad \mathbb{B}\cong V_{1}\oplus V_{0},\qquad 3+1=4 .
$$

Each label occurs once, so each summand is the whole isotypic piece of its label: a subspace that is invariant and of the right dimension *is* the summand, and no further identification is needed.

**The two projectors.** The split is realized by two operators built from the natural conjugation alone,

$$
P_{0}=\tfrac12\bigl(\mathrm{id}+\natural\bigr),\qquad P_{1}=\tfrac12\bigl(\mathrm{id}-\natural\bigr),
\qquad
P_{0}^{2}=P_{0},\quad P_{1}^{2}=P_{1},\quad P_{0}P_{1}=0,\quad P_{0}+P_{1}=\mathrm{id},
$$

because $\natural^{2}=\mathrm{id}$ and $\natural$ is complex-linear: it fixes $e_t$ and $i$ and negates the vectors, and it does not touch the coefficients. On $\tilde X=Q_te_t+\vec Q$ they read

$$
P_{0}\tilde X=Q_te_t,\qquad P_{1}\tilde X=\vec Q,
$$

so the summands are the centre and the vector part,

$$
P_{0}\mathbb{B}=\mathbb{B}_C=\mathbb{C}e_t,\qquad P_{1}\mathbb{B}=\mathbb{C}\mathfrak{k},
$$

of complex dimensions $1$ and $3$, with real forms $\mathbb{R}e_t$ and $\mathfrak{k}$.

**Why the natural conjugation and not the star.** The star is the natural conjugation followed by the conjugation of $i$, so it is conjugate-linear, and a conjugate-linear involution does not split a complex space: its two eigenspaces are real subspaces of real dimensions $4$ and $4$. That split exists, it is $\mathbb{B}=\mathbb{B}_\Phi\oplus\mathbb{B}_\Psi$, and it is the split used by the closures of *The Closure of a Carrier*. The Clebsch–Gordan split of the algebra is the complex-linear one, and its two summands are complex subspaces.

**The equivariance.** For a rotor $\tilde u_{\mathrm r}$ one has $\natural\tilde u_{\mathrm r}=\tilde u_{\mathrm r}^{*}=\tilde u_{\mathrm r}^{-1}$, and $\natural$ is an anti-automorphism, so

$$
P_{0}\bigl(\tilde u_{\mathrm r}\tilde X\tilde u_{\mathrm r}^{*}\bigr)=\tilde u_{\mathrm r}\,P_{0}\bigl(\tilde X\bigr)\tilde u_{\mathrm r}^{*},
\qquad
P_{1}\bigl(\tilde u_{\mathrm r}\tilde X\tilde u_{\mathrm r}^{*}\bigr)=\tilde u_{\mathrm r}\,P_{1}\bigl(\tilde X\bigr)\tilde u_{\mathrm r}^{*}.
$$

The projectors therefore intertwine the conjugation action of the rotors with itself: each summand is invariant under the action $X\mapsto\tilde u_{\mathrm r}X\tilde u_{\mathrm r}^{*}$, and the split belongs to the two-sided action and to nothing one-sided.

**The labels, read at the general axis.** The label of each summand is its largest weight, and the weights are read from the generator $A(\vec u_{\mathrm r})$ of the conjugation action. On the centre the action is trivial, so the weight set is $\{0\}$ and the label is $0$. On the vector part the action is the cross product, by the second identity of *The Rotation Action*, so with an oriented orthonormal pair $\vec u_2,\vec u_3$ completing the axis the operator sends $\vec u_2\pm i\vec u_3$ to $\mp i(\vec u_2\pm i\vec u_3)$ and kills the axis: the weight set is $\{-1,0,+1\}$ and the label is $1$. The two labels are the two terms of the series, read on the two subspaces and not on a list.

**What the decomposition settles, and what it leaves open.** It settles the two summands: their subspaces, their labels, and their canonicity, since neither projector contains an axis or a basis. It does not settle the third carrier. The slot is a factor of the algebra and not a summand of it: $S$ is not a subspace of $S\otimes S^{*}$, and a realization of it inside $\mathbb{B}$ needs a minimal left ideal, that is, an idempotent and an axis. That is the whole content of *The Carriers* and of *The Summands and the Factor*, and it is why the article lists three carriers while the series gives two summands.

## The Rotation Action

**The rotation group.** A **rotation** of the pure part is a real-linear map $R:\mathfrak{k}\to\mathfrak{k}$ that preserves the form and has determinant $1$. The rotations form the group $SO(\mathfrak{k})$, the usual group of spatial rotations.

**Definition (real representation).** Let $H$ be a group and $V$ a real vector space. A **real representation** of $H$ on $V$ is a map $\varrho:H\to GL_\mathbb{R}(V)$ with

$$
\varrho(e_t)=\mathrm{id}_V,\qquad \varrho(uv)=\varrho(u)\varrho(v).
$$

The second line is the law. It is what makes the operator a function of the group element rather than a table indexed by elements: two successive rotations have the operator of their product, with no freedom. Every space below is a real vector space and every operator is real-linear.

**The three actions.** Three representations occur.

The **trivial action** on a real line, $\varrho_{\mathrm{tr}}(u)=\mathrm{id}$.

The **adjoint action** on the pure part, $\varrho_{\mathrm{ad}}(u)=\operatorname{Ad}_u$. It preserves $\mathfrak{k}$, because $u\vec vu^{*}$ is again a real pure element for $\vec v\in\mathfrak{k}$ and $u\in G$, and it preserves the form, because the norm is multiplicative, $N(u)N(u^{*})=N(uu^{*})=1$, so $N(u\vec vu^{*})=N(\vec v)$, and the form is recovered from the norm by $(\vec p,\vec q)=\tfrac14\bigl(N(\vec p+\vec q)-N(\vec p-\vec q)\bigr)$. So $\varrho_{\mathrm{ad}}$ is a homomorphism $G\to SO(\mathfrak{k})$.

The **spinor action** on a real plane, $\varrho_{\mathrm{def}}(X)=L_X$. Unlike the other two it is defined for every element of the algebra and not only for the units, because left multiplication is multiplicative on the whole algebra. The plane it acts on is described in *The Carriers*.

**Definition (carrier).** A **carrier** is a nonzero real subspace of $\mathbb{B}$ that is invariant and irreducible under one of these actions. The action is part of the carrier, because the same subspace can be reducible for one action and irreducible for another. The three carriers are computed in *The Carriers*, and the list is complete: there are three and no more, which is proved in *Three and No More* and not assumed.

**How the rotor performs the rotation.** For the rotor of an axis $\vec u_{\mathrm r}$ and an angle $\theta_{\mathrm{axr}}$, the operator $\operatorname{Ad}_{\tilde u_{\mathrm r}}$ on $\mathfrak{k}$ is the rotation about $\vec u_{\mathrm r}$ through $\theta_{\mathrm{axr}}$:

$$
\operatorname{Ad}_{\tilde u_{\mathrm r}}(\vec v)=\vec v_\parallel+\vec v_\perp\cos\theta_{\mathrm{axr}}+(\vec u_{\mathrm r}\times\vec v)\sin\theta_{\mathrm{axr}},
$$

with $\vec v_\parallel=(\vec u_{\mathrm r}\cdot\vec v)\vec u_{\mathrm r}$ and $\vec v_\perp=\vec v-\vec v_\parallel$. The angle appears halved in the rotor because the rotor enters twice, once on each side, and the two halves add. The map $Sp(1)\to SO(\mathfrak{k})$ is onto with kernel $\{\pm e_t\}$, so a rotation has two rotors and the cover is two to one.

**The generator.** The **generator** along the axis is the real pure element

$$
A(\vec u_{\mathrm r})=\tfrac12\vec u_{\mathrm r},
$$

and $A_k=\tfrac12\vec e_k$ for the three coordinate axes. It is one half of the axis, and it lies in $\mathfrak{k}$. The derivative at $t=0$ of $t\mapsto\varrho(\exp t\vec u_{\mathrm r})$ is $\varrho(\vec u_{\mathrm r})$, so the generator of the action is $\varrho(A)$, and

$$
\varrho(\tilde u_{\mathrm r})=\exp\bigl(\theta_{\mathrm{axr}}\,\varrho(A(\vec u_{\mathrm r}))\bigr).
$$

This is the exponential form used below: real operator, real exponent, no $i$ in the display. The Hermitian element of the corpus is $\tilde S(\vec u_{\mathrm r})=\tfrac12 i\vec u_{\mathrm r}\cdot\vec e=iA$, and the two forms agree, since $-i\theta_{\mathrm{axr}}\tilde S=\theta_{\mathrm{axr}}A$.

**The two identities.** Every computation below follows from two identities, and from nothing else. At a unit real axis $\vec u_{\mathrm r}$ and its idempotent $\tilde\Pi_+(\vec u_{\mathrm r})$,

$$
\vec u_{\mathrm r}\tilde\Pi_+(\vec u_{\mathrm r})=\tilde\Pi_+(\vec u_{\mathrm r})\vec u_{\mathrm r}=-i\tilde\Pi_+(\vec u_{\mathrm r}),
\qquad
[\tfrac12\vec u_{\mathrm r},\vec v]=\vec u_{\mathrm r}\times\vec v\quad(\vec v\in\mathfrak{k}).
$$

The first holds in one line: $\tilde\Pi_+$ is a polynomial in $\vec u_{\mathrm r}$, so the two commute, and $\vec u_{\mathrm r}\tilde\Pi_+=\tfrac12\bigl(\vec u_{\mathrm r}+i\vec u_{\mathrm r}^2\bigr)=\tfrac12\bigl(\vec u_{\mathrm r}-ie_t\bigr)=-i\tilde\Pi_+$. The second is the quaternion product rule $\vec u\vec v=-\vec u\cdot\vec v+\vec u\times\vec v$, applied to the difference $\vec u\vec v-\vec v\vec u$. Both are identities at the general axis: no coordinate is chosen, and no array is printed. The two display the whole method — the axis multiplied into the idempotent gives the scalar $-i$, and the commutator with the axis gives the cross product. One carrier is read from the first, the other from the second.

**Definition (weights and spectrum).** Let $W$ be a carrier with action $\varrho$ on the real space $V_W$. The **weights** of $W$ are the real numbers $\lambda$ such that $i\lambda$ is an eigenvalue of $\varrho(A(\vec u_{\mathrm r}))$ on $V_W$, each counted with its multiplicity. The **spectrum** is the list of weights.

**Remark (the weights come in pairs).** The operator is real, so its eigenvalues are either real or come in conjugate pairs, and the eigenvalues are purely imaginary on the three carriers. A weight $\lambda\ne0$ therefore occurs together with $-\lambda$ and with the same multiplicity, and $0$ may occur alone. This is why every spectrum below is symmetric about zero, and the symmetry is read off the reality of the operator rather than checked case by case.

**Lemma (the weights are real).** On each of the three carriers the eigenvalues of $\varrho(A(\vec u_{\mathrm r}))$ are purely imaginary, so the weights are real.

*Proof.* For the trivial action the operator is zero. For the adjoint action the operator is the cross product with the axis, by the second identity, and the cross product annihilates $\vec u_{\mathrm r}$ and turns the perpendicular plane by a quarter turn: with an oriented orthonormal pair $\vec u_2,\vec u_3$ completing the axis so that $\vec u_{\mathrm r}\times\vec u_2=\vec u_3$, it sends $\vec u_2\pm i\vec u_3$ to $\mp i(\vec u_2\pm i\vec u_3)$. The eigenvalues are therefore $0,-i,+i$. For the spinor action the operator acts on the plane as the complex scalar $-\tfrac i2$, by the first identity, so its eigenvalues are that scalar and its conjugate, $-\tfrac i2$ and $+\tfrac i2$. Both operators are real-linear, so both spectra are symmetric under conjugation and both are purely imaginary.

**Lemma (the weights do not depend on the axis).** For two unit real axes $\vec u_{\mathrm r}$ and $\vec u_{\mathrm r}'$ the operators $\varrho(A(\vec u_{\mathrm r}))$ and $\varrho(A(\vec u_{\mathrm r}'))$ are similar, hence have the same spectrum with the same multiplicities.

*Proof.* Since $Sp(1)\to SO(\mathfrak{k})$ is onto, there is a rotor $\tilde g$ with $\operatorname{Ad}_{\tilde g}\vec u_{\mathrm r}=\vec u_{\mathrm r}'$. The generator is equivariant, $A(\vec u_{\mathrm r}')=\operatorname{Ad}_{\tilde g}\bigl(A(\vec u_{\mathrm r})\bigr)$, because $\operatorname{Ad}$ is real linear and carries the axis to the axis. A representation intertwines the conjugation with itself,

$$
\varrho(\operatorname{Ad}_{\tilde g}X)=\varrho(\tilde g)\varrho(X)\varrho(\tilde g)^{-1},
$$

for both the spinor and the adjoint action, as checked in the appendix. The two operators are therefore similar.

**Definition (spin).** The **spin** of a carrier is

$$
s=\max\operatorname{spec}W,
$$

the largest weight, with $s=0$ for the spectrum $\{0\}$. The definition is well posed by the two lemmas: the weights are real, so the maximum exists, and they do not depend on the axis, so the number depends on the carrier and not on a choice. It agrees with the definition by dimension, the identity $2s+1=\dim_\mathbb{R}$ of *The Spin Table*: on an irreducible carrier the weights are $s,s-1,\dots,-s$, so there are $2s+1$ of them.

## The Slot: the Label $\tfrac12$

**The factor.** The series of *The Clebsch–Gordan Decomposition* is the square of one carrier, and the carrier that is squared is the slot on which the algebra acts by left multiplication. Its label is $\tfrac12$, and the computation below reads it from the Casimir of the left-regular generators alone: three operators and one sum of squares. What the computation identifies is the label of a factor, not a summand of the algebra.

**The rotor group.** The rotors form $Sp(1)$, the unit sphere of the quaternion layer,

$$
S^3=\{q\in\mathbb{H}:N(q)=1\},
$$

of real dimension $3$, and the map to $SO(\mathfrak{k})$ is onto with kernel $\{\pm e_t\}$. The group is $S^3$. Every spin below is the label of a carrier of this group: the rotor acts on space by the two-sided product and one-sidedly on the carrier, and the label is read from that action. The group is $S^3=\mathrm{Spin}(3)$, the unit sphere of the real form, and every group of operators used below is an image of it under one of its actions. Nothing else enters, and every computation below is a computation about real left multiplication on the quaternion layer.

**The left-regular generators.** Read the quaternion layer $\mathbb{H}=\mathbb{R}e_t\oplus\mathbb{R}\vec e_x\oplus\mathbb{R}\vec e_y\oplus\mathbb{R}\vec e_z$ as a real space of dimension $4$. Left multiplication by $\vec e_k$ is the real operator $L_k:=L_{\vec e_k}$, and the three of them satisfy

$$
L_k^2=-\mathrm{I}_4,\qquad [L_x,L_y]=2L_z\quad\text{and cyclically.}
$$

The first identity is $\vec e_k^2=-e_t$ read in the display: the square of a basis vector is minus the identity of the algebra, so its left multiplication squares to minus the identity of the space. The second is $\vec e_x\vec e_y-\vec e_y\vec e_x=2\vec e_z$ read in the display, which is the quaternion rule $\vec u\vec v=-\vec u\cdot\vec v+\vec u\times\vec v$ applied to two different coordinate axes.

**The normalization.** The generators of the action are the halved ones, $A_k=\tfrac12\vec e_k$, the same element $A(\vec u_{\mathrm r})$ of *The Rotation Action* at the coordinate axes, and with them the bracket is the standard one,

$$
[A_x,A_y]=A_z\quad\text{and cyclically},\qquad L_k=2\,\varrho_{\mathrm{def}}(A_k).
$$

**The Casimir.** The **Casimir** of the single rotor is the sum of squares of the three generators. On the quaternion layer,

$$
\sum_k L_k^2=-3\,\mathrm{I}_4,\qquad \sum_k A_k^2=\tfrac14\sum_kL_k^2=-\tfrac34\,\mathrm{I}_4 .
$$

The first is the sum of three copies of $-\mathrm{I}_4$, by $L_k^2=-\mathrm{I}_4$. The second follows from it by the factor $4$ in $L_k=2A_k$.

**Proposition (the Casimir of an irreducible carrier).** On a carrier of spin $s$ the Casimir is the scalar

$$
\sum_kA_k^2=-s(s+1),
$$

the sign being that of the antisymmetric generators. The values on the three carriers are computed in *The Quadratic Element*, where the element $C=\sum_k\tilde S_k^{2}$ with $\tilde S_k=iA_k$ is shown to take the values $0,\tfrac34,2$, so that $\sum_kA_k^{2}=-C$ takes the values $0,-\tfrac34,-2$; these are $-s(s+1)$ at $s=0,\tfrac12,1$.

**Theorem (a single rotor carries spin $\tfrac12$).** The quaternion layer carries the spin $\tfrac12$, and the number is read from the Casimir of the left-regular generators alone.

*Proof.* By the computation above the Casimir on the layer is the scalar $-\tfrac34\mathrm{I}_4$. By the proposition a carrier of spin $s$ has the scalar $-s(s+1)$, so

$$
s(s+1)=\tfrac34\quad\Longrightarrow\quad s=\tfrac12,
$$

the other root being $s=-\tfrac32$ and the spin being taken non-negative. ∎

**Remark (the type, not the copy).** The layer of real dimension $4$ is not irreducible: its weight string is $\pm\tfrac12$ each with multiplicity two, so it is two copies of the plane, by the remark on repeated weights in *The Criterion*. The Casimir does not notice, because it is a sum of squares of operators and acts as one scalar on both copies. What it reads is therefore the type and not the copy, which is exactly what a spin label is.

**Remark (the two readings agree).** The Casimir gives $s=\tfrac12$. The largest weight gives $s=\tfrac12$ as well: on the plane the operator $\varrho\bigl(A(\vec u_{\mathrm r})\bigr)$ is the scalar $-\tfrac i2$, so the weights are $\pm\tfrac12$, as computed in *The Spinor Plane*. The two readings are of one number, one from a sum of squares and one from a spectrum, and the plane is where the second is read.

**Remark (what the generators do not give).** The three generators $L_k$ act on one carrier, that carrier is of one type, and the type is $\tfrac12$. No other spin is obtained by squaring them, halving them or combining them, because a combination of operators on one carrier is again an operator on that carrier. Another spin needs another carrier, and the next section produces one from a second factor.

## The Product: the Labels $0$ and $1$

The two integer labels are already placed on subspaces, $\mathbb{R}e_t$ and $\mathfrak{k}$, by the projectors. This section reads them a second time, on a different carrier and from a different operator: the tensor square of two slots, with the total Casimir of a pair acting on two sides. The agreement of the two readings is the check on the series.

**Why the two-sided form is forced.** Let $X$ be an element and $L_X$ left multiplication. Then

$$
L_X(YZ)=XYZ,\qquad L_X(Y)L_X(Z)=XYXZ,
$$

so $L_X$ is multiplicative as an operator on the algebra exactly when $X=e_t$. One factor on one side is therefore not an action by automorphisms, and the count of factors is the whole obstruction: the left side of the first display carries one copy of $X$ and the left side of the second carries two. A two-sided product carries one copy on each side, and it is multiplicative.

**The two two-sided operators.** Two of them occur, and they differ in the second factor:

$$
\Theta_Q(X)=QXQ^{*},\qquad \Phi_Q(X)=QXQ^{\natural}.
$$

Both are multiplicative on the rotors. That is the content of *A.4*, and it is stated there once: for invertible $Q$,

$$
\Phi_Q=N(Q)\operatorname{Ad}_Q,\qquad \Theta_Q=\operatorname{Ad}_Q\iff Q^{*}Q\ \text{is central},
$$

and on the group of invertibles, $Q^{*}=Q^{-1}$, both reduce to conjugation by the inverse. The second equivalence is the one that matters here: $\Theta_Q$ is conjugation by the inverse exactly on $G$, and it is not multiplicative off it.

**The rotor and the boost.** The two types of element behave differently, and the difference is read off $N$ and the two conjugations.

For a rotor $\tilde u_{\mathrm r}$, the coefficients are real, so $\tilde u_{\mathrm r}^{*}=\tilde u_{\mathrm r}^{\natural}=\tilde u_{\mathrm r}^{-1}$ and $N(\tilde u_{\mathrm r})=1$. Both operators are the same operator, and each is conjugation by the inverse.

For a boost $\tilde U_{\mathrm b}=\cosh\tfrac\phi2\,e_t+i\sinh\tfrac\phi2\,\vec n$ with real unit $\vec n$, the element is Hermitian, $\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}$, and it is not the inverse of itself. But its norm is

$$
N(\tilde U_{\mathrm b})=\cosh^{2}\tfrac\phi2-\sinh^{2}\tfrac\phi2=1,
$$

because $(i\vec n)^{2}=+e_t$ and the two squares therefore subtract. So $\tilde U_{\mathrm b}^{\natural}=\tilde U_{\mathrm b}^{-1}$, and the operator $\Phi$ is conjugation by the inverse on the boost sector as well. The operator that fails there is $\Theta$: its second factor is $\tilde U_{\mathrm b}$ and not $\tilde U_{\mathrm b}^{-1}$, and $\tilde U_{\mathrm b}^{*}\tilde U_{\mathrm b}=\tilde U_{\mathrm b}^{2}$ is not central, so $\Theta_{\tilde U_{\mathrm b}}$ is not multiplicative at all.

The sentence to keep is this. The two-sided form is compulsory, and it is conjugation by the inverse exactly on the surface where the mark in use agrees with the inverse. On the rotor sphere the two marks coincide. On the boost sector they separate, and it is the star that separates them.

**The pair.** A pair of operators acting on two sides is an element of $S^3_L\times S^3_R$, acting by

$$
(q,p):X\longmapsto qXp .
$$

Two carriers occur, and they are different objects.

The two-sided action on the algebra itself is the pair acting on $\mathbb{H}$, of real dimension $4$. Since right multiplication is an anti-homomorphism, $R_qR_p=R_{pq}$, the diagonal generator is the difference of the two families,

$$
A_k^{\mathrm{tot}}=A_k-A'_k,\qquad A'_k=\tfrac12R_{\vec e_k},
$$

and it satisfies the standard bracket, because the minus sign of the right bracket cancels the minus sign of the difference.

Two independent systems give the tensor carrier $\mathbb{H}\otimes\mathbb{H}$, of real dimension $16$, with the generators

$$
A_k\otimes\mathrm{I}+\mathrm{I}\otimes A_k,
$$

by the Leibniz rule of a derivation. This is the carrier of two rotors, each in its own layer.

**The two Casimirs.** Each factor has its own Casimir, and each is the value of a single rotor:

$$
\sum_kA_k^2=-\tfrac34\,\mathrm{I},\qquad \sum_kA_k^{\prime2}=-\tfrac34\,\mathrm{I}.
$$

The two families commute, since left and right multiplication commute, so the two Casimirs commute and each is a scalar. Each factor carries the label $\tfrac12$, by *The Slot*.

**The total Casimir.** The Casimir of the pair is the sum of squares of the total generators,

$$
\mathbf{A}^2_{\mathrm{tot}}:=\sum_k\bigl(A_k^{\mathrm{tot}}\bigr)^2 .
$$

**The addition rule.** The carriers of the rotor group are labelled by

$$
j\in\tfrac12\mathbb{Z}_{\ge0}=\{0,\tfrac12,1,\tfrac32,2,\dots\},
$$

the carrier of label $j$ having spin $j$, that is Casimir $-j(j+1)$ and complex dimension $2j+1$. Two labels combine by

$$
j_{\mathrm{tot}}\in\bigl\{|j_1-j_2|,\;\dots,\;j_1+j_2\bigr\}.
$$

This is a theorem about the carriers of $S^3$: the product of two irreducible carriers is a sum of irreducible carriers, and the labels that occur are exactly those in the display, each once. It is a statement about the group and its modules. It is not a table of coefficients, and no coefficient is computed or needed in this article.

**Theorem (the pair carries spin $0$ or $1$).** Two rotors carry the spins $0$ and $1$, and no other.

*Proof.* By *The Slot* each factor carries $j=\tfrac12$. The addition rule with $j_1=j_2=\tfrac12$ gives

$$
j_{\mathrm{tot}}\in\{0,\,1\}. \qquad\blacksquare
$$

**The Casimir check.** The conclusion is confirmed by squaring, and the confirmation is a computation and not a restatement. On a summand of total spin $j$ the total Casimir is the scalar $-j(j+1)$, so the two values are

$$
j=0\ \Rightarrow\ \mathbf{A}^2_{\mathrm{tot}}=0,\qquad j=1\ \Rightarrow\ \mathbf{A}^2_{\mathrm{tot}}=-2 .
$$

On the tensor carrier of real dimension $16$ the spectrum of $\mathbf{A}^2_{\mathrm{tot}}$ is $0$ with multiplicity $4$ and $-2$ with multiplicity $12$, and nothing else. On the two-sided carrier of real dimension $4$ it is $0$ once and $-2$ three times. The equation $-j(j+1)\in\{0,-2\}$ with $j\ge0$ has exactly the solutions $j=0$ and $j=1$.

**Remark (the multiplicities are dimensions).** The two spectra are consistent with the two carriers. In the two-sided case, $1+3=4$, one copy of the singlet and one of the triplet. In the tensor case, $4\cdot1+4\cdot3=16$, four copies of each, because two rotors each in a layer of types $2$ give four copies of the pair of types. The multiplicities differ and the labels do not, and the labels are what the spin is.

**Remark (no spin $2$).** The pair gives $0$ and $1$ and nothing else, and the arithmetic says why. Spin $2$ would need $j_1+j_2=2$ with both labels from halves present in the product, which needs four factors of $\tfrac12$, or the product $\mathfrak{k}\otimes\mathfrak{k}$ of two vector parts, whose labels are $1\otimes1=0\oplus1\oplus2$. Neither is the pair acting on two sides. A pair is two factors, and two halves reach $1$.

**Remark (the check is not circular).** The addition rule is a theorem about the carriers of $S^3$, stated before any array is written. The total Casimir is defined independently, as a sum of squares of explicit operators. The equation $-j(j+1)$ then identifies the eigenvalues $0$ and $-2$ with the labels $0$ and $1$. Neither step uses the other, and their agreement is the content of the check.

**The three spins.** The slot and the product together give

$$
s\in\bigl\{0,\;\tfrac12,\;1\bigr\},
$$

with $s=\tfrac12$ from one rotor and $s\in\{0,1\}$ from a pair. These three are the input of *The Carriers*: for each of them, the next section names the subspace of $\mathbb{B}$ of real dimension $2s+1$ that carries it.

## The Criterion

The slot and the product fixed the three spins. What is still missing is a test, since irreducibility is the property that the dimension cannot supply: a space of the right dimension can be reducible, and the question of which subspace carries a given spin is a question of irreducibility.

Irreducibility is the one property of a carrier that no dimension can supply, and it is normally checked case by case. One test covers every module that arises here, and it is worth stating on its own, because it turns irreducibility into a reading of the spectrum.

**Definition (simple and spaced).** A string of weights is **simple** when no value occurs twice, and **spaced by one** when consecutive values differ by $1$.

**Theorem (irreducibility from the string).** Let $V$ be a finite-dimensional complex module for the rotation algebra, and suppose that the weights of $\varrho(A(\vec u_{\mathrm r}))$ on $V$ are simple and spaced by one, the largest being $s$. Then $V$ is irreducible, $s$ is its highest weight, and $\dim_\mathbb{C}V=2s+1$.

*Proof.* The rotation group is compact, so $V$ is a direct sum of irreducible submodules, by the averaging argument of *Representations of Groups*, which needs no finiteness and no array. On an irreducible submodule the weights form one string, simple, spaced by one, and symmetric about zero: the submodule is generated by an eigenvector of the largest weight, and the algebra acts on it through $\varrho(A(\vec u_{\mathrm r}))$ together with the two ladder elements $\tilde S_\pm=\tilde S(\vec u_2)\pm i\tilde S(\vec u_3)$ built on an oriented orthonormal pair completing the axis. Since $\vec u_2\times\vec u_3=\vec u_{\mathrm r}$, these satisfy

$$
\bigl[\varrho(\tilde S(\vec u_{\mathrm r})),\varrho(\tilde S_\pm)\bigr]=\pm\varrho(\tilde S_\pm),
$$

so on an eigenvector of weight $\lambda$ they produce an eigenvector of weight $\lambda\pm1$, or zero when the string ends. A string that is symmetric about zero and spaced by one contains the value $0$, once. The multiplicity of the weight $0$ on $V$ is therefore the number of its irreducible summands, and the hypothesis makes that number one.

**Corollary (the three carriers pass the test).** The strings $\{0\}$, $\{\pm\tfrac12\}$ and $\{\pm1,0\}$ are simple and spaced by one, with largest values $0$, $\tfrac12$ and $1$. Each of the three carriers is therefore irreducible, and after complexification its dimension is $2s+1$, which is $1$, $2$ and $3$.

**Remark (the string carries the dimension and the highest weight).** The largest weight is read from the string, and the length of the string is the complex dimension. So a carrier is determined in both respects by its spectrum, and the identity $2s+1=\dim$ of *The Spin Table* is a relation between two readings of one string rather than between two independent numbers.

**Remark (a repeated weight is a direct sum).** Under left multiplication on the whole algebra the weights are $\pm\tfrac12$ each with multiplicity two, and $\mathbb{B}=S_+\oplus S_-$ is a sum of two carriers of one type. The repetition is the multiplicity of a type, not a second type, and this is why the criterion is a statement about multiplicities and not only about the set of values.

## The Carriers

The series gives two summands of the algebra, and the two summands are complex subspaces already: $P_0\mathbb{B}=\mathbb{C}e_t$ with the label $0$, and $P_1\mathbb{B}=\mathbb{C}\mathfrak{k}$ with the label $1$. The carriers are their real forms, the line $\mathbb{R}e_t$ and the vector part $\mathfrak{k}$. The third carrier is the slot, and a slot is a factor and not a subspace: it has to be realized inside the algebra, and the realization is a minimal left ideal, that is, a complex line built from an idempotent at an axis. So the article lists three carriers where the series gives two summands, and the difference between the two counts is the difference between a summand and a factor.

Each of the three is a real subspace of $\mathbb{B}$ of dimension $2s+1$, invariant and irreducible under one of the actions: the spin $s=0$ is carried by the fixed line $\mathbb{R}e_t$, the spin $s=\tfrac12$ by the spinor plane $\Sigma$, the spin $s=1$ by the vector part $\mathfrak{k}$. The assignment is forced by the dimension $2s+1$ and by the natural action of $\mathbb{B}$ on itself — trivial, left multiplication, conjugation — and the criterion of the preceding section is what makes each of the three irreducible and not merely of the right size.

The three carriers are stated in the order of their spins, $0$, $\tfrac12$, $1$, which is also the order line, plane, vector part: the two summands of the series first, the factor after. Each is described by the same template: the subspace, the action, the operator, the spectrum, the dimension, the spin, and the sign of a full turn.

### The Fixed Line

This is the carrier of $s=0$.

**The subspace.** The real line $\mathbb{R}e_t$, of real dimension $1$.

**The action.** The conjugation acts trivially, because $ue_tu^{*}=e_t$ for every invertible $u$. The line is fixed pointwise, and it is the carrier of the trivial action.

**The operator.** $\varrho(A)=0$.

**The spectrum.** $\{0\}$, with multiplicity $1$.

**Dimension, spin, full turn.** $\dim_\mathbb{R}=1$, $s=0$, and $2s+1=1$. The full turn has operator $\varrho(-e_t)=\mathrm{id}$, so the sign is $+1$.

### The Spinor Plane

This is the carrier of $s=\tfrac12$. Its weights are $\pm\tfrac12$, matching the Casimir of the slot computed in *The Slot*.

**The subspace.** Fix a unit real axis $\vec u_{\mathrm r}$ and the idempotent

$$
\tilde\Pi_+(\vec u_{\mathrm r})=\tfrac12\bigl(e_t+i\vec u_{\mathrm r}\bigr),\qquad \tilde\Pi_+^2=\tilde\Pi_+ .
$$

The plane is the complex line spanned by it, read as a real plane:

$$
\Sigma(\vec u_{\mathrm r})=\mathbb{C}\tilde\Pi_+(\vec u_{\mathrm r})=\mathbb{R}\bigl\{\tilde\Pi_+,\ i\tilde\Pi_+\bigr\},
$$

of real dimension $2$, with the real basis $p_1=\tilde\Pi_+(\vec u_{\mathrm r})$ and $p_2=i\tilde\Pi_+(\vec u_{\mathrm r})$. The plane lies in the left ideal $S_+=\mathbb{B}\tilde\Pi_+$, so $L_X\Sigma\subseteq S_+$ for every $X$, and it carries the one-sided action. The axis is a parameter of the family and not a datum of the algebra.

**The action.** Left multiplication, $\varrho_{\mathrm{def}}(X)=L_X$. On the plane the rotor acts by a phase of half its angle, and this is where the half-integer arises. By the first identity, $\vec u_{\mathrm r}\tilde\Pi_+=-i\tilde\Pi_+$, so for the rotor $\tilde u_{\mathrm r}=\cos\tfrac{\theta_{\mathrm{axr}}}{2}\,e_t+\sin\tfrac{\theta_{\mathrm{axr}}}{2}\,\vec u_{\mathrm r}$,

$$
\tilde u_{\mathrm r}\tilde\Pi_+(\vec u_{\mathrm r})=\Bigl(\cos\tfrac{\theta_{\mathrm{axr}}}{2}-i\sin\tfrac{\theta_{\mathrm{axr}}}{2}\Bigr)\tilde\Pi_+(\vec u_{\mathrm r})=e^{-i\theta_{\mathrm{axr}}/2}\,\tilde\Pi_+(\vec u_{\mathrm r}).
$$

The rotor multiplies the plane by the phase $e^{-i\theta_{\mathrm{axr}}/2}$, at every axis and by one line of algebra: the half angle is not inserted, it is what the identity gives.

**The operator.** Since $\tilde u_{\mathrm r}=\exp\bigl(\theta_{\mathrm{axr}}A(\vec u_{\mathrm r})\bigr)$ and the phase in the display is $e^{-i\theta_{\mathrm{axr}}/2}$, the operator $L_{A(\vec u_{\mathrm r})}$ acts on the plane as the complex scalar $-\tfrac i2$. It is complex-linear, with no other component; as a real operator on the two real dimensions its eigenvalues are the scalar and its conjugate, $-\tfrac i2$ and $+\tfrac i2$.

**The spectrum.** $\{+\tfrac12,-\tfrac12\}$, with multiplicities $1,1$.

**Dimension, spin, full turn.** $\dim_\mathbb{R}=2$, $s=\tfrac12$, and $2s+1=2$. The full turn is $\theta_{\mathrm{axr}}=2\pi$, and the rotor acts by $e^{-i\pi}=-1$: a full rotation of space is a half turn of the plane. The sign is $-1$, and here it is visible in the plane itself, without any complexification.

**Remark (the plane is not invariant under the full group).** The plane is carried by the rotations about its own axis and by no others: left multiplication by the transverse axis $\vec u_2$ sends $\tilde\Pi_+(\vec u_{\mathrm r})$ out of $\Sigma(\vec u_{\mathrm r})$, and the smallest real subspace of $\mathbb{B}$ that contains $\Sigma$ and is invariant under the whole group has real dimension $4$. The carrier is therefore a carrier for the circle of rotations about the axis. Why this is so, and what it costs, is *The Closure of a Carrier*.

### The Vector Part

This is the carrier of $s=1$. Its weights are $\pm1,0$, matching the pair spin of *The Product* and the summand $V_1$ of the series.

**The subspace.** $\mathfrak{k}=\mathbb{R}\vec e_x\oplus\mathbb{R}\vec e_y\oplus\mathbb{R}\vec e_z$, of real dimension $3$.

**The action.** The conjugation, $\varrho_{\mathrm{ad}}(u)=\operatorname{Ad}_u$. It preserves $\mathfrak{k}$ and it preserves the form, so it is a representation into $SO(\mathfrak{k})$; the map is onto with kernel the central circle $\{\lambda e_t:\lambda\bar\lambda=1\}$, which is $\{\pm e_t\}$ on the rotors $Sp(1)$.

**The operator.** By the second identity the operator is the cross product with the axis,

$$
\varrho_{\mathrm{ad}}\bigl(A(\vec u_{\mathrm r})\bigr)(\vec v)=\vec u_{\mathrm r}\times\vec v ,
$$

which is the zero of $\vec u_{\mathrm r}$ and a quarter turn of the plane perpendicular to it. With the oriented pair $\vec u_2,\vec u_3$ completing the axis as before, it sends $\vec u_2\pm i\vec u_3$ to $\mp i(\vec u_2\pm i\vec u_3)$, so the eigenvalues are $-i$, $+i$ and $0$.

**The spectrum.** $\{+1,0,-1\}$, with multiplicities $1,1,1$.

**Dimension, spin, full turn.** $\dim_\mathbb{R}=3$, $s=1$, and $2s+1=3$. The full turn is a rotation of space through $2\pi$, which is the identity on $\mathfrak{k}$, so the sign is $+1$.

**Remark (why the two spectra differ by a factor of two).** The generator is the same real element $\tfrac12\vec u_{\mathrm r}$ in both cases, and the two identities say why the spectra differ. On the vector part the operator is the commutator with $\tfrac12\vec u_{\mathrm r}$, which equals the cross product with the whole axis $\vec u_{\mathrm r}$: the two sides of the product both contribute, and the quarter turn of the cross product gives the eigenvalues $\mp i$, hence the weights $\pm1$. On the plane the operator is a single multiplication by one half of the axis, which gives the scalar $-\tfrac i2$, hence the weights $\pm\tfrac12$. The commutator consumes the axis twice and the multiplication consumes it once, and that is the factor of two.

### The Summands and the Factor

Two of the three carriers are summands of the series and the third is the factor that the series squares, so the three cannot be the pieces of one decomposition: a factor is not a piece of the product it forms. The arithmetic agrees with this and says more. The two summands add to $1+3=4$, which is the complex dimension of the algebra and the content of $3+1=4$; the slot contributes the complex dimension $2$ to the product, and $2$ is nowhere in the sum. Counting all three, $1+2+3=6$, against a real dimension of $8$, since the complex dimensions double in the real reading.

The two summands are canonical subspaces, and neither depends on an axis. The slot is realized by a minimal left ideal, and every minimal left ideal depends on an axis. This is the sharp form of the difference, and it is the reason the closure of the slot needs two steps where the closure of each summand needs one.

Two other decompositions of the algebra exist, in two different categories, and neither is the Clebsch–Gordan one.

From the star, $\mathbb{B}=\mathbb{B}_\Phi\oplus\mathbb{B}_\Psi$, the anti-Hermitian and Hermitian halves, of real dimensions $4+4=8$; the first contains the vector part.

From the idempotent, $\mathbb{B}=S_+\oplus S_-$ as left modules, where $S_\pm=\mathbb{B}\tilde\Pi_\pm$, and each summand has real dimension $4$.

The spinor plane occurs in neither as a summand: it is a complex line inside $S_+$, and not a left module over the whole algebra. The line, the plane and the vector part are three carriers, not three summands.

## Three and No More

The series produces the labels $0$ and $1$ on the two summands, and the slot produces the label $\tfrac12$; the two sections above read the three numbers a second time, from Casimir sums. This section proves that the list is complete: the biquaternion algebra carries no fourth carrier.

The proof does not use the series, and this is deliberate. It classifies the two actions the algebra has on itself: the multiplication, which gives one simple module, and the conjugation, which gives two. The series and the classification agree, and their agreement is the strongest form of the statement.

The proof has one half for each action. Both halves use one form, and the form is not the trace form: it is the polar form of the norm.

**The form.** For elements $X,Y$ put

$$
\beta(X,Y)=\tfrac12\bigl(N(X+Y)-N(X)-N(Y)\bigr),
$$

so that $N(X+Y)=N(X)+N(Y)+2\beta(X,Y)$. In the four complex coordinates it is

$$
\beta(X,Y)=Q_t(X)Q_t(Y)+Q_x(X)Q_x(Y)+Q_y(X)Q_y(Y)+Q_z(X)Q_z(Y),
$$

which is complex-bilinear, symmetric and non-degenerate, and which reads the scalar part on the unit:

$$
\beta(e_t,Y)=Q_t(Y),\qquad \beta(ie_t,Y)=i\,Q_t(Y).
$$

*Proof.* The coordinate display is the polar form of the sum of four squares, and the two evaluations are that display at $X=e_t$ and at $X=ie_t$, whose coordinates are $(1,0,0,0)$ and $(i,0,0,0)$.

**Lemma (the form is invariant).** For an invertible element $u$ and elements $X,Y$, $\beta(uXu^{*},uYu^{*})=\beta(X,Y)$.

*Proof.* The norm is multiplicative and $N(uu^{*})=N(e_t)=1$, so $N(uZu^{*})=N(Z)$ for every $Z$. Apply this to $Z=X+Y$, to $Z=X$ and to $Z=Y$ in the definition of $\beta$.

**Theorem (the multiplication carriers).** Up to isomorphism there is one simple left $\mathbb{B}$-module, of complex dimension $2$: every minimal left ideal is a copy of it, and every left ideal is a sum of copies.

*Proof.* A minimal left ideal is $S=\mathbb{B}e$ for a primitive idempotent $e$, and two such ideals are isomorphic as left modules whenever their idempotents are conjugate, which for the full endomorphism algebra is always. Let $W$ be a simple left module. It is a quotient of the regular module $\mathbb{B}$, hence $\mathbb{B}/M$ for a maximal left ideal $M$, and every such quotient is a minimal left ideal up to a sum of minimal ones. All the minimal ones are copies of one module, so the simple module is unique up to isomorphism. Its complex dimension is $2$, since $\mathbb{B}$ is the algebra of endomorphisms of a two-dimensional complex space and the minimal left ideals are its columns.

**Theorem (the conjugation carriers).** Up to isomorphism there are exactly two: the centre, the trivial module of complex dimension $1$, and the scalar-free part, the adjoint module of complex dimension $3$.

*Proof.* Let $W\subseteq\mathbb{B}$ be nonzero and invariant under $\operatorname{Ad}_u$ for every invertible $u$. Since $\beta(e_t,Y)=Q_t(Y)$, the orthogonal complement of the centre is the scalar-free part,

$$
\mathbb{B}=\mathbb{B}_C\perp\mathbb{B}_V,\qquad \mathbb{B}_V=\{X:Q_t(X)=0\},
$$

and both summands are invariant: the centre is fixed pointwise, and the scalar-free part is its orthogonal complement, invariant because $\beta$ is. The group $G$ is compact, so the average of $uXu^{*}$ over $u\in G$ is defined; it is a map of modules, it is the identity on $\mathbb{B}_C$ and zero on $\mathbb{B}_V$, and applied to an element of $W$ it returns an element of $W$, because $W$ is invariant and linear. The average is the projection onto the fixed space, by the argument of *Representations of Groups* that gives complete reducibility for compact groups. So each $X\in W$ splits as $X=\pi X+(X-\pi X)$ with both terms in $W$, and

$$
W=(W\cap\mathbb{B}_C)\oplus(W\cap\mathbb{B}_V).
$$

An irreducible $W$ is therefore one of these two summands. The centre is a complex line, hence irreducible. The traceless part is irreducible by the criterion: its weights at the axis are $\{+1,0,-1\}$, simple and spaced by one. Two summands, both irreducible, and no third.

**Corollary (three and not four).** Up to isomorphism the carriers of $\mathbb{B}$ are three: the trivial module of complex dimension $1$, the module of a minimal left ideal of complex dimension $2$, and the adjoint module of complex dimension $3$. One comes from multiplication and two from conjugation, and there is no fourth, because a carrier is irreducible for one of the two actions and both actions are now classified.

**Remark (what is counted).** The count is a count for the two actions the algebra carries on itself: multiplication, which is an action of the algebra, and conjugation, which is an action of the group of invertibles by automorphisms. No third action is used anywhere in this group of articles. Left and right multiplication give the same types, because the algebra is a full endomorphism algebra, and the derived form of the conjugation is the bracket.

**Remark (copies are not types).** $S_+$ and $S_-$ are two carriers of one type, not two types. The multiplicity is a property of the algebra as a module, not a count of types, and it is the reason the weight string of the whole algebra repeats.

## The Spin Table

| carrier | $\dim_\mathbb{R}$ | action | $\varrho\bigl(A(\vec u_{\mathrm r})\bigr)$ | weights | $s$ | $2s+1$ | full turn |
| --- | --- | --- | --- | --- | --- | --- | --- |
| fixed line $\mathbb{R}e_t$ | $1$ | trivial | $0$ | $\{0\}$ | $0$ | $1$ | $+1$ |
| spinor plane $\Sigma$ | $2$ | $L_u$ | the scalar $-\tfrac i2$ | $\{\pm\tfrac12\}$ | $\tfrac12$ | $2$ | $-1$ |
| vector part $\mathfrak{k}$ | $3$ | $\operatorname{Ad}_u$ | $\vec u_{\mathrm r}\times$ | $\{\pm1,0\}$ | $1$ | $3$ | $+1$ |

**Proposition ($2s+1=\dim_\mathbb{R}$).** The identity holds for each of the three carriers: $1=2\cdot0+1$, $2=2\cdot\tfrac12+1$, $3=2\cdot1+1$. It is checked in the three cases, and since the list of carriers is complete the check covers every carrier of $\mathbb{B}$. It is not a numerical coincidence: the dimension and the largest weight are the same kind of number here, both read from the same real space.

**Theorem (the full turn).** The operator of a full rotation, $\varrho(-e_t)$, is $+1$ on the line and on the vector part and $-1$ on the plane; that is, its value is $(-1)^{2s}$.

*Proof.* Let $\lambda$ run over the weights, and let $\varrho(A)$ be the operator of the generator. The eigenvalues of $\varrho(A)$ are $i\lambda$, so the eigenvalues of $\varrho(\tilde u_{\mathrm r})=\exp(\theta_{\mathrm{axr}}\varrho(A))$ are $e^{i\theta_{\mathrm{axr}}\lambda}$. At $\theta_{\mathrm{axr}}=2\pi$ the rotor is $-e_t$ and the eigenvalues are $e^{2\pi i\lambda}$. For $\lambda\in\{0,\pm1\}$ this is $+1$; for $\lambda=\pm\tfrac12$ it is $e^{\pm i\pi}=-1$. On each carrier all the eigenvalues are equal and the operator is diagonalisable, so the operator is that single value times the identity: $+1$ on the line and on the vector part, $-1$ on the plane.

**Remark (the reading of the sign).** The sign is not a defect of the computation. On the plane $\varrho$ is defined on the rotors, and a full rotation has the rotor $-e_t$, which is not the identity of the rotor group; the value $-1$ shows that the action does not descend to the rotation group. The half-integer carrier is therefore an action of the double cover, and the integer carriers are actions of the rotation group. On the plane the statement is geometric: a full rotation of space is a half turn of the plane.

**Remark (the spacing).** The three spectra are symmetric about zero, spaced by $1$, and of length $2s+1$: $0$ alone, then $+\tfrac12$ and $-\tfrac12$, then $+1,0,-1$ in steps of $1$. The spacing is checked in the three cases; it is not assumed.

## The Quadratic Element

The same three numbers are values of one element of the algebra, and this is a second reading of them, independent of the dimension and of the string.

**Definition (the quadratic element).** With $\tilde S_k=\tfrac12 i\vec e_k$ for the three coordinate axes, the **quadratic element** is

$$
C=\tilde S_x^{2}+\tilde S_y^{2}+\tilde S_z^{2}.
$$

**Proposition (the value in the algebra).** $C=\tfrac34 e_t$.

*Proof.* $\tilde S_k^{2}=\tfrac14 i^{2}\vec e_k^{2}$, and $i^{2}=\vec e_k^{2}=-e_t$, so $\tilde S_k^{2}=\tfrac14 e_t$ and the three terms give $\tfrac34 e_t$. The value is central.

**Proposition (the values in the three modules).** Acting in the module of each carrier,

$$
C\big|_{\mathbb{B}_C}=0,\qquad C\big|_{S_\pm}=\tfrac34,\qquad C\big|_{\mathfrak{k}}=2 .
$$

*Proof.* On the centre the module is trivial, and $C$ is central, so it acts as the scalar $0$. On $S_\pm$ the action is left multiplication by the central $\tfrac34 e_t$, so it acts as the scalar $\tfrac34$. On $\mathfrak{k}$ the action is the bracket, and $\operatorname{ad}_{\tilde S_k}^{2}$ kills the axis $\vec e_k$ and fixes its orthogonal plane: from $[\vec e_x,\vec e_y]=2\vec e_z$ and $[\vec e_x,\vec e_z]=-2\vec e_y$ one has $\operatorname{ad}_{\vec e_x}^{2}\vec e_y=-4\vec e_y$ and $\operatorname{ad}_{\vec e_x}^{2}\vec e_z=-4\vec e_z$, and $\operatorname{ad}_{\tilde S_x}^{2}=-\tfrac14\operatorname{ad}_{\vec e_x}^{2}$ is therefore the identity on that plane. The three operators are the three coordinate projections, and their sum is $2$ on a three-dimensional space.

**Corollary (one polynomial, three carriers).** The three values are $s(s+1)$ at $s=0,\tfrac12,1$:

$$
0=0\cdot1,\qquad \tfrac34=\tfrac12\cdot\tfrac32,\qquad 2=1\cdot2 .
$$

**Remark (two elements, one scalar).** The element $C=\tfrac34e_t$ of the algebra and the element $\sum_k\tilde S_k\otimes\tilde S_k$ of the enveloping algebra are different objects, and they are not interchangeable. The first is central, so the adjoint action, which kills the centre, sends it to the operator $0$ on $\mathfrak{k}$: read with the algebra product, the quadratic element is $0$ on the adjoint carrier. The second is the composed operator, and it is $2$ there. The value attached to a carrier is the second, and the two agree only on $S_\pm$, where the module is the defining one and the product and the symmetrised product coincide.

**Remark (what the value does not determine).** The value $\lambda=s(s+1)$ is quadratic in $s$, so it determines $s$ only up to the other root, $s\mapsto-1-s$. The largest weight being non-negative fixes the choice here, and the values $0,\tfrac34,2$ are distinct, so on these three carriers there is no ambiguity left. In general the ambiguity is present, which is why the quadratic element is a reading of the highest weight and not a definition of it.

**Remark (what the polynomial does not prove).** The identity $2s+1=\dim_\mathbb{R}$ rests on the trichotomy and on the three computations, not on this element: the values $0,\tfrac34,2$ are consistent with the three spins, and consistency is not derivation. What the element adds is that the three numbers are the values on the three carriers of one invariant of the algebra, computed once and read three times.

## What the Construction Uses and Does Not Use

**The axis.** The axis is a parameter. The spectrum does not depend on it, by the lemma of *The Rotation Action*, and the spin therefore does not depend on it. The answer is a property of the carrier and not of a direction.

**The angle.** The spin is read from the generator at the identity, so no angle enters it. The angle enters once, at $\theta_{\mathrm{axr}}=2\pi$, in the theorem of the full turn. The halved angle of the rotor is not used to define the weights; it is the reason the exponent in the full turn is $2\pi\lambda$.

**The two conjugations.** The natural conjugation is used once, and everything it does is the Clebsch–Gordan split: it is complex-linear and involutive, so its two projectors split the algebra into two canonical summands. The star is used in the closures, where it is the involution of the anti-Hermitian space, and its conjugate-linearity is what makes that split a split of real spaces and not of complex ones.

**The complex structure.** $i$ is used twice: it is what the first closure adjoins, and it is what the idempotent $\tilde\Pi_+$ contains. No carrier is defined by means of it, and the weights are real numbers throughout.

**The norm.** The norm is used three times. It identifies the rotor as an invertible element, $\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}=e_t$. It gives the pure part its positive definite form, which is what makes $SO(\mathfrak{k})$ a group of rotations. And its polar form $\beta$ is the invariant form of *Three and No More*, where it does the work that the trace form does in a treatment by arrays. The spectra, the spin and the sign of the full turn use the product, the star and the commutator only.

**No array.** No argument array is used, and no basis is fixed. The two identities $\vec u_{\mathrm r}\tilde\Pi_+=-i\tilde\Pi_+$ and $[\tfrac12\vec u_{\mathrm r},\vec v]=\vec u_{\mathrm r}\times\vec v$ carry every computation, and the spectra are read from the scalar action on the plane and from the exhibited eigenvectors on the vector part. A display in a fixed frame would have introduced the axis into statements that do not contain one.

**What is read from an element.** Only the scalar part and the vector part are used, read off the coefficients. No pairing of the algebra with itself is needed for the spectra, and no invariant of a linear operator is taken; the spectra are read from the action of the axis and from eigenvectors that are written out. The one pairing used in this article is the polar form $\beta$ of the norm, and it is used once, in *Three and No More*.

**Regularity.** No decomposition into regular and degenerate parts is assumed. The idempotent is degenerate by construction, since $\tilde\Pi_+\ne e_t$, and the plane is built from it. The construction therefore does not assume that the algebra is a division algebra: $\mathbb{B}$ is not one, and the existence of a nontrivial idempotent is exactly the failure.

**The classification.** The statement that there are three carriers and no more is proved in *Three and No More*, from the polar form of the norm and from the compactness of the group of invertibles. It is not quoted, and the proof writes no array.

## The Closure of a Carrier

A carrier carries a spin $s$. The closure places it in a subspace of $\mathbb{B}$. A carrier is a module, the question asks for subspaces, and the two are not the same object: the passage from one to the other is a step of its own. The step is a **closure**: to a carrier, attach a real subspace of $\mathbb{B}$ in which it sits and on which the action is defined.

**Definition (closure).** Let $W$ be a carrier with representation space $V_W$. A **closure** of $W$ is a real subspace $\overline{W}\subseteq\mathbb{B}$ that contains $V_W$, is invariant under the action of $W$, and is the smallest subspace of $\mathbb{B}$ with a further property, named by the rule of the case.

The definition is deliberately incomplete, and the incompleteness is the content of this section. The further property is not the same in the four cases, and the four rules below are not one rule applied four times.

**The four properties.** For the line the property is being a complex subspace, since the line is real and the algebra has an $i$ to spend. For the plane no further property is needed: invariance under the whole group is the property, and it is the plane that fails to have it, not the definition. For the spinor space the property is containing both members of the Peirce pair. For the vector part the property is being the whole eigenspace of the conjugation.

The plane needs two steps and the other two need one.

The closures are read in the order of the spins: the spin $0$ line closes to the centre; the spin $\tfrac12$ plane closes to the spinor space and then, in a second step, to the bispinor space; the spin $1$ vector part closes to the anti-Hermitian space. Four rules, four properties, four subspaces.

| carrier | $\dim_\mathbb{R}$ | closure | $\dim_\mathbb{R}$ | property the rule adds |
| --- | --- | --- | --- | --- |
| fixed line | $1$ | centre $\mathbb{C}e_t$ | $2$ | being a complex subspace |
| spinor plane | $2$ | spinor space $S_+\cong\mathbb{C}^2$ | $4$ | none: invariance under the whole group |
| spinor space | $4$ | a bispinor space, one per Peirce basis | $8$ | containing both members of the pair |
| vector part | $3$ | anti-Hermitian space $\mathbb{B}_\Phi$ | $4$ | being the whole eigenspace of the conjugation |

### The Centre

**The space.** $\mathbb{C}e_t=\mathbb{R}e_t\oplus\mathbb{R}(ie_t)$, of real dimension $2$.

**Why it is the closure of the line.** The line is fixed pointwise by the conjugation, and the fixed space of the conjugation is exactly the centre: $uXu^{*}=X$ for every invertible $u$ holds only for the central elements. The line is real and the property named for it is being complex, so the closure takes the smallest complex subspace containing it, which is $\mathbb{C}e_t$: the line together with $ie_t$. That the result is the whole fixed space, and not merely a complex line through $e_t$, is a theorem about the conjugation and not a part of the rule.

**The carrier inside.** Every element of the centre is fixed, so the space carries the trivial carrier with multiplicity two: the lines $\mathbb{R}e_t$ and $\mathbb{R}(ie_t)$ are two copies of it, and they are the real and imaginary parts of one complex line. The spin is $s=0$.

### The Bispinor Spaces

**The first step, and why it is forced.** No real subspace of $\mathbb{B}$ of dimension $2$ is invariant under the whole rotation group. The plane $\Sigma$ is invariant under the rotations about its axis and under no others, and the smallest real subspace containing it and invariant under all of them has dimension $4$, which is $S_+=\mathbb{B}\tilde\Pi_+$.

*Proof.* The plane is the complex line $\mathbb{C}\tilde\Pi_+$. For an element $X$ whose product $X\tilde\Pi_+$ is not a complex multiple of $\tilde\Pi_+$, the space $L_X\Sigma$ is not contained in $\Sigma$, and the transverse axis $\vec u_2$ is such an element. The real span of $\Sigma$ and $L_{\vec u_2}\Sigma$ is $S_+$, of real dimension $4$, and $S_+$ is closed under every $L_X$ and under $L_{iX}$. Hence the smallest invariant real subspace containing the plane is $S_+$.

So the first closure is not a convenience, and it is not a matter of supplying $i$ either: the plane is a complex line already, and multiplication by $i$ acts inside it. What the plane lacks is the transverse direction. The image of the plane under left multiplication by the transverse axis, $L_{\vec u_2}\Sigma$, is a second complex line, and the real span of the two is $S_+$. The step is a step inside the ideal, from one complex line to two, and it adds two real dimensions.

**The spinor space.** $S_+=\mathbb{B}\tilde\Pi_+=\mathbb{C}\{\tilde\Pi_+,\vec u_2\tilde\Pi_+\}$, of real dimension $4$ and complex dimension $2$. It is a minimal left ideal: no nonzero left subspace of it is invariant. It carries the spinor carrier, with weights $\pm\tfrac12$ and $s=\tfrac12$.

**The second step.** The complementary idempotent $\tilde\Pi_-(\vec u_{\mathrm r})=\tfrac12(e_t-i\vec u_{\mathrm r})=e_t-\tilde\Pi_+$ gives a second ideal $S_-=\mathbb{B}\tilde\Pi_-$, also of real dimension $4$, and

$$
\mathbb{B}=S_+\oplus S_-,\qquad 4+4=8 .
$$

The two idempotents satisfy $\tilde\Pi_\pm^2=\tilde\Pi_\pm$ and $\tilde\Pi_+\tilde\Pi_-=0$, so they form a **Peirce basis** and the sum is direct. Each axis therefore produces a **bispinor space**: the algebra $\mathbb{B}$ read through the Peirce basis of that axis, that is, the pair of spinor spaces and their sum.

**The four corners.** Each summand splits further. The four Peirce corners $\tilde\Pi_\epsilon\mathbb{B}\tilde\Pi_\delta$ with $\epsilon,\delta\in\{+,-\}$ have real dimension $2$ each, and the two spinor spaces are their grouping two by two.

**The family, and why the plural.** There is one bispinor space per Peirce basis, so there are infinitely many: one for each unit real axis, and two axes that differ by a sign give the same unordered pair, so the family is indexed by the real projective plane. For two distinct axes the spinor spaces differ, since each contains its own idempotent. The sum does not move, $\mathbb{B}\tilde\Pi_+\oplus\mathbb{B}\tilde\Pi_-=\mathbb{B}$ for every axis.

As sets the members of this family coincide, because each of them is $\mathbb{B}$. What varies is the splitting. The family is therefore a family of decompositions of one space and not a family of subspaces of it, and the naming keeps that apart: the spinor spaces are subspaces, and a bispinor space is the whole space together with a Peirce basis. A subspace is a subset, a bispinor space is a subset and a splitting, and the count of the first is two per axis while the count of the second is one per axis.

**The two idempotents and the two conjugations.** The idempotents are exchanged by the natural conjugation, $\tilde\Pi_+^{\natural}=\tilde\Pi_-$, and each is fixed by the star, since $(i\vec u_{\mathrm r})^{*}=i\vec u_{\mathrm r}$ at a real axis. The two **ideals** are exchanged by neither, and indeed they cannot be: each is a left ideal, and the natural conjugation carries a left ideal to a right ideal.

### The Anti-Hermitian Space

**The space.** $\mathbb{B}_\Phi=\{X\in\mathbb{B}:X^{*}=-X\}=\mathbb{R}(ie_t)\oplus\mathfrak{k}$, of real dimension $4$. This is the half the corpus calls the **material part** of an element, the other half $\mathbb{B}_\Psi=\mathbb{R}e_t\oplus i\mathfrak{k}$ being the informational part. It is a real subspace and not a complex one: multiplication by $i$ carries it to $\mathbb{B}_\Psi$.

**Why it is the closure of the vector part.** The property named for the vector part is being the whole eigenspace of the conjugation. The star is an involution, so it splits the algebra into its $+1$ and $-1$ eigenspaces, of real dimensions $4+4$. The vector part lies in the $-1$ eigenspace and is not the whole of it: multiplication by $i$ carries the vector part to a Hermitian space, so the $-1$ eigenspace needs a real line as well, and that line is $\mathbb{R}(ie_t)$. The closure takes the whole eigenspace, which is $\mathbb{B}_\Phi$. Read with the commutator, $\mathbb{B}_\Phi$ is a real Lie algebra, and the display is a split of Lie algebras,

$$
\mathbb{B}_\Phi=\mathfrak{u}(2)=\mathfrak{u}(1)\oplus\mathfrak{su}(2),
$$

with $\mathfrak{k}$ the second summand and $\mathbb{R}(ie_t)$ the centre; it is the Lie algebra of the group $G$ that acts.

**The carrier inside.** $\mathfrak{k}$, of real dimension $3$, with weights $\{\pm1,0\}$ and $s=1$. The line $\mathbb{R}(ie_t)$ is not a second carrier: it is the degenerate summand, fixed by the action, and it is the same carrier as the line of the centre.

**Remark (why this half and not the other).** The Hermitian half $\mathbb{B}_\Psi=\mathbb{R}e_t\oplus i\mathfrak{k}$ is also invariant and also of real dimension $4$, and it too splits as a line and a three-dimensional summand. The two halves carry the same module, since $X\mapsto iX$ is a real-linear isomorphism carrying one onto the other and commuting with every conjugation. What separates them is read off the involution identity

$$
(XY)^{*}=Y^{*}X^{*},
$$

which needs no axis. On $\mathbb{B}_\Phi$ every element is anti-Hermitian, so $X^{*}=-X$ and $Y^{*}=-Y$ give $(XY)^{*}=YX$ and $(YX)^{*}=XY$, hence $[X,Y]^{*}=-[X,Y]$: the bracket of two elements of the half is again in the half.

$$
[\mathbb{B}_\Phi,\mathbb{B}_\Phi]\subseteq\mathbb{B}_\Phi .
$$

On $\mathbb{B}_\Psi$ every element is Hermitian, so $X^{*}=X$ and $Y^{*}=Y$ give $(XY)^{*}=YX$ as well, and the bracket of two elements is anti-Hermitian. But the two halves meet only at the origin, $\mathbb{B}_\Phi\cap\mathbb{B}_\Psi=\{0\}$, and the bracket is not identically zero on the half: $\mathfrak{k}$ is non-abelian, $[\vec v,\vec w]\neq0$ for some pair, and $i\mathfrak{k}$ lies in $\mathbb{B}_\Psi$. So for a suitable pair the bracket of two elements of $\mathbb{B}_\Psi$ is a nonzero element of $\mathfrak{k}$, which $\mathbb{B}_\Psi$ does not contain.

$$
[\mathbb{B}_\Psi,\mathbb{B}_\Psi]\subseteq\mathbb{B}_\Phi,\qquad [\mathbb{B}_\Psi,\mathbb{B}_\Psi]\not\subseteq\mathbb{B}_\Psi .
$$

The same identity shows that the anticommutator runs the other way, $\{X,Y\}^{*}=YX+XY=\{X,Y\}$ for two elements of $\mathbb{B}_\Psi$, so that half is closed under the symmetrisation and not under the bracket. Both closure statements are computations in the involution, and neither refers to a basis: the vector part lies in $\mathbb{B}_\Phi$, which is closed, and that is the half the table names.

**Remark (the bracket alone does not name it).** Being closed under the commutator is necessary and not sufficient. Of the four halves $\mathbb{B}_\Psi$, $\mathbb{B}_\Phi$, $\mathbb{B}_H=\mathbb{R}e_t\oplus\mathfrak{k}$ and $\mathbb{B}_{iH}$, exactly two are closed under the bracket: $\mathbb{B}_\Phi$ and $\mathbb{B}_H$. The reason is that the bracket of two elements of any half is anti-Hermitian and scalar-free, so it lands in $\mathfrak{k}$, which lies in both. What singles out $\mathbb{B}_\Phi$ is the two facts together, containing the carrier and being closed under the bracket. A third test completes the picture: of the four halves only $\mathbb{B}_H$ is closed under the algebra product, and as an algebra it is the real quaternions, a division algebra. So the two halves that carry a bracket are distinguished by the product, and $\mathbb{B}_\Phi$ is the one that carries a bracket and not a product.

**Remark (the naming is a convention with a warrant).** The table names one half for the carrier, and no number depends on the choice. If the other half were named, the types, the weights $\{0,\pm1\}$ and the spin would all be unchanged; what would change is the algebra structure that comes with the name, since one half is closed under the bracket and the other is not. The warrant for $\mathbb{B}_\Phi$ is that it contains the carrier and is a Lie algebra under the bracket, which is the structure the action itself uses.

### The Spaces Together

**What the closures add.** The centre adds the complex structure to a line. The first closure of the plane adds the transverse direction, which is the second complex line of the ideal; the second adds the second idempotent. The anti-Hermitian space adds the fixed line to the vector part. Four rules, each with its own property, and no two of them the same.

**The dimensions.** The carriers are $1,2,3$; the spaces are $2$, $4$, $8$, and $4$ for the vector part. The two lists are not proportional and no rule turns one into the other: the line doubles, the plane is squared and then doubled, the vector part gains one.

**They are not a decomposition.** One of the four is a bispinor space, and as a set it is the whole algebra; the sum of the four space dimensions is $2+4+8+4=18$, which is not $8$. The sum counts the same algebra several times over. The four spaces are four readings of one algebra, one for each action and one for the second step of the plane, and the decompositions of the algebra itself are three and of three different kinds: the Clebsch–Gordan split $V_1\oplus V_0$ of the complex algebra, the split $\mathbb{B}_\Phi\oplus\mathbb{B}_\Psi$ of the real algebra by the star, and the split $S_+\oplus S_-$ into left ideals by a Peirce basis. None of the four closure spaces is one of these pieces either.

**The overlaps.** The four spaces are not disjoint, and two inclusions say how they meet. The centre and the anti-Hermitian space intersect in the line $\mathbb{R}(ie_t)$. The spinor space lies inside the bispinor space, as one of its two summands. Nothing else overlaps: the plane meets $S_-$ only at the origin, and the vector part meets $\mathbb{B}_\Psi$ only at the origin.

**The order of the steps.** The rotation acts; the action has three carriers; each carrier closes into a space. The first step is a question about the group, the second about the modules, the third about the subspaces. A statement about a carrier and a statement about its closure are different statements, and the two are kept apart by the naming: the line and the centre, the plane and the spinor space, the vector part and the anti-Hermitian space.

## Discussion

**The four steps.** The article proceeds in four steps, and the order is the whole point. *The Clebsch–Gordan Decomposition* comes first: the algebra is the square of one slot, the series turns that square into two summands, and the two projectors built from the natural conjugation place them as the centre and the vector part, with the labels $0$ and $1$ read at the general axis. *The Slot* then identifies the label of the factor, $\tfrac12$, from the Casimir of the left-regular generators, and *The Product* reads the labels $0$ and $1$ a second time, on the tensor square and from the total Casimir. In *The Carriers* each label is read as a real subspace of $\mathbb{B}$ of dimension $2s+1$, the dimension and the action forcing the assignment, and the one-sided carrier is the slot realized by a minimal left ideal. In *The Closure of a Carrier* each carrier is placed in a subspace of $\mathbb{B}$ by a rule named for that carrier. *Three and No More* proves, without the series, that the list is complete, and *The Quadratic Element* reads the same three values $s(s+1)$ from one central element of the algebra.

**What is established.** The decomposition $\mathbb{B}\cong V_1\oplus V_0$, with the two projectors and their equivariance; three carriers of real dimensions $1$, $2$, $3$; the actions trivial, by left multiplication, and by conjugation; the weights $\{0\}$, $\{\pm\tfrac12\}$ and $\{\pm1,0\}$ obtained from the two identities without any array; the spins $0,\tfrac12,1$; the identity $2s+1=\dim_\mathbb{R}$ checked in the three cases and covering every carrier, because the list is complete and the completeness is proved; the full-turn sign $(-1)^{2s}$, with the $-1$ visible as a half turn of the plane; the quadratic element, whose values on the three carriers are $s(s+1)$; and the closures — the centre, the spinor and bispinor spaces, and the anti-Hermitian space.

**What it means.** The three numbers $1,2,3$ are the real dimensions of three carriers, and the label $s$ is the largest weight of each, so the identity that relates them relates two counts of the same nature. Two of the three labels come from the series and one from the factor that the series squares: the algebra decomposes, and the slot does not. The closure then places each carrier in the algebra, at the cost of one complex structure, one transverse direction, one second idempotent, and one fixed line.

**Limitations.** The article studies the conjugation by the invertibles with $uu^{*}=e_t$. It does not study the conjugation by the general invertible elements, which does not preserve the pure part. It does not study products of carriers, or the bracket as a structure. And it states the closure of the three carriers only.

**Two questions left open.** The first is whether the completeness of the list can be proved without classifying the two actions one at a time, that is, whether the series alone can be shown to exhaust the carriers of the algebra; the quadratic element is a second reading of the three numbers and not such a proof. The second is whether the bispinor family has a canonical member, that is, whether the axis can be fixed by a condition internal to the algebra; on the three carriers the axis is a free parameter, and nothing in the algebra singles one out.

## Appendix

### A.1 Conventions

| symbol | meaning |
| --- | --- |
| $\mathbb{B}$ | the biquaternion algebra, a real algebra of dimension $8$, with $i$ an element |
| $\vec u_2,\vec u_3$ | an oriented orthonormal pair with $\vec u_{\mathrm r}\times\vec u_2=\vec u_3$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis of the quaternion layer, with $e_t$ the identity |
| $\tilde Q=Q_te_t+\vec Q$ | an element, with scalar part $Q_t$ and vector part $\vec Q$ |
| ${}^{\natural}$, ${}^{*}$ | the natural conjugation and the star |
| $\mathfrak{k}$ | the real span of the pure part, dimension $3$ |
| $P_0=\tfrac12(\mathrm{id}+\natural)$, $P_1=\tfrac12(\mathrm{id}-\natural)$ | the two Clebsch–Gordan projectors |
| $V_j$ | the carrier of label $j$, of complex dimension $2j+1$ |
| $\mathbb{B}_C$ | the centre $\mathbb{C}e_t$, dimension $2$ over $\mathbb{R}$ |
| $\mathbb{B}_\Psi$, $\mathbb{B}_\Phi$ | the Hermitian and anti-Hermitian halves |
| $G=\mathrm U(2)$ | the unitary elements, $uu^{*}=e_t$ |
| $Sp(1)$ | the rotors, the unit sphere of the quaternion layer |
| $\vec u_{\mathrm r}$ | a unit real axis |
| $\theta_{\mathrm{axr}}$ | the rotation angle, twice the angle of the rotor |
| $\tilde u_{\mathrm r}$ | the rotor of the axis and the angle |
| $A(\vec u_{\mathrm r})=\tfrac12\vec u_{\mathrm r}$ | the generator along the axis, an element of $\mathfrak{k}$ |
| $\tilde S(\vec u_{\mathrm r})=iA$ | the Hermitian element of the corpus |
| $\beta$ | the polar form of the norm, invariant and non-degenerate |
| $C=\sum_k\tilde S_k^{2}$ | the quadratic element, equal to $\tfrac34e_t$ |
| $\tilde\Pi_\pm(\vec u_{\mathrm r})=\tfrac12(e_t\pm i\vec u_{\mathrm r})$ | the two idempotents of the axis, a Peirce basis |
| $\Sigma=\mathbb{C}\tilde\Pi_+$ | the spinor plane, dimension $2$ over $\mathbb{R}$ |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the spinor spaces, dimension $4$ over $\mathbb{R}$ |
| $\varrho$ | a representation of the action on a carrier |
| $\lambda$, $s$ | a weight, and the spin, the largest weight |

### A.2 The Operator Identities

**Proposition (the elementary identities).** For elements $X,Y$ and an invertible element $u$:

1. $L_XL_Y=L_{XY}$ and $R_XR_Y=R_{YX}$.
2. $\operatorname{ad}_X=L_X-R_X$.
3. $\operatorname{Ad}_u=L_uR_{u^{*}}$ for $uu^{*}=e_t$, and there $R_{u^{*}}=R_{u^{-1}}$.
4. $\operatorname{Ad}_{uv}=\operatorname{Ad}_u\operatorname{Ad}_v$ and $\operatorname{Ad}_{e_t}=\mathrm{id}$.
5. $\varrho(\operatorname{Ad}_uX)=\varrho(u)\varrho(X)\varrho(u)^{-1}$ for the spinor action and for the adjoint action.
6. $\varrho(\exp X)=\exp\varrho(X)$.
7. $\operatorname{Ad}_{\exp X}=\exp(\operatorname{ad}_X)$.

*Proof.* Items 1 and 2 are the associativity of the product and the definition of the bracket. Item 3 is $uYu^{*}=(uY)u^{*}$. Item 4 is associativity again. Item 5: for the spinor action, $L_{uXu^{*}}=L_uL_XL_{u^{*}}$ by item 1 and $L_{u^{*}}=L_u^{-1}$; for the adjoint action, $\operatorname{ad}_{uXu^{*}}=\operatorname{Ad}_u\operatorname{ad}_X\operatorname{Ad}_u^{-1}$, checked by applying both sides to $Y$ and using item 4. Item 6 is the exponential series, whose terms are the powers of the operator. Item 7 is item 6 applied to the adjoint action, whose derived map is the commutator.

**Corollary (the exponential form).** For the rotor $\tilde u_{\mathrm r}$ and the generator $A=A(\vec u_{\mathrm r})$,

$$
\varrho(\tilde u_{\mathrm r})=\exp\bigl(\theta_{\mathrm{axr}}\varrho(A)\bigr)
$$

for both the spinor and the adjoint action.

*Proof.* By item 6 it suffices to compute the derived map on $\vec u_{\mathrm r}$, which is $\varrho(\vec u_{\mathrm r})=2\varrho(A)$, and to replace the exponent $\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}$ accordingly.

**Corollary (the eigenvalues of a rotor).** The eigenvalues of $\varrho(\tilde u_{\mathrm r})$ are $e^{i\theta_{\mathrm{axr}}\lambda}$, where $\lambda$ runs over the weights.

### A.3 The Three Computations

Everything below uses the two identities of *The Rotation Action*, at a general unit real axis $\vec u_{\mathrm r}$, and one oriented orthonormal pair $\vec u_2,\vec u_3$ with $\vec u_{\mathrm r}\times\vec u_2=\vec u_3$ and $\vec u_2\times\vec u_3=\vec u_{\mathrm r}$. No array is written and no coordinate is used.

**The line.** $\varrho(A)=0$ on $\mathbb{R}e_t$, so the spectrum is $\{0\}$.

**The plane.** By the first identity, $\vec u_{\mathrm r}\tilde\Pi_+(\vec u_{\mathrm r})=-i\tilde\Pi_+(\vec u_{\mathrm r})$ and therefore

$$
L_{A(\vec u_{\mathrm r})}\tilde\Pi_+(\vec u_{\mathrm r})=\tfrac12\vec u_{\mathrm r}\tilde\Pi_+(\vec u_{\mathrm r})=-\tfrac i2\,\tilde\Pi_+(\vec u_{\mathrm r}),
\qquad
L_{A(\vec u_{\mathrm r})}\bigl(i\tilde\Pi_+(\vec u_{\mathrm r})\bigr)=-\tfrac i2\,i\tilde\Pi_+(\vec u_{\mathrm r}).
$$

So the operator is the complex scalar $-\tfrac i2$ on the whole plane, and on the two real dimensions its eigenvalues are the scalar and its conjugate, $-\tfrac i2$ and $+\tfrac i2$. The weights are $\pm\tfrac12$. The half angle follows in the same line: multiplying by the rotor gives the phase $e^{-i\theta_{\mathrm{axr}}/2}$, whose exponent at $\theta_{\mathrm{axr}}=2\pi$ is $-i\pi$.

**The vector part.** By the second identity, $\varrho_{\mathrm{ad}}(A(\vec u_{\mathrm r}))(\vec v)=\vec u_{\mathrm r}\times\vec v$. The cross product with a unit vector is the zero on the axis and a quarter turn on its orthogonal plane, so

$$
[\tfrac12\vec u_{\mathrm r},\vec u_2+i\vec u_3]=-i\,(\vec u_2+i\vec u_3),
\qquad
[\tfrac12\vec u_{\mathrm r},\vec u_2-i\vec u_3]=+i\,(\vec u_2-i\vec u_3),
\qquad
[\tfrac12\vec u_{\mathrm r},\vec u_{\mathrm r}]=0 .
$$

The eigenvalues are $-i,+i,0$ on the complexification of $\mathfrak{k}$, so the weights are $\pm1,0$.

**The full turns.** Exponentiating the three operators at $\theta_{\mathrm{axr}}=2\pi$: on the line, $\varrho(2\pi A)=e_t$ acts as $+1$; on the plane, the phase is $e^{-i\pi}=-1$, so the operator is $-\mathrm{id}$ on the two real dimensions, a half turn; on the vector part, $\exp(2\pi\,\vec u_{\mathrm r}\times)$ is the identity, because the cross product is a quarter turn and four quarter turns are a full turn.

**The invariance of the plane.** For a rotor $\tilde u_{\mathrm r}$ of the same axis, the product $\tilde u_{\mathrm r}\tilde\Pi_+(\vec u_{\mathrm r})=e^{-i\theta_{\mathrm{axr}}/2}\tilde\Pi_+(\vec u_{\mathrm r})$ is a complex multiple of the idempotent, so the plane is preserved. For the transverse axis it is not: $\vec u_2\tilde\Pi_+(\vec u_{\mathrm r})$ is not a complex multiple of $\tilde\Pi_+(\vec u_{\mathrm r})$, since it has a component in the direction $\vec u_3\tilde\Pi_+$, and the two together span $S_+$.

### A.4 The Correction on the Conjugation

Two two-sided maps occur, and they differ. The **inner automorphism** is $\operatorname{Ad}_u(Y)=uYu^{-1}$, defined for every invertible element. The **conjugation with the star** is $\Psi_u(Y)=uYu^{*}$, defined for every element. They agree exactly on $G$:

$$
\Psi_u=\operatorname{Ad}_u\iff u^{*}=u^{-1}\iff uu^{*}=e_t .
$$

**Proposition (when the star conjugation is multiplicative).** Let $u$ be invertible. Then $\Psi_u$ is multiplicative exactly when $u^{*}u$ is central, in which case $u^{*}u=\mu e_t$ for a nonzero complex $\mu$ and $\Psi_u=\mu\operatorname{Ad}_u$.

*Proof.* Compute $\Psi_u(X)\Psi_u(Y)=uX(u^{*}u)Yu^{*}$. If $u^{*}u=\mu e_t$ the middle factor is the scalar $\mu$, and the product is $\Psi_u(XY)$. If $u^{*}u$ is not central there is $Y$ with $[u^{*}u,Y]\ne0$, and then $\Psi_u(X)\Psi_u(Y)-\Psi_u(XY)=X[u^{*}u,Y]\ne0$ for $X=e_t$.

**Remark (invertible is not enough).** The hypothesis $N(u)\ne0$ does not imply $uu^{*}=e_t$. The central $u=2e_t$ has $N(u)=4$ and $\Psi_{2e_t}(Y)=4Y$: the product of two images is $16XY$, while the image of the product is $4XY$, so $\Psi_{2e_t}$ is not multiplicative. The same element is a perfectly good inner automorphism, since $\operatorname{Ad}_{2e_t}=\mathrm{id}$; the failure is in the star.

**Remark (a non-central invertible element does not preserve the pure part).** Write $u=\alpha e_t+\beta\vec u_{\mathrm r}$ at a unit real axis, with complex $\alpha,\beta$. Then $N(u)=\alpha^2+\beta^2$ and

$$
\operatorname{Ad}_u(\vec u_{\mathrm r})=\bigl(|\alpha|^2+|\beta|^2\bigr)\vec u_{\mathrm r}+\bigl(\alpha\bar\beta-\bar\alpha\beta\bigr)e_t .
$$

The scalar term is $2i\operatorname{Im}(\alpha\bar\beta)$, and it vanishes exactly when $\alpha\bar\beta$ is real, that is, when $uu^{*}$ is central. The element $u=2e_t+i\vec u_{\mathrm r}$ has $N(u)=3$, so it is invertible, and it sends $\vec u_{\mathrm r}$ to $5\vec u_{\mathrm r}-4ie_t$, which is not in $\mathfrak{k}$. Every statement about $\operatorname{Ad}_u$ in this article is made for $u\in G$, and that is the hypothesis which makes the conjugation preserve $\mathfrak{k}$ and the form.

## Further Reading

- [The Clebsch–Gordan Decomposition of the Biquaternion Algebra](the-clebsch-gordan-decomposition-of-the-biquaternion-algebra.html), for the series, the two projectors, the Casimir as the projector and the coefficients
- [Introduction to the Spin-Zero Centre Subspace](the-spin-zero-centre-subspace.html), for the line and the centre taken on their own, with the proof that the fixed space is exactly the centre and that no other complex line is invariant
- [Introduction to the Spin-Half Bispinors Spaces](the-spin-half-bispinor-spaces.html), for the plane, the two spinor spaces and the infinite family of bispinor spaces
- [Introduction to the Spin-One Anti-Hermitian Subspace](the-spin-one-anti-hermitian-subspace.html), for the vector part, the cross product operator and the split $\mathfrak{u}(2)=\mathfrak{u}(1)\oplus\mathfrak{su}(2)$
- [The Minimal Left Ideals of the Biquaternion Algebra](the-minimal-left-ideals-of-the-biquaternion-algebra.html), for the idempotents, the minimality and the splitting of the algebra
- [The Peirce Basis of the Biquaternion Algebra](the-peirce-basis-of-the-biquaternion-algebra.html), for the basis, the gauge and the system of Peirce units
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the four corners and the diagonal part
- [The Regular Module in the Biquaternion Algebra](the-regular-module-in-the-biquaternion-algebra.html), for the algebra read as a module over itself
- [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html), for the centre, the pure part and the two Hermitian halves
- [Representations of Groups](representations-of-groups.html), for complete reducibility by averaging, which is what compactness of the group of invertibles supplies
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), for the rotor, the two-to-one cover and the comparison of the two two-sided actions
- [Operator and Calculus Conventions](operator-and-calculus-conventions.html), for the glyphs $L_X$, $R_X$, $\operatorname{Ad}_u$ and $\operatorname{ad}_X$
- [Matrix Representations Conventions](matrix-representations-conventions.html), for the rule that no array is written in a symbol, and the basis-free form of an operator
- [Why AXF Matrices instead of Pauli and Gamma Matrices](../articles_physics/the-axf-matrices-axis-free-integer-entries.html#why-the-pauli-and-the-gamma-displays-are-refused), for the axis carried by an array and the axis-free display that does not carry one
