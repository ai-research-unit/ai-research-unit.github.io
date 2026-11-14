# __The Carriers, the Representation, the Spin and the Closure__

## Introduction

The question of this article is fixed, and so is its answer.

**The question.** How do spatial rotations act on the biquaternion algebra — what are its rotation-invariant pieces and one-sided ideals?

**The answer.** A line of real dimension $1$ with the trivial action and spin $0$; a plane of real dimension $2$ with the spinor action and spin $\tfrac12$; and the vector part of real dimension $3$ with the adjoint action and spin $1$. The dimensions are $1,2,3$, and the spin is $s$ with $2s+1=\dim_\mathbb{R}$.

The whole article is written over the reals, and this is not a matter of taste. A spatial rotation acts on a real space; a subspace that a rotation leaves alone is a real subspace; and the question asks for those subspaces. Over the reals the three dimensions are $1,2,3$, the three spins are $0,\tfrac12,1$, and the identity $2s+1=\dim$ compares two counts of the same nature. Over the complex numbers the three dimensions would be $1,2,3$ again, but the identity would compare a complex dimension with a weight count, which is weaker.

The complex structure $i$ is an element of the algebra here and not a scalar of the ground field. It is one of the operators, on the same footing as $\vec e_x,\vec e_y,\vec e_z$, and the fact that it is available is what the closure steps use.

*Preliminaries* fixes the real algebra. *The Rotation Action* fixes the action and the generator. *The Carriers* and *The Spin Table* contain the answer, with the three carriers read off the action itself. *What the Construction Uses and Does Not Use* records the limits. *The Closure of a Carrier* is the last step: a carrier is a module, and the question asks for subspaces, so each carrier is closed into a subspace — the centre, the spinor and bispinor spaces, and the anti-Hermitian space. The appendix holds the computations.

Three things are not claimed. The article does not derive the trichotomy: that there are exactly three carriers is *The Carriers of the Biquaternion Algebra*, and it is quoted here. It does not read the label as anything but a spectral quantity. And it does not present the closure as a decomposition: the three closures are not the pieces of one splitting of the algebra.

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

The **star** is the natural conjugation followed by the conjugation of $i$, and it is the Hermitian conjugation of the algebra:

$$
(Q_te_t+\vec Q)^{*}=\bar Q_te_t-\bar{\vec Q},\qquad (XY)^{*}=Y^{*}X^{*}.
$$

An element is **Hermitian** when $X^{*}=X$ and **anti-Hermitian** when $X^{*}=-X$.

**The norm and the units.** The **norm** is

$$
N(\tilde Q)=Q_t^2+Q_x^2+Q_y^2+Q_z^2,
$$

multiplicative, and vanishing exactly on the elements without an inverse. An element is **invertible** when $N(\tilde Q)\ne0$. An element is a **unit** when $XX^{*}=e_t$; the units form the group $G=\mathrm U(2)$, of real dimension $4$. Every unit is invertible, since $X^{-1}=X^{*}$; the converse fails, and $2e_t$ is invertible without being a unit.

**The rotor.** A **unit real axis** is a real pure element $\vec u_{\mathrm r}$ with $(\vec u_{\mathrm r},\vec u_{\mathrm r})=1$ for the positive definite form on $\mathfrak{k}$. For a real angle $\theta_{\mathrm{axr}}$ the **rotor** is

$$
\tilde u_{\mathrm r}=\cos\frac{\theta_{\mathrm{axr}}}{2}\,e_t+\sin\frac{\theta_{\mathrm{axr}}}{2}\,\vec u_{\mathrm r},
$$

with real coefficients and $\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}=e_t$. The rotors form $Sp(1)$, the unit sphere of the quaternion layer, of real dimension $3$.

**The operators.** For an element $X$ the four operators used below are

$$
L_X(Y)=XY,\qquad R_X(Y)=YX,\qquad \operatorname{ad}_X(Y)=XY-YX,\qquad \operatorname{Ad}_u(Y)=uYu^{*},
$$

the last one for $uu^{*}=e_t$. The first two are left and right multiplication, the third is the commutator, the fourth is the conjugation by a unit.

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

