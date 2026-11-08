# __Spinors and Dirac Spinors in the Biquaternion Algebra__

## Introduction

The biquaternion algebra carries two objects that the literature calls a spinor, and the difference between them is a factor of two in dimension and one algebraic datum. An **elementary spinor** is an element of a complex two-dimensional space on which the left multiplications act irreducibly, with weights $+\tfrac12$ and $-\tfrac12$, so that a rotation through $\theta$ about $\vec u$ multiplies it by $e^{-i\theta\vec u\cdot\vec S}$. A **Dirac spinor** is an element $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$ of the biquaternion algebra $\mathbb{B}$ whose two parts are its two components in the decomposition of $\mathbb{B}$ into minimal left ideals; each part is an elementary spinor of complex dimension two.

This article fixes both definitions, proves what they imply, and separates them from the three pictures that stand in their place in the older literature: the column of a matrix model, the gamma matrices, and a second rotation triple attached to the conjugate part. Three results carry the content. A vector carrier has the weights $0$ and $\pm1$, a spinor carrier has $\pm\tfrac12$, and the parity of the weights is what separates them. The two parts of a Dirac spinor are not two independent carriers but two copies of one, because in adapted bases the same left multiplication has the same matrix on both. And no left multiplication carries one part into the other, so the operator that couples them multiplies on the right.

The article is the spinor counterpart of *Angular Momentum and Spin in the Biquaternion Algebra*: that article defines the spin of a carrier as a maximal weight and classifies the carriers; this one takes the two spinor carriers it produces and names them. The algebra, the units, the two-sided operator and the conjugation are those of *Algebra and Element Conventions*. The two definitions use none of a Clifford relation, a gamma basis operator, a Pauli array, a volume element or a Peirce basis; the Pauli arrays appear twice, in worked instances, and never as a definition.

## The Side of a Multiplication

The two families of operators are the left and the right multiplications,

$$
L_a\tilde{Ξ}=a\tilde{Ξ},\qquad R_b\tilde{Ξ}=\tilde{Ξ}b .
$$

They commute, $L_aR_b=R_bL_a$, because the product is associative: both sides are $a\psi b$. That one line is the engine of everything below, and its consequence is a rule about subspaces.

**Proposition (left ideals are stable, right ideals are not).** If $J\subseteq\mathbb{B}$ is a left ideal then $L_aJ\subseteq J$ for every $a$; if $J$ is a left ideal and $b\ne0$ then $R_bJ$ need not be contained in $J$.

*Proof.* $L_aJ=aJ\subseteq J$ by the definition of a left ideal. For the second statement take $J=\mathbb{B}\tilde\Pi_+$, the first column of the matrix model, and $b=i\vec e_x$; the product of a first-column matrix with $\sigma_1$ is a second-column matrix, so the image leaves $J$. The computation is carried out below.

The asymmetry is the reason the definitions are possible. A left multiplication never leaves the part it acts on; a right multiplication can. So a decomposition into left ideals is stable under the operators of the equation, which act on the left, and is moved only by an operator written on the other side. That is the content of **operator chirality** in this algebra (*Operator Chirality on the Biquaternion Algebra*): the side on which an operator multiplies, and not the sign of a generator.

## The Elementary Spinor

**Definition (elementary spinor).** An **elementary spinor** is an element of a complex two-dimensional space on which the left multiplications act irreducibly with weights $+\tfrac12$ and $-\tfrac12$, so that a rotation through $\theta$ about $\vec u$ multiplies it by $e^{-i\theta\vec u\cdot\vec S}$.

Three things are packed into that sentence, and each is a theorem below: what the carrier is, that the weights are exactly $\pm\tfrac12$, and that the rotation is a left multiplication with the half-angle. The vector $\vec u$ stands also for the pure quaternion $u_x\vec e_x+u_y\vec e_y+u_z\vec e_z$, as it does throughout the corpus, so that $i\vec u$ is an element of the algebra.

**Proposition (the carrier is a minimal left ideal).** A complex two-dimensional subspace of $\mathbb{B}$ on which the left multiplications act irreducibly is a minimal left ideal, and the minimal left ideals are

$$
S_\pm(\vec u)=\mathbb{B}\tilde\Pi_\pm(\vec u),\qquad \tilde\Pi_\pm(\vec u)=\tfrac12\bigl(e_t\pm i\vec u\bigr),
$$

for a unit real vector $\vec u$.