**Definition (carrier).** A **carrier** is a nonzero real subspace of $\mathbb{B}$ that is invariant and irreducible under one of these actions. The action is part of the carrier, because the same subspace can be reducible for one action and irreducible for another. The three carriers are computed in *The Carriers*, and the list is complete: there are three and no more.

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

the largest weight, with $s=0$ for the spectrum $\{0\}$. The definition is well posed by the two lemmas: the weights are real, so the maximum exists, and they do not depend on the axis, so the number depends on the carrier and not on a choice. It agrees with the definition by dimension of *The Spin of a Carrier*: on an irreducible carrier the weights are $s,s-1,\dots,-s$, so there are $2s+1$ of them.

## The Carriers

The three carriers are stated in the order line, plane, vector part: the two rotation-invariant pieces first, the one-sided one after. Each is described by the same template: the subspace, the action, the operator, the spectrum, the dimension, the spin, and the sign of a full turn.

### The Fixed Line

**The subspace.** The real line $\mathbb{R}e_t$, of real dimension $1$.

**The action.** The conjugation acts trivially, because $ue_tu^{*}=e_t$ for every unit $u$. The line is fixed pointwise, and it is the carrier of the trivial action.

**The operator.** $\varrho(A)=0$.

**The spectrum.** $\{0\}$, with multiplicity $1$.

**Dimension, spin, full turn.** $\dim_\mathbb{R}=1$, $s=0$, and $2s+1=1$. The full turn has operator $\varrho(-e_t)=\mathrm{id}$, so the sign is $+1$.

### The Spinor Plane

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

**The subspace.** $\mathfrak{k}=\mathbb{R}\vec e_x\oplus\mathbb{R}\vec e_y\oplus\mathbb{R}\vec e_z$, of real dimension $3$.

**The action.** The conjugation, $\varrho_{\mathrm{ad}}(u)=\operatorname{Ad}_u$. It preserves $\mathfrak{k}$ and it preserves the form, so it is a representation into $SO(\mathfrak{k})$; the map is onto with kernel $\{\pm e_t\}$.

**The operator.** By the second identity the operator is the cross product with the axis,

$$
\varrho_{\mathrm{ad}}\bigl(A(\vec u_{\mathrm r})\bigr)(\vec v)=\vec u_{\mathrm r}\times\vec v ,
$$

which is the zero of $\vec u_{\mathrm r}$ and a quarter turn of the plane perpendicular to it. With the oriented pair $\vec u_2,\vec u_3$ completing the axis as before, it sends $\vec u_2\pm i\vec u_3$ to $\mp i(\vec u_2\pm i\vec u_3)$, so the eigenvalues are $-i$, $+i$ and $0$.

**The spectrum.** $\{+1,0,-1\}$, with multiplicities $1,1,1$.

**Dimension, spin, full turn.** $\dim_\mathbb{R}=3$, $s=1$, and $2s+1=3$. The full turn is a rotation of space through $2\pi$, which is the identity on $\mathfrak{k}$, so the sign is $+1$.

**Remark (why the two spectra differ by a factor of two).** The generator is the same real element $\tfrac12\vec u_{\mathrm r}$ in both cases, and the two identities say why the spectra differ. On the vector part the operator is the commutator with $\tfrac12\vec u_{\mathrm r}$, which equals the cross product with the whole axis $\vec u_{\mathrm r}$: the two sides of the product both contribute, and the quarter turn of the cross product gives the eigenvalues $\mp i$, hence the weights $\pm1$. On the plane the operator is a single multiplication by one half of the axis, which gives the scalar $-\tfrac i2$, hence the weights $\pm\tfrac12$. The commutator consumes the axis twice and the multiplication consumes it once, and that is the factor of two.

### Why the Three Are Not a Direct Sum

The three carriers are not the pieces of one decomposition, and the arithmetic says so at once: $1+2+3=6$, while $\mathbb{B}$ has real dimension $8$.

Two decompositions of the algebra exist, in two different categories.

From the star, $\mathbb{B}=\mathbb{B}_\Phi\oplus\mathbb{B}_\Psi$, the anti-Hermitian and Hermitian halves, of real dimensions $4+4=8$; the first contains the vector part.

From the idempotent, $\mathbb{B}=S_+\oplus S_-$ as left modules, where $S_\pm=\mathbb{B}\tilde\Pi_\pm$, and each summand has real dimension $4$.

The spinor plane occurs in neither as a summand: it is a complex line inside $S_+$, and not a left module over the whole algebra. The line, the plane and the vector part are three carriers, not three summands.

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

## What the Construction Uses and Does Not Use

**The axis.** The axis is a parameter. The spectrum does not depend on it, by the lemma of *The Rotation Action*, and the spin therefore does not depend on it. The answer is a property of the carrier and not of a direction.

**The angle.** The spin is read from the generator at the identity, so no angle enters it. The angle enters once, at $\theta_{\mathrm{axr}}=2\pi$, in the theorem of the full turn. The halved angle of the rotor is not used to define the weights; it is the reason the exponent in the full turn is $2\pi\lambda$.

**The complex structure.** $i$ is used twice: it is what the first closure adjoins, and it is what the idempotent $\tilde\Pi_+$ contains. No carrier is defined by means of it, and the weights are real numbers throughout.

**The norm.** The norm is used twice. It identifies the rotor as a unit, $\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}=e_t$, and it gives the pure part its positive definite form, which is what makes $SO(\mathfrak{k})$ a group of rotations. The spectra, the spin and the sign of the full turn use the product, the star and the commutator only.

**No array.** No argument array is used, and no basis is fixed. The two identities $\vec u_{\mathrm r}\tilde\Pi_+=-i\tilde\Pi_+$ and $[\tfrac12\vec u_{\mathrm r},\vec v]=\vec u_{\mathrm r}\times\vec v$ carry every computation, and the spectra are read from the scalar action on the plane and from the exhibited eigenvectors on the vector part. A display in a fixed frame would have introduced the axis into statements that do not contain one.

**What is read from an element.** Only the scalar part and the vector part are used, read off the coefficients. No pairing of the algebra with itself is needed, and no invariant of a linear operator is taken; the spectra are read from the action of the axis and from eigenvectors that are written out.

**Regularity.** No decomposition into regular and degenerate parts is assumed. The idempotent is degenerate by construction, since $\tilde\Pi_+\ne e_t$, and the plane is built from it. The construction therefore does not assume that the algebra is a division algebra: $\mathbb{B}$ is not one, and the existence of a nontrivial idempotent is exactly the failure.

**The classification.** The statement that there are three carriers and no more is quoted from *The Carriers of the Biquaternion Algebra* and is not reproved.

## The Closure of a Carrier

A carrier is a module; the question asks for subspaces. The two are not the same object, and the passage from one to the other is a step of its own. The step is a **closure**: to a carrier, attach a real subspace of $\mathbb{B}$ in which it sits and on which the action is defined.

**Definition (closure).** Let $W$ be a carrier with representation space $V_W$. A **closure** of $W$ is a real subspace $\overline{W}\subseteq\mathbb{B}$ that contains $V_W$, is invariant under the action of $W$, and is the smallest subspace of $\mathbb{B}$ with a further property, named by the rule of the case.

The definition is deliberately incomplete, and the incompleteness is the content of this section. The further property is not the same in the four cases, and the four rules below are not one rule applied four times.

**The four properties.** For the line the property is being a complex subspace, since the line is real and the algebra has an $i$ to spend. For the plane no further property is needed: invariance under the whole group is the property, and it is the plane that fails to have it, not the definition. For the spinor space the property is containing both members of the Peirce pair. For the vector part the property is being the whole eigenspace of the conjugation.

The plane needs two steps and the other two need one.

| carrier | $\dim_\mathbb{R}$ | closure | $\dim_\mathbb{R}$ | property the rule adds |
| --- | --- | --- | --- | --- |
| fixed line | $1$ | centre $\mathbb{C}e_t$ | $2$ | being a complex subspace |
| spinor plane | $2$ | spinor space $S_+\cong\mathbb{C}^2$ | $4$ | none: invariance under the whole group |
| spinor space | $4$ | a bispinor space, one per Peirce basis | $8$ | containing both members of the pair |
| vector part | $3$ | anti-Hermitian space $\mathbb{B}_\Phi$ | $4$ | being the whole eigenspace of the conjugation |