*Proof.* The irreducible modules of $M_2(\mathbb{C})$ are its minimal left ideals, which are the columns of a matrix model; the map $\vec u\mapsto S_+(\vec u)$ is a bijection from the unit sphere onto them (*Angular Momentum and Spin in the Biquaternion Algebra*, §*The Left Module: Spin One Half*). A two-dimensional left-invariant subspace is therefore one of these, and each has dimension two over $\mathbb{C}$.

So an elementary spinor is an element of $S_+(\vec u)$ or of $S_-(\vec u)$ for some axis $\vec u$, and the axis is what names the carrier. Every axis gives the same module up to isomorphism, so an elementary spinor without a named axis means an element of some one of the carriers, and no statement about it depends on which.

**Proposition (the weights).** On $S_+(\vec u)$ the operator $\vec u\cdot\vec S$ has the two eigenvalues $+\tfrac12$ and $-\tfrac12$, each once, and the same holds on $S_-(\vec u)$.

*Proof.* The generator is $\tilde S_k=\tfrac12 i\vec e_k$, so $\vec u\cdot\vec S=\tfrac12 i\vec u$, and

$$
\bigl(\tfrac12 i\vec u\bigr)\tilde\Pi_+(\vec u)=\tfrac12\tilde\Pi_+(\vec u),\qquad
\bigl(\tfrac12 i\vec u\bigr)\tilde\Pi_-(\vec u)=-\tfrac12\tilde\Pi_-(\vec u),
$$

the first because $(i\vec u)^2=+e_t$ and $i\vec u$ commutes with $\tilde\Pi_+(\vec u)$, the second by the same computation with $\vec u$ replaced by $-\vec u$. The weight $-\tfrac12$ vector of $S_+(\vec u)$ is the companion corner $\tilde\Pi_-(\vec u)\,\mathbb{B}\,\tilde\Pi_+(\vec u)$. It is one-dimensional; every $\nu$ in it satisfies $\nu=\tilde\Pi_-(\vec u)\nu$, so $\tfrac12 i\vec u\,\nu=-\tfrac12\nu$; and it is square-zero, because $\nu=\nu\tilde\Pi_+(\vec u)$ together with $\tilde\Pi_+(\vec u)\tilde\Pi_-(\vec u)=0$ gives $\nu^2=\nu\tilde\Pi_+(\vec u)\tilde\Pi_-(\vec u)\nu=0$. For $\vec u=\vec e_z$ it is $\vec\Upsilon_{-+}=\tfrac12(i\vec e_x+\vec e_y)$. Two independent weight vectors exhaust a two-dimensional carrier, so each weight occurs once.

**Corollary (the dimension is forced).** The spin of the carrier is $\tfrac12$, the Casimir is $\tfrac34$, and the dimension is $2s+1=2$.

*Proof.* The spin is the maximal weight of $\vec u\cdot\vec S$ by the definition of *Angular Momentum and Spin in the Biquaternion Algebra*, §*The Casimir and the Definition of Spin*, and that maximum is $\tfrac12$; the Casimir value and the dimension are the theorem of the same article.

**The rotation is a multiplication with the half-angle.** The rotation through $\theta$ about $\vec u$ is the exponential of the generator,

$$
\exp\bigl(-i\theta\,\vec u\cdot\vec S\bigr)
=\exp\bigl(\tfrac{\theta}{2}\,\vec u\bigr)
=\cos\tfrac{\theta}{2}\,e_t+\sin\tfrac{\theta}{2}\,\vec u ,
$$

and the elementary spinor is multiplied by that element on the left. The multiplier is a unit quaternion, so it acts on a vector by the adjoint action, turning it through a full angle, while on the spinor it acts by left multiplication with the eigenvalues $e^{\mp i\theta/2}$, the half-angle. The exponential is the corpus's own (*Angular Momentum and Spin in the Biquaternion Algebra*, §*The Rotation Generators*), and the sense of the turn follows from it. The adjoint action of $\cos\tfrac{\theta}{2}+\vec u\sin\tfrac{\theta}{2}$ turns a vector through $+\theta$ about $\vec u$ (*Quaternion Rotations and Reflections*, §*The Adjoint Action*), and that is the multiplier above at $\theta=\theta$: the spinor and the vector turn through the same angle and in the same sense, and the half-angle appears only in the eigenvalues of the multiplier. At $\theta=2\pi$ the multiplier is $-e_t$ and the spinor returns with the opposite sign; at $\theta=4\pi$ it returns unchanged. That is the double cover, and no vector carries it: a vector is returned to itself by a full turn, while a spinor is returned to its negative (*Angular Momentum and Spin in the Biquaternion Algebra*, §*The Rotation Generators*).