### The Centre

**The space.** $\mathbb{C}e_t=\mathbb{R}e_t\oplus\mathbb{R}(ie_t)$, of real dimension $2$.

**Why it is the closure of the line.** The line is fixed pointwise by the conjugation, and the fixed space of the conjugation is exactly the centre: $uXu^{*}=X$ for every unit $u$ holds only for the central elements. The line is real and the property named for it is being complex, so the closure takes the smallest complex subspace containing it, which is $\mathbb{C}e_t$: the line together with $ie_t$. That the result is the whole fixed space, and not merely a complex line through $e_t$, is a theorem about the conjugation and not a part of the rule.

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

**Remark (why this half and not the other).** The Hermitian half $\mathbb{B}_\Psi=\mathbb{R}e_t\oplus i\mathfrak{k}$ is also invariant and also of real dimension $4$, and it too splits as a line and a three-dimensional summand. Two facts separate them. The vector part lies in $\mathbb{B}_\Phi$ and meets $\mathbb{B}_\Psi$ only at the origin. And $\mathbb{B}_\Phi$ is closed under the commutator, while $\mathbb{B}_\Psi$ is not: the bracket of two Hermitian elements is anti-Hermitian and leaves it. The two halves carry the same module with $i$ inserted; the table names the half that contains the carrier.

### The Spaces Together

**What the closures add.** The centre adds the complex structure to a line. The first closure of the plane adds the transverse direction, which is the second complex line of the ideal; the second adds the second idempotent. The anti-Hermitian space adds the fixed line to the vector part. Four rules, each with its own property, and no two of them the same.

**The dimensions.** The carriers are $1,2,3$; the spaces are $2$, $4$, $8$, and $4$ for the vector part. The two lists are not proportional and no rule turns one into the other: the line doubles, the plane is squared and then doubled, the vector part gains one.

**They are not a decomposition.** One of the four is a bispinor space, and as a set it is the whole algebra; the sum of the four space dimensions is $2+4+8+4=18$, which is not $8$. The sum counts the same algebra several times over. The four spaces are four readings of one algebra, one for each action and one for the second step of the plane, and the only decompositions available are the pair stated in *The Carriers*.

**The overlaps.** The four spaces are not disjoint, and two inclusions say how they meet. The centre and the anti-Hermitian space intersect in the line $\mathbb{R}(ie_t)$. The spinor space lies inside the bispinor space, as one of its two summands. Nothing else overlaps: the plane meets $S_-$ only at the origin, and the vector part meets $\mathbb{B}_\Psi$ only at the origin.

**The order of the steps.** The rotation acts; the action has three carriers; each carrier closes into a space. The first step is a question about the group, the second about the modules, the third about the subspaces. A statement about a carrier and a statement about its closure are different statements, and the two are kept apart by the naming: the line and the centre, the plane and the spinor space, the vector part and the anti-Hermitian space.

## Discussion

**What is established.** Three carriers of real dimensions $1$, $2$, $3$; the actions trivial, by left multiplication, and by conjugation; the weights $\{0\}$, $\{\pm\tfrac12\}$ and $\{\pm1,0\}$ obtained from the two identities without any array; the spins $0,\tfrac12,1$; the identity $2s+1=\dim_\mathbb{R}$ checked in the three cases; the full-turn sign $(-1)^{2s}$, with the $-1$ visible as a half turn of the plane; and the closures — the centre, the spinor and bispinor spaces, and the anti-Hermitian space.

**What it means.** The three numbers $1,2,3$ are the real dimensions of three carriers, and the label $s$ is the largest weight of each, so the identity that relates them relates two counts of the same nature. The closure then places each carrier in the algebra, at the cost of one complex structure, one transverse direction, one second idempotent, and one fixed line.

**Limitations.** The article studies the conjugation by the units with $uu^{*}=e_t$. It does not study the conjugation by the general invertible elements, which does not preserve the pure part. It does not study products of carriers, or the bracket as a structure. And it states the closure of the three carriers only.