**Coordinates.** In the carrier $S_+(\vec u)$ an element is $d_0\tilde\Pi_+(\vec u)+d_1\nu(\vec u)$ with $d_0,d_1\in\mathbb{C}$ and $\nu$ the companion nilpotent, so an elementary spinor is a pair of complex numbers, a coordinate vector $(d_0;d_1)$ on the carrier. The number is two because the spin is $\tfrac12$; it is not a free choice of the model.

## The Dirac Spinor

**Definition (Dirac spinor).** A **Dirac spinor** is an element $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$ of $\mathbb{B}$, the two parts being its two components in the decomposition of $\mathbb{B}$ into minimal left ideals,

$$
\mathbb{B}=S_+(\vec u)\oplus S_-(\vec u),\qquad \tilde\Pi_\pm(\vec u)=\tfrac12\bigl(e_t\pm i\vec u\bigr),
$$

for a declared unit imaginary direction $\vec u$, and each part is an elementary spinor of complex dimension two.

**Proposition (the two parts are the two carriers, and they exhaust the algebra).** Each summand is a minimal left ideal of complex dimension two, the sum is direct, and $2+2=4=\dim_\mathbb{C}\mathbb{B}$. With the axis declared, every element of the algebra is a Dirac spinor, and only the zero element has both parts zero.

*Proof.* $\tilde\Pi_+(\vec u)$ and $\tilde\Pi_-(\vec u)$ are idempotent, orthogonal and sum to $e_t$; so $\mathbb{B}\tilde\Pi_+(\vec u)+\mathbb{B}\tilde\Pi_-(\vec u)=\mathbb{B}$ and the intersection is zero. Each summand is two-dimensional by the counting of the preceding section. The last statement is the definition of a direct sum.

**Remark (the four coordinates).** In the units $e_t,\vec e_x,\vec e_y,\vec e_z$ a Dirac spinor is four complex numbers, and in the frame of the two carriers it is two pairs, one pair per part. The count $4=2\times2$ is the product of the spin dimension and the number of parts, and the two factors have different origins: the first is the weight string $\pm\tfrac12$, the second is the number of lines in the decomposition.

**Remark (the names of the parts).** The two labels $L$ and $R$ are a convention and carry no invariant content. Exchanging them is the substitution $\vec u\mapsto-\vec u$, because

$$
\tilde\Pi_+(\vec u)=\tfrac12\bigl(e_t+i\vec u\bigr)=\tfrac12\bigl(e_t-i(-\vec u)\bigr)=\tilde\Pi_-(-\vec u).
$$

So the pair is unordered, and the definition orders it only to give the two parts names. A statement that treats the two parts differently is a statement about the declared axis and not about the algebra.

**Example (the axis $\vec u=\vec e_z$).** In the matrix model $\mathsf{M}_2$ of *Algebra and Element Conventions*, $\mathsf{M}_2(i\vec e_k)=\sigma_k$, so $\tilde\Pi_+(\vec e_z)$ is the array $\operatorname{diag}(1,0)$ and $\tilde\Pi_-(\vec e_z)$ the array $\operatorname{diag}(0,1)$. The two parts are therefore the two columns of the matrix model: the first part is the first column, the second part the second column. A Dirac spinor is a $2\times2$ array read as two columns, which is what a four-component column says in a basis that nobody had to choose.

## The Pair Is a Multiplicity

The definition says that the algebra is the sum of the two carriers. It does not yet say how they are related, and the answer is that they are the same carrier twice.

**Proposition (the same matrix on both parts).** Let $\vec v$ be a unit real vector perpendicular to $\vec u$. Right multiplication by $i\vec v$ maps $S_+(\vec u)$ onto $S_-(\vec u)$ bijectively and is left-linear. Consequently, in the bases $(\nu_1,\nu_2)$ of $S_+(\vec u)$ and $(\nu_1i\vec v,\nu_2i\vec v)$ of $S_-(\vec u)$, every left multiplication $L_a$ has the same matrix on the two parts.

*Proof.* Left-linearity: $R_{i\vec v}(ax)=ax(i\vec v)=a\,R_{i\vec v}(x)$. The image of $\mathbb{B}\tilde\Pi_+(\vec u)$ is $\mathbb{B}\bigl(\tilde\Pi_+(\vec u)i\vec v\bigr)$, which is a left ideal generated by a nonzero element, hence minimal, and a computation in the matrix model identifies it as $S_-(\vec u)$. With $\vec u=\vec e_z$ and $\vec v=\vec e_x$ the generator is $\operatorname{diag}(1,0)\sigma_1=E_{12}$, which generates the second column. Bijectivity follows from the dimensions. For the matrices, $L_aR_{i\vec v}=R_{i\vec v}L_a$, so $L_a$ applied to the transported basis equals the transport of $L_a$ applied to the original basis, and the two matrices agree.

**Corollary (the multiplicity two).** As a left module $\mathbb{B}\cong S\oplus S$ with $S$ the simple module, so the left multiplication acts on one factor and the decomposition into the two parts is a multiplicity, not a direct sum of two different representations. The Dirac spinor is a carrier of spin $\tfrac12$ with multiplicity two, and the second factor is what the labels $L$ and $R$ index.

Two consequences follow. The four coordinates of a Dirac spinor are not four independent numbers acted on by a four-dimensional irreducible representation of the algebra: this left action is two-dimensional and repeats. And the second factor carries no new representation of the algebra: it is a copy, and the index that separates the two parts is a copy index (*The Pauli Module of the Biquaternion Algebra*).

**Remark (the two readings of the pair).** Everything above is the left action on the two left ideals. The physics of the corpus reads the same two subspaces a second way: on the Dirac module $\Delta=S\oplus S^{\mathrm{c}}$ the second factor is the conjugate module, on which $Q$ acts as $\bar Q$, so a scalar $\lambda$ multiplies one part by $\lambda$ and the other by $\bar\lambda$ (*The Unpolarized Module of the Biquaternion Algebra*; *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*). The subspaces are the same in both readings, because coefficient conjugation carries $S_+(\vec u)$ onto $S_-(\vec u)$; what differs is the action declared on the second. A statement about the two parts therefore has to name its reading, and the two names are the same pair of ideals with the copy action and with the conjugate action.

**The grading and the projector.** Right multiplication by $\tilde\Pi_+(\vec u)$ is the projection onto $S_+(\vec u)$ along $S_-(\vec u)$: it is idempotent, of trace two, the identity on the first part and zero on the second, because $\tilde\Pi_+^2=\tilde\Pi_+$ and $\tilde\Pi_-\tilde\Pi_+=0$. The grading behind it is a right multiplier, $R(i\vec u)$, which has the eigenvalue $+1$ on $S_+(\vec u)$ and $-1$ on $S_-(\vec u)$; so the two parts diagonalise it, and

$$
R\bigl(\tilde\Pi_+(\vec u)\bigr)=\tfrac12\bigl(\mathrm{id}+R(i\vec u)\bigr),\qquad
R\bigl(\tilde\Pi_-(\vec u)\bigr)=\tfrac12\bigl(\mathrm{id}-R(i\vec u)\bigr).
$$

That grading is the object the corpus calls the chirality operator of a frame: in the axis-free frame the basis operator is the right multiplier $-iR_{\vec e_z}$ (*Operator Chirality on the Biquaternion Algebra*, *The Pauli Module of the Biquaternion Algebra*), which is the negative of $R(i\vec u)$ at $\vec u=\vec e_z$, and a grading agrees with its negative on the two parts and differs only in which part carries which sign. The idempotent form is used here because the idempotent is what defines the carrier, and it names no frame. What the basis operator does not give is invariant data of the pair: the two parts are two copies, the index that separates them is a copy index, and the sign attaches to the declared axis (*The Polarized Module of the Biquaternion Algebra*).

## What Carries One Part to the Other

The two parts are stable under every left multiplication, and only a right one moves them. The exact statement is the following, and it is the algebraic content of the mass term of the Dirac equation.

**Proposition (no left multiplication exchanges the parts).** For every $a\in\mathbb{B}$, $L_a\,S_+(\vec u)\subseteq S_+(\vec u)$ and $L_a\,S_-(\vec u)\subseteq S_-(\vec u)$.

*Proof.* $S_\pm(\vec u)$ are left ideals, and a left multiplication preserves a left ideal by the definition.