**Two questions left open.** The first is whether the count $2s+1$ can be proved without the classification, by an argument that does not run through the list. The second is whether the bispinor family has a canonical member, that is, whether the axis can be fixed by a condition internal to the algebra; on the three carriers the axis is a free parameter, and nothing in the algebra singles one out.

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
| $\mathbb{B}_C$ | the centre $\mathbb{C}e_t$, dimension $2$ over $\mathbb{R}$ |
| $\mathbb{B}_\Psi$, $\mathbb{B}_\Phi$ | the Hermitian and anti-Hermitian halves |
| $G=\mathrm U(2)$ | the units, $uu^{*}=e_t$ |
| $Sp(1)$ | the rotors, the unit sphere of the quaternion layer |
| $\vec u_{\mathrm r}$ | a unit real axis |
| $\theta_{\mathrm{axr}}$ | the rotation angle, twice the angle of the rotor |
| $\tilde u_{\mathrm r}$ | the rotor of the axis and the angle |
| $A(\vec u_{\mathrm r})=\tfrac12\vec u_{\mathrm r}$ | the generator along the axis, an element of $\mathfrak{k}$ |
| $\tilde S(\vec u_{\mathrm r})=iA$ | the Hermitian element of the corpus |
| $\tilde\Pi_\pm(\vec u_{\mathrm r})=\tfrac12(e_t\pm i\vec u_{\mathrm r})$ | the two idempotents of the axis, a Peirce basis |
| $\Sigma=\mathbb{C}\tilde\Pi_+$ | the spinor plane, dimension $2$ over $\mathbb{R}$ |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the spinor spaces, dimension $4$ over $\mathbb{R}$ |
| $\varrho$ | a representation of the action on a carrier |
| $\lambda$, $s$ | a weight, and the spin, the largest weight |

### A.2 The Operator Identities

**Proposition (the elementary identities).** For elements $X,Y$ and a unit $u$:

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
[\tfrac12\vec u_{\mathrm r},\vec u_{\mathrm r}]=0 .$$ The eigenvalues are $-i,+i,0$ on the complexification of $\mathfrak{k}$, so the weights are $\pm1,0$.

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

- [The Carriers of the Biquaternion Algebra](the-carriers-of-the-biquaternion-algebra.html), for the carrier, the type and the completeness of the list
- [Introduction to the Spin-Zero Centre Subspace](the-spin-zero-centre-subspace.html), for the line and the centre taken on their own, with the proof that the fixed space is exactly the centre
- [Introduction to the Spin-Half Bispinor Spaces](the-spin-half-bispinor-spaces.html), for the plane, the two spinor spaces and the infinite family of bispinor spaces
- [Introduction to the Spin-One Anti-Hermitian Subspace](the-spin-one-anti-hermitian-subspace.html), for the vector part, the cross product operator and the split $\mathfrak{u}(2)=\mathfrak{u}(1)\oplus\mathfrak{su}(2)$
- [The Weights of a Carrier](the-weights-of-a-carrier.html), for the weight, the weight string and the three spectra
- [The Spin of a Carrier](the-spin-of-a-carrier.html), for the definition of the spin by dimension and its agreement with the largest weight
- [The Minimal Left Ideals of the Biquaternion Algebra](the-minimal-left-ideals-of-the-biquaternion-algebra.html), for the idempotents, the minimality and the splitting of the algebra
- [The Peirce Basis and Norm Regularity](the-peirce-basis-and-norm-regularity.html), for the Peirce basis and the four corners
- [The Regular Module in the Biquaternion Algebra](the-regular-module.html), for the algebra read as a module over itself
- [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html), for the centre, the pure part and the two Hermitian halves
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), for the rotor, the two-to-one cover and the comparison of the two two-sided actions
- [Operator and Calculus Conventions](operator-and-calculus-conventions.html), for the glyphs $L_X$, $R_X$, $\operatorname{Ad}_u$ and $\operatorname{ad}_X$
- [Matrix Representations Conventions](matrix-representations-conventions.html), for the rule that no array is written in a symbol, and the basis-free form of an operator
- [Why AXF Matrices instead of Pauli and Gamma Matrices](../articles_physics/why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the axis carried by an array and the axis-free display that does not carry one