**Proposition (what a right multiplier does to the axis).** Let $\vec v=\cos\theta\,\vec u+\sin\theta\,\vec n$ with $\vec n$ a unit real vector perpendicular to $\vec u$. Then right multiplication by $i\vec v$ carries $S_+(\vec u)$ onto $S_+(\vec w)$ with

$$
\vec w=\cos2\theta\,\vec u+\sin2\theta\,\vec n,
$$

so it preserves the part at $\theta=0$, exchanges the two parts at $\theta=\tfrac{\pi}{2}$, where $\vec w=-\vec u$ and $S_+(-\vec u)=S_-(\vec u)$, and otherwise carries it to a carrier at a different axis, which is a third carrier beside the two at $\vec u$. The same holds with $S_+$ replaced by $S_-$.

*Proof.* Put $q=\tilde\Pi_+(\vec u)i\vec v$, which is nonzero and of rank one, so $\mathbb{B}q$ is a minimal left ideal; it equals $S_+(\vec w)$ exactly when $q\in S_+(\vec w)$, because one minimal left ideal that meets another is that other. A carrier has the description

$$
S_+(\vec w)=\bigl\{x\in\mathbb{B}: x\,i\vec w=x\bigr\},
$$

the $+1$ eigenspace of $R(i\vec w)$, which in the matrix model is the set of arrays whose rows lie in the $+1$ eigenline of $\vec w\cdot\vec\sigma$. Take $\vec u=\vec e_z$ and $\vec n=\vec e_x$; then

$$
\mathsf{M}_2(q)=\mathsf{M}_2\bigl(\tfrac12(i\vec v-\vec e_z\vec v)\bigr)
=\tfrac12\bigl(\cos\theta\,(I_2+\sigma_3)+\sin\theta\,(\sigma_1+i\sigma_2)\bigr)
=\begin{pmatrix}\cos\theta & \sin\theta\\ 0 & 0\end{pmatrix},
$$

whose rows lie in the line at angle $\theta$ from the first coordinate axis. The $+1$ eigenline of $\vec w\cdot\vec\sigma$ is the spinor line at half the angle of $\vec w$, so the line at angle $\theta$ belongs to $\vec w$ at angle $2\theta$, that is $\vec w=\cos2\theta\,\vec e_z+\sin2\theta\,\vec e_x$; the identity $q\,i\vec w=q$ confirms it, and with it $q\in S_+(\vec w)$. The general pair $(\vec u,\vec n)$ is carried to this frame by a left multiplication with a unit, which maps carriers onto carriers and conjugates a right multiplier into a right multiplier. The special values follow by substitution, and $S_+(-\vec u)=S_-(\vec u)$ because $\tilde\Pi_+(-\vec u)=\tilde\Pi_-(\vec u)$.

**Proposition (the exchange is unique up to a scalar).** Let $\vec v$ and $\vec v'$ be unit real vectors perpendicular to $\vec u$. Then $R(i\vec v)$ and $R(i\vec v')$ agree on the whole of $S_+(\vec u)$ up to one nonzero complex scalar, and the same holds on $S_-(\vec u)$. Consequently the space of left-linear maps from one part to the other is a complex line.

*Proof.* A left-linear map $\varphi:S_+(\vec u)\to S_-(\vec u)$ satisfies $\varphi(a\tilde\Pi_+)=a\varphi(\tilde\Pi_+)$, so it is determined by the single vector $\varphi(\tilde\Pi_+)$, and the consistency condition $a\tilde\Pi_+=0\Rightarrow a\varphi(\tilde\Pi_+)=0$ selects the line $\tilde\Pi_+S_-(\vec u)=\tilde\Pi_+(\vec u)\mathbb{B}\tilde\Pi_-(\vec u)$, of complex dimension one. For the multipliers: $q=\tilde\Pi_+(\vec u)i\vec v$ is nonzero, because $i\vec v$ has purely imaginary coefficients and $\vec u\vec v$ has real ones, and for $\vec v\perp\vec u$ the element $q$ generates $S_-(\vec u)$ by the proposition on the axis, so $q$ lies in the corner and is not zero. Each $R(i\vec v)$ therefore realises the nonzero element of the line, and two of them differ by a nonzero scalar.

**Remark (the mass is one complex number).** The mass of the biquaternionic Dirac equation acts on the right: it carries the field from one value to the other, and it is neither a central scalar nor a left multiplication. The two propositions above say what it can be. It is a right multiplication, the multiplier must be perpendicular to the declared axis, and there is only one such map up to a scalar; so the mass is a complex number times a fixed exchange, and no perpendicular direction is a second datum. The terms that act on the left stay in their part. The two-sided form of the equation, in which one factor acts from the left and the mass from the right, is therefore not a rewriting: it is the only side on which the mass can act.

**Example (the exchange at $\vec u=\vec e_z$).** With $\vec v=\vec e_x$ the multiplier is $i\vec e_x$, whose matrix is $\sigma_1$, and the exchange acts on the two columns by

$$
E_{11}\,\sigma_1=E_{12},\qquad E_{21}\,\sigma_1=E_{22},
$$

so it sends the first column onto the second coordinate by coordinate. The multiplier $i\vec e_z$ instead keeps each column in place, which is the case $\vec v=\pm\vec u$ of the second proposition.

## What the Definitions Do Not Use

The definition of an elementary spinor names the axis that selects its carrier, and the definition of a Dirac spinor names one axis and nothing else. The two definitions use none of: a Clifford relation, a gamma basis operator, a Pauli array, a volume element, a Peirce basis, a second rotation triple. Three claims of the older literature are replaced, and each replacement is a statement of the same fact with fewer objects.

**The four-component column.** A column of four components is a Dirac spinor written in a chosen frame, namely the frame of the two carriers read as two columns. The definition does not need the frame: the element exists before the columns do, and the columns are its coordinates in the decomposition.

**The two-component spinor.** A column of two components is an elementary spinor written in a chosen carrier. The carrier is a minimal left ideal, and the ideal is selected by an axis; the column is the coordinate form of an element of that ideal.

**The second triple.** No second rotation triple is needed to distinguish the two parts, and none can do it. A triple of left multiplications acts inside each part; by the first proposition of the preceding section it cannot move between them. What distinguishes the parts is the side of the multiplication, and the side is a datum of the operator, not of a generator. In particular the two parts carry the same operator with the same weights, and a statement that gives them opposite signs is a statement about a different algebraic object.

**What the definitions cost.** One declared direction $\vec u$ between them, and it is the only datum they cost. The direction is a point of the sphere; it selects the two carriers and the decomposition, and a change of it changes nothing else: the dimension, the weights, the spin, the multiplicity and the exchange are the same at every axis. The price of splitting an algebra into two parts is one frame, named where it is used.

## Summary

An elementary spinor is an element of a complex two-dimensional carrier on which the left multiplications act irreducibly with weights $\pm\tfrac12$. In $\mathbb{B}$ the carriers are the minimal left ideals $S_\pm(\vec u)=\mathbb{B}\tilde\Pi_\pm(\vec u)$, the weight string is $(+\tfrac12,-\tfrac12)$, the spin is $\tfrac12$ and the dimension is $2=2s+1$. A rotation through $\theta$ about $\vec u$ multiplies the spinor by $\cos\tfrac{\theta}{2}e_t+\sin\tfrac{\theta}{2}\vec u$, so the multiplier carries the half-angle and a full turn returns the element with the opposite sign.

A Dirac spinor is an element of $\mathbb{B}$ whose two parts are its two components in the decomposition of $\mathbb{B}$ into the minimal left ideals at a declared axis, and each part is an elementary spinor. The parts are the two columns of the matrix model at $\vec u=\vec e_z$, the algebra is their direct sum, and the four coordinates are two pairs.

The pair is a multiplicity. Right multiplication by $i\vec v$ with $\vec v\perp\vec u$ carries one part onto the other and is left-linear, so in adapted bases every left multiplication has the same matrix on both parts. The decomposition is therefore one carrier taken twice, not two carriers.

No left multiplication moves between the parts, so the coupling of the parts is a right multiplication. The multipliers that do it are the imaginary units, and the axis of the image doubles the angle: a perpendicular unit exchanges the two parts, a parallel unit preserves them, and anything between carries the carrier to a third one. All perpendicular units give the same map up to a nonzero scalar, so the space of such maps is a complex line and the mass is one complex number times a fixed exchange. The two names cost one declared direction between them, and no Clifford relation, no gamma basis operator and no second triple.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | The biquaternion algebra, $M_2(\mathbb{C})$, complex dimension four |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | The units, $e_t^2=e_t$ and $\vec e_k^2=-e_t$ |
| $L_a\tilde{Ξ}=a\tilde{Ξ}$, $R_b\tilde{Ξ}=\tilde{Ξ}b$ | Left and right multiplication; they commute |
| $\tilde S_k=\tfrac12 i\vec e_k$ | The spin generators, Hermitian, with eigenvalues $\pm\tfrac12$ on a carrier |
| $\vec S$ | The same generators read as one vector, $\vec u\cdot\vec S=u_k\tilde S_k$; pure, so arrowed and without the tilde |
| $\vec u$ | A unit real vector, the declared direction |
| $\tilde\Pi_\pm(\vec u)=\tfrac12(e_t\pm i\vec u)$ | The rank-one idempotents at the axis; $\tilde\Pi_+\tilde\Pi_-=0$ and $\tilde\Pi_++\tilde\Pi_-=e_t$ |
| $S_\pm(\vec u)=\mathbb{B}\tilde\Pi_\pm(\vec u)$ | The minimal left ideals at the axis, $\mathbb{B}=S_+\oplus S_-$ |
| $(d_0;d_1)$ | The coordinates of an elementary spinor on its carrier |
| $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$ | A Dirac spinor, one part in each carrier |
| $R(i\vec u)$ | The grading of the two parts, $+1$ on $S_+(\vec u)$ and $-1$ on $S_-(\vec u)$; $\tfrac12(\mathrm{id}+R(i\vec u))$ is the projector $R(\tilde\Pi_+(\vec u))$ |
| $S^{\mathrm{c}}$ | The conjugate module, on which $Q$ acts as $\bar Q$ |
| $\mathsf{M}_2$, $\sigma_k$ | The matrix model, $\mathsf{M}_2(e_t)=I_2$ and $\mathsf{M}_2(i\vec e_k)=\sigma_k$, with $\sigma_k$ the Pauli matrices |
| $s=\tfrac12$, $2s+1=2$ | The spin of the carrier and its dimension |
| $\vec\Upsilon_{-+}=\tfrac12(i\vec e_x+\vec e_y)$ | The nilpotent weight $-\tfrac12$ vector of $S_+(\vec e_z)$ |
| $R(i\vec v)$, $\vec v\perp\vec u$ | The left-linear exchange of the two parts; unique up to a nonzero scalar |

## Further Reading

- [Angular Momentum and Spin in the Biquaternion Algebra](angular-momentum-and-spin-in-the-biquaternion-algebra.html), for the definition of spin as a maximal weight, the Casimir, the sphere of minimal left ideals, the double cover and the four uses of the word spin.
- [Operator Chirality on the Biquaternion Algebra](operator-chirality-on-the-biquaternion-algebra.html), for the side of a multiplication as the chirality, and for the swap.
- [The Polarized Module of the Biquaternion Algebra](the-polarized-module-of-the-biquaternion-algebra.html), for the decomposition $V\cong S\oplus S$ of the carrier and the two spinor spaces.
- [The Pauli Module of the Biquaternion Algebra](the-pauli-module-of-the-biquaternion-algebra.html), for the two slots as two copies of one module and for the chirality operator whose eigenspaces they are.
- [The Unpolarized Module of the Biquaternion Algebra](the-unpolarized-module-of-the-biquaternion-algebra.html), for the Dirac module $S\oplus S^{\mathrm{c}}$, the conjugate action on the second factor, and the no-go theorem on the basis operator.
- [Quaternion Rotations and Reflections](quaternion-rotations-and-reflections.html), for the rotation through $\theta$ about $u$ as the adjoint action of $\cos\tfrac{\theta}{2}+u\sin\tfrac{\theta}{2}$, which fixes the sign used above.
- [Spinors as Peirce Coordinates](spinors-as-peirce-coordinates.html), for the coordinate vector on a Peirce carrier and the weight condition that makes it a spinor.
- [Spinors as Coordinates in $M_4(\mathbb{C})$](spinors-as-coordinates-in-m4c.html), for the same construction at $n=4$, the $2+2$ chiral split and the higher spin.
- [The Dirac Equation in Biquaternionic Form](../articles_physics/the-dirac-equation-in-biquaternionic-form.html), for the chiral pair and the mass term that the last section reads.
- [Peirce Coordinates and Companion Nilpotents](peirce-coordinates-and-companion-nilpotents.html), for the coordinate theory of a carrier and its nilpotent companion.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition and the corner algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the classical construction of the spinor spaces and its comparison with the algebraic one.
